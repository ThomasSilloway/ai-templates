# Bug Fix Plan: Gift Sub Duration Not Calculated

## 1. Current Implementation Analysis

### Calculation Flow
1. **StreamerbotService.ts** receives gift sub events with `duration_months` parameter
2. **PointManager.ts** handles subscription logic but doesn't use duration months
3. **points.ts** calculates points without duration multiplier

### Key Issues
- `handleGiftSubEvent` in StreamerbotService.ts passes `cumlativeTotal` as `monthStreak` (misused parameter)
- `calculateSubPoints` in points.ts doesn't account for duration months
- Debug logging doesn't show duration calculation

## 2. Required Changes

### StreamerbotService.ts
- Modify `handleGiftSubEvent` to:
  - Extract `duration_months` from event data
  - Pass duration months to `handleSubscription`
  - Add debug logging for duration months

### PointManager.ts
- Update `handleSubscription` to:
  - Accept new `durationMonths` parameter
  - Pass duration to `calculateSubPoints`
  - Add debug logging for duration calculation

### points.ts
- Modify `calculateSubPoints` to:
  - Accept `durationMonths` parameter (default: 1)
  - Multiply total points by duration months
  - Add debug logging for duration multiplication

## 3. Debug Logging Improvements

Add detailed logging at each calculation step:
1. Input values (tier, count, duration)
2. Base points calculation
3. Duration multiplication
4. Final points total

Example log format:
```
[Points] Gift sub calculation - Tier: ${tier}, Count: ${count}, Duration: ${duration} months
[Points] Base points: ${basePoints} × ${count} = ${subTotal}
[Points] Applying duration multiplier: ${subTotal} × ${duration} = ${totalPoints}
```

## 4. Verification Test Cases

Test scenarios to verify:
1. Single gift sub with 1 month duration
2. Multiple gift subs (5) with 1 month duration
3. Single gift sub with 12 month duration 
4. Multiple gift subs (3) with 6 month duration
5. Non-gift subs (should remain unchanged)

Expected results:
- Points = base × count × duration
- Non-gift subs unaffected
- Existing functionality preserved

## 5. Potential Side Effects

Considerations:
1. Backward compatibility with existing subscriptions
2. Impact on point leaderboards
3. Database storage of calculated points
4. UI display of point totals
5. Interaction with other point sources (bits, cheers)

Mitigation:
- Thorough testing of all subscription types
- Verification of point totals in UI
- Monitoring after deployment