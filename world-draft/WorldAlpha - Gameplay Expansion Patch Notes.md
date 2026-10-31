# WorldAlpha — Gameplay Expansion Patch Notes

2026-10-30

## Beta2 quest schema correction

Fixed the Studio-reported errors in Find Afternoon Work and Visit the Glowhaven Guild: both now have a required questSource string; the guild quest uses a supported story completion query. Its objective remains visiting the public hall, with registration optional. The work goal has a blank location so any suitable actual employer can satisfy it. Full world and standalone quests are synchronized. See the findings report for the correction and local checks.
## Beta playtest 2

Restored ten user-authored NPC voices from the latest supplied export, retained Ritsu's added assignment, disabled passive Mana/Stamina recovery, strengthened practice and acquisition, and added optional afternoon-work and guild-visit goals to all four student starts. Added a player-specific portrait prompt route after comparing the references' installed mod lists and image guidance.

See [Beta Playtest 2 - Findings and Changes](../research/Beta%20Playtest%202%20-%20Findings%20and%20Changes.md) for the complete voice table, source distinction, mod IDs, level-range explanation, recovery details and verification results. Pre-update files are in backups/Beta Playtest 2 20261030. Local checks pass; Voyage runtime and portrait generation remain untested.
## Beta status and playtest update

The project is officially in Beta as of 2026-10-30. The existing WorldAlpha filenames are retained as repository names; the full WorldAlpha export remains the import target.

- Re-merged only the user-supplied ItemGenerationAndUsage block, whose compact JSON serialization is exactly 20,000 characters. Kept the newer character-portrait prompt improvements already in the active draft.
- Changed Ritsu Kurogane's voice tag to the catalog voice "female harsh commanding."
- Set neutral, routine, and ordinarily pleasant relationship openings to 0. Require an observable, meaningful reason for any positive relationship delta; routine conversation, politeness, correct answers, and scene completion earn no points by themselves.
- Added 18 Marks to universal starting items and aligned the currency name to the defined Mark item, giving all story starts the same modest reserve.
- Raised primary aptitude bonuses from +4 to +5 and secondary bonuses from +2 to +3. Practical Training now offers up to two distinct choices. The current trait-category schema has a maximum-selection field but no documented minimum-selection field, so it cannot force at least one choice.
- Added per-NPC knowledge boundaries across opening scenes, NPC intent, dialogue, updates, summaries, and new-NPC creation. The player's private profile and backstory are narrator context; characters need a plausible source before acting on a fact.

The knowledge-boundary pattern is based on observed instructions in the read-only Overlord and Luxcellia examples and adapted to Glowhaven; it does not copy their world-specific content.

Validation: edited JSON files parse; compact ItemGenerationAndUsage length and full/split section synchronization were checked. Studio import, platform validation, relationship behavior, and runtime starting-item delivery still need playtesting.

## Character-creation portrait prompt polish

Merged the portrait-prompt improvements into `aiInstructions.generateCharacterBackground` in both the [standalone AI patch](WorldAlpha%20-%20AI.json) and the [full WorldAlpha export](WorldAlpha%20-%20World.json). The `Appearance` field now uses a labeled, image-ready prompt with deliberate pose, visual hierarchy, richer but controlled 2D-anime lighting/color, and a small number of setting anchors. It preserves the existing standing, centered hip-up 2:3 composition, headroom, selected appearance options, affinity rules, actual equipment, opening context, and separate narrator-facing background. Story narration and unrelated world data are unchanged.

Validation: JSON parsing and synchronization checks passed for both drafts; all character-generation instruction leaves remain under the documented per-leaf cap. No Studio image generation or visual playtest was run for this prompt-only change.
2026-10-27

## Files and preservation

The complete updated world is [WorldAlpha - World.json](WorldAlpha%20-%20World.json). Standalone NPCs, locations, and lore have been synchronized; the unchanged game-mode section still matches its standalone file. Use the full export when importing this update: the prison, quests, items, and instructions depend on one another.

