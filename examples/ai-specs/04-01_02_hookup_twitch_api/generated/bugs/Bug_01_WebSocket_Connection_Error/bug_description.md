# Bug Report: WebSocket Connection Error in Streamerbot Service

## Error Details
A WebSocket connection error occurs when attempting to establish a connection with Streamer.bot, resulting in a DOMException indicating an attempt to use an unusable object.

### Error Message
```
Uncaught (in promise) DOMException: An attempt was made to use an object that is not, or is no longer, usable
```

### Stack Trace
```
    send index.js:782
    response index.js:811
    request index.js:795
    subscribe index.js:898
    connectionPromise StreamerbotService.ts:221
    connect StreamerbotService.ts:194
    handleConnect SettingsTab.svelte:18
```

## Steps to Reproduce
1. Launch the Twitch app prototype
2. Navigate to the Settings tab
3. Attempt to connect to Streamer.bot using valid host/port configuration
4. Observe the connection error in the console

## Expected Behavior
- The application should establish a WebSocket connection with Streamer.bot
- The connection status should update to "Connected"
- Event subscriptions should be registered successfully

## Actual Behavior
- The WebSocket connection fails to establish
- A DOMException is thrown indicating the WebSocket object is unusable
- The connection attempt fails and triggers the onError handler
- The connection status remains in a disconnected state

## Impact
- Users cannot establish connection with Streamer.bot
- Core functionality depending on Streamer.bot integration is unavailable
- Event subscriptions for Twitch events (cheers, subs, etc.) cannot be established
- Points management system is non-functional due to lack of event data

## Environment Details
- Application: Twitch App Prototype
- Component: StreamerbotService
- Browser: Any (WebSocket API)
- Streamer.bot Integration: @streamerbot/client library