# NPC Story and Quest Proposals

**Status: proposals for review, not adopted canon or implemented quests.** Prepared 27 October 2026 from the current standalone WorldAlpha NPC roster, Locations, World Lore, Character Creation Format, and Academy NPC Placement Report. The roster contains 68 academy NPCs: 17 per academy, comprising an Archon, a headmaster, three teachers, and twelve students each.

No NPC records, location records, quest JSON, triggers, or story starts were changed. No portraits were commissioned. These are narrative design proposals; field names and engine behavior are not being specified. The complete-world export currently has empty `quests`, `narrativeEvents`, and `triggers` collections. Its embedded NPC snapshot is older than the standalone roster used here.

## Recommendation

Develop recurring situations around existing motives before expanding the cast substantially. The roster already supplies conflicts, friends, rivals, teachers, ordinary interests, and places to meet. The missing piece is a sequence of situations in which those things matter to the player's choices.

Start with twelve academy anchors, three per academy:

- Phoenix Wing Academy: **Riko Umezawa, Kokona Hanamori, Miyabi Tsukishiro.** One social conflict can involve the clique; a separate practical project brings in Hinae Komori and the city.
- Gryffin Tail Academy: **Satoru Kanda, Renji Hanabusa, Chiharu Arai.** These offer practical learning, academic dishonesty, and public organizing, with quite different activities and moral choices.
- Dragon Hoard Academy: **Mai Kajiwara, Retsu Arakida, Suzune Mikazuki.** These offer craft and work, accountability for bullying, and cooperative field problem-solving.
- Hydra Head Academy: **Tamaki Kiryū, Kana Fujimoto, Homura Hibino.** These offer tactical disagreement, teaching competence, and ambitious practical spectacle. Kana Fujimoto provides a junior instructor's perspective alongside the student stories.

Develop Ranka Kagari's accountability arc and Gen'ichirō Mizuhara's institutional campaign after players have met affected students. Genzō Iwakura is an excellent additional personal arc. Let Asuka Tsurugi, Shiori Minase, Nemu Usami, Nahlah Qamar, and the comic ensembles provide recurring companionship alongside the heavier plots.

An anchor gets a short chain with several outcomes. A supporting NPC gets an active role and a smaller follow-up inside someone else's chain. A light NPC gets worthwhile activities, preferences, and continuity without being assigned a crisis or secret tragedy.

## New major characters: six candidate archetypes

These are unnamed concepts, not complete character cards. Their roles, histories, and quest incidents are proposed additions. No title, rank, noble portfolio, country, or formal legal procedure is established by this document. Start with the first three; reserve the others until a clear gap remains.

### 1. The courteous elite officer who expects an inconvenient answer

**Archetype:** The principled professional whose loyalty becomes harder to practice than obedience. Exceptionally capable in their field, socially patient, and initially more interested in the player's observations than combat potential.

**What they want:** A genuinely reliable account of an incident involving an influential household. They believe official channels can work and have invested their identity in that belief.

**Contradiction:** They welcome criticism in principle, then hesitate when following it would embarrass someone they have trusted for years. Avoid making them automatically corrupt or secretly correct about everything.

**Possible questline — The Account That Changed:** At an ordinary delivery dispute, the player notices that a witness's account has been shortened in a way that changes its meaning. The officer asks the witness's permission to revisit it. Accompany interviews, retrace a delivery, and compare the original account with the summary. Decide whether to submit a complete account through the officer, let the witness approach another appropriate official, or step away from an inquiry the witness no longer wants to pursue. Direct public disclosure is possible only if the player actually obtains the information and accepts its consequences.

**Follow-through:** The officer may correct their own earlier judgment, lose a trusted contact, or choose institutional loyalty over the player's recommendation. The witness decides what they are willing to say. A student helps with accessible local evidence; they are not casually handed confidential-service authority. Later, the officer remembers whether the player respected witnesses or treated them as useful evidence.

**Why add them:** Connects ordinary city encounters to the elite force and government without requiring every plot to begin at the palace. Nao Tsukuda, Tetsuya Ōmi, and local carriers can remain important within their own roles.

### 2. The generous patron who wants to own the outcome

**Archetype:** The helpful power broker. Charming, competent, and sincerely willing to pay for improvements—provided the terms secure their future influence.

**What they want:** A useful magical product or public project that succeeds under an exclusive agreement. They see control as the price of accepting financial risk.

**Contradiction:** Their money provides real opportunities, but their preferred terms restrict other people's future choices. They can be negotiated with; generosity is neither proof of innocence nor a disguise for pure evil.

**Possible questline — A Gift with Terms:** A student prototype wins their attention. The player helps demonstrate it, speaks to prospective users and workshops, and compares what different funding arrangements would permit. Accept exclusivity for dependable funding and distribution; seek a smaller independent launch with slower development; or negotiate a narrower agreement that gives up some support. Do not offer a consequence-free option that grants all benefits.

**Follow-through:** A funded workshop becomes available, but later prototypes and credit may become disputed. An independent project keeps control but must scale down its first release. The patron continues pursuing promising work elsewhere if refused.

**Why add them:** Makes contracts, patronage, and the enchanted-goods economy playable. Mai Kajiwara, Shunpei Makino, and Hanae Goldbarrow provide natural connections. This differs from Gen'ichirō Mizuhara's control over educational recognition: the patron's leverage concerns ownership, production, and access to money.

### 3. The former prodigy who left on purpose

**Archetype:** The disillusioned independent mentor who has built a worthwhile life outside the prestigious career everyone expected.

**What they want:** A small practical teaching project to succeed without being swallowed by an academy or by their own old reputation.

**Contradiction:** They defend students' freedom, yet dismiss institutional education so broadly that they can reproduce the same contempt they resent.

