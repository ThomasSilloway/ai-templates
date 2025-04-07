# Bug Fix Plan: Layout Template Render Error

## Issue Analysis
The error `first_child_getter is undefined` occurring in root.svelte during initial app load suggests:
1. The layout template system is failing during initialization
2. The error occurs during hydration, indicating a mismatch between server and client rendering
3. Based on the stack trace, the error is related to template operations in +layout.svelte

## Potential Root Causes
1. The activeTab store is being accessed during server-side rendering before initialization
2. The layout component is attempting to access child elements before they're ready
3. The template structure might be incompatible with Svelte 5's hydration process

## Investigation Steps
1. Check if activeTab store is properly initialized before first access
2. Review +layout.svelte's template structure for proper child handling
3. Examine slot usage in the layout template

## Fix Strategy
1. Modify +layout.svelte to handle initialization state:
   ```ts
   // Initialize activeTab with a default value
   let initialTab = 'settings';
   activeTab.set(initialTab);
   ```

2. Add safe-guards around slot rendering:
   ```svelte
   <div class="app">
     <nav class="nav-tabs">
       <!-- nav buttons -->
     </nav>
     {#if $$slots.default}
       <slot />
     {/if}
   </div>
   ```

3. Ensure store initialization happens early:
   - Move store initialization to a separate initialization module
   - Import and initialize stores before component rendering

## Implementation Steps
1. Modify the +layout.svelte file:
   - Add slot existence check
   - Add store initialization
   - Restructure template for safer hydration

2. Create stores initialization module if needed:
   - Centralize store initialization
   - Ensure stores are ready before component mounting

3. Testing:
   - Verify app loads without hydration errors
   - Test tab navigation after fix
   - Ensure proper initial tab state

## Validation
- App should load without initial render errors
- Layout structure should be visible
- Tab navigation should work as expected
- No hydration warnings in console