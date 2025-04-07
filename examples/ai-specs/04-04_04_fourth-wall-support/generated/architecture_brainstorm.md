# Architecture Brainstorm: Fourth Wall Event Integration

This document outlines potential approaches for integrating Fourth Wall events (Donation, Gift Purchase, Order Placed) into the Twitch App Prototype. The goal is to add UI configuration for points associated with these events and log the raw event data received from Streamer.bot.

## Requirements Summary

*   **Events:** Handle `Fourthwall.Donation`, `Fourthwall.GiftPurchase`, `Fourthwall.OrderPlaced` from Streamer.bot.
*   **UI:** Add a "FourthWall" section to `PointConfigForm.svelte` with inputs for points related to these events.
    *   Placement: Below "Resub Bonuses", above "Progress Bar Configuration".
    *   Default Values: Donation (100 points/dollar), Gift Purchase (500 points), Order Placed (500 points). *Note: The donation points/dollar needs clarification on how the dollar amount is received in the event payload.*
*   **Service:** Create a new service (`FourthWallService.ts`) to handle these events.
*   **Functionality:** Log the raw event data to the debug console (`messages` store). No point calculation or allocation logic is needed yet.
*   **Store:** Update the `pointConfiguration` store (`stores/progress.ts`) to include fields for the new point settings.

## Implementation Options

Here are three potential ways to structure the implementation:

### Option 1: Dedicated Service (`FourthWallService.ts`)

*   **Summary:** Create a new service `FourthWallService.ts` solely responsible for handling the specified Fourth Wall events. `StreamerbotService.ts` subscribes to `Fourthwall.Donation`, `Fourthwall.GiftPurchase`, and `Fourthwall.OrderPlaced` and routes these events to dedicated handlers within `FourthWallService.ts`. These handlers log the raw event data. The UI and store are updated as per requirements.
*   **Pros:**
    *   **Clear Separation of Concerns:** Keeps Fourth Wall logic isolated.
    *   **Maintainability:** Easier to manage and extend Fourth Wall features later.
    *   **Consistency:** Follows the existing pattern established with `TwitchChatService.ts`.
    *   **Focus:** `StreamerbotService.ts` remains focused on connection management and basic event routing.
*   **Cons:**
    *   **More Files:** Introduces an additional service file.
    *   **Boilerplate:** Requires setting up the service instance and routing logic in `StreamerbotService.ts`.

### Option 2: Integrate into `StreamerbotService.ts`

*   **Summary:** Add new event handlers (`handleFourthWallDonation`, etc.) directly within `StreamerbotService.ts`. This service subscribes to the events and processes them internally by logging the raw data. UI and store updates are the same.
*   **Pros:**
    *   **Centralization:** All Streamer.bot event handling logic resides in one file.
    *   **Fewer Files:** No new service file is created initially.
*   **Cons:**
    *   **Increased Complexity:** `StreamerbotService.ts` becomes larger and handles more diverse responsibilities (connection, Twitch events, Fourth Wall events).
    *   **Reduced Focus:** Violates the Single Responsibility Principle.
    *   **Inconsistent Pattern:** Deviates from the pattern of separating concerns used for `TwitchChatService.ts`.
    *   **Scalability:** Harder to scale if more event sources are added later.

### Option 3: Generic Event Handler Service (e.g., `PlatformEventService.ts`)

*   **Summary:** Create a generic service (e.g., `PlatformEventService.ts`) designed to handle events from various non-Twitch sources. `StreamerbotService.ts` routes events like `Fourthwall.*` to this service. The service internally differentiates handlers based on the event source and type (e.g., `handleFourthWallDonation`). UI and store updates remain the same.
*   **Pros:**
    *   **Future-Proofing:** Provides a structure for integrating other potential event sources (e.g., Ko-fi, Patreon) without needing a new service each time.
    *   **Separation:** Still separates non-Twitch logic from `StreamerbotService.ts`.
*   **Cons:**
    *   **Potential Overkill:** Might be unnecessarily complex if Fourth Wall is the only non-Twitch source anticipated soon.
    *   **Less Specific:** The service name is less descriptive than `FourthWallService.ts`.

## Recommendation

**Option 1 (Dedicated Service - `FourthWallService.ts`)** is recommended. It aligns best with the user's request for a *new service*, follows the existing architectural pattern (`TwitchChatService.ts`), offers the clearest separation of concerns, and provides good maintainability for Fourth Wall-specific logic.