**Possible questline — A Lesson Worth Keeping:** Hinae Komori asks for help adapting one useful technique for home use. The player accompanies trials, listens to residents' existing methods, and helps revise the lesson. An academy offers resources and recognition under proposed supervision. Choose to pursue affiliation, remain independent with fewer resources, or create a small cooperative arrangement with explicitly divided responsibilities. The former prodigy must decide what they can accept; the player can disagree or join a different approach.

**Follow-through:** Residents retain the method they actually helped test. The mentor may acknowledge that a formal teacher contributed something useful, or become more entrenched if the process is handled contemptuously. No academy's exclusive civic duty is assigned, and the lessons do not automatically bypass future accreditation debates.

**Why add them:** Gives the player a credible alternative model of adulthood and learning. They need not be stronger than the Archons, and leaving academia is not a failure waiting to be reversed.

### 4. The cheerful investigator who sells truthful information

**Archetype:** A delightful, unreliable ally whose evidence is often accurate and whose loyalties are negotiable.

**What they want:** To profit from knowing what other people need to know. They consider disclosure a service, even when someone else bears its cost.

**Possible questline — The Price of a Correction:** Start with a minor false accusation involving a student commission. Follow purchases, compare accounts, and discover that a genuine wrong was committed by a sympathetic person. Decide what to verify, whom to inform, and whether to publish evidence involving someone who never agreed to become part of a story. The investigator may sell a narrower verified account even after the player declines a more damaging one.

**Follow-through:** A correction can clear one person while exposing another's private problem. A protected source may later cooperate; a betrayed source may refuse. Their transactions remain visible enough for players to judge them rather than being an endless stream of unknowable betrayals.

**Why add them:** Supports investigation and political play without making all truth flow through authorities. Keep them distinct from Sena Moriyama's social exclusions and Issei Kurose's deliberate sabotage.

### 5. The celebrated contender with an ordinary household to support

**Archetype:** The formidable public rival who treats competition as skilled work, with people and obligations beyond the arena.

**What they want:** A dependable competitive income and control of how their public image is used.

**Possible questline — The Bout They Can Afford:** Accompany preparations for a proposed exhibition. Test equipment with actual craftspeople, practice, and negotiate conflicting commitments. A lucrative private engagement clashes with a less profitable public event they previously promised to support. Help rearrange the work, back one commitment at a real cost to the other, or refuse to manage their calendar. The contender makes the final professional choice and still competes independently.

**Follow-through:** A sponsor relationship, a community promise, and the contender's future availability change. Win or lose, a later meal or training invitation reflects how the player treated the person behind the performance. No fixed arena ladder, prize system, or automatic entry rule is assumed.

**Why add them:** A recurring rival can remain friendly and formidable without becoming an enemy, romantic prize, or quest dispenser. Tomoe Enokida offers an existing bridge into the venue.

### 6. The charming former fraudster whose victims still exist

**Archetype:** The useful rogue who wants a second chance but resents the price of making amends.

**What they want:** A legitimate livelihood repairing or assessing magical goods. They possess relevant skills acquired through earlier dishonest work.

**Possible questline — Every Piece Accounted For:** A cheap enchanted item fails during an ordinary job. Trace its repair history, identify a group of past customers, and accompany a voluntary demonstration of the defects. The former fraudster asks the player to support a business restart that could fund repayments. Choose whether to recommend them under clear terms, assist only with restitution, or tell prospective partners why trust is not yet justified. Former victims need not forgive or participate.

**Follow-through:** Some customers accept repairs, some demand repayment, and others decline further contact. Rebuilding income and accountability compete for limited resources. The character may improve, cut corners, or leave the arrangement depending on their choices and the player's involvement.

**Why add them:** Creates a major character through relationships and consequences rather than power level. A proposed conviction or sentence needs separate authoring; do not assume they escaped Wraith Island Prison or define prison law through this pitch.

## Existing characters already suited to major roles

| NPC | Major role worth developing | Keep intact |
|---|---|---|
| Ilyra Stillglass | An aging ruler balancing continuity, privacy, and succession. | No convenient cure, invented academy origin, automatic abdication, or player-appointed successor. |
| Gen'ichirō Mizuhara | A powerful institutional antagonist whose apparently neutral standards hide prejudice and control. | His severity is not secretly benevolent; challenging him requires evidence, alliances, and institutional leverage. |
| Issei Kurose | A student-level political operator who can become a persistent ally, competitor, or antagonist. | Competence and sabotage can coexist. Cooperation does not guarantee redemption or friendship. |
| Reika Saionji | A patron of independent research who must choose how to share real decision-making power. | Her shyness is not incompetence, and the proposed fund is not yet operating merely because she wants it. |
| Akane Todo | A protector and researcher whose judgment deserves attention before danger begins. | Give her research, leadership, cooking, and independent initiatives alongside combat. |
| Tōru Shizunami | A capable leader who wants a life he has not permitted himself to choose. | His talent is real; a student should not single-handedly repair the institution so he can leave. |
| Ranka Kagari | A dangerous, intermittently useful teacher facing consequences for concealed harm. | Gambling and comic behavior do not excuse injured students or falsified records. |

## Full academy review: all 68 NPCs

**Anchor** = first twelve priorities above. **Later arc** = substantial chain once relationships exist. **Supporting** = active part in shared quests plus a modest individual follow-up. **Light** = retain a stable personality and provide enjoyable activities; do not manufacture a crisis. Conflicts described as existing are drawn from the roster; all incidents, offers, choices, and outcomes below are proposals.

### Phoenix Wing Academy

