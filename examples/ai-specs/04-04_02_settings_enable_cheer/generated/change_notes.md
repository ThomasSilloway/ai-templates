# Change Notes

## v05

* Bug Fixes:
  - Fixed event handler persistence for Cheer events
  - Implemented proper cleanup of WebSocket event handlers
  - Added synchronization between subscription state and event handlers

* Technical Improvements:
  - Refactored subscription management into dedicated methods
  - Enhanced logging for subscription and handler states
  - Improved type safety in subscription handling

## v04

* Bug Fixes:
  - Fixed checkbox state binding to allow unchecking Enable Cheer Event option
  - Implemented proper config persistence for Debug Settings
  - Added local state management to prevent form state overwrites
  - Enhanced store updates to handle nested config objects correctly

* Developer Experience:
  - Added comprehensive debug logging for state changes
  - Improved config persistence debugging
  - Enhanced form state change tracking

## v03

* Bug Fixes:
  - Fixed settings persistence for Debug Settings after page refresh
  - Corrected cheer event subscription toggling behavior
  - Ensured debug console messages display for subscription state changes
  - Fixed store state handling for nested debug settings

* UI Polish:
  - Improved layout of Test Message section with inline description
  - Fixed styling consistency for form elements

## v02

* UI Improvements:
  - Added Save button for persisting Debug Settings changes
  - Set consistent minimum width (120px) for all Debug Settings labels
  - Left-aligned all Debug Settings labels
  - Removed colons from form labels
  - Updated checkbox state persistence to match Point Configuration pattern

## v01

* Store Updates:
  - Added `subscribeToCheerEvents` boolean to DebugSettings interface in streamerbot store
  - Set default value to true in defaultConfig
  - Integrated with existing config store persistence mechanism

* UI Updates:
  - Added checkbox input for cheer event subscription in DebugSettingsForm
  - Labeled as "Enable Cheer Event" with descriptive helper text
  - Implemented handleCheerToggle handler for real-time subscription updates

* Service Updates:
  - Added toggleCheerSubscription method to StreamerbotService
  - Enhanced setupSubscriptions to conditionally include Cheer events based on config
  - Added detailed debug logging for cheer subscription status changes
  - Implemented dynamic subscription management without requiring reconnection