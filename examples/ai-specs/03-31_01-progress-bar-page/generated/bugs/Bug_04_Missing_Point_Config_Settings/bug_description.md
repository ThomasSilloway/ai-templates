# Bug Report: Missing Point Configuration Settings in Settings Tab

## Bug Description
The Settings tab is missing critical point configuration settings that are required per the PRD. These settings are essential for calculating points earned through various Twitch interactions.

### Expected Behavior
The Settings tab should contain configuration fields for the following point settings as defined in the PRD:

- Points per 100 bits
- Base subscription points
- Tier 2 multiplier
- Tier 3 multiplier
- Gift sub/resub bonuses
- Default target points

These settings should be exposed through the interface:
```typescript
interface PointConfig {
  hundredBits: number;     // Points per 100 bits
  subPoints: number;       // Base sub points
  tier2Multiplier: number; // Tier 2 multiplier
  tier3Multiplier: number; // Tier 3 multiplier  
  giftBombBonus: number;   // Gift bomb bonus
  resubMultiplier: number; // Resub multiplier
  streakBonus: number;     // Streak bonus
  defaultTarget: number;   // Default target
}
```

### Current Behavior
The Settings tab does not contain any of the point configuration settings specified in the PRD. This means there is no way for streamers to customize how points are awarded for different types of Twitch interactions.

### Impact
1. **Point Calculation**: Without these settings, the system cannot properly calculate points for:
   - Bit donations
   - Subscriptions at different tiers
   - Gift subscriptions
   - Resubscriptions
   - Subscriber streaks

2. **User Experience**: Streamers cannot customize the point system to match their community's engagement patterns or reward preferences.

3. **Default Target**: Missing default target setting means each new progress bar must have its target manually set, increasing setup time and effort.

### Additional Context
This is a critical feature gap as these settings form the core configuration for the point-based progress bar system. The missing configuration options prevent proper implementation of the point calculation logic specified in the PRD.

## Environment
- Location: Settings Tab
- Component: Point Configuration Section
- Project: Progress Bar Page