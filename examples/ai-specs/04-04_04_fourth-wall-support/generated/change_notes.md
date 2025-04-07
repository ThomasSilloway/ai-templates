## v01 - Fourth Wall Event Scaffolding

Added initial scaffolding for handling Fourth Wall events (Donation, Gift Purchase, Order Placed).

* Updated `stores/progress.ts` to include configuration fields (`fourthwallDonationPointsPerDollar`, `fourthwallGiftPurchasePoints`, `fourthwallOrderPlacedPoints`) and default values in `pointConfiguration`
* Modified `components/settings/PointConfigForm.svelte` to add a new "FourthWall Rewards" section with corresponding inputs, placed between "Resub Bonuses" and "Progress Bar Configuration"
* Created `services/FourthWallService.ts` as a Singleton service with handlers (`handleDonation`, `handleGiftPurchase`, `handleOrderPlaced`) to log raw event payloads to the debug console
* Integrated `FourthWallService` into `services/StreamerbotService.ts` by adding instantiation, subscribing to `Fourthwall.Donation`, `Fourthwall.GiftPurchase`, `Fourthwall.OrderPlaced` events, and routing them to the new service's handlers

#### Review Notes

* Verified implementation against PRD requirements - all requirements from sections 3.1, 3.2, 3.3, and 3.4 met.
* Confirmed correct fields (`fourthwallDonationPointsPerDollar`, `fourthwallGiftPurchasePoints`, `fourthwallOrderPlacedPoints`) and defaults in `progress.ts`.
* Confirmed UI elements layout and bindings in `PointConfigForm.svelte` matches requirements.
* Confirmed `FourthWallService.ts` follows Singleton pattern and correctly implements logging for each event type.
* Confirmed `StreamerbotService.ts` properly integrates with FourthWall by instantiating service and setting up event routing.
* Confirmed trailing newlines exist in all modified files (`progress.ts`, `PointConfigForm.svelte`, `FourthWallService.ts`, `StreamerbotService.ts`).