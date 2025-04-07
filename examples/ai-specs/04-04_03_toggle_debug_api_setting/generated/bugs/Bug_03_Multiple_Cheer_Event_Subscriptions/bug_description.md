# Bug: Multiple Cheer Event Subscriptions

## Description
Toggling the "Enable Cheer Event" checkbox in the Debug Settings panel multiple times causes the cheer event to be subscribed to multiple times. When a single cheer event is triggered in Streamerbot, the points are added multiple times (once for each subscription).

## Symptoms
- Multiple log entries for a single cheer event
- Points being added multiple times for a single cheer
- Multiple point calculations and queuing operations per cheer event

## Reproduction Steps
1. Open the Settings tab
2. Navigate to Debug Settings
3. Toggle the "Enable Cheer Event" checkbox OFF and save
4. Toggle the "Enable Cheer Event" checkbox ON and save
5. Repeat steps 3-4 multiple times
6. Trigger a cheer event in Streamerbot

## Expected Behavior
When a cheer event occurs, it should be processed exactly once, resulting in:
- A single log entry for the cheer event
- Points being added only once
- A single calculation and queuing operation

## Actual Behavior
When a cheer event occurs after multiple toggle operations, it is processed multiple times, resulting in:
- Multiple identical log entries for the same cheer event
- Points being calculated and added multiple times
- Multiple queuing operations for the same user

## Log Evidence
```
[19:06:45.426] Event subscriptions configured
[19:06:47.780] [toggleCheerSubscription] Called with enable=false
[19:06:47.782] Updating config with new subscription state: false
[19:06:49.122] [toggleCheerSubscription] Called with enable=true
[19:06:49.123] Updating config with new subscription state: true
[19:06:50.649] [toggleCheerSubscription] Called with enable=false
[19:06:50.650] Updating config with new subscription state: false
[19:06:52.081] [toggleCheerSubscription] Called with enable=true
[19:06:52.082] Updating config with new subscription state: true
[19:06:53.527] [toggleCheerSubscription] Called with enable=false
[19:06:53.528] Updating config with new subscription state: false
[19:06:55.029] [toggleCheerSubscription] Called with enable=true
[19:06:55.031] Updating config with new subscription state: true
[19:06:58.914] CHEER: Fuzzhead93 cheered 500 bits with message: Cheer100 Cheer100 Cheer100 Cheer100 Cheer100
[7:06:58 PM] [Points] Bits calculation: 500 bits * 100 points/100 = 500 points
[7:06:58 PM] [Points] Queued 500 points for user Fuzzhead93
[19:06:58.914] CHEER: Fuzzhead93 cheered 500 bits with message: Cheer100 Cheer100 Cheer100 Cheer100 Cheer100
[7:06:58 PM] [Points] Bits calculation: 500 bits * 100 points/100 = 500 points
[7:06:58 PM] [Points] Queued 500 points for user Fuzzhead93
[19:06:58.915] CHEER: Fuzzhead93 cheered 500 bits with message: Cheer100 Cheer100 Cheer100 Cheer100 Cheer100
[7:06:58 PM] [Points] Bits calculation: 500 bits * 100 points/100 = 500 points
[7:06:58 PM] [Points] Queued 500 points for user Fuzzhead93
[19:06:58.915] CHEER: Fuzzhead93 cheered 500 bits with message: Cheer100 Cheer100 Cheer100 Cheer100 Cheer100
[7:06:58 PM] [Points] Bits calculation: 500 bits * 100 points/100 = 500 points
[7:06:58 PM] [Points] Queued 500 points for user Fuzzhead93
```

## Technical Analysis
The bug appears to be in the event subscription handling in the StreamerbotService. 