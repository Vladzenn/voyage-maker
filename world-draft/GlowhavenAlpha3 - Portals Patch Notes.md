# Portals and regional expeditions patch notes

2026-10-27. Based on the current Schools of Magic export. New destination names and connective details are draft content authored under the user's request.

## World changes

- Renamed the main realm **Glowhaven City → Glowhaven**, and renamed its map region to **Glowhaven** for consistent regional scope. All structured references were updated; the city's proper name in prose remains Glowhaven City. Existing map geometry and images are unchanged.
- Added **Evertree Base - Portal Room**, connected to Rear Palace Walk. Permission for transit does not grant unrestricted palace or tree access. Operating portals carry permitted passengers, including noncasters.
- Added **Drakenspire Mountains**, a snowy, dragonkin-majority highland realm emphasizing stone-built settlement, warriors and metalwork. Its five locations are Drakenspire, Embersteel Foundries, Stonefang Training Grounds, Whitepass Caravan Lodge and Rimecrest Trail.
- Added **Asterveil Sky Archipelago**, a fae-inhabited floating-island realm with mythical mana beasts. Its five locations are Cloudbloom Landing, Asterveil Canopy, Bellwind Conservatory, Mythwing Meadows and Broken Halo Ruins.
- Added four endpoint-gated outbound/return rules. Arrival points are **Drakenspire - Arrival Gate** and **Cloudbloom Landing - Return Gate**; both return to the Portal Room. Actual transit requires an explicit choice, permitted passage and an available route.
- The two destination realms begin undiscovered and are revealed through their travel rules. Most public locations are known once that map is accessible; Broken Halo Ruins remains undiscovered. No map image, location illustration or developer portrait URL was invented.

## Expedition correction

The quest is now **Beyond Glowhaven: An Authorized Expedition**. All references use the new key. Students must leave the whole Glowhaven region, not merely the city walls. Existing local farms, woods, Greywatch Keep, settlements, Wraith Island and Wraith Island Prison are ineligible.

The fieldwork script requires recorded authorization and a completed authorized objective in Drakenspire Mountains or Asterveil Sky Archipelago. It records the destination realm, region, location and scene. Arrival itself is not credit. Local Genzō Iwakura woodland practice remains a separate useful activity.

## Map containment

`newRegionGenerationEnabled` is false, matching the two referenced worlds. Dedicated travel and generation instructions preserve authored maps, avoid invented realms or off-map destinations, and keep any appropriate new local room/site inside an existing region's bounds. Failed navigation stays local. The native switch covers new regions; the broader narrative restrictions still need live verification.

## Names and narrator

The supplied ChikaraOld has 10 name-filter entries and Luxcellia has 291. Glowhaven grows from 20 to **261**, with eight nonempty name-token alternatives per entry. Given names replace given names and surnames replace surnames. Canonical cast names are protected; existing French/Elvish and foreign identities remain valid. Full-name random pools and generation guidance reinforce First name Last name and avoid exact roster duplicates. Prose deletion entries are not copied from Luxcellia.

The narrator style takes inspiration from Chikara's routines, distinct voices and sincere tonal shifts, and Luxcellia's visual richness, committed comedy and focused scenes. It remains within the 2,000-character field limit. Warriors, brawlers, craftspeople, investigators, merchants, travelers and noncasters receive appropriate attention. Ordinary physical actions do not acquire MP costs. Existing player-agency and authoritative-combat rules remain.

## Developer Playtester

Select **Developer Playtester** in premade character creation and use any existing opening. Keep its developer trait when customizing. It receives:

- Every existing skill at **100** and all **ten** existing techniques.
- Initial **100,000 HP/MP maxima** before normal level scaling.
- **100,000 marks** and six ordinary weapon/focus/equipment types.
- A player-scoped runtime setup that sets character level and all six attributes to **100**, then marks setup complete.

The ordinary starting attribute cap remains 16. Developer traits are absent from normal selection categories and the level-up pool. The setup targets only eligible developer players, including a later joining tester, and does not repeatedly stack bonuses. No NPC is replaced. The test background permits arranged Portal Room inspection without a long access subplot. Use ordinary characters for balance, social progression and resource testing.

## Totals and preservation

**4 realms, 4 regions, 91 locations, 345 areas, 58 lore entries, 128 NPCs, 23 quests, 44 general triggers, 22 party quest triggers, 43 traits, 42 skills, 10 abilities, one premade.** Forty-one traits remain the ordinary creation catalogue; the additional two are developer-only support.

Every NPC entry and roster position is unchanged. All 268 existing media URL fields are retained; the main region image's parent key changes with the region rename. Existing starts, skill caps, progression rates, HP/MP rules, item definitions and the 14 prison facilities are preserved. Previous canonical files and their input hashes are backed up.

Local structural, size, reference, naming and preservation checks passed. **19 local script/lifecycle fixtures passed.** These simulate typed effects and supply semantic decisions. No live Studio validation, import, AI-routing trial, multiplayer portal session or playtest was performed. Portal permissions and group-consent interpretation remain AI-dependent. Use a new game; old saves may retain the former quest key and settings.

See [alpha missing pieces](Alpha%20Readiness%20-%20Missing%20Pieces.md) and [research decisions](../research/Portals%20Naming%20and%20Narration%20-%20Implementation%20Notes.md). The full export is **GlowhavenAlpha3 - Portals.json**, identical to the canonical **WorldAlpha - World.json**.
