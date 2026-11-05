"""Seed proposed handoff work records; these are not applied world changes."""
import csv, pathlib
ROOT=pathlib.Path(__file__).resolve().parents[2]
PLAN=ROOT/'world-draft/authoring/plans'
STEM='Glowhaven - World Overhaul '

def write(name,fields,records):
    with (PLAN/(STEM+name+'.csv')).open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(records)

retcons=[
('R01','Reika Saionji has a private intention to fund independent research.','Make the fund a playable project; introduce controlling conditions and a particular prior investment failure as proposed history.','Generosity and independence can produce real conflict.','Reika Saionji; Hydra Head Academy; related researchers, boutique staff, funding quests and lore'),
('R02','Miyu Asahina is characterized heavily through supporting an overworked Archon.','Give her a positive directorial program, successful delegation, outside interests and a consequential transition project.','Creates agency and relationships beyond perpetual overwork.','Miyu Asahina; Tōru Shizunami; Dragon Hoard Academy; staff and starts'),
('R03','Tōru Shizunami wants leave but keeps postponing it.','Make the desired leave a concrete negotiable development with alternative outcomes.','Turns a repeating condition into a choice with aftermath.','Tōru Shizunami; Miyu Asahina; Dragon Hoard Academy'),
('R04',"Gen'ichirō Mizuhara seeks certification monopoly and applies prejudice behind standards.",'Specify a useful common standard, its discriminatory exceptions, actual beneficiaries and opposition.','Makes the political mechanism legible while retaining culpability.',"Gen'ichirō Mizuhara; Gryffin Tail Academy; reassessment and certification material"),
('R05','Akane Todo wants judgment and research valued alongside her fighting.','Develop a disputed protective program where her readiness criteria exclude useful contributors.','Gives competence a consequential blind spot.','Akane Todo; Phoenix Wing Academy; fieldwork'),
('R06','Sena Moriyama organizes the clique and fears losing her place.','Add an independent ambition and a significant outside tie; give exclusions concrete aftermath.','Supports multiple kinds of scenes and genuine social change.','Sena Moriyama; Miu Shinohara; Riko Umezawa; affected students'),
('R07','Ruri Saegusa has a formal duel identity and attraction to Tatsuo Nagase.','Develop a particular competitive goal, technical limitation and off-duty pleasure beyond romance.','Sustains individual scenes across different player interests.','Ruri Saegusa; Tatsuo Nagase; Gryffin Tail dueling material'),
('R08','Daigo Kisaragi wants an independent company and a lodge.','Make investment, specialist hiring and lodge plans consequential optional projects.','Connects expedition work to long ambitions.','Daigo Kisaragi; Chisato Akamine; Tomoe Inukai; Gaku Shindō; Bellwether Company'),
('R09','Shigure Tsubakiri has land coercion, a prototype and generic pressure-point prose.','Specify his particular supplier network, beneficiaries and project-specific tradeoffs.','Improves antagonist specificity and credible alternatives.','Shigure Tsubakiri; Kureha Tsubakiri; Hatsu Kanesue; Naoe Futami; imported-edge arc'),
('R10','Ilyra Stillglass has long continuity and succession concerns.','Author particular achievements, compromises and differing assessments, while retaining unknown academy origin.','Creates a political legacy players can evaluate.','Ilyra Stillglass; Council; Conclave; relevant civic lore'),
('R11','Noelle Ashford is defined chiefly by foreignness and coercion.','Develop prior-life interests, a distinctive voice and independent post-release choices.','Sustains personhood through and beyond the central predicament.','Noelle Ashford; actual receiving-program scenes and outcomes'),
('R12','Council constituency and succession maneuvering are broad descriptions.','Author a coherent named participation/representation model and concrete projects before implementing election choices.','Makes authority and political influence playable without inventing outcomes.','Council; Conclave; relevant existing representatives, factions, lore and quests'),
('R13','Academies have mandates and initial practicals.','Develop complete first-year project sequences and later-study continuations with durable outcomes.','Makes school choice change activities over a long campaign.','All four academies; teachers; students; starts; quests; curriculum lore'),
('R14','Many local contacts have short role-centered cards.','Replace repetitive generic motives and disclosures with individual competences, pleasures, ties and stakes throughout all mutable realms.','Ensures whole-roster redevelopment rather than principal-only polish.','All mutable NPC rows and their actual communities'),
('R15','Magical invention and specialty opportunities are distributed across broad guidance.','Create an authored opportunity map for every ordinary discipline and concrete signature-working projects.','Gives magical growth functional milestones without changing the numerical curve.','Existing abilities, teachers, research, lore, commissions and learning ownership'),
]
fields=['retcon_id','old_fact','proposed_replacement','rationale','affected_records','mechanical_dependencies','migration_boundary','status','review']
write('Retcons',fields,[dict(zip(fields,[a,b,c,d,e,'Inspect affected native quests/controllers; preserve numerical balance and protected mechanics.','Proposed new-game content; existing history is not silently rewritten.','proposed not applied',''])) for a,b,c,d,e in retcons])

