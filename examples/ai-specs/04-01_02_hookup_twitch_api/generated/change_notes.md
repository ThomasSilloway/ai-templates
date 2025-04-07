# Change Notes

## v01 - Initial Setup and Event System
- Created the change_notes.md file to track implementation progress
- Created points.ts utility file with point calculation functions
- Implemented PointManager service for handling point allocation and queuing
- Added TypeScript definitions for Twitch events and integration types
- Updated StreamerbotService with:
  - Twitch event subscriptions (Cheer, Sub, Resub, GiftSub, GiftBomb)
  - Event handlers for processing Twitch events
  - Points calculation and queueing logic
  - Debug logging for all events
- Added type-safe event handling with proper Streamerbot event type definitions
- Implemented fallback values for optional event data

## v02 - WebSocket Connection Bug Fix
- Fixed race condition in WebSocket connection lifecycle
- Moved subscription setup into separate private method
- Ensured subscriptions are only set up after WebSocket connection is established
- Added connection state validation before setting up subscriptions
- Improved error handling and state management in StreamerbotService

## v03 - Username Bug Fix
- Fixed undefined username in Twitch subscription events
- Updated TwitchSubData interface to correctly reflect event structure
- Modified StreamerbotService to use `data.user.name` for username
- Added debug logging for subscription events
- Verified points are now correctly assigned to users

## v04 - Gift Sub and Cheer Event Data Fix
- Fixed gift sub event handler to correctly access gifter information from `user` property instead of non-existent `gifter` property
- Fixed cheer event handler to correctly access message text from nested `message.message` property
- Updated TwitchCheerData and TwitchGiftSubData interfaces to match actual event data structure from Streamer.bot
- Improved error handling by using correct property paths in event handlers
- Maintained all existing debug logging for better observability

## v05 - Command Event Display Name Fix
- Fixed command event handler to use `user.display` instead of `user.display_name`
- Updated TwitchUser interface to reflect correct property name
- Corrected debug logging for command events to show proper username

## v06 - Bits Points Calculation Fix
- Fixed calculateBitsPoints to properly handle fractional points for small bit donations
- Removed Math.floor operation that was causing small bit values to be rounded down to 0
- Implemented proportional points calculation that preserves decimal precision
- Added detailed calculation logging in PointManager to show the bits-to-points conversion
- Supports all point ratio scenarios (1:1, 2:1, 1:2) correctly

## v07 - Pending Points Display Implementation
- Added pending points display section to DebugPanel
- Integrated userPendingPoints store to show queued points per user 
- Implemented real-time updates of pending points display
- Added styling consistent with existing debug sections
- Included empty state handling for when no points are pending

## v08 - Debug Panel Layout Fix
- Moved pending points display to the right of action history
- Updated layout to use horizontal flex container
- Added proper border and padding styling for side-by-side layout
- Fixed indentation for better code readability

## v09 - User Display Names Enhancement
- Added display names to Action History for command events
- Updated userPendingPoints store to include display names alongside points
- Modified PointManager to track and pass user display names
- Updated all Twitch event handlers to properly pass user display names
- Enhanced DebugPanel to show display names in Pending Points section
- Improved code consistency in handling user information across components

## v10 - Debug Test Message Feature
- Added Debug Settings panel to Settings Tab
- Implemented test message configuration for subscription events
- Updated PointManager to handle command messages in subscriptions
- Modified StreamerbotService to apply test messages to events
- Enhanced debug log messages to include usernames
- Fixed action history not updating for command events
- Enhanced event handlers to support direct point allocation with test messages