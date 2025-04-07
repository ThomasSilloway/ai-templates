# Twitch App Setup Changes Required

The following files need to be updated to convert the counter-app structure to twitch-app-prototype:

## Package.json Updates
```json
{
  "name": "twitch-app-prototype",
  "private": true,
  "version": "0.0.1"
  // rest remains the same
}
```

## Batch File Updates

### start-counter.bat → start-app.bat
- Rename file
- Update echo message to "Starting Twitch App Prototype..."

### stop-counter.bat → stop-app.bat
- Rename file
- Update echo message to "Stopping Twitch App Prototype..."

### export-build.bat
- Update directory references from "counter-app" to "twitch-app-prototype"
```batch
REM Clean previous build
if exist "..\bin\twitch-app-prototype" rmdir /s /q "..\bin\twitch-app-prototype"

REM Create new directory
mkdir "..\bin\twitch-app-prototype"
```

## README.md Updates
- Update title to "Twitch App Prototype"
- Update description to reflect new application purpose
- Update any references to "counter-app" in paths or instructions

## Implementation Steps

1. Rename the batch files:
   - start-counter.bat → start-app.bat
   - stop-counter.bat → stop-app.bat

2. Update package.json with new application name

3. Update export-build.bat directory references

4. Update README.md content to reflect new application

5. Test the application startup:
   ```
   ./start-app.bat
   ```

6. Verify in browser:
   ```
   http://localhost:3456
   ```

All other configuration files (svelte.config.js, vite.config.ts, tsconfig.json) can remain unchanged as they don't contain application-specific naming.