# Approved world and workflow decisions

These notes carry context between desktop and web chats. They supplement the actual JSON and creation guides; newer explicit user instructions take precedence.

## Steel and Spirits — follow-up decisions

The author names the release **Steel and Spirits**. Generate the remaining cast portraits; keep exact NPC filenames and upload/link them through the official API. The author separately authorizes one new pass for Sana Kuroiwa’s broken spear and Shōen Kagetsuna’s horns, missing magic and foreground people. A later explicit answer authorizes one covered-outfit replacement for Misao Shingū after API rejection. No other automatic extra pass. All 97 new NPCs end with hosted portraits.

Use the latest location-only export `43fe08da-66f0-451e-bf62-281d8f699479`, preserving all pins/regions/images. The author corrects Mirror-Reed from lake/ferry settlements to the pictured forested ridges and river. Rewrite seven local sites, four resident roles and two quests; update every reference, not only surface text. Normalize the capital guild to Adventurer's Guild - Benitsuru Branch. The author approves finishing the onsen placeholder and adding its proprietor/portrait; Hinoki Hollow Onsen and Atsuha Yunokawa bring the launch cast to 97. No location images now.

Plain selectable descriptions should replace literal Markdown asterisks. Every foreign start explicitly names its country/realm, and the Glowhaven adventurer start goes above the Akitsuhara openings. Characters beginning abroad can get a Glowhaven key locally through a genuinely authorized delegate, not only after a prior Evertree journey. Keep actual approval and existing fixed returns; do not force travel or introduce another hub.

Add optional veteran, former adventurer and criminal histories as a separate Past Experience category, plus more Drakenspire clan/community origins. Ordinary clan membership does not prescribe named kinship, a chiefship or current occupation. Physical Foundations adds +1 Force Combat/+1 Finesse Combat alongside its existing attribute bonuses. Do not silently change the public title of the whole world or begin another future expansion.

## 2 November 2026 — Akitsuhara implementation and live-playtest follow-ups

The author explicitly authorized the full country using Studio export `74c54aa4-8d7d-4ba4-927f-6cb52be23c1a`. Final names are Akitsuhara and capital Benitsuru. Keep all twelve supplied region images/crops/grid positions. Launch with 96 named characters, including adventurers, rōnin, foreigners and a bandit group; 14 major portraits first, other 82 pending. Only four named yōkai; ordinary creatures remain npcTypes. Additional people later means more households and independent stories, not omission of the approved social groups now.

The Spirit Realm is The Veiled Beyond, a small seven-location fog wilderness. Restored Way Bell comes from a modest accessible local shrine undertaking and permanently awakens Moonless Torii. Opening is separate from entering, later loss of the bell does not close the gate, and its fixed return remains local. The public transit torii is separate, uses delegated court permissions and returns to the Evertree. Preserve all existing Spider content and once-only anomaly behavior exactly. Hagire is the unique hostile, lanky, dislocating-limbed forest stalker. Local magic retains the global rules while emphasizing felt mana and softer flowing forms; clothing/palettes/lighting vary. Magitech is selective imported swords/crossbows/armor, no firearms. One extraordinary prototype belongs to Shigure Tsubakiri's concealed project.

Six local country starts plus Drakenspire and Asterveil researcher starts go immediately below academy student openings and above faculty work. New Origin & Upbringing choices cover local towns, rural/household/dojo/shrine communities and mountain/sky backgrounds; modest utility bonuses do not impose race, titles, property or named kinship. Add useful professions and categories. Physical Foundations should have a positive longer description. The author approves up to two optional Special Talents as a phantom change; omit that increased limit from public notes.

Starting 1018 marks came from the shared 18 plus each start's 1000; remove only the shared 18 and retain intentional money traits. Assessment examples must not produce real contracts. Fix the demonstrated overlapping guild acceptances narrowly: require the actual single displayed choice, retain old work/settlement owners, and reinforce the actual client/site/fee. Do not rewrite all quests or invent a state machine per conversation.

Ordinary new quests use native typed completion and one reward owner. Two developing arcs provide arms-politics and spirit exploration, with bounded alternative endings. Avoid adding always-active arcs solely to cover every local dispute. Official draft validation found area paths can only reference their own parent location; country roads are ordinary narrated travel described in the location text, with a connected authoring index, rather than unsupported cross-parent links. No new regional imprisonment controller, global schedule system or future expansion is implied.

The official API key is kept outside Git and logs, despite the user's willingness to commit it. Only generated assets, hosted URLs, exact receipts, reviewed code and project decisions are synchronized. Official `/validate` is a draft check; no Studio save/publication or live AI playtest is claimed.

