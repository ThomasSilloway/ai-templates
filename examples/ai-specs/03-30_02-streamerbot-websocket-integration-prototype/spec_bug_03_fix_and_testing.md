# twitch-interactive-app

## High Level Overview
 We just implemented a new feature. We found a bug in the implementation. If more logging is needed, let's add more. If not, please fix the bug and I'll retry to see if it's fixed.

 Follow the steps below, starting with the first one and then choose the next task based off of the instructions.

## Logs 
```
[2025-03-30T07:41:25.871Z] Setting up event subscriptions...
[2025-03-30T07:41:25.872Z] Event subscriptions configured
[2025-03-30T07:41:25.872Z] Event handlers registered
[2025-03-30T07:41:25.876Z] Connected to Streamer.bot Streamer.bot v0.2.6
[2025-03-30T07:41:38.309Z] Raw.Action event received
[2025-03-30T07:41:38.309Z] DEBUG: Action event data received: {
  "timeStamp": "2025-03-30T03:41:38.3079792-04:00",
  "event": {
    "source": "Raw",
    "type": "Action"
  },
  "data": {
    "id": "686cd3ee-6b86-4672-bf0f-95bd5f50d323",
    "actionId": "ade5d835-58d5-4c14-a192-0ac8fb89fb58",
    "name": "TestActionForApp",
    "arguments": {
      "isTest": true,
      "triggerId": "839c529c-ab66-43d5-9605-7fc10cabfe3d",
      "triggerName": "Test",
      "triggerCategory": "Core",
      "actionId": "ade5d835-58d5-4c14-a192-0ac8fb89fb58",
      "actionName": "TestActionForApp",
      "eventSource": "misc",
      "runningActionId": "686cd3ee-6b86-4672-bf0f-95bd5f50d323",
      "actionQueuedAt": "2025-03-30T03:41:38.3079792-04:00"
    }
  }
}
[2025-03-30T07:41:38.310Z] Raw.SubAction event received
[2025-03-30T07:41:38.310Z] DEBUG: SubAction event data received: {
  "timeStamp": "2025-03-30T03:41:38.3079792-04:00",
  "event": {
    "source": "Raw",
    "type": "SubAction"
  },
  "data": {
    "parentId": "ade5d835-58d5-4c14-a192-0ac8fb89fb58",
    "parentName": "TestActionForApp",
    "type": 1020,
    "id": "686cd3ee-6b86-4672-bf0f-95bd5f50d323",
    "actionId": "bdf210df-e2bb-4377-82bb-0a0d89d674da",
    "name": "Log Information (test action)",
    "arguments": {
      "isTest": true,
      "triggerId": "839c529c-ab66-43d5-9605-7fc10cabfe3d",
      "triggerName": "Test",
      "triggerCategory": "Core",
      "actionId": "ade5d835-58d5-4c14-a192-0ac8fb89fb58",
      "actionName": "TestActionForApp",
      "eventSource": "misc",
      "runningActionId": "686cd3ee-6b86-4672-bf0f-95bd5f50d323",
      "actionQueuedAt": "2025-03-30T03:41:38.3079792-04:00"
    }
  }
}
```
## Feature info

Set up an initial prototype for connecting to Streamer.bot websocket server.

### Settings tab

- add some connection status to the websocket server info, whatever you think would be a nice display for a dashboard.

- Maybe we need some input fields to configure the connection?

### DebugConsole tab

Subscribe to the `Raw` websocket server event so we can see all of the actions that are executed.

For each action executed add to the debugconsole this line: `ACTION: <actionname> Args: "arg1": "value1", "arg2": "value2", etc`

- For any values that are more than 20 characters, truncate them

For each subaction executed add the same as above for debugconsole bug prefix with `[ParentActionName] <subactionname> Args: same as above, etc`
 
## Project Details
The Twitch App Prototype is a SvelteKit-based application featuring a three-tab interface (Progress Bar, Settings, and Debug) with seamless tab switching powered by a shared state management system. The Debug console implements a sophisticated color-coding system that visually distinguishes between different types of Twitch events (subscriptions in green, bits in purple, and general messages in gray) to enhance readability and event tracking. The app utilizes a persistent message store that maintains debug messages across tab switches, preparing for future integration with Streamer.bot's websocket API. The development environment is containerized using Docker, with separate configurations for development (with hot-reload) and production, making it easy to develop and deploy across different environments.

## Tasks
Perform the following tasks in order:

### Fix Bug Plan
```
- ASK me any questions about the bug or code files you might have before proceeding
- WRITE bug_fix_plan.md with the details of how to fix the bug. Use same directory as the `bug_description.md`
- ASK me to review the new document and provide feedback
```

### Fix the bug
```
- IMPLEMENT the bug_fix_plan.md plan
- ASK me to run the app again and check functionality
- After reading my feedback: 
 - CHOOSE the next task below, whichever seems more appropriate [Complete] or [Fix Bug] or [Add more logging]
```

### Add more logging
```
 - READ Related logs
 - ANALYZE the code files and the logs to spot potential issues
 - ADD Logging to help observability of any issues - logs should be output to the DebugConsole in the app
 - ASK me to run the app again and gather the logs 
 ```

 ### Complete
 ```
 - WRITE bug_fix_learnings.md with the details of what worked, what didn't work from this process. Use same directory as the `bug_description.md`
 ```
