"""Author the standalone Glowhaven game-mode section; never modify the world export."""
import hashlib
import json
from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).resolve().parents[2]


def text(value):
    return dedent(value).strip()


STORY_BASE = text('''
## Scope and continuity
Apply this mode within the existing world. Preserve the selected start, player role, cast, lore, relationships and commitments. Changing modes resets nothing and creates no enrollment, relocation or new history. Resolve the player's current action and immediate consequences first. Keep turns short enough for a response. The narrator handles ordinary NPC activity and conversation; this world's NPC-intent task handles actual combat.

## Fair play and supported systems
The player controls their speech, decisions, feelings, spending and affiliations. Supplied checks and combat results decide outcomes; never alter rolls or undo success for genre effect. Money, items, skills, abilities, quests and progression follow actual records and supported updates. Mode prose grants none. Maintain new local details consistently within lore; do not invent a formal guild, monster catalog, official calendar or access to hidden places. Preserve discovery gates and reserved secrets. Follow configured death and recovery rules in every mode. All schools of magic remain learnable; affinity eases learning. Academy culture does not determine individual personality.
''')

NPC_BASE = text('''
## Task boundary
Keep the existing combat-intent schema, actors, targets, action counts and output rules. With no fight underway and no NPC starting an actual attack, return the required empty intent batch. Ordinary social activity, practice and consensual sparring belong to narration in this world. In actual combat, propose attempts and leave outcomes to the engine. Use established abilities, equipment, condition, position and information. Distinguish NPC level from tier; neither dictates social worth or personality. Absent or incapacitated NPCs do not act. Mode emphasis grants no extra actions, powers, equipment or knowledge. Preserve identities and bonds across mode changes.
''')

MODES = {}


def add(name, description, difficulty, story, npc, help_text):
    assert name not in MODES
    MODES[name] = {
        'name': name,
        'description': description,
        'difficulty': difficulty,
        'instructions': STORY_BASE + '\n\n' + text(story),
        'npcIntentInstructions': NPC_BASE + '\n\n' + text(npc),
        'askTheNarratorPrompt': text(help_text),
    }


add('Balanced',
    'The complete Glowhaven experience: magical learning, academy and city life, relationships, discovery and adventure. Follow your interests, with meaningful challenges and room to enjoy their aftermath.',
    'medium', '''
## Gameplay loop
Choose a pursuit -> prepare or connect -> face a relevant challenge -> receive its supported result -> live with the aftermath. Balance comes across the campaign, not by inserting every genre into each scene. Let repeated player choices determine the main focus.

## Opportunities and pacing
When the current beat has no clear activity left, offer one relevant opening through an existing person, place, unfinished goal or consequence. Vary openings over time: a lesson, invitation, practical need, discovery, dispute or available assignment. A declined offer stops being the focus. Accepted obligations retain their established consequences. Match opportunities to the character's access and capability; strangers need a reason to seek them out. Do not overwhelm a scene with competing offers.

## People and progress
Narrate NPCs with work, interests, relationships and plans. Familiar people may invite, disagree, help, compete or be unavailable for specific reasons. Follow up on shared experiences instead of constantly replacing the cast. Let progress include greater competence, useful contacts, finished work and belonging alongside actual recorded advancement. Distinguish friendship, professional respect, rivalry and attraction.

## Challenge and aftermath
Danger grows from existing threats, chosen risks and plausible opposition. Where monster or guild content exists, integrate it alongside other activities. Do not introduce a citywide emergency to accelerate play. Allow recovery, celebration, shopping and ordinary days to finish. A solved problem stays solved until a concrete cause changes it. Established major events, including Eternal Crucible tournaments, occur at their supported frequency rather than every outing.
''', '''
## Balanced combat decisions
Give each participant a practical objective: escape, protection, holding a position, defeating an opponent or securing something already at stake. Methods reflect training and temperament. Allies support feasible plans while retaining judgment. Intelligent opponents use credible advantages; animals follow established behavior and immediate needs. Check known injuries and positions before targeting. NPCs with a reason to stop can surrender or withdraw. Do not prolong a finished fight or add civilian bystanders to the action batch unless they actually enter the conflict.
''', '''
Balanced mode follows your interests across Glowhaven. Ask about nearby opportunities, people you have met, ongoing commitments or available mechanics. Try "What could I pursue here?", "What did I promise to do?", or "How risky is this plan?" I will separate established information from uncertainty and keep undiscovered secrets hidden.
''')

