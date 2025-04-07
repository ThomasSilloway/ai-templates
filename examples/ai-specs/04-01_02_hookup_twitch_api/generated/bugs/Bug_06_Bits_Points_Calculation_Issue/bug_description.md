# Bug Report: Bits Points Calculation Issue

## Description
Small bit donations (less than 100 bits) are not generating any points in the system. When a user makes a cheer with 1 bit, it should add the appropriate fractional points based on the configured points per 100 bits, but currently adds 0 points.

## Expected Behavior
- If 100 bits = 100 points, then 1 bit should add 1 point
- If 100 bits = 200 points, then 1 bit should add 2 points
- The points should scale proportionally based on the configured points per 100 bits

## Current Behavior
- When a user cheers with less than 100 bits, no points are added
- This is due to Math.floor(bits/100) in the calculateBitsPoints function, which rounds down to 0 for any value less than 100

## Steps to Reproduce
1. Configure the system with any points value for 100 bits
2. Have a user cheer with 1 bit
3. Observe that no points are added to the system

## Technical Details
The issue is in the calculateBitsPoints function in points.ts:
```typescript
export function calculateBitsPoints(bits: number, config: PointConfig): number {
    return Math.floor(bits / 100) * config.hundredBits;
}
```
The Math.floor operation causes any bits value less than 100 to be rounded down to 0, resulting in no points being added.

## Impact
Users who make small bit donations are not receiving any points, which could discourage smaller contributions and creates an inconsistent user experience.