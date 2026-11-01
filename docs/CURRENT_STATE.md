# Current state

Updated 1 November 2026 after **Champions of the Crucible**. The earlier Character Creation & Polish patch and its import hotfix are preserved.

Public release numbering: Character Creation & Polish was published as **🐙 Minor Patch 3**. Minor titles use an unrelated animal emoji followed by `Minor Patch n`; feature names belong in body subheadings. The next new minor release is **Minor Patch 4**. This title-convention clarification changes documentation only.

Public announcement style: minor patches stay compact; major releases use fuller, more descriptive thematic sections, short paragraphs and selected bullets. The Crucible announcement has been expanded accordingly, including the author's requested short Conservatory unlock explanation (championship trophy and Silver Web Portal Key at the Evertree Portal Room). `research/Patch Note Creation Guide.md` records the distinction and allows explicit author-requested unlock guidance. This follow-up changes documentation only; the playable world is unchanged.

Studio import hotfix: the reported rejection exposed twenty-four missing `amount` fields on talent ability requirements and two Special-tier item prices below the configured minimum. All twenty-four trait requirements now include numeric `amount: 1`; Rain-Counting Brooch and Polite Kettle Bell are priced at 300 marks, inside their existing tier. The builder and portable validator are corrected, with regression tests reconstructing all twenty-six reported errors. No other world content, media, maps or Spider Realm mechanics change. Reimport the refreshed full patch file; local checks do not replace a fresh Studio import.

## Active world

The canonical full world is `world-draft/WorldAlpha - World.json`. The latest user-supplied Studio export is `b44dcd0f-0fe6-49d9-9b55-34301190d203`. Its thirty-three added location images, sixteen uploaded Adventurers portraits, Marika Hoshino level 30, removed non-badge item art, Permadeath naming, three-level attribute-award interval and other user edits are preserved. Its 80% Stamina rest fraction remains; the accompanying explicit instruction set starting/base maximum Stamina to 100. Derived section files remain synchronized.

Current content: 272 NPCs, 176 locations, 736 areas, 6 realms, 10 regions, 144 quests, 3 native arcs, 412 items, 694 abilities, 670 traits, 114 NPC types, 29 factions and 408 root triggers. Character cap 150; skill cap 100. Resources remain Health, Mana, Stamina, Renown and Infamy.

## Champions of the Crucible — implemented

See [mechanics and live-test guide](../world-draft/Champions%20of%20the%20Crucible%20-%20Mechanics%20and%20Playtest%20Guide.md) and [public Markdown](../world-draft/Champions%20of%20the%20Crucible%20-%20Patch%20Notes.md). The full downloadable export is `world-draft/The Schools of Magic, Arise! Full World Update 5 - Champions of the Crucible.json`; the canonical copy above remains the shared authoring source. `tools/crucible/build.py` uses an explicit merge base; `tools/crucible/export.py` packages the current world. Do not rerun the builder on an already updated full world.

- Optional persistent individual championships, not a native creation Game Mode. One human entrant, NPC companions outside the ring. Four/eight-person fields preserve actual NPC levels, results and eliminations; finals close once, prizes have one typed owner, and the next edition waits 100 engine ticks. Human roster changes pause for review rather than transferring the entry.
- Semantic recognition handles real registration, readiness, surrender/referee outcomes, treatment and collection. Stored state preserves the bracket and rewards; native Health can override a false win. No conversation-by-conversation quest machine.
- Latest user steering supersedes strict medical gates: appropriate optional care/rest, no invented injuries for unharmed fighters, and no exact resource-percentage requirement. Player treatment uses normal resource updates. Regulated nonlethal behavior, especially with native Permadeath, still requires live testing; no per-bout death toggle is claimed.
- Thirty-two new competitors, four staff, six crime contacts and Threnvoss: 43 JSON cards and 43 one-pass PNG portraits. All are saved under exact names. Rena Kogetsu/Fuyumi Hase have flagged gender-presentation mismatches; Nene Inui/Threnvoss have head-silhouette crop flags. No unauthorized re-generation. Full review/upload manifest is in `output/champions-of-the-crucible/` and original prompts are in `tools/crucible/`.
- The Sepulchral Conservatory is a compact midgame Nature/Soul dungeon: safe portal staging point, two guarded tending wings, gated heart, optional garden and archive, finite npcTypes guidance, named level-50 caretaker and combat/release outcomes. Backtracking remains available. The route needs a Championship Trophy and Silver Web Portal Key at the Evertree, not a spider-queen kill. Existing anomaly and Spider content remain unchanged.
- One square realm-map PNG and three location images accompany the dungeon. These and the portraits require Studio uploads; no hosted URLs or unsupported local-image fields were invented.
- 160 additional abilities, eight finite illicit jobs with negotiated compensation, one native sanctuary investigation, focused Oni culture lore and unchanged Oni ancestry modifiers. No Oni realm or other planned expansion was built.

