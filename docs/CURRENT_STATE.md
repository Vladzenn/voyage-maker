# Current state

Updated 1 November 2026 after implementing **Adventurers of Glowhaven**.

## Active world

The canonical full world is `world-draft/WorldAlpha - World.json`. The latest user-supplied Studio export (`90acb453-9939-48f1-84a8-d6d5bf681211`) differed from our preceding local world only by nineteen item image URLs. Those images, all existing hosted media, map placements and voices are preserved in this release. Derived section files include a new Arcs export.

Current content: 229 NPCs, 173 locations, 716 areas, 5 realms, 9 regions, 135 quests, 3 native arcs, 367 items, 510 abilities, 460 traits, 106 NPC types, 28 factions and 378 root triggers. Character cap 150; skill cap 100. Resources remain Health, Mana, Stamina, Renown and Infamy.

The previous Curios, Scrolls and Gentler Adventures pass remains intact: 300 additional items, thirty teaching scrolls, thirty scroll-only spells and their formula traits. All 360 preceding item definitions and all 119 preceding quests are unchanged. Ordinary beginner safeguards remain; the Spider Realm's existing configuration, events, cast and surprise difficulty are protected.

## Adventurers of Glowhaven — implemented

Read `world-draft/Adventurers of Glowhaven - Development Notes.md` for mechanics, sources, limitations and the live test checklist. Short public notes are in `world-draft/Adventurers of Glowhaven - Patch Notes.md`.

The public announcement was revised to the author's screenshot style: grouped features, a conversational opening and broad descriptions rather than small exact counts. This follow-up changes documentation only; the canonical world is unchanged.

- Sixteen new NPCs with sixteen completed PNG portraits: the Bellwether Company, Copper Laurels, Ysolenne, Suzuha Midorise and six guild/city/prison contacts. Six major portraits receive extra flair. Native JSON cards and separate copyable blocks are supplied. New portraitUrl fields remain blank pending actual Studio uploads; no invented hosted URL is used.
- Three native arcs: **The Woman Beyond the Frost**, **A Thesis No One Would Fund**, and **A Very Reasonable Recovery Fee**. Fighting and negotiation are genuine winter-arc outcomes; the pearl exists but the researcher's theory needs correction. The thieves are comic opportunists with independent lives.
- Sixteen finite native quests, including eight additional guild postings and two authorized prison errands. One completion/reward owner each. No new Silken Descent quest.
- Eighteen public situations and three arc leads surface sparingly without accepting quests. Occasional returning-client acknowledgments share their pacing limit.
- Eight half-day touring stops over four days for Ragnar Leonhart, Adoha Aonuma and Karia Morino. Adoha's Asterveil visits stay within the settlement. Presence, combat, party membership, incapacitation and actual commitments pause movement. Orivelle's existing circuit is unchanged.
- Six room/property arrangements inside existing locations: three rentals and three purchases. Native payer-scoped effects issue fixed keys/deeds after an agreed payment. Arbitrary new property keys use the normal item-generation workflow; a generic trigger cannot create a novel itemType directly. No offscreen rent deduction or passive-income system.
- Six creature types and twelve additional starting equipment kits; native permitted bonus ranges and refinement ceilings. Ordinary repairs and refinement must update the actual inventory instance without duplicating it.
- Weapon-led movement uses the actual Force/Finesse/Guarded delivery. Ally orders are distinct from the player's attack; finite allied healing and actions follow the native intent protocol.
- Optional solo **Ironman Mode**, reinforced by a fatality ending trigger. The main world retains native `death.permadeath=false`, as Luxcellia does. A separate full-world **Native Ironman — Solo** export enables the global native flag for strict permanent death. A game mode alone cannot toggle that native flag.
- Approved honor-based OOC repair command: `quest done: Exact Quest Name`. Completes accepted runtime quests only, including generated quests, through their ordinary completion/reward owner. It intentionally trusts the player; no new fictional deed is narrated.

Seventy-four existing NPC levels were recalibrated. Faculty/headmasters generally occupy 28–32, Archons 52–55, court elites 42–45 and Karia Morino 42. **Ilyra Stillglass remains 100; Ragnar Leonhart remains 67.** Rovakthuun, Orrum, Orivelle and Spider Realm NPCs are preserved. Being a headmaster does not itself imply greater combat power.

## Validation and live checks

Use the portable README commands for current results. `tools/adventurers/validate.py` additionally verifies this release's preservation fingerprints; it is not a permanent prohibition on later approved changes.

Controlled trigger-eligibility probes found a real Canopy overload (18 checks against a 15-check no-active-quest budget). A planning dispatcher and eight narrowed state-phase offer gates reduce that probe to 7–8; eight representative scenes fit the documented budgets. These are configuration probes, not live engine traces. Scripts run after their conditions; they do not prefilter their own semantic checks.

Important manual checks: native arc surfacing and chapter assignment; winter combat and negotiation; research evidence choices; repeated encounters with the same thieves; touring movement/holds; rental and purchase recipients; real repair/refinement inventory changes; quest repair; Ironman death versus nonlethal training; multiplayer payouts and transactions; and an ordinary Bronze opening. Local tests and GitHub CI do not constitute Studio validation or live playtesting. Existing saves may retain older NPC levels and generated enemies.

## Workflow and remaining plans

The private repository is https://github.com/Vladzenn/voyage-maker. Desktop completed work is published with `tools/project.py publish`; cloud work must be committed and merged before the next desktop fast-forward. Preserve `sources/` and the original AGENTS.md. The user confirmed the **voyage-maker** Codex Cloud environment is published; no task in that runtime has been verified by this chat.

Other expansion titles in `world-draft/Upcoming Updates.md` remain plans: Crucible expansion, Oni country/spirit gate, Vladimir Kujo's Shadowspire, the Eternal Chained Dragon and Citadel of Dreams. Do not implement them merely because their blueprint exists. The narrow Crime and Prison system is already shipped; broader prison simulation remains outside this release.