## 2 November 2026 — Silver marks and map halves

Currency follow-up: retain the original financial/property safeguards verbatim; add focused currency wording rather than compressing those rules. A mistaken coin label never authorizes a 1:1 conversion: retain an established Mark price or state and agree the intended Mark price first. Do not add a blanket ban on conjuration/counterfeiting play to solve denomination drift. The Revised currency export supersedes the initial patch file.

The author requested a preventive currency phantom patch, not attribution of an anonymous report to this world. Silver marks are the sole common currency across the setting; mark/marks/silver marks are one unit backed by the existing `Mark` identity. Gold, silver, copper and platinum remain materials, colors or ranks, not new denominations. Keep barter, appraisal and agreed sales; no invented exchange table or duplicate purse. Preserve the latest Studio export and existing prices, funds and reward mechanics.

The author approved refining the two supplied map halves with the built-in generator. Use the full master and overlap for continuity, retain national scale, and improve architectural/terrain definition. Two production images still support the planned 4 × 3 regions. Their generated edges are not mechanically locked; inspect and align the join before treating it as a finished atlas.

## 2 November 2026 — Oni map production pilot

The author rejected the external 4K map's art treatment and close-scale composition. Use the built-in image generator for the replacement, with the actual Glowhaven map as style reference and the supplied national atlas as scale reference. A continuous country composition in the established art style takes priority over a resolution label. One 1447 × 1087 native master is saved for review; final 4:3 cropping, tile refinement and nation implementation are not approved by its existence. The author may slice the base and return a ZIP; later refinements should use original-map context and overlaps, and must be inspected at joins rather than assuming regeneration preserves exact borders. No automatic expansion to twelve generated tiles.

## World identity

Glowhaven is a mostly human, autonomous, magic-heavy city around the **Evertree**. Its four academies have nuanced civic duties, not one-word personality cultures. Morning classes are mandatory; students have varied lives outside them. All authored academy students are adults in a four-year program. Faculty are trained, capable adults even when lazy, unpleasant or weak by their peers' standards.

The Great Sage governs; Archons are exceptionally powerful representatives and Conclave members; headmasters run their schools. Preserve canonical office holders and full names. Existing nations, realms and maps constrain generation. Ordinary new household rooms can be areas inside existing locations.

Drakenspire is a snowy dragonkin-majority alpine city with a higher fortress, sacred dragon skeleton and clan-based elective Jarl. It is allied with Glowhaven. Dragon worship and ancestors matter. Rovakthuun is the elusive gray lightning dragon; Orrum is an isolated named yeti, not a generic repeatable type.

Asterveil is predominantly wilderness with four regional biomes, a small fae settlement and expedition work. It remains midgame. Fae appearances vary broadly; most dragonkin are humanoid with human faces, horns, slit pupils, scales and thick tails.

## Magic and combat

All disciplines can be learned; affinity eases learning rather than restricting it. Affinity and starting studies are separate creation choices. One affinity is most common (65%), two 25%, three 10% for generated characters unless explicitly directed otherwise.

Logic: Arcane, Metal, Gravity, Enchantment, Space. Passion: Fire, Lightning, Earth, Wind, Water. Empathy: Healing, Nature, Light, Summoning, Soul. Intuition: Divination, Void, Illusion, Ice, Sound. Force and Finesse support physical delivery. No separate Endurance attribute. Magitech includes the former Artifice scope.

Spell invention requires Spellcraft; ordinary casting uses the discipline. Simple invention can be a quick experiment; difficult spells require research. Time is configured but reserved, absent from affinity and normal creation. Space has a Gravity foundation and difficult private travel. Public court-issued portal keys are separate permissions. Light is not Healing; Nature heals plants; Soul includes spell-specific necromancy.

Ordinary physical attacks and routine defense remain useful without spending Stamina. Demanding techniques spend it. Bonuses, cooldowns and other mechanics must use supported fields. Temporary conjuration does not generate endless permanent crafting supplies.

## Fixed events and consequences

The Evertree base is the Glowhaven portal hub. Authorized court keys regulate outbound public travel. All cross-realm returns go there. The level-20+ anomaly is a once-only surprise crossing into the Spider Realm, independent of briefing/exam completion. Its boss, Vhalessra, and authored mechanics stay unchanged unless requested. The boss trophy can enable the Ryūka Marufuji bazaar confrontation. Those are events, not reasons to turn every normal quest into a trigger machine.