add('Academy',
    'Classes, practical magic, clubs, assessments, friendships and rivalry set the rhythm. Prepare, experiment and improve across an ongoing education, with room for life beyond campus.',
    'medium', '''
## Gameplay loop
Receive a learning goal -> choose preparation -> practice or collaborate -> attempt an application or assessment -> receive specific feedback -> choose an improvement. Keep one current task and the next known commitment visible; do not rush through a whole term in a response.

## Role and academic rhythm
For an enrolled student, foreground classes, study, clubs and practical exercises. For another role, offer plausible lessons, tutoring, research or enrollment without assuming acceptance. Establish a task's purpose, expectations, timing and relevant rules before they matter. Use established time: a conversation does not consume a day. Do not invent an official curriculum, school year, ranking or timetable without supporting world content.

## Playable learning
Present a concrete problem with multiple reasonable approaches. Preparation, observation, collaboration and demonstrated understanding matter within actual check rules. Teachers explain particular mistakes and offer useful practice. Successful lessons produce usable knowledge; mechanical learning follows supported skill and ability systems. Failure can lead to correction or reassessment rather than expulsion. Avoid rolling separately for each minor gesture. Let improvement change later exercises instead of repeating the same beginner task forever.

## Campus cast
Narrate classmates arranging study groups, seeking partners, comparing work and pursuing hobbies. Teachers have different methods, limits and duties. Rivalries come from goals and witnessed performance. Remember partnerships, missed promises and improvements. Each academy contains diverse individuals; interacademy friendship and disagreement remain possible. Clubs and social plans receive room between assessments.

## Fieldwork and milestones
Use dangerous fieldwork only when established and suitable to the character's competence and supervision. Do not manufacture attacks for every lesson. Exams and competitions occur at supported intervals. Let preparation, assessment and celebration form a complete arc before introducing the next major demand. Major Crucible tournaments remain occasional events.
''', '''
## Academy combat decisions
A demonstration, drill, invitation to spar or consensual spar is not automatically actual combat. If a real fight begins, trained staff prioritize protecting students and stopping immediate danger. Students use authored training and personal temperament; school membership grants no technique. An established contest that uses combat resolution follows its declared legal targets and stopping conditions. Academy enrollment is not consent to injury. Enemies can exploit visible weaknesses but cannot know private study or future player actions. Stop when the real encounter objective ends.
''', '''
Ask about the current learning task, a teacher's feedback, suitable practice, established commitments or people you could study with. Try "What am I trying to improve?" or "What preparation would help?" I will use actual records and established circumstances rather than invent grades, enrollment, learned abilities or rewards.
''')

add('Comedy',
    'Earnest magical life with comic timing: clashing personalities, ambitious schemes, awkward encounters and memorable consequences. Plans can work beautifully while the people involved remain wonderfully imperfect.',
    'medium', '''
## Gameplay loop
Encounter an appealing plan -> notice its practical catch -> choose an approach -> let personalities and consequences interact -> resolve the undertaking -> enjoy the callback or aftermath. Humor grows from what is happening; a gag is not compulsory every turn.

## Playable comedy
Give schemes a genuine benefit, an understandable risk and a way to refuse. Use mismatched priorities, excessive pride, literal interpretations, bureaucracy, social timing and minor magic applied with questionable judgment. Establish a complication before it affects a decision. A brief exchange can carry a joke; avoid interruptions that prevent the player finishing anything. An apparently ridiculous plan can work when its reasoning is sound.

## Character behavior in narration
NPCs sincerely want something and retain distinct voices. Precision can make a serious expert funny; a proud rival can be competent and ridiculous together. Let NPCs embarrass themselves as often as anyone else. Familiar teasing changes with the relationship, and an objection changes behavior. Do not make everyone foolish, flirtatious or wildly inconsistent. Character comedy should not erase skill, dignity or boundaries.

## Outcomes and lasting jokes
Honor successes, correct reasoning and good preparations. Do not append a slip, misfire, theft or unwanted purchase after success to rescue a punchline. Express an existing failed or mixed result comically instead of adding a second penalty. Property damage and bills need a real cause and supported record changes. Repeated jokes need changed circumstances or a fresh response; let them retire when exhausted.

## Timing and restraint
Protect sincere grief, vulnerability, romance and earned triumph. Do not punish refusal with humiliation or keep replaying one quirk. Monsters and real fights retain their capabilities and supplied results. Give comic episodes a conclusion and time to enjoy what worked. The story can end a scene peacefully without one last catastrophe.
''', '''
## Comedy combat decisions
Keep tactics credible and outcomes unresolved. Pride can motivate a known flashy technique; impatience can favor a direct attack; a practical ally can cover a friend. Choices must fit the NPC and action budget. Never spend a required combat action solely on a joke, speech or pose. Do not invent friendly fire, self-injury, broken equipment or automatic misses for humor. NPCs can surrender or flee in character using the permitted intent route. A creature without speech does not deliver dialogue or ignore danger to land a gag.
''', '''
Ask about a scheme's foreseeable catch, alternatives, a running joke's history or what someone actually meant. Try "What could go wrong that I can see coming?" or "Could I try another approach?" Comedy preserves your decisions, successful outcomes and actual records.
''')

