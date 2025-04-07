## v01 - Refactor Point Stores for Configs Feature

* **Description:** Renamed core point tracking stores to be generic in preparation for the progress bar configurations feature.
* **Details:**
    * Renamed `totalBeardPoints` store to `totalLeftSidePoints` in `src/lib/stores/progress.ts`.
    * Renamed `totalShavePoints` store to `totalRightSidePoints` in `src/lib/stores/progress.ts`.
    * Updated all references to these stores in:
        * `src/lib/components/DebugPanel.svelte`
        * `src/lib/components/ProgressBarContainer.svelte`
        * `src/lib/services/PointManager.ts`

## v02 - Implement Progress Bar Configurations Feature

*   **Description:** Added the full Progress Bar Configurations feature, allowing users to create, manage, and select different visual themes for the progress bar.
*   **Details:**
    *   **Core Service & Type:**
        *   Created `Config` type definition (`src/lib/types/config.ts`).
        *   Created `ConfigService` (`src/lib/services/ConfigService.ts`) with:
            *   Singleton pattern.
            *   Persistence via `localStorage` for configurations and active selection.
            *   Default "Beard or Shave" configuration handling.
            *   Readable stores (`configs`, `activeConfigId`, `activeConfig`).
            *   Implemented CRUD methods (`addConfig`, `updateConfig`, `deleteConfig`, `setActiveConfigId`).
    *   **UI Structure:**
        *   Added "Configs" tab to main navigation (`src/routes/+layout.svelte`).
        *   Created route and page component (`src/routes/configs/+page.svelte`).
    *   **Configuration Management UI (`src/lib/components/ConfigsTab.svelte`):**
        *   Implemented UI to list existing configurations.
        *   Added "Add Configuration" button functionality.
        *   Created editor form for each configuration (Name, Left/Right Text, Left/Right Color).
        *   Integrated `svelte-color-picker` for color selection.
        *   Implemented "Update" button logic calling `ConfigService.updateConfig`.
        *   Implemented "Delete" button logic (with confirmation) calling `ConfigService.deleteConfig`.
    *   **Integration:**
        *   Added configuration selector dropdown to `DebugPanel.svelte`.
        *   Updated `DebugPanel.svelte` labels and button styles to reflect the active configuration.
        *   Updated `ProgressBar.svelte` labels and segment colors to reflect the active configuration.

## v03 - Fix Tab Switching and Color Picker Issues

*   **Description:** Fixed a bug where the application UI was stuck on the Settings page content, and addressed a related missing dependency issue.
*   **Details:**
    *   Corrected the conditional rendering logic in `src/routes/+page.svelte` to ensure the `{#if $activeTab ...}` block correctly displayed content for all tabs ('progress', 'settings', 'configs', 'debug').
    *   Created a local placeholder `ColorPicker.svelte` component (`src/lib/components/ColorPicker.svelte`) to resolve build errors caused by the missing `svelte-color-picker` dependency.
    *   Updated `src/lib/components/ConfigsTab.svelte` to import and use the local `ColorPicker` component.

## v04 - Fix Progress Bar Direction Bug

*   **Description:** Fixed a bug where the progress bar moved in the wrong direction when using the test buttons in the Debug Panel.
*   **Details:**
    *   Corrected the `netPoints` calculation formula in `src/lib/components/DebugPanel.svelte` to be `$totalLeftSidePoints - $totalRightSidePoints`.
    *   Corrected the corresponding `netPoints` calculation formula in `src/lib/components/ProgressBar.svelte` (or the function it uses) to be `leftPoints - rightPoints`.
    *   Removed diagnostic logging added during the debugging process from both `DebugPanel.svelte` and `ProgressBar.svelte`. (Note: This removal step assumes the logging added in the previous step is no longer needed now that the bug is fixed. If the user wants to keep the logging, this line should be omitted).

## v05 - Fix Progress Bar Color Reversal Bug

*   **Description:** Fixed a bug where the progress bar displayed colors opposite to the selected configuration (e.g., left color appeared on the right).
*   **Details:**
    *   Identified the issue in `src/lib/components/ProgressBar.svelte` where CSS variables `--left-color` and `--right-color` were applied incorrectly to the container and overlay backgrounds, causing a visual swap.
    *   Corrected the CSS rules for `.progress-bar-container` and `.progress-bar-overlay` to use the appropriate CSS variables (`--right-color` for container background, `--left-color` for overlay background), ensuring colors match the configuration.

## v06 - Implement Left/Right Command Integration

*   **Description:** Added functionality to define custom commands per configuration for triggering point allocation.
*   **Details:**
    *   Added `leftCommand` and `rightCommand` fields to the `Config` type (`src/lib/types/config.ts`) and updated `ConfigService` (`src/lib/services/ConfigService.ts`) to handle defaults and persistence for these new fields.
    *   Created the new `CommandService` (`src/lib/services/CommandService.ts`) to manage command matching logic based on the active configuration's `leftCommand` and `rightCommand`.
    *   Modified `StreamerbotService` (`src/lib/services/StreamerbotService.ts`) to route incoming `Command.Triggered` events from Streamer.bot to the `CommandService` for processing.
    *   Added `applyPendingPointsForSide` and `resetCurrentPoints` methods to `PointManager` (`src/lib/services/PointManager.ts`) to handle point allocation triggered by commands and reset points on config change, respectively. Removed old hardcoded command checks from `PointManager`.
    *   Added a call to `PointManager.resetCurrentPoints()` within `ConfigService` to clear points when the active configuration is changed.
    *   Updated the `ConfigsTab.svelte` UI (`src/lib/components/ConfigsTab.svelte`) to include input fields for `leftCommand` and `rightCommand`, incorporating them into the new layout structure.
    *   Implemented input validation in `ConfigsTab.svelte` to ensure commands start with the required '!' prefix.
    *   Verified implementation against PRDv2 requirements and ensured trailing newlines in all modified files.
