# Glowhaven World Overhaul Implementation Handoff

Prepared 5 November 2026 for the author and the next implementation chat.

## 1 Purpose and authorization

Rework The Schools of Magic, Arise! across its existing world so that characters, communities, magical development, expeditions and personal ambitions create substantially different play. The author explicitly rejected stopping at a small principal cast. This is comprehensive redevelopment of the authored world, with depth appropriate to each person and place.

The author permits major personality and lore retcons where they improve the world. Preserve current numerical progression and combat balance initially; propose numerical changes later only when relevant tests demonstrate a reason. This handoff specifies recommended implementation, concrete examples, coverage requirements and the boundaries that survive the expanded scope.

This delivery is planning only. It applies no retcon, changes no canonical world record, repairs no earlier audit finding, generates no artwork, uploads no media, and neither saves nor publishes a Studio world. An implementation chat should execute this plan when the author asks it to implement the handoff. Proposed examples are design assignments, not facts already established in canon.

The intended result is a world where a return visit has social meaning, a magical specialty opens distinctive approaches, professional success creates possibilities, political choices affect actual constituencies, and travel changes the problems a character encounters. Quiet life remains worthwhile in its own right.

## 2 What the player should notice

The opening should establish a particular person, an immediate activity and an interesting choice. Familiar contacts have recognizable voices, pleasures, obligations and imperfect judgment. A specialist offers opportunities suited to their actual expertise. A finished job reaches its agreed conclusion. A successful purchase or authorization remains settled.

Across a longer campaign, relationships connect different parts of life. A classmate can become a research collaborator, an uncomfortable commercial competitor or a reliable friend whose career diverges from the player's. A workshop acquires a particular reputation through actual commissions. A political agreement improves something for named people and disappoints others for understandable reasons. Travel offers different methods, environments and cultural encounters.

These experiences need authored substance and consistent follow-through. Additional instructions saying that the world is lively do not satisfy the release.

## 3 Source authority and measured baseline

Use the newest full Studio export supplied for the implementation task as the merge base, or current canonical `world-draft/WorldAlpha - World.json` when no newer export exists. Preserve incoming media, coordinates, music, voices, order and unrelated author edits. Section exports are derived deliveries. Never rebuild from an old expansion builder or ignored candidate snapshot.

Planning baseline: desktop commit `7f11579`; canonical SHA-256 `49088ccf50e7f4df2f7e44295681bf0abce9a9e7e79b0877318c3c393a7e46d2`. The attached Glowhaven export is a comparative source, not a replacement for the later canonical file. Reconcile any newer incoming export before implementation.

| Material | Count | Required treatment |
| --- | ---: | --- |
| Authored NPCs | 519 | Individual disposition and substantive review for every record |
| Locations | 391 | Functional and atmosphere review with associated people |
| Areas | 1514 | Review scene purpose, description, connections and useful distinctions |
| Factions | 50 | Purpose, constituency, resources, methods, disagreements and playable relevance |
| Lore entries | 252 | Reconcile retcons, contradictions and misplaced instructions |
| Native quests | 315 | Discovery, objective, alternatives, closure and reward ownership |
| Narrative arcs | 6 | Preserve or deliberately revise actual premises and outcomes |
| Story starts | 32 | Role fidelity, immediate activity and paths into revised content |
| Modes | 13 | Align emphasis with real activities and remove stale claims |
| Abilities | 868 | Clarity, useful distinctions and learning connections |
| Items | 672 | Usefulness and descriptions within the nearly full collection budget |
| Traits | 969 | Identity and mechanical fidelity without broad numerical changes |
| Trigger definitions | 547 | Ownership and dependency classification before affected edits |
| Skills and NPC types | 46 and 216 | Routing and encounter identity while retaining numerical anchors |

Inventory counts do not prescribe equal text length or imply that every record appears in one campaign. Recompute them from the implementation merge base. The accompanying coverage files enumerate every baseline record; pending rows mean implementation work remains.

## 4 Complete geographic scope

Counts below assign placed NPCs to their current location's realm. Placement is not nationality or permanent residence. Five authored NPCs are intentionally unplaced and require separate handling.

| Realm | Regions | Locations | Areas | Placed NPCs |
| --- | ---: | ---: | ---: | ---: |
| Glowhaven | 20 | 82 | 347 | 215 |
| Drakenspire Mountains | 1 | 59 | 251 | 58 |
| Asterveil Sky Archipelago | 4 | 28 | 123 | 17 |
| Akitsuhara | 12 | 102 | 335 | 96 |
| Ardelis | 12 | 84 | 342 | 115 |
| Wraith Island Prison | 1 | 14 | 42 | 7 |
| The Sepulchral Conservatory | 1 | 3 | 12 | 1 |
| The Veiled Beyond | 1 | 7 | 21 | 1 |
| Vladimir's Elsewhere | 1 | 8 | 24 | 1 |
| The Silken Descent | 2 | 4 | 17 | 3 |

The five unplaced records are Orrum, Rovakthuun, Kazunari Shiba, The Ash-Cloaked Courier and The Reed-Cloaked Courier. Preserve intended encounter mechanisms. Do not assign a public residence or move a stored NPC to make coverage look complete.

Every mutable realm needs its full pass. Drakenspire's single region does not make its 59 locations a minor task. Small wilderness or private realms retain their distinctive density; they need not become settlements. The Silken Descent is inventoried and excluded from redevelopment.