All **128 NPC identities**, their roster order, portraits, biographies, personalities, affinities, equipment, and baseline placements are retained. All **269 existing URL fields** remain at their original paths, including every portrait, location/area image, map, and music URL. Existing location names, coordinates, radii, and discovery flags are retained. The existing prison location has a new parent region and realm. Its original image and original four areas remain.

The exact pre-update files are in [Gameplay Expansion 20261027-120442](backups/Gameplay%20Expansion%2020261027-120442/).

## Scale of this update

| Content | Before | After |
| --- | ---: | ---: |
| NPCs | 128 | 128 |
| Locations | 68 | 68 |
| Areas | 275 | 283 |
| Lore entries | 34 | 41 |
| Quests | 1 | 22 |
| General triggers | 0 | 31 |
| Party quest triggers | 1 | 22 |
| Item definitions | 0 | 18 |
| Realms | 1 | 2 |
| Regions | 1 | 2 |
| Game modes | 12 | 12 |

No new character-creation trait system, player spell catalog, or permanent companion recruitment was introduced. The focus is existing places, existing people, ordinary work, consequences, and scene quality.

## Places that support play

**27 locations** now have expanded functions and narrator-only situations: the 26 listed below plus Wraith Island Prison. Public descriptions explain services and actual role-holders. Selected room descriptions identify usable tasks and access rules. Hidden information distinguishes the real cause, who can help, and possible changes without publicly exposing secrets.

The situations include practical magic, awkward social priorities, paid work, professional reputation, unfair treatment, and ordinary pleasures. They are opportunities selected when relevant, not incidents that automatically restart on every visit.

