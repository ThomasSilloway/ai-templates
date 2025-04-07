# Configuration

## Options

The StreamerbotClient constructor accepts a configuration object with the following options:

```ts
interface StreamerbotClientConfig {
  // Connection Options
  host?: string            // Host to connect to (default: '127.0.0.1')
  port?: number           // Port to connect to (default: 8080)
  endpoint?: string       // WebSocket endpoint (default: '/ws')
  password?: string      // Password if required (default: undefined)
  
  // Behavior Options
  immediate?: boolean     // Connect immediately on instantiation (default: true)
  autoReconnect?: boolean // Attempt to reconnect on disconnect (default: true)
  reconnectInterval?: number // Time between reconnection attempts (ms) (default: 5000)
}
```

## Default Configuration

If no configuration is provided, these defaults are used:

```ts
const defaultConfig = {
  host: '127.0.0.1',
  port: 8080,
  endpoint: '/ws',
  password: undefined,
  immediate: true,
  autoReconnect: true,
  reconnectInterval: 5000
}
```

## Event Handlers

### Connection State

```ts
// Import
import { StreamerbotClient } from '@streamerbot/client'

// Create client
const client = new StreamerbotClient()

// Add event handlers
client.on('connected', () => {
  console.log('Connected!')
})

client.on('disconnected', () => {
  console.log('Disconnected!')
})

client.on('error', (error) => {
  console.error('Error:', error)
})
```

### Example with Full Configuration

```ts
const client = new StreamerbotClient({
  // Connection
  host: 'localhost',
  port: 8080,
  endpoint: '/ws',
  password: 'your-password',

  // Behavior
  immediate: true,       // Connect immediately
  autoReconnect: true,   // Auto reconnect on disconnect
  reconnectInterval: 5000 // Retry every 5 seconds
})

// Subscribe to all events
client.subscribe('*')

// Handle connection events
client.on('connected', () => {
  console.log('Connected to Streamer.bot!')
})

client.on('disconnected', () => {
  console.log('Disconnected from Streamer.bot')
})

client.on('error', (error) => {
  console.error('Streamer.bot Error:', error)
})