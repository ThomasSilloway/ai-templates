# Product Requirements Document: Debug Setting - Cheer Event Subscription

**Version:** 1.0
**Date:** 2025-04-04

## 1. Overview

This document outlines the requirements for adding a new debug setting to the Twitch interactive overlay application. This setting will allow users to dynamically enable or disable the subscription to Twitch Cheer events received via the Streamer.bot WebSocket connection, primarily for debugging and testing purposes.

## 2. Goals

*   Provide a user interface control to toggle the subscription status of Twitch Cheer events.
*   Allow dynamic subscription/unsubscription without requiring a full disconnect/reconnect cycle.
*   Persist the user's preference for Cheer event subscription across application sessions.
*   Provide clear feedback in the Debug Console when the subscription status changes.

## 3. User Stories

*   As a developer/tester, I want to be able to turn off Cheer event processing temporarily so I can isolate and debug other event types (like subs or commands) without Cheer events cluttering the logs or triggering point calculations.
*   As a developer/tester, I want to easily re-enable Cheer event processing when needed without restarting the application or reconnecting to Streamer.bot.
*   As a user configuring the application, I want my preference for Cheer event subscription to be saved so I don't have to set it every time I launch the app.

## 4. Requirements

### 4.1. Functional Requirements

*   **FR1: Checkbox Control:** A checkbox input shall be added to the `DebugSettingsForm.svelte` component.
    *   **Label:** "Enable Cheer Event"
    *   **Placement:** Located directly above the existing "Test Message" input field within the Debug Settings section of the Settings Tab.
*   **FR2: State Persistence:** The state of the checkbox (checked/unchecked) shall be persisted.
    *   A new boolean property, `subscribeToCheerEvents`, will be added to the `debugSettings` object within the `config` store (`src/lib/stores/streamerbot.ts`).
    *   The checkbox's checked state will be bound to this store value.
    *   The store's persistence mechanism will automatically save this setting.
*   **FR3: Initial Subscription:** Upon establishing a connection to Streamer.bot, the application shall check the persisted `subscribeToCheerEvents` setting.
    *   If `true`, the application must subscribe to the `Twitch.Cheer` event as part of the initial `setupSubscriptions` process in `StreamerbotService`.
    *   If `false`, the application must *not* subscribe to the `Twitch.Cheer` event initially.
*   **FR4: Dynamic Toggling (Subscribe):** When the checkbox is toggled from unchecked to checked *while connected* to Streamer.bot:
    *   The `StreamerbotService` shall be invoked to subscribe to the `Twitch.Cheer` event.
    *   This action must *not* require disconnecting and reconnecting.
*   **FR5: Dynamic Toggling (Unsubscribe):** When the checkbox is toggled from checked to unchecked *while connected* to Streamer.bot:
    *   The `StreamerbotService` shall be invoked to unsubscribe from the `Twitch.Cheer` event.
    *   This action must *not* require disconnecting and reconnecting.
*   **FR6: Debug Console Feedback:**
    *   When the application successfully subscribes to Cheer events (either initially or via toggle), a message like "Subscribed to Twitch Cheer events" shall be added to the Debug Console.
    *   When the application successfully unsubscribes from Cheer events (via toggle), a message like "Unsubscribed from Twitch Cheer events" shall be added to the Debug Console.

### 4.2. Non-Functional Requirements

*   **NFR1: Performance:** The act of subscribing/unsubscribing should have negligible performance impact on the application.
*   **NFR2: Reliability:** The subscription state should reliably reflect the checkbox state and persisted configuration.
*   **NFR3: Maintainability:** The implementation should follow existing code patterns and be easy to understand and modify (aligning with Approach 2).

## 5. Design / UI

*   The UI change is limited to adding a standard HTML checkbox input with the label "Enable Cheer Event" within the `DebugSettingsForm.svelte` component, positioned above the "Test Message" input group. Styling should match existing form elements.

