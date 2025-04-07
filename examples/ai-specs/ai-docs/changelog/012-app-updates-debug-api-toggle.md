# App Updates - Debug API Toggle &amp; Polish

This update focuses on adding a new debug setting for API event logging, implementing several UI polish improvements, and fixing bugs related to point calculations.

## Feature: Enable Debug API Logging (v1.0.0)

*   **New Setting:** Added an "Enable Debug: API" checkbox to the Debug Settings section.
    *   Allows users to toggle the visibility of detailed Streamer.bot API event logs in the Debug Console.
    *   Setting state persists across application restarts via the configuration store.
*   **Implementation:**
    *   Added `enableApiDebugging` flag to the `DebugSettings` store interface.
    *   Implemented the UI checkbox in `DebugSettingsForm.svelte`.
    *   Created a dedicated `addApiDebugMessage` method in relevant services (`StreamerbotService`, `TwitchChatService`) to handle conditional logging based on the setting.
    *   Refactored existing API log calls to use the new dedicated function.

## UI Polish (v1.1.0, v1.2.0)

*   **Debug Console Enhancements (v1.1.0):**
    *   Adjusted height to dynamically use available viewport space, fixing the previous cutoff issue.
    *   Implemented "smart" auto-scrolling: automatically scrolls to new messages only if the user is already near the bottom, preserving scroll position otherwise.
*   **Point Configuration Precision (v1.2.0):**
    *   Updated multiplier inputs (Tier 2, Tier 3, Resub) in `PointConfigForm.svelte` to support up to 3 decimal places (e.g., 2.512), allowing for finer control.
*   **Number Formatting Consistency (v1.2.0):**
    *   Created a shared utility (`numberFormat.ts`) to standardize the display of point values.
    *   Applied formatting to Action History, Pending Points, and other relevant displays in `DebugPanel.svelte`.
    *   Ensures numbers are rounded to the nearest hundredth (2 decimal places) and trailing zeros are removed for whole numbers, fixing floating-point display artifacts.

## Bug Fixes (v1.2.1, v1.2.2)

*   **Gift Sub Points Calculation (Cumulative Total) (v1.2.1):**
    *   Fixed a bug where the `cumulativeTotal` (number of subs gifted in a single event) was ignored.
    *   Points are now correctly calculated as `(base points) * cumulativeTotal`.
    *   Enhanced debug logging for verification.
*   **Gift Sub Points Calculation (Duration Months) (v1.2.2):**
    *   Fixed a bug where the `durationMonths` for gifted subs was ignored.
    *   Points are now correctly calculated as `(base points) * cumulativeTotal * durationMonths`.
    *   Enhanced debug logging for verification.