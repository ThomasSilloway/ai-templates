# Product Requirements Document: Progress Bar Configs - Command Integration (v2)

## 0. Document Purpose

This document extends the original PRD (`prd.md`) for the **Progress Bar Configurations** feature. It details the specific requirements for adding **LeftCommand** and **RightCommand** functionality, allowing users to define custom commands (which are triggered via Streamer.bot) that allocate pending points for the active configuration.

## 1. Overview

Building upon the ability to create and manage visual configurations (labels, colors), this enhancement introduces user-defined commands (`LeftCommand`, `RightCommand`) for each configuration. When Streamer.bot triggers a command that matches the active configuration's command name (e.g., `!left`, `!right`), it will trigger the application of any pending points for the triggering user to the corresponding side of the progress bar within the SvelteKit app. This replaces the previously hardcoded `!beard` and `!shave` logic.

## 2. Goals

*   Extend the configuration options to include `LeftCommand` and `RightCommand`.
*   Update the "Configs" tab UI to allow editing of these new command fields.
*   Implement logic to process incoming `Command.Triggered` events from Streamer.bot, checking if the triggered command name matches the *active* configuration's commands (case-insensitive).
*   Trigger the application of pending points via `PointManager` when a matching command event is detected.
*   Implement logic to reset the current progress bar points (`totalLeftSidePoints`, `totalRightSidePoints`) when the active configuration is changed, while preserving pending points.
*   Ensure commands are validated (must start with `!`).

## 3. User Stories

*   **As a streamer, I want** to define custom commands (like `!teamA` and `!teamB`) for each of my progress bar configurations **so that** viewers can use thematic commands (configured in Streamer.bot) to apply their pending points.
*   **As a streamer, I want** the application to only process command triggers associated with the currently active configuration **so that** triggers for commands from inactive themes don't accidentally trigger point allocation.
*   **As a streamer, I want** the progress bar to reset its current points when I switch configurations **so that** the visual representation accurately reflects the newly activated theme's starting point (while keeping pending points queued).

## 4. Functional Requirements

*(This section extends FRs defined in `prd.md`)*

### 4.1. Navigation & Tab (Reference `prd.md` FR1)

*   No changes from `prd.md`.

### 4.2. Configuration Data Structure (Updates `prd.md` FR2)

*   **FR2.1 (Update):** Each configuration object shall contain the following properties:
    *   `id`: string (unique identifier, e.g., UUID)
    *   `name`: string (user-defined name for the configuration)
    *   `leftText`: string (text label for the left side)
    *   `rightText`: string (text label for the right side)
    *   `leftColor`: string (hex color code, e.g., "#FF0000")
    *   `rightColor`: string (hex color code, e.g., "#0000FF")
    *   **`leftCommand`: string (command name for the left side, e.g., "!left")**
    *   **`rightCommand`: string (command name for the right side, e.g., "!right")**

### 4.3. Configuration Management (Configs Tab UI) (Updates `prd.md` FR3)

*   **FR3.1 - FR3.2:** No changes.
*   **FR3.3 (Update):** Creating a new configuration should initialize `leftCommand` and `rightCommand` with default values (e.g., `"!left"`, `"!right"`).
*   **FR3.4 (Update):** Each configuration entry shall allow editing of its `name`, `leftText`, `rightText`, `leftColor`, `rightColor`, **`leftCommand`**, and **`rightCommand`**.
    *   Text fields shall be provided for `name`, `leftText`, `rightText`, **`leftCommand`**, and **`rightCommand`**.
    *   **FR3.4.1 (New):** Input fields for `leftCommand` and `rightCommand` shall visually enforce or indicate the required `!` prefix. Basic validation should ensure the input starts with `!`.
    *   Color inputs remain as defined in `prd.md`.
    *   The "Update" or "Save" button persists all changes, including commands.
*   **FR3.5 - FR3.6:** No changes regarding deletion or color picker.
*   **FR3.7 (New - UI Layout):** The editor for a configuration shall be structured as follows:
    *   `Name` input field at the top.
    *   A horizontal container below the name.
    *   Inside the container, two distinct sections: "Left" and "Right".
    *   Each section ("Left"/"Right") contains input fields for:
        *   Text (`leftText`/`rightText`)
        *   Command (`leftCommand`/`rightCommand`)
        *   Color (`leftColor`/`rightColor`)
    *   The "Update" button below the horizontal container.

