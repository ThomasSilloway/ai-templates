# twitch-interactive-app

## High Level Overview
 We just implemented a new feature. We found a bug in the implementation.

 Follow the steps below, starting with the first one and then choose the next task based off of the instructions.

## Bug Description

- 

## Docs

Related Files: 

PRD: @/ai-specs\04-30_01_improve-best-practices-updates\generated\prd.md

Change Notes: @/ai-specs\04-30_01_improve-best-practices-updates\generated\change_notes.md

Best Practices: @/ai-docs/best_practices.md 

Project Tech Design: @/project-tech-design.md

## Feature info

improve-best-practices-updates
create a more robust feedback loop where learnings from manual and semi-automated bug fixing/polishing, captured in Git commits, are automatically analyzed and used to continuously improve a central "best practices" document. This ensures the AI's knowledge base stays up-to-date with encountered issues and their resolutions, leading to fewer repeated mistakes in future AI-generated code.

 
## Project Details

This project integrates a Python Discord bot (discord.py) frontend (app/discord-bot) with a Google Agent Development Kit (ADK) agent backend (app/ai-agent). The goal is to enable real-time interaction between a user-facing Discord interface and AI processing capabilities provided by the ADK agent.

The Discord bot (app/discord-bot/src/bot.py) handles receiving user messages and forwards them to the ADK agent via a WebSocket connection established through the agent's `/ws/{session_id}` endpoint. The ADK agent (app/ai-agent/app/adk_agent/agent.py), configured using the google-adk library and potentially a Gemini model (with instructions in prompt.py), processes these messages. Responses are planned to be sent back to the Discord bot using an ADK tool that instructs the bot to post the reply in the appropriate channel.

Configuration relies on separate .env files (implied) within each component's directory for storing sensitive keys like the Discord token and Google API keys. Project dependencies for each component are managed separately via their respective requirements.txt files.

The application components are designed to be run containerized using Docker, with services for both the discord-bot and ai-agent defined in the root docker-compose.yml file for orchestrated startup. 

## Generated Folder Path

Full path to generated folder: ai-specs\04-30_01_improve-best-practices-updates

## Boomerang mode sub task creation

  - You are in boomerange mode, you can read files, but you cannot write to them. You can create sub tasks to edit files.
  
  - When creating subtasks with boomerang mode, make sure to include enough context including the filepaths to any files to be modified, filepaths to design docs, etc

  - Each filepath should be prepending with the (at symbol) followed by (forward slash) symbol followed by the full path relative to the workspace root.  
  
  - IMPORTANT: Do not use backticks around file paths.

  - When creating subtasks use the format below

  - When creating the `Tasks` section from the template, keep each task very discreet, it should only be at most 3 lines per task. 
    - Always have the first word be a verb and ALL CAPS like: CREATE, IMPLEMENT, READ, REVIEW, UPDATE, etc
    - Always create a task for updating the common errors doc
```
# Overview

{{Overview}}

## Docs

{{Docs}}

## Feature info

improve-best-practices-updates
create a more robust feedback loop where learnings from manual and semi-automated bug fixing/polishing, captured in Git commits, are automatically analyzed and used to continuously improve a central "best practices" document. This ensures the AI's knowledge base stays up-to-date with encountered issues and their resolutions, leading to fewer repeated mistakes in future AI-generated code.

 
## Project Details

This project integrates a Python Discord bot (discord.py) frontend (app/discord-bot) with a Google Agent Development Kit (ADK) agent backend (app/ai-agent). The goal is to enable real-time interaction between a user-facing Discord interface and AI processing capabilities provided by the ADK agent.

The Discord bot (app/discord-bot/src/bot.py) handles receiving user messages and forwards them to the ADK agent via a WebSocket connection established through the agent's `/ws/{session_id}` endpoint. The ADK agent (app/ai-agent/app/adk_agent/agent.py), configured using the google-adk library and potentially a Gemini model (with instructions in prompt.py), processes these messages. Responses are planned to be sent back to the Discord bot using an ADK tool that instructs the bot to post the reply in the appropriate channel.

Configuration relies on separate .env files (implied) within each component's directory for storing sensitive keys like the Discord token and Google API keys. Project dependencies for each component are managed separately via their respective requirements.txt files.

The application components are designed to be run containerized using Docker, with services for both the discord-bot and ai-agent defined in the root docker-compose.yml file for orchestrated startup. 

## Generated Folder Path

Full path to generated folder: ai-specs\04-30_01_improve-best-practices-updates

## Tasks

### Task 1
 - <insert instructions>

### Task 2
 - <insert instructions>

### Task 3
 - <insert instructions>

### Update common_coding_mistakes doc
  - Review this chat history for any coding mistakes that you made and had to correct
  - Update <insert_full_path> common_coding_mistakes.md
  - Purpose: We'll use this doc to try to improve our best practices for the coding agent over time so it can make less errors.
  - Details to include: compile errors that mistakes caused, how it overcame them and how we could prevent that issue in the future with better documentation, prompts, etc.

```