| NPC / scope | Personal conflict to activate or preserve | Proposed side quest and player involvement |
|---|---|---|
| Akane Todo — Later arc | Her research is overlooked while others assume she will personally confront every threat. | **Before the Alarm:** accompany a modest field survey and interview workers about conflicting observations. Compare explanations and recommend practical precautions. Reliable observations improve a later training exercise; flashy but unsupported claims waste time. She acts on the assessment and credits useful disagreement. |
| Kōhei Sanada — Supporting | His public forfeit and private judgment about injury become relevant again; he need not reveal his history to justify a safe decision. | **The Unfinished Bout:** assist with an exhibition where a participant conceals an injury. Observe practice, ask questions, and support a withdrawal, adjusted demonstration, or honest report. A later conversation can reveal his past if earned, with his consent. The injured participant's future conduct matters more than restoring his heroic reputation. |
| Ritsu Kurogane — Supporting | Teaching control clashes with a student copying only her spectacular movement. | **Learn to Stop:** practice braking and positioning with Takeru Akabane, then revise the drill for a partner who moves differently. Choose whether to chase a fast demonstration or show consistent control. She changes future lessons in response; no teacher/student romance is implied. |
| Haruki Saitō — Light | Preserve a contented ordinary life and discreet care for students. He does not need a tragic past or secret greatness. | **The Quiet Practice Match:** help arrange a low-audience rematch for a struggling participant. Scout a suitable time, practice one useful adjustment, and decide together whether feedback stays private. Later he asks about that participant's progress and remembers the player's conduct. |
| Ranka Kagari — Later arc | Convenience, gambling income, and experimental access conflict with responsibility for real concealed harm. | **The Results She Changed:** assist a student seeking an accurate account of a potion incident. Collect voluntarily shared notes, compare versions, and choose whether to help make a formal report, demand a documented correction, or refuse her request to conceal it. Medical care comes first. A private fix does not erase the injury; victims can continue pursuing accountability. |
| Yūma Kurobane — Supporting | He fears being ordinary and uninteresting without his persona. | **A Sovereign's Small Errand:** jointly stage a clearly fictional treasure game for willing participants, with Nemu Usami helping choose harmless tricks. During an ordinary setback, practical care matters more than his script. Support theatrical fun or ask for a plain conversation; neither route reveals real sealed powers. He later risks an honest invitation. |
| Kokona Hanamori — Anchor | Being admired as kind competes with choosing helpful action when it earns no admiration. Lack of emotional empathy is not the wrongdoing. | **No One Watching:** help with an unglamorous task after a classmate has been hurt by the clique's behavior. Ask the affected person what help they want; share work, respect a refusal, and decide whether to back a public image campaign or quiet restitution. Kokona Hanamori can learn deliberate, reliable care without acquiring emotional empathy or confessing to the whole school. |
| Miu Shinohara — Supporting | Fear of irrelevance provokes cruelty toward people who attract attention without her approval. | **Someone Else's Applause:** co-organize a student presentation where another participant deserves the spotlight. Miu Shinohara can help secure the event or sabotage its social atmosphere. The player can negotiate a real role, challenge exclusion, or decline involvement. Later invitations reflect actual conduct; an impressive performance does not settle harm to classmates. |
| Riko Umezawa — Anchor | Private guilt conflicts with the public approval she seeks from the clique. | **The Second Invitation:** someone is excluded after a cruel joke. Help her arrange a repair the affected person actually wants, then encounter a second moment where silence has a visible cost. Back a public correction, a private apology with a practical boundary, or leave her to choose. The affected person may reject the apology; real progress is whether she behaves differently next time. |
| Sena Moriyama — Supporting | Feeling indispensable depends on managing hierarchy through deniable exclusions. | **A Place on the List:** help prepare invitations, then discover someone was deliberately omitted. Compare the stated criteria with the actual list and choose whether to challenge her openly, help create an independent gathering, or cooperate for access. She responds by sharing control, defending the exclusion, or seeking a different ally. Do not turn her into an omniscient blackmailer. |
| Takeru Akabane — Supporting | Admiration for Ritsu Kurogane makes developing his own style feel disloyal. | **A Different Foot Forward:** join controlled trials of his movement with different routes and teammates. Encourage an original solution or a polished imitation; his later duel behavior should reflect what he actually practiced. Ritsu Kurogane can respect adaptation. Recognition comes from skill and judgment, not a flattering speech. |
| Miyabi Tsukishiro — Anchor | She resents being used as a family asset while treating commoners' judgment as inherently inferior. | **A Useful Introduction:** a proposed practical project gives her access to a valuable contact through Hinae Komori. Work alongside residents and negotiate credit, scope, and leadership. Accept useful support with conditions, insist on resident control, or withdraw. She can contribute while remaining prejudiced; gradual respect requires repeated choices. Hinae Komori and residents are not props for her redemption. |
| Kōta Arakawa — Supporting | He equates rest with surrender and hides fatigue or injury. | **A Day Without a Duel:** help him prepare for a practice match using observation, planning, and recovery rather than extra sparring. If he insists on a risky match, the player can withdraw support or seek appropriate help. The outcome changes future training habits gradually; injury is never magically made harmless to reward persistence. |
| Sōma Kisaragi — Supporting | Others' expectations of his talent conflict with choosing his own purpose and acknowledging effort. | **No Audience:** he asks for an off-hours practice partner without wanting a public narrative about it. Test a technique with a clear weakness and decide what, if anything, he is ready to share with Kōta Arakawa. An honest rivalry or private collaboration follows; secrecy is not automatically cured by exposing him. |
| Hinae Komori — Supporting | Fear of seeming unsophisticated competes with bringing useful knowledge home. | **Something Worth Taking Home:** visit Pebbletown, listen to a concrete local problem, and test a small adaptation with residents and Momo Karube. Choose an affordable, maintainable solution over an impressive demonstration if the evidence supports it. A failed trial produces a revised lesson, not a ruined village. She can later invite the player back to see what people kept using. |
| Shiori Minase — Light | She wants connection without compulsory performance or public exposure of her conversation notes. | **An Invitation with an Exit:** co-plan a small study outing or puzzle session, agree on its size and noise, and leave room to stop. The player can enjoy quiet company, ask about a shared subject, or decline gracefully. Later she initiates a specific invitation herself. Success does not make her extroverted. |
| Nemu Usami — Supporting | She fears being valued only as entertainment and hides genuine limits on stamina. | **A Prank That Can Rest:** plan a harmless, opt-in puzzle trail with short routes and places to stop. The player can share physical setup, respect a request to end early, or propose a quieter version. She later includes the player in a joke without feeling obliged to perform. Do not cure her stamina or reveal hidden fighting prowess. |

