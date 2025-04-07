# Bug Fix Plan: Progress Bar Colors Reversed (Bug_06)

## 1. Problem Analysis

The investigation revealed that the progress bar colors are reversed due to how the CSS variables are applied in `src/lib/components/ProgressBar.svelte`.

- The main container (`div.progress-bar-container`) has its background set using the `--left-color` CSS variable.
- The overlay element (`div.progress-bar-overlay`), which visually represents the progress and grows from left to right, has its background set using the `--right-color` CSS variable.

This causes the `--right-color` to appear on the left side of the bar as the overlay fills, and the `--left-color` to appear on the right side (the remaining background of the container). This is the inverse of the intended display based on the configuration names (`leftColor`, `rightColor`).

## 2. Proposed Solution

The fix involves swapping the CSS variable assignments in the CSS rules within `src/lib/components/ProgressBar.svelte`.

- **Modify CSS Rule for `.progress-bar-container` (approx. line 91):**
    - Change `background: var(--left-color, #1E88E5);`
    - To: `background: var(--right-color, #f44336);` /* Use right color for the base background */

- **Modify CSS Rule for `.progress-bar-overlay` (approx. line 118):**
    - Change `background: var(--right-color, #f44336);`
    - To: `background: var(--left-color, #1E88E5);` /* Use left color for the overlay */

This change will ensure that the overlay element, which represents the "left" side's progress visually, uses the `leftColor` from the configuration, and the remaining background represents the "right" side using the `rightColor`.

## 3. Implementation Steps (Pseudo Code)

1.  Open `src/lib/components/ProgressBar.svelte`.
2.  Locate the CSS rule for `.progress-bar-container`.
3.  Update the `background` property to use the `--right-color` variable.
4.  Locate the CSS rule for `.progress-bar-overlay`.
5.  Update the `background` property to use the `--left-color` variable.
6.  Save the file.

## 4. Testing

- After applying the fix, load the application.
- Select a configuration (e.g., the default "Beard or Shave" with Left=Blue, Right=Red, or the user-reported config Left=Red, Right=Blue).
- Verify that the colors displayed on the progress bar match the configuration: the color defined as `leftColor` should appear on the left, and `rightColor` on the right.
- Test adding points to ensure the bar fills correctly with the intended colors.