Crime and Prison is a narrow system: deliberate evil killing of nonhostiles or destruction of multiple buildings can lead to a wanted poster after three turns. Torture alone, theft, accidents, self-defense and hostile combat do not trigger this automatic loop. Poster possession controls enforcement; discarding it stops this loop by user choice. Arrest needs an actual outcome. Automatic custody is solo-only. Actual prisoners have the fifteen-turn release loop; lawful visitors do not. The prison is a separate realm; Wraith Island is a Glowhaven location.

## Character and art authoring

Use given name then family name, including Japanese-inspired names. Named references in factual NPC records use full canonical names to prevent duplicates. Nonhumanoids can have different naming conventions. Cards are native NPC JSON by default and use the established format. No pronoun profile field, no redundant Faction profile bullet, no Structured Profile heading; role in faction stays. Equipment is a Basic Info paragraph, weapons first only when present. Appearance includes hair and eye colors. Concealment and knowledge is consistently present.

Do not add phantom sections or engine-state notes to public character prose. Give people ordinary pleasures, real flaws, relationships and independent wants. Not everyone is a hidden genius or secretly kind. Romance, appreciation, work and party membership are different.

Portraits are colorful crisp 2D anime illustrations, default waist/hip up, no text, with appropriate setting backgrounds. Major characters get suitable flair; minor characters retain polished art. Player portrait customization is flexible. Follow the actual portrait guide. Save PNGs under the exact NPC name. Existing uploaded media URLs are preserved during merges.

Reference cast: Ragnar Leonhart is the adapted gravity veteran, level 67, with his horse only in lore. Adoha Aonuma carries a magitech voice amplifier. Karia Morino's revised portrait is the less literal adaptation. Preserve the user's latest voices; descriptive voiceTag text may fall back to a stock voice and must not be called a verified celebrity voice.

## Guild, quests and public prose

International guild with a court-permitted Glowhaven branch. Bronze, Silver, Gold, Platinum; examination for licensure, genuine assessments for promotion. Posted rewards are paid in full. The guild's commission is background economics, not an extra deduction. Rank is not level, automatic enrollment, recruitment or portal permission.

Use native completion for simple ordinary quests; explicit stages only where evidence, permissions or real choices need them. One completion owner and one reward owner. Existing offer flags may have dynamic writers in gh_guild_board; test those rather than declaring them missing from a text search. First thesis is once per playthrough, not repeated paperwork.

Inventory descriptions, locations and dialogue must read naturally. Technical flags, save instructions, authored/generation notes and hidden conditions belong in internal fields and development notes. Short public patch notes are copyable Markdown and describe player benefits; do not expose Easter-egg conditions.

## Adventurers of Glowhaven — approved implementation

The sixteen-person cast, three native arcs, additional finite work and all sixteen portraits are implemented. Snow-spirit conflict permits force or negotiation. The Hydra Head researcher is an adult fourth-year, talented in research and weak in combat; the Stillwind Pearl exists but does not validate her original theory. Copper Laurels are comic opportunists, not compulsory lethal enemies. The two adventuring companies are factions, not automatic player-party membership.

Use the revised power anchors: academy faculty and headmasters generally 28–32, Archons 50–55, court elites 40–45 and Karia Morino 42. **Ilyra Stillglass remains level 100 and Ragnar Leonhart 67**, explicitly exempted by the user. Legendary creatures, Orrum and the Spider Realm are not subject to this ordinary cast rebalance. Level bands do not make every trained adult a famous prodigy.

Rentals and modest purchases should leave natural keys/deeds in actual inventory. Six fixed arrangements have native payment/key grants; arbitrary household keys still require supported item generation. No automatic offscreen rent deductions, eviction clock or passive income is implied. Losing a key does not erase legal ownership.

Public leads reveal circumstances rather than accepting quests or exposing secrets. Returning clients can acknowledge an actual outcome without becoming repeatable reward sources. Native arcs remain distinct from simple authored quests and exact event triggers; do not fabricate authored quest arcId fields.

The user approved an honor-based `quest done: Exact Quest Name` repair action for an accepted journal quest that fails recognition. It may settle ordinary rewards without independent proof. It is OOC, exact-name based and not NPC dialogue.

Ironman is optional and solo. The main world's native death flag remains false for ordinary modes; Ironman's instructions and an ending trigger reinforce final lethal outcomes. For native permanent death use the separate full-world Solo Ironman export, where the global flag is true. Do not claim a game-mode record can override that flag, or that AI instructions are a guaranteed native toggle.

