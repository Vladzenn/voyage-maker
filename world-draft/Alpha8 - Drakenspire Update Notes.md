# Alpha 8 — Drakenspire Expansion

The full world export is **GlowhavenAlpha8 - Drakenspire.json**, byte-identical to the canonical **WorldAlpha - World.json** at publication. It starts from the author's image-updated local world, including the last dragonkin appearance clarification. It is a complete world file, not a location-only patch.

## What changed

Drakenspire grows from **5 locations / 16 areas** to **60 locations / 253 areas**. This adds **55 locations and 237 areas**, bringing the full world to **152 locations / 601 areas**. Glowhaven remains at **67 locations / 273 areas**. The scale is comparable while the two places have distinct identities and uses.

The higher northeastern fortress and the ancestral dragon skeleton form one dominant landmark. The busy lower shelf has homes, clanholds, markets, specialist craft, freight, food, an ordinary schoolhouse, entertainment, a small fight pit and one onsen. The outer map includes working and abandoned mines, amber caverns, a small hamlet, sparse pine country, a frozen basin, a neighboring peak, old shrines, wyvern perches and giant territory.

Every location has public information, scoped narrator context, four to six authored areas and connected, reciprocal area paths. Locations offer practical activities and conditional situations rather than an active conspiracy in every building. Named service personnel have not been invented: the existing **130-NPC roster is unchanged**. New regional characters can occupy these roles when authored.

## National lore and institutions

- Established Drakenspire as both nation and capital, governed by a Jarl elected through clan chiefs in a decentralized order. Merchants and military leaders have influence without automatically becoming electoral chiefs.
- Developed the ancient protector's founding story, sacred remains, dragon and ancestor worship, restrained fortress government and lively lower-city culture.
- Established the distant gray guardian's four legs, separate pair of wings, lightning breath, intelligence and spellcasting. His lair remains genuinely unlocated; the number of sacred dragons and their generations is unknown.
- Connected metallurgy, specialist spellblade work, mana crystals, amber and creature materials to real craft and trade. Rare unfertilized dragon eggs and shed scales remain meaningful gifts, not repeatable free loot or automatic MP restoration.
- Added waterworks, geothermal use, goat/sheep husbandry, stores and imports; the skeleton supplies neither heat nor magical infrastructure.
- Kept one modest schoolhouse and no rival magical academy. Serious magical study commonly takes residents to Glowhaven.
- Defined local guards, the street-dueling ban, lawful fighting venues and a friendly but sovereign relationship with Glowhaven.
- Added six supporting factions: Drakenspire Clan Assembly, Drakenspire Hold Guard, Keepers of the Crescent, Clan Iwatsugu, Clan Yukinose and Clan Arashimine. The existing civic Drakenspire faction is rewritten as a proper national description. The world now has **23 factions**.

The three named clans are authored examples of prominent houses, not the complete national clan list. Their names, site names and specific everyday situations are design additions built from the author's answers; no real-world Japanese etymology is claimed. Norse/Gaelic institutional inspiration does not override the author's Japanese-inspired First name Last name preference for local characters.

## Species and generated NPCs

Dragonkin lore and the type description now include roughly human height, a lifespan up to about two centuries, hereditary but non-determinative scale colors, and regional variation within one species. Human faces, horns, lateral facial scales, slit pupils, scaly backs of hands and arms, human-looking palms and thick tails remain consistent. Nahlah Qamar's established desert origin is preserved, and no existing NPC appearance or portrait was rewritten in this pass.

Added **Giant** and **Yeti** types, bringing the world to **64 NPC types**. Refined the generic Wyvern description to distinguish smaller, two-legged winged predators from dragons and dragonkin. The yeti is real but rarely encountered; the knowledge of local people remains uncertain. No fixed new boss or NPC is spawned by these definitions.

