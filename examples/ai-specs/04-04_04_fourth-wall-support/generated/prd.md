# Product Requirements Document: Fourth Wall Event Scaffolding

## 1. Introduction

This document outlines the requirements for adding initial support for specific Fourth Wall events within the Twitch App Prototype. The goal is to create the necessary scaffolding to receive and log these events, and to add configuration options for points associated with them, without implementing the actual point calculation or allocation logic at this stage.

## 2. Goals

*   Integrate basic handling for Fourth Wall events: Donation, Gift Purchase, and Order Placed.
*   Provide UI configuration for assigning point values to these events.
*   Establish the service structure for future expansion of Fourth Wall event processing.
*   Enable developers to observe the raw data structure of these events via the debug console.

## 3. Requirements

### 3.1. UI Changes (`PointConfigForm.svelte`)

*   **New Section:** Add a new configuration section titled "FourthWall Rewards".
    *   **Placement:** This section should appear after the "Resub Bonuses" section and before the "Progress Bar Configuration" section.
*   **New Settings:** Add the following number input fields within the "FourthWall Rewards" section:
    *   **Donation Points (per dollar):**
        *   Label: "Points per $1 Donation:"
        *   Tooltip: "Points awarded for every dollar donated via Fourth Wall."
        *   Default Value: `100`
        *   Input Type: `number`, min `0`, step `1` (or appropriate decimal if needed).
    *   **Gift Purchase Points:**
        *   Label: "Gift Purchase Points:"
        *   Tooltip: "Points awarded for a Fourth Wall gift purchase event."
        *   Default Value: `500`
        *   Input Type: `number`, min `0`, step `1`.
    *   **Order Placed Points:**
        *   Label: "Order Placed Points:"
        *   Tooltip: "Points awarded for a Fourth Wall order placed event."
        *   Default Value: `500`
        *   Input Type: `number`, min `0`, step `1`.
*   **Validation:** Ensure existing validation logic applies (values >= 0).
*   **Persistence:** These new settings should be saved to and loaded from the `pointConfiguration` store.

### 3.2. Store Changes (`stores/progress.ts`)

*   **Update Interface:** Modify the `PointConfig` interface (or equivalent type definition) to include the new fields:
    *   `fourthwallDonationPointsPerDollar: number;`
    *   `fourthwallGiftPurchasePoints: number;`
    *   `fourthwallOrderPlacedPoints: number;`
*   **Update Defaults:** Update the default values within the `pointConfiguration` store definition to reflect the specified defaults (100, 500, 500).

### 3.3. New Service (`FourthWallService.ts`)

*   **Create File:** Create a new service file at `src/lib/services/FourthWallService.ts`.
*   **Structure:** Implement it as a Singleton class, similar to `TwitchChatService.ts`.
*   **Dependencies:** Inject or import the `messages` store for logging.
*   **Event Handlers:** Create public methods to handle each relevant Fourth Wall event:
    *   `handleDonation(payload: unknown): void`
    *   `handleGiftPurchase(payload: unknown): void`
    *   `handleOrderPlaced(payload: unknown): void`
    *   *(Note: The `payload` type is initially `unknown`. Future work will involve defining specific TypeScript interfaces based on observed raw data).*
*   **Logging:** Each handler method should:
    *   Log the *raw* event payload received from `StreamerbotService` to the debug console using the `messages` store (e.g., using `addDebugMessage` or a similar utility, potentially tagging the message type as 'fourthwall' or similar for filtering/styling).
    *   Include a descriptive prefix, e.g., "FOURTHWALL DONATION PAYLOAD:", "FOURTHWALL GIFT PURCHASE PAYLOAD:", etc.

### 3.4. Integration (`StreamerbotService.ts`)

*   **Instantiation:** Instantiate the `FourthWallService` singleton within `StreamerbotService`.
*   **Subscription:** Modify the `setupSubscriptions` (or equivalent connection logic) method to subscribe to the following Streamer.bot events:
    *   `Fourthwall.Donation`
    *   `Fourthwall.GiftPurchase`
    *   `Fourthwall.OrderPlaced`
*   **Event Routing:** Add event listeners (`client.on(...)`) for these three events.
*   **Handler Calls:** Each event listener should call the corresponding handler method in the instantiated `FourthWallService`, passing the raw event payload.

## 4. Technical Design Notes

*   This feature will follow **Architecture Option 1 (Dedicated Service)** as defined in `architecture_brainstorm.md`.
*   The initial implementation focuses solely on logging raw event data. Defining specific TypeScript interfaces for the event payloads will be part of subsequent work, informed by the logged data.

## 5. Out of Scope

*   Calculating or allocating points based on Fourth Wall events.
*   Handling any other Fourth Wall events not listed (e.g., `ProductCreated`, `SubscriptionPurchased`).
*   Displaying Fourth Wall event details in the UI beyond the raw debug log.
*   Creating specific TypeScript interfaces for the Fourth Wall event payloads (this will be done later based on observed data).
*   Implementing the logic for "points per dollar" for donations; this requires understanding the event payload structure first.