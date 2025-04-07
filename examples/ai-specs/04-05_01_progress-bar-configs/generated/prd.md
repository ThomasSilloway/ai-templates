# Product Requirements Document: Progress Bar Configurations

## 1. Overview

This document outlines the requirements for a new feature in the Twitch App Prototype: **Progress Bar Configurations**. This feature will allow users to define and manage multiple visual styles (text labels, colors) for the main progress bar display. Users will be able to create, update, delete, and select configurations through a new dedicated UI tab.

## 2. Goals

*   Introduce a new "Configs" tab in the main navigation.
*   Allow users to create, read, update, and delete (CRUD) progress bar configurations.
*   Each configuration should store a name, left/right text labels, and left/right colors.
*   Enable users to select an "active" configuration from the `DebugPanel`.
*   Update the main `ProgressBar` and relevant `DebugPanel` elements (buttons, labels) to reflect the active configuration's style.
*   Refactor the underlying point storage (`totalBeardPoints`, `totalShavePoints`) to be generic (`totalLeftSidePoints`, `totalRightSidePoints`) to support different visual themes using the same point totals.
*   Persist configurations and the active selection using `localStorage`.
*   Provide a default "Beard or Shave" configuration.
*   Implement a user-friendly color picker for selecting configuration colors.

## 3. User Stories

*   **As a streamer, I want** to create different visual themes for my progress bar (e.g., "Beard or Shave", "Good vs Evil", "Hydrate vs Caffeine") **so that** I can match the bar's appearance to different stream goals or events.
*   **As a streamer, I want** to easily switch between my saved progress bar configurations **so that** I can quickly change the active theme during a stream via the debug panel.
*   **As a streamer, I want** the configuration settings (name, labels, colors) to be saved **so that** I don't have to recreate them every time I load the application.
*   **As a streamer, I want** a clear interface to manage my configurations (add, edit, delete) **so that** I can keep my themes organized.
*   **As a streamer, I want** an intuitive color picker **so that** I can easily select the exact colors for each side of the progress bar.

## 4. Functional Requirements

### 4.1. Navigation & Tab

*   **FR1.1:** A new tab labeled "Configs" shall be added to the main navigation bar.
*   **FR1.2:** The "Configs" tab shall appear between the "Settings" and "Debug" tabs.
*   **FR1.3:** Clicking the "Configs" tab shall display the configuration management interface.

### 4.2. Configuration Data Structure

*   **FR2.1:** Each configuration object shall contain the following properties:
    *   `id`: string (unique identifier, e.g., UUID)
    *   `name`: string (user-defined name for the configuration)
    *   `leftText`: string (text label for the left side)
    *   `rightText`: string (text label for the right side)
    *   `leftColor`: string (hex color code, e.g., "#FF0000")
    *   `rightColor`: string (hex color code, e.g., "#0000FF")

### 4.3. Configuration Management (Configs Tab UI)

*   **FR3.1:** The "Configs" tab shall display a list of all existing configurations.
*   **FR3.2:** Each configuration in the list shall display its `name` and provide controls for editing and deleting.
*   **FR3.3:** (Create) A button labeled "Add Configuration" shall be present. Clicking it shall add a new, blank configuration entry to the list or open a form/modal for creating one.
*   **FR3.4:** (Update) Each configuration entry shall allow editing of its `name`, `leftText`, `rightText`, `leftColor`, and `rightColor`.
    *   Text fields shall be provided for `name`, `leftText`, `rightText`.
    *   Color inputs (using a color picker component) shall be provided for `leftColor` and `rightColor`. The hex value should also be displayed.
    *   An "Update" or "Save" button shall be present for each configuration to persist changes.
*   **FR3.5:** (Delete) Each configuration entry shall have a "Delete" button. Clicking it shall prompt the user for confirmation before removing the configuration. The default configuration ("Beard or Shave") should ideally not be deletable, or handled gracefully if deleted (e.g., reset to default on next load if none exist).
*   **FR3.6:** (Color Picker) Clicking a color input shall reveal a color picker component (e.g., `svelte-color-picker` or similar) allowing selection via gradient, hue slider, hex input, and potentially pre-defined swatches, similar to the reference image.

### 4.4. Active Configuration Selection (DebugPanel)

*   **FR4.1:** A dropdown menu shall be added to the `DebugPanel` component.
*   **FR4.2:** The dropdown shall be populated with the `name` of all available configurations from the `ConfigService`.
*   **FR4.3:** The dropdown shall display the currently active configuration's name.
*   **FR4.4:** Selecting a different configuration from the dropdown shall update the application's active configuration state via the `ConfigService`.

