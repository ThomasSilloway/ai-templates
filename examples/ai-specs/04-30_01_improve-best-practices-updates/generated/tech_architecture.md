# Technical Architecture: Git-Informed Best Practices Updater

This document outlines the technical architecture for the "improve-best-practices-updates" feature.

## 1. File Structure

This section details the proposed file structure for the new Python module responsible for analyzing Git commit history.

### `scripts/identify_coding_errors/`

This directory contains the core logic for identifying coding errors and learnings from Git history, as required by FR-001 in the PRD. The structure promotes modularity as specified in the NFRs and Design Considerations.

```
scripts/
└── identify_coding_errors/
    ├── __init__.py           # Makes the directory a Python package.
    ├── main.py               # Main entry point for the script, orchestrates the workflow, handles user interaction (e.g., commit hash prompt), and is executed by the VSCode task.
    ├── feature_finder.py     # Contains logic to scan `ai-specs/` and identify the latest feature specification folder based on naming conventions (FR-001, AC 34).
    ├── git_handler.py        # Handles all Git interactions: finding merge-base, searching for the 'First pass' commit, determining the commit range for analysis (FR-001, AC 35-39).
    └── diff_generator.py     # Responsible for iterating through the identified commit range, extracting commit messages and diffs, and generating the sequentially named `.diff` files in the target directory (FR-001, AC 40-45).
```

**File Descriptions:**

*   **`__init__.py`**: Standard Python file to mark the directory as a package, allowing for imports like `from scripts.identify_coding_errors import ...`.
*   **`main.py`**: Orchestrates the overall process. It will likely import functions from the other modules, call them in sequence (find feature folder -> handle git range -> generate diffs), manage overall error handling, and handle any necessary user interaction (like prompting for a commit hash if the "First pass" commit isn't found). This is the target for the VSCode task execution (`python -m scripts.identify_coding_errors.main`).
*   **`feature_finder.py`**: Encapsulates the logic for locating the correct feature specification directory within `ai-specs/`. This isolates the directory scanning and parsing logic.
*   **`git_handler.py`**: Contains all functions related to interacting with the Git repository. This includes finding the merge-base commit, searching commit history for specific messages, and determining the exact start and end commits for the analysis range. Uses `GitPython` or `subprocess`.
*   **`diff_generator.py`**: Focuses solely on the task of retrieving the commit message and diff for each commit in the specified range and writing this information to the correctly named `.diff` files in the `generated/git_changes/` sub-directory of the identified feature folder.

This modular structure separates concerns, making the code easier to understand, test, and maintain, fulfilling the requirements outlined in the PRD.