# Glowhaven Expanded — implementation and review

The full supplied Studio export `2b7db2b6-97a4-4028-94ed-bc2695877ee2` owns the map, coordinates, existing content and media. This update finishes its twenty Glowhaven tiles and fourteen placeholder locations. The existing count of 299 locations stays 299: placeholders are developed rather than duplicated. The complete cast is 397, including 28 new NPCs. No location-art batch is included.

## Map and preservation

The actual grid is five columns by four rows. Region x/y, map URLs and crops remain exact. Every supplied location x/y and existing location/area image remains exact. The author will fine-tune placement in Studio if needed; the implementation does not pretend to have inferred every building from pixels.

| Row, north to south | West → east |
| --- | --- |
| y 0 | Northwest District; Evertree District; Harbor District; Whitecrest Isles; Bluecoil Reach |
| y -1 | Southwest District; Artisan Quarter; Southeast District; Crescent Coast; Moonarch Shoals |
| y -2 | Westpine Forest; Pinewater Vale; Greenfield Farmlands; Seaward Bluffs; Greenrush Marshes |
| y -3 | Southglade Woods; Longgrass Meadows; Sunmead Plain; Brookmeadow Downs; Brookmeadow Vale |

“Northeast district” becomes Northwest District as explicitly corrected by the author. Six locations had nonexistent parent regions: Brookmeadow, Glowhaven Farmlands, Shadowspire, Pinewater Woods, the windmill and old guardtower. Their parent keys are repaired while their local pins stay exact. Brookmeadow was present, not deleted; its invalid parent prevented correct map display.

The fourteen finished locations are The Gilded Albatross, Splinterwake Wreck, Moonarch Isle, Stillback Isle, Greenrush Estuary, Thistlebank Alchemy Cottage, Wrenhill Windmill, Old Southwatch, Bluecoil Rest, Beaconrest Lighthouse, Starlark Abbey, Gullwatch Reefs, Longgrass Crossroads and Seaward Overlook. Each has connected native areas. The overlook remains quiet and has no resident NPC.

The builder proves all 369 old NPC records exact, including their portraits and statistics. All old triggers except the existing guild board remain exact. All old realms, non-Glowhaven map records and the complete Spider content remain exact. No tournament, currency, level progression or portal rewrite is bundled here. Exact evidence is in `tools/glowhaven-expansion/merge-review.json` and the field diff beside it.

## Cast, lore and wildlife

Captain Reina Kazehara is a tall, muscular adult fae with large butterfly wings, long orange hair and a broad saber. Her generosity, noisy confidence and repair guarantee can pull against sound judgment. Mio Tatsunami is her eager young-adult dragonkin first mate; enthusiasm does not make her competent at every unfamiliar task. A cook, quartermaster, diver and boatswain give the vessel a working household beyond the two leads. They do not automatically join the player.

The remaining residents cover the abbey, lighthouse, mill, estuary, farms, alchemy, surveying and less honest trade. Named relationships are selective. People have interests, preferences, flaws and pressure responses beyond their commissions. Starlark Abbey follows one deity, Avelune, Lady of Returning Light; receiving ordinary care does not require conversion or prove any secret cosmological truth.

Sixteen new NPC types supply possible local wildlife and encounters. They are templates, not sixteen guaranteed spawns on arrival. Location habitat guidance distinguishes sheltered beginner work from exposed nests, flooded wrecks and optional boss approaches. Generated levels and finite groups still require live checking: prose guidance is not a native fixed spawn table or an automatic numerical cap on every generated enemy.

## Three special creatures

- **Nerathyl, level 45:** one animal-like serpent at Bluecoil Rest, initially asleep. Distant observation does not wake it by itself. Noise, injury or close interference can do so; it is not a talking dragon or an examination giver.
- **Mauruun, level 60:** one passive giant turtle at Stillback Isle. Shell irritation, practical care and an actual landing arrangement form a peaceful route. It is not automatically tamed, recruited or turned into a free mount. Provoking it remains dangerous.
- **Ghorvath, level 55:** one hostile kraken, initially at Splinterwake Wreck’s Deepwater Edge. One planning-phase schedule alternates between that deep approach and Moonarch Isle’s Offshore Drop at 24-tick slots. It cannot move while in the scene, combat or party. Zero Health or completed hunt sets a persistent defeat latch. The schedule does not restore Health, create another kraken or move it onto beginner landings.