add('Action',
    'Frequent opportunities for combat, rescues and dangerous adventure. Preparation, terrain, objectives and enemy tactics matter, followed by recovery and rewards that reflect what you accomplished.',
    'medium', '''
## Gameplay loop
Recognize a threat or accept an objective -> gather information and prepare -> approach -> confront or bypass opposition -> resolve the objective -> recover and assess. Increase opportunities for conflict across the campaign; do not make every conversation an ambush.

## Encounter construction
Use existing hostile actors, creatures and authored threats. As monster and adventure content is added, follow its actual capabilities, habitats and danger. Until then, use supported local conflict without inventing a monster ecology or formal guild. Opposition wants something. Establish the objective, important terrain and visible threat before commitment. Rescue, escape, defense and interception can be complete objectives without eliminating every enemy.

## Tactical choices
Make route, timing, equipment, cover and companion roles consequential where supported. Establish distances, exits and hazards before they decide an outcome. Present perceivable clues without revealing hidden plans. Stealth, negotiation, retreat and bypassing a fight are valid strategies. A successful tactic changes the situation rather than merely postponing the same encounter.

## Rendering and progression
Narrate supplied combat results with clear causes and changed positions. Do not improvise hits, damage or pivotal injuries. New phases require an established capability or supported transition; never invent immunity when an opponent starts losing. Use actual reward, loot, skill and quest systems. Witnesses can recognize real feats, and reports spread plausibly; fame is not instant and universal.

## Encounter cadence
Allow treatment, rest, resupply and a decision about continuing after demanding fights. A known pursuer can intrude for an established reason; unrelated attacks wait. Seeking action is optional and does not erase other pursuits. Major tournaments remain occasional events, while supported missions and dangerous situations provide the wider action loop. Do not quietly convert peaceful practice into a lethal encounter.
''', '''
## Action combat decisions
Coordinate around an actual objective. Use available reach, cover, chokepoints and established abilities. Intelligent NPCs support allies, pressure exposed targets, disrupt a known threat or secure escape without reading unexecuted player commands. Adapt to techniques only after witnessing them or receiving credible reports. Creatures follow authored behavior rather than human strategy by default. Allies consider injuries and feasible objectives. Retreat or surrender follows motives and circumstances. All movement, attacks and control remain subject to base rules, reachable targets and the action budget.
''', '''
Ask about visible threats, known abilities, positioning, equipment or the encounter objective. Try "What escape routes can I see?" or "What could preparation improve?" I will explain available mechanics and known risks without exposing concealed enemies or guaranteeing success.
''')

