# Overview

  Some work on this new feature has already begun, let's document the progress thus far into /ai-docs/changelog/<number>-app-updates.md

  Follow each task below one by one, make sure not to skip any steps.

## Feature Overview

Set up an initial prototype for connecting to Streamer.bot websocket server.

## Settings tab

- add some connection status to the websocket server info, whatever you think would be a nice display for a dashboard.

- Maybe we need some input fields to configure the connection?

## DebugConsole tab

Subscribe to the `Raw` websocket server event so we can see all of the actions that are executed.

For each action executed add to the debugconsole this line: `ACTION: <actionname> Args: "arg1": "value1", "arg2": "value2", etc`

- For any values that are more than 20 characters, truncate them

For each subaction executed add the same as above for debugconsole bug prefix with `[ParentActionName] <subactionname> Args: same as above, etc`


## Docs

- 

## Project Details

The Twitch App Prototype is a SvelteKit-based application featuring a three-tab interface (Progress Bar, Settings, and Debug) with seamless tab switching powered by a shared state management system. The Debug console implements a sophisticated color-coding system that visually distinguishes between different types of Twitch events (subscriptions in green, bits in purple, and general messages in gray) to enhance readability and event tracking. The app utilizes a persistent message store that maintains debug messages across tab switches, preparing for future integration with Streamer.bot's websocket API. The development environment is containerized using Docker, with separate configurations for development (with hot-reload) and production, making it easy to develop and deploy across different environments.

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