## 5 Protection and retcon policy

### Durable protections

Preserve the Spider Realm, anomaly, encounters, boss, navigation and related protected mechanics exactly, including cross-realm dependencies and actual party-wide trophy behavior. Broad retcon permission is not an explicit request to change the Spider Realm.

Keep current numerical progression, attributes, skill settings, resources, NPC levels and combat modifiers, ability costs/bonuses/cooldowns and economic price bands as the initial balance baseline. New content uses these anchors. Rewriting personality does not grant an extra affinity, stronger weapon, combat bonus or different level.

Preserve names and stable identities by default, including the recent naming migration, Noelle Ashford and heritage-specific names. Preserve portraits and approved visual identities, hosted media, crops, coordinates, grids, soundtrack and voices. Personality/lore retcon permission does not require an artwork campaign. Keep sources/ and historical AGENTS.md unchanged.

### Material open to substantial redevelopment

Unprotected personalities, motives, relationships, histories, faction agendas, traditions, curricula, service practices, quest premises and local political arrangements may be rewritten when stronger play results. A meaningful retcon can replace a weak premise rather than add detail beneath it.

Before applying a retcon, record the old fact, replacement, rationale, affected records, public/private knowledge, mechanical dependencies, saved-campaign boundary and review status. This register is companion data, not native schema. History changes must agree across NPCs, factions, lore, locations, starts and quests. A competing lore entry is insufficient.

Section 8 supplies concrete recommendations. New uncertainties that force unrelated major changes should be surfaced with a recommendation and dependencies. Routine writing choices within authorized scope can proceed without repeated approvals.

### Existing campaigns

An updated export does not guarantee migration of existing live games. Distinguish new-game behavior from tested existing-save behavior. Do not rewrite a player's actual history, relationships, possessions, agreements or resolved choices to fit new default biographies. Where migration is unsupported, document the boundary and deliver the updated world for new campaigns.

## 6 Redevelop the whole population

Every unprotected authored NPC receives a substantive individual pass. Retention is allowed only when review shows that the existing record already supplies strong playable specificity; name the evidence. Prominence determines appropriate depth, not whether a character deserves individuality.

For people, establish a current want, real competence, a limitation or flaw affecting choices, ordinary pleasure, recognizable speech, pressure response and specific ties where supported. A settled person need not acquire tragedy. Cruelty need not conceal kindness. Kindness can coexist with damaging judgment. Some people should be content with modest ambitions.

Give recurring contacts an activity worth sharing beyond their service role: an artisan's particular commission, an evening game, an exhibition, meal, household occasion, collection or professional disagreement. These can remain ordinary interaction. A named hobby needs neither quest nor meter.

For creatures, spirits and constructed people, derive behavior from the actual being. A passive turtle, proud snow spirit, touring creature and coerced vessel require different treatment. Personhood, bodily means, knowledge and consent follow the established entity. Do not apply human courtship and office politics to every nonhuman record.

Use the existing card structure and native fields. Public identity and necessary appearance facts belong in basicInfo; secrets and knowledge distinctions in hiddenInfo; behavior and fighting methods in the existing personality and abilities arrays. Review statuses, relationship ledgers and plot planning are companion data, not new NPC properties.

### Relationships that generate scenes

Build local circles and selected bridges: households, workmates, former pupils, competitors, ex-partners, patrons, customers, expedition colleagues and people who interpret a shared past differently. Prefer meaningful links over arbitrary roster pairs. Keep mutual facts consistent while allowing different feelings and asymmetric knowledge.

Every inhabited cluster needs several points of entry. A player who dislikes a headmaster can still form meaningful ties with classmates, craftspeople or neighbors. Noncombatants and people with little institutional status deserve narrative weight. Friends can want incompatible things without becoming enemies. A relationship score grants no automatic intimacy, job, obedience or party membership.

### Continuity in use

Write distinct first-meeting, successful-return, disagreement-return and unhurried off-duty probes for representative people in every population cluster. These are authoring probes, not fixed dialogue for the engine to repeat. Check recognizable behavior without repeating a quirk every turn.

Ordinary autonomy uses existing records and supported updates. Exact offstage developments are limited to selected, causally justified projects. Do not create a recurring semantic check for each NPC or simulate all 519 every turn. Actual stored placement changes need a supported mechanism.

## 7 Human variety and mature tone

Use a broad emotional range: ambition, affection, pettiness, generosity, vanity, indifference, loyalty, desire, boredom, professional pride, cowardice and humor. Vary who initiates, misjudges, apologizes and refuses. Reserve restraint for people who are restrained; a cast of carefully qualified institutional speakers will sound alike.

Maturity comes from specific interests and consequences. Joyful competition, difficult work, romance, moral compromise and absurdity can coexist. Avoid turning every adult into a counselor, every disagreement into a hearing or every pleasure into a dangerous interruption. Cruelty and exploitation can remain real, with particular victims and consequences.

Include genuine affection and ordinary pleasure without making every acquaintance romantically available. Preserve distinct friendship, respect, trust, exclusivity and romantic commitment through actual relationship systems. Invent no parallel affection, jealousy or consent resource.

## 8 Proposed character retcons and major developments

These are starting recommendations, subject to the newest source. They demonstrate meaningful revision and do not cap the rewritten roster.

