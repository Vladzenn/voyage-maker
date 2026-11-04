# Schools of magic, Rebirth!

Implementation record · 5 November 2026

## Approved base and delivery

The author confirmed the current local world as the merge base. Its last world edit was **Universal Fishing and the Studio import hotfix**, commit `48445de`, SHA-256 `a84f4a5e898d6bd85f35b96b354523fe36a0afaeea556b8c827f261d22613200`. The checkout and GitHub were both at `364fca2` when implementation began. The later commits before this build contain planning and handoff documentation.

The canonical import is **WorldAlpha - World.json**. Rebirth is applied there after candidate validation, with section files regenerated through `tools/project.py sync`. The separate download is `output/rebirth-2026-11-05/The Schools of Magic, Arise! - Rebirth.json`. The original planning brief and its verbatim author proposals remain the design history. The author's later answers determine the release boundary described here.

This stage implements the Glowhaven chapters and ends after checking the relay evidence and identifying an Ardelis receiving station. The explorable Ardelis country, new port region and controlled rival's deployment are deferred to the author's later map and country stage. The current quests reach an actual local conclusion. They do not wait indefinitely for unfinished country content.

## The opening and ordinary life

**Rebirth: A Morning in Brookmeadow** is first in the start list. It begins in Mihana Orihara's cottage, a new area of the existing Brookmeadow location. Mihana paints lamp covers for a living. Kenta Matsuba helped bring the unconscious traveler from the shore and has his own work to get back to. Existing NPC records, appearances and relationships are preserved.

The player retains past-life memories and their selected current body. The opening stops before their answer. Mihana knows what she saw during a rescue. She has no knowledge of reincarnation unless it is actually disclosed. Her record explicitly limits the rescue premise to the Rebirth opening, so an ordinary village character is not assigned the same past.

The exact chosen start grants **Summoned one** through a player-scoped mechanical tick-zero effect. The trait grants no stats. It is absent from creation categories and blocked from ordinary level-up offers by a requirement above the current character cap. Later joiners do not inherit it from the host's continuing story. The opening includes one optional journal suggestion, **Rumor: A Living to Be Made**, pointing toward actual local work, lodging, contacts or the city guild. It accepts several ways of finding a foothold and gives no license, job, property or portal key.