## Tasks
Perform the following tasks in order:

### Create bug report
```
Record your notes about the bug in a new file inside ai-specs\04-30_01_improve-best-practices-updates\generated\bugs\ 
- Located the ai-specs\04-30_01_improve-best-practices-updates\generated\bugs folder in the same directory as the prd file
- Find the highest bug number folder in the ai-specs\04-30_01_improve-best-practices-updates\generated\bugs folder
- Naming convention: Bug_<number + 1>_<Bug_Description>
- Note the bug description in the folder name should be 5 words or less
- Example: Bug_01_Signal_Connection_API_Incompatibility
- CREATE the new folder with that name in ai-specs\04-30_01_improve-best-practices-updates\generated\bugs\
- Then write the bug description into a new file inside the folder called `bug_description.md`
- Do not write any possible solutions in the bug report, just details about the bug
```

### Create common mistakes doc
```
- CREATE common_coding_mistakes.md in ai-specs\04-30_01_improve-best-practices-updates\generated folder above if it doesn't exist
- PROMPT coding subtasks to update this file any time our coding agent makes a mistake which causes an error. 
   - Purpose: We'll use this doc to try to improve our best practices for the coding agent over time so it can make less errors.
  - Details to include: compile errors that it caused with its code, how it overcame them and how we could prevent that issue in the future with better documentation, prompts, etc.
- PROMPT coding subtasks to use the best practices docs above to improve the code quality and reduce errors in the future.
```


### Bug report review
```
- ASK ME to review the bug report before doing anything else
```

### Figure out next steps
```
 - ASK me which of the following steps below we should continue with (root cause analysis, Architecture Analysis, add logging, write bug fix plan, fix the bug immediately)
```

### Root Cause Analysis
```
- INVESTIGATE related code files to figure out the root cause
- WRITE root_cause_analysis.md with the details of root cause.  If unsure, write 3 options of what the root cause might be
  - Note: Use same directory as the `bug_description.md`
  - Note: Use only pseudo code if its even necessary, do not write full code blocks
- ASK me to review the new document and provide feedback
```

### Architecture Analysis
```
  - IDENTIFY related code files
  - WRITE architecture_analysis.md with details about how the related files and functionality work together, what issues this architecture might have related to the bug, root cause analysis, proposed solutions
   - Note: Use same directory as the `bug_description.md`
   - Note: Use only pseudo code if its even necessary, do not write full code blocks
  - ASK me to review the new document and provide feedback
```

### Add more logging
```
 - ASK me any questions about the bug or code files you might have before proceeding
 - ANALYZE the code files to try to find the root cause
 - ADD Logging to help observability of any issues - logs should be output to the DebugConsole in the app
 - ASK me to run the app again and gather the logs 
 ```

### Write Fix Bug Plan
```
- INVESTIGATE related code files to figure out the root cause
- WRITE bug_fix_plan.md with the details of root cause.  If unsure, write 3 options of what the root cause might be
  - Note: Use same directory as the `bug_description.md`
  - Note: Use only pseudo code if its even necessary, do not write full code blocks
- ASK me to review the new document and provide feedback
```

### Fix the bug
```
- IMPLEMENT the bug fix
- ASK me to run the app again and check functionality
- REPEAT steps above as necessary
```

 ### Complete
 ```
 - WRITE bug_fix_learnings.md with the details of what worked, what didn't work from this process. Use same directory as the `bug_description.md`
 ```

### Update change_notes.md file
- IMPORTANT: Always preserve existing content and append new changes
- First READ the current content of ai-specs\04-30_01_improve-best-practices-updates\generated/change_notes.md to determine the next version number
- Add a new section with:
  - Version title (increment from last version, e.g., if last was v03, use v04)
    - A brief description of the changes made already made, IMPORTANT: not planned changes
    - Details of what was already implemented/fixed
    - IMPORTANT:
      - ONLY append new changes, DO NOT modify or delete existing content
      - ONLY include changes that have ALREADY been implemented, not future plans
      - Each new version should be added at the bottom of the file
      - Keep the same format as previous versions
      - When creating subtask for boomerang mode - only include the text that needs to change, don't include the entire change notes in the subtask prompt