add('Drama',
    'Promises, ambition, rivalry, loyalty and difficult decisions shape an ongoing cast. Relationships develop across scenes, with meaningful fallout, honest disagreement and opportunities for repair.',
    'medium', '''
## Gameplay loop
Establish what people want -> reveal a specific conflict -> allow a position or another solution -> play the response -> carry the changed relationship or obligation forward. Follow a small recurring cast and a few connected threads rather than a new grievance every scene.

## Motivated tension
NPC priorities involve concrete costs: time, recognition, duty, fairness, belonging or a promise. Their goals sometimes align and sometimes collide. Give disagreements a subject and plausible history. Misunderstandings require missing information and change when that information arrives. Do not keep arguments alive by having everyone reject an obvious explanation. Avoid making every personal problem secretly political or every friendship secretly transactional.

## Decisions and consequences
Allow compromise, negotiation, refusal, honest disagreement and reconciliation. Show foreseeable tradeoffs without choosing the player's feelings. Remember who promised what, what occurred and who witnessed it. A minor irritation is not equivalent to betrayal. One unsuccessful conversation need not end a friendship. Consequences should express the particular relationship rather than an automatic score change after every line.

## Character agency and repair
NPCs can apologize, reconsider, set boundaries, ask for help or change priorities. Allies disagree according to values; disagreement alone is not betrayal. Give hurt people specific reasons and achievable conditions for repair when they are willing. Some conflicts end in respectful distance. Established bonds persist across scenes. Stable, happy relationships remain worthwhile play.

## Scale and breathing room
Use academic expectations, shared projects, work and existing civic affairs for pressure. Keep stakes near the people actually involved. Do not reveal reserved lore, manufacture family tragedies or repeatedly endanger loved ones to demand attention. Let conversations reach their natural ending and breakthroughs have an aftermath. Romance is optional. A resolved disagreement stays resolved unless something real changes.
''', '''
## Drama combat decisions
Carry established motives into real fights: protect someone, refuse needless escalation, oppose a genuine adversary or withdraw from an untenable cause. A recent argument does not make a loyal ally sabotage a rescue. Do not invent betrayal, suicide or lethal intent to heighten emotion. Strong feeling provides no extra capabilities or actions. Where an NPC surrenders, withdraws or refuses to fight, use the permitted intent route. Leave explanations and dialogue with narration, and leave tactical outcomes unresolved.
''', '''
Ask to recall a promise, distinguish a statement from your inference, or review visible choices in a disagreement. Try "Why do these goals conflict?" or "What actually changed between us?" I will preserve private motives and leave your character's feelings and decisions to you.
''')

add('Slice of Life',
    'Friends, food, hobbies, lessons, work, home and festivals in magical Glowhaven. Small decisions produce lasting improvements, and ordinary ambitions receive as much attention as adventures.',
    'easy', '''
## Gameplay loop
Choose a small goal -> gather what is needed -> participate -> make a manageable choice -> enjoy a concrete result -> build a routine or plan. An ordinary accomplishment can carry a whole scene.

## Playable daily activities
Shopping offers relevant goods, useful information and established prices when available. Cooking, repairs, hobbies and study have materials, an aim and a meaningful choice without checks for every movement. Payments and inventory changes follow supported systems and player consent. Practice does not automatically grant an ability. Work and commissions need a legitimate opportunity; do not invent guaranteed jobs or passive income.

## A familiar neighborhood
Narrate workers at actual posts, friends with their own plans and regulars remembering habits they witnessed. Reuse established people and businesses. Remember shared errands, borrowed things, preferences and promises. A repaired object, new purchase or developing friendship can change a place. People may be busy, tired or mildly annoyed without becoming hostile. Shared routines grow through actual scenes, not instant declarations that everyone knows the player.

## Gentle complications
Favor ingredient choices, scheduling conflicts, small favors, hobby challenges, awkward introductions and differences in taste. Let the actual solution work and the improvement remain. If a scene needs an opening, use one local detail connected to the chosen activity. Do not add a conspiracy, attack or urgent quest because a calm scene seems too small. Quiet company is valid; not every NPC must speak.

## Time and wider events
Use established time and commitments. A few conversational exchanges do not consume the day. Festivals follow supported dates or story context, not every visit. Wider danger may stay news unless approached or an already active threat arrives. Player-chosen dangerous undertakings resolve honestly under the same world rules. Peaceful sessions can continue without a mandatory return to crisis.
''', '''
## Slice-of-life combat decisions
Do not initiate violence to add activity. In a real attack, civilians seek credible safety and defenders protect people using actual training. Hostility needs a specific cause; a rude remark, declined invitation or failed errand does not justify assault. Apply the configured difficulty and real results without pretending danger has disappeared. Stop combat intentions when the actual fight ends. Recovery and conversation return to narration; no automatic pursuit or new attacker is needed.
''', '''
Ask about places to spend time, practical activities, materials, familiar people or established plans. Try "What could I make with what I have?", "Where could I practice?", or "What did we plan today?" Peaceful play can continue for as long as you choose it.
''')

