# twitch-interactive-app

## High Level Overview
 We just implemented a new feature. We found a bug in the implementation. If more logging is needed, let's add more. If not, please fix the bug and I'll retry to see if it's fixed.

 Follow the steps below, starting with the first one and then choose the next task based off of the instructions.

 When creating subtasks with boomerang mode, make sure to include enough context including the filepaths to any files to be modified, filepaths to design docs, etc

   For all .md file changes use Architect mode

  For all code changes use Code mode

## Bug Description

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

### Create bug report
```
Record your notes about the bug in a new file inside {{ generated_folder }}\generated\bugs\ 
- Located the {{ generated_folder }}\generated\bugs folder in the same directory as the prd file
- Find the highest bug number folder in the {{ generated_folder }}\generated\bugs folder
- Naming convention: Bug_<number + 1>_<Bug_Description>
- Note the bug description in the folder name should be 5 words or less
- Example: Bug_01_Signal_Connection_API_Incompatibility
- CREATE the new folder with that name in {{ generated_folder }}\generated\bugs\
- Then write the bug description into a new file inside the folder called `bug_description.md`
- Do not write any possible solutions in the bug report, just details about the bug
- ASK ME to review the bug report before doing anything else
```

### Write Fix Bug Plan
```
- ASK me any questions about the bug or code files you might have before proceeding
- INVESTIGATE related code files to figure out the root cause or if unknown, then which logs to add
- WRITE bug_fix_plan.md with the details of how to fix the bug. Use same directory as the `bug_description.md`
  - Use only pseudo code if its even necessary, do not write full code blocks
- ASK me to review the new document and provide feedback
```

### Fix the bug
```
- IMPLEMENT the bug_fix_plan.md plan
- ASK me to run the app again and check functionality
- After reading my feedback: 
 - CHOOSE the next task below, whichever seems more appropriate [Complete] or [Fix the Bug] or [Add more logging]
```

### Add more logging
```
 - READ Related logs
 - ANALYZE the code files and the logs to spot potential issues
 - ADD Logging to help observability of any issues - logs should be output to the DebugConsole in the app
 - ASK me to run the app again and gather the logs 
 ```

 ### Complete
 ```
 - WRITE bug_fix_learnings.md with the details of what worked, what didn't work from this process. Use same directory as the `bug_description.md`
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
