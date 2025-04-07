# Feature Requirements: Twitch Integration for Progress Bar

## Overview
Integrate Twitch bits, subscriptions, and other monetary events with the existing progress bar system, including support for queued points when no command is specified.

## Current System Analysis
1. **Point Configuration**
   - Already implemented in `pointConfiguration` store
   - Supports configurable values for:
     - Bits (per 100)
     - Subscriptions (base points)
     - Tier 2/3 multipliers
     - Gift bomb bonus
     - Resub multiplier and streak bonus

2. **Progress System**
   - Uses `totalBeardPoints` and `totalShavePoints` stores
   - `userPendingPoints` store exists for queuing points

3. **Event System**
   - Currently only subscribing to `Raw.Action` and `Raw.SubAction`
   - Need to update to subscribe to Twitch-specific events

## Required Changes

### 1. Event Subscription Updates
- Update StreamerbotService to subscribe to Twitch events:
  ```typescript
  this.client.subscribe({
    Twitch: [
      'Cheer',
      'Sub',
      'Resub',
      'GiftSub',
      'GiftBomb'
    ]
  });
  ```

### 2. Event Handlers
- Add handlers for each Twitch event type:
  - Cheer: Convert bits to points
  - Sub: Apply appropriate tier multipliers
  - Resub: Apply resub multiplier and streak bonus
  - GiftSub: Award points to gifter
  - GiftBomb: Apply gift bomb bonus

### 3. Point Queue System
- Utilize existing `userPendingPoints` store
- Queue points when no command is present
- Apply all queued points when user uses command
- Log point applications through DebugPanel

### 4. Command Integration
- Enhance !beard and !shave commands to:
  - Check for queued points
  - Apply any pending points
  - Update progress bar
  - Log point application in debug panel

## Technical Details

### Required Store Updates
- No new stores needed, existing stores sufficient:
  - `pointConfiguration` for settings
  - `userPendingPoints` for queue
  - `totalBeardPoints`/`totalShavePoints` for progress

### Event Handler Implementation
```typescript
// Example structure for event handlers
private handleCheerEvent(data: TwitchCheerPayload) {
  const points = calculateBitsPoints(data.message.bits);
  if (hasCommand(data.message.message)) {
    applyPointsToProgress(points, command);
  } else {
    queuePointsForUser(data.message.userId, points);
  }
}
```

## Integration Points
1. StreamerbotService.ts
   - Add Twitch event subscriptions
   - Implement event handlers
   
2. DebugPanel.svelte
   - Use existing logging system for point updates

3. Command Processing
   - Enhance command handlers to check/apply queued points

## Testing Requirements
1. Verify point calculations for:
   - Different bit amounts
   - Sub tiers
   - Gift subs and bombs
   - Resub multipliers

2. Test queue system:
   - Points queue correctly
   - All points apply on command
   - Queue persists between sessions

## Success Criteria
1. Points are correctly calculated and applied for all Twitch events
2. Points queue properly when no command is present
3. Queued points are correctly applied when commands are used
4. Debug panel shows all point transactions
5. All existing functionality remains working