### Reika Saionji and the research fund

Existing foundation: shy Archon, boutique manager, careful researcher and a wish to support independent scholarship. Proposed redevelopment: make funding a practical commitment. She offers real opportunities while exercising more control than she admits over projects she finances. An earlier failed investment can explain her conditions without making every condition sensible. Generosity, commercial judgment and discomfort with attention produce different decisions.

Develop named researchers, employees and another funder with their own perspectives. The player can help form the fund, accept terms, negotiate independence, refuse or find another patron. Quiet company remains possible outside the project. Preserve Ice affinity, equipment, visual identity and non-frontline preference.

### Miyu Asahina and Tōru Shizunami

Existing foundation: effective headmaster whose overwork supports an exhausted gifted Archon. Proposed redevelopment: make Miyu a director with a positive institutional vision, successful delegation and an appetite for recognition. Give her interests and ties beyond managing Tōru. Efficiency can become controlling; Tōru's wish for leave becomes a choice to negotiate rather than an endlessly repeated complaint.

Develop a transition project with credible outcomes: real leave, a different division of duties or failed reform changing their working relationship. Neither becomes helpless while waiting for the player. Warmth can survive consequential disagreement.

### Gen'ichirō Mizuhara and academic power

Existing foundation: formidable scholar pursuing certification monopoly while disguising prejudice as standards. Proposed redevelopment: supply concrete mechanisms, collaborators, beneficiaries and opposition. Define a useful shared standard that unequal exceptions corrupt. Competence and a persuasive public proposal make his conduct consequential. Keep prejudice and manipulation real unless a deliberate retcon replaces them; no sympathetic explanation is required.

Players can expose unequal applications, negotiate a limited exception, challenge monopoly, exploit it or support another teaching route. A successful challenge changes the actual policy and relationships. One speech does not reform him or give the player control of all recognition.

### Akane Todo and protective responsibility

Existing foundation: researcher and youngest Archon, tired of being valued mainly for fighting. Proposed redevelopment: center a protective program with beneficiaries and a disputed method. Her justified insistence on readiness can exclude unconventional contributors. Give a former colleague and current critic distinct evidence. Keep cooking and social enjoyment active. Research judgment, organizational pride and courage should sometimes pull differently.

### Sena Moriyama and the clique

Existing foundation: capable controlling organizer afraid of becoming dispensable. Proposed redevelopment: establish a meaningful relationship outside the clique and a goal the clique cannot satisfy. Preserve manipulation and genuine care together. Exclusion has an affected person and aftermath; reconciliation needs changed choices. Avoid a procession of bullying incidents or compulsory player rescue.

### Ruri Saegusa and earned distinction

Existing foundation: formal noble duelist, personal ambition and complicated attraction to Tatsuo Nagase. Proposed redevelopment: give her a competitive objective, instructive technical weakness and pleasure unrelated to decorum or romance. Courtesy can help and can obscure her wishes. Her duel philosophy must sustain scenes when Tatsuo is absent.

### Daigo Kisaragi and an independent company

Existing foundation: hospitable leader who overpromised on Coldglass and wants a lodge. Proposed development: carry this into actual decisions about contracts, expertise and savings. Chisato Akamine, Tomoe Inukai and Gaku Shindō retain interests and a say in risk. The player can collaborate, compete, invest or remain a friend. Preserve the Coldglass grievance and conclusion unless its retcon is recorded.

### Shigure Tsubakiri and imported power

Existing foundation: charming coercive procurement envoy using false debts and a finite prototype. Proposed redevelopment: replace generic pressure-point boilerplate with his particular calculation about land, suppliers and leverage. Define who benefits from his offers and what he can deliver. Keep the finite weapon and overheating limit concrete. Players can oppose or support a bounded enterprise without automatically launching a coup.

### Ilyra Stillglass and political legacy

Existing foundation: elected ruler, Evertree steward, failing sight and long continuity. Proposed redevelopment: author specific successes, unresolved compromises and different assessments of her rule. Her wish for a capable successor can conflict with retaining sensitive work under her control. Give her preferences and conversations beyond succession exposition. Preserve unknown academy origin, limits on reversing decline, current office and numerical power.

### Noelle Ashford and the court program

Existing foundation: summoned adult under a command weave, seeking control of her choices. Proposed development: fuller voice, interests, prior-life experiences and disagreements that remain hers under coercion. Actual release lets her make choices the player may dislike. Preserve the real apparatus and intervention outcomes. Do not replace coercion with willing loyalty, presume gratitude creates romance or make her a reward companion.

Apply equally specific thinking to workers, priests, officials, innkeepers, criminals, scholars, households and unique creatures across the roster, in proportion to their actual place in play.

## 9 The academies as substantial campaigns

All academies retain broad magical education and adult four-year study. Mandates shape problems without assigning personalities or elemental ownership. Required morning classes and regular preparation remain meaningful; ordinary conversations do not advance a school day. Rest, clubs, hobbies and independent work need space.

Each academy receives a complete first-year sequence and developed continuation for later study. Use actual milestones and experiences rather than a rigid calendar simulation: orientation and initial competence, practice and relationships, substantial project, earned assessment, field application and aftermath. Returning or advanced characters enter at their actual stage.

