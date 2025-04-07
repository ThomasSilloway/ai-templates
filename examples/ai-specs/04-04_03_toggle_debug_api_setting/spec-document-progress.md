# Overview

  Some work on this new feature has already begun, let's document the progress thus far into /ai-docs/changelog/<number>-app-updates.md

  Follow each task below one by one, make sure not to skip any steps.

## Feature Overview

We need a new setting added to `Debug Settings` section of the Settings tab called `Enable Debug: API` -  When this is toggled on, the event data logs that we already have (some commented in, some commented out) will be enabled.  When the setting is toggled off, these logs will no longer display.  The logs are currently outputting to the DebugConsole which is great and want to maintain that.



## Docs

PRD: @/ai-specs\04-04_03_toggle_debug_api_setting\generated\prd.md

Change Notes: @/ai-specs\04-04_03_toggle_debug_api_setting\generated\change_notes.md

## Project Details

This SvelteKit-based Twitch app prototype features a multi-tab interface with shared state management, integrating with Streamer.bot via WebSocket SDK for comprehensive event handling of Twitch monetary events (bits, subscriptions, gift subs) and commands. The Settings tab provides extensive configuration options, including connection settings, point system configuration with support for various ratio scenarios, and real-time connection status monitoring. The Debug Settings panel now includes an "Enable Cheer Event" checkbox, allowing dynamic WebSocket event subscription management with persistent configuration. The app's core feature is an interactive progress bar system that tracks beard and shave points with smooth animations, configurable totals, and a 50/50 starting position, now enhanced with automatic point allocation from Twitch events and a queuing system for pending points. A Debug console offers extensive monitoring capabilities, displaying formatted Streamer.bot actions with color-coding, subscription status messages, a dedicated point testing panel, and a new pending points display that shows queued points per user with real-time updates. The entire application is containerized with Docker for consistent development and deployment, utilizing persistent stores for configuration, debug messages, and point tracking, ensuring state preservation across sessions while maintaining type-safe event handling throughout the system. 

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