# Steel and Spirits — location artwork and portal review

## Scope and current evidence

Completed one establishing shot for each of the 109 new locations across Akitsuhara and the Veiled Beyond, plus a separate interior shot for Benitsuru Portal Shrine - Portal Hall. Other nested areas and old-world images are outside this batch. All 110 original PNGs are 1254 × 1254, generated with the built-in tool under the existing location-art guide. Per-image checkpoints and official upload receipts in `tools/oni-nation/location-art/` record 110 distinct hashes and hosted URLs. Generation and upload are not a Studio save or publication.

Each job records its exact parent location, optional nested area, API target, prompt and project filename. PNGs retain their original pixels. The official upload routine records actual SHA-256, dimensions and returned hosted URL, and resumes completed work without another upload. The final merge changes only selected establishing-shot fields and default crops for previously unillustrated records. Its reversible comparison proves every other field unchanged. All 285 latest supplied pins/regions remain exact. No existing valid artwork was replaced. Official Creator API draft validation returns zero errors and warnings; `official-validation.json` and `merge-report.json` retain the evidence.

The final six labeled contact sheets were visually reviewed. The set differentiates snowy northern passes, lakeside towns, bamboo, the capital, farmland, redleaf streets and dim spirit wilderness. Some archives and shrines look grander than their modest roles, and a few decorations resemble calligraphy or musical symbols. Portal Hall uses an open pillared hall with Evertree/root imagery through the portal. These are review caveats, not claims of perfect geographical or crop fidelity. No completed image was silently rerolled. Check actual arrival-card/banner crops in Voyage.

Deliveries are in `output/steel-and-spirits-art-2026-11-03/`: full world, locations-only JSON, all 110 named originals in a ZIP, the coordinate/URL CSV and six review sheets. Use the full world import to carry the cross-section shrine rename.

## Author placements and shrine name

Export `23da8cc9-d365-41ab-8dde-4aacbe87a199` supplies five newer Mirror-Reed pins. Export `f940372c-656b-461b-9bd6-1625c8088cd4` then changes Bellroot Refuge, The Listening Cedars and Ashen Festival Road. The later export owns all 285 location coordinates and region assignments. Their images and all other fields are preserved. Exact before/after values and source hashes are in `source-merge.json` and `latest-placement.json`.

**Benitsuru Transit Shrine** becomes **Benitsuru Portal Shrine** throughout the live world: location/area keys, paths, NPC placement, portal destinations, quest references, item descriptions and source fixtures. This is a name change at the same pin, not a second portal building. The separate Moonless Torii is unchanged.

## Portal audit

The implementation retains the existing fixed destinations, reusable keys, companion moves and shared per-turn crossing lock. The new regression cases execute actual emitted scripts with supplied semantic answers; they do not prove live AI recognition.

| Route | Outward condition | Return |
| --- | --- | --- |
| Evertree to Drakenspire | Genuine Drakenspire Portal Key; actual crossing | Drakenspire Portals to Evertree Base - Portal Room |
| Evertree to Asterveil | Genuine Asterveil Portal Key; actual crossing | Cloudbloom Landing to Evertree Base - Portal Room |
| Evertree to Akitsuhara | Genuine Oni Nation Portal Key; actual crossing | Benitsuru Portal Shrine to Evertree Base - Portal Room |
| Evertree to the Silken Descent | Existing anomaly/discovery and Silver Web route | Existing entrance arch to Evertree, without descent or boss victory |
| Evertree to the Sepulchral Conservatory | Existing earned discovery/open passage | Sepulchral Portal House to Evertree Base - Portal Room |
| Moonless Torii to the Veiled Beyond | Existing permanently awakened Soul Torii | Veiled Threshold to Moonless Torii in Akitsuhara |
| Wraith Island Prison | Existing custody/visitor transport | Existing release/transport; no public portal-key escape |

Fixed home arches still allow retreat without a key; carrying a key is not remote teleportation from an arbitrary street. Court/delegated issuance remains distinct from simply requesting a key. The three foreign transit desks can approve an appropriate Glowhaven journey locally. Existing post-transit grants retain their single owner and avoid a second held copy.

Two narrow changes accompany the rename. Benitsuru’s direct solo shortcut now recognizes explicit use of a held Glowhaven Portal Key. Both Oni direct shortcuts require a solo session, leaving multiplayer to the existing semantic consent gate. The Conservatory return query explicitly recognizes its held return key. No trigger is added, no key is consumed, and no Spider trigger, enemy, quest or difficulty is changed.

## Prototype clarification

Shigure Tsubakiri’s concealed prototype is an oversized articulated Magitech polearm: crystal-fed braces unfold around a cutting staff. Setup, charging, recovery and overheating limit it. Hatsu Kanesue maintains the mechanism and knows its overheating problem. It is secret character equipment/story material, not a separately configured catalogue weapon or an automatically awarded item. Public images must not reveal it merely because Shigure appears.

## Required live review

Inspect the location arrival-card and banner crops in Voyage. Test key handovers to foreign starters, explicit key-use wording, free fixed returns and the renamed shrine’s NPC/quest references. Verify shared-party consent in multiplayer. Local fixtures and official draft schema validation are separate from those live tests.

Documentation consulted: [community trigger reference](https://wiki.unofficial.voyage/mechanics/triggerDefinitions), [community location schema](https://wiki.unofficial.voyage/world/locations), and the live official Creator API OpenAPI contract retrieved by the upload client. The wiki is community-maintained, not an official guarantee of runtime narration.
