# Ardelis capital implementation

This record describes the 5 November capital expansion, built from the author-approved Rebirth world (`eda234f`, file SHA-256 `77d47b4384db822c6021fb5c9ef29bde3daabfb557bf948b62f2a3bd3ccf8b59`). The supplied Locations export adds eighteen unfinished pins and leaves all 307 existing locations unchanged. The author separately supplied twelve complete map-region records. The grid is four columns by three rows, not the earlier Glowhaven grid or a guessed subdivision of the original PNG.

**Delivery status:** the current follow-up installs all 116 selected portrait URLs, preserves 84 location and two area images, and merges the author’s latest complete map sections. Exact files, names, targets and URLs are checked in `tools/ardelis-followup/art-verification.json`. Validation results and the completion status are recorded in CURRENT_STATE. This is an import package; it does not save or publish the Studio world.

## 5 November follow-up — current delivery

Build on current Ardelis commit `1b42222`, not the earlier Rebirth export. `tools/ardelis-followup/review.json` is a reversible delta and historical fixtures reconstruct their original revisions without relaxing old assertions. Do not rerun the old builder or one-time migration against the current file.

**Names and history:** 108 Ardelis character names and four associated family forms are migrated throughout native references. Shared human names reflect the former settlement’s heritage; western fantasy court dress and architecture remain. Noelle Ashford and five established Elven names stay unchanged. Glowhaven’s founders led independence after heavy imperial taxes and coerced mage war service; the empire formally recognizes the new nation while the crown retains an agenda. No founding date, battle roster or historical ruler is invented.

**Focused progression repairs:** a genuinely resolved peaceful delegation can advance directly from phase 1 to 3 without forcing Vladimir into the scene. Genuine ongoing questioning and Shiba’s death retain separate paths. Carrier and audience leads now initialize only while the exact native quest is planned. Available, accepted, completed, rejected, abandoned and expired quests are not reinitialized. Existing XP and rewards remain owned by their original undertaking.

**Recurring pursuit:** the actual player with both the Summoned one origin and corroborated trace is the bearer. After the initial interception or established phase-5 investigation, a suitable public scene may host a finite retrieval attempt. The controller requires at least 100 completed game ticks after the previous actual resolution, defers combat and protected/private venues, and never stacks an active attempt. Stronger spectators do not raise the bearer’s level band. One lead uses target level ±2 capped at 45; from the third attempt at most one weaker support may join, capped at 35. Desperation changes tactics rather than endlessly adding bodies.

Native semantic conditions judge genuine scene suitability and an actual ended encounter; scripts own bearer identity, interval, team bounds and end flags. NPC generation still creates the requested new instances: their final stats and live scheduling need a Voyage test. Capture remains real captivity; the cooldown is not release or healing. The receiving-operation conclusion stops new teams without erasing current danger. Runtime lore contains setting facts; numeric implementation notes stay here and in the controllers.

**Portrait selection:** supporting pose draws are recorded once. Jōji’s original was restored after an erroneous selection for replacement. The selected new passes are Maiko’s pose, Akito after rejection, Edmée’s angled pose, Kaede’s intact rapier and Rumi after rejection. Each has explicit author authorization and previous-selection provenance. Kaede’s later screenshot clarified the already selected replacement and did not authorize or produce another generation. Noelle’s previously approved choice remains. Some outputs have tighter headroom or prop encroachment than the guide, and repeated city-arch backgrounds; no automatic rerolls or quality claims conceal those limits.

**Audit scope:** the Gemini DOCX was reviewed, with reproducible observations and unsupported claims separated in `research/Gemini Audit Review - 2026-11-05.md`. The author chose findings first. No scroll, guild-board, equipment-slot, opening-placement, encounter-guidance or travel-toggle repair from that audit is included. `audit_snapshot.cjs` is diagnostic only.

**Verification:** `test_ardelis_followup.cjs` covers the incoming section hashes, name/reference migration, preserved Spider content and party diadem, peaceful transition, guarded offers, same-bearer selection, 100-turn pacing, scene guards, count/caps and concluded-operation stop. These are static and isolated emitted-script tests; they do not prove live semantic judgment, generated stats or multiplayer scheduling. Playtest peaceful departure, optional investigation order, actual pursuit escape/capture, a mixed party and final stop before release.

## Scope and geography

Caelrath is the capital of the **Empire of Ardelis**. The titles King and Queen remain as requested. The city sits on connected mountain terraces above coastal water: reservoirs and channels descend through the city to deep lower harbors. It is not a floating city. Other imperial cities and provinces exist in lore but are not added as playable destinations. The abandoned Glowhaven port-town proposal is excluded.

