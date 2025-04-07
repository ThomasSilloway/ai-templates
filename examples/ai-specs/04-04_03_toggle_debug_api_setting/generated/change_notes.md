# Enable Debug API Logging Change Notes

## v1.2.2

### Bug Fixes
- Fixed gift sub points not being multiplied by duration months
- Maintained backward compatibility with existing point calculations

### Debug Logging Improvements
- Added duration months to debug logging output
- Enhanced visibility into duration-based calculations

### Verification Results
- Verified correct point calculations with various duration/sub count combinations
- Confirmed debug logging shows complete duration calculation details
- Validated backward compatibility with existing configurations

## v1.2.1

### Bug Fixes
- Fixed gift sub points not being multiplied by cumulativeTotal
- Added detailed debug logging for gift sub calculations
- Updated point calculation logic to properly handle cumulative multipliers

### Debug Logging Improvements
- Enhanced debug output for point calculations
- Added detailed logging of gift sub event processing
- Improved visibility into multiplier application

### Verification Results
- Confirmed proper point calculations with multiple test cases
- Verified debug logging shows complete calculation details
- Validated correct multiplier application across different scenarios

## v1.2.0

### UI Polish Improvements
- Increased decimal place support to 3 places in Point Configuration multiplier inputs
- Improved number formatting consistency across displays:
  - Created shared number formatting utility for standardization
  - Enhanced Action History display formatting
  - Refined Pending Points display formatting
  - Fixed floating point precision display issues

### Technical Changes
- Implemented shared numberFormat utility for consistent number handling
- Updated multiplier input validation to support 3 decimal places
- Refactored number display logic to use shared formatting utility
- Fixed floating point rounding and display precision across components

### Verification Results
- Number Input: Verified 3 decimal place support in multiplier configuration
- Display Formatting: Confirmed consistent number presentation across all displays
- Precision Handling: Validated proper handling of floating point calculations

## v1.1.0

### UI Polish Improvements
- Implemented dynamic height adjustment for DebugConsole to optimize viewport usage
- Added smart auto-scrolling for improved message visibility:
  - Automatically scrolls to new messages when already at bottom
  - Maintains scroll position when reviewing historical messages
  - Visual indicator shows when new messages arrive while scrolled up

### Technical Changes
- Enhanced DebugConsole component with ResizeObserver for dynamic height calculations
- Implemented scroll position tracking and smart scroll behavior logic
- Added scroll position state management for improved user experience

### Verification Results
- Height Adjustment: Verified dynamic resizing based on available viewport space
- Auto-scroll Behavior: Confirmed proper scroll management in various scenarios
- Visual Feedback: Validated new message indicator functionality

## v1.0.0

### Feature Additions
- Added enableApiDebugging toggle to DebugSettings interface in config store for controlling API debug message visibility
- Added "Enable Debug: API" checkbox to DebugSettingsForm between "Enable Cheer Event" and "Test Message" controls
- Created addApiDebugMessage method in StreamerbotService and TwitchChatService to standardize API debug logging
- Implemented persistence of API debug setting through config store

### Technical Changes
- Refactored existing API-related debug calls to use new addApiDebugMessage method for consistent logging

### Verification Results
- Store Implementation: Verified enableApiDebugging property in DebugSettings interface with correct default value
- UI Implementation: Confirmed checkbox placement, label text, description text, and proper save functionality
- Logging Function: Verified addApiDebugMessage implementation in both services with correct config integration
- All files contain proper empty line at end