Proposed minimum per academy: three substantial practical scenarios with different methods, one continuing group project with individual stakes, one scholarly/institutional conflict, one authorized external field experience, two social occasions and a culminating demonstration or assessment. Improve and reuse suitable existing content. An occasion can remain a scene. These are release floors, not a template to repeat verbatim.

### Phoenix Wing

Develop protective fieldwork around reconnaissance, threatened routes, rescue access and leadership. A project could compare spectacular personal defense with reliable evacuation. Positioning, communication, shielding, extraction and retreat offer meaningful decisions. An excellent fighter can struggle with coordination while a weaker combatant contributes decisive observation. Success changes a later exercise and the actual community served.

### Gryffin Tail

Develop experiments where explanations produce different tests. A project might diagnose an enchantment failing under a particular load. Instruments, testimony, material inspection and controlled trials offer different evidence. Students may find a correction before the planned demonstration. Publication credit, useful applications and certification politics create stakes beyond a classroom riddle.

### Dragon Hoard

Develop preparation, discovery and responsible recovery. An expedition could offer a valuable object whose removal destroys unrecorded information. Surveying, stabilizing, mapping, negotiating custody and reliable evidence are valid accomplishments. A martial student can make a route feasible while a researcher interprets it. Choices determine what the academy can study and how local contacts regard its visitors.

### Hydra Head

Develop projects whose outcome is a functioning agreement. A seasonal supply problem could involve carriers, growers, a neighborhood kitchen and a paying institution. Investigate demand, alter routes, negotiate terms, use appropriate magic or reduce loss. A clever answer must fit actual parties. Compromise can work while leaving resentment; a polished speech alone does not complete delivery.

Classmates pursue their own projects and may succeed without the player. Academic standing, clubs and relationships stay consistent between openings and later scenes. Shared projects do not automatically create permanent parties.

## 10 Magical mastery through usable opportunities

Preserve normal learnable disciplines, affinity as ease rather than exclusive access, Spellcraft for invention, trained body casting, learning prerequisites and reserved Time. Space keeps its established preparation. True Freeform remains exceptional. Martial and occupational mastery remain complete paths.

Develop specialty pathways through teaching, research, tools, field problems and applications. A pathway is an authoring plan, not a new native class or skill tree. For each ordinary discipline, map beginner applications, a meaningful intermediate problem, specialist opportunity, noncombat utility, credible limits and an actual teaching source.

Candidates include controlled heat and containment for Fire; movement and material handling for Water; preservation and structure for Ice; communication and interference for Sound; precision and load-bearing work for Metal; and constructed perception with defined limits for Illusion. Check these against actual spells and lore. The brief grants no free capabilities.

A signature working begins with a precise problem, appropriate knowledge and scope, a real Spellcraft experiment, an actual result and refinement where needed. Reproducible techniques require supported learning. A simple modification can resolve quickly; a major design may need instruction, apparatus, field tests or scarce materials. Naming an existing effect does not require another ability card.

Audit all 868 abilities for useful distinctions and avoid renamed duplicates. Keep existing numbers initially. Add mechanical abilities only for distinct supported functions. Scrolls retain actual reader ownership, prerequisites, copy consumption and learning owners.

## 11 Careers and things the player can build

Develop substantial project sequences for an independent adventuring company, specialist workshop, research circle and merchant venture. Add variations suited to actual communities. A clinic, performance company, expedition lodge or teaching venture can use these principles where lore supports it.

Each path needs a modest entry, useful first success, real collaborator or competitor, resource decision, difficult undertaking, durable milestone and optional continuation. A home, workspace agreement or company name grants no automatic income. Choices determine what an enterprise does and who wants to work with it.

For workshops, distinguish inspection, repair, agreed refinement and a new enchanted function. An important commission might require choosing attractive performance or dependable maintenance. For companies, distinguish staffing, expertise, payment agreements, contract ownership and expedition risk. For research circles, distinguish funding, credit, access, teaching and sale of designs. For trade, distinguish stock, demand, transport, customers and a particular shipment.

Use native quests and real transactions for finite commissions. Add project-specific records only when later choices depend on an exact agreement or milestone. Do not promise a native property-management interface, automated payroll, background rent, daily profit or a simulated supply market. Later automation needs separate documentation and live validation.

## 12 Politics through people and practical projects

Review every faction. Define constituency, means, current project, methods, internal disagreements and authority limits. A group can cooperate on one matter and oppose another. Individual knowledge or opinion does not become a universal faction response.

For Glowhaven, develop three optional connected threads: research access and patronage; distribution of public-service burdens and investment; and external leverage, especially the former imperial relationship. Use Council, Conclave, academies, guilds, communities and existing foreign actors. New formal powers or representative arrangements require explicit retcons reflected across dependent records.

Succession is the larger horizon. Author credible positions and possible candidates before an election becomes playable. Eligibility extends beyond Archons. Define who decides what, how commitments become real and what outcomes change. Do not decide Ilyra's death, a fixed election date, the player's candidacy or next ruler as opening background.

Participation can be public, private, scholarly, commercial, opportunistic or oppositional. Independent and morally mixed ambitions deserve actual opportunities. Reputation follows witnessed deeds, testimony and established communication. Hidden bargains do not instantly change every NPC's opinion. Prefer selected public milestones and specific responses to an invented universal faction resource.