The later complete Locations and Regions exports supersede the initial provisional pins. All 391 locations and 55 regions match those normalized incoming sections exactly. The Ardelis grid remains four by three. All 84 Ardelis positions are now author-corrected; `tools/ardelis-followup/placements.json` and its CSV record their current values. The original placement ledger remains historical. Existing locations, artwork, maps, music, voices, progression, resources and Spider content remain exact, apart from the specifically reviewed Evertree portal-room description. Existing story starts retain their relative order.

The capital has 84 sites and connected areas, 115 new named NPC cards, 64 native quests including the local licensure quest, 24 concise items, 20 learned techniques and 27 new type definitions. The extra luxury arcade, concert hall, sewer site and four residents follow the author's later request. All 115 new Ardelis NPCs now have selected, officially uploaded portraits, including the three major paladins. Vladimir retains his approved replacement. There are 116 selected portraits in the complete archive.

## People and institutions

Kenzō Shirogane is an aging ambitious king. Reiko is a cruel political operator with separate adult affairs. Their three adult daughters—Ayame, Yurika and Mio—have military, artistic and scholarly interests. Minazuki, Takamine, Kagetsu and Orselle households have distinct economic influence and internal disagreements. Adult affairs are not blanket consent or an exemption from the existing betrayal consequences.

The church honors Astraeon, the High Star. Masafumi's public church, the Starward paladins, Shūgo's household guard and the Unveiled Star cult are distinct. Akihiro, Serika and Osamu are named major paladins with different knowledge and culpability. The Glass Knives pursue their own criminal interests rather than secretly controlling every problem. Ordinary paladins, courtiers, artisans, bards, performers and workers have type definitions for additional suitable encounters. Named characters have actual workplaces and partial knowledge; none is an omniscient tour guide.

All principal and supporting cards use native fields. Weighted affinity counts were drawn independently and saved once (65% one, 25% two, 10% three). Noelle and the experimental construct have authored exceptions. Affinity is not automatic mastery. Existing Ilyra, Ragnar, Orrum and all previous cast levels remain unchanged.

## Portal behavior

1. The party reaches the actual Evertree Portal Room.
2. Limited bilateral sponsorship is authenticated. Reika's court route can verify Harunobu's genuine correspondence **without requiring prior entry into Ardelis**. Vladimir is an optional alternative, arranging his own meeting rather than joining the party.
3. An authorized delegate actually hands the named traveler their reusable Ardelis Portal Key. A shared authorization flag alone does not issue a key to a different person: the player-scoped native semantic handover checks that recipient. The optional writ records the specific real sponsorship.
4. Committing to cross uses the same native destination-key conditions, exact location effects, companion placement and shared `ghPortalTransitTick` lock as the existing routes.
5. The preexisting once-only level-20 anomaly behavior is retained in the new route. No old Spider or portal trigger is edited. Its intended destination is recorded as Ardelis when applicable.
6. Normal arrival ends at **Caelrath Portal Hall — Portal Room**. The only fixed return ends at **Evertree Base — Portal Room**. Return does not require a key, exact source sub-area or a particular spoken key-use formula. One action does not cross back automatically.

Vladimir leaves independently after the actual completed meeting; his home content remains available. The new local starts grant neither international permission nor a guild badge. A route key does not grant palace access or legal immunity. The native action queries accept natural committed speech; raw script text matching is not presented as semantic interpretation.

## Quests, discovery and budget

Ordinary jobs use native typed `completionCondition` objects, native objective maps and `onCompleteEffects`. There is one configured reward owner. A short repair or delivery need not have a twist. Other undertakings offer disputes over wages, ownership, water, patronage, evidence or loyalty. Queued stories can conclude through performed settlements, supported reports, refusal or concrete alternatives when their agreed scope allows it; acceptance or invented offscreen work never suffices.

New quests begin `planned`. A relevant deliberate inquiry offers one undertaking through `quest-init`; it does not accept it. Linked chapters are offered by their predecessor's completion. Old saves that completed the Glowhaven relay chapter can receive the same next lead without replaying the old reward. Suggestions in new starts stay optional.

The Caelrath guild uses **one** semantic request check for its live board, not thirteen simultaneous contract checks. Its script selects a genuinely rank-eligible planned contract near the weakest human party member's level. A specific eligible title is a deliberate choice; harder-work wording permits a broader selection. The offer remains visible and rejectable. A generic exam sample is never a live contract. Existing badges and actual partial pass records remain usable; the canonical Bronze Document badge is the sole certification award. No duplicate Relic, fee, free weapon or portal key is added.