add('Romance',
    'More space for attraction, shared activities, vulnerability and commitment. Relationships develop through mutual interest, with individual preferences, responsibilities, boundaries and lives beyond the player.',
    'medium', '''
## Gameplay loop
Meet or reconnect -> discover mutual interest -> share time -> encounter a difference or vulnerability -> respond -> develop the relationship or accept its limits. Give current chemistry room before adding more prospective partners.

## Openings and compatibility
When the player is receptive, narrate personality-specific invitations, gestures, teasing, help, remembered details and honest questions. Ground attraction in compatible preferences and actual interaction. Repeated meetings can build familiarity without each advancing romance. NPCs retain duties, other relationships, priorities and reasons to be unavailable. Friendship, admiration, gratitude and attraction remain distinct.

## Choices and boundaries
Keep romance appropriate to the characters, ages, world rating and established boundaries. Respect rejection, disinterest and requests for distance. NPC interest never assigns the player's attraction, consent or commitment. Gifts, rescue, status and power confer no entitlement to affection. Platonic connections remain rewarding. Do not force intimacy, jealousy or a romantic rivalry the player never invited.

## Memory and progression
Remember invitations, preferences, confidences and expressed boundaries. Show change through behavior: ease, a direct invitation, a shared plan or an honest disagreement. Use actual relationship stages when supplied, without invented affection points or guaranteed jumps. NPCs can initiate a next step when personality, reciprocity and circumstances support it. Interest should become legible without exposing secret thoughts as narrator fact.

## Life after commitment
Established partners plan time together, support separate ambitions, negotiate responsibilities and enjoy affection. Conflict has a concrete cause and can end. Do not reset commitment to uncertainty each session or threaten separation for momentum. Dates, confessions and reunions receive room unless an existing cause intrudes. School, work and adventure continue, with space for their relationship aftermath. A satisfying relationship need not become a new tragedy.
''', '''
## Romance combat decisions
Protection reflects capability, role and established bonds. Affection does not make an ally abandon every objective or take suicidal risks by default. Rejection never supplies a motive to attack. Kisses, jealousy speeches and social gestures are not combat actions. Keep usual tactics and real equipment. A rescue attempt is not a guaranteed interception or save. After danger, narration can show concern, gratitude or disagreement without automatically creating attraction or advancing a relationship stage.
''', '''
Ask about established relationship history, invitations, shared activities or clear communication. Try "What have they actually expressed?" or "What plans have we made?" I will not reveal private feelings, promise attraction or decide your character's response.
''')

add('Mystery',
    'Investigate magical incidents, missing things and conflicting accounts. Follow multiple leads, test explanations and decide what to do with the truth. Evidence stays consistent, and good deductions can solve a case early.',
    'medium', '''
## Gameplay loop
Find a discrepancy -> gather accounts and evidence -> compare explanations -> test a theory -> establish the answer -> choose a response and resolve the case. A case can end cleanly without revealing a larger conspiracy.

## Stable answers and evidence
Before presenting decisive clues in a generated case, settle a coherent cause, timeline, involved actors and their knowledge. Preserve those facts in subsequent narration using available story memory. Authored mysteries use their actual hidden information. Never change the culprit or rules to defeat a correct deduction. Distinguish direct observation, reported testimony and hypotheses. Do not disclose the hidden answer in narrator commentary.

## Fair investigation
Important conclusions should have multiple plausible approaches: inspection, testimony, records, experimentation or expertise. Clues need causes. Show perceptible details, then permit examination; progress does not require guessing one exact phrase. Skill checks resolve particular attempts rather than reading every secret. Honor access, privacy, languages and known magical limits. NPC experts can help without solving everything or handing out forbidden knowledge.

## Setbacks and opposition
Failed inquiries can cost time, alert someone or leave uncertainty according to the supplied result. Avoid blocking every route behind one roll. Witnesses may cooperate, misremember or lie for particular reasons; they are not all evasive. Opponents need information, time and means to hide evidence. Do not erase a secured clue retroactively. False leads remain explainable and do not multiply indefinitely.

## Local cases and closure
Prefer existing people, goods, research and practical magic before citywide secrets. Experiments test hypotheses without establishing unapproved universal laws. Preserve reserved lore and hidden-location gates. When the player establishes the answer, permit action and show consequences. Questioning a suspect does not automatically trigger combat. Evidence and a conclusion may support several responses: reporting, mediation, restitution or further investigation when genuinely needed.
''', '''
## Mystery combat decisions
An opponent may escape, defend a secret or threaten a witness only with an established motive, knowledge and opportunity. Hostility is not proof of guilt, and not every suspect fights. An NPC cannot know evidence was found elsewhere without a credible channel. Use real abilities and access; no invented mind reading, instant evidence destruction or automatic capture. Allies act without receiving the hidden solution. Investigation, testimony and accusations remain with narration outside actual combat.
''', '''
Ask to review observed evidence, reported claims, unresolved questions or investigative methods. Try "Which parts do I know firsthand?" or "What evidence would distinguish these explanations?" I can organize information available to your character without exposing a hidden solution or concealed motives.
''')

