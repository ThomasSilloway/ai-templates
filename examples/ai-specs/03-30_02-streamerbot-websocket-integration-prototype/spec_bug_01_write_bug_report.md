## High Level Overview
 We just implemented a new feature. I've provided the details of a bug that's occuring, please document it.

  Follow each task below one by one, make sure not to skip any steps.

## Bug description

When clicking the disconnect button in the Settings tab, it seems to hang for a while and the disconnect only happens when I refresh the page.  Disconnect should happen almost immediately and the status reflected on the Settings page using the existing UI.

## Docs

PRD: 

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

### Read docs and request updated scene files
```
 - READ All docs in the `## Docs` section
 - TELL ME which docs are already in your context
 - TELL ME which docs are not already in your context from the lists above
 - READ all the docs that are not yet in your context
 ```

### Create bug report
```
Record your notes about the bug in a new file inside .\generated\bugs\
- Find the highest bug number folder in the generated\bugs folder
- Naming convention: Bug_<number + 1>_<Bug_Description>
- Note the bug description in the folder name should be 5 words or less
- Example: Bug_01_Signal_Connection_API_Incompatibility
- CREATE the new folder with that name in .\generated\bugs\
- Then write the bug description into a new file inside the folder called `bug_description.md`
- Do not write any possible solutions in the bug report, just details about the bug
- ASK ME to review the bug report before doing anything else
```
