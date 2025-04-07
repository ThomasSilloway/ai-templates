# Overview

  Some work on this new feature has already begun, let's document the progress thus far into /ai-docs/changelog/<number>-app-updates.md

  Follow each task below one by one, make sure not to skip any steps.

## Feature Overview

We need to support some more events coming in from Fourth wall this time instead of twitch. These events are Donation, Gift Purchase, and  Order Placed. You can see more details in the websocket-event-types.md    We don't have any documentation yet of what the websocket events will look like, so for this feature let's just set up the scaffolding.
This includes:
- Update `Point Configuration` panel on the `Settings` page to include points for each of these events. It should just be raw points for each of them. So only 3 new settings under the heading FourthWall
- Add the ability to capture these streamerbot events from the websocket and print out the raw data we get from them. Don't try to do any parsing of them yet.  The normal service file is getting long, so create a new service to handle this like we did for the twitch cheer



## Docs

PRD: @/ai-specs\04-04_04_fourth-wall-support\generated\prd.md

Change Notes: @/ai-specs\04-04_04_fourth-wall-support\generated\change_notes.md

## Project Details

This SvelteKit-based Twitch app prototype features a multi-tab interface with shared state management, integrating with Streamer.bot via WebSocket SDK for comprehensive event handling of Twitch monetary events (bits, subscriptions, gift subs - now with accurate point calculation for cumulative counts and duration months) and commands. The Settings tab provides extensive configuration options, including connection settings, point system configuration with support for various ratio scenarios (now with increased precision for multipliers), and real-time connection status monitoring. The Debug Settings panel includes controls like "Enable Cheer Event" and "Enable Debug: API", allowing dynamic WebSocket event subscription and logging management with persistent configuration. The app's core feature is an interactive progress bar system that tracks beard and shave points with smooth animations, configurable totals, and a 50/50 starting position, now enhanced with automatic point allocation from Twitch events and a queuing system for pending points. A Debug console offers extensive monitoring capabilities (now with dynamic height and smart auto-scrolling), displaying formatted Streamer.bot actions with color-coding, subscription status messages, consistently formatted point values using a shared utility, a dedicated point testing panel, and a new pending points display that shows queued points per user with real-time updates. The entire application is containerized with Docker for consistent development and deployment, utilizing persistent stores for configuration, debug messages, and point tracking, ensuring state preservation across sessions while maintaining type-safe event handling throughout the system. 

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