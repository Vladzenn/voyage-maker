# Steel and Spirits — Akitsuhara implementation and review

Initial implementation from supplied Studio export `74c54aa4-8d7d-4ba4-927f-6cb52be23c1a`. This export owns the twelve supplied map images and coordinates. Earlier planning counts and names are superseded by this implementation. The later placed-location export and character-creation/portrait follow-up are documented in Akitsuhara - Placement and Portrait Follow-up.md and docs/CURRENT_STATE.md.

## Delivered content

| Addition | Implemented |
| --- | --- |
| Country | Akitsuhara; capital Benitsuru, western Mizuhara and eastern Koganedai |
| Country map | Twelve supplied tiles, unchanged images/crops and region coordinates |
| Geography | 102 country locations / 335 areas; seven spirit locations / 21 areas |
| Cast | 93 people and four individually named yōkai; all 97 portraits uploaded |
| Encounter templates | 34 new npcTypes; ordinary enemies are generated instances |
| Native quests | 47 new undertakings and one local licensure copy |
| Developing native arcs | The Price of a New Edge; Where the Fog Answers |
| Items and techniques | 40 items, 54 abilities, six talents and six starting kits |
| Creation backgrounds | 21 additional origins; 14 optional past-experience choices; 44 additional professions |
| Starts | Six Akitsuhara, one Drakenspire, one Asterveil researcher |
| Factions | Eight additions; international Guild affiliation remains established |
| Lore | 18 additions and the older Oni Magitech entry reconciled |

Country roads and institutions have practical purposes. Households have rival interests without every resident belonging to a conspiracy. The cast includes independent adventurers, rōnin, foreign visitors, bandits, civilian workers and household members. Minor residents have their own interests and flaws; roles are not quest objectives disguised as people. Named nonhumanoids retain their own anatomy and naming patterns.

## Map and travel

The placeholder New Realm becomes Akitsuhara. Region 1–12 follow the supplied four-column, three-row grid, renamed Blackpine March, Thundercrag Highlands, Mount Shiun, Snowcedar Heights, Mizuhara Lake Country, Bamboo Veil Valleys, Benitsuru Basin, Koganedai Terraces, Mirror-Reed Lowlands, Golden Grain Plain, Redleaf River Country and Lanternwood Border. Locations have provisional coordinates for the author to refine. The packaged CSV/Markdown index lists every address, band and initial resident.

Native `areas.*.paths` accepts references inside the same parent location. Official validation identified and rejected the first attempt to use those arrays for roads between locations. The final file keeps reciprocal local area paths; ordinary inter-location routes are described in actual location text, with a connected authoring index. This is free country travel, not a new dungeon gate controller.

The regular capital transit shrine connects with Evertree Base - Portal Room. Authorized transit desks in Benitsuru, Drakenspire and Asterveil can approve a legitimate Glowhaven journey and issue its key locally, including to characters who begin abroad. This is actual approval and handover, not an automatic starting grant. Its outward route copies the existing portal decision, including the original once-only anomaly and shared per-turn transit lock. Every old portal trigger and all old Spider data are unchanged. Return always lands at the Evertree hub. Oni Nation Portal Key issuance uses existing court/delegate approval; Evertree staff can handle a legitimate request without sending the traveler on an unnecessary tour. A bare unapproved claim does not grant a key.

Moonless Torii is a different local gate. A Bell for the Mist is a small level-3 shrine undertaking: recover an accessible clapper near the mooring and restore the bell with Sae Kagurazaka. No rare drop, powerful boss or particular affinity is required. Deliberately ringing Restored Way Bell permanently opens the gate. Opening does not automatically move the party. Subsequent entry needs the stored opening, not continued possession of the bell. The Veiled Threshold return is always available and leads to Moonless Torii - Torii Court, not Glowhaven.

## Quests, arcs and exact events

Ordinary new jobs use native typed `completionCondition`, conclusive outcomes and `onCompleteEffects`. They do not receive individual acceptance/progress/completion controllers. A client, suitable guild board or an actual developing story can introduce them. Job fees, experience and any service credit have one completion owner. Foreign expeditions remain separate from the interrupted level-twenty field test.

The two native arcs describe public circumstances, concealed stakes, possible developments and bounded endings. They do not prescribe the player's allegiance or a single combat solution. Water disputes and the forest hunt remain ordinary quest/local situations rather than two additional always-active arcs. This avoids adding unnecessary global semantic checks.

The 24 new root triggers cover the network route, delegated key issue, Soul Torii, one bounded roaming actor, occasional requested forest information, the local branch and a shared contract-choice helper. They are not controllers for every conversation. Existing licensure and promotion logic is reused with the international badges and credits.

Hagire is the unique level-42 hostile stalker. Her three-haunt placement changes at most once per 24-turn interval, only while offstage and not engaged, accompanying a party, dead or already excluded from the protected route through the completed hunt. Her individual card is not an instruction to create multiple copies. Ordinary yōkai use npcTypes; Oroha, Koma and Suzu-no-Ura are the other three named exceptions.