- **Phoenix Wing Academy:** Red pennants snap above dueling rings and noticeboards crowded with cooking contests and field-partner requests. Visitors can ask about lessons, book supervised practice, consult instructors, or watch a legal bout. Kōhei Sanada handles academic permissions; Ritsu Kurogane teaches combat movement, Haruki Saitō explains fundamentals, and Ranka Kagari handles alchemy and healing. Akane Todo is the academy's Archon, with duties beyond its reception desk.
- **Gryffin Tail Academy:** Cyan banners hang above orderly lecture corridors, a sheltered reading garden, and a much less quiet training court. Visitors can attend announced lectures, request research access, arrange consultations, or find a study partner. Norio Shibata handles records and appointments. Gen'ichirō Mizuhara controls senior academic policy; professors retain individual priorities and methods.
- **Dragon Hoard Academy:** Yellow-and-gold displays fill the entrance gallery with working models, ambitious prototypes, and occasional apologetic notices. Visitors can inspect demonstrations, request supervised equipment tests, or find repair referrals. Miyu Asahina manages approvals. Madoka Narukami teaches stormcraft, Genzō Iwakura field survival, and Noriaki Takatsuki summoning and ritual practice.
- **Hydra Head Academy:** Violet awnings shade garden paths and broad tables where apparently incompatible people keep working together. Visitors can arrange consultations, observe demonstrations, discuss commissions, or join invited practice. Kiyoko Fujinami manages the school day with Reika Saionji. Kaoruko Hanazono teaches botanical and fragrance work, Reon Fujisaki enchantment, and Kana Fujimoto introductory lessons and spell safety.
- **Four Sages Bazaar:** Water splashes around the founders' monument as stallkeepers call over baskets and display charms. Rinpei Komatsu performs illusion demonstrations near the fountain and can give directions or introduce actual tradespeople. The arcades offer shopping, notices, and public meeting places.
- **Rune and Raven's:** Sample focuses glow behind glass while a workbench clicks behind the counter. Rui Takatori handles fittings and diagnosis; Reiji Takatori demonstrates accessories and adaptations. Customers can test a focus with permission, request a written estimate, or compare modest equipment with expensive alternatives.
- **The Perfumed Rose:** Scent strips stand beside sealed preparations in Céline Desrosiers's alchemical shop. Perfumes are the specialty, alongside labeled household goods and limited supplies. Customers can discuss a scent brief, compare samples, or commission a preparation after receiving a quote.
- **Violet Thread:** Garment rails surround Aya Orimoto's fitting alcove. Customers can seek repairs, practical academy clothing, formal commissions, and alterations based on how an outfit will actually be used. Reika Saionji's commercial interests do not make her permanently present at the counter.
- **The Farmer's Exchange:** Produce carts crowd balances, chalk prices, and damp sacking. Aoi Yonekura checks weights, negotiates loads, and introduces buyers to actual growers. Residents can buy staples, seek delivery work, or compare a disputed consignment.
- **Whitecrest Harbor:** Cargo chains clink above salt-darkened steps. Kaito Minato coordinates cargo handling and points travelers toward passenger desks, claims, and controlled sailings. Visitors can seek dock work, verify manifests, book passage, or ask about weather-dependent routes.
- **Roseberry Inn:** Supper reaches the common room before its plates do. Noriko Hanesawa offers beds, meals, directions, and limited introductions to people who use her inn. A shared bunk costs 6 marks and a plain private room 12 per night.
- **Crooked Tankard:** Benji Takarada's taproom is loud enough for laughter and arranged well enough for a quiet hearth-side conversation. It serves meals, drinks, introductions, and occasional paid help with a busy evening. A filling meal costs 3 marks and a modest drink 2.
- **The Golden Ladle:** Daichi Kamado serves craftspeople whose tools are still warm from work. Visitors can buy a dependable meal, order packed food, or compare commissions after a shift. A plain meal costs 2 marks, a substantial supper 4, and a packed lunch 3.
- **The Everlight Public Library:** Reading lamps illuminate shared desks and shelves polished by generations of hands. Lucien Delorme helps beginners and scholars locate useful sources. Public reading is free; copying, loan deposits, private manuscripts, and restricted access have separate conditions.
- **The Eternal Crucible:** Painted boundaries divide the tournament floor beneath steep public stands. Tomoe Enokida coordinates the work behind the spectacle. Visitors can watch announced bouts, ask about entry conditions, book approved practice, or seek event work.
- **Glowhaven Farmlands:** Tracks run between grain, vegetables, and irrigation channels that flash in the sun. Takumi Hatano organizes channel work and knows which growers share each run. Visitors can seek seasonal labor, buy produce by arrangement, or inspect a blocked branch.
- **Greywatch Keep:** Broken stone encloses the overgrown yard of an obsolete founding-era outpost. It has no active garrison or official use. Osamu Iseki sometimes visits to sketch masonry; accessible approaches allow surveys, drawings, and discussions of the old defenses.
- **Moonwhisker Emporium:** Perches, carriers, feed bins, and carefully spaced enclosures serve ordinary pets and magical companions. Mihoko Nekozawa offers supplies and practical care consultations. A summoned creature's needs depend on its nature; magic does not excuse neglect.
- **The Compassmaker:** Small mechanisms tick beside partly repaired compasses and labeled drawers. Seiji Haguruma diagnoses trinkets, replaces modest parts, and explains a device's limits before selling it. Customers may request an estimate or help reproduce an intermittent fault.
- **Blackstone Smithy:** Forge heat rolls past a counter stacked with hinges, blades, and practical hardware. Kazuo Kurogaki handles durable metalwork, tools, and honest repair estimates. Customers can commission a part or bring failed equipment for inspection.
- **The Silver Anvil:** Finished metalwork gleams beyond Shōko Shirogane's consultation desk while harder noises come from the workroom. Formal commissions, finishing, and inspections consider fit, use, material, and delivery time.
- **The Magistrate's Hall:** Petitioners wait under tall windows as clerks carry files between counters and hearings. Naoki Fudemura explains filing, authorized copies, and notices; magistrates make judgments. Residents may report disputes, answer summonses, seek an advocate, or request their own case records.
- **City Guard Headquarters:** Public reports arrive at Tetsuya Ōmi's desk while officers cross toward briefings and the yard. The City Guard patrols streets, investigates ordinary crimes, and makes lawful arrests. Visitors can report incidents, identify recovered property, or ask about summonses.
- **The Grand Sage's Court:** Public galleries lead toward an audience hall, council chamber, and offices where petitions acquire stamps and consequences. Visitors can submit evidence, seek hearings, or arrange authorized audiences. Ilyra Stillglass is not automatically available to every arrival.
- **Evertree Base:** Controlled palace approaches lead to roots where dense mana is almost tangible. Authorized researchers and maintenance personnel can make approved observations or assist a defined task. Strength, academy membership, and a casual palace visit do not grant entry.
- **Wraith Island:** Rocky shores and controlled landings surround the offshore prison route. Mirei Shiozaki pilots authorized supplies and checks weather, manifests, and passenger permissions. Visitors may work a legitimate delivery or arrange an approved crossing; this is not a public sightseeing excursion.

