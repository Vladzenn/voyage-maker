# Wider Earth lore — implementation, 2 November 2026

The author approved the existing **Lore Update Proposal — Wider Earth** and supplied a new full Studio export. This is a lorebook expansion. It does not launch the proposed nations or the Oni homeland as playable destinations.

## Source and scope

- Full Studio source: attachment `1d3eed47-6a6c-4042-9335-98614aba6de8`, SHA-256 `0c231ddb78b80c20956c2da4fe5fee86af98e3ab82700af1fb55ef6f6dd438b2`.
- The supplied export differs from the preceding canonical world only in `extraRequiredXPPerCharacterLevel`: 50 → **60**. The user's value is retained; the starting requirement remains 400.
- The native `worldLore` section uses the existing `{ "text": "…" }` entry shape. No secrecy, travel, ancestry or other schema field was invented.
- The lorebook grows from 173 to **200 entries**. Twenty-seven genuinely new entries are added; the old diplomacy entry is renamed in its existing position, and thirteen other entries are revised. Existing-entry order and all unrelated lore remain intact. The new tail follows the proposal's topic order.
- Every non-lore field equals the supplied Studio source: all media, crops, coordinates, voices, music, starts, quests, abilities, NPCs, factions, items, triggers and mechanics. Current cast and difficulty are unchanged.

## Implemented setting

Earth has real-Earth scale and ordinary cosmic/physical principles alongside magic, with its own continents and histories. Foreign lands have cities, institutions, maritime trade, local diversity and lives beyond Glowhaven. The expansion covers Ardelis's kingdom/celestial worship, Valcéranne's elven communities, Dunbrae's dwarven maritime commonwealth and varied beastfolk-populated Yunhai.

Glowhaven was founded by the four Archmages and is politically independent of Ardelis. Former subordination wording in diplomacy, noble civic service and academy mandates is reconciled. No separation war, date or present feud is invented. Its existing council, Great Sage and four academies remain intact.

Permanent portals are unusually expensive undertakings. The Evertree sustains the known hub connections; Glowhaven established the Drakenspire endpoint. This does not grant Drakenspire independent equivalent portal-making technology or alter personal Space magic, route keys, permissions, fixed return endpoints or passenger costs.

Elves live roughly a thousand years, mature physically at about the human rate and retain youthful adult appearance. Mana changes can suggest age to knowledgeable observers without becoming a scan, stat bonus or universal knowledge. Ilyra Stillglass's exact age, sight, biography and 254-year reign remain untouched. Physical maturity and cultural seniority are distinct; the unresolved social-adulthood threshold remains unassigned and existing adults are not reclassified.

Elvish remains French in dialogue. Dwarven speech receives a focused narrator convention for readable Scottish-accented English and selected Scots expressions, varied by speaker. No Scottish Gaelic translation mandate or voice asset/tag replacement is added. Public cultural prose remains ordinary description.

The four existing Oni topics remain focused entries. Their ordinary life, martial traditions, limited Arcane/Soul magitech and yokai context are polished without naming or mapping the homeland or opening a torii route. Hell, new peoples, extra nations and later arcs remain outside this implementation.

## Private origin boundary

`Author Background — Primordial Origins` explicitly begins with **AUTHOR/NARRATOR ONLY — NEVER DISCLOSE DURING PLAY**. It records the approved private account, curiosity as the sacrificing primordial's motive, mana's origin and the prohibition on any in-game discovery. Mortals, celestials, gods, oracles, books, histories, research, inscriptions, cults, revelations, Divination and direct narrator disclosure gain no exception. Religion entries describe beliefs and claims without revealing that account.

This is instruction text, **not a native hidden flag or technical access control**. No guarantee is made that an AI can never leak prompt context. The account should not be transformed into a quest hook or a reachable secret. The Evertree's founding and Asterveil ruins remain unrelated mysteries. A source scan confirms that primordial terminology appears only in this explicitly private lore entry, not in public lore or NPC records.

## Verification

`tools/wider-earth/merge-report.json` records source/proposal hashes, changed/renamed entries, every preserved non-lore source-section fingerprint and every unchanged lore-entry fingerprint. Only the active preservation fingerprints for the author's XP edit and the approved lore section were refreshed; Spider, NPC, artwork and encounter fingerprints remain unchanged.

The implementation uses only existing native lore entries and plain text. No new mechanic requires a platform capability investigation. Maximum lore-entry length is below 5,000 UTF-16 units. Portable structural, item, fieldwork, adventure, creation, Crucible and artwork regressions are run before publishing the repository. These are local checks, not a Studio import, live playtest or AI-secrecy proof.

A targeted scan found no non-lore assertion of continuing Ardelis jurisdiction, a conflicting explicit elven lifespan or a fixed 100-year social-adulthood threshold. No broad NPC rewrite was needed. The author's source progression change is the only non-lore difference from the previous local world.

### Manual review

1. Ask ordinary NPCs about Ardelis and local authority; they should describe independent Glowhaven without inventing a founding war or date.
2. Discuss Valcéranne, Dunbrae or Yunhai through actual knowledge and ordinary connections. No new map, operating portal or compelled diplomatic quest should appear.
3. Ask about creation in a temple or research scene. Local beliefs may be discussed; the private primordial account must not become an answer, hint, revelation or discoverable objective.
4. Compare elven age and competence without assuming a young face means a student, assigning an exact age by scanning, changing Ilyra's biography or reclassifying authored adults.
5. Check readable dwarven speech without a forced voice change, universal caricature or invented Gaelic translation rule.
6. Reimport the full world into Studio and check current validation. Existing routes, keys, Spider content, coordinates and artwork should behave as before.

## Delivery and release

Full import: `output/wider-earth-2026-11-02/The Schools of Magic, Arise! - Wider Earth Lore.json`. Canonical, derived sections and the current revised/fieldwork full exports are synchronized. Historical earlier snapshots remain historical.

At the author's request, the unreleased **Champions of the Crucible** notes gain only **“Lore expanded.”** There is no separate minor announcement, future-nation advertisement or disclosure of the private origin account.
