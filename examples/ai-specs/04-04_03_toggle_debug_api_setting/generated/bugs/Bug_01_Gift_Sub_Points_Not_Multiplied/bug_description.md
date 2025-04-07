# Bug Report: Gift Subscription Points Calculation Error

## Description
The points calculation system is not correctly handling gift subscriptions by failing to multiply the points by the number of gifted subscriptions. The system is ignoring the cumulative total value (5) that should be used as a multiplier for the points awarded.

## Steps to Reproduce
1. Open the Twitch stream overlay application
2. Enable points system
3. Configure gift subscription points value
4. Trigger a gift subscription event with multiple subs (e.g. 5 gift subs)
5. Observe the points calculation in logs and final total

## Expected Behavior
- For a gift subscription event of 5 subs:
  - System should take the base points value
  - Multiply it by the number of gifted subs (5)
  - Add the result to the user's point total

## Actual Behavior
- The system only awards points for a single subscription
- The cumulative total (5) is completely ignored
- Points are added as if only one subscription was gifted
- Total points awarded are significantly lower than intended

## Log Data
Points calculation log shows:
- Base points value being registered
- Gift subscription event detected
- Cumulative total (5) present but unused in calculation
- Final point total missing multiplication factor

## Affected Functionality
- Gift subscription points calculation
- Total points accumulation
- User progression system
- Reward milestone tracking

## Impact on Users
### Streamers
- Incorrect point distribution for community engagement
- Inaccurate reward progression
- Misrepresented community support metrics

### Viewers
- Missing earned points from gift subscriptions
- Delayed progression in point-based systems
- Undervalued community contributions
- Incorrect standing in point-based leaderboards

## Technical Impact
- Points economy significantly deflated
- Historical point totals may be incorrect
- Community reward thresholds harder to reach
- Engagement metrics showing incorrect values