```svelte
<!-- twitch-app-prototype/src/lib/components/settings/DebugSettingsForm.svelte (Conceptual) -->

<script lang="ts">
  import { config } from '../../stores/streamerbot';
  import { StreamerbotService } from '../../services/StreamerbotService'; // Added

  let subscribeToCheerEvents: boolean;
  let testMessage: string;

  $: {
    subscribeToCheerEvents = $config.debugSettings.subscribeToCheerEvents ?? true; // Default to true if undefined
    testMessage = $config.debugSettings.testMessage;
  }

  const handleCheerToggle = () => {
    config.updateConfig({
      debugSettings: {
        ...$config.debugSettings,
        subscribeToCheerEvents
      }
    });
    // Call service method to handle dynamic sub/unsub
    StreamerbotService.getInstance().toggleCheerSubscription(subscribeToCheerEvents);
  };

  const handleTestMessageChange = () => {
    // ... existing logic ...
  };
</script>

<div class="debug-settings-form">
  <!-- NEW Checkbox -->
  <div class="input-group checkbox-group"> <!-- Added class for potential styling -->
    <label for="subscribeCheer">Enable Cheer Event:</label>
    <input
      type="checkbox"
      id="subscribeCheer"
      bind:checked={subscribeToCheerEvents}
      on:change={handleCheerToggle}
    />
    <div class="input-description">
      Toggle subscription to Twitch Cheer events via Streamer.bot.
    </div>
  </div>

  <!-- Existing Test Message Input -->
  <div class="input-group">
    <label for="testMessage">Test Message:</label>
    <!-- ... rest of input ... -->
  </div>
</div>

<style>
  /* Add styles for .checkbox-group if needed */
  .checkbox-group {
    flex-direction: row; /* Example: align label and checkbox horizontally */
    align-items: center;
    gap: 0.5rem;
  }
  .checkbox-group label {
     width: auto; /* Override default width if needed */
  }
  .checkbox-group input[type="checkbox"] {
     width: auto; /* Checkboxes don't need full width */
     /* Add more specific checkbox styles */
  }
  .checkbox-group .input-description {
     flex-basis: 100%; /* Make description take full width below */
     margin-top: 0.25rem;
     margin-left: 0; /* Adjust as needed */
  }
  /* ... existing styles ... */
</style>
```

## 6. Technical Implementation (Approach 2)

1.  **Store Update:** Add `subscribeToCheerEvents: boolean` to the `DebugSettings` interface and the initial state in `src/lib/stores/streamerbot.ts`. Ensure persistence handles this new key. Provide a default value (e.g., `true`).
2.  **UI Component (`DebugSettingsForm.svelte`):**
    *   Add the checkbox input as described in section 5.
    *   Bind its `checked` state to `$config.debugSettings.subscribeToCheerEvents`.
    *   Add an `on:change` handler (`handleCheerToggle`).
    *   Inside `handleCheerToggle`:
        *   Update the `config` store with the new boolean value.
        *   Call a new method on the `StreamerbotService` instance (e.g., `toggleCheerSubscription`) passing the new boolean state.
3.  **Service (`StreamerbotService.ts`):**
    *   **New Method (`toggleCheerSubscription`):**
        *   Accept a boolean `enable` parameter.
        *   Check if `this.client` exists and `this._isConnected` is true.
        *   If `enable` is true, call `this.client.subscribe({ Twitch: ['Cheer'] })`. Log success ("Subscribed...") to Debug Console.
        *   If `enable` is false, call `this.client.unsubscribe({ Twitch: ['Cheer'] })`. Log success ("Unsubscribed...") to Debug Console.
        *   Include error handling (try/catch) and log errors to Debug Console.
    *   **Modify `setupSubscriptions`:**
        *   Before calling `this.client.subscribe`, check `this.currentConfig.debugSettings.subscribeToCheerEvents`.
        *   Conditionally include `'Cheer'` in the `Twitch` array passed to `this.client.subscribe` based on the config value.
        *   Log the initial subscription status for Cheers.
4.  **Debug Console (`DebugConsole.svelte` / `messages` store):** Ensure the `addDebugMessage` function in `StreamerbotService` correctly adds messages with appropriate timestamps. No direct changes needed here if `addDebugMessage` is used correctly.

## 7. Acceptance Criteria

*   **AC1:** A checkbox labeled "Enable Cheer Event" exists in the Debug Settings section, above "Test Message".
*   **AC2:** The checkbox state is loaded correctly based on the persisted value when the application starts.
*   **AC3:** If the checkbox is checked on application start/connection, Cheer events are received and processed.
*   **AC4:** If the checkbox is unchecked on application start/connection, Cheer events are *not* received or processed.
*   **AC5:** While connected, checking the checkbox subscribes to Cheer events without reconnecting, and a confirmation message appears in the Debug Console. Cheer events start being processed.
*   **AC6:** While connected, unchecking the checkbox unsubscribes from Cheer events without reconnecting, and a confirmation message appears in the Debug Console. Cheer events stop being processed.
*   **AC7:** The checkbox state is correctly saved when changed and persists across application restarts.