# Bug Fix Plan: Bits Points Calculation Issue

## Overview
Fix the calculateBitsPoints function to properly handle fractional points for bit donations less than 100 bits, preserving decimal precision.

## Current Implementation
```typescript
export function calculateBitsPoints(bits: number, config: PointConfig): number {
    return Math.floor(bits / 100) * config.hundredBits;
}
```

## Solution Approach

### 1. Update Calculation Logic
- Remove the Math.floor operation that's causing small bit values to be rounded down to 0
- Calculate the proportional points based on the bits-to-points ratio
- Preserve decimal precision without rounding
- Maintain floating-point accuracy for fractional points

Pseudo code:
```typescript
export function calculateBitsPoints(bits: number, config: PointConfig): number {
    // First multiply to preserve precision, then divide
    // No rounding - keep decimal points
    // e.g., for 1 bit when 100 bits = 50 points:
    // (1 * 50) / 100 = 0.5 points
    return (bits * config.hundredBits) / 100;
}
```

### 2. Add Debug Logging
Add logging in the PointManager's handleBitsCheer method to verify:
- Input bit amount
- Configured points per 100 bits
- Calculated points value (including decimals)
- Whether points were applied directly or queued

### 3. Testing Plan
1. Test small bit amounts:
   - Test with 1 bit (should give proportional points)
   - Test with 50 bits (should give half the points of 100 bits)
   - Test with 99 bits (should give 99% of the points of 100 bits)

2. Test different point configurations:
   - When 100 bits = 100 points (1:1 ratio)
     * 1 bit should give 1 point
     * 50 bits should give 50 points
   - When 100 bits = 200 points (2:1 ratio)
     * 1 bit should give 2 points
     * 50 bits should give 100 points
   - When 100 bits = 50 points (1:2 ratio)
     * 1 bit should give 0.5 points
     * 2 bits should give 1 point
     * 50 bits should give 25 points

3. Test with commands:
   - Bits cheer with !beard command (points should be applied immediately)
   - Bits cheer with !shave command (points should be applied immediately)
   - Bits cheer without command (should queue points)

## Implementation Steps
1. Update calculateBitsPoints function in points.ts to preserve decimal precision
2. Add detailed debug logging in PointManager.ts
3. Test all ratio cases thoroughly to verify proper decimal handling
4. Verify queued points work correctly with decimal values

## Success Criteria
- Small bit donations (1-99) generate proportional points
- Points scale correctly for all ratios (1:1, 2:1, and 1:2)
- Decimal points are preserved (e.g., 0.5 points for 1 bit in 1:2 ratio)
- Debug logging shows precise decimal values
- All test cases pass as specified in the testing plan