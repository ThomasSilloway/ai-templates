# Bug Description: Stuck on Settings Page

**Observed Behavior:**
The application consistently displays only the Settings page content. Clicking on other navigation tabs (Progress Bar, Configs, Debug) does not change the displayed content area; it remains showing the Settings UI.

**Expected Behavior:**
Clicking a navigation tab should update the main content area to display the component associated with that tab (e.g., clicking "Debug" should show the Debug Console).

**Feature Context:**
This bug was observed after implementing the "Progress Bar Configurations" feature (v02 in change notes), which involved modifications to `+layout.svelte`, `+page.svelte`, `activeTab` store, and the addition of the `configs` route/page/component.