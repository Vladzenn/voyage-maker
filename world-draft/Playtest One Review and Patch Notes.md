# Playtest One review and patch notes

2026-10-27. Based on the unchanged local Portals export and the author's PlaytestOne.docx. The source document was read, its three embedded illustrations inspected, and its observations compared with current world data and the ChikaraOld/Luxcellia references. It was not modified.

The author confirmed that the spider incident should be built now, ordinary foreign routes should remain usable before it, and the compulsory examination applies to enrolled students while outsiders may opt in. The later inventory-key idea supersedes the earlier separate hidden-room proposal.

## What the playtest revealed

| Evidence | Finding | Change |
|---|---|---|
| Turn 11: Akane has short dark hair; Tōru becomes a gray-bearded, gruff man. | Their real appearances lived in visualDescription, which the community reference says is not read by the narrator. | Established appearance is now included in every existing NPC's basicInfo. Portraits and visualDescription remain unchanged. |
| Turn 13: “The authored realms are this world…” | Production vocabulary had been placed in lore and public descriptions without a strong separation from dialogue. | Cleaned the public entries and added a private-rules boundary across story/dialogue generation. Residents discuss places and routes naturally. |
| Turn 10: “I flash a Sage Court sigil” is spoken aloud. | A described gesture was treated as part of the quotation. | Explicit dialogue/physical-action separation, preserving only supplied spoken words. |
| Turns 10–19: accepted credentials are repeatedly questioned. | Identity verification, an order's scope and willingness to act were being reset or conflated. | Preserve resolved verification and the actual achievable result of social checks; allow practical disagreement without repeating the same proof demand. |
| Turn 3: only three students are named when the full roster is requested. | The answer dodges available information and invents a timetable. Kōta Arakawa and Miyabi Tsukishiro are real cast members, not hallucinated names. | Added the four exact rosters and instructions to answer finite information requests fully without inventing schedules or cohorts. |
| Turns 7–11: the Archons' locations are inferred from their offices. | Holding a Conclave seat does not establish a particular meeting or override current placement. | Current-state and actual-movement guidance; a question about someone's location does not teleport them. |
| Repeated “measured,” “dry,” credential speeches and signature gestures. | Different people drift toward one formal bureaucratic voice. | Character-specific action/voice guidance and contextual rather than constant quirks. |
| Strong spells visibly scratch the developer construct. | A huge developer HP pool is not a normal target for judging Archon power. Reika also lacked an abilities array in the source JSON. | Preserve authoritative damage while rendering real scale; restored Reika's five exact approved abilities. Existing levels and numerical combat parameters are unchanged. |
| A formal encounter produces a substantial early relationship change. | A successful official request is not automatically friendship or attraction. | Proportionate relationship guidance, with no claim that prose alone fixes engine scoring. |
| A walk is reported as 20 km. | This is map scale/distance behavior, not proof that room prefixes caused a teleport. | Retained the author's geometry; narration should respect supplied distance and actual transport. Rescaling the existing city is a separate decision. |

## Starts and first-day flow

All four academy openings now follow **enrollment → orientation → an actual first class/activity**, with their own people, rooms and colors. They establish admitted adult students and supply the correct admission packet. Each has an enrollment quest whose finish requires recorded check-in. Visitors are no longer the default explanation for these explicitly selected student openings.

Non-academy choices remain separate:

- **Merchant: First Morning** at Four Sages Bazaar.
- **Village Life: Pebbletown**, **Clovermead**, or **Saltmere**. Separate cards provide an explicit native location choice without inventing a new creation selector.
- Four **First Day of Work** starts, one academy each, with a genuine appointment letter. The teaching/support role follows the actual background; existing professors keep their posts.
- **Random**, retaining its existing public Glowhaven locations.
- **Developer: Portal Inspection**, paired with the existing noncanonical developer preset.

There are **14 starts**. Dragon Hoard's old Missing Staff start becomes **Dragon Hoard: Arrival Gallery**; Hydra Head's Garden Walk becomes **Hydra Head: Arrival Court**. All trigger references were updated. Employment starts establish context but do not silently grant an experienced professor's mechanical build; broader starting experience/progression remains to be designed.

## Natural names and stable identity

Stored NPC keys, proper names, state updates, roster records and factual card relationships retain canonical full names. Ordinary speech and narration may use a first name, surname, title or suitable honorific: Professor Saitō, Sanada-sensei, Archon Todo, Hinae. These forms map back to the same existing identity. A spoken address is not a new NPC or an instruction to rename a stored character.

The Character Creation Format was updated with that distinction. Appearance in the narrator-facing field is now a verified export requirement. There is no new aliases field or separate display-name schema invented for this purpose.

## Portal keys

| Key | Actual use | Availability |
|---|---|---|
| Drakenspire Portal Key | Selects Drakenspire from the existing Evertree Portal Room. | Ordinary authorized issuance; included in developer test equipment. |
| Asterveil Portal Key | Selects Asterveil from the same room. | Ordinary authorized issuance; included in developer test equipment. |
| Silver Web Portal Key | Opens the anchored route to Stranded Threshold from that room. | First actual return from the displaced examination, or a legitimate replacement afterward. |

