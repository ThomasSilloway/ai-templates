# Bug Description: Progress Bar Colors Reversed

**Observed Behavior:**
The progress bar colors are displayed in the reverse order compared to the active configuration settings.

**Expected Behavior (Based on User Report of Config):**
- Left side color: Red
- Right side color: Blue

**Actual Behavior:**
- Left side color: Blue
- Right side color: Red

**Configuration Source:**
The active configuration selected in the Debug Panel. The user reported the configuration specifies Left=Red, Right=Blue.

**Relevant Files:**
- Configuration UI: `src/lib/components/ConfigsTab.svelte`
- Configuration Service: `src/lib/services/ConfigService.ts`
- Progress Bar Component: `src/lib/components/ProgressBar.svelte`
- PRD (defines default config): `ai-specs/04-05_01_progress-bar-configs/generated/prd.md`