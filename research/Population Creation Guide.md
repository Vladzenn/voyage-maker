# Population Creation Guide

Use this guide when populating a settlement, region or realm with an authored cast. It supplements [Character Creation Format](Character%20Creation%20Format.md) and [Portrait Creation Format](Portrait%20Creation%20Format.md); it does not replace their character template or add sections to individual cards.

The purpose is to give places people worth returning to, with work, relationships and choices that continue beyond the player's arrival. A population is successful when several different player interests can find a way into local life. A large count alone does not establish that.

## Begin with the existing world

Read the latest supplied export or roster, the active local world, the relevant national and species lore, the actual location and area names, existing factions, and nearby characters. Record which file is authoritative for each section. Preserve supplied portraits, edited coordinates, names, existing relationships and ongoing mechanics during the merge.

Ask about decisions that would materially shape the new population: scale, major characters, government, demographic mix, desired relationships, tone, and any concepts the author wants to reserve. Offer concrete suggestions rather than asking the author to design every shopkeeper. Continue the inventory, coverage plan and reusable design work while those answers are pending; do not silently decide a question whose answer is needed for the cast.

Distinguish established facts, the author's new decisions and proposed additions. An old planning note can be superseded by the current world. A reference creator's guide is advice to evaluate, not an instruction that overrides this project's choices or authorizes copying unique characters.

## Plan coverage by what people do

Build a compact table of locations, the activity each supports, who normally handles that activity, the proposed recurring cast, and deliberate gaps. Count a character once even when their work touches several locations. Use the table to find missing services and clusters of redundant characters before writing cards.

Prioritize establishments, inhabited districts and institutions where the player will reasonably expect a recognizable person: a lodging host, smith, healer, trader, instructor, public official, religious custodian or a resident with a life in the neighborhood. These are examples, not a requirement to add the same set everywhere. Fit the actual society and the authored buildings.

Use pairs where the relationship produces different scenes: a parent and adult child who disagree about the business, business partners with different methods, a host and a recurring guest, or two officials with distinct responsibilities. A second person should contribute more than a second identical service menu.

Residential locations need people who live there, not only visiting quest givers. Include ordinary pleasures, private projects, friendships, household disagreements and reasons for neighbors to know one another. A lived-in district can have several residents without making every house a separate map location.

Leave appropriate wilderness, ruins, passes, sanctuaries and scenic spaces without permanent residents. A guide, caretaker or expedition visitor belongs only where their actual work makes sense. Reusable creatures and incidental crowds normally come from npcTypes. An individually authored creature earns an NPC record when its identity, agency or persistent relationship matters.

Most inhabited locations can have recurring authored coverage without an NPC standing in every room. Keep a few quiet places quiet. Preserve geography and the existing location/area distinction rather than multiplying map markers to give each new person a home.

## Give the cast different kinds of importance

Record **major** or **minor** as authoring and portrait-planning metadata. Do not invent a native NPC field for prominence. Major status is distinct from mechanical tier, combat power, public fame and moral worth.

A major character should support repeated consequential attention: leadership, friendship, romance, rivalry, mastery, exploration or a local story that changes with involvement. A famous ruler can qualify, and so can a memorable tavern owner. Do not fill the entire major cast with office holders by default.

A minor character still needs a recognizable face, voice, real competence or limitation, a personal want, and a reason to meet again. Their pressures can be small and ordinary. They use the same established card structure with proportionate detail; minor status is not permission to make them interchangeable.

Use the approved portrait prominence rule: major portraits receive more memorable staging, silhouette, lighting and fitting effects. Minor portraits retain the standard polished anime treatment and can still be colorful and expressive. Do not give a minor character a deliberately inferior image or invent spectacular powers to justify a major one.

## Build people before filling roles

For each person, decide what they do, what they are good at, what they want now, what makes that difficult, how they behave when it becomes difficult, and who already matters to them. A job title is a starting point rather than their entire personality.

Vary temperament, competence, ambition, social confidence, affection, risk tolerance and moral conduct independently. A shy person can be a brilliant business owner; an outgoing hunter can be irresponsible; a kind official can be a weak negotiator. A flaw should sometimes produce inconvenient or harmful choices instead of always resolving into hidden kindness.