### Gryffin Tail Academy

| NPC / scope | Personal conflict to activate or preserve | Proposed side quest and player involvement |
|---|---|---|
| Gen'ichirō Mizuhara — Later arc | His proposed curricular monopoly and prejudice conflict with others' education and independence. This is an external struggle as well as a personal agenda. | **The Same Mistake:** compare assessments willingly shared by students, repeat equivalent demonstrations, and establish where criteria changed. Decide how to protect sources and whom to approach with a careful case. One proven discrepancy can win a review or ally, not instantly remove an Archon or overturn kingdom policy. He can offer conditional support, retaliate through existing discretion, or revise his tactics. |
| Norio Shibata — Supporting | Correctly applying a rule may preserve an unfair result, while challenging policy risks his comfortable career. | **Correctly Rejected:** help a student whose application is accurate but rejected under a proposed eligibility condition. Reconstruct the process and help present an appeal or request a policy exception. Norio Shibata can clarify the record without supporting reform; the player decides whether that limited help is enough. Do not pretend every unfair outcome is a clerical error. |
| Ririka Kujō — Supporting | Hunger for elite recognition competes with honest credit and effective teaching. | **The Demonstration after the Demonstration:** assist a polished presentation, then help classmates reproduce it without her intuitive shortcuts. Decide whether to coach her privately, document missing steps, or let spectacle carry the event. Better teaching can earn lasting student respect; an embellished romantic history need not be exposed to achieve it. |
| Kei Aoki — Light | Preserve competence and low ambition. He can choose a limited professional commitment without becoming secretly passionate about everything. | **One Precise Question:** investigate an ordinary botanical problem, collect usable observations, and bring him a genuinely precise question. Negotiate a bounded field visit rather than solving his personality. He answers seriously, returns to his routines, and may later recognize that the player respects his time. |
| Sōichirō Takamine — Later arc | He wants intellectual freedom without others controlling an unpublished body of work. | **Permission to Read:** assist one harmless optical trial only after he chooses what to share. Help test reproducibility, agree attribution, and discuss an invitation to disclose more. Support limited publication, continued privacy, or a narrower collaboration. Personal trust never grants unrestricted ownership of his notes. |
| Satoru Kanda — Anchor | He wants theoretical work valued while embarrassment makes practical collaboration difficult. | **Proof in Practice:** partner with Maki Ogasawara and Fumito Sakurai to test a concise explanation against real casting. Alternate observing, explaining, and trying a small cast under agreed conditions. Decide who presents which contribution. He can become a respected collaborator with imperfect casting; a single public triumph is not the only successful ending. |
| Renji Hanabusa — Anchor | Protecting bought prestige through cheating conflicts with honest learning and other students' opportunities. | **An Answer of His Own:** a study invitation becomes a request to help maintain an academic deception. Offer real preparation, refuse dishonest help, or knowingly participate. If credible evidence of cheating emerges, decide what to do with it without inventing evidence or granting the player control of disciplinary outcomes. Later work and consequences test whether his choice was genuine. |
| Yōsuke Inada — Supporting | Avoidance protects his claim of hidden potential from the humiliation of being a beginner. | **The First Missing Lesson:** choose one real gap in his knowledge, work through it together, and apply it to a manageable task. Let him admit ignorance without turning him into a secret prodigy. Renji Hanabusa's image can become a comparison he questions, but he should not receive someone else's private confession automatically. |
| Maki Ogasawara — Supporting | She wants boxing competence recognized but must still learn material she has neglected. | **Explain It with Your Hands:** work with Satoru Kanda to connect one theory lesson to her actual glove technique. Test short explanations and practice questions. Choose a sustainable study plan or a desperate cram session with costs. Passing does not require her to love books, and failure should open a concrete next step rather than erase her competence. |
| Fumito Sakurai — Supporting | Curiosity and effort have become entangled with grades and unhealthy overwork. | **The Unfinished Revision:** prepare a joint practice session while he keeps adding topics. Agree a stopping point, divide teaching roles, and return after rest to see what was learned. He can still care deeply about marks. One conversation does not remove the habit or make the player responsible for supervising his health forever. |
| Nahlah Qamar — Light | Preserve curiosity and mixed feelings about home: homesickness is compatible with enjoying study abroad. | **Almost the Right Taste:** shop for ingredients, compare substitutions with willing cooks, and prepare a meal with Maki Ogasawara or Fumito Sakurai. Let her reject an inaccurate substitute, keep an imperfect version, or save a family recipe for later. The reward is shared company and a recurring meal, not revealing that her homeland is secretly in crisis. |
| Chiharu Arai — Anchor | Starting worthy causes competes with finishing one and listening to the people affected. | **After the Posters:** ask workers or residents to define a modest project, organize help, and stay for maintenance after publicity fades. A visible first-day success may conflict with a less impressive durable fix. Issei Kurose may offer useful publicity with conditions. Later return to see whether the work remains useful and who received credit. No exclusive academy civic assignment is established. |
| Tatsuo Nagase — Supporting | Economic insecurity and hunger for affection make transactional attention difficult to distinguish from freely offered care. | **A Fair Day's Work:** accompany a paid event job and compare work terms before committing. He can ask for proper payment, accept a short-term compromise, or refuse an exploitative favor. Share a meal afterward without making company conditional on labor. His poverty is not solved by a date or by making him a comic servant. |
| Issei Kurose — Later arc | He seeks rule through leverage and sabotage, not merely confidence or misunderstood social awkwardness. | **A Useful Endorsement:** he offers tangible help to Chiharu Arai's project in exchange for visible influence and access. Investigate claims before backing them, negotiate a limited alliance, compete for credit, or refuse. If sabotage is discovered, preserve evidence and let affected people choose their response. He continues pursuing power even if the player ignores him. |
| Ruri Saegusa — Supporting | She wants an independent reputation and struggles when sincere conduct lacks the etiquette she expects. | **The Formal Invitation:** help organize a public practice or reception with people whose customs differ. Agree basic conduct, handle an actual disagreement, and decide whether formality serves the occasion or excludes someone unnecessarily. She may revise a judgment without abandoning courtesy or becoming automatically paired with Tatsuo Nagase. |
| Élodie Vautrin — Supporting | She wants affection understood while relying on a language she thinks keeps it private. | **Words Chosen Twice:** co-prepare a small reading or exchange of texts she willingly shares. Ask what she wants translated or left private. If the player actually understands Elvish, let honest clarification change the relationship. Do not use overheard French as a universal shortcut into romance or expose private notes without consequence. |
| Mitsuki Amano — Supporting | Respect for an unconventional technique competes with fear of changing or damaging a cherished focus. | **A Better Way to Carry It:** test sling and stand prototypes with Mai Kajiwara or Makoto Sashihara, budget materials, and try a controlled casting exercise. Choose comfort, protection, or casting access with real compromises. She decides whether to adopt the design. The sphere remains a Light focus, not a prophecy device. |

