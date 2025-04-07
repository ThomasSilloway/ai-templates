# Bug Description: Command Point Allocation Mismatch (Bug_07)

**Observed Behavior:**
When points are queued (e.g., from bits, subs without commands) and subsequently allocated using a command (`!beard` or `!shave`), there is a discrepancy between the logged action and the actual state update. The Action History log correctly reflects the command used (e.g., "+500 Shave"), but the points are added to the *opposite* side's total (`totalLeftSidePoints` instead of `totalRightSidePoints`, or vice-versa), and the progress bar moves incorrectly based on this erroneous update.

**Example Scenario:**
1. User cheers 500 bits. Points are queued for the user.
2. User types the `!shave` command in chat.
3. Streamer.bot sends the command event to the application.
4. The `PointManager.applyQueuedPoints` method is triggered.
5. **Expected:** `totalRightSidePoints` increases by 500, Action History logs "+500 Shave".
6. **Actual:** `totalLeftSidePoints` increases by 500, `totalRightSidePoints` is unchanged, Action History logs "+500 Shave", and the progress bar moves towards the left side.

**Impact:**
The progress bar does not accurately reflect point allocations made via commands, leading to incorrect visual representation of the goal progress.

**Potential Areas:**
- Logic within `PointManager.applyQueuedPoints` responsible for determining which store (`totalLeftSidePoints` or `totalRightSidePoints`) to update based on the command (`!beard`/`!shave`).
- How the command string is interpreted or mapped to the "left" or "right" side for the store update vs. the action history logging.

**Relevant Files:**
- Point Allocation Logic: `src/lib/services/PointManager.ts` (specifically `applyQueuedPoints`)
- Point Stores: `src/lib/stores/progress.ts` (`totalLeftSidePoints`, `totalRightSidePoints`)
- Action History Store: `src/lib/stores/actionHistory.ts`
- Command Event Handling: `src/lib/services/StreamerbotService.ts` (handler for command events)
- Configuration Service (for text mapping): `src/lib/services/ConfigService.ts`