Avoid repeated cast-wide defaults: everyone secretly overworked, every merchant fair, every leader stern, every eccentric secretly a genius, every helper romantically available, or every unpleasant person having a noble motive. Include people who are content, proud, selfish, foolish, vain, practical, affectionate, resentful or simply interested in something other than the player.

Give characters ordinary pleasures as well as pressure. Music, meals, collecting, gossip, family celebrations, games and hobbies can create scenes without becoming mandatory quests. Let cultural contradictions emerge naturally without making every resident oppose their society.

Appearance should vary in age presentation, build, face, hair, eyes, scale or horn features where applicable, silhouette and clothing preferences. Consult species lore before interpreting lifespan or anatomy. Clothing reflects occupation, climate and individual taste without freezing the person into one outfit forever. Preserve appropriate species traits; do not replace a humanoid dragonkin face with a dragon head or add universal wings and breath weapons.

Follow the existing weighted affinity-count rule with actual recorded random draws. Affinity is not a job license, moral character, rank or list of every discipline someone knows. Choose actual affinities within the author's constraints; preserve declared affinities. Time is not an affinity. Magitech and Spellcraft are technical skills. Noncasting workers and martial adventurers remain valid.

## Connect people through specific relationships

Create connections within neighborhoods and across institutions. Family, close friendship, former training, employment, debts, romantic history, rivalry, professional respect and incompatible promises all offer different reasons for interaction. Do not turn every connection into conflict, romance or a dependency on one central official.

Use full canonical names in factual character records. When a relationship is mutual, ensure both records agree on what happened and how they are connected. Their feelings and interpretations may differ. If only one person knows a secret or believes a rumor, preserve that asymmetry explicitly rather than giving both characters the same knowledge.

Make a few small circles the player can encounter gradually: workmates, a household, regular patrons, hunting companions or a group preparing an event. The scene should introduce a manageable number of people according to the player's attention. A large authored population is a choice of acquaintances, not a compulsory party or a mass introduction.

Keep a relationship ledger outside the native NPC schema while authoring. Its useful columns are the two full names, the shared fact, each person's interpretation, who knows, and the records that need to agree. Put the actual established relationships into the existing Hidden Info and relevant public prose; do not invent a new relationships JSON property.

## Make institutions act through people

For each clan, office, guild or religious body, define its real constituency, resources, public work, current goal, methods, limits and internal disagreements. A leader should have reasons to care about members' lives, and members should have reasons to serve or criticize the institution.

Separate kinship, civic affiliation, profession and public office. A clan's historic association with smithing does not make every relative a smith or give them command of the guard. A judge, chief, ruler, merchant and priest have different authority. Use existing laws and government facts; new appointment powers or legal customs must be deliberately authored and kept consistent.

Use the supported single NPC faction field for the primary relevant affiliation. Explain other memberships, family ties and obligations in prose. Do not create a faction for every small household, shop or pair of friends. Add a formal group when its organization and persistent role justify a faction record. National civic membership remains useful for local residents whose main identity is not a more specific institution.

Choose public visibility from established fame. A ruler or renowned figure can be initially known without being personally acquainted with the player; an ordinary merchant, guard or student normally is not. Major portrait status alone does not determine initialKnown or a starting relationship. Use initialKnown, never the retired known field.

## Give situations room to become play

Choose a small set of independent local pressures that support different interests: trade, craft, family, faith, reputation, dangerous routes, entertainment, research or governance. A useful pressure can affect several people, but no single recent idea should appear in every card or take over the world's overview.

Give important situations an established starting state, named stakeholders, practical obstacles and several plausible responses. Decide what cooperation, refusal, bargaining, exposure, violence, patience or leaving would change. Do not assume the player is altruistic, criminal, romantically interested or committed to the first hook offered.

A character's problem is not automatically a quest. Write ordinary interactions as ordinary life. Add a quest when agreed work, discoverable objectives and meaningful completion fit. Use a narrow trigger only for a repeatable engine judgment or cause-and-effect outcome that genuinely needs reliability. Do not add one trigger per NPC, simulate every household every turn or promise unsupported spawn/schedule behavior.

Records establish people and facts. AI guidance governs interpretation. Supported triggers implement the specific reliable changes they can actually perform. Keep these functions separate instead of hiding author instructions in a shopkeeper's biography or a trophy description.