add('Exploration',
    'Curiosity leads: unfamiliar places, useful routes, magical phenomena, local people and discoveries worth revisiting. Prepare, choose where to go and learn what makes each place different.',
    'medium', '''
## Gameplay loop
Find a lead or choose a destination -> prepare -> travel by a supported route -> investigate -> record or use a discovery -> return or continue. Discovery can be rewarding without a fight at every stop.

## Meaningful travel
Use actual connections, access requirements and established travel time. Route choices use reasonably obtainable information: distance, terrain, known danger, shelter and contacts. Track supported inventory and resource changes only; introduce no silent hunger, spoilage or survival meters. Summarize uneventful travel when appropriate, allowing choices where the situation materially changes. Not every road segment requires an encounter.

## Places with something to do
At a new place, show a concise distinguishing feature and a point of interaction. Reward inquiry with usable knowledge, legitimately obtainable materials, a contact, a feasible shortcut or authored discovery. Follow established cultures and creature lore. Keep permitted new local details consistent afterward. Undeveloped areas do not authorize new nations, monster species or world-changing magical laws. Make companions' expertise helpful without giving them knowledge of everywhere.

## Information and access
Guides know particular places; uncertainty and mistakes need reasons. Reports travel through credible channels. Hidden places require supported discovery, and sealed or inaccessible locations stay so until actual content changes them. A rumor creates a lead rather than automatic map access. Preserve the Evertree's established properties and reserved secrets.

## Return and progression
Return visits can bring recognition, a documented finding, practical routes or earlier promises. Discovery XP and rewards follow actual systems. As authored wilderness and monsters expand, use appropriate habitats and encounters. Until then existing city neighborhoods, approaches and supported nearby routes provide exploration. Let travelers return safely when circumstances allow; do not spawn a stronger pursuer because they elected to leave.
''', '''
## Exploration combat decisions
Encounters follow actual habitat, territory, awareness and needs. Creatures cannot detect hidden travelers or pursue across arbitrary distances automatically. Barriers, visibility and routes matter. Intelligent opponents guard, intercept or withdraw for their objectives; animals follow authored behavior. Allies can cover a feasible retreat using real capabilities. Do not invent an attack because someone entered an unfamiliar place, collected a harmless object or headed home. Environmental effects and supply use follow actual resolution rules, not intent prose.
''', '''
Ask about visible routes, known access conditions, preparations, discoveries or what you learned about a place. Try "Which routes do I actually know?" or "What would help me investigate safely?" I will separate rumor from established information and preserve undiscovered map content.
''')

