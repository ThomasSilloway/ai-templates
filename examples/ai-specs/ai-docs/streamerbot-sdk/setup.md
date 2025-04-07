# Setup & Configuration

## Configuration Options

When creating a new StreamerbotClient instance, you can provide configuration options:

```ts
const client = new StreamerbotClient({
  // Connection Options
  host: '127.0.0.1',      // Host to connect to
  port: 8080,             // Port to connect to
  endpoint: '/ws',        // WebSocket endpoint
  password: undefined,    // Password if required
  
  // Behavior Options
  immediate: true,        // Connect immediately on instantiation
  autoReconnect: true,    // Attempt to reconnect on disconnect
  reconnectInterval: 5000 // Time between reconnection attempts (ms)
})
```

## Connection Events

The client emits several events for connection state:

```ts
// Connection succeeded
client.on('connected', () => {
  console.log('Connected to Streamer.bot!')
})

// Connection closed
client.on('disconnected', () => {
  console.log('Disconnected from Streamer.bot')
})

// Connection error occurred
client.on('error', (error) => {
  console.error('Error:', error)
})
```

## Connection Methods

```ts
// Manual connection
await client.connect()

// Manual disconnection
await client.disconnect()

// Check connection state
const isConnected = client.connected

// Get current state
const state = client.state // 'connected' | 'connecting' | 'disconnected'
```

## Event Subscription

You must subscribe to events to receive them:

```ts
// Subscribe to all events
client.subscribe('*')

// Subscribe to specific events
client.subscribe({
  Twitch: ['Follow', 'Sub', 'ChatMessage'],
  YouTube: ['SuperChat']
})

// Unsubscribe from events
client.unsubscribe({
  Twitch: ['ChatMessage']
})