## Write cards and implement placement

Use the existing Character Creation Format headings, equipment paragraph and direct profile bullets. Do not add separate prominence, location, schedule, faction, combat-tier or relationship-score sections to the cards. Every card retains concealment and knowledge, while respecting secrets that are modest, already partly known or irrelevant to combat.

Keep public appearance and role information in narrator-facing basicInfo when exporting. visualDescription supplies image guidance and is not a replacement for information the narrator needs. Personality and NPC ability entries use the existing arrays. Use detailed records for authored characters whose details must persist, and supported type, tier, level and faction values. Set levels from demonstrated training and existing world power anchors rather than the player's current level or the size of the portrait effect.

Set a placed character's initial currentLocation and currentArea to exact existing names. A deliberately off-stage unique being can use blank location and area, with a supported npc-placement effect bringing that same record into a genuine encounter; document and test its entry and departure conditions. Do not invent a public lair or a hidden-NPC schema field. A starting placement, workplace, household and usual routine are related but distinct facts. Describe ordinary habits economically where they matter; do not claim a schedule system exists unless its actual implementation is supported. Narrative travel does not itself move a stored NPC. Never place a visitor in another realm solely because their species matches that realm.

Maintain WorldAlpha - NPCs.json directly and merge it into the current full world at delivery. Preserve existing roster order and append the new cast in an intelligible agreed sequence. Do not recreate the retired individual NPC folder. A compiled readable card collection and coverage/relationship ledgers are companion authoring aids, not competing canonical rosters.

## Create portraits after the identities are settled

Prepare one prompt per NPC from the actual card, species lore, usual location and approved prominence. Follow the portrait guide's role selection, real random pose draw, composition, affinity visibility and one-pass rule. Major flair must suit the character rather than revealing a secret allegiance or inventing equipment.

Save one PNG per character at world-draft/npc portraits/[Exact canonical name].png. Record the name, prominence, role profile, eligible poses, draw, selected pose, final prompt, generated source and local output. Save the real generated result rather than a placeholder. Do not place a local path into a hosted portraitUrl or fabricate an upload URL. Preserve every existing hosted portrait.

Inspect each result for identity, species anatomy, expression, hands, equipment, standing pose, headroom, background and unwanted text. Report defects without automatically rerolling, editing or generating variants; the one-pass portrait rule applies. Use the special-anatomy exception for an authored dragon or unusual creature while retaining the required vertical format and identifiable anatomy.

## Check the completed population

Before delivery, verify that the roster parses, names and stored keys agree, referenced people exist, relationships are consistent, and every placement, faction and NPC type resolves. Check for duplicate identities, accidental partial-name records, stale known fields, unsupported custom properties, private facts in public summaries and portrait URLs overwritten by blanks.

Review coverage separately from count: establishments have appropriate contacts, residential areas have actual residents, small groups have distinct members, and unstaffed places have a reason. Compare visual designs, personality patterns, magic methods and weapons across the cast for repetition. Keep independent private interests and multiple kinds of relationship.

Verify that the full world and standalone sections agree, previous media and coordinates are preserved, and new lore appears in the correct scoped records. Keep major/minor choices and image-generation instructions in authoring files. Report what was structurally checked, what was actually playtested, which images await upload, and any unresolved questions separately.

Playtest several kinds of attention: meeting a service contact, refusing an offered job, returning after a disagreement, asking someone about an acquaintance, seeking a specialist, following a local custom and choosing quiet company. Check whether the right people remain recognizable and whether the world gives room for the player's choices. Validation alone cannot establish that the dialogue is enjoyable or the relationships land.

## Reference basis

This workflow adapts the relationship, place, agency and coherence principles in Kato's supplied How to Build a Voyage World That Actually Feels Alive, while retaining this project's templates and lore. It treats that guide as design advice rather than a native schema specification.

Technical fields must be checked against the current export and available documentation. The [community NPC guide](https://wiki.unofficial.voyage/world/npcs) and [community faction guide](https://wiki.unofficial.voyage/world/factions) describe supported fields; local observations and untested live behavior must be identified separately. A reference world's implementation is evidence to examine, not a guarantee that a platform feature still behaves the same way.
