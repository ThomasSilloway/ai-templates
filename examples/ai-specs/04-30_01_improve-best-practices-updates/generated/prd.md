# Product Requirements Document: Git-Informed Best Practices Updater

**Version:** 1.1
**Date:** 2025-04-30

## 1. Introduction / Vision

This document outlines the requirements for an enhancement to an existing AI-assisted development workflow used within the `Godot-AI-Developer` project. The current workflow involves generating feature-specific prompts from templates and manually using these prompts with an AI agent for initial code implementation and subsequent bug fixing.

The vision is to create a more robust feedback loop where learnings from manual and semi-automated bug fixing/polishing, captured in Git commits, are automatically analyzed and used to continuously improve a central "best practices" document. This ensures the AI's knowledge base stays up-to-date with encountered issues and their resolutions, leading to fewer repeated mistakes in future AI-generated code.

## 2. Goals & Objectives

* **Goal:** Automate the extraction of coding error patterns and best practice learnings from Git commit history after a feature is completed.
* **Goal:** Improve the accuracy and relevance of the central `ai-docs/best_practices.md` file.
* **Goal:** Reduce the recurrence of specific coding mistakes (e.g., API misuse, framework hallucinations) in future AI-generated features.
* **Objective:** Develop a Python module (`identify_coding_errors`) that analyzes a specified range of Git commits (messages and diffs) for a completed feature.
* **Objective:** Modify the existing `spec-document-progress.md` prompt template to utilize the output of the commit analysis module.
* **Objective:** Ensure the process integrates smoothly with the existing manual workflow trigger points.
* **Objective:** Provide a convenient way to execute the analysis module via a VSCode task.

## 3. Target Audience / User Personas

* **Primary User:** The individual developer using the `Godot-AI-Developer` workflow for personal projects.

## 4. Functional Requirements (Features / User Stories)

**MVP (Minimum Viable Product):**

1.  **FR-001: Commit Analysis Functionality (`identify_coding_errors` module)**
    * **User Story:** As a developer, I want a tool that I can run manually when a feature branch is complete, so that it can identify and extract relevant commit information for analysis.
    * **Acceptance Criteria:**
        * The Python module resides within `/scripts/identify_coding_errors/`.
        * The tool determines the **latest feature specification folder** by scanning directories within `ai-specs/` and selecting the one with the most recent `MM-DD_NN` prefix (e.g., finds `ai-specs/04-30_01_new_feature` over `ai-specs/04-29_02_old_feature`).
        * The tool determines the feature branch's merge-base commit with `main`.
        * It searches the latest ~50 commits unique to the feature branch (since the merge-base) for the most recent commit message starting with "First pass" (case-insensitive).
        * If found, uses the commit *after* this as the start of the analysis range.
        * If not found, prompts the user interactively to provide the short commit hash for the starting commit (and uses the commit *after* this).
        * The end of the analysis range is the current `HEAD` of the feature branch.
        * For each commit within the calculated range (chronological order):
            * Extracts the full commit message.
            * Extracts the code diff.
            * Creates a file named sequentially (e.g., `01_<short_hash>.diff`, `02_<short_hash>.diff`).
            * Writes the commit message and the diff content into the corresponding file.
        * Saves these generated `.diff` files into a new sub-directory within the identified latest feature folder: **`ai-specs/<latest_feature_folder>/generated/git_changes/`**.
        * Handles potential errors gracefully (e.g., Git command failures, invalid user input, no feature folders found).

2.  **FR-002: Update Progress Documentation Prompt Template (`spec-document-progress.md`)**
    * **User Story:** As a developer, I want the AI prompt for documenting progress to use the generated Git diff files as its primary input for identifying coding mistakes and learnings, so that the analysis is based on actual changes.
    * **Acceptance Criteria:**
        * The template file `ai-specs/templates/spec-document-progress.md` is modified.
        * New task instructions are added (likely near the end).
        * These instructions clearly guide the AI agent to:
            * Locate the **`generated/git_changes`** directory within the current feature's spec folder.
            * Iterate through the `NN_<hash>.diff` files in chronological order (based on the `NN` prefix).
            * For each file, analyze the commit message (at the top) and the code diff.
            * Synthesize findings from all processed files to generate the content for the feature-specific `coding_mistakes.md` file (overwriting any previous intermediate versions).
            * Extract generalizable patterns, corrections, and best practices from the analyzed changes.
            * Update the global `ai-docs/best_practices.md` file by appending or intelligently merging these new learnings, focusing on areas like API usage, variable naming, framework specifics, error handling, and logic patterns.
        * Instructions should de-emphasize or remove reliance on any pre-existing `coding_mistakes.md` file as input for this analysis step.

3.  **FR-003: VSCode Task Definition**
    * **User Story:** As a developer, I want a pre-defined VSCode task so that I can easily run the commit analysis functionality with a single command.
    * **Acceptance Criteria:**
        * A new task definition is added to `.vscode/tasks.json`.
        * This task correctly executes the main entry point of the `identify_coding_errors` Python module (e.g., `python -m scripts.identify_coding_errors.main`).
        * The task runs successfully from the VSCode command palette or terminal task runner.

