# Crime and Creation — Development Notes

Prepared 31 October 2026 against the author's latest uploaded export. This is the implementation record; the separate public Patch Notes file is the short copyable release post.

## Source and preservation

Incoming SHA256: `be9eec7fd529f512a1205e212ddc840a86e186163b83520df3db737de5ab948d`.

The exact attachment is retained in `authoring/crime-update-2026-10-31/incoming-world.json`. It takes precedence over earlier Alpha28 and the 30 October planning snapshot. All supplied media, location and region coordinates, existing NPC identity and statistics, soundtrack configuration, Renown/Infamy, resource settings, level-150 progression, new equipment slots and original quest/trigger behavior is retained, with eight start-reference values migrated in the Studio identity fix. Evertree Base remains initially known with its supplied large radius. No NPC has been reassigned to another academy. Yūji Nishimura remains a Dragon Hoard student; the isolated Hydra Head encounter is not treated as a reproduced roster bug.

The export has 210 NPCs, 173 locations, 480 abilities, 119 quests, 17 story starts, 418 traits and 309 triggers. The incoming export already contained 118 quests; this pass adds one. Counts refer to configured content, not new content in this release.

## Crime and Prison

Five script-driven rules implement the narrow loop agreed with the author:

1. `cp_detect_heinous_crime`: latest-turn deliberate evil killing of a nonhostile person, or deliberate evil destruction of multiple buildings/a city block, in Glowhaven. Queues a poster three ticks later. Excludes torture alone, petty theft, ordinary assault, accidents, self-defense, hostile-enemy fighting, lawful duels, plans and remembered incidents.
2. `cp_clock_and_prison_release`: grants the queued `Wanted Poster` once; removes held copies inside Wraith Island Prison; counts only prisoner turns spent there; returns a prisoner after fifteen counted turns.
3. `cp_guard_arrest_attempt`: while the poster is held in Glowhaven, stages a real available City Guard patrol or present officer. Four-tick demand spacing. No dead officer resurrection or invincible police.
4. `cp_arrest_and_transport`: actual surrender or resolved capture plus a living registered officer in the scene before typed transport to Intake and Property Office — Processing Desk. No automatic capture from low Health or a demand alone.
5. `cp_voluntary_serve_remainder`: the actual prisoner explicitly elects to serve the remaining term quietly; asking how long remains is insufficient.

The poster's public description is simply “A wanted poster with your face on it.” Its actual presence is the enforcement switch. Disposal ends that automatic pursuit; no background flag restores it. Entry removes posters from visitors/workers too but does not assign them custody. The ordinary inventory system handles intentional disposal. A fresh qualifying crime may create a fresh case.

All five new scripts fail closed if `player-level` exposes more than one human player. NPC companions are not additional human players. Accompanying NPC positions are moved explicitly through the transfer and return, as escorted visitors/witnesses rather than additional prisoners. Actual party agency and role still require narration testing.

The old custody, work, release and escape definitions are retained. The short timer supplies a separate real release route; ordinary shifts and knockouts still do not discharge an inmate. No automatic fine, confiscation, replacement kit, prison start, compulsory escape arc or new reputation meter is added. Existing optional prison quests remain.

The timer is evaluated in planning and the crime/capture recognition in state. A first patrol may appear one turn after the item grant depending on native condition evaluation order. This is not a claim of transactional storage/effect commits.

## Supporting cast

- **Shūgo Katase** — human warden, security headquarters; a practical former aspiring singer with a real custody remit.
- **Chisato Kurebayashi** — rat beastfolk intake/release officer, processing desk; brisk, funny and precise about people's actual status.
- **Ena Minamori** — human infirmary practitioner, treatment room; gentle treatment and terrible jokes.
- **Tobio Hanekawa** — human inmate, mess hall; fraudulent maps, excellent patter and poor geography.
- **Mizue Akeboshi** — dark elf inmate, holding corridor; capable, acerbic and insufficiently repentant about retaliatory arson.

All five are detailed local characters with initially unknown journals, approved profile fields, behavior, concealment/knowledge, relationships and practical responses to danger. Affinity-count RNG draws are recorded in the change manifest. Akira Oritsu retains his job, statistics and portrait; only his relationship note is expanded. The five new portraitUrl values are blank, with no fabricated uploads. Their cards are compiled in Crime and Creation — Character Cards.md; the JSON remains the roster source of truth.

## Creation and portraits

Added 71 cosmetic choices and four start-only bond traits. Optional ancestry categories: Beastfolk Form (11), Fae Form (8) and Fae Stature (4), gated by earlier ancestry or Mixed Ancestry. Beastfolk default to mostly human bodies; more animal-like forms need explicit direction. Fae choices are individual examples rather than rigid subraces.

Appearance Builder retains the author's hair/eye/skin/build work and expands outfits to 26. Its background group moves into its own optional category. Four optional portrait categories offer 7 styles, 2 crops, 5 camera treatments and 24 backgrounds. Each portrait category permits one selection. The inherited Appearance Builder still groups choices under one category; its “one per group” wording is guidance, not a native per-subcategory selection cap. Written final appearance resolves conflicts.