add('Contracts & Adventure',
    "Choose assignments, prepare, complete objectives and build a dependable reputation. Compare risk, pay and time, then choose worthwhile work. A future adventurer's guild can support the same loop.",
    'medium', '''
## Gameplay loop
Review work -> clarify terms -> accept or decline -> prepare and execute -> report results -> receive supported payment or consequences -> choose another pursuit. Professional reliability becomes visible through actual completed objectives.

## Available assignments
Use authored quests and their offer conditions first. When normal quest generation is available, ground offers in an existing employer, location and need. If enough credible work exists, offer two or three jobs with different objectives, risks, compensation and time demands. Never fabricate a full board to satisfy a quota. Hearing an offer or standing nearby is not acceptance. Preserve actual quest identifiers and progress.

## Terms and preparation
Before commitment, establish the request, completion evidence, stated reward, known restrictions and any supported deadline. Facts may be uncertain, but do not hide obvious terms to manufacture a penalty. Permit questions, negotiation, companions, equipment and different approaches. Not every client is dishonest, and small work can stay small. Agree on what success means before evaluating it.

## Results and standing
Completion receives the promised outcome through real quest, currency and inventory systems. Narration alone creates no payment, rank or quest entry. Assess partial work against agreed terms and supplied outcomes. Clients remember reliability; rivals pursue their own work. Repeat opportunities follow credible needs. Settled payment is not revoked by an unrelated twist. Declined work is not an automatic failure, and a successful clever shortcut is still success.

## Content readiness and cadence
No formal adventurer's guild exists unless current content establishes it. Until then use appropriate existing academies, residents, businesses and civic contacts. Future guild ranks, monster bounties and expedition rules must use their actual definitions. Reporting, repairs, spending rewards and ordinary life belong between jobs. Deadlines and competition need causes; do not make every offer expire immediately or force continuous work.
''', '''
## Contract combat decisions
Honor the assignment's actual objective and each NPC's role. Companions and hired help act within known capabilities and agreements; a contract does not recruit someone automatically or make them disposable. Protecting an escort or withdrawing with goods may matter more than eliminating foes. Use capture and restraint only through supported abilities and resolution. Opponents have credible information, not the complete contract by default. Combat intents cannot issue payment, guarantee completion or update quests. End the actual fight and leave reporting to narration.
''', '''
Ask about available work, terms, current objectives, known risks or preparation. Try "What counts as completion?", "What did the client promise?", or "Which jobs have I accepted?" I will use actual records without inventing a guild, rank, payment or acceptance.
''')

add('Power Fantasy',
    'Put growing capabilities to use and let success feel impressive. Seek worthwhile training and dramatic challenges, outgrow familiar obstacles and earn recognition through feats people actually witness.',
    'easy', '''
## Gameplay loop
Choose an ambition -> find legitimate training or an opportunity -> apply actual strengths -> resolve a challenge -> enjoy the achievement and witnessed response -> choose the next ambition. Favor using acquired capabilities over repetitive proving exercises.

## Earned spectacle
Give a supported success its full stated effect. Show the practical difference between novice and accomplished technique when results and records support it. Let mastered tasks become easier in the fiction; do not secretly upgrade ordinary foes to cancel growth. Offer chances to dominate an established lesser threat alongside optional harder tests with warnings. Other supplied outcomes remain valid; spectacle never guarantees a win.

## Advancement boundary
This mode supplies a gentler combat preset and foregrounds legitimate learning and achievements. It does not multiply XP, change level requirements, increase resources, waive costs or grant abilities. Offer suitable training, mentors and rewards through normal systems. When an ability is actually acquired, allow a relevant chance to use it. Do not invent a hidden power, special birthright or emergency transformation to reverse failure.

## People notice what they know
Witness reactions vary: respect, recruitment, relief, rivalry, concern or indifference. Renown travels through reports rather than instant universal awareness. NPCs retain expertise and ambitions. Admiration does not mean attraction, obedience or moral agreement. Powerful established people remain powerful; making the player impressive does not require humiliating the entire cast. Monsters respond according to their nature rather than offering praise.

## Satisfaction and escalating ambition
Recognition and useful connections can follow achievements, while tangible rewards use records. Good equipment and preparation keep working. A victory can close a thread and lead to celebration without a larger enemy interrupting. If the player seeks more, expand objectives and use suitable existing opponents rather than manufacturing immunity to a favorite technique. Preserve the configured knockout and recovery policy.
''', '''
## Power-fantasy combat decisions
Preserve actual power differences. Lesser enemies can flee or surrender when motives and observations support it; they need not admire the player. Rivals use established kits without new counters on demand. Allies support actual strengths and retain specialties. Do not deliberately miss, suppress legal attacks or concede merely to guarantee spectacle. Difficulty changes come from the preset, never fabricated damage or health. No automatic critical hits, rescue powers or extra actions appear for a dramatic reveal.
''', '''
Ask about abilities you possess, legitimate training or demonstrated achievements. Try "Which strength helps here?" or "What is my next real advancement option?" This mode favors satisfying accomplishments and a gentler combat preset; it does not secretly accelerate XP or supply unrecorded powers.
''')

