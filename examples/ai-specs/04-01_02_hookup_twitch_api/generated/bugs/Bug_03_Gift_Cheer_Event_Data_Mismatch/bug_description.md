# Bug Description: Gift Sub and Cheer Event Data Mismatch

## Issue Summary
Two distinct but related issues with event data processing:

1. Gift Sub Event Error
- Error: `TypeError: gifter is undefined`
- Root Cause: Code attempts to access `gifter` property but the gifter information is actually in the `user` field of the event data
- Event Data Structure:
```json
{
  "user": {  // Contains gifter info
    "id": "84393066",
    "login": "fuzzhead93",
    "name": "Fuzzhead93"
  }
}
```

2. Cheer Event Error
- Error: `TypeError: message.toLowerCase is not a function`
- Root Cause: Code attempts to call toLowerCase() on message object instead of the text content
- Event Data Structure:
```json
{
  "message": {
    "message": "Cheer100",  // Actual message text is nested
    // ... other message properties
  }
}
```

## Impact
- Gift sub events fail to process properly
- Cheer events fail to process properly
- Both errors prevent proper point allocation and progress bar updates

## Steps to Reproduce
1. Receive gift sub event from Twitch
2. Receive cheer event from Twitch
3. Observe errors in debug console:
   - `ERROR: Failed to process gift sub event: TypeError: gifter is undefined`
   - `ERROR: Failed to process cheer event: TypeError: message.toLowerCase is not a function`

## Environment
- Browser: Any
- Event Source: Twitch via Streamer.bot

## Verification Data
Raw event data has been logged and verified showing the actual data structure differs from what the code expects.