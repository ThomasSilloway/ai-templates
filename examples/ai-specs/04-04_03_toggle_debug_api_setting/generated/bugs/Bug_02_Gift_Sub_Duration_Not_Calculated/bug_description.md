# Bug Report: Gift Sub Duration Not Calculated in Points

## Description
The gift subscription point calculation is not properly accounting for the subscription duration (durationMonths) when calculating total points. The system only multiplies the base points by the number of subscriptions, ignoring the duration multiplier.

## Steps to Reproduce
1. Send a gift subscription batch with 5 subs
2. Set the subscription duration to 6 months
3. Observe the points calculation in the logs

## Expected Behavior
Points should be calculated as: 
`(base points) * (number of subs) * (duration in months)`

For example, with base points of 10, 5 subs, and 6 months duration:
`10 * 5 * 6 = 300 points`

## Actual Behavior
Points are calculated as:
`(base points) * (number of subs)`

Using the same example:
`10 * 5 = 50 points` (missing the 6x multiplier)

## Relevant Log Data
Logs show the calculation stopping after multiplying base points by sub count, without applying the duration multiplier:
```
[TwitchPoints] Calculating gift sub points - count: 5, duration: 6
[TwitchPoints] Base points: 10
[TwitchPoints] Calculated points: 50 (expected: 300)
```

## Affected Functionality
- Gift subscription point calculations
- Point totals displayed to streamer
- Point leaderboard calculations

## Impact on Users
- Viewers receive incorrect point totals for gifted subscriptions
- Streamer sees inaccurate point distribution in dashboard
- Potential fairness issues in point-based rewards