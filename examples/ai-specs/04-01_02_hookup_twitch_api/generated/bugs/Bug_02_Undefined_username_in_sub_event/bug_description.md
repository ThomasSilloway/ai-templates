# Bug Report: Undefined Username in Sub Event

## Error Details
When a subscription event is received from Streamer.bot, the username is logged as `undefined` despite being available in the action arguments.

### Error Message
```
[19:49:25.566] SUB: undefined subscribed with tier 1000
[19:50:11.221] SUB: undefined subscribed with tier 1000
```

### Related Logs
```
[19:49:25.568] ACTION: message_sub Args: fromSharedChat: "false", tier: "tier 3", isPrimeSub: "false", color: "null", badgeCount: "1", badges: "[object Object]", monthsSubscribed: "1", isMultiMonth: "false", multiMonthDuration: "1", isTest: "true", triggerName: "Subscription", triggerCategory: "Twitch/Subscriptions", actionName: "message_sub", user: "Fuzzhead93", userName: "fuzzhead93", userId: "84393066", userType: "twitch", userGroups: "", isSubscribed: "true", subscriptionTier: "3000", isModerator: "true", isVip: "false", userPreviousActive: "2025-04-01T19:48:...", eventSource: "twitch", broadcastUser: "Fuzzhead93", broadcastUserName: "fuzzhead93", broadcastUserId: "84393066", broadcasterIsAffiliate: "true", broadcasterIsPartner: "false"
```

## Steps to Reproduce
1. Launch the Twitch app prototype
2. Connect to Streamer.bot successfully
3. Trigger a test subscription event in Streamer.bot
4. Observe the debug console logs

## Expected Behavior
- The subscription event should log the correct username
- Points should be assigned to the correct user
- The progress bar should update for the correct user

## Actual Behavior
- The username in the SUB log is `undefined`
- Points are queued for "undefined" user
- The progress bar doesn't update correctly

## Impact
- Points system doesn't work for subscriptions
- Users don't get credit for their subscriptions
- Progress bar doesn't reflect subscription events
- Core monetization feature is non-functional

## Environment Details
- Application: Twitch App Prototype  
- Component: StreamerbotService/PointManager
- Event Type: Twitch Subscription
- Streamer.bot Integration: @streamerbot/client library