## 5. Non-Functional Requirements

* **Usability:**
    * The commit analysis tool should provide clear output regarding the identified latest feature folder, the commit range determined, and the location of the generated diff files.
    * Interactive prompts (if needed) should be clear.
* **Reliability:**
    * The tool must reliably interact with Git and handle common scenarios.
    * Must reliably identify the latest feature specification folder based on the defined naming convention.
    * Error handling prevents crashes.
* **Maintainability:**
    * The Python code for the `identify_coding_errors` functionality **must** be modular, broken into multiple files within its directory (`/scripts/identify_coding_errors/`) to separate concerns.
    * Code should be well-commented and follow standard Python best practices (PEP 8).
* **Performance:**
    * Tool execution should be reasonably fast for typical feature branches.
* **Security:**
    * Standard secure coding practices for file handling and subprocess execution (if used) should be followed.

## 6. Design Considerations / Implementation Details

* **Tool Location:** `/scripts/identify_coding_errors/`
* **Tool Modularity:** Implementation **must** be split into multiple Python files (e.g., `git_handler.py`, `diff_generator.py`, `feature_finder.py`, `main.py`).
* **Identifying Latest Feature Folder:** Implement logic to scan `ai-specs/`, parse folder names matching the `MM-DD_NN_*` pattern, sort them chronologically/numerically, and select the latest.
* **Git Interaction:** Utilize `GitPython` or `subprocess` calls with robust error handling.
* **Prompt Engineering:** Modifications to `spec-document-progress.md` require careful engineering for the AI to process the sequence of diff files effectively.
* **VSCode Task:** Define the task in `.vscode/tasks.json` using standard task properties (`label`, `type`, `command`, `problemMatcher`, etc.).

## 7. Technical Constraints & Integrations

* **Environment:** Local developer machine, within the `Godot-AI-Developer` project structure.
* **Dependencies:**
    * Python 3.x
    * Git (installed and in PATH)
    * Potentially `GitPython`
* **Existing Workflow Integration:** Manually triggered tool, output feeds into subsequent manual AI prompt step.
* **IDE Integration:** Integration with VSCode via a defined task in `.vscode/tasks.json` for easy execution.

## 8. Data Requirements

* **Input Data:** Git repository history (commit messages, diffs) for the specific feature branch.
* **Generated Data:** Sequentially named `.diff` files containing commit messages and diff content, stored in `ai-specs/<latest_feature_folder>/generated/git_changes/`.
* **Output Data (via subsequent AI step):**
    * Updated `ai-specs/<latest_feature_folder>/generated/coding_mistakes.md`
    * Updated `ai-docs/best_practices.md`

## 9. Potential Risks & Edge Cases

* **Risk:** Difficulty finding "First pass" commit. (Mitigation: Fallback).
* **Risk:** Large commit histories (>50). (Mitigation: Limit is configurable later if needed).
* **Risk:** Complex Git history (merges/rebases). (Mitigation: `git show` per commit is generally robust).
* **Risk:** AI struggles with synthesis. (Mitigation: Prompt refinement).
* **Risk:** Incorrect identification of the latest feature folder if naming conventions are broken or parsing fails. (Mitigation: Clear error reporting).
* **Edge Case:** Running on `main` or branch without merge-base. (Mitigation: Add checks).
* **Edge Case:** No commits between start and HEAD. (Mitigation: Report and exit).
* **Edge Case:** No folders matching the pattern found in `ai-specs/`. (Mitigation: Report error).
* **Edge Case:** `.vscode/tasks.json` doesn't exist or is malformed. (Mitigation: Standard JSON handling, document requirement for `.vscode` folder).

## 10. Release Criteria / Success Metrics

* **Release Criteria:**
    * Commit analysis tool successfully identifies the correct commit range and **latest feature folder**.
    * Tool correctly generates numbered `.diff` files (message + diff) in **`generated/git_changes/`**.
    * Modified `spec-document-progress.md` template exists.
    * Manual testing confirms AI agent processes diffs via modified prompt successfully.
    * Tool code is **modular** and in `/scripts/identify_coding_errors/`.
    * **A functional VSCode task exists** in `.vscode/tasks.json` that successfully runs the commit analysis functionality.
* **Success Metrics:**
    * Reduction in recurring error types (qualitative).
    * Developer perception of improved `best_practices.md`.
    * Successful end-to-end runs on multiple features.

## 11. Future Considerations / Roadmap

* **Automation:** Explore automating the trigger for the commit analysis functionality (e.g., via Git hooks on merge to `main`, though manual review might still be desired).
* **AI Integration:** Potentially integrate the AI analysis step directly into the Python module, removing the need for manual copy-pasting into an external agent (would require API access and careful handling of AI interaction).
* **Advanced Analysis:** Implement more sophisticated analysis of diffs within the Python module itself (e.g., using static analysis tools or linters) to pre-process information for the AI.
* **Configurability:** Allow configuration of the commit search limit (~50) or the "First pass" trigger phrase via a config file.
* **Error Categorization:** Enhance the prompt to categorize identified mistakes/learnings when updating `best_practices.md`.
