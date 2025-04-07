# Overview

  We've just planned out a new feature and created a PRD. Let's work on implementing.

  Follow each task below one by one, make sure not to skip any steps. When creating subtasks with boomerang mode, make sure to include enough context including the filepaths to any files to be modified, filepaths to design docs, etc

## Docs

Related Files: 

PRD: @/ai-specs\04-04_03_toggle_debug_api_setting\generated\prd.md

Change Notes: @/ai-specs\04-04_03_toggle_debug_api_setting\generated\change_notes.md

Best Practices: @/ai-docs/best_practices.md 

## Feature info

We need a new setting added to `Debug Settings` section of the Settings tab called `Enable Debug: API` -  When this is toggled on, the event data logs that we already have (some commented in, some commented out) will be enabled.  When the setting is toggled off, these logs will no longer display.  The logs are currently outputting to the DebugConsole which is great and want to maintain that.

 
## Project Details

This SvelteKit-based Twitch app prototype features a multi-tab interface with shared state management, integrating with Streamer.bot via WebSocket SDK for comprehensive event handling of Twitch monetary events (bits, subscriptions, gift subs) and commands. The Settings tab provides extensive configuration options, including connection settings, point system configuration with support for various ratio scenarios, and real-time connection status monitoring. The Debug Settings panel now includes an "Enable Cheer Event" checkbox, allowing dynamic WebSocket event subscription management with persistent configuration. The app's core feature is an interactive progress bar system that tracks beard and shave points with smooth animations, configurable totals, and a 50/50 starting position, now enhanced with automatic point allocation from Twitch events and a queuing system for pending points. A Debug console offers extensive monitoring capabilities, displaying formatted Streamer.bot actions with color-coding, subscription status messages, a dedicated point testing panel, and a new pending points display that shows queued points per user with real-time updates. The entire application is containerized with Docker for consistent development and deployment, utilizing persistent stores for configuration, debug messages, and point tracking, ensuring state preservation across sessions while maintaining type-safe event handling throughout the system. 

## Generated Folder Path

Full path to generated folder: ai-specs\04-04_03_toggle_debug_api_setting

## Tasks

### Implement PRD
 - Implement the PRD, keeping in mind to limit files to 500 lines of code or less. For each feature/section in the PRD that makes sense, create a new subtask for boomerang mode.

### Update change_notes.md file
- IMPORTANT: Always preserve existing content and append new changes
- First READ the current content of ai-specs\04-04_03_toggle_debug_api_setting\generated/change_notes.md to determine the next version number
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
