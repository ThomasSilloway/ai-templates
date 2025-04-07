# Architecture Brainstorm: Enable Debug API Logging

This document outlines potential approaches for implementing the "Enable Debug: API" setting.

## Feature Goal

Add a persistent setting in the Debug Settings section to toggle the display of Streamer.bot event data logs (currently added via `this.addDebugMessage` primarily in `StreamerbotService.ts` and potentially `TwitchChatService.ts`) in the DebugConsole.

## Implementation Options

Here are three potential ways to implement this feature:

### Option 1: Direct Check in `addDebugMessage`

*   **How:** Add a new boolean flag, `enableApiDebugging`, to the `$config.debugSettings` store. Modify the existing `addDebugMessage` method(s) to check the value of this flag. If `enableApiDebugging` is false, the method returns early without adding the message.
*   **Pros:**
    *   Minimal changes needed, primarily within the `addDebugMessage` function itself.
    *   Conceptually simple.
*   **Cons:**
    *   Requires careful modification of the core `addDebugMessage` logic.
    *   If `addDebugMessage` is used for non-API-event logs, this approach might unintentionally suppress them unless additional logic (like message categorization) is added, increasing complexity.
    *   Assumes *all* relevant logs exclusively use `addDebugMessage`.

### Option 2: Conditional Call Sites

*   **How:** Add the `enableApiDebugging` flag to the `$config.debugSettings` store. Identify all locations in the code (e.g., `StreamerbotService.ts`, `TwitchChatService.ts`) where `this.addDebugMessage` is called for API events. Wrap each of these calls in a conditional statement: `if ($config.debugSettings.enableApiDebugging) { this.addDebugMessage(...); }`.
*   **Pros:**
    *   Keeps the `addDebugMessage` function unchanged.
    *   Explicit control over which specific log calls are conditional.
*   **Cons:**
    *   Requires finding and modifying potentially numerous call sites across different files.
    *   Increases code verbosity around logging calls.
    *   Higher risk of missing some relevant log calls during implementation or future development.

### Option 3: Dedicated API Logging Function

*   **How:** Add the `enableApiDebugging` flag to the `$config.debugSettings` store. Create a new, dedicated method like `addApiDebugMessage` (e.g., within `StreamerbotService` or a shared utility). This new method internally checks the `enableApiDebugging` flag before calling the original `addDebugMessage`. Refactor all existing API-event-related `addDebugMessage` calls to use `addApiDebugMessage` instead.
*   **Pros:**
    *   Clear separation between general debug logging and API-specific debug logging.
    *   Centralizes the control logic for API logs within the new function.
    *   Keeps the original `addDebugMessage` clean for other potential uses.
    *   More maintainable and less error-prone for future changes to API logging.
*   **Cons:**
    *   Requires refactoring all existing API log call sites to use the new function.
    *   Introduces a new function/method to the codebase.