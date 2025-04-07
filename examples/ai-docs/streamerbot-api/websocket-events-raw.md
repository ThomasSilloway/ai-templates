# Streamer.bot Raw Events

This document outlines the raw events emitted by the Streamer.bot WebSocket Server.

## Action Event

Emitted when an action is executed.

```json
{
  "id": "cc8a2cd1-eb33-45b0-9f16-f752abe6fbff",
  "name": "PyramidSuccess",
  "arguments": {
    "totalPyramids": 4,
    "pyramidWidth": 3,
    "pyramidEmote": "nate121Heart"
  },
  "user": {
    "id": 0,
    "login": "<username>",
    "display_name": "<user's display name>",
    "subscribed": true,
    "role": 1
  }
}
```

### Fields Explanation
- `id`: Unique identifier for the action
- `name`: Name of the action
- `arguments`: Custom arguments passed to the action
- `user`: Information about the user who triggered the action
  - `role`: User's role level (1 - Viewer, 2 - VIP, 3 - Moderator, 4 - Broadcaster)

## SubAction Event

Emitted when a sub-action within an action is executed.

```json
{
  "parentId": "cc8a2cd1-eb33-45b0-9f16-f752abe6fbff",
  "parentName": "PyramidSuccess",
  "type": 10,
  "id": "29e34a9b-5856-4133-85eb-f812597c4d89",
  "name": "Message (Nice %pyramidWidth%-width %pyramidEmote%...)",
  "arguments": {
    "totalPyramids": 4,
    "pyramidWidth": 3,
    "pyramidEmote": "nate121Heart",
    "user": "<user's display name>",
    "userName": "<username>",
    "userId": 0,
    "isSubscribed": true,
    "isModerator": false,
    "isVip": false,
    "broadcastUser": "nate1280",
    "broadcastUserName": "nate1280",
    "broadcastUserId": 0,
    "broadcasterIsAffiliate": true,
    "broadcasterIsPartner": false,
    "randomUser0": "<user's display name>",
    "randomUserName0": "<username>",
    "randomUserId0": 0,
    "randomUser1": "<user's display name>",
    "randomUserName1": "<username>",
    "randomUserId1": 0,
    "randomUser2": "<user's display name>",
    "randomUserName2": "<username>",
    "randomUserId2": 0
  },
  "user": {
    "id": 0,
    "login": "<username>",
    "display_name": "<user's display name>",
    "subscribed": true,
    "role": 1
  }
}
```

### Fields Explanation
- `parentId`: ID of the parent action
- `parentName`: Name of the parent action
- `type`: Type identifier for the sub-action
- `id`: Unique identifier for the sub-action
- `name`: Name/description of the sub-action
- `arguments`: Contains various context variables and arguments:
  - Action-specific arguments (e.g., `totalPyramids`, `pyramidWidth`)
  - User context (`user`, `userName`, `userId`)
  - User status flags (`isSubscribed`, `isModerator`, `isVip`)
  - Broadcaster information
  - Random user selections (up to 3 random users)
- `user`: Information about the user who triggered the action
  - `role`: User's role level (1 - Viewer, 2 - VIP, 3 - Moderator, 4 - Broadcaster)

> Note: The arguments object can vary depending on the type of sub-action being executed.