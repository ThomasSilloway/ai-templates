# Changelog - App Updates (Points & Events)

## Feature: Pending Points Removal (v01)

Implemented functionality to manage pending points via the DebugPanel:

*   **PointManager (`src/lib/services/PointManager.ts`):**
    *   Added `removePendingPointsForUser(userId: string, displayName: string)`: Removes points for a specific user and logs the action.
    *   Added `clearAllPendingPoints()`: Clears all pending points and logs the action.
*   **DebugPanel (`src/lib/components/DebugPanel.svelte`):**
    *   Added clickable 'x' icons (color: `#888888`) next to each pending point entry to trigger `removePendingPointsForUser`.
    *   Added a "Clear All" button (background: `#555555`, color: `white`, normal font weight) next to the "Pending Points" heading to trigger `clearAllPendingPoints`.
    *   Ensured UI updates instantly and removal actions are logged to the Debug Console.
    *   Fixed styling issues to prevent background inheritance and ensure correct button appearance.

## Feature: Fourth Wall Event Scaffolding (v01)

Added initial support for handling Fourth Wall events (Donation, Gift Purchase, Order Placed):

*   **Configuration (`stores/progress.ts` & `components/settings/PointConfigForm.svelte`):**
    *   Added new fields to `PointConfig` interface and `pointConfiguration` store defaults:
        *   `fourthwallDonationPointsPerDollar: 100`
        *   `fourthwallGiftPurchasePoints: 500`
        *   `fourthwallOrderPlacedPoints: 500`
    *   Added a "FourthWall Rewards" section to the Settings page (`PointConfigForm.svelte`) with number inputs for these new configuration options.
*   **New Service (`src/lib/services/FourthWallService.ts`):**
    *   Created a Singleton service to handle Fourth Wall events.
    *   Implemented handlers (`handleDonation`, `handleGiftPurchase`, `handleOrderPlaced`) that log the *raw* event payload received from Streamer.bot to the debug console using the `messages` store.
*   **Integration (`src/lib/services/StreamerbotService.ts`):**
    *   Instantiated `FourthWallService`.
    *   Subscribed to Streamer.bot events: `Fourthwall.Donation`, `Fourthwall.GiftPurchase`, `Fourthwall.OrderPlaced`.
    *   Routed these events to the corresponding handlers in `FourthWallService`.

These changes establish the foundation for Fourth Wall integration and provide enhanced control over the pending points system.