New locations have explicit generated-NPC bands. Ordinary city sites are generally 5–30, specialist workplaces reach 35–45, and government/security sites can reach 50–60. Easier field routes remain available around 15–40. Wyvern country, giant territory and the remote yeti basin are progressively more demanding; the last uses 55–75. These bands constrain ordinary generation rather than guarantee player-balanced encounters. Existing fixed NPC levels, player progression, HP/MP rules and combat settings are unchanged.

## Map, visibility and travel

All 60 Drakenspire locations use a regular **8-column grid**, ten coordinate units apart, radius two, within the existing region. Four cells remain spare in the final row. Grid coordinates are editor staging positions, not final geography. **They currently affect location distances and travel until manually rearranged.** Intended districts and geographic routes are supplied separately for the map design; no unsupported cross-location area paths were inserted.

**56 locations are initially known.** Four obscure sites begin with `initialKnown: false`: The White Silence, First Shelter Ruins, Coldglass Galleries and The Fallen Pass Shrine. They have no extra hidden lock. Their discovery remains narrative/engine discovery rather than a newly scripted unlock quest. Existing realm/region discovery settings are retained.

The five preexisting location keys and all sixteen old area keys remain valid. The arrival endpoint is still **Drakenspire → Drakenspire - Portal Room**, connected to **Evertree Base - Portal Room**. The expanded location named Drakenspire describes the portalward quarter inside the larger city; it is not a second capital. Portal keys, crossing authorization, the one-time anomaly, Silken return travel, the postponed field test and the separate expedition questline are unchanged.

Glowhaven is restored to the first position in the realm list, as previously requested. Realm names and identities remain unchanged.

## Scope and preservation

All **298 media URL fields, including 289 nonempty URLs**, and all existing image blocks/crops are preserved. New places have no fabricated image URLs. No map or portrait was generated or uploaded.

The stable story overview, narrator style, global image prompts, skills, attributes, resources, items, story starts, NPC roster, quests and trigger scripts are preserved. Only three relevant AI entries were adjusted: Drakenspire's naming convention, dragonkin height/lifespan/color interpretation, and the existing regional-identity paragraph. New regional facts live in local lore and places instead of being repeated throughout unrelated generation tasks.

Sources and historical named exports remain unchanged. Backups of the overwritten canonical files and notes are in `backups/2026-10-28-before-alpha8-drakenspire/`.

## Checks and practical limits

**4,194 local checks passed**, covering scoped changes, input preservation, references, text sizes, area connectivity, reciprocal paths, unique grid coordinates, faction links, media preservation and general AI limits. **92 mechanics fixtures passed** using the existing real trigger scripts in a local test environment with mocked typed effects and supplied semantic decisions.

This is not a live Voyage Studio validation, generated-story quality test or encounter-balance result. Automatic encounters remain in their existing configuration; location descriptions and NPC types do not claim to install a new automatic spawn system. Import the complete file and use a fresh game to check first arrival, map discovery and the atmosphere of several representative city and wilderness scenes. Existing saved games may retain their own generated state.

The map brief, location catalogue, readable national lore, grid manifest and intended-route guide accompany the full world. The authored map contains one onsen, one small fight pit, one ordinary schoolhouse, a working capital and broad outer country. It contains no confirmed guardian lair, new magical academy, city-heating skeleton or fixed roster of newly named service NPCs.

## Reference basis

The local Luxcellia reference supplied useful service-rich spaces and practical reasons to interact with locations; Chikara supplied clear separation of ordinary facilities and area links. Their unique setting content, currencies, institutions and named people were not copied. Current detailed field guidance is community-maintained and unofficial: [locations and sibling-area paths](https://wiki.unofficial.voyage/world/locations), [regions](https://wiki.unofficial.voyage/world/regions), and [NPC appearance fields](https://wiki.unofficial.voyage/world/npcs). These references support the authoring approach, not a claim that Studio has accepted this export.

The visual fortress reference is [Hohensalzburg's official site](https://www.festung-hohensalzburg.at/en/the-fortress). The author's Glowhaven map establishes the shared illustrated finish, while Drakenspire's geography and monumental crescent follow the author's answers.