Tick-zero mechanical grants are documented, but their exact ordering in a fresh multiplayer lobby still needs a Voyage test. [Trigger timing and targeting](https://wiki.unofficial.voyage/mechanics/triggerDefinitions)

## The Glowhaven investigation

The delegation cannot surface before **200 completed turns**. A mechanical clock also requires an origin bearer and a suitable location. Eligible public stops are Brookmeadow, Four Sages Bazaar, the Glowhaven guild and the Great Sage's Court. A native semantic condition then checks an established ordinary life and a calm scene. Combat, flight, an expedition, an assessment, a championship or an urgent rescue must delay it.

The first interruption places Kazunari Shiba and offers **The Sage's Visitors**. His delegation has genuine diplomatic business and only a broad shore date and location. It starts without a name, face or knowledge of the player's memories. When actual intrusive questioning occurs, Vladimir intervenes on his own business. Shiba recognizes him. Vladimir's look is ambiguous and his public exchange supplies no diagnosis, training or invitation. The departure waits at least two more turns so it cannot remove the participants before their scene. If Shiba actually dies before this exchange, his fate is preserved and authentic records or witnesses remain usable.

Native quest completion carries the investigation forward.

| Undertaking | What actually completes it | What it provides |
| --- | --- | --- |
| The Sage's Visitors | Hear or check the real inquiry and make an informed response | Offers the shore-ledger investigation |
| A Name in the Shore Ledger | Establish an actual step in the copy's custody and decide what to protect or disclose | Offers the carrier investigation |
| The Carrier behind the Ledger | Corroborate the intermediary's connection to the delegation and pump house | Offers the relay work and optional Shadowspire audience |
| The Pump House That Hummed | Investigate the actual site, secure checked dispatch evidence and disable its local use or arrange a real authorized response | One dispatch copy per participating party member, the stated reward and the concluding court conversation |
| A Second Receiving Station | Present the checked findings to an informed authority and learn where the next operation is being prepared | Closes this local investigation with the Ardelis lead |

The six main and audience undertakings begin `planned`, using the documented reserved quest state. Their configured event or predecessor offers them through `quest-init`. Ordinary quest completion owns their rewards and successor offers. Merely meeting Reika early is not the intended activation path. Verify that the current Studio/runtime respects this reservation during the fresh-start playtest. [Quest lifecycle and chains](https://wiki.unofficial.voyage/world/quests)

**At the Wandering Door** is optional. Reika can arrange a request for an audience. Accepting it and reaching the outer clearing places Vladimir for that agreed meeting. Declining leaves Reika's independent investigation available. A conversation about the diagram can reveal facts from Vladimir's actual observations. He remains independent and declines recruitment. His NPC record preserves immortality and psychic immunity.

## The personal interception and multiplayer

The delegation does not automatically establish a personal lead. A separate, player-scoped semantic condition requires a real witness or copy to have reached the intermediary with a corroborated identity and whereabouts. A false report, protected witness or private confidence is insufficient. The condition gives the actual matching bearer **Traced Shore Record**, a private story marker with no stats or ordinary creation availability.

The interception needs a traced bearer at level 15 or above, at least 60 turns after the lead, the correct story phase and a suitable rural approach. The native player scope and recipient level condition keep a strong spectator from qualifying another character. Both initial identities and the later trace remain attached to people. Companions can participate in the shared fight. The semantic placement check still has to confirm that this actual person is present and that no unrelated emergency is underway.

The two authored couriers have separate Health and capture outcomes. They look like travelers; their public cards do not identify them as constructs. Their private records limit them to a local description and an interception task. They have no royal stamp, maker's mark, dispatch or reporting channel. Actual secured custody of a living courier sets only that courier's Health to zero through a native effect. A threat, ordinary knockout, failed grapple or the player's capture cannot activate that shutdown.

An actual resolved interception can end through victory, escape, release or another established outcome. A one-time stored roll may bring Vladimir to a plausible aftermath scene. It never resolves the player's battle or invents recovered remains. Otherwise, Reika supplies the independent evidence route. The entire encounter is bounded and is not a recurring ambush generator. The relay can also be investigated without fighting the couriers.

This supports multiplayer through native recipient targeting and shared scene state. The fixture supplies semantic answers. Concurrent real players, save reloads and the storyteller's choice of target remain live-test requirements. [Official NPC state effects](https://voyage.io/whats-new/patch/patch:100001188) · [Player scope and NPC Health effects](https://wiki.unofficial.voyage/mechanics/triggerDefinitions)

## Shadowspire and the private realm

The existing Shadowspire pin, forest, trail and artwork are retained. The tower adds a threshold hall, upper study and Cellar Gate. Vladimir must actually approve and hand over a **Shadowspire Guest Key**. One held key covers the party admitted with its bearer. An uninvited direct approach to the interior is redirected to the outer clearing. Losing a key still permits an exit and a request for replacement.

The private portal runs only between **Shadowspire - Cellar Gate** and **Shifting Gallery - Return Lantern**. The player must commit to crossing at the real endpoint. Entry needs the genuine credential; return needs no key. This private return remains at Shadowspire. An arrival without the established entry state is corrected to the outer clearing.

**Vladimir's Elsewhere** has one compact region and eight named destinations.

- **Shifting Gallery** holds the return lantern and moving arcades.
- **Glassroot Gardens** has translucent roots, small antlered hares and air-swimming rays.
- **Inverted Court** has marked safe footing, a wall stair and uphill water.
- **Porcelain Workshops** contains household frames and real repair benches.
- **The Little Kingdom** houses the model valley, games table and kites.
- **Tilt Court** supports voluntary ringball and agreed practice.
- **The Rainward Orchard** contains the sideways-rain experiment and potting shed.
- **The Cabinet of Evenings** offers different window skies, tea and a viewing balcony.

Ordinary native travel connects these locations through marked corridors. Each location's `areas.paths` stays within that parent location. This was corrected after official validation rejected cross-location area links. Corridors can change scenery and optional shortcuts in narration while addresses and the marked way out stay stable. No constantly changing mechanical maze or additional sports controller is introduced. The new realm has provisional pins and no newly generated map image.

The Brass Usher has household work, tastes and opinions beyond giving tasks. Two small optional native quests involve the stalled model carriage and misplaced rain rail. Their completed work earns an actual teaching scroll. Ordinary garden animals and practice frames are npcTypes. Familiar materials alone do not connect Vladimir's household to the disguised couriers.

## Ancestry and tone

Character creation now includes the distinct rare **Beastfae** ancestry with **+1 Empathy, +2 Survival and +10 Health capacity**, chosen as the alternative to the rejected Force/Intuition suggestion. Its 48 optional forms preserve full animal faces and coherent upright bodies. Fae have 32 form presets and Beastfolk have 36. The existing form keys, Mixed Ancestry access and separate Fae Stature choice remain available. Form choices are cosmetic and do not prescribe a temperament or grant extra powers.

The tone pass changes the narrator's opening emphasis, opening-task phrasing and one existing relevance/knowledge instruction. It adds short body-continuity guidance for Beastfae. The existing soundtrack, modes, global quest-generation guidance and art settings are preserved. The goal is concrete ordinary life, consequential decisions and humor that belongs to a character or moment.

## A hundred teaching scrolls

The catalogue adds **100 abilities and 100 scrolls**, five for each public magical discipline. Sixty formulas are practical, thirty-five advanced and five masterworks. Utility and trade workings give low and middle proficiency characters things to do. Defense, movement and attack workings use actual skill and committed Mana. Time receives no public scroll. Space keeps Gravity Magic 25 as a native prerequisite. Formula traits remain exclusive learning records and are blocked from ordinary level-up selection.

Ten small mechanical registries share one study template. They activate an exact native learning check only for a held unfamiliar formula being studied in context. Each active check retains its own item, formula, ability, prerequisite and player scope. A supplied successful semantic result grants the exact trait and ability and removes one copy from the satisfying reader. Failure, a trade, a different reader and a known formula cannot consume the wrong copy. Study grants no discipline rank or instant cast.

The registries retain up to eight formula focuses across the party, with eight-turn expiry after research stops. They admit natural continuation language when the preceding scene concerns study and normalize curly apostrophes. The scene should identify the formula once. Ambiguous unnamed scroll selection and live continuation remain manual tests. A runtime guard reserves semantic-definition headroom. Carrying the new catalogue with no active research adds no learning judgment. An idle registry with no focus avoids its inventory scan.

The existing thirty scroll settlement rules are preserved. The new shared template has local ownership and retry tests, but the planning brief requires a live multiplayer prototype before migrating those older rules. That migration remains a tested-next-step item rather than an asserted runtime result. The full compact item catalogue is under 250,000 units, with roughly eight thousand units of headroom at this build.

## Validation, artwork and remaining checks

`tools/rebirth/review.json` records the base, the exact reversible changes and the resulting world hash. Existing NPCs, map pins/images, music, progression settings, resource settings and Spider content are checked against the base. The only existing trigger edit is the approved level-20 mechanical gate for `gh_exam_volunteer`. The new Rebirth suite checks the actual emitted scripts with supplied semantic answers. Older preservation suites use an exact reverse projection, which rejects drift and restores their prior test input without rewriting historical fingerprints.

The official Creator API draft validator returned **zero errors and zero warnings** for the corrected candidate. Its recorded hash is in `tools/rebirth/official-validation.json`. This is API validation, not a Studio save or a gameplay test. The new area-path check is also in the portable validator, and Rebirth's fixtures run in the standard publish command and GitHub Actions.

Four principal portraits were generated with the built-in imagegen tool and saved under `world-draft/npc portraits/Rebirth/` with exact canonical filenames. Pose eligibility, actual random draws and final prompts are recorded in `tools/rebirth/portrait-prompts.json`. Three successful official uploads are linked by image hash in `hosted-portraits.json`. Voyage rejected Vladimir's image with `studio_media_failed`; the author explicitly chose to keep that generated file and handle his upload later. Each portrait used one generation pass. Their headroom is tighter than the guide's target and is flagged in the selection record. The named-image ZIP is supplied with the download.

Before releasing the storyline, test these cases in Voyage.

1. Start fresh in solo and with multiple initial players. Check the origin and chosen anatomy on the first turn, and add an unrelated later player. Keep private memories out of NPC speech.
2. Rush levels before turn 200, travel abroad at turn 200, and return during combat or a championship. The delegation waits. Return calmly to an eligible town after establishing a life.
3. Refuse questions, protect the ledger, investigate a false witness, and produce a real disclosure. Only the last can establish the personal trace.
4. Put a weak bearer beside a strong unrelated player. Check the intended target and the shared encounter. Test actual escape, ordinary knockout, failed restraint and genuine custody separately.
5. Ignore or decline the audience. Complete the carrier and relay work through Reika. Test an agreed audience and actual guest-key handover independently.
6. Try direct tower and realm entry without permission. Enter with one key and companions. Lose it inside and return through the fixed lantern. Visit each destination and find its ordinary way back.
7. Study a practical scroll, an advanced scroll and a masterwork. Try natural follow-ups, failure, reload, two readers, two copies, a traded active scroll, insufficient Gravity and a known formula. Watch live logs for late or duplicate effects.
8. Complete the local investigation with the dispatch copy and with an authenticated alternative after losing it. The chapter concludes with the Ardelis lead and ordinary play continues.
