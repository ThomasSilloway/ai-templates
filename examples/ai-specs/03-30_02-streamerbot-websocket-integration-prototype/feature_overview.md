Set up an initial prototype for connecting to Streamer.bot websocket server.

## Settings tab

- add some connection status to the websocket server info, whatever you think would be a nice display for a dashboard.

- Maybe we need some input fields to configure the connection?

## DebugConsole tab

Subscribe to the `Raw` websocket server event so we can see all of the actions that are executed.

For each action executed add to the debugconsole this line: `ACTION: <actionname> Args: "arg1": "value1", "arg2": "value2", etc`

- For any values that are more than 20 characters, truncate them

For each subaction executed add the same as above for debugconsole bug prefix with `[ParentActionName] <subactionname> Args: same as above, etc`