### 4.4. Active Configuration Selection (DebugPanel) (Reference `prd.md` FR4)

*   **FR4.1 - FR4.4:** No changes to the selection mechanism itself.
*   **FR4.5 (New):** Changing the active configuration via the dropdown shall trigger the progress bar point reset logic (see FR6.5).

### 4.5. Progress Bar & DebugPanel Updates (Reference `prd.md` FR5)

*   No direct changes needed here based *only* on adding commands. Updates defined in `prd.md` (labels, colors) still apply.

### 4.6. Point Store Refactoring & Logic (Updates `prd.md` FR6)

*   **FR6.1 - FR6.2:** Point stores (`totalLeftSidePoints`, `totalRightSidePoints`) remain as refactored in `prd.md`.
*   **FR6.3 (Update - Command Detection):**
    *   A dedicated `CommandService` shall be implemented.
    *   `StreamerbotService` shall forward relevant data from incoming `Command.Triggered` events (e.g., command name, user info) to `CommandService`.
    *   `CommandService` shall subscribe to the `activeConfig` store from `ConfigService`.
    *   `CommandService` shall compare the received command name (case-insensitively) against the `activeConfig.leftCommand` and `activeConfig.rightCommand`.
    *   The comparison must verify the command name matches exactly (after case normalization). The `!` prefix is part of the command name stored.
*   **FR6.4 (Update - Point Application Trigger):**
    *   If a `Command.Triggered` event's command name matches the active `leftCommand`, `CommandService` shall call a method on `PointManager` (e.g., `applyPendingPointsForSide(userId, 'left')`) using the user info from the event data to apply that user's pending points to `totalLeftSidePoints`.
    *   If a `Command.Triggered` event's command name matches the active `rightCommand`, `CommandService` shall call `PointManager.applyPendingPointsForSide(userId, 'right')` to apply points to `totalRightSidePoints`.
*   **FR6.5 (New - Progress Reset on Config Change):**
    *   When `ConfigService.setActiveConfigId` is called and successfully changes the active configuration:
        *   `ConfigService` shall call a new method on `PointManager` (e.g., `resetCurrentPoints()`).
        *   `PointManager.resetCurrentPoints()` shall set both `$totalLeftSidePoints` and `$totalRightSidePoints` back to 0.
        *   This reset **must not** affect the `userPendingPoints` store.

### 4.7. Default Configuration (Updates `prd.md` FR7)

*   **FR7.1 (Update):** The default configuration shall include:
    *   `leftCommand`: "!beard" (or a generic default like "!left")
    *   `rightCommand`: "!shave" (or a generic default like "!right")
    *   Other fields as defined in `prd.md`.
*   **FR7.2:** No change.

## 5. Non-Functional Requirements

*(This section extends NFRs defined in `prd.md`)*

*   **NFR1 - NFR2, NFR4:** (Persistence, UI/UX, Responsiveness) No changes from `prd.md`.
*   **NFR3 (Update - Error Handling):**
    *   Input validation for `leftCommand` and `rightCommand` should ensure the value starts with `!`. Provide user feedback if the format is incorrect upon trying to save.
    *   Other error handling as per `prd.md`.
*   **NFR5 (New - Code Structure):** Implement the logic using a new `CommandService` as per Architecture Brainstorm Approach 3.

## 6. Technical Design Summary (Approach 3)

*   A singleton `ConfigService` manages configuration state (including `leftCommand`, `rightCommand`) using persisted Svelte stores.
*   **A new singleton `CommandService` is introduced.**
*   `StreamerbotService` forwards relevant data from `Command.Triggered` events to `CommandService`.
*   `CommandService` subscribes to `activeConfig` from `ConfigService` and performs command name matching (case-insensitive, using stored command names like "!left").
*   If a command name matches, `CommandService` calls `PointManager.applyPendingPointsForSide(userId, side)` using user info from the event.
*   `PointManager` handles the application of pending points to `totalLeftSidePoints` or `totalRightSidePoints`.
*   `ConfigService`, upon changing the active config, calls `PointManager.resetCurrentPoints()` to clear the progress bar totals.
*   UI components (`ConfigsTab`, `DebugPanel`, `ProgressBar`) interact with `ConfigService` and reflect the active configuration.
*   Point stores remain generic (`totalLeftSidePoints`, `totalRightSidePoints`).
*   A color picker library is used.

## 7. Out of Scope

*   No changes from `prd.md`.