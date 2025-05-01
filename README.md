# AI Templates

This repository provides tools and templates to streamline AI-assisted development workflows, focusing on feature specification generation and continuous improvement of coding best practices.

## Overview

The AI Templates repository contains two main tools:

1. **Template Generation Tool**: Automates the creation of standardized folder structures and template files for new feature specifications. It generates dated and numbered folders with required subdirectories and template files, replacing placeholders with relevant project and feature details.

2. **Identify Coding Errors Tool**: Analyzes Git commit history to identify coding errors and best practices. It helps create a feedback loop where learnings from bug fixing and code polishing are automatically analyzed and used to continuously improve a central "best practices" document.

**Note:** The provided templates and configurations contain examples suitable for a Svelte project. You should review and customize these files to match your specific project's needs and conventions.

**Warning:** These templates are currently in transition, so some aspects may need to be updated or adjusted to work properly in your environment.

## Setup

Before using the tools, you need to integrate the components into your project:

1. **Copy Folders**: Copy the following folders/files from this template repository into your project's root directory:
   * `templates/scripts/template-generation` → `scripts/template-generation`
   * `templates/scripts/identify_coding_errors` → `scripts/identify_coding_errors`
   * `templates/ai-specs` → `ai-specs`
   * `templates/.vscode/tasks.json` → `.vscode/tasks.json` (Create the `.vscode` directory if it doesn't exist)

2. **Install `uv`**: If you don't have `uv` installed, follow the instructions on the [official Astral `uv` documentation](https://github.com/astral-sh/uv). Typically, you can install it using pip: `pip install uv`.

3. **Create Prerequisite Files**: Ensure the `project-summary.md` and `project-tech-design.md` files exist in your project root (or update the paths in `scripts/template-generation/config.yaml` if you place them elsewhere). These files provide context for the generated specs. You can start with empty files if needed.

Note: Dependencies are automatically installed when running the VS Code tasks, so you don't need to install them manually.

## Usage

### Template Generation Tool

You can generate a new feature spec structure using one of the following methods:

**Method 1: VSCode Task (Recommended)**

1. Open your project in VSCode.
2. Open the Command Palette (usually `Ctrl+Shift+P` or `Cmd+Shift+P`).
3. Type "Tasks: Run Task" and select it.
4. Choose the "Create New Feature Spec" task.
5. A new terminal panel will open, and the script will prompt you for the feature name and overview.

**Method 2: Command Line**

1. Open your terminal in your project's root directory.
2. Run the script using `uv`:
   ```bash
   uv run scripts/template-generation/main.py
   ```
3. Follow the prompts in the terminal to enter the feature name and overview.

Either method will create the new feature specification folder and files within the `ai-specs` directory in your project root.

### Identify Coding Errors Tool

This tool analyzes Git commit history to identify coding errors and best practices. It works with a specific Git workflow:

**Expected Git Workflow:**
- Maintain a `main` branch as the primary branch
- For each feature, create a feature branch
- After the first implementation of a feature by the AI Agent, create a commit with a message containing "First pass xxxxx"
- The tool looks for this "First pass" commit to determine the starting point for analysis
- If the "First pass" commit isn't found, the tool will prompt you for a commit hash

You can run the tool using:

**Method 1: VSCode Task (Recommended)**

1. Open your project in VSCode.
2. Open the Command Palette (usually `Ctrl+Shift+P` or `Cmd+Shift+P`).
3. Type "Tasks: Run Task" and select it.
4. Choose the "Analyze Feature Commits for Best Practices" task.

**Method 2: Command Line**

1. Open your terminal in your project's root directory.
2. Run the script using `uv`:
   ```bash
   uv run scripts/identify_coding_errors/main.py
   ```

The tool will:
1. Find the latest feature folder in the `ai-specs` directory
2. Determine the commit range for analysis (starting from the "First pass" commit or a manually specified commit)
3. Generate diff files in the `generated/git_changes` directory of the feature folder
4. These diffs can then be analyzed to update the best practices document

## Examples

The repository includes example files to help you understand how to use the tools:

* **Example Best Practices Document**: See `examples/ai-specs/04-30_01_improve-best-practices-updates/spec-document-best-practices.md` for an example of how to document best practices based on Git commit analysis.

* **Example Coding Mistakes Document**: The `examples/ai-specs/04-30_01_improve-best-practices-updates/generated/coding_mistakes.md` shows how to document coding mistakes identified from Git history.

## Configuration

### Template Generation (`scripts/template-generation/config.yaml`)

* **`paths`**:
  * `templates`: Location of the source template files.
  * `project_summary`: Path to the markdown file containing the overall project summary.
  * `project_tech_design`: Path to the markdown file containing the project's technical design.
* **`template_files`**: A list of markdown template filenames that will be copied and processed.
* **`required_dirs`**: A list of subdirectory names to be created within each new feature folder.

## Components

### Template Generation Tool

* **`main.py`**: The main entry point for the script. It orchestrates the process by coordinating the other modules.
* **`config.py` & `config.yaml`**: Manages configuration settings.
* **`input_manager.py`**: Handles collecting user input and generates a unique, formatted folder name.
* **`folder_generator.py`**: Creates the main feature folder and required subdirectories.
* **`project_manager.py`**: Loads content from project files for template variables.
* **`file_generator.py`**: Copies and processes template files with variable replacement.

### Identify Coding Errors Tool

* **`main.py`**: The main entry point that orchestrates the Git commit analysis process.
* **`feature_finder.py`**: Finds the latest feature folder based on the naming convention.
* **`git_handler.py`**: Handles Git repository interactions and commit range determination.
* **`diff_generator.py`**: Generates diff files from the identified commit range.
