# Bug Fix Plan: Undefined Username in Sub Event

## Root Cause Analysis
- The Twitch.Sub event from Streamer.bot is not providing the username in the expected format
- The username is available in action args but not in the raw sub event data
- The current code doesn't have a fallback mechanism to get the username from action args

## Proposed Solution
1. Modify `handleSubEvent` in StreamerbotService.ts to:
   - First try to get username from sub event data
   - If not available, try to extract from action args if present
   - Add debug logging for both attempts

2. Update the type assertion for TwitchSubData to be more flexible:
   - Make username optional in the type
   - Add validation before using the username

3. Add additional debug logging:
   - Log the raw sub event data structure
   - Log when falling back to action args for username

## Implementation Steps
1. In StreamerbotService.ts:
```pseudo
function handleSubEvent(rawData) {
  try {
    const data = rawData.data as TwitchSubData;
    
    // Use userName as primary field
    let username = data.userName;
    let source = 'userName';
    
    // Fallback to displayName if userName is missing
    if (!username && data.displayName) {
      username = data.displayName;
      source = 'displayName';
    }
    
    // Log which field was used
    debugLog(`Got username from ${source} field: ${username}`);
    
    const tier = data.tier || '1000';
    debugLog(`SUB: ${username} subscribed with tier ${tier}`);
    
    pointManager.handleSubscription(tier, data.userId);
  } catch (error) {
    debugLog(`Error processing sub: ${error}`);
  }
}
```

2. In types/twitch.ts:
```pseudo
interface TwitchSubData {
  userId: string;
  userName: string;  // Correct field name per Streamer.bot docs
  displayName?: string;  // Optional fallback
  tier?: string;
  planName?: string;
}
```

## Verification Steps
1. Trigger test subscription events
2. Verify logs show:
   - Where username was obtained from (sub event or action args)
   - Correct username is logged
   - Points are assigned to correct user
3. Check console for any error messages

## Risk Assessment
- Low risk changes
- Added logging helps verify behavior
- Fallback mechanism ensures functionality even if data format changes