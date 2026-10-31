> Import correction: the Alpha25/26 full exports contain eight invalid quest completionCondition strings. Use Alpha27, which preserves this content and fixes their typed object shape.

# Alpha26 — Site Danger, AuthorSeeds and Image Merge

Use **GlowhavenAlpha26 - Site Danger and Author Seeds.json**, identical to WorldAlpha - World.json. This contains Alpha25's first-day/appearance update plus the latest supplied images and positions.

## Lossless merge

The pasted export was still based on Alpha24. A three-way merge against the preserved Alpha24 release applies its image/position changes without rolling back Alpha25. **All 77 incoming changed fields were verified:** 12 NPC portrait URLs, 59 location image objects (including supplied crop settings) and six coordinate values. There were no merge conflicts. Other coordinates and existing images remain unchanged. The incoming file itself was not edited.

## Danger within locations

Corrected the earlier diagnosis: **locationSettings.encountersEnabled controls unscripted travel encounters**, not a universal switch for every local threat. Its supplied value remains **false**. New-region generation also stays disabled. A local NPC, guardian or physical hazard does not require another journey roll.

Fifteen location archetypes now include three new concrete patterns—Hunted Ground, Guardians Without Masters and The Ground Will Not Hold—and stronger Outer Route and Field Site / Restricted or Dangerous Site entries. They describe habitats, relevant existing npcTypes, motives, physical hazards, counterplay, safer approaches and remembered resolutions. Archetypes are generation guidance, not per-location attachment fields or automatic spawn tables. Region archetypes were left unchanged; they are not a danger slider.

Because all these locations are already detailed, templates alone would not update them. Applied local danger facts to **37 existing sites**: fifteen Glowhaven/Drakenspire sites and twenty-two Asterveil wilderness sites. Added physical cues to the relevant fifteen existing area descriptions. Wolves, boars, web hunters, wyverns, giants and surviving mechanisms fit their actual habitats; ice, water, snow and unstable masonry can be dangerous without a monster. Five previously unbounded Glowhaven locations gain modest local generated-NPC bands. No authored NPC's level, health or other stats changed. A band constrains new individuals; it is not a hostility setting.

Six maintained Asterveil hubs and the Silken arrival refuge explicitly resist ambient monster placement. Investigating occupied hunting/guarding ground should produce an actual finite opponent when appropriate rather than endless tracks. Current creatures are reused, cleared danger stays resolved, ordinary wildlife can remain neutral, and actual opponents/actions are needed before combat damage. New-NPC guidance now explicitly permits a real finite creature encounter even if the creature will not become a recurring story character.

**No new triggers were added or edited.** All 300 triggers, 116 quests, 480 abilities, resources and progression settings match Alpha25. The Spider Realm's existing finite pack and boss mechanics remain; they were not replaced by speculative generation. Rare unique creatures keep their actual contact rules. The location-archetype-only approach cannot guarantee a runtime spawn; this pass improves the local records and AI routing and still needs playtesting.

## AuthorSeeds

The old single general checklist was valid but supplied no variety. Replaced it with **sixteen focused five-line writing lenses**. The [research report](../research/NPC%20Author%20Seeds%20-%20Research%20and%20Revamp.md) explains the selection mechanism, reference-version difference and design choices. The standalone **WorldAlpha - Author Seeds.json** is a plain section map for Studio replacement.

Under the [community documentation](https://wiki.unofficial.voyage/other/authorSeeds), only one lens is randomly supplied for strong/elite/boss/mythic NPC detail generation; ordinary lower tiers do not receive the pool. Shared instructions preserve basic quality for all tiers and prevent a lens from assigning power, changing an existing identity, forcing romance, or making a nonhumanoid behave as an employed human. The sixteen entries are alternatives, not sixteen mandatory character features. Existing authored cards were not regenerated.

## Verification

- **3,946 local checks passed**, covering all incoming image/position edits, protected Alpha25 content, type/area references, seed structure, scope, instruction budgets, map metadata and safe hubs.
- **226 existing script/offer checks passed** across eleven guild contracts.
- Twenty-one standalone maps match the full export, including the new Author Seeds and Location Archetypes files.
- Preserved 205 NPCs, 173 locations, 480 abilities, 116 quests, 300 triggers and fourteen story starts. All first-day, instructor and appearance changes survive the older-export image merge.

No Studio import, live NPC-generation sample, combat test, multiplayer test or existing-save migration was performed. Test a fresh game. The practical test is to enter an occupied local danger area without first traveling to another location: a finite real threat should emerge where warranted. Then retreat, return and check persistence. Compare a quiet town visit and a maintained refuge; neither should inherit a monster because the region contains dangerous wildlife. Check a seeded strong humanoid and a strong nonhumanoid separately. These are model-directed behaviors, not certified guarantees.

## References

- [NPC AuthorSeeds](https://wiki.unofficial.voyage/other/authorSeeds): community schema and random-selection scope.
- [Location Archetypes](https://wiki.unofficial.voyage/other/locationArchetypes) and [Location Details](https://wiki.unofficial.voyage/ai/generateLocationDetails): reusable directions for generating/expanding places, not encounter-table switches.
- [Location Settings](https://wiki.unofficial.voyage/other/locationSettings), [Encounters](https://wiki.unofficial.voyage/ai/generateEncounters) and [Encounter Elements](https://wiki.unofficial.voyage/other/encounterElements): travel encounter controls and ingredient palette.
- [Locations](https://wiki.unofficial.voyage/world/locations): local area/path structure and when detailed generation runs.
- Local read-only Luxcellia exports: observed structural comparisons, not proof of the current screenshot version or automatic correctness.

The precise schema guidance above comes from community documentation and inspected exports. The actual new profiles, seed directives and scene routing are this project's design, with runtime outcomes still to test.
