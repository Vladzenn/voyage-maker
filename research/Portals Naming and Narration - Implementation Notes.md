# Portals, naming and narration: implementation notes

2026-10-27. Based on the current Schools of Magic world export and the user's new regional-expedition, portal, naming, narrator and developer-testing directions. Source worlds remain read-only. New destination names, sites and connective cultural details are authored draft suggestions under that request.

## Geography and travel

The main realm and its existing mapped region are now both **Glowhaven**. This keeps the region label consistent with its actual scope: the city, farms, woods, coast and neighboring settlements. Existing coordinates and images are retained. **Drakenspire Mountains** and **Asterveil Sky Archipelago** are separate realm maps for distant regions of the same world. The existing **Wraith Island Prison** realm remains a physical prison map offshore from Glowhaven.

The community realm guide documents key/name consistency, parent-region references and movement via a destination location. Moving to a location updates the parent realm and region. This supports named endpoint travel without inventing portal-specific schema fields. The author's geographical use of realms takes precedence over the guide's preference for planar scenarios. [Community realm reference](https://wiki.unofficial.voyage/world/realms)

The new Portal Room is an area inside Evertree Base, joined to Rear Palace Walk. Two outbound and two return triggers use exact location/area gates, a declared player-action check, supported discovery effects, and location/area movement. Destination maps begin undiscovered. A permitted explicit crossing reveals its destination and arrives at the authored endpoint. Return goes specifically to the Portal Room. Visitors need actual transit permission but do not need to cast the portal.

Permission and route availability in the action gate are AI-judged. The local fixtures supply these decisions; they do not establish that the live AI will judge them correctly. The travel effects move a party: the authored queries require solo play or the whole active player party traveling together. Independent split-party portal movement is not implemented. Native map travel and an available portal need live testing together, especially after both realms have become known.

`newRegionGenerationEnabled` is now false, matching both ChikaraOld and Luxcellia. That switch controls automatic new-region creation. Additional task instructions prohibit invented realms and off-map destinations, preserve chosen routes, and anchor any new local site within an existing region. They do not claim a separate undocumented engine switch for realm generation. [Community location settings](https://wiki.unofficial.voyage/other/locationSettings)

## Expedition correction

Leaving the city walls is no longer sufficient. The expedition quest is renamed **Beyond Glowhaven: An Authorized Expedition**, with all references updated. Its fieldwork script now requires Drakenspire Mountains or Asterveil Sky Archipelago, actual recorded authorization, and the existing semantic completed-objective gate. Local countryside and the prison realm are rejected. The fieldwork ledger records realm, region and location as well as the scene and tick.

The destination requirement is map-based, not species- or spell-based. A permitted route survey, negotiation, protective assessment, craft investigation, habitat observation or relic documentation can count when it is the authorized objective and actually completed. Portal arrival alone does not count. Local Genzō Iwakura woodland practice remains useful without becoming distant expedition credit.

## Naming comparison

Observed in the supplied files: ChikaraOld has **10** filter entries; Luxcellia has **291**; Glowhaven previously had **20**. More entries do not by themselves prove better names. Luxcellia provides broader coverage of recurring fantasy-name patterns, while Chikara demonstrates that much of a world's cultural naming consistency also lives in its cast and generation guidance.

Glowhaven now has **261** name-replacement entries. The old given-name-to-full-name substitutions were corrected: given names replace given names, surnames replace surnames. This avoids a replacement such as a full Japanese name receiving another generated surname. Replacement strings are nonempty name tokens, not prose deletion commands. The community reference describes this field as name replacement, not a general story-word censor. [Community name-filter reference](https://wiki.unofficial.voyage/other/nameFilterSettings)

All tokens in the existing cast's canonical full names are protected from becoming forbidden keys. Full-name random pools are expanded without adding authored NPCs or duplicating their exact names. Generation guidance enforces First name Last name, canonical diacritics, existing-cast reuse and identity continuity. French/Elvish and established foreign names remain valid; Japanese-inspired names are the default for new Glowhaven locals, not a universal rule for every people.

The native filter has no authored gender/culture routing condition here. Its alternatives follow the intended source-name category, while context-sensitive decisions remain generation guidance. It cannot guarantee a perfectly unique new name; actual duplicate avoidance needs observation in play.

## Narrator comparison

Chikara contributes attention to routine, contrasting peaceful life and danger, distinct voices and sincere escalation. Luxcellia contributes appealing sensory scenes, strong visual character identity, committed comedy, energetic action and focus on the people actually present. These are observed stylistic patterns, not copied setting rules or a claim that one narrator is universally best.

The dedicated narrator style is **1,707 characters**, within the community-documented 2,000-character limit. Detailed travel, identity and player-path guidance lives in relevant AI tasks rather than overflowing that field. [Community narrator-style reference](https://wiki.unofficial.voyage/other/narratorStyle)

Warriors, brawlers, craftspeople, merchants, investigators and noncasters receive the same narrative attention as mages. Practical tools, physical positioning, negotiation and retreat can matter. Ordinary physical actions acquire no automatic MP cost. The world remains rich in magic without inventing a mandatory magical identity or academy enrollment for the player. Serious scenes retain weight; character flaws are not silently softened, and every quiet visit need not become an emergency.

## Developer preset

**Developer Playtester** is a selectable, explicitly noncanonical premade. It does not replace an NPC. Its premade-only Developer Playtest Kit supplies every actual authored skill at 100, all ten existing techniques, six ordinary equipment types, 100,000 marks, and modifiers producing initial 100,000 HP/MP maxima before normal level scaling.

Premades receive skills, resources, items and abilities through traits in the community-documented pipeline. The normal starting attribute cap remains 16; instead of pretending a preset bypasses it, a player-scoped runtime trigger sets all six attributes and character level to 100. A separate marker prevents repeating setup and permits a later eligible tester to initialize without changing ordinary party members. [Community premade reference](https://wiki.unofficial.voyage/world/premadeCharacters), [trait reference](https://wiki.unofficial.voyage/mechanics/traits)

The traits are absent from normal selection categories and the level-up pool. Choose the preset, retain its developer trait if customizing, and use any existing start. Ask to inspect Evertree Base's Portal Room; its test background allows arranged inspection access without a long permit subplot. The preset grants no automatic quest outcomes, hidden knowledge, mind control, universal invulnerability or new NPC role. No portrait URL was fabricated. Normal saves are still needed to test balance and progression.

## Verification

Local JSON, size, references, name-token, existing-media, map and roster-preservation checks pass. Nineteen fixtures test script compilation, endpoint-only round trips, negative travel decisions, distant-only expedition credit, actual authorization, and developer setup in ordinary and mixed parties. The fixtures execute authored code and mock the documented effects; semantic decisions are supplied test inputs.

No full platform validator, live Studio import, AI-classification trial, multiplayer travel session or gameplay playtest was performed. Existing-save migration is not included. Use a new test game for the changed quest key and definitions.
