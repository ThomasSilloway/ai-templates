# Bug: Resub Message Parsing Issue

## Description
The Streamerbot Resub event message is not being parsed correctly in the application. The event data contains a command message "!shave" but it's not being properly handled.

## Event Data Example
```json
{
    "cumulativeMonths": 0,
    "durationMonths": 0,
    "streakMonths": 0,
    "subTier": "2000",
    "isPrime": false,
    "isGift": false,
    "gifterIsAnonymous": false,
    "text": "!shave",
    "parts": [
        {
            "type": "text",
            "text": "!shave"
        }
    ],
    "user": {
        "role": 1,
        "badges": [
            {
                "name": "subscriber",
                "version": "0",
                "imageUrl": "https://static-cdn.jtvnw.net/badges/v1/5d9f2208-5dd8-11e7-8513-2ff4adfae661/3",
                "info": "0"
            }
        ],
        "subscribed": false,
        "monthsSubscribed": 0,
        "id": "84393066",
        "login": "fuzzhead93",
        "name": "Fuzzhead93",
        "type": "twitch"
    },
    "systemMessage": "Fuzzhead93 subscribed at tier 2. They've subscribed for 0 months!",
    "isTest": true
}
```

## Impact
- Commands within Resub event messages are not being processed
- The application may be missing important user interactions during subscription events

## Suspected Cause
The type definitions in twitch.ts may be incorrect for handling the event structure, particularly for subscription-related events.