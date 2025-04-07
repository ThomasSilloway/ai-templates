## High Level Overview
 We just implemented a new feature. There's a few things to tweak to add some polish

  Follow each task below one by one, make sure not to skip any steps.

  When creating subtasks with boomerang mode, make sure to include enough context including the filepaths to any files to be modified, filepaths to design docs, etc

  For all .md file changes use Architect mode

  For all code changes use Code mode

## Polish

- 

## Docs

Related Files: 

PRD: @/{{ prd_link }}

Change Notes: @/{{ change_notes }}

Best Practices: @/ai-docs/best_practices.md 

## Feature info

{{ feature_overview }}
 
## Project Details

{{ project_details }} 

## Project Tech Design

{{ project_tech_design }}

## Generated Folder Path

Full path to generated folder: {{ generated_folder }}

## Tasks
Perform the following tasks in order:

### Create polish plans
```
Record your notes about each polish item in a new file inside {{ generated_folder }}\generated\polish\ 
- Find the highest number folder in the {{ generated_folder }}\generated
- Naming convention: Polish_<number + 1>_<Polish_Description>
- Note the Polish description in the folder name should be 5 words or less
- Example: Polish_01_Improve_Timestamp_Formatting
- CREATE the new folder with that name in {{ generated_folder }}\generated\polish\
- Then write the polish description into a new file inside the folder called `polish_description.md`
- Write 3 possible solutions for how to implement this small change to the feature
- ASK ME to review the polish reports before doing anything else
```

### Implement the changes for each polish item one by one
```
- IMPLEMENT the polish_description.md plan with the accepted solution
- ASK me to run the app again and check functionality
```

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