### 4.5. Progress Bar & DebugPanel Updates

*   **FR5.1:** The `ProgressBar` component shall dynamically display the `leftText` and `rightText` from the currently active configuration.
*   **FR5.2:** The `ProgressBar` component shall dynamically use the `leftColor` and `rightColor` from the active configuration for its visual segments.
*   **FR5.3:** The `DebugPanel` component shall update its labels and button colors to match the active configuration:
    *   Labels displaying point totals should use `leftText`/`rightText` (e.g., "Total [Left Text] Points:").
    *   The "Add Points" buttons should be labeled using `leftText`/`rightText` (e.g., "Add [Left Text] Points") and potentially use `leftColor`/`rightColor` for styling (e.g., background or border).

### 4.6. Point Store Refactoring

*   **FR6.1:** The existing Svelte stores `totalBeardPoints` and `totalShavePoints` shall be renamed to `totalLeftSidePoints` and `totalRightSidePoints`, respectively.
*   **FR6.2:** All references to the old store names throughout the codebase (components, services) shall be updated to use the new generic names.
*   **FR6.3:** The underlying point accumulation logic remains the same; only the presentation changes based on the active configuration.

### 4.7. Default Configuration

*   **FR7.1:** Upon initial load (or if no configurations exist in storage), a default configuration shall be created with the following values:
    *   `id`: (generate a unique ID)
    *   `name`: "Beard or Shave"
    *   `leftText`: "Beard"
    *   `rightText`: "Shave"
    *   `leftColor`: (e.g., "#0000FF" - Blue)
    *   `rightColor`: (e.g., "#FF0000" - Red)
*   **FR7.2:** This default configuration shall be set as the active configuration initially.

## 5. Non-Functional Requirements

*   **NFR1:** (Persistence) All configurations and the ID of the currently active configuration shall be persisted in the browser's `localStorage`. The application state should be restored upon page load/refresh.
*   **NFR2:** (UI/UX) The "Configs" tab UI should follow the application's existing dark theme and general layout principles. The layout of individual configuration editors should closely resemble the provided reference image:
    *   Each configuration editor section should be clearly delineated, potentially with the configuration `name` as a heading.
    *   Input fields for `name`, `leftText`, and `rightText` should be standard text inputs with clear labels positioned above or to the left.
    *   Color inputs for `leftColor` and `rightColor` should include:
        *   A text label (e.g., "Left Color").
        *   A small square color preview swatch showing the currently selected color.
        *   A text input displaying/allowing entry of the hex color code (e.g., "FF0000").
        *   Clicking the swatch or input should reveal/toggle a detailed color picker component.
    *   The color picker component itself (as shown expanded in the image) should offer:
        *   A saturation/brightness selection area (square gradient).
        *   A hue selection slider (vertical rainbow).
        *   A text input for the hex code.
        *   A palette of predefined color swatches (e.g., 8 common colors + 8 grayscale).
    *   An "Update" button should be clearly associated with each configuration editor section.
    *   A "Delete" button should be positioned distinctly for each configuration, perhaps aligned to the top right of its section.
    *   An "Add Configuration" button should be present outside the individual editor sections to allow creating new ones.
*   **NFR3:** (Error Handling) Basic validation should be considered (e.g., preventing empty names). Deleting the active configuration should gracefully select another (e.g., the default or the first in the list).
*   **NFR4:** (Responsiveness) The new tab and components should be reasonably responsive to different screen sizes, consistent with the rest of the application.

## 6. Technical Design Summary (Approach 3)

*   A singleton `ConfigService` will manage configuration state.
*   The service will internally use persisted Svelte stores (`progressBarConfigs: Writable<Config[]>` and `activeConfigId: Writable<string>`).
*   The service will expose methods for CRUD operations (`addConfig`, `updateConfig`, `deleteConfig`, `setActiveConfigId`) and readable stores/methods for accessing data (`getConfigs(): Readable<Config[]>`, `getActiveConfig(): Readable<Config | null>`).
*   Components (`ConfigsTab`, `DebugPanel`, `ProgressBar`) will interact with the `ConfigService` API.
*   Point stores will be refactored (`totalBeardPoints` -> `totalLeftSidePoints`, `totalShavePoints` -> `totalRightSidePoints`).
*   A color picker library (e.g., `svelte-color-picker`) will be integrated.

## 7. Out of Scope

*   Supporting multiple *simultaneously displayed* progress bars.
*   Associating specific point *types* (e.g., bits vs. subs) with different configurations. Points remain generic left/right totals.
*   Advanced validation rules beyond basic presence checks.
*   Import/Export functionality for configurations.