Local validation covers schema/reference/size limits and emitted-script fixtures, including low/high-level fields, repeated callbacks, knockout contradictions, departure, identity changes, cooldown, prize ownership, both circuits, early heart clicks and portal return. All preceding NPCs/items/abilities and protected Spider configuration have preservation fingerprints. The static semantic-budget probe includes the new scenes. This is not live Studio validation or a claim of flawless AI recognition.

The previous Curios, Scrolls and Gentler Adventures pass remains intact: 300 additional items, thirty teaching scrolls, thirty scroll-only spells and their formula traits. This minor patch preserves every preceding item and ability exactly as supplied in the current export. Ordinary beginner safeguards remain; the Spider Realm's configuration, events, cast and surprise difficulty are protected.

## Character Creation & Polish — implemented

See `world-draft/Phantom Patch - Development Notes.md` and `world-draft/Phantom Patch - Creation Guide.md` for author-facing detail. Public notes intentionally omit the requested silent changes.

- Optional zero-to-three affinities and Physical Foundations at the top of starting studies (+1 Force/Finesse, no spells).
- Forty-eight total professions, more impactful native ancestry/temperament benefits, and an optional single Special Talent from forty-eight choices. Strong gifts carry native penalties or vulnerabilities; twenty-four talent techniques have real costs/cooldowns and trait gates. No Space/Time starting gift.
- Starting attribute ceiling 20 to accommodate selected bonuses; ordinary spending ceiling and the supplied two-points-every-three-levels cadence remain unchanged. Attributes still have no configured direct damage modifiers.
- Explicit Bald, more outfits, a separate optional accessory/outer-layer category, broader backgrounds and optional unusual player portrait compositions. Default framing remains waist/hip up; manual NPC portrait work is unchanged.
- Forty new items and sixteen starter kits, retaining a one-kit limit and existing combat methods.
- Cue-based fighting/death/travel music and narrower mood matches; every supplied audio variant and the existing MashMode are preserved. No music pinning state machine.
- Exact badge issuance reserved for the existing typed effects, with anti-alias inventory guidance and no extra quest-completion badge. Fresh runtime verification is still necessary.
- More compatible menu emoji with exact corresponding references renamed together. Permadeath naming from the user export is retained.

