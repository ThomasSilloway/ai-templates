# Test Cases for Debug Panel Button Fix

1. Adding Left Points:
   - Starting state: Empty progress
   - Active config: Left Text = "Shave", Right Text = "Beard"
   - Action: Click "Add Shave Points" button (top button)
   - Expected Results:
     * Points added to `totalLeftSidePoints`
     * Action History shows: "Test Add Points: +500 shave"
     * Current Values shows: "Total Shave Points: 500"

2. Adding Right Points:  
   - Starting state: Previous test state
   - Active config: Same as above
   - Action: Click "Add Beard Points" button (bottom button)
   - Expected Results:
     * Points added to `totalRightSidePoints`
     * Action History shows: "Test Add Points: +500 beard"  
     * Current Values shows: "Total Beard Points: 500"

3. Switch Configuration:
   - Action: Change active config to one with different text labels (e.g., "Good" vs "Evil")
   - Expected Results:
     * Button labels update to show new text
     * Button colors update to match new config
     * Clicking buttons logs actions with new text labels
     * Point totals display with new text labels

4. Reset and Verify:
   - Action: Click "Reset Progress"
   - Expected Results:
     * Both point totals return to 0
     * Action History is cleared
     * Buttons retain the active configuration's text/colors