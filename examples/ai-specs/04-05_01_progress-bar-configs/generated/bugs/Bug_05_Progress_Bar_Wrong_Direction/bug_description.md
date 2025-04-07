# Bug Description: Progress Bar Moves Wrong Direction

## Issue

The progress bar moves in the opposite direction intended when using the test buttons located in the `DebugPanel`.

## Expected Behavior

-   Clicking the **top** test button (associated with the configured `leftText`, e.g., "Add Beard Points") should increase the value associated with the left side (`totalLeftSidePoints`) and visually move the progress bar indicator **to the right** (increasing the percentage/width of the left side color).
-   Clicking the **bottom** test button (associated with the configured `rightText`, e.g., "Add Shave Points") should increase the value associated with the right side (`totalRightSidePoints`) and visually move the progress bar indicator **to the left** (decreasing the percentage/width of the left side color / increasing the right side).

## Actual Behavior

-   Clicking the top test button moves the progress bar indicator **to the left**.
-   Clicking the bottom test button moves the progress bar indicator **to the right**.

## Context

-   This issue occurs specifically with the test buttons in the `DebugPanel` component (`src/lib/components/DebugPanel.svelte`).
-   The underlying point stores (`totalLeftSidePoints`, `totalRightSidePoints`) might be updating correctly, but the visual representation or the button actions in `DebugPanel` seem reversed relative to the visual bar movement.
-   The active configuration's `leftText` and `rightText` are displayed correctly on the buttons.