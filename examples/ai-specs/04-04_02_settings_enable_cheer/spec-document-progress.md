# Overview

  Some work on this new feature has already begun, let's document the progress thus far into /ai-docs/changelog/<number>-app-updates.md  Also include the notes from the previous feature - gigantify-powerups below

  ```
  # Change Notes

## Version 0.1.0 - Initial Implementation
- Added ChatMessage type definitions to twitch.ts for improved type safety
- Created new TwitchChatService with bit detection logic to handle chat interactions
- Updated StreamerbotService to use ChatMessage events 
```

  Follow each task below one by one, make sure not to skip any steps.

## Feature Overview

We need to add a debug settings to the SettingsPanel under the `Debug Settings` header. It should be a checkbox for if the Cheer websocket event should be subscribed to or not. Toggling it off should unsubscribe, toggling it on should subscribe. Each of those should show a message in the DebugConsole tab for the current status and confirm the toggle worked.  You should not have to disconnect and reconnect to get this toggling.  However, it should save the setting, so next time you run the app it should know to subscribe or not based off that setting.



## Docs

PRD: @/ai-specs\04-04_02_settings_enable_cheer\generated\prd.md

Change Notes: @/ai-specs\04-04_02_settings_enable_cheer\generated\change_notes.md

## Project Details

This SvelteKit-based Twitch app prototype features a multi-tab interface with shared state management, integrating with Streamer.bot via WebSocket SDK for comprehensive event handling of Twitch monetary events (bits, subscriptions, gift subs) and commands. The Settings tab provides extensive configuration options, including connection settings, point system configuration with support for various ratio scenarios, and real-time connection status monitoring, while a new Debug Settings panel enables test message configuration for subscription events. The app's core feature is an interactive progress bar system that tracks beard and shave points with smooth animations, configurable totals, and a 50/50 starting position, now enhanced with automatic point allocation from Twitch events and a queuing system for pending points. A Debug console offers extensive monitoring capabilities, displaying formatted Streamer.bot actions with color-coding, a dedicated point testing panel, and a new pending points display that shows queued points per user with real-time updates. The entire application is containerized with Docker for consistent development and deployment, utilizing persistent stores for configuration, debug messages, and point tracking, ensuring state preservation across sessions while maintaining type-safe event handling throughout the system. 

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