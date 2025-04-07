# Streamer.bot WebSocket Requests

This document outlines all requests that can be made to the Streamer.bot WebSocket Server.

## Base Request Format

All requests and responses follow this base schema:

```json
{
  "request": "<request>",
  "id": "<id>"
}
```

The `id` can be any string value and is used to identify request/response pairs.

## Available Requests

### Subscribe

Subscribes to events from the Streamer.bot instance. Events are not sent unless subscribed to.

**Note**: If using the @streamerbot/client library, subscriptions are automatically added when using the `.on()` event handler.

```json
{
  "request": "Subscribe",
  "id": "<id>",
  "events": {
    "<event category>": [
      "<event name>",
      "<event name>",
      "..."
    ]
  }
}
```

### UnSubscribe

Unsubscribes from currently subscribed events.

```json
{
  "request": "UnSubscribe",
  "id": "<id>",
  "events": {
    "<event category>": [
      "<event name>",
      "<event name>",
      "..."
    ]
  }
}
```

### GetEvents

Fetches a list of all subscribable events from the connected instance.

```json
{
  "request": "GetEvents",
  "id": "<id>"
}
```

### GetActions

Retrieves a list of all actions in the connected instance.

```json
{
  "request": "GetActions",
  "id": "<id>"
}
```

### DoAction

Executes an action on the connected instance.

```json
{
  "request": "DoAction",
  "action": {
    "id": "<guid>",
    "name": "<name>"
  },
  "args": {
    "key": "value"
  },
  "id": "<id>"
}
```

### GetBroadcaster

Fetches information about the connected broadcaster account(s).

```json
{
  "request": "GetBroadcaster",
  "id": "<id>"
}
```

### Credits System Requests

#### GetCredits
Fetches current credits system data.
```json
{
  "request": "GetCredits",
  "id": "<id>"
}
```

#### TestCredits
Fills credits system with test data.
```json
{
  "request": "TestCredits",
  "id": "<id>"
}
```

#### ClearCredits
Resets the current credits system data.
```json
{
  "request": "ClearCredits",
  "id": "<id>"
}
```

### GetInfo

Retrieves information about the connected Streamer.bot instance.

```json
{
  "request": "GetInfo",
  "id": "<id>"
}
```

### GetActiveViewers

Fetches a list of all active viewers for connected Twitch or YouTube accounts.

```json
{
  "request": "GetActiveViewers",
  "id": "<id>"
}