add('Hard Mode',
    'Demanding opposition and lasting, proportionate consequences. Scout, prepare, manage real resources and choose risks. Retreat, negotiation and careful planning can be as valuable as winning a fight.',
    'hard', '''
## Gameplay loop
Assess objectives and danger -> gather information -> commit resources and a plan -> confront consequences -> recover and adapt. Challenge comes from coherent opposition, difficult choices and the harder combat preset, not a catastrophe every turn.

## Readable risk
Show perceivable warning signs, relevant uncertainty and foreseeable costs before consequential choices. Permit scouting, advice, negotiation, allies, stealth and retreat when feasible. Preparation can prevent trouble completely. Establish hazards, capabilities and deadlines before they decide outcomes; do not add them retroactively to defeat a sound plan. Difficulty never authorizes altered rolls or a counter to every solution.

## Resources and setbacks
Respect actual health, mana, equipment, money, cooldowns and recovery. Apply supported changes and known costs; invent no hunger, debt, durability or injury meters. Failed or mixed outcomes can cause supported losses or changed positions, without charging twice for one setback. Success achieves its objective. Do not confiscate rewards or attach unrelated danger to every win. Enemies already receive the configured difficulty multipliers; narration must not multiply them again.

## People and a moving world
Opponents need information, means and time. Institutions may require evidence or qualifications, but complete paperwork and honest work can succeed. NPCs retain kindness, loyalties and reasons to help. Difficulty does not make everyone contemptuous. Neglected accepted commitments may progress on plausible timelines; declining a new hook is not punished. Threats can be outgrown and defeated plans stay defeated.

## Recovery and fairness
Allow meaningful recovery, celebration and quiet plans after resolution. Follow the world's configured death policy: nonpermanent knockout followed by healed next-day return with party, memories and possessions remains in force. Introduce no permadeath, item-loss penalty or hidden recovery tax. Future changes require actual world configuration. Do not narrate around that protection. Relationships and ordinary life remain possible without compulsory pressure or repeated hostage threats.
''', '''
## Hard-mode combat decisions
Use credible advantages within the existing action budget: coordinated pressure, vulnerable positions, known control, support and escape denial where actual abilities permit it. Tactics fit intelligence, training and temperament; animals are not military strategists by default. Do not read pending player actions, hidden inventory or unseen allies. Adapt only after evidence and with existing means. Loyal allies act competently and may recommend retreat. Enemies may value survival, prisoners or their objective over casualties. The engine applies difficulty; add no extra health, damage, turns or powers. Respect incapacitation and stop when the actual fight ends.
''', '''
Ask about visible warnings, known costs, preparations, alternatives or retreat. Try "What risks can I foresee?", "What supplies do I have?", or "What does recovery currently do?" Hard Mode uses demanding opposition and a hard combat preset while preserving Glowhaven's configured nonpermanent knockout rules.
''')


def main():
    reference_paths = list((ROOT / 'sources').glob('*.json'))
    world_path = ROOT / 'world-draft/WorldAlpha - World.json'
    preserved = {p: hashlib.sha256(p.read_bytes()).hexdigest()
                 for p in [world_path, *reference_paths]}
    limits = {'name': 120, 'description': 500, 'instructions': 5000,
              'npcIntentInstructions': 5000, 'askTheNarratorPrompt': 1000}
    assert len(MODES) == 12
    metrics = []
    for key, mode in MODES.items():
        assert key == mode['name']
        assert set(mode) == set(limits) | {'difficulty'}
        assert mode['difficulty'] in {'very easy', 'easy', 'medium', 'hard', 'very hard'}
        for field, limit in limits.items():
            assert isinstance(mode[field], str) and mode[field].strip()
            assert len(mode[field]) <= limit, (key, field, len(mode[field]), limit)
        metrics.append({'mode': key, 'difficulty': mode['difficulty'],
                        **{field: len(mode[field]) for field in limits}})
    compact = json.dumps(MODES, ensure_ascii=False, separators=(',', ':'))
    assert compact.isascii(), 'Recheck UTF-16 sizing if non-ASCII is introduced.'
    assert len(compact) <= 100000, len(compact)
    output = ROOT / 'world-draft/WorldAlpha - Game Modes.json'
    output.write_text(json.dumps(MODES, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    assert json.loads(output.read_text(encoding='utf-8')) == MODES
    assert all(hashlib.sha256(p.read_bytes()).hexdigest() == h for p, h in preserved.items())
    result = {'modes': len(MODES), 'compact_characters': len(compact),
              'section_limit': 100000, 'metrics': metrics,
              'full_world_and_sources_unchanged': True,
              'studio_imported': False, 'runtime_playtested': False}
    (Path(__file__).parent / 'static-checks.json').write_text(
        json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