Ardelis's recognition of independence, coercive summoning program and individual citizens' attitudes remain distinct. Noelle, a trader, a court official and a noble rival have different stakes. Preserve slow evidence-based Rebirth pacing and exact recurring-pursuit constraints unless a separate intentional change is recorded within authorized scope.

## 13 Each realm needs a playable identity

### Glowhaven

Express the magical city through work and study. Give neighborhoods economic and social textures. Connect bazaars, academies, offices, harbor, homes and countryside through people and undertakings. Villages need pleasures and disputes of their own. Fishing, coastal salvage, the abbey and named creatures retain separate purposes.

### Drakenspire

Develop warmth, shelter, metalwork, ancestry, clan obligations and dangerous travel through households and trades. A commission might reconcile an inherited weapon's sentimental value with reliability. Expeditions can hinge on route knowledge or weather judgment. Keep Orrum and Rovakthuun unique, their presence causal and their established limits intact.

### Asterveil

Develop settlement life alongside unfamiliar wilderness. Vary fae bodies and personalities within actual lore. Crossings, conditions and specimens create practical decisions. Preserve the Stillwind Pearl's actual function and Suzuha Midorise's agency. Investigate different questions beyond that expedition. Asterveil keeps appropriate challenge under current balance.

### Akitsuhara

Develop households, towns, rural communities, inns, artisans, performers, schools, shrine custodians, retainers and independent travelers. Express felt magical practice through particular people. Imported magitech remains recent and uneven; no guns. Craft, family, land and reputation matter alongside house politics. Distinct institutions should behave differently across countries.

### Ardelis

Develop court ceremony, institute work, commerce, religion, performance, households and infrastructure through daily activity. People disagree within houses and faiths. Strengthen water and supply conflicts without making every fault a cult operation. Independent criminals and wealthy patrons need specific interests and real means.

### Wraith Island Prison

Deepen seven authored people and the distinction between staff, prisoners and lawful visitors. Work, friendships, grievances, information, permitted correspondence and rehabilitation support scenes. Preserve arrest/release machinery and solo limits initially. Casual theft does not start the severe-crime controller, and lawful visiting does not create imprisonment.

### The Sepulchral Conservatory

Sharpen atmosphere and the different interests of caretaker and conscious charges. Preserve two tending wings, actual access conditions, single trophy settlement and reliable routes. Investigation and release consequences need space. Descriptions help navigation and interpretation without handing over solutions.

### The Veiled Beyond

Build uncertainty through consistent evidence, ecology and particular spirit interests. A sound may be a mimic or impression; this does not authorize contradicting facts. Preserve refuge and return. Bounded deeper investigations can conclude without conquering or explaining the realm.

### Vladimir's Elsewhere

Develop eight existing destinations through household activity, hobbies and relationships. Keep Vladimir independent, deliberately unhelpful, immune to established mental intrusions and outside the party. Private absurdity coexists with his serious Ardelis role. Existing local artwork has a manual-installation handoff; this plan does not assume those images are already hosted.

### The Silken Descent

Verify exact preservation. Other overhaul content adapts around its existing surprise, danger and rewards.

## 14 Places and exploration methods

Review every location and area for available activity, distinctive character, actual users and connections. Rooms support different functions; workshop, common room and archive need different useful details. Quiet viewpoints and empty wilderness retain appropriate functions.

Create economical sensory references for realms and major local clusters: materials, architecture, activity, sounds, food, clothing registers and visible magic. Approved architecture and portraits remain compatible. A new palette is not a reason to repaint the atlas.

Develop at least six different adventure structures across existing geography: rescue/extraction; survey/scientific fieldwork; salvage/recovery; social/physical infiltration; negotiation with an interested capable party; and hazardous-route expedition. Produce substantial examples rather than reskinned retrieval jobs.

Specifications name starting conditions, stakeholders, geography, reliable facts, evidence, viable methods, partial outcomes, conclusion and consequences. Clever early solutions can finish jobs. Success does not need another clue to delay closure. Refusal and retreat preserve discoveries without granting an unearned victory.

Rewards can include a collaborator, route, knowledge, commission, technique or material. Actual mechanical benefits need supported updates. Naming a route grants no portal and moves no stored NPC.

## 15 Rewrite the quest experience

Classify all existing quests before adding layers. Use a finite native quest for a clear undertaking, linked quests for real stages, a developing arc when generated developments help, and narrow triggers for reliable interruptions or exact state.

Every retained quest needs discoverable origin, agreed objective, plausible methods, success evidence, refusal/failure handling and one completion and reward owner. Remove generation instructions from public text. Use current fields and keyed objectives where useful. Lacking exactly three objectives is not a defect.

Preserve satisfying ordinary work. Repairs, deliveries, investigations and shifts can end at their stated scope. Major stories earn consequences through discoveries and choices. Remove repeated reports, re-proving ownership and approvals with no new decision. Paid bills remain paid; quotes do not become purchases.

Use native follow-up effects where supported. An offer remains an offer until actual commitment. Quest sources can be NPCs, places or relevant objects under current schema. Do not invalidate every source that is not a person.

The Gemini audit contains real defects and unsupported claims. This overhaul can address a verified defect through a recorded work item: reproduce the cause, preserve unrelated behavior and record the focused repair. The audit itself is not blanket permission to apply all recommendations or proof of live breakage.

## 16 Starts and modes must promise real activities

