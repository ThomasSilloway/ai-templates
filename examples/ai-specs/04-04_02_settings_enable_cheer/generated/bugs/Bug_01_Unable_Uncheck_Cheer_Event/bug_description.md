# Unable to Uncheck Cheer Event Setting

## Summary
Users are unable to uncheck the "Enable Cheer Event" checkbox in the Debug Settings panel. This prevents users from disabling Twitch Cheer event subscriptions through the UI.

## Steps to Reproduce
1. Open the application
2. Navigate to the Debug Settings panel
3. Locate the "Enable Cheer Event" checkbox
4. Attempt to uncheck the checkbox
5. Click "Save Changes" button

## Expected Behavior
- The checkbox should be unchecked when clicked
- Upon saving, the cheer event subscription should be disabled
- The setting should persist across application restarts

## Actual Behavior
- The checkbox cannot be unchecked
- The "Enable Cheer Event" setting remains enabled despite user attempts to disable it

## Related Components/Files
- `/twitch-app-prototype/src/lib/components/settings/DebugSettingsForm.svelte`
- `/twitch-app-prototype/src/lib/services/StreamerbotService.ts`
- `/twitch-app-prototype/src/lib/stores/streamerbot.ts`

## Impact on Functionality
- Users cannot disable Twitch Cheer event notifications
- Prevents customization of event subscriptions
- May impact system performance by processing unwanted events
- Reduces user control over application behavior

## Technical Context
The issue appears in the interaction between the DebugSettingsForm component and the StreamerbotService. The form binds to the config store's debugSettings.subscribeToCheerEvents value, but the checkbox state cannot be toggled off, suggesting a potential issue with either the form binding or the underlying state management.