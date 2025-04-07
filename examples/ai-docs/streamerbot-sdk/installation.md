# Installation

Install using one of the following:

```bash
npm install @streamerbot/client

# or
yarn add @streamerbot/client

# or
pnpm add @streamerbot/client
```

## Usage

Basic usage example:

```ts
import { StreamerbotClient } from '@streamerbot/client'

// Create a new client
const client = new StreamerbotClient({
  host: '127.0.0.1',   // default
  port: 8080,          // default
  endpoint: '/ws',     // default
  password: undefined, // default
})

// Handle events
client.on('Twitch.ChatMessage', (data) => {
  console.log(data)
})

// Connect to Streamer.bot
await client.connect()
```

You can also use events to handle connection state:

```ts
client.subscribe('*')

client.on('connected', () => {
  console.log('Connected!')
})

client.on('disconnected', () => {
  console.log('Disconnected!')
})

client.on('error', (error) => {
  console.error('Error:', error)
})