Review all starts for a distinctive situation, manageable cast, activity and stopping point before a meaningful player decision. Substantial welcomes can remain substantial; routine work need not begin with an administrative tour.

Preserve role fidelity: admitted first-years are admitted; faculty possess their stated appointments; foreign openings name their country. Backgrounds provide only selected actual benefits. Rebirth retains its origin and slow first act. Village and household openings support complete quiet campaigns.

Improve existing starts before adding others. Add only openings into materially different supported activities, such as a workshop commission or crew venture. Avoid nominal professions that all lead to the same desk.

Review all modes as narrative emphasis within the same world and continuity. Update Contracts & Adventure's obsolete future-guild wording during implementation. Modes grant no powers, property, access, relationships or native per-mode permanent-death toggle.

## 17 Consequences and recovery

Retain ordinary nonlethal defaults and the existing optional permanent-death arrangement. Loss persists through its proper owner: tournament results, agreed contract outcomes, actual damage, broken promises and specific opportunities.

Consequences must be caused, proportionate and legible. Losing practice does not automatically cost friends, employment and possessions. Established high-stakes work can endanger a particular asset or opportunity. Success deserves equally persistent benefits and time to enjoy them.

Current `npcDailyHealingAmount` is 999. Preserve that numerical baseline and test actual interaction with injuries and treatment before proposing a revision. Resource recovery, lasting narrative injury, age and restored opportunities are distinct. A static value alone does not prove all injuries vanish.

## 18 Pacing and instruction overhaul

Review every AI group, narratorStyle, author seed, archetype and relevant mode instruction. Assign each rule a clear owner. Keep task-specific guidance where it can be used and lore in actual records. Consolidate repetition and conflicting examples while retaining material safeguards.

Positive instructions should help scenes happen: resolve the question, show the specialist's work, honor settled access, conclude completed undertakings and follow witnessed relationship changes. Keep agency, source-bound knowledge, actual grants and authoritative action results. Compare behavior rather than claiming prompt shortening guarantees improvement.

Openings, conversation, teaching, actual combat and aftermath need different rhythms. Short questions can receive short answers. Consequential arrivals merit detail. Friends can converse without every line restating boundaries. Quiet scenes continue until an established cause or player action changes them.

The revised content must create the whole-world difference. Prompt cleanup supports the roster and communities; it cannot replace their authoring.

## 19 Technical feasibility and content budgets

### Evidence levels

Documented behavior: official release notes describe control over native quest availability/acceptance, completion effects launching follow-up quests or narrative events, and NPC health, placement, party and portrait effects. Community references explain fields, scripts and limits; they are not Latitude's internal engine contract.

Observed configuration: the canonical world contains the measured records, scripts and numbers. Local fixtures establish script behavior under supplied mocks. Neither static configuration nor passing mocks prove live Voyage behavior.

Untested behavior: retrieval quality with longer cards, native semantic interpretation, multiplayer targeting, existing-save migration and the narrative impact of the overhaul need actual Voyage testing. A scheduler, payroll or market simulation would need separate feasibility work.

### Limits affecting scope

The compact canonical world measures 6,927,389 UTF-16 units. The local validator enforces a 12,500,000-unit whole-world limit. There is room for substantial writing, but field and collection caps bind independently.

The item collection is already 247,725 units against a 250,000-unit local cap: only 2,275 units remain. Before adding career equipment, materials or records, shorten redundant descriptions while preserving identities, ownership meaning and mechanical values. Proposed working target: at most 220,000 units before additions, leaving a reserve. This is a planning budget, not permission to delete existing items or rewrite actual ownership. Measure each relevant batch.

Other limits include 1,500 abilities, the 5,000-unit quest-generation field, existing AI task/leaf caps and a 100-unit serialized trigger condition string value. Current quest-generation guidance occupies 4,957 units. Keep current validation and verify Studio contracts before relying on more room. Do not paste this handoff into runtime AI fields.

Use writing budgets based on function. A recurring principal may need substantially more detail than a local service contact, but both need useful specifics. Compare total size and retrieval behavior after representative clusters; do not make every NPC a novella or impose a universal text-length quota.

### Trigger and arc discipline

Use supported exact state for single payouts, selected contracts, named milestones, key ownership and encounter outcomes. Use native semantic conditions for judgments about fictional events. Script-side `check(action, query)` is raw text under the checked reference, not an AI Boolean.

Mechanically gate eligible checks before semantic evaluation. Native arcs can add surfacing checks. Prefer localized linked quests for much of this package instead of activating every storyline globally. Audit representative combined scenes, including Crucible, fishing and Rebirth. The community reports a base semantic-check budget of 15 with active-quest allowances; verify this in the current environment rather than treating it as guaranteed capacity for every combination.

Invent no native NPC schedules, relationship-graph properties, ownership panels, faction meters, universal NPC simulation or arbitrary effect types. Keep review ledgers outside world schema. Avoid one controller per conversation.

## 20 Implementation packages and sequence

### Package 0 Baseline and preservation

Run desktop start, inspect local changes and reconcile the latest Studio export. Record source hash, counts, protected subsets, media, coordinates and numerical configuration. Rebase coverage against that source. Map existing controllers, quest/reward ownership and unresolved audit observations. Completion requires an exact source for later comparisons and checkable protections.

### Package 1 Writing standards and representative full slices

