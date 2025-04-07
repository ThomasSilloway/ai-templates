# Bug Fix Plan: Missing Point Configuration Settings

## 1. File Analysis

### Existing Implementation
- `src/lib/stores/progress.ts` already contains:
  - PointConfig interface definition
  - Default configuration values
  - Writable store implementation (pointConfiguration)

### Files to Modify
- `src/routes/settings/+page.svelte` - For adding point configuration UI
- `src/lib/stores/progress.ts` - Add persistence layer to existing store
- `src/lib/components/settings/` - Create new components for point config UI

### Settings Tab UI Location
- Add new "Point Configuration" section in Settings tab
- Place after general settings and before any advanced settings
- Use consistent styling with other settings sections

## 2. Implementation Steps

### Store Enhancement
1. Add localStorage persistence to existing pointConfiguration store:
```typescript
// In src/lib/stores/progress.ts
const STORAGE_KEY = 'pointConfig';

// Load initial state from localStorage or use default
const storedConfig = localStorage.getItem(STORAGE_KEY);
const initialConfig = storedConfig ? JSON.parse(storedConfig) : defaultPointConfig;

// Enhance store with persistence
export const pointConfiguration = writable(initialConfig);
pointConfiguration.subscribe(value => {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(value));
});
```

### Settings UI Components
1. Create new component `src/lib/components/settings/PointConfigForm.svelte`:
```typescript
interface PointConfigFormData {
  config: PointConfig;
  isValid: boolean;
}
```

2. Required form sections:
- Bit Rewards
  - Points per 100 bits input
- Subscription Rewards
  - Base sub points
  - Tier multipliers (2 & 3)
  - Gift bomb bonus
- Resub Bonuses
  - Resub multiplier
  - Streak bonus
- General Settings
  - Default target

3. Form Features:
- Number inputs with proper step values
- Help tooltips explaining each setting
- Reset to defaults button
- Save configuration button

### Form Validation Requirements
- All number fields required
- Simple validation:
  - All values must be greater than 0
  - Show inline error if value ≤ 0
- Disable save button when any validation fails