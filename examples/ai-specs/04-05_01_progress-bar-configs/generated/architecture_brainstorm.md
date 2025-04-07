# Architecture Brainstorm: Progress Bar Configurations Feature

## 1. Feature Goal

Introduce a new "Configs" tab to manage different visual configurations (name, left/right text, left/right color) for the main progress bar. Allow the user to select an active configuration via a dropdown on the `DebugPanel`, which updates the appearance (labels, colors) of the progress bar and associated debug controls. Configurations should persist using `localStorage`.

## 2. Core Requirements & Decisions

*   **New Tab:** "Configs" tab after "Settings", before "DebugConsole".
*   **Config Data:** Each config needs: `id` (unique), `name` (string), `leftText` (string), `rightText` (string), `leftColor` (string - hex), `rightColor` (string - hex).
*   **Storage:** A new Svelte store (`progressBarConfigs`) holding an array of configuration objects, persisted to `localStorage`.
*   **Active Selection:** A mechanism to track the currently active configuration ID (e.g., a new store `activeConfigId`, also persisted).
*   **UI:**
    *   **Configs Tab:** UI for Creating, Reading, Updating, Deleting (CRUD) configurations.
    *   **DebugPanel:** Dropdown to select the active configuration from the `progressBarConfigs` list. Buttons (`Add Left Points`, `Add Right Points`) should use the active config's colors and text.
    *   **ProgressBar:** Labels and bar segment colors should reflect the active configuration.
*   **Point Logic Refactor:** Existing `totalBeardPoints` and `totalShavePoints` stores need refactoring to generic names (e.g., `totalLeftSidePoints`, `totalRightSidePoints`) as the underlying points are shared, only the presentation changes.
*   **Default Config:** A default "Beard or Shave" configuration should be present initially.
*   **Color Picker:** Use a library like `svelte-color-picker` for a good UX in the Configs tab.

## 3. Implementation Approaches

Here are three potential ways to structure the implementation:

### Approach 1: Centralized Config Store + Generic Point Stores + Derived Active Config

*   **Stores:**
    *   `progressBarConfigs`: `Writable<Config[]>` (persisted)
    *   `activeConfigId`: `Writable<string>` (persisted)
    *   `totalLeftSidePoints`: `Writable<number>` (refactored from `totalBeardPoints`)
    *   `totalRightSidePoints`: `Writable<number>` (refactored from `totalShavePoints`)
*   **Logic:**
    *   Components (`DebugPanel`, `ProgressBar`, `ConfigsTab`) subscribe to `progressBarConfigs` and `activeConfigId`.
    *   A derived store or reactive statement (`$: activeConfig = $progressBarConfigs.find(c => c.id === $activeConfigId);`) is used within components needing the active config details.
    *   The `ConfigsTab` handles CRUD operations, updating the `progressBarConfigs` store.
    *   The `DebugPanel` dropdown updates the `activeConfigId` store.
    *   Point updates modify `totalLeftSidePoints`/`totalRightSidePoints`.
*   **Pros:**
    *   Clear separation of configuration data and point data.
    *   Leverages Svelte's built-in reactivity effectively (derived values).
    *   Relatively straightforward data flow.
*   **Cons:**
    *   Requires immediate refactoring of point store names throughout the codebase where they are used.
    *   Components needing the active config need the logic (albeit simple) to find the object from the array using the ID.

### Approach 2: Centralized Config Store + Dedicated Active Config Object Store

*   **Stores:**
    *   `progressBarConfigs`: `Writable<Config[]>` (persisted)
    *   `activeConfigId`: `Writable<string>` (persisted) - Used internally to manage the active object.
    *   `activeConfig`: `Writable<Config | null>` (derived/managed store, potentially not directly persisted itself but initialized from `activeConfigId` and `progressBarConfigs`).
    *   `totalLeftSidePoints`: `Writable<number>` (refactored)
    *   `totalRightSidePoints`: `Writable<number>` (refactored)
*   **Logic:**
    *   Components (`DebugPanel`, `ProgressBar`) subscribe directly to the `activeConfig` store for easy access to labels/colors.
    *   A separate piece of logic (perhaps in the `DebugPanel` or a root component) subscribes to `activeConfigId` and `progressBarConfigs`. When `activeConfigId` changes, it finds the corresponding config object in `progressBarConfigs` and updates the `activeConfig` store.
    *   The `ConfigsTab` handles CRUD for `progressBarConfigs`. If the currently active config is deleted/updated, `activeConfig` needs to be updated accordingly (e.g., set to default or null).
    *   Point updates modify `totalLeftSidePoints`/`totalRightSidePoints`.
*   **Pros:**
    *   Simplifies access for components that only need to *read* the active configuration details.
*   **Cons:**
    *   Adds complexity in managing the `activeConfig` store – ensuring it stays synchronized with `progressBarConfigs` and `activeConfigId`, especially during CRUD operations.
    *   Still requires the point store refactoring.

### Approach 3: Config Store + Config Service

*   **Stores:**
    *   `progressBarConfigs`: `Writable<Config[]>` (persisted) - Potentially managed *internally* by the service.
    *   `activeConfigId`: `Writable<string>` (persisted) - Potentially managed *internally* by the service.
    *   `totalLeftSidePoints`: `Writable<number>` (refactored)
    *   `totalRightSidePoints`: `Writable<number>` (refactored)
*   **Service:**
    *   `ConfigService`: (Singleton)
        *   Manages CRUD operations on `progressBarConfigs`.
        *   Provides methods like `getConfigs(): Readable<Config[]>`, `setActiveConfigId(id: string)`, `getActiveConfig(): Readable<Config | null>`.
        *   Internally uses `progressBarConfigs` and `activeConfigId` stores. The `getActiveConfig` method/store would handle the lookup logic.
*   **Logic:**
    *   Components (`DebugPanel`, `ProgressBar`, `ConfigsTab`) interact with `ConfigService` methods and subscribe to its readable stores.
    *   `ConfigsTab` calls service methods for CRUD.
    *   `DebugPanel` calls `setActiveConfigId` and subscribes to `getActiveConfig`.
    *   `ProgressBar` subscribes to `getActiveConfig`.
    *   Point updates modify `totalLeftSidePoints`/`totalRightSidePoints`.
*   **Pros:**
    *   Encapsulates all configuration management logic within the service.
    *   Potentially cleaner components, as they interact with a defined service API.
*   **Cons:**
    *   Adds another layer of abstraction (the service).
    *   Requires careful design of the service's reactive interface (readable stores) for components to subscribe to changes effectively.
    *   Still requires the point store refactoring.

## 4. Recommendation

All approaches require refactoring the point stores (`totalBeardPoints` -> `totalLeftSidePoints`, etc.).

*   **Approach 1** is often the most idiomatic Svelte approach, relying on derived state within components. It's direct but involves minor repetition of the lookup logic.
*   **Approach 2** simplifies component access but adds synchronization complexity for the `activeConfig` store.
*   **Approach 3** offers the best encapsulation but adds a service layer, which might be slight overkill for this specific feature unless configuration logic becomes significantly more complex later.

**Recommendation:** Start with **Approach 1** due to its directness and reliance on standard Svelte patterns. If the logic for finding/using the active config becomes cumbersome across many components, refactoring towards Approach 3 could be considered later.

## 5. Next Steps

*   Review the approaches above.
*   Choose a preferred approach.
*   Proceed to create the PRD based on the chosen architecture.