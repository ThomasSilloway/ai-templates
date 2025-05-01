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

### Analyze Git Commits for Best Practice
```
- LOCATE ai-specs\04-30_01_improve-best-practices-updates\generated\git_changes directory in the current feature's spec folder
- ITERATE through all `NN_<hash>.diff` files chronologically
- ANALYZE each commit message and diff to identify coding mistakes
- GENERATE the feature-specific {{ generated_folder }}\generated\coding_mistakes.md with findings
- UPDATE `ai-docs/best_practices.md` by extracting general patterns from the analysis and merging new patterns intelligently
  - IMPORTANT: Avoid duplication
  - IMPORTANT: Maintain clear organization
```
