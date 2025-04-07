# Bug Description: Command Event Display Name Field Mismatch

## Issue Summary
The command event handler attempts to access `user.display_name` but the actual event data uses `user.display` for the display name field, causing undefined values in command logging.

## Event Data Structure
```json
{
  "data": {
    "command": "!beard",
    "user": {
      "display": "Fuzzhead93",  // Field is 'display', not 'display_name'
      "id": "84393066",
      "name": "fuzzhead93",
      "role": 4,
      "subscribed": true,
      "type": "twitch"
    }
  }
}
```

## Impact
- Command events show "undefined used !beard" in logs instead of the user's name
- Affects readability and debugging of command usage
- Core functionality still works as user ID is correct

## Steps to Reproduce
1. Execute a command in Twitch chat (e.g., !beard)
2. Observe in debug console:
   - `COMMAND: undefined used !beard`
   - The error occurs because we try to access `display_name` when the field is actually `display`

## Environment
- Browser: Any
- Event Source: Twitch via Streamer.bot

## Verification Data
Raw event data has been logged and shows the correct field name should be 'display' instead of 'display_name' in our code.