No additional cast nerf was performed. Every supplied NPC record, including Marika at 30, is preserved. The current role-mixed named-NPC medians (27 locally, 22 in Luxcellia and 18 in Chikara's positive-level records) are comparison data, not evidence for a blanket rebalance.

**Still open:** missing artwork for authored catalogue items. The global image switch is true, but the exact effect of per-item `needsMediaGeneration` remains unverified. Its tooltip was tautological and the browser helper failed; no unsupported bulk flag changes or invented image effects were applied. Keep badge artwork. See `docs/NEXT_PATCH.md`.

## Adventurers of Glowhaven — implemented

Read `world-draft/Adventurers of Glowhaven - Development Notes.md` for mechanics, sources, limitations and the live test checklist. Short public notes are in `world-draft/Adventurers of Glowhaven - Patch Notes.md`.

The public announcement was revised to the author's screenshot style: grouped features, a conversational opening and broad descriptions rather than small exact counts. This follow-up changes documentation only; the canonical world is unchanged.

- Sixteen new NPCs with sixteen completed PNG portraits: the Bellwether Company, Copper Laurels, Ysolenne, Suzuha Midorise and six guild/city/prison contacts. Six major portraits receive extra flair. Native JSON cards and separate copyable blocks are supplied. The user's latest export now includes actual hosted portrait URLs for all sixteen.
- Three native arcs: **The Woman Beyond the Frost**, **A Thesis No One Would Fund**, and **A Very Reasonable Recovery Fee**. Fighting and negotiation are genuine winter-arc outcomes; the pearl exists but the researcher's theory needs correction. The thieves are comic opportunists with independent lives.
- Sixteen finite native quests, including eight additional guild postings and two authorized prison errands. One completion/reward owner each. No new Silken Descent quest.
- Eighteen public situations and three arc leads surface sparingly without accepting quests. Occasional returning-client acknowledgments share their pacing limit.
- Eight half-day touring stops over four days for Ragnar Leonhart, Adoha Aonuma and Karia Morino. Adoha's Asterveil visits stay within the settlement. Presence, combat, party membership, incapacitation and actual commitments pause movement. Orivelle's existing circuit is unchanged.
- Six room/property arrangements inside existing locations: three rentals and three purchases. Native payer-scoped effects issue fixed keys/deeds after an agreed payment. Arbitrary new property keys use the normal item-generation workflow; a generic trigger cannot create a novel itemType directly. No offscreen rent deduction or passive-income system.
- Six creature types and twelve additional starting equipment kits; native permitted bonus ranges and refinement ceilings. Ordinary repairs and refinement must update the actual inventory instance without duplicating it.
- Weapon-led movement uses the actual Force/Finesse/Guarded delivery. Ally orders are distinct from the player's attack; finite allied healing and actions follow the native intent protocol.
- Optional solo **Permadeath Mode** (originally named Ironman), reinforced by a fatality ending trigger. The main world retains native `death.permadeath=false`, as Luxcellia does. A separate full-world **Native Permadeath — Solo** export enables the global native flag for strict permanent death. A game mode alone cannot toggle that native flag.
- Approved honor-based OOC repair command: `quest done: Exact Quest Name`. Completes accepted runtime quests only, including generated quests, through their ordinary completion/reward owner. It intentionally trusts the player; no new fictional deed is narrated.

The Adventurers release recalibrated seventy-four existing NPC levels. Faculty/headmasters generally occupy 28–32, Archons 52–55, court elites 42–45 and Karia Morino 42. **Ilyra Stillglass remains 100; Ragnar Leonhart remains 67.** The user's subsequent Marika level 30 is retained. Rovakthuun, Orrum, Orivelle and Spider Realm NPCs are preserved. Being a headmaster does not itself imply greater combat power.

## Validation and live checks

Use the portable README commands for current results. `tools/adventurers/validate.py` additionally verifies this release's preservation fingerprints; it is not a permanent prohibition on later approved changes.

Controlled trigger-eligibility probes found a real Canopy overload (18 checks against a 15-check no-active-quest budget). A planning dispatcher and eight narrowed state-phase offer gates reduce that probe to 7–8; eight representative scenes fit the documented budgets. These are configuration probes, not live engine traces. Scripts run after their conditions; they do not prefilter their own semantic checks.

Important manual checks: native arc surfacing and chapter assignment; winter combat and negotiation; research evidence choices; repeated encounters with the same thieves; touring movement/holds; rental and purchase recipients; real repair/refinement inventory changes; quest repair; Ironman death versus nonlethal training; multiplayer payouts and transactions; and an ordinary Bronze opening. Local tests and GitHub CI do not constitute Studio validation or live playtesting. Existing saves may retain older NPC levels and generated enemies.

## Workflow and remaining plans

**Current planning scope: Champions of the Crucible.** The [new implementation plan](../world-draft/authoring/plans/Champions%20of%20the%20Crucible%20-%20Implementation%20Plan.md) records the approved individual/nonlethal format, one recovery per bout, finite summons, withdrawal on venue departure, a 100-turn edition cooldown and about thirty-two new fighters. It proposes one persistent activity controller, result/reward ownership, varied actual arenas, a gated levels-35–50 Nature/Soul dungeon, ability expansion, crime jobs and Oni lore preparation. No playable world changes, portraits or new realm have been implemented in this planning session. Native-Permadeath nonlethal behavior, same-turn result ordering, resource-fill behavior and multiplayer targeting are explicit prototype gates. The Oni country expansion remains unstarted.

The pre-implementation failure audit is included in planning edition 1.1. It corrects the review-phase name, requires conflicting terminal observations to be reconciled before a winner is selected, and preserves unpaid prizes/medical care across edition replacement. Additional cases include knockout recovery teleporting before observation, wrong-fight evidence, schedule reservations, save migration and bounded no-contest/replay handling. These are design corrections, not runtime fixes or live-tested results.

Before the next implementation, read [NEXT_PATCH.md](NEXT_PATCH.md). It records the remaining runtime-artwork investigation and live badge check. The previously pending Studio edits are now merged; do not restore the older images, mode labels, Marika level or attribute cadence.

The private repository is https://github.com/Vladzenn/voyage-maker. Desktop completed work is published with `tools/project.py publish`; cloud work must be committed and merged before the next desktop fast-forward. Preserve `sources/` and the original AGENTS.md. The user confirmed the **voyage-maker** Codex Cloud environment is published; no task in that runtime has been verified by this chat.

Other expansion titles in `world-draft/Upcoming Updates.md` remain plans: Crucible expansion, Oni country/spirit gate, Vladimir Kujo's Shadowspire, the Eternal Chained Dragon and Citadel of Dreams. Do not implement them merely because their blueprint exists. The narrow Crime and Prison system is already shipped; broader prison simulation remains outside this release.