One new native developing arc covers civic water and supply conflicts. It may develop consequences beyond the configured jobs but must not create duplicate versions of those jobs or pay them twice. The existing regression scene budget includes the additional arc-surfacing check; the current worst historical example reaches the documented budget rather than being described as verified spare capacity. Exact new-scene live scheduling still needs testing.

## Rebirth continuation

The old local chapter still concludes; it now offers a permission route toward the receiving address. The Ardelis investigation verifies a patient transfer, meets or obtains direct evidence about Noelle, understands her command link, resolves the actual deployment and disposes of corroborated evidence. Vladimir's invitation is not compulsory. Noelle is an adult woman summoned from a nonmagical alternate Earth, with twenty public affinities and finite learned hand-cast techniques. She has no weapon, staff or wand. Her command restraint does not erase her entire personality; a genuine circuit or protective intervention is needed, rather than a flattering sentence.

The conclusion can expose or compromise the operation without automatically overthrowing the empire, ending every war or recruiting the rescued person. The court, households and civic capital remain playable afterward. Glowhaven academy expeditions never assign Ardelis; the local institute has its own adult apprentices and observed demonstrations.

## Lower palace and sewers

The separate optional palace descent is:

`Service Stair → Receiving Cellar → Calibration Gallery → Cooling Vault → Warded Crossing → Resonance Cradle`

The assistant investigation can establish access without the Rebirth origin. A real cooling-feed and crossing solution opens the final approach. A planning guard handles explicit early jumps mechanically because Voyage rejects semantic planning conditions; a state-phase backstop corrects direct area entry. The native quest's semantic completion recognizes an actual feasible solution. These are complementary layers, not a claim that the script can understand every paraphrase. Earlier rooms and retreat remain available.

Thaurivex is one named level-45 experimental vessel, not a deity or repeatable type. Defeat or actual containment can resolve its danger. Its inert diadem has one separate recovery owner after real safe removal; quest rewards do not add another copy. A later visitor does not respawn the boss.

The Caelrath Sewers are a **different** connected maintenance site. Raised walks, sluices, an abandoned branch and a tide outlet give bounded level-7–18 work. Drinking-water conduits remain sealed and separate from foul-water channels. Ordinary rats, drain slimes or occasional smugglers can occur in suitable disused sections; maintained streets do not become monster zones, and the sewer is not a free palace shortcut.

## Artwork and upload provenance

Use the project's normal fantasy-anime portrait rendering. Principal profiles and randomly selected compatible poses are saved with each prompt. Noelle's later direct author requests override the original all-affinities display and random pose: her final selected image has empty lowered hands, camera gaze and an angled stance. Three explicitly requested revisions are recorded; they are not automatic rerolls. Vladimir's replacement follows the later brown-hair/brown-eye, oversized-hat and ornate-glass-staff direction, preserving immortality and psychic immunity. The previous rejected Vladimir image is retained locally.

One square establishing image is prepared per new location, plus the portal-room and empty Resonance Cradle area views. The visual identity follows the supplied map, while each establishment gets functional props and its own palette. No permanent boss or named foreground actor is baked into location art. Tall/wide crop safety is prompted but requires Studio preview; portrait headroom is sometimes tighter than the guide target and no unauthorized rerolls are made.

`portrait-files.json` and `location-files.json` bind canonical names to byte hashes. The reviewed official upload flow requests an allowance, sends bytes without the Creator bearer to the signed storage URL, then moderates the exact target. Public receipts contain final URLs and hashes, never the credential or signed direct-upload URL. Retries resume by target/name/hash. They do not re-request an exact image rejected by moderation. `upload_art.py` never saves or publishes Studio.

## Verification and limits

The content candidate passed the official draft validator after fixing the native `average` tier enum and the planning-phase semantic restriction. The final receipt records the exact final check. This is not a Studio save, crop preview or gameplay test.

`test_ardelis.cjs` executes emitted portal/board/guard scripts with supplied semantic answers, verifies single recovery, rejects same-turn bounce and confirms exact preexisting content and map pins. Historical fixtures reconstruct the exact reviewed Rebirth revision through the reversible manifest; their original fingerprints are not relaxed. All prior behavior suites continue to run. Neither a fixture nor draft validation proves live AI understanding, combat timing or multiplayer behavior.

Before release, playtest: each new start; basic licensing without quest spam; first rat job and its single payment; separate rank/level board choices; both permission routes; a recipient with no permission; keyless return phrased “I use the return portal”; a level-20 first transit; mixed-player travel; non-Rebirth Ardelis visitors; each evidence alternative; Noelle escape/control/defeat outcomes; a credible lower-ward technical solution; early map-click cradle entry; retreat and revisit after the boss; safe sewer work; housing keys and actual rental payment; portrait crop previews and all uploaded URL/name pairs.