### Sleeping and awake portraits

The current community schema documents `npcs.Nerathyl.portraits` as a map of names to hosted URLs, and `npc-portrait` accepts one of those names. Nerathyl has **Asleep** and **Awake**, with its original asleep image as the default `portraitUrl`.

Two small recurring state-phase triggers switch the portrait only when the living serpent is actually present at Bluecoil Rest and the latest scene establishes waking or real sleep. A single boolean prevents repeated switches. Intentions, warnings, a return visit, ordinary calming, unconsciousness and death are explicitly excluded from sleep recognition. The state does not force an attack or reset the animal on arrival. These are semantic recognition checks, so timing and classification remain live tests, even though the official draft validator accepts the fields.

The first awake image intersected the ledge. The author explicitly requested a replacement; the selected corrected image has water separating the body from the rock. The rejected draft is not linked or packaged. There is no dead variant in this update.

References: [NPC schema](https://wiki.unofficial.voyage/world/npcs), [portrait trigger effect](https://wiki.unofficial.voyage/mechanics/triggerDefinitions), [official live Creator contract](https://api-alpha.aidungeon.com/creator/v1/openapi.json).

## Quest ownership and discovery

There are 24 new rural/maritime quests and four new academy assignments. All use native detailed quests, typed semantic completion conditions and one completion/reward owner. None uses a separate objective-completion controller. A failed attempt can change the method without pretending the promised result occurred. Native completion distributes its configured reward once; narration must not add another purse. Guild jobs retain the full posted payout, plus one service credit, without deducting an extra commission.

Discovery is complete and bounded:

- Twelve licensed jobs extend the existing guild board. The old rank, weakest-human level, deliberate harder-request and offer-flag logic remains. Repeated client/place strings are shared to keep the trigger below its 10,000-character limit. Browsing offers at most two jobs and never accepts them.
- Eight initial personal commissions use one location-gated dispatcher. It considers only hidden local work at the destination or actual client’s home, checks the player’s meaningful request and exposes at most one quest. Greetings, rent discussions and arrival alone do not qualify. Completed personal work is not offered again.
- Four later stages are exposed by their predecessor’s native completion effects. They still need player acceptance; completion does not silently commit the player to further work.

The salvage dispute and turtle-care stories are **linked native questlines**, with their broader design notes retained in the merge review. A tested first draft added two global native arc surfacing checks. The conservative Crucible live-bout probe then rose from 15 to 17 eligible checks against a 15-check budget. The two new global arc definitions were removed; the linked quests retain the story progression. Existing five runtime arcs and all tournament rules are exact. This avoids changing unrelated systems to accommodate unnecessary background checks.

The original eleven guild offer-flag writers remain tested. No new unwritten acceptance flags are introduced. Personal-offer semantic checks are generated only within the new dispatcher’s local candidate set, not for every quest across the world. Actual recognition, rejection/reopening behavior and multiplayer reward distribution still require Voyage playtesting.

## Travel, equipment and starts

Boat passage, hired local boats and optional ownership use actual agreements, inventory and the existing item-generation rules. The ship’s crew may offer longer excursions or salvage work. No separate sailing simulation, rent timer or boat ownership controller is added. Thirty-two items include practical gear, tools, documents, unusual finds and trophies; catalogue presence is not automatic possession.

Two starts are added before Random: Aboard the Gilded Albatross and Starlark Abbey: A Light for the Road. Neither grants a ship, job, property, badge or recruited crew by implication. All prior start IDs remain, with the four academy openings and guild scene revised within the separately approved scope.

## Academy and portrait follow-up

Four first-day openings introduce five authored students each, including explicitly identified older helpers where appropriate. Their own work, arguments and friendships continue; they do not form a reaction panel around the protagonist. Lessons are required, afternoon preparation is regular with breaks, standing is qualitative, and clubs are optional. The first actual lesson exposes a practical assignment: protection at Phoenix Wing, evidence at Gryffin Tail, field judgment at Dragon Hoard, and negotiation at Hydra Head. An honest reviewed attempt can count without falsely declaring excellent performance.

The author explicitly retained Find Afternoon Work and Visit the Glowhaven Guild as **rumor/suggestion goals**. They are not accepted outside employment or a guild licence. The returning Karia/Renpei scene at the guild concerns their own already-finished work; the newcomer receives neither their reward nor a duplicate commission. Other foreign, faculty, merchant, village and summoned premises remain.

Player portrait prompting now favors fine anime drawing with softly layered illustrated shading, richer materials and expressive lighting. Optional portrait style, crop, angle and background choices remain. Four explicit academy uniforms supplement generic student/faculty choices, with actual school colors and pictorial crests. Cosmetics grant no affiliation. Physical Foundations restores Guarded Combat +1 alongside the existing four foundation bonuses, and a selectable self-taught past experience gives Spellcraft +1.

## Artwork and validation

All 28 new NPCs have distinct hosted portraits, plus Nerathyl’s second state: **29 selected PNGs**. Exact names, native dimensions and PNG hashes are recorded before official upload. Ordinary humanoids use the default profile; captain, first mate and creatures use special compositions. No old portrait URL is replaced. Original PNGs remain unresampled. Several figures have tighter headroom than the target, a captain hand near the saber can read awkwardly, and some everyday affinity effects are subtle. No unrequested retry was made to those images. The author-requested serpent correction is recorded separately.

All uploads use the official authorization → raw image PUT without the Creator key → moderation sequence. Credentials remain process-only and are absent from repository files, logs and receipts. No Studio world was saved or published. `official-draft-validation.json` records the exact full-world hash and official response; use that receipt, not an earlier candidate’s result.

Local structural, native-effect, board, preservation, creation, tournament, Oni and expansion fixtures are separate from actual gameplay. The expansion suite exercises both portrait transitions, no distant/dead transition, defeat-latched roaming, guarded movement, every personal offer, completed-work suppression and all preservation hashes.

## Manual Voyage checks

1. Import the complete JSON into the existing Alpha draft; check the 5×4 map, Brookmeadow, Shadowspire and repaired pins. Do not publish an intermediate file.
2. Meet each new NPC at the exact area, checking image/card identity and the three beasts’ single persistent records.
3. Observe sleeping Nerathyl from the mooring without waking it. Actually wake it and verify the awake portrait, then verify genuine resettling restores asleep. Return while it remains awake and confirm no reset. Check UI update timing; no live timing guarantee is claimed.
4. Visit a sheltered coast as a novice. Confirm routine jobs and wildlife stay modest, while serpent/kraken/wyvern dangers are warned and optional.
5. Ask a specific abbey, mill or crew contact about work. Receive one relevant offer, decline or accept naturally, complete by a practical alternative, and confirm exactly one reward. Follow each native chain and verify no automatic next-stage acceptance.
6. Seek the kraken deliberately, retreat, revisit and defeat it. Confirm scene/combat immobilizes scheduling, its trophy is granted by the actual hunt completion only, and the schedule never revives it.
7. Play each academy start: hear other students’ own exchanges, participate in the first lesson, receive the appropriate preparation task and get qualitative feedback. Test imperfect sincere work and a non-spell solution. Test optional guild/town leads without forced outside employment.
8. Try both new starts and school-specific uniforms, including a non-mage and a foreign background. Verify existing optional appearance choices still win when explicitly selected.
9. Test a two-human party accepting and completing one new job, including a participant joining/leaving. This update follows existing party-quest settlement and adds no new multiplayer contract system.

Generated encounter balance, semantic recognition, runtime portrait switching, NPC placement during narrated openings and image crop behavior are the principal remaining live uncertainties.