The description preserves its route and, for the silver key, its discovery history. Keys are reusable and have no passive combat bonus. Outbound triggers check real inventory possession; a spoken claim or drawing does not suffice. A public transit counter can issue ordinary keys without an audience with the Great Sage. An accepted mission contact can also arrange one.

Keys record portable access while persistent flags preserve the one-time incident, discovered route and defeated enemies. Losing a key does not undo the history. Return arches at the destinations do not require a key, so losing one there does not itself strand a traveler. There is **no separate Silver Webby Portal Room** area or location.

## The first regional field examination

An eligible enrolled student receives the examination notice at **level 20 or later**. It is a due educational task, not a teleport in the middle of another activity. Outsiders can volunteer. Developer level 100 does not automatically activate the event; a developer can explicitly request the test.

After acceptance and an actual court-authorized briefing, the first committed use of an ordinary route key for that examination is displaced once. The same route rule chooses normal travel or that one displacement, avoiding two competing teleport triggers. The real traveling party and actual party NPCs travel together; unrelated classmates do not get recruited or moved.

They arrive at **Stranded Threshold** in **The Silken Descent**, a defined otherworld. A visible return arch works immediately. The player can leave without descending, fighting or defeating a boss. First return gives the Silver Web key and establishes its arch in the existing Portal Room. Drakenspire and Asterveil remain available.

Reporting the incident completes the examination record. The optional deeper investigation is **Silver Threads Below**:

1. Stranded Threshold.
2. Threadfall Galleries.
3. Molting Warrens.
4. Sunken Broodworks.
5. Silkbound Reliquary.
6. Widow's Crucible.

Resolved passage challenges reveal the next location without teleporting the party there. Observation, tools, physical skill, bypasses and actual magic can contribute. Retreat remains possible. Two authored spider defenders persist as individuals rather than respawning because the player returns.

**Shizuru Amagumo**, an adult arachne matron, occupies the lowest chamber. She is a level-38 boss, dangerous rather than an endgame replacement for the Archons. Actual combat defeat requires authoritative HP/result evidence; a genuinely achieved nonlethal surrender is a separate possibility. Owning the key, flirting, declaring victory or finding an empty map label does not resolve her. Her magic does not drain souls.

The final investigation needs both the real matron outcome and a received report to the court oracle. The explicit reward is **1,800 XP**, applied once by the quest effect; it is a draft balance value. The route stays available after resolution. No new apocalypse timer, fixed three-student team rule or prophecy from the player's improvised dialogue was promoted to world canon.

## New cast

- **Mihoshi Kagamihara:** Human, 35, Divination affinity; the Great Sage's warm, plainspoken court oracle. She separates a seen fragment from an inference and refuses to turn uncertainty into compulsory destiny. She receives visitors in a new court observatory.
- **Shizuru Amagumo:** Adult arachne matron, 147, Nature and Fire affinities; a proud, territorial boss whose weaving snagged the transit route.
- **Silverthread Stalker:** An upper-gallery spider defender.
- **Moltback Silkguard:** A heavier broodworks defender.

The two humanoid affinity counts used independent weighted draws saved in the authoring record. New portraits and dungeon artwork were not generated. The new cards are available separately for review; JSON remains the roster source of truth.

Voyage normally generates missing NPC and location images during play. Add your own art before encountering this new content if you want to avoid that generation. No placeholder external URLs were fabricated. The community references describe this behavior for [NPC portraits](https://wiki.unofficial.voyage/world/npcs) and [location images](https://wiki.unofficial.voyage/world/locations).

## What was preserved and what was tested

All 128 original NPC identities, order, portraits, placements and numerical combat settings are retained. Their public information now includes established appearance, Tōru's body-casting wording is clarified, and Reika's missing approved ability list is restored. Every existing map coordinate, image and path is retained except the added observatory connection. All **268 existing media fields** are preserved. No synced source, supplied document or reference world was changed.

Current totals: **132 NPCs, 5 realms, 5 regions, 97 locations, 364 areas, 61 lore entries, 14 starts, 29 quests, 75 general triggers, 34 item types**. The 22 existing party quest triggers remain. Six attributes, 42 skills, ten player techniques and the existing HP/MP/progression settings are preserved.

Local structural, reference, size, roster and media checks passed, as did **35 script/lifecycle fixtures**. Fixtures cover inventory requirements, one-time displacement, normal travel before the event, retreat, repeat visits, replacement keys, actual followers, progression gates, real victory, one-time reward and enrollment state. They execute the scripts while mocking the documented runtime and supplying semantic decisions.

**No Studio import, full platform validator, live AI dialogue test, multiplayer session, downed-companion transport test or boss balance playthrough was performed.** The first playable version still needs these checks. Narrator discipline, eligibility from background, fresh handover detection, consent and actual surrender remain AI-judged. The documented placement effect cannot move a downed NPC; carrying or evacuating one needs specific live testing rather than an unsupported promise.

Use a **new test game**: start keys and some opening definitions changed, and the update is not an old-save migration. See the next-playtest checklist and research decisions for a focused test sequence.