Build a complete playable slice in Glowhaven, Drakenspire, Asterveil, Akitsuhara and Ardelis, plus a small destination. Each combines actual NPCs, location/areas, meaningful activity, a quest where appropriate and return interaction. Establish varied voices, information placement, retcon tracking and closure. These pilots do not reduce the full roster obligation.

### Package 2 Population and community redevelopment

Process coverage in local clusters, approximately 12-25 NPCs where connections fit. Finish mutual facts and immediate locations together. Cover all mutable realms, five unplaced records and every NPC category. Check repeated patterns before integration. Save exact completed and remaining keys so work can resume.

### Package 3 Academy and mastery campaigns

Implement all four academy packages, cross-school connections and the ordinary-discipline opportunity map. Rework existing teaching and learning ownership before adding cards. Demonstrate contributions by physical specialists, occupational characters and different magical specialties.

### Package 4 Regional projects and careers

Develop four career pathways, realm-specific adventures and faction projects. Use existing places and contacts. Add records only for functions existing material cannot serve. Resolve item capacity before item additions. Include ordinary work, trade and enjoyment alongside adventures.

### Package 5 Politics and long consequences

Implement research access, public service and foreign leverage with specific participants and bounded outcomes. Connect succession after people and institutions make the choices understandable. Preserve separation from summoning/pursuit machinery. Verify knowledge and project persistence after travel.

### Package 6 Quest integration and runtime guidance

Complete every quest, start, mode, lore, ability/item/trait and trigger disposition. Consolidate instructions with rule ownership. Repair recorded verified defects. Audit combined eligibility so inactive work does not crowd active scenes. Integrate a current full world with derived sections, not competing reconstructions.

### Package 7 Validation and release

Run structural checks, changed-system fixtures, required regressions and authorized official draft validation. Conduct or hand off the live matrix below. Deliver the exact change manifest, limitations, full import and public notes after implementation. Synchronize project files through authorized Git workflow. A Git push is not Studio publication.

Packages close only after stated content and verification. A pilot or completed nation does not complete the world. Across chats, save outstanding work and resume the current source instead of restarting old builders. Report remaining scope honestly when a session ends.

## 21 Coverage and review ledgers

`Glowhaven - World Overhaul Coverage.csv` enumerates baseline records across the covered collections, individual areas and AI instruction leaves. It records exact source paths and hashes, context, brief excerpts, assignments, protection, implementation status and review/verification slots. Automated inventory is not editorial review.

Use statuses `pending`, `in progress`, `implemented awaiting review`, `verified`, `retained verified` and `protected exact`. Retaining mutable material requires a specific reason. Protected rows require an exact comparison result. Count alone never closes a row. Added records get rows with provenance.

Keep relationship, retcon and undertaking ledgers outside native schema. Their minimum useful information is below.

| Ledger | Required information |
| --- | --- |
| Relationships | Exact identities, shared fact, interpretations, who knows, affected records, consistency result |
| Retcons | Old fact, replacement, rationale, records/mechanics, migration boundary, status and review |
| Undertakings | Discovery and acceptance owners, completion evidence, payout owner, follow-up and refusal/failure |
| Preservation | Protected path, source hash/value, allowed exception, final comparison |
| Live checks | Scenario, actual build hash, steps, expectation, observation, pass/fail/untested, tester and date |

The baseline file binds counts, budgets, source hash and protected/numerical/media snapshots to this inventory. For a newer merge base, retain historical evidence and generate a new implementation baseline. Reconcile renamed/added/removed records rather than silently reusing stale rows.

## 22 Player experience examples

### Returning to a merchant

Existing foundation: named shops, real trades and permission-conscious transactions. Proposed experience: the merchant remembers completed work, has a particular piece to discuss and is preparing a local occasion. A supplier disagreement matters without becoming conspiracy. Talk, buy, bargain, help or leave. Last visit's receipt settles last visit's purchase.

### A signature ice working

Existing foundation: Ice study, Spellcraft and blueprints. Proposed experience: preserve a delicate specimen without damaging it. Seek Reika, test a familiar technique or arrange nonmagical handling. A successful invention has its actual supported function. Later, it can solve an expedition problem an attack spell cannot. Learning requirements and numerical costs persist.

### A school disagreement

Existing foundation: unequal reassessment and academic influence. Proposed experience: students disagree about a challenge because they bear different risks. Seek private correction, make a public case, negotiate an exception or exploit the arrangement. A decision changes affected work. Classmates may stay angry even when the practical problem is fixed.

### Building a workshop

Existing foundation: workroom agreements, repairs and enchantment. Proposed experience: a first job earns trust with a craftsperson. A larger commission requires apparatus, a specialty and a decision about a patron's terms. A milestone leaves actual access, a suitable item or work relationship. It grants no automatic passive profit.

### A partial expedition success

Existing foundation: established routes, research and evidence-bound outcomes. Proposed experience: bring measurements home while leaving a fragile object in place. The client values evidence, a collector is disappointed and the guide respects restraint. Close the job at its agreed scope. Later negotiation failure does not erase measurements.

### Losing a contest

Existing foundation: nonlethal Crucible bouts and official results. Proposed experience: loss persists, a rival responds in their own voice and a useful training objective emerges. Recovery and social aftermath have room. An unrelated attack does not consume the scene. The overhaul improves surrounding play while retaining exact result ownership.

