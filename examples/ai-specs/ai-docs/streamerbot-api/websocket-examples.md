# Streamer.bot WebSocket Examples

This document provides example code for interacting with the Streamer.bot WebSocket server using JavaScript.

> **Note**: For JavaScript or TypeScript projects, it's recommended to use the official Streamer.bot Client library for easier integration.

## Basic Usage

### Connecting to the Server

The Streamer.bot Client will automatically connect to the default WebSocket server address (127.0.0.1:8080):

```javascript
const client = new StreamerbotClient();
```

### Executing Actions

You can execute actions using their unique ID:

```javascript
// Execute a specific action by ID
const response = await client.doAction("9c6203fd-363f-4834-983e-b10423c568ea");

// Execute an action with arguments
const response = await client.doAction("9c6203fd-363f-4834-983e-b10423c568ea", {
  message: "Hello World",
  count: 42
});
```

## Event Handling

### Subscribing to Events

You can subscribe to specific events and handle them using event handlers:

```javascript
// Subscribe to Twitch Chat messages
client.on('Twitch.ChatMessage', (data) => {
  console.log('Twitch Chat:', data);
});

// Subscribe to Channel Point Redemptions
client.on('Twitch.Redemption', (data) => {
  console.log('Channel Points Redeemed:', data);
});

// Subscribe to Follow events
client.on('Twitch.Follow', (data) => {
  console.log('New Follower:', data);
});
```

## Complete Example

Here's a complete example showing how to set up a connection and handle multiple event types:

```javascript
const StreamerbotClient = require('@streamerbot/client');

// Create and connect the client
const client = new StreamerbotClient();

// Handle connection events
client.on('connected', () => {
  console.log('Connected to Streamer.bot!');
  
  // Subscribe to events after connection
  client.subscribe('Twitch.Follow');
  client.subscribe('Twitch.ChatMessage');
  client.subscribe('Twitch.Redemption');
});

client.on('disconnected', () => {
  console.log('Disconnected from Streamer.bot');
});

// Handle specific events
client.on('Twitch.ChatMessage', (data) => {
  const { message, user } = data;
  console.log(`${user.displayName}: ${message}`);
  
  // Example: Respond to commands
  if (message.startsWith('!hello')) {
    client.doAction('send-greeting', {
      username: user.displayName
    });
  }
});

client.on('Twitch.Follow', (data) => {
  console.log(`New follower: ${data.displayName}`);
  
  // Example: Trigger a follow alert
  client.doAction('trigger-follow-alert', {
    follower: data.displayName
  });
});

client.on('Twitch.Redemption', (data) => {
  console.log(`${data.displayName} redeemed ${data.title}`);
  
  // Example: Handle specific rewards
  if (data.title === 'Highlight Message') {
    client.doAction('highlight-message', {
      message: data.message,
      user: data.displayName
    });
  }
});

// Error handling
client.on('error', (error) => {
  console.error('WebSocket Error:', error);
});
```

## Best Practices

1. **Connection Management**
   - Always handle both connection and disconnection events
   - Implement reconnection logic for robustness
   - Subscribe to events after confirming connection

2. **Error Handling**
   - Implement error handlers for both WebSocket and action execution errors
   - Log errors appropriately for debugging
   - Consider implementing retry logic for failed actions

3. **Event Handling**
   - Keep event handlers focused and modular
   - Consider implementing rate limiting for action execution
   - Use async/await for better flow control with actions

4. **Security**
   - Validate all user input before executing actions
   - Implement appropriate access controls
   - Be careful with sensitive information in logs

5. **Performance**
   - Only subscribe to events you need
   - Clean up event listeners when no longer needed
   - Consider batching actions if performing multiple operations