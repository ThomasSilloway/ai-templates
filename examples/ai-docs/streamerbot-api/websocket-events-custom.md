# Streamer.bot Custom Events

This document outlines how to work with custom events in the Streamer.bot WebSocket server.

## Subscribing to Custom Events

To enable Custom events, send the following Subscribe request:

```json
{
  "request": "Subscribe",
  "id": "my-request-id",
  "events": {
    "General": [
      "Custom"
    ]
  }
}
```

## Broadcasting Custom Events

Custom events can be broadcast using C# methods within Streamer.bot actions. There are two main methods available for broadcasting custom events:

### WebsocketBroadcastString

Sends a custom string to all connected WebSocket clients.

```csharp
public void WebsocketBroadcastString(string data)
```

Example usage:
```csharp
CPH.WebsocketBroadcastString("Hello, world!");
```

### WebsocketBroadcastJson

Sends a custom JSON event to all connected WebSocket clients.

```csharp
public void WebsocketBroadcastJson(string data)
```

Example usage:
```csharp
CPH.WebsocketBroadcastJson("{'key': 'value'}");
```

## Best Practices

1. When broadcasting JSON data, ensure it's properly formatted to avoid parsing errors on the client side.
2. Consider implementing a consistent event structure for your custom events to make handling them easier on the client side.
3. Use meaningful event names and data structures that clearly communicate the purpose of the event.

## Example Implementation

Here's a complete example of broadcasting and handling a custom event:

1. Broadcasting from Streamer.bot:
```csharp
// Inside a Streamer.bot action
CPH.WebsocketBroadcastJson(@"{
    'eventType': 'scoreUpdate',
    'data': {
        'playerName': 'Player1',
        'score': 100,
        'timestamp': '2024-03-30T02:17:00Z'
    }
}");
```

2. Handling in your client application:
```javascript
// Assuming you're using a WebSocket client
ws.addEventListener('message', (event) => {
    const data = JSON.parse(event.data);
    if (data.eventType === 'scoreUpdate') {
        updateScoreDisplay(data.data);
    }
});