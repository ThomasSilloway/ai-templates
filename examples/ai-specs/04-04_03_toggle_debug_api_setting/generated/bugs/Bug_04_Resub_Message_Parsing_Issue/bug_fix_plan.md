# Bug Fix Plan: Resub Message Parsing Issue

## Steps to Fix

1. Examine and update the types in twitch.ts to properly handle the Resub event structure:
   - Add proper typing for the `text` field in the Resub event
   - Add proper typing for the `parts` array structure
   - Ensure the user object structure matches the incoming data

2. Update the event handling logic:
   - Add parsing for the message text in Resub events
   - Extract command (!shave) from the text field
   - Process the command similar to regular chat commands

3. Add debug logging:
   - Log the parsed command from Resub events
   - Log when a command is detected in a Resub event
   - Log if the command processing succeeds or fails

4. Test cases:
   - Test with Resub event containing !shave command
   - Verify command is extracted correctly
   - Verify command triggers appropriate action
   - Check debug logs show proper parsing

## Files to Modify
- twitch.ts - Update type definitions
- relevant event handler file for Resub events