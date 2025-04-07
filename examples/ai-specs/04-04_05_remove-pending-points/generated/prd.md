# Product Requirements Document: Remove Pending Points Feature

## 1. Overview

This document outlines the requirements for adding functionality to remove pending points within the `DebugPanel` component of the Twitch App Prototype. This allows moderators or the streamer to correct mistakes or clear the queue if necessary.

## 2. Goals

*   Allow removal of pending points for individual users.
*   Allow clearing of all pending points at once.
*   Provide clear visual controls for these actions within the `DebugPanel`.
*   Ensure the application state updates correctly and instantly.
*   Log removal actions for debugging purposes.

## 3. User Stories / Requirements

*   **As a moderator/streamer, I want to see an 'x' icon next to each user in the 'Pending Points' list so that I can remove their specific pending points.**
    *   Acceptance Criteria:
        *   A clickable 'x' icon (color: `#aaaaaa`) appears next to each entry in the "Pending Points" list in `DebugPanel.svelte`.
        *   Clicking the 'x' icon immediately removes that user's entry from the `userPendingPoints` store.
        *   The list display updates instantly to reflect the removal.
        *   A message is logged to the Debug Console indicating which user's points were removed.
*   **As a moderator/streamer, I want to see a 'Clear All' button next to the 'Pending Points' heading so that I can remove all pending points at once.**
    *   Acceptance Criteria:
        *   A clickable "Clear All" button appears next to the "Pending Points" `<h4>` heading in `DebugPanel.svelte`.
        *   The button is right-aligned within its container (e.g., using flexbox `justify-content: space-between` on the header container).
        *   Clicking the "Clear All" button immediately removes all entries from the `userPendingPoints` store (sets it to an empty object `{}`).
        *   The list display updates instantly to show "No pending points".
        *   A message is logged to the Debug Console indicating that all pending points were cleared.

## 4. Technical Implementation (Based on Architecture Option 2)

*   **`PointManager` Service (`src/lib/services/PointManager.ts`):**
    *   Add a new public method: `removePendingPointsForUser(userId: string, displayName: string)`
        *   This method will update the `userPendingPoints` store by removing the entry corresponding to `userId`.
        *   It will call `this.logPointCalculation()` (or a similar new logging method specific to removals) to log a message like `"[Points] Removed pending points for user {displayName}"`.
    *   Add a new public method: `clearAllPendingPoints()`
        *   This method will update the `userPendingPoints` store by setting it to an empty object (`{}`).
        *   It will call `this.logPointCalculation()` (or similar) to log a message like `"[Points] Cleared all pending points"`.
*   **`DebugPanel.svelte` (`src/lib/components/DebugPanel.svelte`):**
    *   Import the `PointManager` instance.
    *   **Pending Points List:**
        *   Modify the `#each` block iterating through `Object.entries($userPendingPoints)`.
        *   Inside the loop, add a clickable element (e.g., a `<span>` or `<button>`) styled as an 'x' icon (using CSS or an SVG). Use the color `#aaaaaa`.
        *   Add an `on:click` handler to this icon that calls `PointManager.getInstance().removePendingPointsForUser(userId, entry.displayName)`. Pass the correct `userId` and `displayName` from the loop variables.
    *   **Pending Points Header:**
        *   Modify the container holding the `<h4>Pending Points:</h4>` heading. Use CSS (e.g., flexbox) to allow for right-alignment of a new button.
        *   Add a `<button>` element with the text "Clear All".
        *   Add an `on:click` handler to this button that calls `PointManager.getInstance().clearAllPendingPoints()`.
        *   Style the button appropriately (e.g., similar to the existing "Reset Progress" button but perhaps less prominent).
*   **Stores:**
    *   No changes required to the structure of `userPendingPoints` or `messages` stores.
*   **Logging:**
    *   Ensure the new methods in `PointManager` use the `messages.addMessage` store (likely via the existing `logPointCalculation` helper or a new one) to log the removal actions as specified in the requirements.

## 5. UI/UX

*   The 'x' icon should be clearly clickable and positioned intuitively next to the user entry it affects (e.g., to the right of the points value).
*   The "Clear All" button should be clearly associated with the "Pending Points" section. Right-alignment next to the heading is preferred.
*   Updates to the list should be immediate upon clicking, with no confirmation dialogs.

## 6. Future Considerations (Out of Scope for this PRD)

*   Adding confirmation dialogs (if user feedback suggests they are needed).
*   Adding undo functionality.