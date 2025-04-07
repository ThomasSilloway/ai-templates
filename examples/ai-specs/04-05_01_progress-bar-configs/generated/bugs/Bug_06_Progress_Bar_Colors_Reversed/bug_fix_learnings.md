# Bug Fix Learnings: Progress Bar Colors Reversed (Bug_06)

## 1. Issue Summary

The progress bar displayed colors opposite to the configuration (e.g., configured Left=Red, Right=Blue showed as Left=Blue, Right=Red).

## 2. Root Cause

The root cause was identified in the CSS implementation within `src/lib/components/ProgressBar.svelte`. The component used CSS variables (`--left-color`, `--right-color`) set based on the configuration. However, the CSS structure applied these variables in a way that caused the visual reversal:
- The container's background (representing the "right" side visually) used `--left-color`.
- The overlay's background (representing the "left" side visually as it fills) used `--right-color`.

## 3. Solution

The fix involved swapping the CSS variable usage within the component's `<style>` block:
- The `.progress-bar-container` background was changed to use `var(--right-color)`.
- The `.progress-bar-overlay` background was changed to use `var(--left-color)`.

## 4. Key Learnings

*   **CSS Structure Matters:** When using visual overlays or complex background layering for effects like progress bars, carefully verify how CSS properties (like `background`) on different elements interact to produce the final visual result.
*   **Variable Naming vs. Application:** Ensure that the application of CSS variables logically matches their intended meaning (e.g., `--left-color` should visually correspond to the left part of the element). A mismatch between the variable name's intent and its CSS application point can lead to confusion and bugs.
*   **Testing Configurations:** When dealing with configurable visual elements, test with different configuration values (especially those that might highlight edge cases or reversals, like distinct left/right colors) to confirm correct behavior.