relations=[
('Miyu Asahina','Tōru Shizunami','Headmaster and Archon with a warm professional history and unequal workload.','Wants her leadership recognized and systems respected.','Trusts her competence while underestimating accumulated extra work.','Each knows their own workload; others know only witnessed portions.','Their two cards; Dragon Hoard Academy; transition project'),
('Sena Moriyama','Miu Shinohara','Sena manages social arrangements that support Miu\'s clique position.','Values friendship and fears dispensability.','Values the useful friend without fully knowing her insecurity.','Preserve current hidden-knowledge distinctions.','Their cards; clique ties and affected scenes'),
('Ruri Saegusa','Tatsuo Nagase','She respects his courage and is unsettled by his blunt attention.','Attraction and irritation coexist.','Does not fully understand why his compliments fluster her.','Private feelings do not become general knowledge.','Their cards; dueling and off-duty scenes'),
('Daigo Kisaragi','Chisato Akamine','Old expedition partners who disagree about admitting the Coldglass expertise gap.','Wants to appear dependable.','Wants specialist help and candid risk decisions.','Company members know their gap; client does not know why work is delayed.','Both cards; Bellwether Company; Coldglass content'),
('Shigure Tsubakiri','Kureha Tsubakiri','Siblings whose interests overlap without being identical.','Wants bargaining power through the private project.','Can sacrifice his scheme to preserve legitimate investment.','Do not share every private plan automatically.','Both cards; House Tsubakiri; imported-edge arc'),
('Shigure Tsubakiri','Hatsu Kanesue','Hatsu maintains his mechanism and knows the overheating defect.','Depends on technical expertise and control of the project.','Knows the actual mechanism better than every political intention.','Technical knowledge does not reveal all coercion plans.','Both cards; prototype and arc'),
]
fields=['person_a','person_b','shared_fact','a_interpretation','b_interpretation','who_knows','affected_records','status','review']
write('Relationships',fields,[dict(zip(fields,list(r)+['baseline fact with proposed development','Verify against latest source before rewriting.'])) for r in relations])