### Dragon Hoard Academy

| NPC / scope | Personal conflict to activate or preserve | Proposed side quest and player involvement |
|---|---|---|
| Tōru Shizunami — Later arc | Real talent and accumulated obligations have crowded out a chosen life. | **A Date on the Calendar:** join a limited research trial he genuinely enjoys, then help identify which commitments require him and which can be delegated. Miyu Asahina and colleagues negotiate coverage; he must actually request leave. The player can advocate a smaller absence or challenge a poor plan, but cannot replace an Archon or solve burnout with a gift. |
| Miyu Asahina — Supporting | She wants durable systems and independent authority but fears being valued only for astonishing usefulness. | **An Ordinary Week:** help test one bounded handover—such as exhibition setup—with written responsibilities and a willing student team. When a small problem arises, choose whether to honor the handover or quietly make her rescue it. Later see whether colleagues use the process. She remains the headmaster rather than the Archon's secretary. |
| Madoka Narukami — Later arc | She demands control while her anger can produce uncontrolled force. | **The Safety Review:** participate in a proposed revised storm drill and raise concerns about a near miss. Compare observations with witnesses, test a safer version under faculty responsibility, and decide whether a quiet adjustment is enough or a documented review is needed. She must own her conduct; students do not manage her emotions as an obligation. |
| Genzō Iwakura — Later arc | He wants a former career back while lasting injury changes what is sensible. | **The Trail Back:** accompany a carefully scoped field exercise, agree stopping conditions, and observe when his plan assumes his old mobility. Retreat, adapt roles, or refuse a risky continuation. A later trip can show a genuinely revised method. Success preserves his experience and agency without curing his leg or proving he was never limited. |
| Noriaki Takatsuki — Supporting | Pride in prestigious standards competes with admitting the work and failed drafts behind mastery. | **The Diagram with Corrections:** help reproduce a supervised summoning exercise using full notes rather than a flawless final sheet. Choose accurate documentation over a more impressive appearance. He can acknowledge a student's useful correction or obscure it, changing later willingness to collaborate. No new summoning bond rules are assumed. |
| Kōsuke Shishido — Supporting | Love for his familiars conflicts with wanting credit for care that trained handlers have supplied. | **The Handler's Day Off:** accompany an ordinary care session, ask a professional for specific advice, and practice the routine with Mihoko Nekozawa. Decide when he should request help rather than improvise. Later demonstrate a modest learned skill. Animals are not disposable test subjects or automatically obedient rewards. |
| Mai Kajiwara — Anchor | Professional pride and joy in diagnosis conflict with others' expectation of free labor. | **One Little Repair:** inspect a genuinely interesting fault, agree a paid scope, source a part, and test the result with its user. A request expands after work begins. Back her boundary, negotiate a smaller repair, or accept a compromise she freely chooses. A completed commission can leave a usable bench, repeat customer, or collaboration with Shunpei Makino; friendship does not entitle the player to free service. |
| Chiyo Tsukikage — Supporting | A dramatic persona helps her approach people but conceals ordinary interests she fears are boring. | **Costume without a Prophecy:** help Ema Tsunoda stage a voluntary performance with rehearsals, prop work, and an audience willing to play along. A scheduling or friendship disagreement needs a plain answer beneath the persona. Let her keep role-play after honesty; the healthy eye and invented mythology remain ordinary. |
| Nanami Tokuda — Supporting | Being a perceptive entertainer conflicts with disregarding someone's explicit request not to be discussed. | **Off the Board:** help her organize predictions for a consenting contest while Yūji Nishimura asks her to remove personal odds. Agree subjects, try alternate entertainment, and choose whether to challenge her if she keeps the line. Repair involves changed behavior and affected people's response, not proving that her prediction was accurate. |
| Retsu Arakida — Anchor | Fear seems safer than respect, and rare-affinity boasting conceals weak technique. Actual bullying must be addressed. | **Terms of the Rematch:** someone she targeted asks for a practical remedy before she seeks another duel with Daigo Bando. The player can support restitution, refuse to facilitate the match, challenge her conduct, or knowingly enable intimidation. A fair match can continue after a loss or win, but neither victory nor a sad confession absolves harm. Her Void magic stays modest unless later learning is authored. |
| Daigo Bando — Supporting | He wants lasting friends and can overlook others' boundaries by treating every encounter as welcome intensity. | **After the Sparring:** help arrange a training session and an ordinary shared meal. Choose pace and invitees together; if someone leaves, respect it rather than making them prove loyalty. He can learn to spend a quiet evening with friends while remaining exuberant. Friendship with Retsu Arakida does not require tolerating bullying. |
| Shunpei Makino — Supporting | He wants independence but accepts enough jobs to make reliability unsustainable. | **Three Jobs, One Afternoon:** plan an honest round of already-agreed errands with real travel time and assistance he can afford. Renegotiate a deadline, delegate with permission, or finish fewer tasks well. Later clients respond to the actual result. Avoid making the player's role simply completing all work for him. |
| Suzune Mikazuki — Anchor | She wants judgment respected beyond an expensive shield and resists being treated as incapable. | **Where the Shield Goes:** co-plan a supervised team exercise, with Mai Kajiwara offering only separately agreed paid technical work. Test routes, assign coverage and address a concrete equipment problem. Success recognizes Suzune Mikazuki’s decisions; removing her shield is not a test of worth. |
| Miharu Amemiya — Supporting | She wants precision recognized and hides how strongly she cares about losing. | **The Run That Counts:** help organize a controlled Water trial with agreed measures and varied setups. Analyze failures and choose a suitable presentation of results. Let her dislike a loss without reducing the story to appearance or public humiliation. Later practical-team consideration is a proposed opportunity, not a guaranteed reward or an existing selection rule. |
| Ema Tsunoda — Light | Preserve sincere enthusiasm while letting her choose taste beyond audience approval. | **Wear It Your Way:** make costumes from an agreed budget, obtain fabric from Aya Orimoto, and fit designs with willing wearers. Trade elaborate presentation against comfort or affordability. A later event shows people using what they chose. She need not discover a hidden trauma, and friendly help is not a romantic promise. |
| Yūji Nishimura — Light | Loneliness leads him to mistake being chosen romantically for proof that he matters. | **An Evening without Odds:** co-plan a casual outing around an interest he actually enjoys, without a target date. Handle invitations, costs, awkward conversation, and Nanami Tokuda's unwanted commentary. Friendship and a good evening can be worthwhile outcomes; no NPC is awarded for completing social tasks, and rejection is not failure of the quest. |

