# Bug Fix Plan: Streamer.bot Actions Not Displaying

## Issue Identification
From the logs, we can see that:
1. Events are being received successfully
2. Debug messages are showing in the console
3. The formatted action/subaction messages are not appearing

The root cause appears to be incorrect data structure access in the event handlers. The event payload has a nested structure that we're not accessing correctly.

## Current Code Issues
1. Event handlers are trying to access `data.data.args` but the actual field is `data.data.arguments`
2. The data structure has an extra nesting level we need to account for

## Fix Plan
1. Update handleActionEvent to use correct field names:
   - Change `data.data.args` to `data.data.arguments`
   - Update message formatting to use `data.data.name`

2. Update handleSubActionEvent to use correct field names:
   - Change `data.data.args` to `data.data.arguments`
   - Access correct parent name field
   - Update message formatting

## Expected Results
After fixing the data structure access:
1. Action messages should appear as: `ACTION: TestActionForApp Args: isTest: "true", triggerId: "839c529c-ab66-..."` 
2. SubAction messages should appear as: `[TestActionForApp] Log Information (test action) Args: isTest: "true", triggerId: "839c529..."` 

## Implementation Steps
1. Update StreamerbotService.ts event handlers
2. Add validation to ensure data structure exists before access
3. Add more specific error logging if data structure is unexpected