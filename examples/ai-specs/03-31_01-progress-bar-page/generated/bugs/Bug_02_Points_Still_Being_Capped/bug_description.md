# Point Limit Cap Bug

## Description
The point system is incorrectly maintaining a 5000-point cap despite recent changes (v04) that removed this limitation. The points should now use proportional calculations without fixed limits, but the implementation is still enforcing the old cap.

## Location
File: `twitch-app-prototype/src/lib/components/DebugPanel.svelte`

## Specific Issue
Two instances of point capping are present in the debug panel code:

1. Line 9: 
```typescript
totalBeardPoints.update(n => Math.min(n + testPoints, $pointConfiguration.defaultTarget));
```

2. Line 19:
```typescript
totalShavePoints.update(n => Math.min(n + testPoints, $pointConfiguration.defaultTarget));
```

These lines are explicitly capping the points at `defaultTarget` (5000) using Math.min(), which contradicts the v04 changes that removed point limits.

## Impact
- Users cannot accumulate more than 5000 points on either side
- The proportional calculation system is not working as intended
- The balance between beard and shave points is artificially constrained
- The true point ratio between sides cannot be accurately represented

## Current Behavior
- Points are capped at 5000 for both beard and shave
- Adding points beyond 5000 has no effect
- The progress bar cannot show the true balance when points exceed the cap

## Expected Behavior
- Points should accumulate without any upper limit
- The progress bar should show the true proportional balance between sides
- The point total should increase indefinitely as users add more points