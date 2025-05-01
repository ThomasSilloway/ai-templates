# Overview

  Some work on this new feature has already begun, let's document the progress thus far into /ai-docs/changelog/<number>-app-updates.md

  You are in Architect mode, you can directly write and modify .md files.

  Follow each Task at the bottom of this prompt one by one, make sure not to skip any steps.

## Feature Overview

improve-best-practices-updates
create a more robust feedback loop where learnings from manual and semi-automated bug fixing/polishing, captured in Git commits, are automatically analyzed and used to continuously improve a central "best practices" document. This ensures the AI's knowledge base stays up-to-date with encountered issues and their resolutions, leading to fewer repeated mistakes in future AI-generated code.



## Docs

PRD: @/ai-specs\04-30_01_improve-best-practices-updates\generated\prd.md

Change Notes: @/ai-specs\04-30_01_improve-best-practices-updates\generated\change_notes.md

Project Tech Design: @/project-tech-design.md

Project Summary: @/project-summary.md

## Project Details

This project integrates a Python Discord bot (discord.py) frontend (app/discord-bot) with a Google Agent Development Kit (ADK) agent backend (app/ai-agent). The goal is to enable real-time interaction between a user-facing Discord interface and AI processing capabilities provided by the ADK agent.

The Discord bot (app/discord-bot/src/bot.py) handles receiving user messages and forwards them to the ADK agent via a WebSocket connection established through the agent's `/ws/{session_id}` endpoint. The ADK agent (app/ai-agent/app/adk_agent/agent.py), configured using the google-adk library and potentially a Gemini model (with instructions in prompt.py), processes these messages. Responses are planned to be sent back to the Discord bot using an ADK tool that instructs the bot to post the reply in the appropriate channel.

Configuration relies on separate .env files (implied) within each component's directory for storing sensitive keys like the Discord token and Google API keys. Project dependencies for each component are managed separately via their respective requirements.txt files.

The application components are designed to be run containerized using Docker, with services for both the discord-bot and ai-agent defined in the root docker-compose.yml file for orchestrated startup. 

## IMPORTANT
 - DO NOT EDIT ANY CODE 

## Tasks

### Add changelog file
```
- FIND the last change log number in /ai-docs/changelog/
- CREATE /ai-docs/changelog/<next-number>-app-updates-<3 word description>.md
- ANALYZE the current project
- UPDATE app updates file with the latest updates we have implemented thus far in the PRD
```

### Update project summary
```
 - READ @/project-summary.md
   - Purpose: to help summarize the project to an LLM agent
 - CONSIDER changes from the latest feature that may need to be included
 - UPDATE project-summary.md by seamlessly integrating the existing summary with any of these new details into a nice summary for future LLMs to use as a reference for the entire project
   - IMPORTANT: do not reference old features, it should just be a summary of the current state of the project, no need to highlight recent features
   - IMPORTANT: Do not print out the changes to the chat log, directly edit the file
   - IMPORTANT: Do not put full sentences in bold
```

### Update tech design doc
```
- ANALYZE @/project-tech-design.md and see if any changes are necessary due to the new changes.
  - The purpose of this file is to help a coding architect LLM understand what files to change when it comes to bug fixing or making a new feature
- UPDATE the tech design doc with any changes
  - IMPORTANT: do not reference old features, it should just be a summary of the current state of the project, no need to highlight recent features
  - IMPORTANT: Do not print out the changes to the chat log, directly edit the file
  - IMPORTANT: Do not put full sentences in bold, if any are, remove them
```

### Update best practices
```
- ANALYZE ai-specs\04-30_01_improve-best-practices-updates\generated\common_coding_mistakes.md
- UPDATE @/ai-docs/best_practices.md with additional best practices that can be cleaned from the mistakes doc
```
