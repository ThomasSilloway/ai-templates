# Bug Fix Plan

## Overview
We need to update our types and code to use the correct property name for the user's display name in command events.

## Fix Steps

### 1. Update TwitchUser Interface
```typescript
// Update interface to match actual event structure
export interface TwitchUser {
  id: string;
  login: string;
  display: string;  // Changed from display_name to display
  subscribed: boolean;
  role: number;
}
```

### 2. Update Command Event Handler
```typescript
// Update handler to use correct property name
private handleCommandEvent(data: CommandPayload) {
  try {
    const { command, user } = data.data;
    this.addDebugMessage(`COMMAND EVENT DATA: ${JSON.stringify(data)}`);
    this.addDebugMessage(`COMMAND: ${user.display} used ${command}`);  // Changed from display_name to display
    this.pointManager.applyQueuedPoints(user.id, command);
  } catch (error) {
    this.addDebugMessage(`ERROR: Failed to process command event: ${error}`);
  }
}
```

## Verification Plan
1. Test command event handling by issuing a test command
2. Verify debug console shows correct username in command log
3. Verify command handling and point application still work correctly
4. Ensure TypeScript doesn't show any type errors

## Implementation Notes
- This is a straightforward property name change
- The core functionality is working, we just need to fix the debug output
- No changes needed to point calculation or application logic