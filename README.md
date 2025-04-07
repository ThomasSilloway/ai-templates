# Prompt Generation Tool

This tool automates the creation of a standardized folder structure and template files for new feature specifications based on predefined templates.

## Overview

This tool automates the creation of a standardized folder structure and template files for new feature specifications based on predefined templates. It prompts the user for a feature name and overview, then generates a dated and numbered folder within the `ai-specs` directory (or as configured). It populates this folder with required subdirectories and copies template files, replacing placeholders with relevant project and feature details.

**Note:** The provided templates (`ai-specs/templates/*.md`) and configuration (`scripts/template-generation/config.yaml`) contain examples suitable for a Svelte project. You should review and customize these files to match your specific project's needs and conventions.

## Setup

Before using the tool, you need to integrate its components into your project:

1.  **Copy Folders**: Copy the following folders/files from this template repository into your project's root directory:
    *   `templates/template-generation` -> `scripts/template-generation`
    *   `templates/ai-specs` -> `ai-specs`
    *   `templates/.vscode/tasks.json` -> `.vscode/tasks.json` (Create the `.vscode` directory if it doesn't exist).
2.  **Install `uv`**: If you don't have `uv` installed, follow the instructions on the [official Astral `uv` documentation](https://github.com/astral-sh/uv). Typically, you can install it using pip: `pip install uv`.
3.  **Install Dependencies**: Open your terminal **in your project's root directory** and use `uv` to install the required Python packages:
    ```bash
    uv pip install "PyYAML>=6.0.1" "pathlib>=1.0.1" "rich>=13.0.0" "prompt-toolkit>=3.0.0"
    ```
    *(Note: `pathlib` is standard in recent Python versions but included here as specified in the script headers).*
4.  **Create Prerequisite Files**: Ensure the `project-summary.md` and `project-tech-design.md` files exist in your project root (or update the paths in `scripts/template-generation/config.yaml` if you place them elsewhere). These files provide context for the generated specs. You can start with empty files if needed.

## Usage

Once the setup is complete, you can generate a new feature spec structure using one of the following methods:

**Method 1: VSCode Task (Recommended)**

1.  Open your project in VSCode.
2.  Open the Command Palette (usually `Ctrl+Shift+P` or `Cmd+Shift+P`).
3.  Type "Tasks: Run Task" and select it.
4.  Choose the "Create New Feature Spec" task.
5.  A new terminal panel will open, and the script will prompt you for the feature name and overview.

**Method 2: Command Line**

1.  Open your terminal in your project's root directory.
2.  Run the script using `uv`:
    ```bash
    uv run scripts/template-generation/main.py
    ```
3.  Follow the prompts in the terminal to enter the feature name and overview.

Either method will create the new feature specification folder and files within the `ai-specs` directory in your project root.

## Configuration (`config.yaml`)

*   **`paths`**:
    *   `templates`: Location of the source template files.
    *   `project_summary`: Path to the markdown file containing the overall project summary.
    *   `project_tech_design`: Path to the markdown file containing the project's technical design.
*   **`template_files`**: A list of markdown template filenames (relative to the `paths.templates` directory) that will be copied and processed.
*   **`required_dirs`**: A list of subdirectory names to be created within each new feature folder.


## Components

*   **`main.py`**: The main entry point for the script. It orchestrates the process by coordinating the other modules.
*   **`config.py` & `config.yaml`**: Manages configuration settings. `config.yaml` defines paths (templates directory, project summary/tech design files), the list of template files to process, and required subdirectories. `config.py` loads this configuration and allows overrides via environment variables (e.g., `TEMPLATE_PATH`).
*   **`input_manager.py`**: Handles collecting user input for the feature name and a detailed feature overview. It also generates a unique, formatted folder name based on the current date and feature name (e.g., `MM-DD_NN_feature-name`).
*   **`folder_generator.py`**: Creates the main feature folder and any required subdirectories as defined in the configuration (e.g., `generated`, `generated/bugs`).
*   **`project_manager.py`**: Loads content from the project summary (`project-summary.md`) and project tech design (`project-tech-design.md`) files specified in the configuration. This content is used for populating template variables.
*   **`file_generator.py`**: Copies template files (listed in `config.yaml`) into the newly created feature folder. It replaces placeholders (like `{{ feature_name }}` or `{{ project_details }}`) within the templates with the actual values collected or loaded by other modules. It specifically handles the creation of `feature_overview.md` from the user's input.


