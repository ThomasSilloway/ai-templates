# Polish Item: Add Debug Message Settings

## Description
Add a Debug Settings panel in the Settings Tab to configure test messages for Twitch subscription events. This will allow simulating scenarios where users include commands like !beard in their subscription messages, enabling direct point allocation without going through the queue system.

## Current Behavior
- Currently unable to test subscription scenarios where users include !beard or !shave commands
- All subscription points go to queue regardless of message content
- No way to simulate command behavior in subscription messages

## Desired Behavior
- New Debug Settings panel in Settings Tab
- Configuration field for test message (empty by default)
- When set to "!beard" or "!shave", points from subs/bits go directly to that side
- Applies to subs, resubs, and bits events
- Debug-only feature for testing purposes

## Potential Solutions

### Solution 1: Debug Store Integration
1. Create new debug settings store to manage debug configuration
2. Add Debug Settings panel component in SettingsTab.svelte
3. Modify event handlers to check debug message setting
4. Update PointManager to handle direct point allocation based on debug settings

Pros:
- Clean separation of debug settings from regular config
- Easy to disable in production
- Maintains existing component structure

Cons:
- Additional store management overhead
- More complex state management

### Solution 2: Extend Existing Config Store
1. Add debug settings section to existing config store
2. Create Debug Settings form component
3. Update event handlers to check debug config
4. Modify point allocation logic

Pros:
- Reuses existing store infrastructure
- Simpler implementation
- Consistent with current settings pattern

Cons:
- Mixes debug settings with production config
- May need cleanup for production deployment

### Solution 3: Debug Mode Toggle
1. Add debug mode toggle in Settings Tab
2. When enabled, show debug settings panel
3. Create dedicated debug event processor
4. Implement command simulation logic

Pros:
- Clear separation between debug and production modes
- Easy to disable debug features
- More structured testing approach

Cons:
- More complex UI management
- Additional mode-specific logic needed

## Recommendation
**Solution 2: Extend Existing Config Store** is recommended because:
1. Most consistent with current application architecture
2. Leverages existing config management patterns
3. Simplest implementation path
4. Matches how other settings are handled in the application