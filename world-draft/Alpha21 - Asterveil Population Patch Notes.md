# Alpha21 — Asterveil Population

Updated from the current Alpha20 canonical world. The complete import is **GlowhavenAlpha21 - Asterveil Population.json**.

- Added twelve NPCs: the two Kazahana sisters, two major visitors, seven minor residents and Orivelle. Total roster: 205. Four major people retain flashier portrait treatment; the unique beast uses special-anatomy framing within the eight minor slots.
- Created twelve exact-name PNG portraits and twelve complete cards using the established headings. All eleven humanoids are adults; short fae have mature adult proportions. Portrait generation used the built-in tool, one pass each; review flags are in Asterveil - Portraits.md.
- Added varied fae anatomy lore and a reusable appearance-selection guide, with recorded random stature, morphology, ears, optional-feature and affinity-count draws. The current player-creation traits and menus are unchanged.
- Preserved independent household government and clarified that Asterveil allowed the Glowhaven portal. Expanded existing civic/cooperative descriptions without adding a new faction for every worker.
- Anchored eighteen existing expedition commissions to authored contacts. Reports can be relayed through the actual registry while scientific work keeps its specialist. Rewards, objective gates, quest keys, offer/report locations and progression remain.
- Added a four-day Orivelle circuit with native placement, plus scoped detention/release pause rules: three triggers total. The Veilhook Ray hunt and ordinary npcTypes remain separate.
- Added individual-faerie identity guidance to the relevant NPC generation and portrait instructions. This is conditional on the subject being fae; the rest of the cast is not changed into fae.

Preservation: all 193 existing NPC records, including hosted portraits, remain byte-value equivalent as parsed JSON. Every existing location’s coordinates, region, radius, paths and images are retained. No locations, areas, player traits, skills, resources, abilities, story starts, portal rules or dungeon progression rules were added or removed. Existing author-supplied trigger removals remain removed. New portraits need manual Voyage upload; no fake URLs were inserted.

Validation passed: **5,173 local structural/reference/preservation checks** and **2,404 local script/state fixtures and script compilations**. All eighteen standalone section maps are synchronized with the full export. This is not a live Voyage import, a playtest or a migration of an existing save.

Technical basis: the community [trigger reference](https://wiki.unofficial.voyage/mechanics/triggerDefinitions) documents day conditions, NPC state checks, persistent storage and native placement. The [NPC reference](https://wiki.unofficial.voyage/world/npcs) documents catalogue records, types and visibility. Live behavior still needs the checks below; documentation is not proof of this world’s live execution.

Manual playtest:

1. Import the complete world and check Studio validation. Upload the twelve PNGs to their matching records.
2. Visit each staffed hub and verify that authored people are reused, with small foreground groups and the correct current area.
3. Ask the sisters about each other, meet the married owners and test the visitors’ independent plans. Friendship does not recruit them.
4. Read and take existing commissions at their original offer places. Submit Canopy reports through Sakuya Tomonari and conservatory reports through Kureha Kazahana. Rewards must pay once as before.
5. Advance the actual day through four stops and a second circuit. The route should move one persistent Orivelle without revealing or teleporting the player.
6. Cross a day boundary while Orivelle is in scene, fighting or in the party. It must stay through that encounter and catch up after the relevant guard ends.
7. Test genuine restraint, false claims of restraint, real release and an unrelated release story. The pause flag must reflect the actual beast’s current circumstances.
8. Defeat or kill it in a test save and advance days. It must not resurrect or be replaced. Confirm the separate Veilhook Ray remains the actual hunt quarry.
9. Generate one incidental fae: check that its individual anatomy reaches the visual description and image prompt. Generated visual compliance remains probabilistic.

Portrait limitation: several outputs use less top margin than requested, and Sakuya Tomonari’s image adds unapproved wings. Written cards and lore remain authoritative. No corrective generation was silently performed.
