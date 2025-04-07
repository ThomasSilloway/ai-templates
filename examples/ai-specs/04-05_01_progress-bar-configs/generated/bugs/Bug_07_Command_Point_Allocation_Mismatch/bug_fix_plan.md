# Bug Fix Plan: Command Point Allocation Mismatch (Bug_07)

## 1. Problem Analysis

The investigation confirmed that when allocating queued points via commands (`!beard`, `!shave`), the points are added to the incorrect store (`totalLeftSidePoints` vs. `totalRightSidePoints`) within `src/lib/services/PointManager.ts`, although the action history log reflects the correct intended target.

- The `applyQueuedPoints` method correctly identifies the command (`!beard` or `!shave`).
- It calls a helper method `updatePoints`, passing a boolean flag (`isBeard`) which is `true` for `!beard` and `false` for `!shave`.
- The `updatePoints` method uses this flag to decide which store to update:
    - `if (isBeard)` updates `totalLeftSidePoints`.
    - `else` updates `totalRightSidePoints`.
- This logic is reversed. Conceptually, `!beard` should affect the left side, and `!shave` the right side, matching the default configuration and the action history logging. The current implementation incorrectly associates `!beard` with `totalLeftSidePoints` and `!shave` with `totalRightSidePoints`.

## 2. Proposed Solution

The fix involves correcting the conditional logic within the `updatePoints` method in `src/lib/services/PointManager.ts` to correctly map the `isBeard` flag (derived from the command) to the appropriate point store.

- **Modify `updatePoints` method in `src/lib/services/PointManager.ts`:**
    - Change the conditional logic:
      ```typescript
      // Current Incorrect Logic:
      if (isBeard) {
          totalLeftSidePoints.update(n => n + points);
      } else {
          totalRightSidePoints.update(n => n + points);
      }

      // Corrected Logic:
      if (isBeard) { // !beard command corresponds to the left side
          totalLeftSidePoints.update(n => n + points); // Keep this as is, assuming leftSide = Beard
      } else { // !shave command corresponds to the right side
          totalRightSidePoints.update(n => n + points); // Keep this as is, assuming rightSide = Shave
      }
      ```
    - **Correction:** Reviewing the logic again based on the bug report (Beard=Left, Shave=Right), the *current* logic in `updatePoints` seems correct IF `isBeard` truly means "target the left side". The problem might be in how `applyQueuedPoints` *calls* `updatePoints` or how it determines the `target` for `actionHistory`. Let's refine the plan:

## 2. Refined Proposed Solution

The core issue is the mismatch between the store updated by `updatePoints` and the target logged by `actionHistory.addAction` within `applyQueuedPoints`. The `updatePoints` logic itself (`isBeard` -> `totalLeftSidePoints`, `!isBeard` -> `totalRightSidePoints`) seems internally consistent *if* `isBeard` means "target left side". The `actionHistory` logging also seems correct based on the command (`!beard` -> 'beard', `!shave` -> 'shave').

The most likely fix is to ensure the `target` passed to `actionHistory.addAction` aligns with the *actual* store being updated, potentially using the configuration text.

- **Modify `applyQueuedPoints` method in `src/lib/services/PointManager.ts`:**
    - Get the active configuration text (e.g., `leftText`, `rightText`) from `ConfigService`.
    - Determine the target side based on the command (`!beard` or `!shave`). Let's assume `!beard` maps to the left side and `!shave` maps to the right side for consistency.
    - Call `updatePoints` with the correct boolean flag (`isBeard = (command === '!beard')`).
    - **Crucially:** When calling `actionHistory.addAction`, set the `target` parameter based on the *side determined by the command* and the *corresponding text from the active configuration*.

      ```typescript
      // Inside applyQueuedPoints...

      const currentConfig = get(activeConfig); // Get active config from ConfigService store
      const isTargetingLeft = command === '!beard'; // Assuming !beard targets left

      // Call updatePoints (passing the flag that determines which store is updated)
      this.updatePoints(pointsToApply, isTargetingLeft);

      // Determine the correct text for the action history log
      const targetText = isTargetingLeft
          ? currentConfig?.leftText ?? 'Left'
          : currentConfig?.rightText ?? 'Right';

      // Log to action history using the config text
      actionHistory.addAction({
          type: 'command',
          points: pointsToApply,
          target: targetText, // Use text corresponding to the updated side
          timestamp: new Date(),
      });

      // Remove points from queue...
      ```

This approach ensures that `updatePoints` modifies the correct store based on the command's intent (left/right) and `actionHistory` logs the action using the user-visible text associated with that same side from the current configuration.

## 3. Implementation Steps (Pseudo Code)

1.  Open `src/lib/services/PointManager.ts`.
2.  Import `get` from `svelte/store` and the `activeConfig` store from `ConfigService`.
3.  In the `applyQueuedPoints` method:
    a.  Before calling `updatePoints` and `actionHistory.addAction`:
        i.  Get the current configuration object: `const currentConfig = get(activeConfig);`
        ii. Determine if the command targets the left side: `const isTargetingLeft = command === '!beard';`
    b.  Ensure the call to `this.updatePoints` uses `isTargetingLeft` as the second argument.
    c.  Determine the target text for logging: `const targetText = isTargetingLeft ? (currentConfig?.leftText ?? 'Left') : (currentConfig?.rightText ?? 'Right');`
    d.  Modify the `actionHistory.addAction` call to use `target: targetText`.
4.  Review the `updatePoints` method to confirm its internal logic correctly maps `isBeard=true` to `totalLeftSidePoints` and `isBeard=false` to `totalRightSidePoints`. No changes should be needed here if the above is implemented.
5.  Save the file.

## 4. Testing

- After applying the fix, load the application.
- Ensure a configuration is active (e.g., "Beard or Shave", Left="Beard", Right="Shave").
- Queue some points (e.g., using the Debug Panel's test cheer/sub buttons or actual Twitch events).
- Use the `!beard` command via Streamer.bot or chat.
    - **Verify:** `totalLeftSidePoints` increases, `totalRightSidePoints` is unchanged, Action History logs "+X Beard" (or the configured `leftText`), progress bar moves left.
- Reset or queue more points.
- Use the `!shave` command.
    - **Verify:** `totalRightSidePoints` increases, `totalLeftSidePoints` is unchanged, Action History logs "+X Shave" (or the configured `rightText`), progress bar moves right.
- Test with a different configuration (e.g., Left="Good", Right="Evil") to ensure the Action History text updates correctly.