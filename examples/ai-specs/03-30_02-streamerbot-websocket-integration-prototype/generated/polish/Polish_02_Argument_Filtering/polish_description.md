# Polish: Argument Filtering

## Current Behavior
All arguments are displayed in action/subaction messages, including internal ones like:
- triggerId
- actionId  
- runningActionId
- actionQueuedAt

## Desired Behavior
Filter out these internal arguments to show only relevant ones, with configuration through Settings tab.

## Implementation Options
1. **Modify formatArgs in StreamerbotService.ts**:
   - Add filtering of known internal fields
   - Pros: Simple, single location change
   - Cons: Hardcoded filter list

2. **Configurable denylist**:
   - Add hiddenArgs array to config store
   - Update Settings UI to manage list
   - Pros: User configurable, flexible
   - Cons: More complex implementation

## Recommended Approach
Option 2 - Configurable denylist:

1. Add to ConfigState:
```ts
interface ConfigState {
  // ...existing fields
  hiddenArgs: string[]; // ['triggerId', 'actionId', ...]
}
```

2. Update SettingsTab to include:
- Toggle switches for default internal args
- Input field to add custom hidden args

3. Modify formatArgs:
```ts
return Object.entries(args)
  .filter(([key]) => !config.hiddenArgs.includes(key))
  .map(...) // rest of existing formatting
```

Benefits:
- User control over filtered args
- Cleaner debug output
- Flexible for future needs