Touring routines move existing Ragnar Leonhart, Adoha Aonuma and Karia Morino through actual addresses and pause for presence, party travel, combat, incapacitation and real commitments. Adoha's Asterveil visits remain in the settlement. Personal travel authorization does not confer portal permissions on the player. Orivelle's existing circuit is preserved.

## Character creation minor patch — 1 November 2026

Player affinities are optional: zero to three. No affinity is a valid choice, distinct from a learned discipline. Physical Foundations supplies +1 Force and +1 Finesse among the starting-study choices. The existing weighted affinity-count rule for newly authored NPCs is unchanged.

Ancestry and optional temperament have actual modest attribute/skill/resource benefits without forcing behavior. Starting attribute ceiling is 20 so selected bonuses have room; normal attribute awards remain two points every three levels, as supplied by the user. Do not reinstate the rejected slower five-level proposal or infer a newly approved normal spending ceiling.

Special Talent is optional with one choice. The user approved stronger gifts having trade-offs. Their actual modifiers, vulnerabilities and granted techniques own effects; they do not grant unlisted affinities, automatic success, unlimited recovery, chosen-god status or Space/Time access. Added cosmetic outfit/accessory/portrait choices do not grant equipment or stats. Waist/hip-up remains the default, with explicitly selected alternate player framing respected.

The accompanying instruction sets starting/base maximum Stamina to 100; the export's 80% rest fraction is preserved. Marika Hoshino stays at the user's level 30. No blanket NPC nerf was authorized for this patch. Ordinary working adventurer generation is generally 20–30; authored exceptional people retain their actual levels.

Preserve all supplied hosted images, voices, coordinates and music. The user removed non-badge item artwork; do not restore it from older exports. Artwork backfill for existing catalogue items remains unverified. The ambiguous needsMediaGeneration toggle is not permission to bulk-enable it.

The public announcement must not disclose this release's Stamina adjustment, alternate framing/camera additions, Default grouping or emoji compatibility work. Those belong in private development notes. Mention Bald, broader creation choices, talents, equipment and minor balance changes as requested.

Studio's 1 November rejection confirms that ability trait requirements still require a numeric `amount`, even though the engine ignores that value for a trait check. Author `amount: 1`. Estimated item prices must be nonnegative whole numbers inside their configured tier range. Portable validation and regression tests now enforce these constraints; do not lower tier boundaries to accommodate an incorrectly priced item.

Minor patch titles use a randomly chosen, unrelated animal emoji plus `Minor Patch n`. No descriptive subtitle in the title; thematic headings may appear in the body. The latest published minor release is **🐙 Minor Patch 3**, so the next new minor release is **Minor Patch 4**. An import hotfix to the same release is not automatically a new numbered patch.

## Champions of the Crucible — planning decisions, 1 November 2026

Plan before implementation. First format: individual championship bouts, regulated nonlethal even in Permadeath, full Health/Mana/Stamina treatment between bouts, finite summons allowed, no outside interference. Leaving the venue withdraws the entrant from that edition. About thirty-two new named fighters. A hundred completed game turns between editions replaces the proposed narrated-day cooldown. Opponent selection should preserve existing NPC levels rather than resize the cast.

New Nature/Soul plant-undead dungeon targets approximately levels 35–50. Its discovery uses the actual Evertree Portal Room plus a championship trophy and Silver Web Portal Key; no spider-queen victory was requested. Preserve the existing Spider Realm and anomaly behavior. The Sepulchral Conservatory premise and named caretaker remain creative proposals.

Oni lore direction: predominantly Edo-inspired countryside/towns, samurai, shinobi, independent factions, Shogun and yokai, with some more-developed Arcane/Soul magitech. No modern metropolis or carved-face mountain. This update prepares lore and modest ancestry details, not the Oni map/realm or spirit portal expansion. The detailed plan separates supported mechanics, observed reference configuration and live-test uncertainties.

## Champions of the Crucible — implementation decisions

The user authorized the full package in one release. Use a persistent opt-in world activity rather than a native character-creation Game Mode. First controlled championships and exhibitions support one human; NPC companions remain outside combat. Do not silently enroll a multiplayer party. A changed human roster pauses review; prize ownership keeps the registered human name.

Latest medical steering supersedes the stricter planning requirement: care/rest is appropriate and optional. Do not invent injuries when unharmed, confuse low Mana with wounds, or gate readiness on exact maximum resource values. Normal narrative/resource updates handle accepted player care; this is not a verified heal-to-max API. Results are recorded before treatment, and later recovery cannot turn a loss into victory.

