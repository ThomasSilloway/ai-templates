# Bug Report: Disconnect Button Hanging

## Description
When clicking the disconnect button in the Settings tab, the disconnect operation appears to hang. The UI does not update to reflect disconnection until the page is manually refreshed.

## Reproduction Steps
1. Start the Twitch App Prototype
2. Navigate to Settings tab
3. Connect to Streamer.bot (verify successful connection)
4. Click the Disconnect button
5. Observe that:
   - Button appears to do nothing
   - Connection status doesn't update
   - App remains in "connected" state
6. Refresh the page
7. Only after refresh does the UI show disconnected state

## Expected Behavior
- Clicking Disconnect should immediately:
  1. Close the WebSocket connection
  2. Update the connection status to "Disconnected"
  3. Enable the Connect button
  4. Show appropriate status indicators
  5. All changes should be visible without page refresh

## Actual Behavior
- Disconnect button appears unresponsive
- Connection status remains as "Connected"
- UI state doesn't update
- Changes only visible after manual page refresh
- Disconnect operation appears to be hanging or not completing properly

## Environment
- Twitch App Prototype version: Current development build
- Streamer.bot version: Latest
- Operating System: Windows 10
- Browser: Chrome

## Impact
This bug affects the core functionality of the WebSocket connection management, making it difficult for users to reliably disconnect from Streamer.bot.