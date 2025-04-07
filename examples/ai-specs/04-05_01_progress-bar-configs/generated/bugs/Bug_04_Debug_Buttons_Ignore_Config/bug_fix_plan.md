# Bug Fix Plan: Debug Buttons Ignore Active Config

## Goal
Modify the Debug Panel test buttons to trigger actions and log history based on the active configuration's `leftText` and `rightText`, instead of hardcoded "Beard" and "Shave" values.

## Affected Files
*   `twitch-app-prototype/src/lib/components/DebugPanel.svelte`

## Proposed Changes

1.  **Introduce New Generic Action Functions:**
    *   In `DebugPanel.svelte`, create two new functions: `addLeftPoints` and `addRightPoints`.
    *   `addLeftPoints` function pseudo-code:
        ```
        function addLeftPoints():
          // Get current active config (already available via $activeConfig)
          // Get testPoints value
          // Update totalLeftSidePoints store by adding testPoints
          // Log action to actionHistory:
          //   type: 'Test Add Points'
          //   points: testPoints
          //   target: $activeConfig.leftText ?? 'Left' // Use dynamic text
          //   timestamp: new Date()
          // (Optional: Keep console.log for debugging, update text)
        ```
    *   `addRightPoints` function pseudo-code:
        ```
        function addRightPoints():
          // Get current active config (already available via $activeConfig)
          // Get testPoints value
          // Update totalRightSidePoints store by adding testPoints
          // Log action to actionHistory:
          //   type: 'Test Add Points'
          //   points: testPoints
          //   target: $activeConfig.rightText ?? 'Right' // Use dynamic text
          //   timestamp: new Date()
          // (Optional: Keep console.log for debugging, update text)
        ```

2.  **Update Button Click Handlers:**
    *   Modify the top button (currently styled with `leftColor` and labeled with `leftText`) to call the new `addLeftPoints` function on click:
        ```html
        <button
          on:click={addLeftPoints} // CHANGE HERE
          style="background-color: {$activeConfig?.leftColor ?? '#1E88E5'}"
        >
          Add {$activeConfig?.leftText ?? 'Left'} Points
        </button>
        ```
    *   Modify the bottom button (currently styled with `rightColor` and labeled with `rightText`) to call the new `addRightPoints` function on click:
        ```html
        <button
          on:click={addRightPoints} // CHANGE HERE
          style="background-color: {$activeConfig?.rightColor ?? '#f44336'}"
        >
          Add {$activeConfig?.rightText ?? 'Right'} Points
        </button>
        ```

3.  **Remove Old Functions (Optional but Recommended):**
    *   Once the new functions are implemented and tested, the old `addBeardPoints` and `addShavePoints` functions can be removed from `DebugPanel.svelte` to avoid confusion.

## Verification Steps
1.  Load the application with a configuration where `leftText` is not "Beard" and `rightText` is not "Shave" (e.g., the user's "Shave"/"Beard" config).
2.  Click the top ("Add [Left Text]") button.
3.  Verify:
    *   The `totalLeftSidePoints` value increases in the "Current Values" display.
    *   The Action History logs an entry with `target:` matching the `leftText` of the active config.
    *   The progress bar moves appropriately (left or right depending on the net points).
4.  Click the bottom ("Add [Right Text]") button.
5.  Verify:
    *   The `totalRightSidePoints` value increases in the "Current Values" display.
    *   The Action History logs an entry with `target:` matching the `rightText` of the active config.
    *   The progress bar moves appropriately.