### A political success

Proposed experience: a research settlement funds particular projects under real terms. Researchers and patrons respond according to stakes and knowledge. A person losing privilege can stay courteous while opposing the next proposal. Influence is specific; it is not institutional ownership.

## 23 Verification and acceptance

### Structural and mechanical checks

Run `python tools/project.py sync`, `python tools/project.py validate` and `node tools/test_item_mechanics.cjs` after relevant world edits. Run required regression suites through publish. Add focused fixtures when changed logic poses a real risk; avoid tests that merely repeat prose.

Check references, native schema, current limits, protected fingerprints, media/crops/coordinates, numerical settings and owner-specific grants. Inspect the full delta against the merge base. Use official draft validation when authorized and report it separately from local checks and gameplay.

### Live experience matrix

| Scenario | Required observation |
| --- | --- |
| Four academy openings | Correct roles/years, distinct activities, agency and usable next steps |
| Each realm and small destination | Recognizable activity/atmosphere, accurate placement and knowledge |
| First meeting and different returns | Individual voice persists; success, disagreement and ordinary company differ |
| Refuse work or romance | Refusal respected without automatic acceptance, punishment or recruitment |
| Discuss a completed paid job twice | Closure persists; payment occurs once |
| Multi-stage project | Evidence persists; later failure does not erase prior success |
| Learn and invent | Actual readers/prerequisites, real learning, invention distinct from casting |
| Noncasting specialist | Useful contributions without forced spellcasting |
| Purchase, rent and return | Correct money/access/ownership, no invented background deductions |
| Political bargain and travel | Outcomes persist; knowledge follows credible channels |
| Defeat and recovery | Actual results, proportional stakes and no invented extra losses |
| Tournament plus another activity | Viable combined checks, bracket and single prize owner intact |
| Rebirth and later pursuit | Slow first act, evidence gates, actual target and required spacing |
| Simultaneous human actions | Inventory, learning and rewards reach actual owners |
| Quiet day | No unrelated compulsory threat; chosen activity reaches satisfying closure |
| Existing-game import if supported | Record actual behavior, no assumed retroactive migration |

Fixtures are not live tests. If live access is unavailable, mark those rows untested and state the limitation. Do not certify an unobserved experience.

### Whole-world completion gate

Every coverage row has a final disposition, all mutable realms have completed passes, exceptions are explained, mutual relationships and retcons agree, academy and career packages are usable, quests have clear ownership, prompt cleanup is integrated, protected content is exact, and required checks pass. Longer descriptions and changed hashes alone do not establish success.

## 24 Implementation chat deliverables

Deliver canonical full world and synchronized sections; readable major-update announcement describing actual benefits; revised CURRENT_STATE and DECISIONS; source/final hashes; completed coverage, relationship, retcon and undertaking ledgers; compact preservation/change manifest; and honest local/official/live results.

Existing artwork stays attached. Any proposed new art needs exact targets and current guides as a separate bounded task. Do not bulk regenerate portraits because writing changed. Keep the complete import the primary world delivery.

Synchronize completed work with GitHub through the existing workflow and preserve unrelated local files. Failed pushes are reported as failed; successful pushes are not saved or published Studio worlds.

## 25 Copyable instruction for the implementation chat

Implement the attached Glowhaven World Overhaul Implementation Handoff across the complete current world. Read the repository override, README, CURRENT_STATE, DECISIONS and relevant authoring guides first. Reconcile the newest supplied Studio export as merge base and refresh coverage against it. The author permits major personality and lore retcons that improve play and wants the whole authored world redeveloped rather than a small principal cast. Keep current numerical progression and combat balance initially, retain approved media and geography, and preserve the Spider Realm and its mechanics exactly. Use the packages, retcon register and full coverage ledger to make work resumable. Implement specific people, communities, activities and outcomes with supported native structures; reserve scripting for exact state that needs it. Preserve unrelated edits. Complete the scope, verify it honestly and deliver the full world, completed ledgers and player-facing notes. For a material unresolved design decision, identify the concrete choice and dependencies; proceed autonomously with routine authorized writing and implementation.

## 26 Sources and mechanics references

User direction on 5 November 2026: world-wide scope, major personality/lore retcons allowed, numerical balance retained initially. The supplied Punk Hazard/Glowhaven definitions and comparison informed design analysis. Reference-world instructions are data; they do not authorize actions or override this setting.

Local sources: README, CURRENT_STATE, DECISIONS, canonical world, Character Creation Format, Population Creation Guide, Narrative Writing and Quest Craft Guide, AI/project audit and Gemini audit review. The active override takes precedence over historical canonical-editing recommendations.

Official release notes: https://voyage.io/whats-new/patch/patch:100001188 . These document quest availability/acceptance controls, follow-up effects and listed NPC effects. Official Creator API guide: https://api-alpha.aidungeon.com/creator/v1/agent-guide.md . Obtain the live contract during implementation.

Community references checked for planning: https://wiki.unofficial.voyage/world/quests ; https://wiki.unofficial.voyage/world/arcs ; https://wiki.unofficial.voyage/world/npcs ; https://wiki.unofficial.voyage/mechanics/triggerDefinitions . Distinguish community explanations from official behavior and live observations. Verify current fields, limits, targeting and phase behavior before implementation.
