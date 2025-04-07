# Overview

  Some work on this new feature has already begun, let's document the progress thus far into /ai-docs/changelog/<number>-app-updates.md

  Follow each task below one by one, make sure not to skip any steps.

## Feature Overview

Set up an initial prototype for the progress bar tab.

* **Goal:** Create the visual progress bar, establish the core Svelte stores, and display basic debug info alongside the bar within the SvelteKit app.
* **Tasks (SvelteKit App):**
    * Create the `ProgressBar.svelte` component (visuals + props for percentage).
    * Create the core Svelte stores needed:
        * `pointConfiguration` (initially with default values for Bits, Subs, etc.)
        * `totalBeardPoints` (initialize to 0)
        * `totalShavePoints` (initialize to 0)
        * `userPendingPoints` (initialize to empty object `{}`)
    * Use the dedicated ProgressBar tab (e.g., "Beard Progress") to display the `ProgressBar`.
    * Add a "Debug Info" section below the progress bar in this view. Display current values from the stores (`totalBeardPoints`, `totalShavePoints`, calculated percentage, relevant `pointConfiguration` values).
	  * Add button to add points to `totalBeardPoints` and `totalShavePoints` for debug purposes
    * Ensure the `ProgressBar` component updates reactively based on changes in the `totalBeardPoints` and `totalShavePoints` stores.
	* Progress bar should update with cool animation
* **Outcome:** A visual progress bar exists, linked to reactive stores, with a basic debug panel showing initial state (zeros) and buttons.


## Docs

- 

## Project Details

This SvelteKit-based Twitch app prototype features a multi-tab interface (including Settings and Debug) powered by shared state management. Core functionality involves integrating with Streamer.bot via its WebSocket SDK for event handling. The Settings tab allows users to configure the connection (host, port, hidden arguments) and view the connection status. A Debug console displays formatted Streamer.bot actions/sub-actions with color-coding and truncation for long values. The app utilizes persistent stores for configuration and debug messages, and is containerized with Docker for development and deployment.

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