## Requested playtest corrections

- **Extra starting marks:** remove the shared 18-mark itemSettings grant; retain every authored start's 1,000 marks and intentional trait money. A wealth/background choice can still alter the final total.
- **Exam becomes a job:** existing and local licensure briefs explicitly identify the judgment notice as a hypothetical sample and the practical as an onsite assessment. Quest-generation guidance repeats this narrow boundary and recognizes a sufficient natural answer. This is AI guidance; live recognition still needs testing.
- **Several unrelated contracts accepted:** 11 older flagged acceptance triggers and the four rank-specific parcel checks now require the same uniquely selected current offer. The board stores its two actual displayed choices and supplies exact client, site and fee. One shared helper handles ordinary native board choices. Native UI acceptance remains available. Ambiguous yes to two offers does not accept either; clear yes to one offer works. Text matching is deliberately narrow and relies on a semantic actual-acceptance condition; unusual paraphrases may still need a clearer choice or the native Accept button.
- **Creation:** Physical Foundations is a longer positive description; the Force attribute and Force Combat skill remain distinct. Expanded origins give a single +1 utility skill. Professions remain one optional useful-skills choice. Up to two Special Talents are permitted by the author's private change; do not mention that selection-limit change in public notes.

These changes do not erase erroneous quests already accepted in an old save. Reject/abandon those explicitly if necessary. Importing a world update is not asserted to migrate every existing save.

## Art

All 97 cast portraits and the Veiled Cedar Reach map are uploaded using the official Creator API, with exact-name/SHA receipts in `tools/oni-nation/hosted-art.json` and the supporting-art receipts. Their URLs are in the world. Existing portraits, map tiles, location images, music and voices are preserved. The supporting batch is complete. Sana Kuroiwa, Shōen Kagetsuna and Misao Shingū each received one separately authorized replacement; unrelated portraits were preserved.

The cast uses the established colorful 2D style. Clothing and lighting vary. Locally practiced magic favors flowing, tapered translucent forms without changing disciplines, numerical strength or the global rendering style. Magitech remains selective new imports; swords, crossbows and armor, no firearms. Shigure Tsubakiri conceals one extraordinary finite articulated polearm prototype.

Visual review found consistent faces, varied clothes and the intended recognizable major silhouettes. Several portraits have tighter headroom than the guide's 12.5% target; some affinity effects are subtler than others. The guide's composition target is not claimed fully satisfied. No extra generation pass was made. The review contact sheet is packaged separately for author approval.

## Validation and manual testing

The official authenticated Creator API `/validate`, draft stage, returns **valid with zero errors and warnings**. It did not save or publish the Studio world. Portable validation checks JSON structure, references and field caps. `test_oni.cjs` executes emitted scripts with supplied semantic answers; the existing creation, items, fieldwork, adventurer and Crucible fixtures also run. Exact authorized-delta hashes extend preservation assertions without replacing the earlier baseline fingerprints. Current behavior tests use the real updated scripts, not the projected older view.

Static semantic eligibility probes cover Benitsuru browsing, Evertree, both Soul Torii sides and all prior scenes. Current examples stay within the documented budgets; Crucible live-bout probe remains at 15/15. These are conservative local estimates, not a live scheduler trace or a guarantee against future crowding. Generated quests and later arcs must be budgeted again.

Before release, test in Voyage:

1. Each new start's actual cast, address, immediate invitation and player freedom; six nation starts should be local and all eight appear before faculty work starts.
2. No-background 1,000 marks versus intentional money traits; optional creation category rendering and the enlarged profession/origin groups.
3. New guild assessment without a sample repair quest; international badge recognition; one chosen contract without unrelated acceptance; unchanged client/site/fee; no duplicate completion payment or badge.
4. Ordinary Akitsuhara crossing below level 20, the unchanged once-only surprise above it, and exact Evertree returns. Use a clean test when testing the surprise.
5. Bell quest with a noncaster, awakening without forced travel, return, reopening after dropping the bell and whole-party movement.
6. Beginner job nuisance damage and optional remote threats; no claim that region bands alone guarantee a combat result.
7. Hagire's rare offstage relocation, real hostility, interrupted movement while present/in combat, finite hunt resolution and no revival after defeat.
8. Fog-map pins and ordinary roads; adjust provisional coordinates to the map in Studio. Confirm that native local area paths stay inside their parent location.
9. Arc recognition of negotiation, refusal and completed settlements; exact prototype ownership and no free confiscation or forced coup.
10. Multiplayer agreement, per-player badges and rewards, split-party portal attempts, and native quest completion recognition. Mocked scripts do not prove live AI or multiplayer behavior.

## Unimplemented future work

Further households and additional independent stories can be added later; the launch cast’s portraits are complete. The Chained Dragon, Shadowspire, Citadel of Dreams and expanded prison stories remain separate future arcs. They are not silently launched by this update. No new NPC schedule system, country-wide crime controller or firearm system was added.
