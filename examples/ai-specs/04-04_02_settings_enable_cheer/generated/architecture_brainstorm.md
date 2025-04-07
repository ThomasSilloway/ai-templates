# Architecture Brainstorm: Enable/Disable Cheer Event Subscription

This document outlines potential approaches for implementing the feature to toggle the subscription to Twitch Cheer events via a checkbox in the Debug Settings.

## Requirements Recap

*   Add a checkbox labeled "Enable Cheer Event" to `DebugSettingsForm.svelte`, placed above the "Test Message" input.
*   The checkbox state should be persisted in the `config.debugSettings` store (using a key like `subscribeToCheerEvents`).
*   Toggling the checkbox **on** should subscribe to `Twitch.Cheer` events via the Streamer.bot WebSocket connection *without* requiring a disconnect/reconnect.
*   Toggling the checkbox **off** should unsubscribe from `Twitch.Cheer` events *without* requiring a disconnect/reconnect.
*   Appropriate messages confirming the subscription status change should be logged to the `DebugConsole`.
*   The initial subscription state upon application load/connection should respect the persisted setting.

## Implementation Approaches

Here are three potential ways to implement this feature:

### Approach 1: Modify `setupSubscriptions` Based on Config (Initial Connection Only)

*   **Summary:** Add the `subscribeToCheerEvents` boolean to `config.debugSettings`. Modify the `setupSubscriptions` method in `StreamerbotService` to conditionally include `'Cheer'` in the `Twitch` event array passed to `client.subscribe()` based on the config value *at connection time*.
*   **Pros:**
    *   Simple modification to existing logic.
    *   Ensures the initial state is correct upon connection.
*   **Cons:**
    *   **Does not meet the core requirement:** Toggling the checkbox *after* connection will have no effect until the user manually disconnects and reconnects.

### Approach 2: Direct `subscribe`/`unsubscribe` Calls on Toggle

*   **Summary:**
    1.  Add the `subscribeToCheerEvents` boolean to `config.debugSettings`.
    2.  Add the checkbox to `DebugSettingsForm.svelte`, bound to this config value.
    3.  Create a new method in `StreamerbotService`, e.g., `toggleCheerSubscription(enable: boolean)`.
    4.  When the checkbox value changes in the form, call this new service method.
    5.  Inside `toggleCheerSubscription`, check if the client is connected. If so, call `this.client.subscribe({ Twitch: ['Cheer'] })` or `this.client.unsubscribe({ Twitch: ['Cheer'] })` based on the `enable` parameter. Log confirmation messages here.
    6.  Modify the existing `setupSubscriptions` method to *also* check the initial config value and subscribe (or not) accordingly when the connection is first established.
*   **Pros:**
    *   **Meets all requirements:** Allows dynamic toggling without reconnecting.
    *   Relatively straightforward implementation.
    *   Keeps subscription logic contained within the service.
*   **Cons:**
    *   Requires adding a new method to the service and handling the toggle logic in the component.
    *   Slightly increases complexity compared to Approach 1.

### Approach 3: Centralized Subscription State Manager

*   **Summary:**
    1.  Add the `subscribeToCheerEvents` boolean to `config.debugSettings`.
    2.  Refactor `StreamerbotService` to have a dedicated mechanism for managing desired subscriptions based on the entire `config` state.
    3.  Create a method like `syncSubscriptions()` that compares the desired state (from config) with the actual current subscriptions and calls `client.subscribe()` or `client.unsubscribe()` for *only the events that need changing*.
    4.  Call `syncSubscriptions()` initially upon connection.
    5.  Use a Svelte store reaction (`config.subscribe(...)`) within the service to automatically call `syncSubscriptions()` whenever relevant parts of the config (like `subscribeToCheerEvents`) change.
    6.  The checkbox in `DebugSettingsForm.svelte` simply updates the config store value.
*   **Pros:**
    *   **Meets all requirements.**
    *   Most robust and scalable approach if more dynamic subscriptions are anticipated in the future.
    *   Decouples the UI component (checkbox) from the direct act of subscribing/unsubscribing; it only modifies the state.
    *   Centralizes subscription logic cleanly within the service.
*   **Cons:**
    *   Highest initial implementation complexity.
    *   Might be overkill if only the Cheer event needs dynamic toggling.
    *   Requires careful handling of store reactions to avoid unnecessary calls.

## Recommendation

Approach 2 seems like the best balance between meeting all requirements and implementation complexity for this specific feature. Approach 3 is architecturally cleaner for future expansion but adds more overhead now. Approach 1 is insufficient as it fails the dynamic toggling requirement.