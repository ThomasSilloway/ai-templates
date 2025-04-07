# Product Requirements Document: Twitch Points Integration

## Overview
Integrate Twitch monetary events (bits, subscriptions) with the existing progress bar system by extending the StreamerbotService to handle Twitch-specific events and manage point allocation through the existing stores.

## Product Goals
1. Automatically process Twitch events and award points based on configured values
2. Queue points when no command is present
3. Apply queued points when users execute commands
4. Show pending points in the DebugPanel
5. Log all events and calculations in DebugConsole

## Current System Analysis
- ProgressBarContainer.svelte: Contains DebugPanel for progress bar specific info
- DebugConsole.svelte: Handles text logging for events
- StreamerbotService: Currently subscribes to Raw.Action and Raw.SubAction
- Progress Store: Already has point configuration and queue system

## Features & Requirements

### 1. Event Integration
#### Functional Requirements
- Subscribe to both Twitch and Command events
```typescript
// Event subscriptions
this.client.subscribe({
  Twitch: ['Cheer', 'Sub', 'Resub', 'GiftSub', 'GiftBomb'],
  Command: ['Triggered']
});
```

#### Command Processing
- Subscribe to Command.Triggered events for !beard and !shave commands
- Parse commands from chat messages in Twitch events
- Command event structure:
```json
{
  "command": "!beard",
  "message": "",
  "user": {
    "id": "user_id",
    "login": "username",
    "display_name": "Display Name",
    "subscribed": true,
    "role": 1
  }
}
```

### 2. Point Queue System
#### Functional Requirements
- Store points in queue when no command is present
- Maintain queue between sessions
- Apply all queued points when user executes command
- Clear queue after points are applied

### 3. Debug Integration
#### DebugPanel (ProgressBarContainer.svelte)
- Add new section for pending points display
- Show user list with queued point totals
- Update in real-time as points are queued/applied
- Layout: Add container to right of action history

#### DebugConsole
- Log all point calculations
- Log queue updates
- Log command processing
- Keep existing message format

### 4. UI Updates
#### Pending Points Display
```typescript
// Example pending points display structure
interface PendingPointsDisplay {
  userId: string;
  username: string;
  pendingPoints: number;
  lastUpdated: Date;
}
```

## Technical Details

### 1. StreamerbotService Updates
```typescript
class StreamerbotService {
  private async setupSubscriptions() {
    this.client.subscribe({
      Twitch: ['Cheer', 'Sub', 'Resub', 'GiftSub', 'GiftBomb'],
      Command: ['Triggered'],
      Raw: ['Action', 'SubAction']
    });
  }

  private handleCheerEvent(data: TwitchCheerPayload) {
    const points = calculateBitsPoints(data.message.bits);
    if (hasCommand(data.message.message)) {
      applyPointsToProgress(points, command);
    } else {
      queuePointsForUser(data.message.userId, points);
    }
  }

  private handleCommandEvent(data: CommandTriggeredPayload) {
    if (data.command === '!beard' || data.command === '!shave') {
      applyQueuedPoints(data.user.id, data.command);
    }
  }
}
```

### 2. Debug Panel Updates
```svelte
<!-- In DebugPanel.svelte -->
<div class="debug-section">
  <div class="action-history">
    <!-- Existing action history -->
  </div>
  <div class="pending-points">
    <h3>Pending Points</h3>
    {#each pendingPointsList as pending}
      <div class="pending-row">
        <span class="username">{pending.username}</span>
        <span class="points">{pending.pendingPoints}</span>
      </div>
    {/each}
  </div>
</div>
```

## Testing Requirements
- Unit tests for point calculations
  - Bit conversion
  - Subscription tiers
  - Gift sub bonuses
  - Resub multipliers

## Implementation Plan

### Phase 1: Event System
1. Update StreamerbotService subscriptions
2. Implement Twitch event handlers
3. Add Command event processing
4. Implement DebugConsole logging

### Phase 2: Debug Updates
1. Add pending points display to DebugPanel

### Phase 3: Integration
1. Connect event handlers to stores
2. Test with sample events

## Success Metrics
1. All Twitch events correctly processed
2. Points queue working reliably
3. Commands properly applying queued points
4. Debug displays updating correctly
5. Smooth user experience

## Dependencies
- Existing StreamerbotService
- Point configuration system
- DebugPanel and DebugConsole
- Progress bar system