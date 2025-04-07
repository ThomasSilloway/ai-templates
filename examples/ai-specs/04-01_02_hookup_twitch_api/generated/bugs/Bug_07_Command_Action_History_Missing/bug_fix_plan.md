# Bug Fix Plan: Command Action History Missing

## Root Cause
The PointManager.applyQueuedPoints() method updates the points when commands are processed but doesn't create entries in the action history. While other operations (like test points) properly use the actionHistory store, command executions are not being recorded.

## Fix Steps

1. Modify PointManager class:
   - Import the actionHistory store
   - Update applyQueuedPoints() to add command actions to history
   - Add entries when points are applied through commands

2. Changes Required:
   ```typescript
   // Add import
   import { actionHistory } from '../stores/actionHistory';
   
   // Inside applyQueuedPoints method, after updating points:
   if (points > 0) {
     this.updatePoints(points, command === '!beard');
     
     // Add action to history
     actionHistory.addAction({
       type: 'Command',
       points: points,
       target: command === '!beard' ? 'beard' : 'shave',
       timestamp: new Date()
     });
     
     // Clear queued points...
   }
   ```

## Testing Steps
1. Connect to Streamer.bot
2. Use !beard or !shave command
3. Verify:
   - Progress bar updates
   - Action appears in Action History panel
   - Points and target are correct
   - Timestamp is present

## Expected Outcome
- Commands will appear in Action History
- Each entry will show:
  - Type: "Command"
  - Points applied
  - Target (beard/shave)
  - Current timestamp