### Hydra Head Academy

| NPC / scope | Personal conflict to activate or preserve | Proposed side quest and player involvement |
|---|---|---|
| Reika Saionji — Later arc | Wanting independent research funding conflicts with reluctance to ask for help and the need to share control over money. | **Who Gets to Ask?:** help run a small proposed funding pilot. Hear pitches, discuss criteria with applicants, and test how costs affect participation. Favor fewer well-supported projects, a broader modest trial, or a revised process. Applicants receive actual decisions, not universal wins. Reika Saionji remains capable; public confidence is not a mandatory personality cure. |
| Kiyoko Fujinami — Light | Preserve a competent professional friendship and attachment to chosen routines; no extra catastrophe is needed. | **Tea without an Agenda:** agree a genuinely free outing with Reika Saionji, help handle one bounded scheduling obstacle, and respect their right to decline work interruptions. They later invite the player into a limited conversation or recommend a place. Their friendship exists independently of the player and is not automatically romantic. |
| Kaoruko Hanazono — Supporting | Commercial success competes with responsible botanical sourcing. | **The Last Bottle of the Old Blend:** compare cultivated substitutes, discuss sourcing with Nozomi Kogusa, and test a revised fragrance with willing users. Accept a changed product, a smaller run, or a delayed launch rather than inventing unlimited rare ingredients. Her scientific and business judgment both matter. Do not redefine ownership of Céline Desrosiers's shop. |
| Reon Fujisaki — Supporting | Enjoyment of glamour coexists with frustration that others dismiss the rigorous work beneath it. | **Beautiful under Load:** help prepare an enchantment demonstration with practical stress tests and a pleasing presentation. Choose what to simplify when time is short. He can insist on function without abandoning glamour, and students can disagree with his staging. His sexuality is not a secret, scandal, or problem to solve. |
| Kana Fujimoto — Anchor | Modest casting strength makes her doubt her right to teach, despite strong preparation. | **A Lesson That Holds:** assist with a trial lesson, ask genuine beginner questions, and practice a controlled demonstration with Homura Hibino as a demanding participant. When the planned demonstration proves unreliable, decide how to adapt openly. Students understanding the safety principle is a valid success even without spectacular casting. She revises the next lesson herself. |
| Yukine Shiratori — Supporting | She wants an artistic magical discipline respected while hiding effort behind effortless presentation. | **The Surface beneath the Spin:** prepare an ice surface with Suiren Ryūgū, test a short routine, and agree judging criteria for an optional friendly challenge with Hayate Shiranui. Handle imperfect conditions without declaring one discipline inherently superior. Later practice acknowledges the work behind the performance. |
| Homura Hibino — Anchor | Desire for a signature spectacle conflicts with resenting recognition for efficient small spells. | **A Sky of Small Fires:** plan a proposed supervised display with a clear site, audience boundary, budget, and stopping conditions. Rehearse small effects, choose sequence and scale, and adapt to changed weather or resources. A carefully staged modest show and a safely supervised larger one can both succeed; the point is ownership and control rather than extinguishing her ambition. |
| Suzuka Amashiro — Light | Preserve a comfortable, food-motivated person with preferences. Not every appetite hides trauma. | **The Dessert Circuit:** compare a few affordable dishes, negotiate a snack debt, and choose a favorite together. A changed menu, missing ingredient, or disagreement about value provides activity. She later remembers the player's taste and whether debts were repaid. No automatic romance or invented metabolic condition is needed. |
| Masamune Tateishi — Supporting | A protective code becomes controlling when he assumes another person's wishes. | **Ask before the Rescue:** an adult peer wants help handling a difficult contest or confrontation but rejects being spoken for. Accompany the preparation, ask what assistance they want, and agree when to intervene. He can revise his conduct while keeping his code. The player also has the option to overstep and face an actual objection. |
| Tōma Utsugi — Supporting | Convenient illusion tricks become dishonest when others rely on the appearance being true. | **The Dummy Attended Class:** after an attendance or presentation deception creates a practical obligation, help prepare the work honestly, refuse to support the pretense, or knowingly assist it. He may bargain for the minimum legitimate solution rather than become diligent overnight. Consequences follow the specific deception; illusion itself is not inherently immoral. |
| Gaku Inukai — Supporting | Being the mastermind matters enough that he conceals a flaw instead of asking for help. | **The Best Terrible Stall:** co-run a small, clearly described market experiment with Bunta Ushijima and optional paid help from Tōma Utsugi. Cost supplies, test the pitch, and choose whether to admit a mistake before taking more orders. Refunds or lost profit can matter without destroying the friendship. |
| Bunta Ushijima — Light | He is loyal but embarrassed to clarify instructions he has lost track of. | **Say It Back:** during the shared stall project, ask him which task he understands and let him describe the plan in his own words. Assign a useful concrete role rather than all heavy lifting. If the player treats him as disposable muscle, he can object or stop helping. He remains comically literal without being denied agency. |
| Ibuki Sakuma — Supporting | Enjoyment of exertion competes with recovery and other people's actual limits. | **An Afternoon Off:** agree a rest-day activity she helps choose, prepare for a later challenge, and let her assess a partner's warning signs. She must decide whether to follow the recovery advice she understands. Accommodating a partner can be progress without turning her sedentary. Healing never erases exhaustion or licenses injury. |
| Asuka Tsurugi — Supporting | Pride makes acknowledging care feel like surrender, while actual skill stays intact. | **The Extra Ticket:** help her choose and prepare an outing or practice invitation she has a real reason to want. Give room for friendship or optional mutual romance and let the invitee answer freely. A successful sincere moment changes future dialogue; she does not return to total denial every scene. Do not force Masamune Tateishi into a predetermined pairing. |
| Suiren Ryūgū — Supporting | She enjoys distance but wants technically precise work that other people actually use. | **Weather for One Courtyard:** co-design a small comfort experiment with willing participants. Observe a breeze helping one activity and disturbing another, then choose a compromise or a limited test area. Later arrange another outing under the umbrella if both want it. Her private notebook is not a mandatory collectible to read without permission. |
| Hayate Shiranui — Supporting | Winning measurable contests competes with contributing to a team whose success does not single him out. | **Finish Together:** prepare a supervised relay or recovery exercise with shared conditions agreed beforehand. Give him a genuinely useful job that offers little glory, then choose how to respond if he abandons it for a better individual time. A later fair rematch can coexist with improved teamwork. No automatic elite-force recruitment is promised. |
| Tamaki Kiryū — Anchor | She wants security and advancement, and is willing to shift risk onto others to obtain them. | **An Acceptable Loss:** participate in a supervised tactical exercise where her plan puts an inconvenient share of the burden on one classmate. Inspect the plan, hear the teammate, and propose a slower or more expensive alternative. Support, revise, refuse, or document her choice. She may respond to incentives rather than conscience. Masamune Tateishi can disagree; the player does not own everyone's decision. |

