# Bug Fix Plan: Progress Bar Moves Wrong Direction

## Bug Reference

*   **Bug Description:** `ai-specs\04-05_01_progress-bar-configs\generated\bugs\Bug_05_Progress_Bar_Wrong_Direction\bug_description.md`
*   **Issue:** Test buttons in `DebugPanel.svelte` move the progress bar visually in the opposite direction intended when adding points to the left side.

## Root Cause Analysis (Confirmed)

The code analysis confirmed that the `on:click` event handlers for the test point buttons (lines 129-140) correctly update the `$totalLeftSidePoints` and `$totalRightSidePoints` stores.

The actual root cause lies in the calculation of the `netPoints` reactive variable within `src/lib/components/DebugPanel.svelte` (lines 19-25). The current formula is:
```typescript
const netPoints = $totalRightSidePoints - $totalLeftSidePoints;
```
This causes the `netPoints` value (and thus the bar position) to decrease when `$totalLeftSidePoints` increases, leading to the bar moving left instead of right.

## Proposed Fix

1.  **Locate Calculation:** Identify the reactive declaration for `netPoints` in the `<script>` section of `src/lib/components/DebugPanel.svelte` (around lines 19-25).
2.  **Correct Calculation:** Modify the formula to correctly reflect the difference, ensuring the left side contributes positively to the net value relative to the right side. Change the line from:
    ```typescript
    const netPoints = $totalRightSidePoints - $totalLeftSidePoints;
    ```
    to:
    ```typescript
    const netPoints = $totalLeftSidePoints - $totalRightSidePoints;
    ```
3.  **Verify Logic:** Ensure this change correctly aligns the `netPoints` calculation with the intended visual representation where increasing left points moves the bar right, and increasing right points moves the bar left (relative to the 50% center).

## Affected Files

*   `src/lib/components/DebugPanel.svelte`

## Verification Steps

1.  Run the application (`npm run dev` or similar).
2.  Navigate to the "Progress Bar" tab which displays the `DebugPanel`.
3.  Ensure a configuration is active (e.g., the default "Beard or Shave").
4.  Click the top test button (e.g., "Add Beard Points"). Verify the progress bar indicator moves **to the right**.
5.  Click the bottom test button (e.g., "Add Shave Points"). Verify the progress bar indicator moves **to the left**.
6.  Check the point totals displayed in the `DebugPanel` to confirm the correct store was updated (this was already verified as working correctly, but good to double-check).
7.  Check the "Action History" list in the `DebugPanel` to confirm the logged actions match the buttons clicked.