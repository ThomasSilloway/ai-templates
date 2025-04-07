# Message Persistence Design

## Overview
To maintain message history when switching between tabs, we need to implement a persistent message store using Svelte's store mechanism.

## Architecture

### 1. Message Store
```typescript
// src/lib/stores/messages.ts
interface DebugMessage {
  text: string;
  type: string;
  timestamp: string;
}

const messages = writable<DebugMessage[]>([]);
```

### 2. Component Integration
The DebugConsole component will:
1. Subscribe to the message store
2. Add new messages to the store
3. Display messages from the store
4. Maintain its state across tab switches

## Implementation Details

### Message Store Operations

1. **Adding Messages**
```typescript
function addMessage(message: DebugMessage) {
  messages.update(msgs => [...msgs, message]);
}
```

2. **Reading Messages**
```typescript
$messages // Svelte store subscription
```

### DebugConsole Component Changes

1. Remove local message state
2. Use shared store instead
3. Keep interval management for simulated messages
4. Maintain scroll position

## Benefits

1. Messages persist between tab switches
2. Prepares for future websocket integration
3. Centralizes message management
4. Enables future features:
   - Message filtering
   - Message search
   - Message export
   - Message persistence to local storage

## Future Considerations

1. Message Limit
   - Consider implementing a maximum message limit
   - Remove oldest messages when limit is reached

2. Performance
   - Monitor performance with large message counts
   - Implement virtualization if needed

3. Persistence
   - Consider adding localStorage backup
   - Enable message history across page reloads

4. Websocket Integration
   - Message store ready for real-time updates
   - Easy integration with external message sources

## Implementation Steps

1. Create messages store
2. Modify DebugConsole to use store
3. Add scroll position management
4. Test persistence across tab switches
5. Add message limit handling
6. Implement auto-cleanup

## Code Structure
```
src/lib/
  ├── stores/
  │   └── messages.ts      # Message store
  └── components/
      └── DebugConsole.svelte