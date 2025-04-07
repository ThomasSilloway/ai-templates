# Streamer.bot WebSocket Events

This document outlines all events emitted by the Streamer.bot WebSocket Server.

> **Important**: Events are only emitted if they have been subscribed to.

## Event Schema

All events are sent from the server in stringified JSON format. Event payloads follow this base schema:

```json
{
  "timeStamp": "Date", // ISO 8601 DateTime
  "event": {
    "source": "string",
    "type": "string"
  },
  "data": {
    // Data specific to the event type
  }
}
```

## Event Categories

The WebSocket server emits different types of events:

1. Command Events - Events related to chat commands
2. Custom Events - User-defined custom events
3. Raw Events - Low-level system events
4. Twitch Events - Events specific to Twitch integration
5. Application Events - Events related to the Streamer.bot application itself

Each category of events has its own specific event types and data structures. See the respective documentation files for detailed information about each category:

- [Command Events](./websocket-events-command.md)
- [Custom Events](./websocket-events-custom.md)
- [Raw Events](./websocket-events-raw.md)
- [Twitch Events](./websocket-events-twitch.md)