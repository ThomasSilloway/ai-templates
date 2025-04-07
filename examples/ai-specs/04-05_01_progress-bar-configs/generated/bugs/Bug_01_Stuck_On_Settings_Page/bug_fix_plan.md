# Bug Fix Plan: Stuck on Settings Page

**Bug:** Application UI does not switch content when navigation tabs (Progress, Configs, Debug) are clicked; it remains showing the Settings content.

**Hypothesis:**
The root cause is likely within the tab switching logic managed by the root layout (`+layout.svelte`) and the `activeTab` store (`src/lib/stores/activeTab.ts`). Potential issues include:
1.  The `handleTabClick` function in `+layout.svelte` is not correctly updating the `activeTab` store.
2.  The conditional rendering block (`{#if $activeTab ...}`) in `+layout.svelte` is flawed, incorrectly defaulting to or always matching the 'settings' case.
3.  The `activeTab` store itself has an issue preventing updates or reads.
4.  A component rendered by one of the page routes (`/`, `/settings`, `/configs`, `/progress`) might be incorrectly manipulating the `activeTab` store after the initial click.

**Investigation & Fix Steps:**

1.  **Verify `activeTab` Store Update:**
    *   **Action:** Add temporary `console.log('Clicked:', tabName, '; New $activeTab:', $activeTab)` inside the `handleTabClick` function in `src/routes/+layout.svelte` *after* the store update call.
    *   **Action:** Add a temporary reactive log in `+layout.svelte`: `$: console.log('Active tab store changed to:', $activeTab);`
    *   **Check:** Run the app, open the browser console, click different tabs, and verify if the store is being updated with the correct values ('progress', 'settings', 'configs', 'debug').

2.  **Inspect Conditional Rendering in `+layout.svelte`:**
    *   **Action:** Carefully review the `{#if $activeTab === ...}` block in `src/routes/+layout.svelte`.
    *   **Check:** Ensure there's a condition for each tab value ('progress', 'settings', 'configs', 'debug').
    *   **Check:** Verify that the correct component or content slot is rendered within each condition block.
    *   **Check:** Ensure there isn't a logic error causing the 'settings' condition to always be met or preventing other conditions from being met.

3.  **Inspect `+page.svelte` (if involved):**
    *   **Action:** Review `src/routes/+page.svelte`.
    *   **Check:** Determine if it plays a role in rendering the tab content based on `$activeTab`. If so, apply similar checks as step 2 to its conditional logic. (Note: Based on recent changes, `+layout.svelte` is the more likely location for the main conditional rendering).

4.  **Inspect Page Route Components:**
    *   **Action:** Briefly review the `onMount` or other logic in `/settings/+page.svelte`, `/configs/+page.svelte`, `/progress/+page.svelte`.
    *   **Check:** Look for any code that might be resetting `$activeTab` back to 'settings' unintentionally.

5.  **Apply Fix:**
    *   Based on the findings from steps 1-4, correct the logic. This will most likely involve fixing the conditional rendering block in `+layout.svelte` to correctly map `$activeTab` values to their respective components/content.
    *   Remove temporary console logs added during investigation.

**Verification:**
*   After applying the fix, run the app and click each tab (Progress, Settings, Configs, Debug) to confirm that the correct content area is displayed for each tab.