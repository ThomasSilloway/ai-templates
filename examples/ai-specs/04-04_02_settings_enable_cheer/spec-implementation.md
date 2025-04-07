# Overview

  We've just planned out a new feature and created a PRD. Let's work on implementing.

  Follow each task below one by one, make sure not to skip any steps. When creating subtasks with boomerang mode, make sure to include enough context including the filepaths to any files to be modified, filepaths to design docs, etc.

  Some of it is already compoleted. here's the latest message form the LLM agent:

  ```
  I've updated the streamerbot store to support cheer event subscription configuration by:

Adding subscribeToCheerEvents boolean to the DebugSettings interface
Setting the default value to true in defaultConfig
Ensuring persistence through the existing config store mechanism
The store is now ready to support the cheer event subscription functionality in the DebugSettingsForm component.
```

## Docs

Related Files: 

PRD: @/ai-specs\04-04_02_settings_enable_cheer\generated\prd.md

Change Notes: @/ai-specs\04-04_02_settings_enable_cheer\generated\change_notes.md

Best Practices: @/ai-docs/best_practices.md 

## Feature info

We need to add a debug settings to the SettingsPanel under the `Debug Settings` header. It should be a checkbox for if the Cheer websocket event should be subscribed to or not. Toggling it off should unsubscribe, toggling it on should subscribe. Each of those should show a message in the DebugConsole tab for the current status and confirm the toggle worked.  You should not have to disconnect and reconnect to get this toggling.  However, it should save the setting, so next time you run the app it should know to subscribe or not based off that setting.

 
## Project Details

This SvelteKit-based Twitch app prototype features a multi-tab interface with shared state management, integrating with Streamer.bot via WebSocket SDK for comprehensive event handling of Twitch monetary events (bits, subscriptions, gift subs) and commands. The Settings tab provides extensive configuration options, including connection settings, point system configuration with support for various ratio scenarios, and real-time connection status monitoring, while a new Debug Settings panel enables test message configuration for subscription events. The app's core feature is an interactive progress bar system that tracks beard and shave points with smooth animations, configurable totals, and a 50/50 starting position, now enhanced with automatic point allocation from Twitch events and a queuing system for pending points. A Debug console offers extensive monitoring capabilities, displaying formatted Streamer.bot actions with color-coding, a dedicated point testing panel, and a new pending points display that shows queued points per user with real-time updates. The entire application is containerized with Docker for consistent development and deployment, utilizing persistent stores for configuration, debug messages, and point tracking, ensuring state preservation across sessions while maintaining type-safe event handling throughout the system. 

## Generated Folder Path

Full path to generated folder: ai-specs\04-04_02_settings_enable_cheer

## Tasks

### Implement PRD
 - Implement the PRD, keeping in mind to limit files to 500 lines of code or less. For each feature/section in the PRD that makes sense, create a new subtask for boomerang mode.

### Update change_notes.md file
- IMPORTANT: Always preserve existing content and append new changes
- First READ the current content of ai-specs\04-04_02_settings_enable_cheer\generated/change_notes.md to determine the next version number
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
