# Polish: Auto-Scroll Debug Console

## Current Behavior
When switching to the Debug tab, the console maintains its current scroll position rather than automatically scrolling to show the latest messages.

## Desired Behavior
When the Debug tab is opened/clicked, the console should automatically scroll to the bottom to show the most recent messages.

## Implementation Options
1. **Svelte onMount in DebugConsole.svelte**:
   - Use onMount lifecycle hook to scroll to bottom
   - Pros: Simple, contained in component
   - Cons: Only runs once on initial mount

2. **Tab Change Event Listener**:
   - Listen for tab change events in DebugConsole
   - Scroll to bottom when Debug tab becomes active
   - Pros: Handles all tab switch cases
   - Cons: More complex event handling

3. **Store-Based Solution**:
   - Add activeTab state to store
   - Watch for changes in DebugConsole
   - Scroll when tab changes to Debug
   - Pros: Centralized state management
   - Cons: More indirect solution

## Recommended Approach
Option 2 - Tab Change Event Listener:
```svelte
<script>
  import { onMount } from 'svelte';
  let consoleRef;

  onMount(() => {
    // Initial scroll to bottom
    scrollToBottom();
    
    // Add tab change listener
    const handleVisibilityChange = () => {
      if (!document.hidden) {
        scrollToBottom();
      }
    };
    
    document.addEventListener('visibilitychange', handleVisibilityChange);
    return () => {
      document.removeEventListener('visibilitychange', handleVisibilityChange);
    };
  });

  function scrollToBottom() {
    if (consoleRef) {
      consoleRef.scrollTop = consoleRef.scrollHeight;
    }
  }
</script>

<div class="debug-console" bind:this={consoleRef}>
  <!-- messages -->
</div>