We are currently doing the cheer/bit detection incorrectly. The current way is missing some of the "Power Ups" like giantify. So instead of the curreent way, we need to refactor it to use the `ChatMessage` event from the websocket. I've put the relevant API info below


{
  "timeStamp": "2025-04-04T01:44:47.9649499-04:00",
  "event": {
    "source": "Twitch",
    "type": "ChatMessage"
  },
  "data": {
    "message": {
      "internal": false,
      "msgId": "42396d17-d046-4258-ac79-ea2f1fb15ec5",
      "userId": "84393066",
      "username": "fuzzhead93",
      "displayName": "Fuzzhead93",
      "channel": "fuzzhead93",
      "message": "fuzzheAliendance",
      "bits": 0,
      "firstMessage": false,
      "returningChatter": false,
      "hasBits": false,
	}
    "isReply": false,
    "isSharedChat": false,
    "isTest": false
  }
}