## High Level Overview
 We just implemented a new feature. There's a few things to tweak to add some polish

  Follow each task below one by one, make sure not to skip any steps. For each task, create a `new_task` to handle it for you using boomerang mode. If that task creates a document, read that document after that sub task is complete to get the new context.

## Polish

- Add more vertical padding bettween the progress bar and the debug panel. Make this a configurable value on the Settings page in a new section called `Misc`
- Progress bar - Debug panel: Make the `Add beard points` button color blue and the shave points button color red to match the progress bar
- Settings Page:
  - Improve formatting of the Connection section at the top. Use similar styling as the Point configuration section below it
  - Improve styling of `Hidden arguments config` section - use similar styling as the point configuration tab for the input box only, everything else is fine

## Docs

PRD: 

Change Notes:

Best Practices: 

Related Files: 

## Feature info

a dynamic progress bar to track "beard" versus "shave" points. The feature will include a main visual bar, a preview bar showing pending points, and smooth animations. Point configuration settings for different monetization methods (bits, subs, tiers) will be managed in a separate settings tab. A debug panel is required for monitoring values, testing point additions, and resetting progress. Development emphasizes modular components and keeping code files under 500 lines.
 
## Project Details

This SvelteKit-based Twitch app prototype features a multi-tab interface (including Settings and Debug) powered by shared state management. Core functionality involves integrating with Streamer.bot via its WebSocket SDK for event handling. The Settings tab allows users to configure the connection (host, port, hidden arguments) and view the connection status. A Debug console displays formatted Streamer.bot actions/sub-actions with color-coding and truncation for long values. The app utilizes persistent stores for configuration and debug messages, and is containerized with Docker for development and deployment.

## Tasks
Perform the following tasks in order:

### Ask me questions
```
- ASK me questions about each polish item to make sure you understand the requirements
```

### Implement the changes for each polish item one by one
```
- IMPLEMENT the change
- ASK me to run the app again and check functionality
```

### Update change_notes.md file
 - If ./generated/change_notes.md file doesn't exist, create it inside the same directory as the prd
 - For each set of changes you implement, add a new section with:
  - ## Version title Ex: v01
    - A brief description of the changes made already made, IMPORTANT: not planned changes
    - Details of what was already implemented/fixed
    - IMPORTANT - ONLY include the changes that have ALREADY been implemented in previous steps, not future plans
 - Always append new changes as a new section at the bottom of the file, keeping the previous change notes intact
