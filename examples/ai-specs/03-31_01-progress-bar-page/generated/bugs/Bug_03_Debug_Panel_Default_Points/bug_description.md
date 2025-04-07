# Bug Description

## Issue
The default Test Points value in the Debug Panel remains at 100 instead of the updated default value of 500 when refreshing the page.

## Location
File: `twitch-app-prototype/src/lib/components/DebugPanel.svelte`
Line: 6
Code: `let testPoints = 100;`

## Expected Behavior
- The Test Points input in the Debug Panel should default to 500 points when the page is loaded/refreshed
- This aligns with other default point values in the system (seen in progress.ts store where bits and sub points default to 500)

## Actual Behavior
- The Test Points input defaults to 100 points when the page is loaded/refreshed
- This creates inconsistency with the rest of the point system which uses 500 as the default

## Impact
- Users testing the system with the Debug Panel get inconsistent point values compared to the actual point system
- Makes testing less efficient as users need to manually change the value to 500 for accurate testing
- Could lead to confusion when testing different point scenarios

## Context
This bug appears to be a remnant from before the v04 update which increased default points from 100 to 500 (as noted in change_notes.md). While the point configuration store was updated, this local variable initialization was missed.