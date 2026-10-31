# Glowhaven Alpha 6 — World Foundation, Authored Openings and NPC Types

2026-10-28. The complete export is **GlowhavenAlpha6 - World.json**. **WorldAlpha - World.json** is the identical canonical working copy. This remains an alpha export for the author's image pass; the beta milestone has not been assigned automatically.

## The central correction

The previous overview matched the supplied excerpt and did give a recent expedition disproportionate weight. This revision separates the stable setting, general generation behavior and particular story situations. A dormant plot stays available through its own lore, quests, characters, locations and triggers; it no longer supplies the agenda for every unrelated scene.

The overview now establishes why people live in Glowhaven, the Evertree's effect on everyday life, learned magic, varied physical and occupational play, the academies' civic responsibilities, government, trade, surrounding countryside and the intended ensemble tone. It no longer walks through Ilyra Stillglass's term history, the level-20 sequence, testing commands or the silver-key reward. Those facts have not been deleted from the records where they belong.

Quest generation now has a general design brief covering concrete situations, local sources, varied work, character pressure, standalone versus multi-quest scope, acceptance, multiple approaches, fair evidence, rewards, ownership and persistent consequences. It offers patterns without scripting a replacement campaign. An ordinary favor can end as an ordinary favor.

## The scope audit

Updated the relevant story, initial-start, NPC-intent, encounter, item, NPC-generation, NPC-update and memory instructions. Removed repeated walkthroughs of the spider incident and named anecdotes about a previous portal-room cast bug from broad task guidance. Developer setup is now described in the actual developer start, rather than becoming a standing subject for every opening. The general travel and inventory tasks retain the rules they need: actual location, one crossing, legitimate authorization, real possession, supported updates, no duplicate awards and persistent outcomes.

The full academy roster remains in its dedicated reference block. Regional and faction tasks still contain relevant geographical/institutional reference information; their purpose genuinely calls for it. Detailed magic resolution, dialogue, relationship calibration, character flaws and party management remain. This pass scopes the instructions rather than replacing the previous structured AI work with short summaries.

The narrator style is unchanged: third-person present, vivid fantasy-anime scenes, character-driven comedy, sincere stakes, varied approaches and player agency. The new openings follow that voice.

## Story starts

The export contains **13 starts**, in this order:

1. Write Your Own
2. Phoenix Wing: Arrival Court
3. Gryffin Tail: Arrival Steps
4. Dragon Hoard: Arrival Gallery
5. Hydra Head: Arrival Court
6. First Day of Work: Phoenix Wing
7. First Day of Work: Gryffin Tail
8. First Day of Work: Dragon Hoard
9. First Day of Work: Hydra Head
10. Merchant: First Morning
11. Village Life: Brookmeadow
12. Developer: Portal Inspection
13. Random

The eleven fixed openings now contain actual scene prose, recognizable dialogue or visible activity, and brief director notes stating their premise, cast, setup and stopping point. They end before the player's answer or next decision. They are alternative beginnings, not a mandatory tour through all the institutions.

The four academy arrivals keep the correct admission packets and enrollment quests. Hinae Komori, Fumito Sakurai, Kōsuke Shishido and Kana Fujimoto remain the respective opening contacts. Their existing selected-start placement effects are preserved; they do not join the party. The employment scenes begin where the headmasters actually are: the first three in Faculty Offices, and Kiyoko Fujinami in Confluence Pavilion. Jobs remain consistent with the chosen background instead of making every hire a professor.

The merchant opening uses Rinpei Komatsu at his real North Arcade stall. It does not invent a player-owned stall or stock. Brookmeadow's opening uses Haruho Taneda in Mill Lane, where he is already placed. A local, returner, worker or visitor background remains possible without inventing family property. Pebbletown, Clovermead and Saltmere remain mapped settlements; their separate village-opening options are removed. Random's village candidate is also Brookmeadow.

**Write Your Own** uses the reserved native name, `allowPlayerInput: true`, and an empty `storyStart`. The empty field is intentional: the community reference says the engine ignores that field for the reserved start and uses native player input. It offers paired public locations and areas in Glowhaven, plus Drakenspire's market and Cloudbloom Landing's terrace. Secret sites and prison cells are not random opening candidates. The actual custom-input UI and its handling of a specifically requested room have not been tested live in this pass.

**Random** is the final JSON entry. It selects a public Glowhaven location and creates a compatible moment there, without assuming enrollment, employment, recruitment or a crisis. Phoenix Wing remains the existing default start; placing Write Your Own first does not silently change the default.

The developer opening is solo-compatible and stops before either portal activates. Its configured kit still supplies the ordinary test keys; the explicit optional incident command remains available there. No keys, powers or companions are granted merely by the opening prose.

## Friendly-reply cleanup

Removed the sole **A Friendly Reply** narrative event. Also retired its directly connected **First Words** tutorial quest, the `first_words_reply` quest trigger that started the event, and the old active **A First Connection** introductory arc. Keeping those records would leave a quest depending on a removed event and an active arc encouraging another version of the same tutorial.

