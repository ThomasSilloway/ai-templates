# Product Requirements Document (PRD): Enable Debug API Logging

## 1. Overview

This document outlines the requirements for adding a new setting to the application's Debug Settings tab. This setting, labeled "Enable Debug: API", will allow users to toggle the visibility of detailed Streamer.bot API event logs within the application's Debug Console.

## 2. Goals

*   Provide users with control over the verbosity of API-related debug messages.
*   Allow users to easily enable/disable detailed API event logging for troubleshooting purposes.
*   Ensure the setting's state persists across application restarts.
*   Maintain the existing functionality of logging messages to the Debug Console.

## 3. User Interface (UI)

*   A new checkbox input will be added to the `Debug Settings` section within the `Settings` tab (`DebugSettingsForm.svelte`).
*   **Placement:** This new checkbox group should appear directly below the existing "Enable Cheer Event" checkbox group and above the "Test Message" input group.
*   **Label:** "Enable Debug: API"
*   **Description (below checkbox):** "Toggle the display of detailed Streamer.bot API event data in the Debug Console."
*   The existing "Save Changes" button in the Debug Settings form will save the state of this new checkbox along with other debug settings.

## 4. Functionality

*   **Toggle Control:** The "Enable Debug: API" checkbox allows users to switch the setting ON or OFF.
*   **Persistence:** The state of this setting (ON/OFF) will be saved within the `$config.debugSettings` persistent store, ensuring it is remembered across application sessions.
*   **Logging Control:**
    *   When the setting is **ON**, calls related to Streamer.bot API events using the designated logging function (`addApiDebugMessage`) will result in messages being added to the Debug Console via the existing `addDebugMessage` mechanism.
    *   When the setting is **OFF**, calls to the designated logging function (`addApiDebugMessage`) will be suppressed, and no corresponding message will be added to the Debug Console.
*   **Target Logs:** This setting specifically controls logs generated from Streamer.bot API events (e.g., incoming WebSocket messages for bits, subs, etc.) primarily within `StreamerbotService.ts` and potentially `TwitchChatService.ts`. Other debug messages added via `addDebugMessage` should remain unaffected.
*   **Output:** Controlled logs will continue to appear in the existing Debug Console component.

## 5. Technical Implementation (Based on Architecture Option 3)

*   **Store Update:**
    *   Add a new boolean property `enableApiDebugging` to the `DebugSettings` interface within the configuration store (`stores/streamerbot.ts` or relevant type definition).
    *   Initialize `enableApiDebugging` with a default value (e.g., `false`).
*   **UI Implementation (`DebugSettingsForm.svelte`):**
    *   Add a new checkbox input bound to a local state variable (e.g., `localEnableApiDebugging`), respecting the placement specified in Section 3.
    *   Initialize the local state variable from `$config.debugSettings.enableApiDebugging` on component load.
    *   Update the `$config.debugSettings.enableApiDebugging` value in the store when the "Save Changes" button is clicked.
    *   Ensure the `hasUnsavedChanges` logic correctly tracks changes to this new setting.
*   **Dedicated Logging Function:**
    *   Create a new method, `addApiDebugMessage(message: string, data?: any, type: string = 'info')`, likely within `StreamerbotService.ts` (or a shared logging utility if deemed more appropriate after code review).
    *   Inside `addApiDebugMessage`, retrieve the current value of `$config.debugSettings.enableApiDebugging`.
    *   If `enableApiDebugging` is `true`, call the existing `this.addDebugMessage(message, data, type)` method.
    *   If `enableApiDebugging` is `false`, the method should do nothing.
*   **Refactoring:**
    *   Identify all existing calls to `this.addDebugMessage` within `StreamerbotService.ts` and `TwitchChatService.ts` (and potentially other relevant services) that log data related to Streamer.bot API events.
    *   Modify these identified call sites to use the new `this.addApiDebugMessage` method instead.

## 6. Acceptance Criteria

*   **AC1:** A new checkbox labeled "Enable Debug: API" with the specified description exists in the Debug Settings section, placed correctly between "Enable Cheer Event" and "Test Message".
*   **AC2:** Toggling the checkbox and clicking "Save Changes" updates the `enableApiDebugging` value in the persistent `$config.debugSettings` store.
*   **AC3:** The state of the checkbox correctly reflects the persisted value when the Settings tab is revisited or the application is restarted.
*   **AC4:** When the checkbox is checked (ON) and changes are saved, detailed Streamer.bot API event logs appear in the Debug Console.
*   **AC5:** When the checkbox is unchecked (OFF) and changes are saved, detailed Streamer.bot API event logs *do not* appear in the Debug Console.
*   **AC6:** Other non-API-related debug messages added via `addDebugMessage` continue to appear in the Debug Console regardless of the "Enable Debug: API" setting state.