Semantic action/story recognition handles actual commitments and sporting decisions. The bracket's stored state owns entrant selection, eliminations, current match, result, 100-tick break and one prize dispatch. There is no championship quest, invented spawn effect or per-bout native permadeath switch. Native knockout/medical timing and semantic recognition require Voyage testing. NPC-only brackets are abstract recorded results rather than fake offscreen combat.

The Sepulchral Conservatory has two tending wings in either order before its gated heart, a safe return refuge, optional investigation and finite creature-type encounter guidance. Both physical circuits must actually be settled; lost keepsake seals do not undo repairs. Threnvoss is the level-50 named caretaker. Actual defeat or genuine release shares one trophy owner. Portal discovery requires the championship trophy plus Silver Web Portal Key at Evertree, with no spider-queen-victory prerequisite and no change to the Spider Realm.

Public notes are a thematic major announcement. Forty-three one-pass portraits and four dungeon environments accompany the native JSON; no unavailable hosted URL is fabricated. Preserve artwork mismatches in the review manifest and obtain a new request before re-generating under the one-pass portrait rule. Sources and the original AGENTS.md remain unchanged.

The author clarified the announcement-length distinction: **minor patches are simple; major releases are more wordy and visually inviting**. Major notes should explain the playable experience through descriptive sections and useful detail, rather than using the same brief checklist as a minor patch. The guide now suggests roughly 400–700 words for a substantial major release, scaled to actual content. Preserve the existing rules against spoilers, internal machinery, padding and unverified claims. The Crucible announcement was expanded; no world mechanics changed in this follow-up.

The author also requested a little unlock information in the major notes. Include the Conservatory entrance requirement in natural terms: carry a Crucible championship trophy and Silver Web Portal Key to the Evertree Portal Room. This is an explicit exception to withholding that hidden condition; later dungeon discoveries remain unspoiled.

2 November public-copy refinement: the author's edited announcement favors a mysterious rumor over an explicit unlock checklist. Refer to a champion's prize and a key from a silken descent beneath the Evertree, without inventing a blessing or favor mechanic. Keep the expanded fighter-roster point and the Oni preparation for the next major update. Retain the author's removal of the closing solo/team-format paragraph from this announcement; this editorial choice does not change runtime capabilities or the mechanics guide.

2 November tournament review: the author requested comparison with Luxcellia and Chikara and questioned whether the system should be simpler, specifically allowing waiting on benches between one's bouts. The audit reproduces five real v1 failure cases and confirms internal venue movement can preserve the current entry. Hold the tournament for repair. The report proposes a smaller recorded player-bout card plus normal narrative interludes; this is a recommendation, not an approved/implemented rewrite. Keep prizes and actual results exact. Do not blindly copy Chikara's public result-token/all-player points triggers or represent Luxcellia's narrative quest templates as a proven native bracket engine. No gameplay changes were made during this research pass.

## 2 November — approved simpler implementation and final steering

The user approved implementing the card proposal with Studio export `eefdd39e-e77a-4b8e-b870-5216d4c9022a`. Preserve its map art, location images and coordinates. The controlled tournament now tracks only the entrant's two/three scheduled bouts and one prize owner. Other matches, conversations, spectating and recovery use normal narration. An actual start is mandatory for results; a pre-start unavailable opponent is substituted or the card cancelled. Double knockout eliminates both and creates care entitlement. No NPC-only bracket, review/replay loop or away/grace state remains.

The user then explicitly rejected overfitting to benches and reminded us of Latitude's AI limits. **Remove bench-specific parsing and movement decision trees. Voluntary withdrawal means an explicit decision to forfeit the entry; ordinary movement alone does not change status.** A started bout still has real surrender, knockout, ring-out and referee outcomes. This supersedes the earlier immediate venue-exit withdrawal proposal. Keep the narrative questions plain and the exact ledger small. No full-resource gate or fabricated injury.

The Conservatory gets a planning route guard plus position-only state backstop modeled on the existing Spider navigation approach; the protected Spider Realm itself is unchanged. Native map-click timing and nonlethal combat remain live-test obligations. Old unfinished v1 controller state is cancelled without an invented result, retaining earned uncollected prizes; importing Studio content is not a promise of existing-save migration.


## 2 November — restored bracket, individual cast and official portrait uploads

The author requested the bracket back after the second audit. Restore a small four/eight-entrant elimination bracket: player fights remain real started bouts; NPC-only matches have one stored abstract official result, with availability checked before resolution and a champion recorded after player elimination. Do not simulate every offscreen attack. Exact ledger state and semantic judgments have distinct jobs. Mere movement does not forfeit; no bench parsing, grace phase or replay loop returns.