The required section containers remain present and empty where appropriate. Existing enrollment quests and placement effects do not depend on the removed tutorial. Ordinary greetings and relationships continue through normal narration, dialogue and updates. There are now 28 quests, 21 party quest triggers and no preauthored narrative events or active greeting arc. All 78 general trigger definitions remain byte-for-byte equivalent as JSON values.

## NPC types and the removed guard

Expanded **8 types to 61**. The original eight definitions are preserved. The 53 additions provide:

- 13 civic/professional roles: academy staff, court officials, city guards, elite operatives, prison officers, merchants, artisans, healers, researchers, field guides, nobles, performers and bandits.
- 3 broad sapient categories: fae, dragonkin and beastfolk. They do not impose a shared temperament or elemental immunity.
- 5 ordinary-animal categories for household, farm, pack, predator and herbivore encounters.
- 17 mana-beast types, from giant spiders, slimes and thorn creepers to mountain and sky creatures. Signs, motives, terrain and noncombat approaches matter.
- 5 constructed bodies with different practical workings, 4 kinds of restless dead, and 6 elemental manifestations.

These are reusable templates, not 53 new residents, quests, guaranteed spawns or a copied monster roster living in every region. Each uses the world's existing damage vocabulary. Human occupational roles have neutral damage arrays. Where a body warrants a profile, its vulnerabilities, resistances and immunities are explicit. A type does not grant an NPC a level, full spell list, automatic loot or social immunity.

The fixed **Moltback Silkguard** NPC is removed from the authored roster. Its portrait field was empty; no artwork was discarded. It is now a reusable type with rust-brown armor, silk anchors, territorial behavior, fire vulnerability and resistance to slashing/piercing damage. Sunken Broodworks locally instructs the normal NPC-generation flow to establish the encounter's actual individual when approached, telegraph it, and preserve its identity and result afterward. It must not generate another guard on every return or after a successful bypass. The existing descent trigger already accepts overcoming or bypassing the span and has no named-guard kill requirement.

This is narrative encounter integration through existing generation behavior, not a newly invented type-spawn trigger. Live generation still needs checking to confirm that the model selects the intended type and keeps the individual. Cinderwoven Skitter and Shizuru Amagumo are retained as their existing authored individuals; no wider roster deletion was inferred.

## Preservation

- All **131 remaining NPCs**, their order, biographies, appearance, equipment, affinities, years, numerical values and saved placement are unchanged.
- All **48 students** retain their four-year standing.
- All **261 nonempty media URLs** are identical. The only removed media field is the guard's empty portrait slot; 271 media fields remain.
- All 5 realms, 5 regions, 97 locations, 364 areas, map coordinates, area identities and paths are preserved. Only the broodworks encounter prose and two localized destination cast/ecology notes change.
- Factions, skills, attributes, progression, HP/MP, abilities, traits, creation, premades, naming, combat settings, music and game modes are unchanged.
- Portal routing, authorization, key issuance, the actual incident sequence, return access, boss/report state and rewards keep their existing mechanics.
- Project sources, supplied attachments and historical named exports are unchanged. Before-update current files are saved under `backups/2026-10-28-before-alpha6/`.

## Checks and limits

Local JSON, field-size, reference, roster, media and preservation checks passed. All **122 local fixtures** passed, including the previous 105 portal/setup regressions and 17 additional opening/cleanup/type/bypass fixtures. The actual existing portal scripts run inside a Node VM; typed engine effects are mocked and semantic judgments are supplied. These checks establish local consistency, not real model quality, current Studio acceptance or live trigger ordering.

The world overview is 3,997 characters; quest guidance is 4,957. All starts and AI tasks are within the currently documented community field/section limits. The complete export remains Alpha 6 for the author's image pass.

For a fresh-game check, sample an academy opening, an employment opening, Brookmeadow and native Write Your Own. Confirm the selected cast and room, no automatic player response, no friendly-reply tutorial, and one ordinary conversation that stays ordinary. In the broodworks, check that a real type-backed guard is generated when relevant, that a viable bypass works, and that return visits preserve the result. Importing a world definition is not a demonstrated migration of an existing playthrough's quest or NPC state.

## Reference basis

**Observed exports:** the supplied Glowhaven overview/starts, and the supplied maintained Luxcellia overview, starts and NPC types. Adopted the separation of premise from quest-design guidance and the authored scene-plus-direction format. Their unique countries, cast, supernatural systems, quest ranks, currency and opening plots were not imported.

**Current community documentation, unofficial rather than Latitude guarantees:** [Story Overview](https://wiki.unofficial.voyage/world/storySettings) distinguishes the broadly included premise from the quest brief; [Story Starts](https://wiki.unofficial.voyage/world/storyStarts) documents the reserved custom start and startup fields; [NPC Types](https://wiki.unofficial.voyage/world/npcTypes) documents type profiles and the damage vocabulary. Template selection and scene quality remain authored design choices requiring live observation.
