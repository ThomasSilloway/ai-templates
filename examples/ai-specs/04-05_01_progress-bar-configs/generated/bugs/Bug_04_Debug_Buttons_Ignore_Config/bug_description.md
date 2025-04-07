# Bug Description: Debug Buttons Ignore Active Config

## Observed Behavior

When using the Debug Panel's test controls:

1.  The "Add [Left Text] Points" button (top button) and "Add [Right Text] Points" button (bottom button) correctly display the `leftText`/`rightText` and `leftColor`/`rightColor` from the currently active configuration.
2.  However, clicking the top button *always* triggers the `addBeardPoints` function, which updates `totalLeftSidePoints` and logs the action with `target: 'beard'`, regardless of the active configuration's `leftText`.
3.  Similarly, clicking the bottom button *always* triggers the `addShavePoints` function, which updates `totalRightSidePoints` and logs the action with `target: 'shave'`, regardless of the active configuration's `rightText`.
4.  The "Current Values" display correctly uses the active configuration's `leftText`/`rightText` when showing the point totals for `totalLeftSidePoints`/`totalRightSidePoints`.

This leads to confusing behavior where the button label and color match the config, but the action performed, the target logged in the history, and the resulting progress bar movement are based on the hardcoded "Beard" (Left) / "Shave" (Right) logic, not the dynamic text of the active configuration.

## Expected Behavior

The Debug Panel test control buttons should:

1.  Visually reflect the active configuration's text and colors (which they currently do).
2.  Trigger actions that correspond to the *visual representation* and the *active configuration*.
    *   Clicking the button associated with `leftText`/`leftColor` should add points to `totalLeftSidePoints` and log an action using `leftText` as the target.
    *   Clicking the button associated with `rightText`/`rightColor` should add points to `totalRightSidePoints` and log an action using `rightText` as the target.

## Related Files

*   `twitch-app-prototype/src/lib/components/DebugPanel.svelte` (Contains the faulty button logic)
*   `twitch-app-prototype/src/lib/services/ConfigService.ts` (Provides the active configuration)
*   `twitch-app-prototype/src/lib/stores/progress.ts` (Contains `totalLeftSidePoints`, `totalRightSidePoints`)
*   `twitch-app-prototype/src/lib/stores/actionHistory.ts` (Where incorrect targets are logged)