# Polish: Timestamp Formatting

## Current Behavior
Timestamps are displayed in full ISO format: [2025-03-30T08:00:19.823Z]

## Desired Behavior
Timestamps should show only time portion: [08:00:19.823]

## Implementation Options
1. **Modify addDebugMessage in StreamerbotService.ts**:
   - Change timestamp generation to use new Date().toLocaleTimeString()
   - Pros: Simple change in one place
   - Cons: Less control over exact format

2. **Update messages store**:
   - Modify the store to transform timestamps on add
   - Pros: Centralized formatting
   - Cons: Requires store changes

3. **Format in DebugConsole.svelte**:
   - Transform timestamp during display
   - Pros: Keeps raw data intact
   - Cons: Requires view layer changes

## Recommended Approach
Option 1 - Modify addDebugMessage to use:
```ts
new Date().toLocaleTimeString() + '.' + Date.now() % 1000
```
This gives us consistent formatting while being performant.