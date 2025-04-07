# Streamer.bot Twitch Events

This document outlines all Twitch-specific events emitted by the Streamer.bot WebSocket Server.

## Channel Events

### Follow
Emitted when a user follows the channel.
```json
{
  "userId": 0,
  "userName": "<username>",
  "displayName": "<display name>",
  "isTest": true|false
}
```

### Stream Update
Emitted when stream information is updated.
```json
{
  "channelId": 0,
  "channel": "<user name of broadcaster>",
  "status": "Doing the things!",
  "oldStatus": "This is a different title!",
  "oldGame": {
    "id": 516097,
    "name": "Deadside"
  },
  "game": {
    "id": 7658,
    "name": "Mario Party 8"
  }
}
```

## Chat Events

### Chat Message
Emitted when a chat message is received.
```json
{
  "message": {
    "msgId": "a0d32df1-d3ca-4fd7-87fb-6c4e958550f0",
    "userId": 0,
    "username": "<username>",
    "role": 4,
    "subscriber": true,
    "displayName": "<display name>",
    "channel": "<broadcaster's channel name>",
    "message": "",
    "isHighlighted": false,
    "isMe": false,
    "isCustomReward": false,
    "isAnonymous": false,
    "isReply": false,
    "bits": 0,
    "hasBits": false,
    "emotes": [
      {
        "id": "300400304",
        "type": "Twitch",
        "name": "nate121Raid",
        "startIndex": 5,
        "endIndex": 15,
        "imageUrl": "https://static-cdn.jtvnw.net/emoticons/v2/300400304/default/dark/2.0"
      }
    ],
    "cheerEmotes": []
  }
}
```

### First Word
Emitted when a user sends their first message in the channel.
```json
{
  "message": "test",
  "action": false,
  "user": {
    "id": 0,
    "login": "<username>",
    "display_name": "<displayname>",
    "subscribed": true,
    "role": 1
  }
}
```

### Whisper
Emitted when a whisper is received.
```json
{
  "message": {
    "msgId": "60",
    "userId": 0,
    "username": "<username>",
    "displayName": "<user's display name>",
    "message": "Test",
    "emotes": []
  }
}
```

### Bot Whisper
Emitted when the bot sends a whisper.
```json
{
  "command": "!bots",
  "counter": 1,
  "userCounter": 1,
  "message": "",
  "user": {
    "id": 0,
    "login": "<username>",
    "display_name": "<user's display name>",
    "subscribed": true,
    "role": 4
  }
}
```

## Monetary Events

### Cheer
Emitted when bits are cheered in the channel.
```json
{
  "message": {
    "msgId": "21605e47-16d2-4496-8001-509438e1b41c",
    "userId": 0,
    "username": "<username>",
    "role": 1,
    "subscriber": true,
    "displayName": "<display name of cheerer>",
    "channel": "<channel>",
    "message": "<message that contained the cheer>",
    "isHighlighted": false,
    "isMe": false,
    "isCustomReward": false,
    "isAnonymous": false,
    "isReply": false,
    "bits": 42,
    "hasBits": true,
    "emotes": [],
    "cheerEmotes": [
      {
        "bits": 42,
        "color": "#979797",
        "type": "CheerEmote",
        "name": "Cheer",
        "startIndex": 0,
        "endIndex": 6,
        "imageUrl": "<url to cheer emote>"
      }
    ]
  }
}
```

## Subscription Events

### Sub
Emitted when a user subscribes to the channel.
```json
{
  "subTier": 0,
  "color": "#008D99",
  "emotes": [],
  "message": "",
  "userId": 0,
  "userName": "<username>",
  "displayName": "<display name>",
  "role": 1
}
```
Note: subTier values: 0 - Prime, 1 - Tier 1, 2 - Tier 2, 3 - Tier 3

### Resub
Emitted when a user resubscribes to the channel.
```json
{
  "cumulativeMonths": 25,
  "shareStreak": true,
  "streakMonths": 1,
  "subTier": 0,
  "color": "#FF4500",
  "emotes": [],
  "message": "",
  "userId": 0,
  "userName": "<username>",
  "displayName": "<display name>",
  "role": 1
}
```

### Gift Sub
Emitted when a subscription is gifted.
```json
{
  "isAnonymous": false,
  "totalSubsGifted": 1,
  "cumulativeMonths": 4,
  "monthsGifted": 1,
  "fromSubBomb": false,
  "subBombCount": 1,
  "recipientUserId": 0,
  "recipientUsername": "<username of recipient>",
  "recipientDisplayName": "<display name of recipient>",
  "subTier": 0,
  "userId": 0,
  "userName": "<username of gifter>",
  "displayName": "<displayname of gifter>",
  "role": 1
}
```

### Gift Bomb
Emitted when multiple subscriptions are gifted at once.
```json
{
  "isAnonymous": false,
  "gifts": 10,
  "totalGifts": 0,
  "subTier": 0,
  "userId": 0,
  "userName": "<username of gifter>",
  "displayName": "<displayname of gifter>",
  "role": 1
}
```

## Channel Point Events

### Reward Redemption
Emitted when a channel point reward is redeemed.
```json
{
  "id": "9d0911db-7884-4e0f-8cf4-c95c5765c2e5",
  "dateTime": "2022-01-31T03:10:23.3611616Z",
  "userId": 0,
  "userName": "<user name of redeemer>",
  "displayName": "<display name of redeemer>",
  "channelId": 0,
  "cost": 42,
  "rewardId": "41f257e9-9688-4944-9bf6-28cda1c3fa1f",
  "title": "Test Reward",
  "prompt": "",
  "inputRequired": false,
  "backgroundColor": "#63D0A9",
  "enabled": true,
  "paused": false,
  "subOnly": false
}
```

### Reward Created
Emitted when a new channel point reward is created.
```json
{
  "id": "41f257e9-9688-4944-9bf6-28cda1c3fa1f",
  "name": "Test Reward",
  "prompt": "",
  "group": "",
  "cost": 42,
  "userInput": false,
  "persistCounter": false,
  "counter": 1,
  "persistUserCounter": false,
  "backgroundColor": "#63D0A9",
  "userCounters": {}
}
```

### Reward Updated
Emitted when a channel point reward is updated.
```json
{
  "dateTime": "2022-01-31T03:10:10.9796761Z",
  "channelId": 0,
  "cost": 42,
  "rewardId": "41f257e9-9688-4944-9bf6-28cda1c3fa1f",
  "title": "Test Reward",
  "prompt": "",
  "inputRequired": false,
  "backgroundColor": "#63D0A9",
  "enabled": true,
  "paused": true,
  "subOnly": false
}
```

### Reward Deleted
Emitted when a channel point reward is deleted.
```json
{
  "dateTime": "2022-01-31T03:18:07.6679489Z",
  "channelId": 0,
  "cost": 42,
  "rewardId": "d52a0894-586e-4943-9027-385e8ea04f79",
  "title": "Test Reward",
  "prompt": "",
  "inputRequired": false
}
```

## Ad Events

### Ad Run
Emitted when an ad is run on the channel.
```json
{
  "length": 90,
  "scheduled": false
}
```

## Role Notes
User roles are represented by numbers:
- 1: Viewer
- 2: VIP
- 3: Moderator
- 4: Broadcaster