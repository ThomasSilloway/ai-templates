# Events

## Overview

The Streamer.bot Client SDK provides a powerful event system that allows you to subscribe to and handle various events from Streamer.bot.

## Event Categories

Events are organized into categories:

- `Raw` - Raw action and sub-action events
- `General` - General application events
- `Twitch` - Twitch-specific events
- `YouTube` - YouTube-specific events
- etc.

## Raw Events

Raw events provide direct access to action and sub-action execution:

```ts
// Subscribe to Raw events
client.subscribe({
  Raw: ['Action', 'SubAction']
})

// Handle Action events
client.on('Raw.Action', (data) => {
  console.log('Action executed:', data.name)
  console.log('Arguments:', data.arguments)
})

// Handle SubAction events
client.on('Raw.SubAction', (data) => {
  console.log('SubAction executed:', data.name)
  console.log('Parent Action:', data.parentName)
  console.log('Arguments:', data.arguments)
})
```

## Event Types

### Action Event
```ts
interface ActionEvent {
  id: string;         // Unique identifier
  name: string;       // Action name
  arguments: {        // Action arguments
    [key: string]: any;
  };
  user: {            // User who triggered the action
    id: number;
    login: string;
    display_name: string;
    subscribed: boolean;
    role: number;    // 1: Viewer, 2: VIP, 3: Moderator, 4: Broadcaster
  };
}
```

### SubAction Event
```ts
interface SubActionEvent {
  parentId: string;   // Parent action ID
  parentName: string; // Parent action name
  type: number;       // SubAction type
  id: string;         // Unique identifier
  name: string;       // SubAction name
  arguments: {        // SubAction arguments
    [key: string]: any;
  };
  user: {            // User who triggered the parent action
    id: number;
    login: string;
    display_name: string;
    subscribed: boolean;
    role: number;
  };
}
```

## Connection Events

The client emits special events for connection state changes:

```ts
// Connection established
client.on('connected', () => {
  // Connection is ready
})

// Connection closed
client.on('disconnected', () => {
  // Handle disconnection
})

// Connection error
client.on('error', (error) => {
  // Handle error
})
```

## Event Handling Best Practices

1. **Subscribe First**: Always subscribe to events before trying to handle them
2. **Error Handling**: Implement error handling for all event callbacks
3. **Type Safety**: Use TypeScript interfaces for event data
4. **Cleanup**: Remember to unsubscribe from events when they're no longer needed
5. **Validation**: Validate event data before processing
6. **Async Handlers**: Use async/await for asynchronous event handling

```ts
// Example with best practices
client.subscribe({
  Raw: ['Action', 'SubAction']
})

client.on('Raw.Action', async (data) => {
  try {
    // Validate data
    if (!data || !data.name) {
      throw new Error('Invalid action data')
    }

    // Process event
    await processAction(data)
  } catch (error) {
    console.error('Error handling action:', error)
  }
})