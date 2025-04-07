## High Level Overview
 We just implemented a new feature. I've provided the details of a bug that's occuring, please document it.

  Follow each task below one by one, make sure not to skip any steps.

## Docs

- None

## Bug description

Uncaught (in promise) TypeError: first_child_getter is undefined

  in root.svelte
    get_first_child operations.js:86
    template template.js:55
    add_locations elements.js:13
    _layout +layout.svelte:38
    effect2 hmr.js:47
    update_reaction runtime.js:430
    update_effect runtime.js:596
    create_effect effects.js:118
    branch effects.js:360
    wrapper hmr.js:38
    update_reaction runtime.js:430
    update_effect runtime.js:596
    create_effect effects.js:118
    block effects.js:352
    wrapper hmr.js:28
    consequent root.svelte:77
    effect2 chunk-JU7SRYCE.js:1151
    update_reaction runtime.js:430
    update_effect runtime.js:596
    create_effect effects.js:118
    branch effects.js:360
    component chunk-JU7SRYCE.js:1151
    update_reaction runtime.js:430
    update_effect runtime.js:596
    create_effect effects.js:118
    block effects.js:352
    component chunk-JU7SRYCE.js:1144
    consequent root.svelte:75
    consequent_effect chunk-JU7SRYCE.js:497
    update_reaction runtime.js:430
    update_effect runtime.js:596
    create_effect effects.js:118
    branch effects.js:360
    update_branch chunk-JU7SRYCE.js:497
    set_branch chunk-JU7SRYCE.js:462
    Root root.svelte:45
    if_block chunk-JU7SRYCE.js:522
    update_reaction runtime.js:430
    update_effect runtime.js:596
    create_effect effects.js:118
    block effects.js:352
    if_block chunk-JU7SRYCE.js:520
    Root root.svelte:141
    effect2 chunk-JU7SRYCE.js:283
    update_reaction runtime.js:430
    update_effect runtime.js:596
    create_effect effects.js:118
    branch effects.js:360
    wrapper chunk-JU7SRYCE.js:277
    update_reaction runtime.js:430
    update_effect runtime.js:596
    create_effect effects.js:118
    block effects.js:352
    wrapper chunk-JU7SRYCE.js:270
    unmount2 render.js:229
    update_reaction runtime.js:430
    update_effect runtime.js:596
    create_effect effects.js:118
    branch effects.js:360
    unmount2 render.js:211
    update_reaction runtime.js:430
    update_effect runtime.js:596
    create_effect effects.js:118
    component_root effects.js:244
    _mount render.js:208
    hydrate render.js:123
    Svelte4Component legacy-client.js:113
    <anonymous> legacy-client.js:52
    initialize client.js:472
    _hydrate client.js:2652

## Feature info

a dynamic progress bar to track "beard" versus "shave" points. The feature will include a main visual bar, a preview bar showing pending points, and smooth animations. Point configuration settings for different monetization methods (bits, subs, tiers) will be managed in a separate settings tab. A debug panel is required for monitoring values, testing point additions, and resetting progress. Development emphasizes modular components and keeping code files under 500 lines.
 
## Project Details

This SvelteKit-based Twitch app prototype features a multi-tab interface (including Settings and Debug) powered by shared state management. Core functionality involves integrating with Streamer.bot via its WebSocket SDK for event handling. The Settings tab allows users to configure the connection (host, port, hidden arguments) and view the connection status. A Debug console displays formatted Streamer.bot actions/sub-actions with color-coding and truncation for long values. The app utilizes persistent stores for configuration and debug messages, and is containerized with Docker for development and deployment.

## Tasks
Perform the following tasks in order:

### Read docs and request updated scene files
```
 - READ All docs in the `## Docs` section
 - TELL ME which docs are already in your context
 - TELL ME which docs are not already in your context from the lists above
 - READ all the docs that are not yet in your context
 ```

### Create bug report
```
Record your notes about the bug in a new file inside .\generated\bugs\
- Find the highest bug number folder in the generated\bugs folder
- Naming convention: Bug_<number + 1>_<Bug_Description>
- Note the bug description in the folder name should be 5 words or less
- Example: Bug_01_Signal_Connection_API_Incompatibility
- CREATE the new folder with that name in .\generated\bugs\
- Then write the bug description into a new file inside the folder called `bug_description.md`
- Do not write any possible solutions in the bug report, just details about the bug
- ASK ME to review the bug report before doing anything else
```