No cosmetic choice grants statistics, equipment, membership or travel. The player route keeps the existing final-Appearance marker but removes mandatory headroom percentages, standing pose and detailed lighting recipes. Defaults remain waist-up/hip-up, complete head visible, crisp 2D anime linework and cel shadows. Realistic, CGI, plastic and sculpted facial treatment is discouraged. Explicit compatible player direction and optional styling guide composition.

Item generation now recognizes the author's configured Relic category, Accessories and Back slots; old contrary category text is removed. Equipment settings themselves are unchanged.

## Starts and first spell

Four starts: Hinae Komori / Haruki Saitō at Phoenix Wing; Satoru Kanda / Kei Aoki at Gryffin Tail; Kōsuke Shishido / Madoka Narukami at Dragon Hoard; Tōma Utsugi / Reon Fujisaki at Hydra Head. Each uses a real existing room and one initial-tick native setup rule placing the actual participants and granting the specific bond.

The bond produces a mild sympathetic heartache when the actual summoner suffers. It grants no copied wound, numerical Health loss, remote coordinates, mind reading, forced obedience, romance, ownership or recruitment. The start does not enroll the player or set academic-year flags. The unusual call is an accident, not a new talent or unrestricted humanoid-summoning power for the student.

Studio requires exact start key/name agreement. Sixteen starts use emoji-prefixed matching IDs and names, while the reserved Write Your Own key and name remain plain. Eight setup-trigger references are migrated to the corresponding IDs. Random remains last. The earlier community-reference interpretation allowing different IDs/display names was rejected by actual Studio validation and is superseded. Repeated free-afternoon slogans are reduced while mandatory morning classes remain. The incoming optional work and guild goals are preserved.

**Your First Spell** is a small optional invention quest, available in the four student starts. One separate discovery hook offers it elsewhere when the player actually begins a safe personal experiment. Native typed completion checks require a real successful Spellcraft design and repeatable test in a known discipline. Failure permits revision; no compulsory thesis. Native completion grants 100 experience once, no free spell card or skill. The ordinary learned-ability workflow records the result when eligible. A pending ability cooldown does not invalidate a verified design. Later accepted academy projects can recognize the same genuinely qualifying work instead of requiring duplicate paperwork.

World tips are replaced with 32 setting-specific messages, enabled every eight turns from turn 3 through turn 300. The other requested appearance and start choices are explicitly optional in their player-facing category descriptions.

## Verification and remaining live checks

The validator checks published task/leaf/aggregate limits, native references, ancestry gates, typed quest conditions, exact existing mechanics preservation, media/geometry preservation and new-character fields. The mechanics harness exercises the actual new scripts and compiles every retained script. Reports are in `authoring/crime-update-2026-10-31/`.

Local checks are not a live Studio schema validation or gameplay test. Test a fresh import and:

- One qualifying malicious killing, one multi-building destruction, and the excluded/innocent cases. Verify recognition uses the latest resolved event and does not repeat an old memory.
- Poster delay, disposal, no false poster in shops, enforcement only in Glowhaven, escape/resistance without forced capture, and an officer defeated before surrender.
- Capture with an NPC companion; the companion remains a visitor, actual positions agree, and there is no false sentence or recruitment.
- Normal intake, visitor/work arrival with a poster, no visitor timer, automatic release after the counted term, early explicit service choice, reload continuity and no immediate rearrest.
- Multiplayer: all five automatic scripts make no changes. Existing narrative/manual law remains separate.
- All four summoned openings on fresh characters; correct cast, rooms, trait, no enrollment/party grants, no unintended compulsory response.
- Optional ancestry gating, skipped portrait choices, multiple supported visual styles, correct waist/hip crop and mostly human Beastfolk; generated images still require visual review.
- First Spell: a failed design, a successful design/test, no duplicate reward, no extra ability while cooldown is pending, and a martial character postponing it.
- Custom start input, random-last display and first-day lessons, with no renamed-ID breakage.

Import the full world to apply the interdependent changes. An export is a fresh-game configuration; no unsupported existing-save migration is claimed.

## References

Community documentation consulted 31 October 2026: [Triggers](https://wiki.unofficial.voyage/mechanics/triggerDefinitions), [Traits](https://wiki.unofficial.voyage/mechanics/traits), [Trait Categories](https://wiki.unofficial.voyage/mechanics/traitCategories), [Story Starts](https://wiki.unofficial.voyage/world/storyStarts), [Tips](https://wiki.unofficial.voyage/other/tipSettings) and [current size limits](https://wiki.unofficial.voyage/appendix/size-limits). These are community schema guidance, not official promises of AI recognition. Local Luxcellia and Chikara exports informed the portrait source priorities and crisp anime direction; their world lore was not copied.

The new local Narrative Writing and Quest Craft Guide cites primary craft sources and records how to use them on future arcs and openings without copying a fixed formula into every AI task.


## Studio identity correction — 31 October 2026

The first import reported 17 story-start key/name mismatches. All 17 are now corrected, with eight typed start conditions migrated. Other world sections and the starts’ prose, media, grants, locations and order are unchanged except the native custom start’s plain display name. The builder now uses the shared story_start_names.py guard. The original malformed map fails 17 identity checks; the fixed map passes. Reimport is still required to confirm Studio acceptance.
