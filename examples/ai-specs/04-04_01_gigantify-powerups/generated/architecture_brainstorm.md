# Architecture Brainstorm: Refactoring Bit Detection with ChatMessage Event

## Feature Goal

Refactor the existing Twitch bit/cheer detection logic to use the `Twitch.ChatMessage` event provided by the Streamer.bot WebSocket connection instead of the current `Twitch.Cheer` event. This is necessary to correctly capture all bit-related events, including "Power Ups" like "giantify", which might not trigger the standard `Twitch.Cheer` event but are reflected in the `bits` field of the `ChatMessage`.

## Current Implementation

The current implementation resides in `StreamerbotService.ts`.
- It subscribes to the `Twitch.Cheer` event.
- The `handleCheerEvent` method processes this event.
- It extracts `bits`, `message.message`, `user.id`, and `user.name`.
- It calls `pointManager.handleBitsCheer` with this extracted data.

## Proposed Implementation Options

### Option 1: Modify `StreamerbotService` Directly

**Summary:**
- Modify `StreamerbotService.ts`.
- Change the subscription from `Twitch.Cheer` to `Twitch.ChatMessage`.
- Add a new handler method (e.g., `handleChatMessage`) or adapt an existing one.
- Inside the handler, check if `data.message.bits > 0`.
- If bits are present, extract `bits`, `message.message`, `userId`, `username` from the `ChatMessage` payload.
- Call `pointManager.handleBitsCheer` with the extracted data.
- Remove the old `handleCheerEvent` method and `Twitch.Cheer` subscription.

**Pros:**
- **Simplicity:** Least amount of structural change. Keeps related logic together.
- **Minimal Overhead:** No new files or complex interactions introduced.

**Cons:**
- **SoC Concern:** `StreamerbotService` might grow large over time, handling many different event types directly.
- **Less Focused:** Blurs the line between connection management and specific event processing.

### Option 2: Introduce a Dedicated `TwitchChatService`

**Summary:**
- Create a new file `src/lib/services/TwitchChatService.ts`.
- `StreamerbotService` subscribes to `Twitch.ChatMessage` but delegates processing to an instance of `TwitchChatService`.
- `TwitchChatService` contains the logic to check `data.message.bits > 0`, extract data, and interact with `PointManager` (e.g., calling `handleBitsCheer`).
- `StreamerbotService` removes its `Twitch.Cheer` subscription and `handleCheerEvent`.

**Pros:**
- **Separation of Concerns:** Clear distinction between connection logic (`StreamerbotService`) and chat message processing (`TwitchChatService`).
- **Testability:** Easier to unit test chat-specific logic in isolation.
- **Maintainability:** Keeps `StreamerbotService` focused on its core responsibility.

**Cons:**
- **Increased Complexity:** Introduces a new class and requires managing its instance and interaction with `StreamerbotService` and `PointManager`.
- **Boilerplate:** Requires setting up the new service class structure.

### Option 3: Event Bus / Store-Driven Approach

**Summary:**
- `StreamerbotService` subscribes to `Twitch.ChatMessage`.
- Upon receiving a `ChatMessage`, `StreamerbotService` pushes the event data (or relevant parts) into a dedicated Svelte store (e.g., `chatMessagesStore`).
- `PointManager` (or another dedicated module) subscribes to this store.
- The store subscriber checks incoming messages for `message.bits > 0`.
- If bits are present, the subscriber extracts data and calls the appropriate `PointManager` method (e.g., `handleBitsCheer`).
- `StreamerbotService` removes its `Twitch.Cheer` subscription and `handleCheerEvent`.

**Pros:**
- **Decoupling:** Very loose coupling between the event source (`StreamerbotService`) and the processor (`PointManager` or subscriber).
- **Extensibility:** Other parts of the application could easily react to chat messages by subscribing to the same store.
- **Reactive:** Aligns well with Svelte's reactive store patterns.

**Cons:**
- **Traceability:** Can be harder to follow the exact flow of data and logic (event -> store -> subscriber -> action).
- **Potential Overkill:** Might be unnecessarily complex if only the `PointManager` needs to react to bits in chat messages.
- **Store Management:** Requires careful design and management of the new store.