The second audit reproduced two actual controller-2 behaviors: unrelated lounge incapacity could settle a bout, and a joining human cancelled the entry. The new observer requires both participants in the actual arena and latches a need for an official semantic ruling after an interruption. A second human suspends control without cancellation or ownership transfer; full multiplayer arena isolation is not claimed.

The author approved redoing all 43 update portraits, with flashier competitor effects, and wanted less uniformly good characters. Forty-two new-cast cards now have individual pressure responses, voices, flaws and secrets; a few are genuinely coercive, exploitative or cruel. Named ties are selective rather than compulsory roster pairs. Levels, affinities, weapons, addresses and identities stay unchanged. The latest 272-NPC export is the NPC merge base; its unrelated fields and images remain intact.

The author explicitly authorized official Creator API artwork uploads and provided the official Alpha documentation/host. Read the live contract and reviewed World Puppeteer source without executing/installing it. The API key is process-only, never a tracked file or log. Upload all 43 selected replacements, match exact canonical names and file hashes, apply only portraitUrl in the uploader, and return the full revised world. No Studio replacement or publication is authorized by this upload workflow. Existing valid portraits remain protected by default in future runs; replacement requires an explicit selection. Current location/map images remain unchanged.

The rental question was clarification, not an instruction to redesign housing. Six fixed offers retain typed keys/deeds. Other genuine acquisitions ask normal item generation for one address/owner/agreement-specific key or deed; narration alone is not proof of an inventory update.

## 2 November — complete selected area artwork

The author accepted the previous close-up portrait review and requested no NPC changes. Use supplied locations section `1b1202c9-464e-4af9-aabf-660ccd145fa2` as the artwork merge base; it matches the current canonical locations. Complete images for every area in the four academies and Adventurer’s Guild, plus the Evertree Portal Room. This does not authorize full-area artwork across every location.

Preserve the twenty existing area shots and crops. Reuse four inspected, previously generated academy entrance PNGs; generate the remaining twenty-eight distinct environments under the existing location-art guide. The author also authorized reuploading the three recent Conservatory location PNGs. Use exact nested area addresses and the official `AREA_IMAGE`/`LOCATION_IMAGE` upload targets. Keep credentials process-only. Merge only returned shot URLs and required default crops for previously empty areas; retain all coordinates, maps, order, text and other world sections. Store prompts, per-file hashes, official receipts and a reviewable URL diff. Official draft validation is distinct from saving or publishing a Studio draft; neither latter action is part of this task.

The nine location preservation fingerprints were updated only after an exact image-only diff proof; all unrelated and protected Spider fingerprints remain unchanged. New original PNGs are shared through the repository's normal selective-media publication workflow.

## 2 November — supporting-card prose and progression-gate clarification

The author requested verification and repair of the reported supporting-card errors, using NPC section `b7f601cd-06d5-4fd8-b45f-165328ed6be2`. The ten malformed public descriptions and their ability grammar were confirmed; one additional dragonkin eye-description error affected Kanna Tsuruno. Make only prose corrections, retaining the full cast, portraits, statistics, equipment, affinities, personalities and concealed material. The rewrite source had used the life-description tuple entry where the occupation belonged; correct that source so future approved regeneration cannot recreate the defect. Do not rerun the full cast rewrite for this hotfix.

The author explicitly clarified that carrying the Crucible trophy and Silver Web Portal Key is a progression gate, not a literal ingredient combination, ritual or explanation of the Conservatory portal. Keep those actual trigger conditions unchanged. Put the narrative distinction only in the relevant discovery instruction; never expose progression checks in public lore or dialogue. The normal destination keys keep their established travel function. This clarification supersedes the earlier public rumor about pairing a champion's prize with a silken key to awaken the passage.

Because a world trigger's instruction changes as well as NPC prose, the author requested a complete updated world file. Preserve the latest academy/guild artwork and all other world content.

## 2 November — faster leveling instead of a general cast nerf

The author raised a small student/adventuring-adult nerf, then preferred changing leveling instead. Implement the playtester’s proposed native curve: 400 XP for the first character level-up, with 50 additional required XP per subsequent level. The previous values were 1,000 and 400. Leave all NPC levels unchanged, including every previously protected exception. Do not compound this change with more XP awards, altered skill progression, stronger level rewards or new leveling triggers. The level cap remains 150. Only the two native progression fields change.

