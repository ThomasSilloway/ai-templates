# Feature Spec Generation Script PRD

## Overview
Create a Python-based automation system to streamline the creation of feature specification folders and files. The system will integrate with VSCode tasks, provide interactive input collection, and manage template-based file generation.

## Technical Requirements

### Environment
- Python 3.12+
- UV for dependency management
- VSCode Task integration
- Project root directory: /scripts/template-generation/

### Dependencies
```python
# /// script
# dependencies = [
#   "rich>=13.0.0",  # Console UI and progress indicators
#   "prompt-toolkit>=3.0.0",  # Interactive input
#   "PyYAML>=6.0.1",  # Configuration management
#   "pathlib>=1.0.1"  # Path manipulation
# ]
# ///
```

## Core Components

### 1. Configuration Management (`config.py`)
- Load and validate template paths
- Store default settings
- Support for environment overrides
- Template directory configuration
- Project paths management

### 2. Input Collection (`input_manager.py`)
- Interactive prompts for:
  - Feature name (for folder)
  - Feature overview content
- Input validation
- Default value handling

### 3. Folder Structure Generator (`folder_generator.py`)
- Date-based folder naming (MM-DD_XX-feature-name)
- Sequential numbering for multiple features
- Required subdirectory creation:
  - /generated
  - /generated/bugs
  - /generated/polish

### 4. File Generator (`file_generator.py`)
- Template file mapping:
  - feature_overview.md - Main feature description
  - spec-architecture-brainstorm-and-prd.md
  - spec-document-progress.md  
  - spec_bug_fixing_all.md
  - spec_polish.md
  - spec_polish_small.md
- Replace template variables:
  - {{ feature_overview }}
  - {{ project_details }}
  - {{ generated_folder }}
  - {{ prd_link }}
  - {{ change_notes }}

### 5. Project Details Manager (`project_manager.py`)
- Load project details from @/project-summary.md
- Handle file paths and references

## File Structure
```
/scripts/template-generation/
├── __init__.py
├── config.py
├── input_manager.py
├── folder_generator.py
├── file_generator.py
├── project_manager.py
├── main.py
```

## Workflow

1. **Initialization**
   - Load configuration
   - Validate template directory exists
   - Check project structure

2. **User Input Collection**
   - Request feature name
   - Generate folder name with date
   - Collect feature overview
   - Validate inputs

3. **Folder Creation**
   - Generate date-based folder name
   - Create required subdirectories
   - Set up generated/ folder

4. **File Generation**
   - For each template:
     - Load template
     - Replace variables
     - Write to new location
   - Copy templates maintaining structure
   - Update paths and references

## VSCode Integration

### Task Configuration
```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Create New Feature Spec",
      "type": "shell",
      "command": "uv run scripts/template-generation/main.py",
      "presentation": {
        "reveal": "always",
        "panel": "new"
      }
    }
  ]
}
```

## Error Handling
- Invalid input validation
- File system errors
- Template processing errors
- Missing configuration
- Project structure issues

## Future Enhancements
- Template customization
- Multiple template sets
- Batch processing
- Configuration UI
- Template validation tools

## Implementation Notes
- All Python files must be 500 lines or less
- Use type hints throughout
- Document all functions and classes
- Include error handling for all operations
- Maintain separation of concerns