## New optional situations

Every new quest has a specific named contact, a location, an objective, design guidance, an explicit completion trigger, and a persistent resolved flag. Availability alone does not start work: the player must actually agree after hearing the premise. Failed, hypothetical, or merely promised results do not complete objectives.

| Situation | Contact | Main activity | Fixed fee |
| --- | --- | --- | ---: |
| A Formula Worth Selling | Ranka Kagari | Resolve the trial discrepancy before the recovery formula is sold. | None |
| One Standard, Two Students | Sōichirō Takamine | Obtain a reasoned decision on inconsistent reassessment requirements. | None |
| The Shield's Late Return | Mai Kajiwara | Diagnose the delayed shield discharge and carry out the agreed response. | None |
| What the Scent Becomes | Kaoruko Hanazono | Give the fragrance collaboration an honest release decision. | None |
| The Wrong Kind of Light | Rui Takatori | Reproduce the lamp fault and deliver the customer's agreed remedy. | 24 marks |
| A Crate Without a Signature | Kaito Minato | Resolve the missing handover signature on a sealed supply crate. | 20 marks |
| Water Owed Downstream | Takumi Hatano | Restore or renegotiate usable water for the affected plots. | 22 marks |
| A Fair Measure | Rinpei Komatsu | Settle the disputed measure through evidence. | None |
| Margins in Two Hands | Lucien Delorme | Submit a sourced correction to the conflicting safety mark. | 15 marks |
| Before the First Bell | Tomoe Enokida | Get a defensible safety decision on a shifted boundary. | 25 marks |
| The Keep's Last Survey | Osamu Iseki | Produce a usable survey and warning for the unsafe upper walk. | 18 marks |
| A Seat That Attended Class | Kana Fujimoto | Resolve the attendance concern using actual evidence. | None |
| Odds Nobody Agreed To | Yūji Nishimura | Carry out the agreed response to the unwanted dating odds. | None |
| Two Tags, Two Households | Mihoko Nekozawa | Return the companions to their actual households. | 12 marks |
| A Shift Behind the Sea Wall | Akira Oritsu | Complete an authorized prison shift and obtain its record. | None |
| A Date in the Ledger | Akira Oritsu | Obtain a verified review of an established custody-record discrepancy. | None |
| Fast Enough to Stop | Ritsu Kurogane | Complete a controlled movement drill and show a repeatable safe stop. | None |
| Explain It to the Fist | Maki Ogasawara | Help Maki Ogasawara demonstrate one understood principle rather than memorize its words. | None |
| The Staff Has a Better Social Life | Kōsuke Shishido | Find the actual missing staff and return or account for it. | None |
| An Explosion of Appropriate Size | Homura Hibino | Resolve Homura Hibino's proposed demonstration under actual agreed limits. | None |
| A Hunter's Pace | Genzō Iwakura | Complete the agreed field inspection and report what the trail actually shows. | None |

