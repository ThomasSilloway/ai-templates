# Bug Fix Plan: WebSocket Connection Error in Streamerbot Service

## Root Cause Analysis

The error occurs due to a race condition in the WebSocket connection lifecycle:

1. The `connect()` method in StreamerbotService.ts creates a new StreamerbotClient
2. Before waiting for the connection to be fully established, it immediately tries to set up event subscriptions (line 221)
3. This causes a DOMException because the WebSocket object is not yet ready for use
4. The error propagates through the promise chain, causing the connection attempt to fail

Key issue: Event subscriptions are being configured before the WebSocket connection is fully established and ready.

## Steps to Reproduce

1. Launch the Twitch app prototype
2. Navigate to Settings tab
3. Enter valid Streamer.bot connection details (host: 127.0.0.1, port: 8080)
4. Click "Connect" button
5. Observe error in console: "DOMException: An attempt was made to use an object that is not, or is no longer, usable"

## Proposed Fix

### Code Changes

1. Modify the `connect()` method in StreamerbotService.ts to ensure proper connection lifecycle:

```typescript
async connect(config: ConfigState): Promise<void> {
  try {
    if (this.client) {
      await this.disconnect();
    }

    // Create a promise that resolves when connection is ready
    const connectionPromise = new Promise<void>((resolve, reject) => {
      this.client = new StreamerbotClient({
        host: config.host,
        port: config.port,
        autoReconnect: true,
        onConnect: (data: ConnectData) => {
          this._isConnected = true;
          connection.setConnected(this.client!);
          this.addDebugMessage(`Connected to Streamer.bot ${data.name} v${data.version}`);
          
          // Move subscription setup inside onConnect callback
          try {
            this.setupSubscriptions();
            resolve();
          } catch (error) {
            reject(error);
          }
        },
        onDisconnect: () => {
          this._isConnected = false;
          connection.setDisconnected();
          this.addDebugMessage('Disconnected from Streamer.bot');
          reject(new Error('Disconnected from Streamer.bot'));
        },
        onError: (error: Error) => {
          this._isConnected = false;
          const errorMsg = error instanceof Error ? error.message : String(error);
          connection.setDisconnected(errorMsg);
          this.addDebugMessage(`Streamer.bot Error: ${errorMsg}`);
          reject(error);
        }
      });
    });

    await connectionPromise;
    
  } catch (error) {
    this._isConnected = false;
    const errorMsg = error instanceof Error ? error.message : String(error);
    connection.setDisconnected(errorMsg);
    this.addDebugMessage(`Failed to connect: ${errorMsg}`);
    throw error;
  }
}

// New private method to encapsulate subscription setup
private setupSubscriptions(): void {
  if (!this.client || !this._isConnected) {
    throw new Error('Cannot setup subscriptions - client not connected');
  }

  this.addDebugMessage('Setting up event subscriptions...');
  
  // Configure subscriptions
  this.client.subscribe({
    Raw: ['Action', 'SubAction'],
    Twitch: ['Cheer', 'Sub', 'ReSub', 'GiftSub', 'GiftBomb'],
    Command: ['Triggered']
  });
  
  // Set up event handlers
  this.client.on('Raw.Action', this.handleActionEvent.bind(this));
  this.client.on('Raw.SubAction', this.handleSubActionEvent.bind(this));
  this.client.on('Twitch.Cheer', this.handleCheerEvent.bind(this));
  this.client.on('Twitch.Sub', this.handleSubEvent.bind(this));
  this.client.on('Twitch.ReSub', this.handleResubEvent.bind(this));
  this.client.on('Twitch.GiftSub', this.handleGiftSubEvent.bind(this));
  this.client.on('Twitch.GiftBomb', this.handleGiftBombEvent.bind(this));
  this.client.on('Command.Triggered', this.handleCommandEvent.bind(this));
  
  this.addDebugMessage('Event subscriptions configured');
}
```

### Key Changes:

1. Moved subscription setup into a separate private method for better organization
2. Moved subscription setup inside the onConnect callback to ensure WebSocket is ready
3. Added connection state validation before setting up subscriptions
4. Improved error handling and state management
5. Maintained debug logging for better diagnostics


## Success Criteria

1. WebSocket connection establishes successfully
2. No DOMException errors in console
3. Event subscriptions configured properly
4. Connection status updates correctly
5. Event handlers receive and process events
6. Clean disconnection when requested

## Additional Considerations

1. Add connection timeout handling
2. Implement retry mechanism with backoff
3. Add more detailed logging for debugging
4. Consider adding connection health checks
5. Document error codes and recovery procedures