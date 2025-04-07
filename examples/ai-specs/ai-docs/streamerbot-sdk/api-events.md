# API Events Documentation

## Connection Events

Connection events are handled through specific methods rather than .on():

```ts
import { StreamerbotClient } from '@streamerbot/client'

const client = new StreamerbotClient()

// Handle connection event
client.onConnect((data) => {
  console.log('Connected!')
})

// Handle disconnect event
client.onDisconnect(() => {
  console.log('Disconnected!')
})

// Handle errors
client.onError((error) => {
  console.error('Error:', error)
})
```

## Event Types

The client provides type-safe event handling through TypeScript types:

```ts
import { StreamerbotClient, StreamerbotEventPayload } from '@streamerbot/client'

// Type-safe event handler
client.on('Raw.Action', (data: StreamerbotEventPayload<'Raw.Action'>) => {
  console.log(data)
})

// Type for Raw.Action event
interface RawActionPayload {
  source: {
    type: 'Raw'
    event: 'Action'
  }
  data: {
    id: string
    name: string
    args: Record<string, unknown>
    user: {
      id: number
      login: string
      displayName: string
      subscribed: boolean
      role: number
    }
  }
}

// Type for Raw.SubAction event
interface RawSubActionPayload {
  source: {
    type: 'Raw'
    event: 'SubAction'
  }
  data: {
    parentId: string
    parentName: string
    type: number
    id: string
    name: string
    args: Record<string, unknown>
    user: {
      id: number
      login: string
      displayName: string
      subscribed: boolean
      role: number
    }
  }
}
```

## Connection State

The client provides connection state through properties:

```ts
// Check if connected
if (client.state === 'connected') {
  // Do something
}

// Possible states: 'connected' | 'connecting' | 'disconnected'