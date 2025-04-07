# 

## High Level Overview
 We just implemented a new feature. There's a few things to tweak to add some polish

  Follow each task below one by one, make sure not to skip any steps.

## Polish

- Settings tab Hidden Arguments Configuration is very ugly. It shows all of the added tags as a centered list and the add argument input box below that. Let's make it prettier. I'd prefer the input box with the add button on the left and then the tags on the right in a horizontal list. If the list gets too long, it can make a second line of them.

## Docs

PRD: 

Latest Polish DOc:

Docs: 

## Feature info

Set up an initial prototype for connecting to Streamer.bot websocket server.

### Settings tab

- add some connection status to the websocket server info, whatever you think would be a nice display for a dashboard.

- Maybe we need some input fields to configure the connection?

### DebugConsole tab

Subscribe to the `Raw` websocket server event so we can see all of the actions that are executed.

For each action executed add to the debugconsole this line: `ACTION: <actionname> Args: "arg1": "value1", "arg2": "value2", etc`

- For any values that are more than 20 characters, truncate them

For each subaction executed add the same as above for debugconsole bug prefix with `[ParentActionName] <subactionname> Args: same as above, etc`
 
## Project Details
The Twitch App Prototype is a SvelteKit-based application featuring a three-tab interface (Progress Bar, Settings, and Debug) with seamless tab switching powered by a shared state management system. The Debug console implements a sophisticated color-coding system that visually distinguishes between different types of Twitch events (subscriptions in green, bits in purple, and general messages in gray) to enhance readability and event tracking. The app utilizes a persistent message store that maintains debug messages across tab switches, preparing for future integration with Streamer.bot's websocket API. The development environment is containerized using Docker, with separate configurations for development (with hot-reload) and production, making it easy to develop and deploy across different environments.

## Tasks
Perform the following tasks in order:

### Create polish plans
```
Record your notes about each polish item in a new file inside .\generated\polish\
- Find the highest number folder in the generated folder
- Naming convention: Polish_<number + 1>_<Polish_Description>
- Note the Polish description in the folder name should be 5 words or less
- Example: Polish_01_Improve_Timestamp_Formatting
- CREATE the new folder with that name in .\generated\polish\
- Then write the polish description into a new file inside the folder called `polish_description.md`
- Write 3 possible solutions for how to implement this small change to the feature
- ASK ME to review the polish reports before doing anything else
```
