# Bug Fix Plan: Remove Point Capping

## Overview
Remove the point capping logic from the debug panel to allow unlimited point accumulation, aligning with v04 changes for proportional calculations.

## Implementation Steps

### 1. Modify Point Addition Logic
- Location: `twitch-app-prototype/src/lib/components/DebugPanel.svelte`
- Changes needed:
  ```typescript
  // Change from:
  totalBeardPoints.update(n => Math.min(n + testPoints, $pointConfiguration.defaultTarget));
  // To:
  totalBeardPoints.update(n => n + testPoints);

  // And:
  totalShavePoints.update(n => Math.min(n + testPoints, $pointConfiguration.defaultTarget));
  // To:
  totalShavePoints.update(n => n + testPoints);
  ```

### 2. Update Input Validation
- Remove the `max` attribute from the test points input field
- The input should still maintain minimum of 0 for logical consistency
```html
<input
  type="number"
  id="testPoints"
  bind:value={testPoints}
  min="0"
/>
```

### 3. Add Debug Logging
Add console logging to track point updates:
```typescript
function addBeardPoints() {
  const newPoints = $totalBeardPoints + testPoints;
  totalBeardPoints.update(n => n + testPoints);
  console.log(`Debug: Added ${testPoints} beard points. New total: ${newPoints}`);
  // ... rest of the function
}

function addShavePoints() {
  const newPoints = $totalShavePoints + testPoints;
  totalShavePoints.update(n => n + testPoints);
  console.log(`Debug: Added ${testPoints} shave points. New total: ${newPoints}`);
  // ... rest of the function
}