projects=[
('AC-PW-01 Keep the Exit Clear','Phoenix Wing practical','Protect a partner while maintaining a usable route; different positions have different tradeoffs.'),
('AC-PW-02 Signals through Smoke','Phoenix Wing group project','Coordinate communication, cover and extraction with real visibility limits.'),
('AC-PW-03 A Defense Others Can Use','Phoenix Wing field application','Deliver an authorized protective method that local participants can actually operate.'),
('AC-GT-01 The Working That Fails under Load','Gryffin Tail experiment','Distinguish plausible causes through controlled tests and preserve genuine measurements.'),
('AC-GT-02 Whose Result Is It','Gryffin Tail group project','Resolve attribution and access after a real useful finding.'),
('AC-GT-03 A Standard Put to the Test','Gryffin Tail institutional conflict','Compare actual applications of a standard and carry out a concrete correction, exception or challenge.'),
('AC-DH-01 Record before Removal','Dragon Hoard expedition','Choose how to record, stabilize or recover a discovery with consequences for information.'),
('AC-DH-02 The Route on Two Maps','Dragon Hoard practical','Reconcile map evidence with actual terrain using different expedition roles.'),
('AC-DH-03 What Comes Home','Dragon Hoard group project','Conclude an expedition with real evidence and an agreed custody/recovery outcome.'),
('AC-HH-01 A Delivery That Actually Works','Hydra Head practical','Develop a supply agreement that fits growers, carriers and users.'),
('AC-HH-02 The Unpopular Compromise','Hydra Head group project','Carry out a workable settlement without requiring universal approval.'),
('AC-HH-03 Who Maintains It','Hydra Head field application','Deliver a useful project with actual maintenance responsibility.'),
('CAREER-01 Independent Company','Existing guild and willing collaborators','Complete a first contract, establish an agreed team role and choose a viable specialty.'),
('CAREER-02 Specialist Workshop','Actual local workroom and craft contacts','Obtain agreed access and deliver a meaningful commission with a chosen function.'),
('CAREER-03 Research Circle','Actual teachers and interested researchers','Carry out funded or independent research with explicit credit/access terms.'),
('CAREER-04 Merchant Venture','Actual local traders and carriers','Complete a particular shipment and establish a continuing customer relationship.'),
('POL-01 Research Access','Council, academies, researchers and actual funders','Carry out a bounded funding/access agreement and preserve who gains or loses influence.'),
('POL-02 Public Service and Investment','Actual communities and relevant civic institutions','Carry out a project or settlement that changes a named community\'s burden or benefit.'),
('POL-03 Foreign Leverage','Actual domestic/foreign participants and agreements','Resolve a bounded trade, scholarly or diplomatic matter without presumed imperial jurisdiction.'),
('ADV-01 Rescue and Extraction','Select existing capable local contacts and geography','Bring actual endangered participants to a credible safe conclusion or record limited/failure outcome.'),
('ADV-02 Survey and Field Science','Select existing field sites and researchers','Return reliable observations or a credible in-place study with stated limits.'),
('ADV-03 Salvage and Recovery','Select existing coast/ruins and actual interested owners','Conclude real recovery/custody and record condition and entitlement.'),
('ADV-04 Infiltration','Select a bounded existing objective with credible access alternatives','Obtain the actual objective through a viable chosen method and preserve evidence/knowledge.'),
('ADV-05 Interested Negotiation','Select an actual capable party with its own interests','Carry out a workable agreement or record real refusal/limited outcome.'),
('ADV-06 Hazardous Route','Select existing meaningful terrain and guides','Complete the chosen passage using actual preparation and consequences.'),
]
fields=['undertaking_key','discovery_owner','acceptance_owner','completion_evidence','payout_owner','follow_up','refusal_failure','status','review']
records=[]
for key,source,evidence in projects:
    records.append(dict(zip(fields,[key,'Proposed source: '+source+'; select exact native owner during implementation.','Native quest acceptance only after actual commitment; use ordinary interaction where no undertaking is needed.',evidence,'One named native completion effect or real transaction; exact owner and fee must be specified before implementation.','Optional next opportunity after actual conclusion; no automatic commitment.','Record chosen scope, retained evidence and actual cost; no forced victory.','proposed design assignment not a native quest key',''])))
write('Undertakings',fields,records)

scenarios=[
'Four academy openings and advanced-role entry','Return to NPC after success','Return to NPC after disagreement','Unhurried off-duty company','Refuse work','Refuse romance','Finish paid job and revisit','Partial project then failed approach','Signature spell invention and later use','Scroll study with two readers','Noncasting occupational specialist','Workshop access after travel','Political agreement and knowledge channels','Each realm atmosphere and placement','Crucible plus concurrent local work','Rebirth slow start and later pursuit','Two humans sharing project rewards','Quiet day without unrelated interruption','Ordinary defeat and recovery','Existing-save import only if supported']
fields=['scenario','build_sha256','steps','expected','observed','result','tester_date']
write('Live Checks',fields,[dict(zip(fields,[s,'','Fill exact procedure for implemented build.','Use handoff section 23 and scenario-specific actual ownership.','','untested',''])) for s in scenarios])
print({'proposedRetcons':len(retcons),'baselineRelationships':len(relations),'proposedUndertakingDesigns':len(projects),'liveCheckRows':len(scenarios)})