## Three shared chains worth writing first

### A. Invitations and consequences — Phoenix Wing Academy

**Main participants:** Riko Umezawa, Kokona Hanamori, Miu Shinohara, Sena Moriyama. An affected student should have a real preference and response, whether drawn from an existing compatible card or authored as a new supporting participant later.

1. **The hook:** the player encounters the social exclusion in an ordinary shared space. Riko Umezawa checks the affected person's reaction and then laughs along. No hidden motives are narrated as publicly known.
2. **Doing something together:** organize an alternative gathering or assist with a concrete damaged arrangement. Speak to the affected person before deciding what repair means. Invitations, room setup, and negotiations create scenes; buying a gift is not the whole quest.
3. **The first decision:** support a private apology, ask for a public correction of a public claim, or refuse an attempt to recruit the player as cover. Keeping an apology private is not necessarily cowardice; the relevant question is whether public harm remains uncorrected.
4. **Pressure returns:** Miu Shinohara or Sena Moriyama proposes a new exclusion for understandable social advantage. Riko Umezawa chooses whether to repeat the behavior. Kokona Hanamori may act helpfully without looking emotionally moved.
5. **Afterward:** the group may reform one practice, split for an occasion, continue without the player, or double down. The affected person need not forgive. Future invitations and who will speak candidly to the player change.

**Declining:** the player can leave. The clique continues, another person may intervene, and the player can encounter the changed social situation later. Do not narrate guilt for declining every school dispute.

### B. Proof in practice — Gryffin Tail Academy

**Main participants:** Satoru Kanda, Maki Ogasawara, Fumito Sakurai. Haruki Saitō is a possible later cross-academy contact, not mandatory access to another school's teaching.

1. **The hook:** Maki Ogasawara stops a correct explanation because it is unusably long. Satoru Kanda becomes defensive; Fumito Sakurai wants to add more notes.
2. **A real joint task:** choose one controlled technique to analyze, observe attempts, and turn the explanation into a brief practical instruction. The player can contribute observation, casting, coordination, or a good question.
3. **The complication:** Satoru Kanda proposes doing the final cast himself to prove he belongs. Maki Ogasawara wants the result to work; Fumito Sakurai is overpreparing.
4. **The decision:** test a limited cast with a small audience, present the pair's distinct contributions, or postpone and simplify. Any route can fail locally and be revised. No one needs to become exceptional at every skill.
5. **Afterward:** later lessons use the concise instruction. Satoru Kanda names someone else's contribution, Maki Ogasawara asks a theory question voluntarily, or a strained collaboration ends with a useful partial result. A return scene demonstrates what changed.

### C. One repair, three priorities — Dragon Hoard Academy, with a Hydra Head connection

**Main participants:** Mai Kajiwara, Shunpei Makino, Suzune Mikazuki. Kana Fujimoto can later request a separately negotiated safety demonstration; do not automatically make all schools attend one event.

