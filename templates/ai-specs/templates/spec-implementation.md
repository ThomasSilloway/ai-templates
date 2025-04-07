# Overview

  We've just planned out a new feature and created a PRD. Let's work on implementing.

  Follow each task below one by one, make sure not to skip any steps. When creating subtasks with boomerang mode, make sure to include enough context including the filepaths to any files to be modified, filepaths to design docs, etc

  For all .md file changes use Architect mode

  For all code changes use Code mode

## Docs

Related Files: 

PRD: @/{{ prd_link }}

Change Notes: @/{{ change_notes }}

Best Practices: @/ai-docs/best_practices.md 

## Feature info

{{ feature_overview }}
 
## Project Details

{{ project_details }} 

## Generated Folder Path

Full path to generated folder: {{ generated_folder }}

## Tasks

### Implement PRD
 - Implement the PRD, keeping in mind to limit files to 500 lines of code or less. For each feature/section in the PRD that makes sense, create a new subtask for boomerang mode.

### Update change_notes.md file
- IMPORTANT: Always preserve existing content and append new changes
- First READ the current content of {{ generated_folder }}\generated/change_notes.md to determine the next version number
- Add a new section with:
  - Version title (increment from last version, e.g., if last was v03, use v04)
    - A brief description of the changes made already made, IMPORTANT: not planned changes
    - Details of what was already implemented/fixed
    - IMPORTANT:
      - ONLY append new changes, DO NOT modify or delete existing content
      - ONLY include changes that have ALREADY been implemented, not future plans
      - Each new version should be added at the bottom of the file
      - Keep the same format as previous versions

### Double check your implementation
```
 - Make sure the PRD was implemented correctly
 - Append the notes of your review to change_notes.md
 - Ensure each file that was touched has an empty line at the end of the file
```