Seven jobs award fixed fees through completion effects, once. The other situations do not invent cash payments: any payment, work credit, or private bargain requires its actual terms. Prison work distinguishes a contractor's negotiated wage from an inmate's credit. Other outcomes can be corrected records, access, trust, a stopped unsafe sale, an honest refusal, or a remembered disagreement.

Ranka Kagari remains selfish and careless; Gen'ichirō Mizuhara can resist a fair standard; Maki Ogasawara retains genuine academic weakness; the chuunibyou characters' invented powers remain fictional. Completing a personal situation does not guarantee redemption, romance, or recruitment.

The supervised woodland task offers observation, crop protection, relocation, a justified hunt, or safe withdrawal. If the boar attacks, supplied combat outcomes decide injuries. Genzō Iwakura stays a capable veteran with a lasting leg injury. Wild Beast is available as a descriptive NPC type for runtime encounters; no new fixed creature or portrait was added to the roster.

## Economy

The existing currency name is retained: **marks**. A single Mark item is the base unit; there is no second wallet or conversion system.

| Anchor | Typical amount |
| --- | ---: |
| Plain meal | 2 marks |
| Substantial supper | 4 marks |
| Packed lunch | 3 marks |
| Shared bunk | 6 marks/night |
| Plain private room | 12 marks/night |
| Straightforward day labor | 18–25 marks |
| Skilled work | 35–60 marks |
| Basic inspection | 6 marks |
| Small repair | 12–25 marks, plus agreed parts |
| Simple casting wand | From 60 marks |
| Household enchanted lamp | Around 80 marks |

Prices can vary for stated reasons. Quotes require acceptance; inspection is not permission to repair. Customer goods, loaned tools, deposits, sealed cargo, and work materials remain accounted for.

The 18 item definitions cover marks, food, bandages, a healing draught, common diagnostics and repair supplies, a basic focus and lamp, fragrance samples, work gear, and legitimate case/custody paperwork. Bandages and the healing draught have limited authored health bonuses; they do not cure aging or lasting injuries. Equipment does not grant unlearned spells.

Fixed quest fees are mechanically authored. Ordinary trade, negotiation, deposits, and ownership still use Voyage's inventory handling and narrative instructions; this update does not install a server-enforced universal shop simulation.

## Wraith Island Prison realm

The exterior **Wraith Island** remains on the Glowhaven coastal map. The existing **Wraith Island Prison** location now belongs to the **Wraith Island Prison** realm and **Wraith Island Custody District** region. This represents the physical secure campus, not a new magical plane.

The prison retains Sea Wall, Entry Landing, Outer Yard, and Cell Wing. Added rooms:

- Intake Room
- Records Desk
- Workroom
- Stores
- Infirmary
- Visiting Room
- Mess Room
- Exercise Yard

All new rooms connect to the existing graph. Original imagery is preserved. No new prison map artwork was generated.

Playable roles include prisoner, employee, contractor, approved visitor, and actual covert intruder. Permission is specific to role. Work is not custody, and a work order is not an exit pass. The narrative must record legal status, property deposited, sentence or review, permissions, and the actual basis for release.

Nine general triggers cover authorized access discovery, the physical crossing, discovery on arrival, recorded intake, worker classification, serious court orders, lawful departure, and successfully resolved escape. Capture, conviction, and successful escape are not decided by a keyword or a single unrelated social roll. A transfer follows actual events and supplied outcomes.

A sentence can be served through an appropriate, actually completed interval followed by verified discharge. There is **no automatic sentence countdown measured in player turns**. Court and property details are preserved in narrative memory; escape can leave a wanted case. The shared party-location effects are used only when a sole player or the whole active player group actually travels. Individual multiplayer imprisonment in a split party is not implemented by these transfer triggers.

Knockout recovery now respects actual custody: a prisoner wakes under custody, usually in the infirmary, rather than automatically waking free in the city with deposited equipment restored into use.

