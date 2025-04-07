# Bug Fix Plan

## Overview
The bug stems from mismatches between our TypeScript interfaces and the actual event data structures received from Streamer.bot. We need to update both our interfaces and the code that handles these events.

## Fix Steps

### 1. Update TwitchGiftSubData Interface
```typescript
// Update interface to match actual event structure
interface TwitchGiftSubData {
  user: {  // Changed from gifter to user
    id: string;
    login: string;
    name: string;
    type: string;
    // ... other user properties
  };
  durationMonths: number;
  subTier: string;  // Changed from tier
  // ... other properties
}
```

### 2. Update TwitchCheerData Interface
```typescript
// Update interface to match actual event structure
interface TwitchCheerData {
  bits: number;
  message: {
    message: string;
    // ... other message properties
  };
  user: {
    id: string;
    login: string;
    name: string;
    // ... other user properties
  };
}
```

### 3. Update Gift Sub Event Handler
```typescript
// Update handler to use correct property paths
private handleGiftSubEvent(rawData: StreamerbotEventPayload<'Twitch.GiftSub'>) {
  const data = rawData.data as unknown as TwitchGiftSubData;
  // Use user instead of gifter
  const { user, subTier } = data;
  // Update log message and point handling
  this.addDebugMessage(`GIFT SUB: ${user.name} gifted a sub with tier ${subTier}`);
  this.pointManager.handleSubscription(subTier, user.id);
}
```

### 4. Update Cheer Event Handler
```typescript
// Update handler to use correct property paths
private handleCheerEvent(rawData: StreamerbotEventPayload<'Twitch.Cheer'>) {
  const data = rawData.data as unknown as TwitchCheerData;
  const { bits, message, user } = data;
  // Access nested message text and use user properties
  this.addDebugMessage(`CHEER: ${user.name} cheered ${bits} bits with message: ${message.message}`);
  this.pointManager.handleBitsCheer(bits, message.message, user.id);
}
```

## Verification Plan
1. Test gift sub event handling by triggering a test gift sub
2. Test bits/cheer event handling by triggering a test cheer
3. Verify debug console shows correct event processing without errors
4. Verify points are properly allocated for both event types

## Implementation Notes
- The changes primarily involve updating our type definitions and adjusting property access paths
- No changes to the underlying point calculation logic are needed
- We'll maintain all existing debug logging to help verify the changes