The author also asked how Luxcellia handles long place names. The latest supplied export uses qualified area keys and local-context resolution; it is not a mandate that players type full addresses. Our movement instructions already resolve shortened area names within the current parent. This was comparison and advice, not authorization to migrate every location key. No place renames were made in this update.

## 2 November — finite beginner contracts and selective quest craft

The author approved adding early nuisance creatures and ready-to-browse guild work, then further sets at levels 7 and 15. Keep the opening and licensure rather than replacing them. Add nineteen ordinary finite native quests and eighteen types; only six existing introductory briefs and the contradictory juvenile-boar notice are revised. Keep all their checks, objectives, effects and settlement owners. No catalogue-wide rewrite, extra acceptance flags, forced twists or new cast nerf. A few jobs may have an interesting reveal; most can simply be satisfying work.

Use the existing board dispatcher for discovery and native acceptance/completion for new ordinary jobs. The first browse should include simple combat and a utility option. Preserve old offer-flag writers, legitimate repeat timing, actual badge permissions, lowest-human difficulty and warned deliberate harder requests. Type entries do not spawn anything or mechanically set individual level/damage. Generated creatures use modest creation profiles, finite encounters and meaningful practical alternatives. Native outcomes remain authoritative; actual low-level damage and semantic completion must be playtested. Add only a connected inn cellar, leaving map coordinates and all old images intact. The Spider Realm remains exact.

The latest author clarification says Champions of the Crucible is still unreleased. Bundle the new fieldwork and already-applied faster leveling into that major announcement, without creating a separate Minor Patch 4. Preserve the established major-update structure and keep the public additions about playable experiences, not trigger IDs, internal progression gates or implementation details.

## 2 November — private Glowhaven map refresh

The author supplied the complete Glowhaven region record as a phantom map update. It matches the current record except its map URL. Merge that URL into the canonical world and current full deliveries; preserve all other content, coordinates, crop, visibility and level range. Record the exact change privately and refresh only the two active region preservation fingerprints with that proof. No public patch-note entry or additional map/placement changes.

The follow-up locations export `6cc3c948-f13a-43ef-999c-ba12853dc3b0` authorizes the author's map-placement adjustments: 49 x/y changes across 33 Glowhaven locations. No other record differs. Merge only those positions, preserving the latest region map, all artwork, areas, paths, content and other realms. Refresh only the affected active location fingerprints with the exact coordinate proof. This remains a private phantom change; do not add it to the public Crucible announcement.


## 2 November — wider Earth lorebook proposal, not implementation

The author requested a complete Markdown handoff for a future lorebook-only minor patch. [Lore Update Proposal — Wider Earth](../world-draft/Lore%20Update%20Proposal%20-%20Wider%20Earth.md) contains confirmed decisions, a private author account, draft entries and reconciliation notes. No canonical world or section JSON changes are authorized by this drafting task.

Earth has real-Earth scale and ordinary astronomy/physics alongside magic, with different continents. Glowhaven is a major magical center with foreign competitors. **The four founders made Glowhaven; it has cut off and no longer answers to Ardelis or its royalty.** This supersedes current lore's subordinate wider-kingdom framing, which remains in JSON until implementation. Permanent portals require enormous expense and power. Glowhaven's mages established distant endpoints using the Evertree's exceptional capacity; Drakenspire's endpoint does not establish independent portal-making technology.

The primordial origin is private author/narrator knowledge. A primordial sacrificed himself out of curiosity to produce life; lingering primordial power is mana. **No being in this world knows the primordial beginnings**, including celestials and worshipped beings. The author clarified that the account may be included in the lorebook as explicitly labeled author/narrator-only background. It must never be known, revealed or discoverable through NPCs, books, research, histories, records or any other in-game source, including direct narrator disclosure during play. This supersedes the earlier instruction to exclude it from runtime lore entirely. Gods are powerful beings with varied worship. Ardelis introduces a celestial deity's religion; the separately suggested celestial nation is deferred. The patron's identity remains open.

Accepted national concepts are Valcéranne (elven kingdom), Dunbrae (dwarven maritime commonwealth) and Yunhai (populated by various beastfolk), alongside Ardelis. Detailed prose is draft development. Elves live about 1,000 years, physically mature at roughly the human rate, retain a youthful adult appearance and show age principally through changing mana. Exact social-adulthood wording needs clarification before assigning a threshold. Ilyra's 254-year reign is not a fixed total age. Dwarven speech uses the recognizable Scottish accent with selected Scots expressions; no Gaelic translation convention or voice replacement was selected.

