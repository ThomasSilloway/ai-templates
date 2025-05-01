## High Level Overview
 We just implemented a new feature. There's a few things to tweak to add some polish

  Follow each Task at the bottom of this prompt one by one, make sure not to skip any steps.

## Polish

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

### Ask me questions
```
- ASK me questions about each polish item to make sure you understand the requirements
```

### Create common mistakes doc
```
- CREATE common_coding_mistakes.md in ai-specs\04-30_01_improve-best-practices-updates\generated folder above if it doesn't exist
- PROMPT coding subtasks to update this file any time our coding agent makes a mistake which causes an error. 
   - Purpose: We'll use this doc to try to improve our best practices for the coding agent over time so it can make less errors.
  - Details to include: compile errors that it caused with its code, how it overcame them and how we could prevent that issue in the future with better documentation, prompts, etc.
- PROMPT coding subtasks to use the best practices docs above to improve the code quality and reduce errors in the future.
```


### Implement the changes for each polish item one by one
```
- IMPLEMENT the change
```

### Review
```
- ASK me to run the app again and check functionality
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
