A couple of notes to iterate on

    - Need to make sure code files are 500 lines or less, if they are more they should be broken into smaller components.
    - Please include all monetization items in the pointConfiguration section from @\ai-docs\streamerbot-api\websocket-events-twitch.md
    TypeScript
```
userPendingPoints: Writable<{ // Pending points by user
  [userId: string]: {
    beard: number;
    shave: number;
  }
}>;
``` - This is incorrect, it should only store a single number of pending points per user, then they're able to assign whichever side they want with the ! command eventually

- I forgot to mention we also need a reset button the debug panel below the progress bar

- `Debug Panel Layout` is correct except the point settings should go on the existing `Settings` tab.  This debug panel on the progress bar tab should only contain information and the buttons



V2 

- `bitsMultiplier` let's change this to points per 100 bits

- primeSubPoints, tier1SubPoints, giftSubPoints should all come from the same configuration variable, so let's not include 3 different configurations, but also note in the doc that each of these should be set by the same config variable