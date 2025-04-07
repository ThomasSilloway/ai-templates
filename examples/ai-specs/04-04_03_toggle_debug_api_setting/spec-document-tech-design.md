# Overview

  Some work on this new feature has already begun, let's document the progress thus far into /project-tech-design.md

  Follow each task below one by one, make sure not to skip any steps.

## Feature Overview

We need a new setting added to `Debug Settings` section of the Settings tab called `Enable Debug: API` -  When this is toggled on, the event data logs that we already have (some commented in, some commented out) will be enabled.  When the setting is toggled off, these logs will no longer display.  The logs are currently outputting to the DebugConsole which is great and want to maintain that.

## Docs

PRD: @/ai-specs\04-04_03_toggle_debug_api_setting\generated\prd.md

Change Notes: @/ai-docs/changelog/

## Project Details

This SvelteKit-based Twitch app prototype features a multi-tab interface with shared state management, integrating with Streamer.bot via WebSocket SDK for comprehensive event handling of Twitch monetary events (bits, subscriptions, gift subs) and commands. The Settings tab provides extensive configuration options, including connection settings, point system configuration with support for various ratio scenarios, and real-time connection status monitoring. The Debug Settings panel now includes an "Enable Cheer Event" checkbox, allowing dynamic WebSocket event subscription management with persistent configuration. The app's core feature is an interactive progress bar system that tracks beard and shave points with smooth animations, configurable totals, and a 50/50 starting position, now enhanced with automatic point allocation from Twitch events and a queuing system for pending points. A Debug console offers extensive monitoring capabilities, displaying formatted Streamer.bot actions with color-coding, subscription status messages, a dedicated point testing panel, and a new pending points display that shows queued points per user with real-time updates. The entire application is containerized with Docker for consistent development and deployment, utilizing persistent stores for configuration, debug messages, and point tracking, ensuring state preservation across sessions while maintaining type-safe event handling throughout the system. 

## IMPORTANT
 - DO NOT EDIT ANY CODE 

## Tasks

### Add tech design file
```
- READ each file in the change log folder /ai-docs/changelog/ to gather context
- CREATE /project-tech-design.md
- UPDATE the tech design with important information that future LLM agents will be able to use for planning and coding in this project
- INCLUDE the following:
   - System architecture
   - Key technical decisions
   - Design patterns in use
   - Component relationships 
```

### Create Task List
```
 - CREATE a directory of each file in /twitch-app-prototype into /project-file-directory.md
 - UPDATE the directory with `[ ]` next to each file representing a task list that can be checked off for each file
```

### Update tech design file
```
- READ /project-file-directory.md
- IDENTIFY the next task by finding the next empty `[ ]` on a line and print out the name of the file for the next task
- READ that file
- UPDATE /project-tech-design.md with important information that future LLM agents will be able to use for planning and coding in this project
- INCLUDE the following:
   - System architecture
   - Key technical decisions
   - Design patterns in use
   - Component relationships 
- UPDATE /project-file-directory.md and mark off this task as complete by changing that file's `[ ]` to `[x]`
```

### Repeat
```
- REPEAT `Update tech design file` over and over until there are no unchecked items ex: `[ ]` in the list
```