No new playable peoples were approved. Hell remains deferred. The Evertree's founding and Asterveil ruins remain mysterious. The Spider Realm and later Oni destination expansion remain untouched. Public patch copy inside the handoff is a future draft, not a release announcement.

## 2 November — Wider Earth lore implementation approved

The author now explicitly requests implementation of the handoff using full Studio export `1d3eed47-6a6c-4042-9335-98614aba6de8`. This supersedes the proposal-only scope above. Adopt the approved national/cultural prose, merge overlap with existing lore and reconcile Glowhaven's independence from Ardelis. Keep the origin account explicitly author/narrator-only and undiscoverable through every in-game source; this is text-level guidance, not a native hidden-record guarantee. No new maps, destinations, systems, NPC cards, traits, voices or racial bonuses. Preserve all non-lore fields from the incoming export, including its 400 starting XP requirement and 60-per-level increment. Do not invent an elven social-adulthood threshold, deity identity, separation date/war, borders, capitals, Hell or an Oni portal route. Keep protected mysteries and Spider content exact.

Bundle the lore into the unreleased Crucible update. The author wants only the public line **“Lore expanded.”**, rather than the proposal's longer public draft. The complete export, canonical world, section files and current revised/fieldwork full downloads are refreshed; exact preservation and manual checks are recorded in the implementation review.

## 2 November — Portal to the Oni Nation planning

The author supplied a planning-only handoff and superseded its vertical/square map suggestion with **four columns and three rows**, horizontal. Ignore its spurious older-date reference. This is a geographically continuous mainland, forested along all four map edges, with no visible coastline. One substantial capital and two smaller castle towns; most land remains countryside/wilderness. The capital's terraced Shogunal castle is backed by a sacred mountain. Include bamboo, shrines, grain/susuki fields and a ronin landscape without copying another game's actual country, settlements or invasion plot.

The author confirmed two separate gates: the main-city torii is the authorized Glowhaven/Evertree network endpoint; a distinct earned-item Soul Torii leads to spirit wilderness. Add an international Adventurer's Guild branch to the capital, using the actual existing badge/permission/reward rules. The author also confirmed beginner routes/jobs at levels 1–5, with optional danger increasing toward about 55. Preserve the existing one-time anomaly and exact network return to Evertree Base - Portal Room; the spirit gate has its own local return anchor.

The handoff sets capable central authority versus semi-independent clans under fragile real peace, restrained Arcane/Soul magitech, substantial population, and five local openings: samurai, shinobi, ronin, shrine apprentice and flexible civilian. Additional guild arrival, final names, faction names, population counts and permanent gate-opening behavior remain proposals. New plans supersede the old small two-region/14–18-person sketch; historical blueprint files remain context, not rebuild authority.

The planning deliverable proposes a continuous master map and deterministic square slices, not independent tile generation. Official API upload facts were checked; no live Studio atlas import or native generation-size promise is claimed. A 5016×3762 master with twelve 1254-square tiles is an export choice, not a required Voyage resolution. Current world JSON, media and all mechanics remain untouched. No assets or implementation before overall direction approval. No public patch announcement is created for this planning pass.


## 2 November — Oni checklist and revised magic presentation

The author requests a fuller implementation checklist before starting the Oni expansion, plus one regional portrait example. Preserve planning-only scope. The new Kato reference is structurally identical to the earlier supplied export; inspect useful movement/local-guild/hunting patterns without claiming unseen newer fixes or importing foreign lore/controllers.

After seeing the sample, the author rejects different overall regional rendering, fixed warm lighting and a limited clothing palette. Keep our established portrait style and varied, often bright Japanese-inspired garments. The intended regional tendency is softer flowing magic: translucent tapered forms, graceful motion and fewer hard glitter/crystalline highlights when the actual discipline permits. This is not weaker magic or a ban on spectacular combat effects. No extra global portrait instructions are added.

For later lore implementation, local magical teaching emphasizes feeling mana, breathing, movement and practiced forms; scholarship and all existing mechanical approaches remain. Magitech is newly imported by some clans, not everyday national infrastructure. Magitech crossbows, swords and armor fill the disruptive imported-arms role; there are no guns/firearms. One extraordinary real prototype weapon concealed by a major antagonist is reserved from the supplied design reference; its owner and workings remain undecided. The Blue Eye Samurai analogy concerns political leverage, not imported plot or historical claims.

Save the single unnamed adult Oni innkeeper/Wind sample and its provenance without adding an NPC or hosted URL. Its headroom remains tighter than the production target; no automatic reroll. Canonical JSON, runtime lore, global guides and other realms remain unchanged. No public release notes or patch numbering for this planning task.
