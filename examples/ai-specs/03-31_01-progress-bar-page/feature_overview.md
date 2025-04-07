Set up an initial prototype for the progress bar tab.

* **Goal:** Create the visual progress bar, establish the core Svelte stores, and display basic debug info alongside the bar within the SvelteKit app.
* **Tasks (SvelteKit App):**
    * Create the `ProgressBar.svelte` component (visuals + props for percentage).
    * Create the core Svelte stores needed:
        * `pointConfiguration` (initially with default values for Bits, Subs, etc.)
        * `totalBeardPoints` (initialize to 0)
        * `totalShavePoints` (initialize to 0)
        * `userPendingPoints` (initialize to empty object `{}`)
    * Use the dedicated ProgressBar tab (e.g., "Beard Progress") to display the `ProgressBar`.
    * Add a "Debug Info" section below the progress bar in this view. Display current values from the stores (`totalBeardPoints`, `totalShavePoints`, calculated percentage, relevant `pointConfiguration` values).
	  * Add button to add points to `totalBeardPoints` and `totalShavePoints` for debug purposes
    * Ensure the `ProgressBar` component updates reactively based on changes in the `totalBeardPoints` and `totalShavePoints` stores.
	* Progress bar should update with cool animation
* **Outcome:** A visual progress bar exists, linked to reactive stores, with a basic debug panel showing initial state (zeros) and buttons.