1. **The hook:** a practical defect threatens an agreed rehearsal, and someone assumes Mai Kajiwara will fix it immediately for free.
2. **Joint work:** inspect the problem together, agree a limited paid scope, and decide which component is truly needed. Use the shop cast for conversations about fit, cost, or alternatives rather than a string of anonymous pickups.
3. **The complication:** a faster workaround leaves a meaningful limitation; a proper repair misses the rehearsal; extra paid help strains the budget. Suzune Mikazuki's own test observations guide a proposed change in formation.
4. **The decision:** repair, adapt the exercise around a tested limitation, or cancel honestly. The owner, craftsperson, and instructor must agree to the arrangement; the player cannot volunteer someone else's unpaid labor or safety.
5. **Afterward:** future work terms, team roles, and available equipment reflect the result. Mai Kajiwara may offer the player a proper collaboration. An unresolved cost can produce a later modest job, but an arbitrary new breakdown should not erase success.

## What keeps these people from becoming interaction menus

### Give every significant quest a shared activity

A dialogue can open a quest, but at least one scene should involve doing something alongside the NPC: rehearsing, testing, observing, teaching, shopping to a budget, preparing a meal, negotiating a scope, visiting home, or handling a public occasion. The activity should expose a choice the NPC finds difficult. A fetch task is useful when choosing the item, seller, terms, or use changes the relationship; collection alone is usually insufficient.

### Let NPCs initiate and disagree

The same person can ask for help, decline the player's plan, arrive with their own solution, invite someone else, or continue after refusal. A favored NPC should sometimes give reasonable advice the player dislikes. An antagonist can offer useful cooperation without secretly becoming good. Plans move forward through NPC decisions as well as player choices.

### Separate discovery, permission, and trust

The player notices a behavior, has a reason to investigate, and earns or obtains relevant knowledge through scenes. A high relationship should not instantly reveal every secret. Access to a notebook does not grant permission to publish it. The narrator knows motives; the player character does not automatically know them.

### Preserve distinct outcomes and room to fail

Winning, losing, withdrawing, compromising, reporting, remaining private, and refusing help should produce specific different continuations. There should often be another way forward after an unsuccessful attempt. Do not make obvious cruelty the only alternative to a perfect best ending, and do not disguise neglect of an injured person as an equally valid preference.

### Let later scenes prove the change

Use observable callbacks: a revised drill, a fair invoice, an invitation the NPC initiates, a corrected record, a project someone maintains, an ally who no longer shares confidential information, or a rival who insists on agreed conditions. A reward screen or a line saying trust increased is not enough. Do not reset successful development to its starting joke in the next scene.

### Keep ordinary company available after resolution

Meals, practice, a quiet seat, an argument about an experiment, a short visit home, or a shared hobby should remain enjoyable even when the NPC has no problem to fix. Romance is optional and requires mutual interest; friendship, rivalry, professional respect, and disagreement should all support sustained play. Not every invitation needs a relationship score or quest marker.

### Limit the active cast and protect pacing

Usually foreground two to four relevant NPCs in a scene. Other cast members can be elsewhere doing their own work. Make deadlines clear when they matter rather than silently expiring opportunities. A player can follow a favorite cast, leave a chain unfinished, or spend time outside school without all 68 arcs advancing into emergencies.

## A compact authoring worksheet for the next pass

For one selected quest, write these before encoding mechanics:

1. **Existing basis:** the exact card motive, behavior, and relationship being activated; list any proposed new fact separately.
2. **Encounter:** a public, observable hook in a valid existing area; no premature reveal of hidden information.
3. **NPC intention:** what the NPC will try if the player helps, disagrees, or declines.
4. **Shared activity:** what the player and NPC actually do across two or more scenes.
5. **Complication:** a specific competing need, limited resource, disagreement, or obstacle.
6. **Choices:** at least two materially different reasonable approaches, plus refusal where appropriate; acknowledge unethical approaches without presenting them as harmless equivalents.
7. **Knowledge and consent:** who knows which facts, who agrees to participate, and what can be disclosed.
8. **Outcomes:** a useful result, a compromised result, and a failed or abandoned attempt with an intelligible next state.
9. **Callback:** a later observable behavior or changed situation, plus an ordinary repeatable interaction.
10. **Implementation boundary:** decide what needs reliable state tracking, then consult current official Voyage documentation, release notes, the community schema, and current Studio output before choosing fields or triggers. Do not assume this narrative worksheet maps directly onto supported JSON properties.

## Canon and editorial cautions

- The current Great Sage succession has no fixed election date, detailed voting system, or player-appointed winner. Preserve Ilyra Stillglass's undisclosed academy origin and the limits on treating her decline.
- Shadowspire's owner remains reserved; its threshold is inaccessible. None of these chains reveals that identity or adds a route inside. Discovery-gated island locations do not become freely accessible because a character knows a worker there.
- The Evertree enhances the learning environment; it does not grant automatic mastery, unlimited mana, or a neighborhood-specific access rule.
- Affinity is not a restriction on other magic and does not measure worth or imply hidden power. These proposals introduce no new affinities.
- Yūma Kurobane and Chiyo Tsukikage remain ordinary role-players with modest real magic. Mitsuki Amano's crystal remains a focus.
- Quietness, atypical empathy, disability, age, sexuality, ordinary ambition, and refusal of romance are not flaws the player must cure. Harmful choices can still have consequences regardless of the actor's feelings or sympathetic history.
- Do not make a student responsible for curing an adult's burnout, enforcing laboratory safety alone, or deciding institutional justice. Students can observe, act, seek help, and build influence while accountable adults retain their responsibilities.
- The existing roster has a few malformed or partial references to Gen'ichirō Mizuhara in older faculty prose. They were not silently edited in this suggestion pass. Use the full canonical names in any approved rewrite.

**Next recommended writing batch:** choose one shared chain per academy, fully author its encounter, two or three playable scenes, alternate outcomes, and return scene, then validate and playtest those selected implementations. Expand from observed play rather than turning all 68 rows into simultaneous quest logs.
