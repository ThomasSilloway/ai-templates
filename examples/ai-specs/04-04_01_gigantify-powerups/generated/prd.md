# Product Requirements Document: ChatMessage-Based Bit Detection

**Version:** 1.0
**Date:** 2025-04-04

## 1. Introduction

This document outlines the requirements for refactoring the Twitch bit/cheer detection mechanism within the Twitch Interactive App prototype. The current system relies on the `Twitch.Cheer` event from Streamer.bot, which fails to capture certain bit-related events like "Power Ups" (e.g., "giantify"). This refactor will switch the detection logic to use the `Twitch.ChatMessage` event, ensuring all events contributing bits are correctly processed.

## 2. Goals

-   Accurately detect and process all Twitch bit donations, including standard cheers and special "Power Up" events associated with bits.
-   Ensure the `bits` value from the `Twitch.ChatMessage` event is reliably used for point calculation.
-   Maintain clear separation of concerns within the application's services.
-   Remove the dependency on the potentially incomplete `Twitch.Cheer` event for bit processing.

## 3. Non-Goals

-   Changing how points are calculated or allocated by the `PointManager` (only changing the *source* of the bit data).
-   Modifying the handling of other Twitch events (Subs, Gift Subs, etc.).
-   Introducing new UI elements related to bit detection.

## 4. Functional Requirements

### FR1: Subscribe to `Twitch.ChatMessage` Event
-   The `StreamerbotService` must subscribe to the `Twitch.ChatMessage` event from the Streamer.bot WebSocket connection.

### FR2: Create `TwitchChatService`
-   A new service class, `TwitchChatService`, shall be created at `src/lib/services/TwitchChatService.ts`.
-   This service should follow the Singleton pattern, similar to `StreamerbotService` and `PointManager`.
-   It should have a method to process incoming `Twitch.ChatMessage` payloads (e.g., `processChatMessage(payload: ChatMessagePayload)`).

### FR3: Delegate Chat Message Processing
-   The `StreamerbotService` shall obtain an instance of `TwitchChatService`.
-   Upon receiving a `Twitch.ChatMessage` event, `StreamerbotService` will call the processing method on the `TwitchChatService` instance, passing the event payload.

### FR4: Implement Bit Detection Logic in `TwitchChatService`
-   The `TwitchChatService.processChatMessage` method must:
    -   Check if the `payload.data.message.bits` property exists and is greater than 0.
    -   If bits > 0, extract the necessary information:
        -   `bits`: `payload.data.message.bits`
        -   `message`: `payload.data.message.message`
        -   `userId`: `payload.data.message.userId`
        -   `username`: `payload.data.message.username` (or `displayName` if preferred/more reliable)
    -   Obtain an instance of `PointManager`.
    -   Call the appropriate method on `PointManager` to handle the bit donation (currently `handleBitsCheer`), passing the extracted data.

### FR5: Remove Old `Twitch.Cheer` Logic
-   The `StreamerbotService` must unsubscribe from the `Twitch.Cheer` event.
-   The `handleCheerEvent` method within `StreamerbotService` must be removed.
-   Any type definitions solely used by the old `handleCheerEvent` can be removed if no longer needed.

## 5. Technical Design (Based on Chosen Architecture Option 2)

1.  **Create `TwitchChatService.ts`:**
    -   Define the class `TwitchChatService`.
    -   Implement the Singleton pattern (`getInstance`).
    -   Add a dependency on `PointManager`.
    -   Implement the `processChatMessage(payload)` method containing the logic from FR4.
    -   Define necessary types (or import from `src/lib/types/twitch.ts`, potentially needing updates for the `ChatMessage` structure).
2.  **Modify `StreamerbotService.ts`:**
    -   Add a dependency on `TwitchChatService`.
    -   In the `setupSubscriptions` method:
        -   Add `'ChatMessage'` to the `Twitch` event array in `client.subscribe`.
        -   Remove `'Cheer'` from the `Twitch` event array.
        -   Add `this.client.on('Twitch.ChatMessage', this.handleChatMessage.bind(this));`
        -   Remove `this.client.on('Twitch.Cheer', this.handleCheerEvent.bind(this));`
    -   Implement a new private method `handleChatMessage(payload)`:
        -   This method will simply call `TwitchChatService.getInstance().processChatMessage(payload);`.
    -   Remove the `handleCheerEvent` method entirely.
3.  **Update Types (`src/lib/types/twitch.ts`):**
    -   Ensure a type definition exists that accurately represents the structure of the `Twitch.ChatMessage` event payload provided in the feature overview. If not, add it.

## 6. Open Questions/Considerations

-   Confirm if `payload.data.message.username` or `payload.data.message.displayName` is the preferred field for identifying the user contributing bits. (Using `username` for consistency unless otherwise specified).
-   Verify the exact structure of the `ChatMessage` payload received from the `@streamerbot/client` library to ensure type safety.

## 7. Future Considerations

-   The `TwitchChatService` could be expanded later to handle other chat-related logic if needed (e.g., command parsing, keyword detection).

---
*End of PRD*