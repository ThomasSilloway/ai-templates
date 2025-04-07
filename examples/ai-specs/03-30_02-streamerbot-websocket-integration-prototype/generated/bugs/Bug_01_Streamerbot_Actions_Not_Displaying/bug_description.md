# Bug Report: Streamer.bot Actions Not Displaying in DebugConsole

## Description
After successfully connecting to Streamer.bot's websocket server, actions and subactions triggered in Streamer.bot are not appearing in the DebugConsole tab. The connection is confirmed both by the UI status and debug messages, but no action/subaction events are displayed.

## Reproduction Steps
1. Start the Twitch App Prototype
2. Navigate to Settings tab
3. Click Connect button
4. Confirm connection success in UI and debug messages
5. Trigger an action in Streamer.bot
6. Observe DebugConsole tab - no action appears

## Expected Behavior
- When an action is executed in Streamer.bot, a formatted message should appear in DebugConsole:
  `ACTION: <actionname> Args: key1: "value1", key2: "value2"`
- When a subaction is executed, a formatted message should appear prefixed with parent action:
  `[ParentActionName] <subactionname> Args: key1: "value1", key2: "value2"`

## Actual Behavior
- No action or subaction messages appear in DebugConsole
- Connection remains stable with no error messages
- Other debug messages (connection status) appear normally

## Environment
- Twitch App Prototype version: Current development build
- Streamer.bot version: Latest
- Operating System: Windows 10