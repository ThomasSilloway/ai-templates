# Streamer.bot Command Events

This document outlines all command-related events emitted by the Streamer.bot WebSocket Server.

## Subscribing to Command Events

To enable Command events, send the following Subscribe request:

```json
{
  "request": "Subscribe",
  "id": "my-subscribe-id",
  "events": {
    "Command": [
      "Triggered",
      "Cooldown"
    ]
  }
}
```

## Available Events

### Triggered

Emitted when a command is triggered by a user.

```json
{
  "command": "!bots",
  "counter": 1,
  "userCounter": 1,
  "message": "",
  "user": {
    "id": 00000000,
    "login": "<username>",
    "display_name": "<user's display name>",
    "subscribed": true,
    "role": 4
  }
}
```

#### Fields Explanation
- `command`: The command that was triggered
- `counter`: Global counter for how many times this command has been used
- `userCounter`: Counter for how many times this user has used this command
- `message`: Any additional message content after the command
- `user`: Object containing information about the user who triggered the command
  - `id`: User's unique identifier
  - `login`: User's login name
  - `display_name`: User's display name
  - `subscribed`: Whether the user is subscribed
  - `role`: User's role level (4 indicates higher privileges)

### Cooldown

Emitted when a command is on cooldown.

```json
{
  "command": "!bots",
  "cooldownLeft": 11,
  "globalCooldownLeft": 11,
  "userCooldownLeft": 0,
  "message": "",
  "user": {
    "id": 00000000,
    "login": "<username>",
    "display_name": "<user's display name>",
    "subscribed": false,
    "role": 1
  }
}
```

#### Fields Explanation
- `command`: The command that is on cooldown
- `cooldownLeft`: Time remaining on the cooldown in seconds
- `globalCooldownLeft`: Time remaining on the global cooldown in seconds
- `userCooldownLeft`: Time remaining on the user-specific cooldown in seconds
- `message`: Any additional message content that was sent with the command
- `user`: Object containing information about the user who attempted to use the command
  - `id`: User's unique identifier
  - `login`: User's login name
  - `display_name`: User's display name
  - `subscribed`: Whether the user is subscribed
  - `role`: User's role level (1 indicates standard privileges)