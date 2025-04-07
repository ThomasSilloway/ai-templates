# Debug Console Color System

## Overview
The debug console implements a color-coding system to make different types of Twitch events easily distinguishable.

## Color Implementation

### 1. CSS Definitions
In `styles.css`, we define different colors for event types:
```css
.debug-line {
  color: #a0a0a0;  /* Default color for standard messages */
}

.debug-line.bits {
  color: #9f7ae5;  /* Purple for bit donations */
}

.debug-line.sub {
  color: #47d147;  /* Green for subscriptions */
}
```

### 2. Event Type Detection
In `DebugConsole.svelte`, the type is determined by analyzing the event message:
```typescript
const type = event.toLowerCase().includes('bits') ? 'bits' : 
             event.toLowerCase().includes('sub') ? 'sub' : '';
```

### 3. Class Application
The type is then applied as a CSS class:
```html
<div class="debug-line {line.type}">
```

## Color Meanings

1. **Default** (#a0a0a0 - Gray)
   - General messages
   - Follows
   - Raids
   - Any unspecified event type

2. **Bits** (#9f7ae5 - Purple)
   - Bit donations
   - Cheers
   - Any message containing "bits"

3. **Subscriptions** (#47d147 - Green)
   - New subscriptions
   - Gift subs
   - Sub renewals
   - Any message containing "sub"

## Implementation Details

1. **Message Processing**
   ```typescript
   interface DebugLine {
     text: string;
     type: string;     // Determines the color
     timestamp: string;
   }
   ```

2. **Type Assignment**
   - Each message is analyzed when created
   - Type is determined by content keywords
   - Type maps directly to CSS class names

3. **Color Application**
   - CSS classes are applied dynamically
   - Multiple classes can be combined
   - Colors are defined using hex values for consistency

## Extending the System

To add new event types and colors:

1. Add new CSS class in `styles.css`:
   ```css
   .debug-line.new-type {
     color: #desired-color;
   }
   ```

2. Update type detection in `DebugConsole.svelte`:
   ```typescript
   const type = event.toLowerCase().includes('new-keyword') ? 'new-type' : 
                // ... existing conditions
   ```

## Best Practices

1. Use distinctive colors that:
   - Are visually separate from other types
   - Have good contrast against the dark background
   - Are comfortable for extended viewing

2. Maintain consistency:
   - Keep similar events in the same color family
   - Use brighter colors for more important events
   - Maintain sufficient contrast ratios

3. Consider accessibility:
   - Ensure color combinations meet WCAG guidelines
   - Don't rely solely on color for differentiation
   - Include additional visual indicators if needed