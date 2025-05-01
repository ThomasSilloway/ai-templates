# Overview

  We've just planned out a new feature and created a PRD. Let's work on implementing.

  Follow each Task at the bottom of this prompt one by one, make sure not to skip any steps. 

## Docs

Related Files: 

Tech Architecture: @/ai-specs\04-30_01_improve-best-practices-updates\generated\tech_architecture.md

PRD: @/ai-specs\04-30_01_improve-best-practices-updates\generated\prd.md

Change Notes: @/ai-specs\04-30_01_improve-best-practices-updates\generated\change_notes.md

Best Practices: @/ai-docs/best_practices.md 

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

### Implement PRD
 - Implement the PRD, keeping in mind to limit files to 500 lines of code or less. Implement using the technical architecture

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

### Double check your implementation
```
 - Make sure the PRD was implemented correctly
 - Append the notes of your review to change_notes.md
 - Ensure each file that was touched has an empty line at the end of the file
```