## Narration and cast behavior

The sparse stage-direction rules were replaced directly in their existing task keys. New guidance asks for compact but vivid scene prose, concrete sensory details, distinctive dialogue, and one responsive beat at a time. Three short examples demonstrate arrival, character pressure, and quiet companionship; they are marked illustrative rather than events to replay.

Rules are placed in the tasks that use them:

- Story: texture, voices, cast size, choices, privacy, and ordinary activity.
- Encounters: relevant local opportunities and appropriate timing.
- New NPCs and NPC details: roster-first role matching, full names, existing card format, adult student cast, and preserved flaws.
- NPC updates: actual relationships, movement, recruitment agreements, and stable competence.
- Items: quotes, consent to transactions, ownership, limited effects, and no double payment.
- Action resolution: learned magic, actual checks, safe testing, and prison access.
- Summaries: evidence, who knows, promises, payment, custody, and unresolved obligations.

The existing combat-only NPC-intent architecture is unchanged. The narrator handles ordinary social scenes; rich prose does not change combat results, invent player thoughts, or choose a player's response. The 12 game modes are preserved.

The resulting Story instruction task is approximately 14,000 raw text characters, beneath the checked documented task cap. This is a focused instruction revision, not a claim that more text guarantees better model behavior.

## Concrete cleanup

- Added the missing City Guard faction used by four existing officers.
- Replaced 59 undefined Unknown NPC-type references with the neutral Resident type. Added Great Sage for Ilyra Stillglass and Wild Beast for relevant generated creatures.
- Assigned intentional positive levels to the 59 city additions: most ordinary residents are level 18; relevant specialists are higher. City gate/desk officers are level 36–42; Akira Oritsu is level 55.
- Added two role-appropriate defensive/control techniques to each of the four city officers and Akira Oritsu. Existing affinities and personalities remain unchanged.
- Retained academy power levels: students 15, professors 50, headmasters 70, Archons 85, and Ilyra Stillglass 100.
- Corrected the prison's operational status and added its access rules.
- Removed production commentary from the affected exported lore while preserving genuine mysteries and unassigned civic portfolios.
- Made the familiar Glowhaven region initially known; the five marked location exceptions remain initially unknown.
- Added a start-specific tick-zero placement for Hinae Komori at Arrival Court. Her ordinary saved Lecture Hall placement and the distributed academy roster remain intact.

## Verification and limits

The local validation pass completed **4,348 assertions** with no failures. It checks JSON, key/name identities, NPC locations/types/factions, region/realm links, area connectivity, quest and item references, clause limits, documented size limits, preservation, and mechanical trigger fixtures.

Fixture scenarios include: no completion before acceptance, no completion for unfinished work, wrong-location hand-ins, one-time fees, correct opening staging, unresolved versus completed crossings, visitor versus custody state, work not clearing custody, and lawful release versus wanted escape. Semantic judgments were supplied as fixtures: these checks test the authored wiring, not an LLM's interpretation of live prose.

All 269 existing URL fields and the permitted scope of NPC changes were checked against the saved baseline. Synchronized standalone sections were read back and compared with the installed full world.

**No live Voyage Studio import, full current codec validation, or gameplay playtest was performed.** The public schema download endpoint refused access with HTTP 403, so the local checks use the documented field shapes, current export conventions, and published limits rather than claiming a full schema pass. In particular, semantic acceptance/completion, inventory effects, cross-realm access, and legal-role behavior need a live import and short gameplay checks.

[Detailed local validation results](authoring/gameplay-expansion-2026-10-27/validation.json)

## Research informing the changes

[Prompt and behavior research](../research/Gameplay%20Expansion%20-%20Prompt%20Research%202026-10-27.md) distinguishes official Voyage announcements, community schema guidance, observed exports, and design choices. The new content is original Glowhaven draft material, not imported Luxcellia lore.
