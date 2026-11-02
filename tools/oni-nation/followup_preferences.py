"""Requested start presentation, foreign home-key access and creation backgrounds."""
import copy,json
from build import ROOT,HERE,dump

PAST=[
 ('Veteran Infantry Soldier','You served through a campaign: long marches, cramped camps and the discipline of holding a line when enthusiasm had gone. You still judge a plan by what ordinary tired people can carry out.','Force Combat'),
 ('Veteran Skirmisher','You learned to move under pressure, choose an approach and leave a bad position before pride made the decision. Old service shaped your timing more than your present occupation.','Finesse Combat'),
 ('Former Watch Officer','You have broken up arguments, watched difficult doors and learned how quickly a crowded street can turn dangerous. Familiar procedure and a steady guard are part of your past.','Guarded Combat'),
 ('Former Guild Adventurer','You have taken commissions, worked alongside unfamiliar partners and learned the difference between an attractive notice and a feasible journey. Something brought you to a fresh beginning.','survival'),
 ('Former Monster Hunter','You have followed signs, waited through poor weather and discovered why a confident description is less useful than a clear track. Preparation still shapes how you read a place.','Perception'),
 ('Expedition Survivor','A difficult expedition taught you to manage injury, limited supplies and frightened companions. You remember the small practical decisions that made returning possible.','Medicine'),
 ('Former Mercenary','You once sold your fighting work, shared camp with people whose loyalties differed and learned to ask exactly what a patron meant by protection.','Force Combat'),
 ('Former Arena Fighter','You have fought before a crowd, recovered from public defeat and learned how to keep your movement controlled when an audience wants a spectacle.','Finesse Combat'),
 ('Former Field Medic','You have worked beside exhausted travelers or fighters, triaged an injury and cared for someone without promising a miracle. Those habits remain useful beyond the field.','Medicine'),
 ('Former Bandit','You once lived by a road crew’s threats, stolen goods and unreliable loyalties. Whether you regret it, justify it or simply left, you know how a nervous lookout behaves.','Stealth'),
 ('Smuggling Past','You have carried goods through unwanted attention, trusted the wrong handover and learned to recognize a price that conceals somebody else’s risk.','Trade'),
 ('Former Burglar','You have studied occupied buildings, quiet approaches and the habits of people who assume their belongings are safe. Your present use of that knowledge is yours to decide.','Stealth'),
 ('Former Confidence Trickster','You have sold a convincing account, watched a mark hesitate and learned how a pleasing detail can distract from the real question.','Deception'),
 ('Time Served','You have lived through confinement, learned the informal rules of shared quarters and noticed how people negotiate a small amount of freedom. That experience is in your past.','Insight')]

DRAK=[
 ('Iwatsugu Clan Upbringing','You grew up as an ordinary member of Clan Iwatsugu in Drakenspire, around household obligations, stonework and arguments about which shared repair should come first. Your own branch and family life can be defined as part of your story.','Trade'),
 ('Yukinose Clan Upbringing','You grew up as an ordinary member of Clan Yukinose in Drakenspire, among winter provisions, carrier news and hospitality that could carry an obligation. Your place in that large household leaves room for your own ambitions.','survival'),
 ('Arashimine Clan Upbringing','You grew up as an ordinary member of Clan Arashimine in Drakenspire, around equipment trials, service commitments and exacting practice. Household expectations are familiar, even if you chose a different direction.','Guarded Combat'),
 ('Crescent Sanctuary Upbringing','You grew up around Drakenspire’s dragon observances, ancestral stories and the practical work of receiving pilgrims. You learned to recognize a solemn occasion and the ordinary person who needs help beside it.','Etiquette'),
 ('Mountain Herding Household','Your Drakenspire household raised goats or sheep along difficult slopes. You learned to read an animal’s unease, judge a shelter and bring a wandering charge home.','Animal Handling'),
 ('Winter Stores Community','You grew up around Drakenspire’s shared stores, distribution queues and neighbors making supplies last. Counting fairly and noticing a strained household became everyday habits.','Insight'),
 ('Mountain Rescue Upbringing','People in your Drakenspire household helped bring lost or injured travelers back from the passes. You learned to watch conditions, prepare a line and take a small warning seriously.','Perception')]

def trait(name,description,skill):
    return {'name':name,'description':description+f' Start with +1 {skill}.','traitNarrativeEffects':description,'attributes':[],'skills':[{'skill':skill,'modifier':1}],'resources':[],'startingItems':[],'abilities':[],'unlockedBy':[],'excludedBy':[],'requirements':[]}

def apply(w):
    descriptions={
     'Write Your Own':'Choose a starting place and describe your first scene: a reunion, a first lesson, a market dispute or a journey already underway. Tell us who is present and the mood you want; a few sentences are enough. In multiplayer, the host describes the shared opening.',
     '🔥 Phoenix Wing: First Day':'Begin your first year at Phoenix Wing Academy in Glowhaven. Collect your timetable, join the welcome and meet the students heading to your first Magic Theory class.',
     '📘 Gryffin Tail: First Day':'Begin your first year at Gryffin Tail Academy in Glowhaven. A busy registrar, a welcome address and your first Magic Theory class give the morning a clear direction.',
     '🐉 Dragon Hoard: First Day':'Begin your first year at Dragon Hoard Academy in Glowhaven. Find your timetable, join the new arrivals and discover what your first teachers expect of you.',
     '💜 Hydra Head: First Day':'Begin your first year at Hydra Head Academy in Glowhaven. Collect your timetable and follow a lively crowd of new students from the welcome to your first class.',
     '🛡️ Adventurer: Guild Counter':'Begin at Glowhaven’s Adventurer’s Guild, where new applicants and seasoned travelers share the counter. Ask about qualifying, bring your existing badge or find out what sort of work suits you.',
     '⚔️ Akitsuhara: Samurai at the Gate':'Begin in the country of Akitsuhara, at a Shogunal household in Benitsuru. A junior service assignment, an impatient commander and a crowded courtyard offer a first taste of life around the capital’s retainers.',
     '🥷 Akitsuhara: Behind the Reed Screen':'Begin in the country of Akitsuhara, among independent scouts at a bamboo-valley training ground. A practical observation exercise asks whether you notice more than the obvious distraction.',
     '🍃 Akitsuhara: A Rōnin’s Morning':'Begin in the country of Akitsuhara, at a crowded inn in Benitsuru. An independent swordsman, an ordinary argument and a busy capital leave you several ways to spend the morning.',
     '🔔 Akitsuhara: The Bell Workshop':'Begin in the country of Akitsuhara, at a working shrine in the redleaf countryside. A small bell repair introduces its keeper, local concerns and the possibility of an unfamiliar path.',
     '🌾 Akitsuhara: Bread before Rumors':'Begin in the country of Akitsuhara, in the farming community of Hoshina. Neighbors, a communal oven and a practical morning problem offer a life beyond the capital’s swords and politics.',
     '🧭 Akitsuhara: The Local Board':'Begin in the country of Akitsuhara, at the Adventurer’s Guild branch in Benitsuru. Meet its lively clerk, qualify locally or bring your badge and ask about the roads ahead.',
     '🏔️ Drakenspire: By the Common Hearth':'Begin in Drakenspire, the snowy dragonkin fortress nation beyond Glowhaven. A shared lodge hearth, an awkward load and travelers comparing the passes make a first foothold in mountain life.',
     '🦋 Asterveil: Notes beneath Glass':'Begin in Asterveil, a fae-inhabited sky archipelago beyond Glowhaven. At an inhabited conservatory, a small research puzzle offers somewhere sensible to start before the wilderness calls.',
     '📚 First Day of Work: Phoenix Wing':'Join Phoenix Wing Academy in Glowhaven as a new instructor. Kōhei Sanada welcomes you to the faculty offices to discuss your subject, classroom and opening lesson.',
     '📚 First Day of Work: Gryffin Tail':'Join Gryffin Tail Academy in Glowhaven as a new instructor. Meet Norio Shibata, get to know the department and prepare for your first lesson tomorrow.',
     '📚 First Day of Work: Dragon Hoard':'Join Dragon Hoard Academy in Glowhaven as a new instructor. Miyu Asahina has a teaching space to show you, a timetable to discuss and colleagues you have yet to meet.',
     '📚 First Day of Work: Hydra Head':'Join Hydra Head Academy in Glowhaven as a new instructor. Kiyoko Fujinami introduces the department and helps you find the shape of tomorrow’s first lesson.',
     '💰 Merchant: First Morning':'Begin among the stalls of Four Sages Bazaar in Glowhaven. Rinpei Komatsu offers a practical demonstration and wants to know what sort of business you hope to build.',
     '🌾 Village Life: Brookmeadow':'Begin in Brookmeadow, a farming village in the Glowhaven countryside. A mill yard, familiar local disagreements and Haruho Taneda’s troublesome tally slate offer a quieter first morning.',
     '✨ Summoned as a Familiar: Phoenix Wing':'Wake inside a spell circle at Phoenix Wing Academy in Glowhaven as Hinae Komori’s unexpected familiar. An alarmed student, a concerned supervisor and a strange new bond await your response.',
     '✨ Summoned as a Familiar: Gryffin Tail':'Wake inside a spell circle at Gryffin Tail Academy in Glowhaven as Satoru Kanda’s unexpected familiar. The theory sounded much simpler before someone appeared in the circle.',
     '✨ Summoned as a Familiar: Dragon Hoard':'Wake inside a spell circle at Dragon Hoard Academy in Glowhaven as Kōsuke Shishido’s unexpected familiar. A surprised summoner and a supervisor with questions make an unusual introduction to academy life.',
     '✨ Summoned as a Familiar: Hydra Head':'Wake inside a spell circle at Hydra Head Academy in Glowhaven as Tōma Utsugi’s unexpected familiar. Discover the person responsible and decide what to make of the bond between you.',
     '🎲 Random':'Let the opening choose a public place in Glowhaven and a plausible moment suited to your character. A conversation, small problem or ordinary day can become the beginning of something larger.'}
    assert set(descriptions)==set(w['storyStarts'])
    for name,text in descriptions.items():w['storyStarts'][name]['description']=text
    adventurer='🛡️ Adventurer: Guild Counter';out={}
    for k,v in w['storyStarts'].items():
        if k==adventurer:continue
        if k=='⚔️ Akitsuhara: Samurai at the Gate':out[adventurer]=w['storyStarts'][adventurer]
        out[k]=v
    w['storyStarts']=out
    for name,desc,skill in PAST+DRAK:
        assert skill in w['skills'];w['traits'][name]=trait(name,desc,skill)
    origins=w['traitCategories']['Origin & Upbringing']
    for name,_,_ in DRAK:
        if name not in origins['traits']:origins['traits'].append(name)
    group={'name':'Drakenspire — Clans and Communities','traits':[n for n,_,_ in DRAK]}
    origins['subcategories']=[g for g in origins['subcategories'] if g['name']!=group['name']]+[group]
    categories={}
    for k,v in w['traitCategories'].items():
        if k=='Past Experience':continue
        categories[k]=v
        if k=='Origin & Upbringing':categories['Past Experience']={'name':'Past Experience','maxSelections':1,'description':'Optional: choose one part of your earlier working life, service or difficult history. It adds a small practiced skill while leaving your present direction open.','traits':[n for n,_,_ in PAST],'subcategories':[{'name':'Service and Fighting','traits':[n for n,_,_ in PAST[:3]+PAST[6:9]]},{'name':'Adventuring and Fieldwork','traits':[n for n,_,_ in PAST[3:6]]},{'name':'Crime and Confinement','traits':[n for n,_,_ in PAST[9:]]}]}
    w['traitCategories']=categories
    physical=w['traits']['Physical Foundations']
    physical['skills']=[{'skill':'Force Combat','modifier':1},{'skill':'Finesse Combat','modifier':1}]
    for field in ['description','traitNarrativeEffects']:
        physical[field]=physical[field].replace('Start with +1 Force and +1 Finesse.','Start with +1 Force, +1 Finesse, +1 Force Combat and +1 Finesse Combat.')
    key='oni_foreign_glowhaven_key_issue'
    w['triggerDefinitions'][key]={'name':key,'recurring':True,'conditions':[{'type':'party-location','operator':'regex','value':'^(Drakenspire Portals|Cloudbloom Landing|Benitsuru Portal Shrine)$'},{'type':'read-boolean','key':'gh_evertree_transited','operator':'equals','value':False},{'type':'player-item','item':'Glowhaven Portal Key','operator':'equals','value':0},{'type':'action','query':'An actually authorized transit delegate at this desk approves the traveler’s legitimate journey to Glowhaven and physically hands over a Glowhaven Portal Key now. Fuyumi Kirihara can handle Drakenspire approvals; Nobu Senda handles Benitsuru; the duty transit delegate handles Cloudbloom. Study, lawful work, trade, family business or credible sponsorship can qualify. Starting here, requesting a key, merely being a pilot, an unofficial gift or another traveler’s approval is not a grant. Identify the travelers actually approved.'}],'effects':[{'type':'item-add','item':'Glowhaven Portal Key','quantity':1,'target':'satisfyingPlayers'},{'type':'story','instruction':'The approved traveler receives one reusable Glowhaven Portal Key, identifying the fixed passage to Evertree Base - Portal Room. Explain the route briefly and leave crossing to their choice. No second copy, forced travel, palace access or other outbound keys are granted.'}]}
    for place in ['Drakenspire Portals','Cloudbloom Landing','Benitsuru Portal Shrine']:
        line=' The authorized transit desk can approve a legitimate visit to Glowhaven and issue its reusable portal key locally. An approved journey is separate from merely standing at the arch.'
        if line not in w['locations'][place]['basicInfo']:w['locations'][place]['basicInfo']+=line
        line=' A character beginning in this realm can request a Glowhaven Portal Key here. A delegated official must actually approve a legitimate journey and hand it over; Kohane Kazahana can introduce the Cloudbloom duty delegate but piloting alone is not issuing authority. Existing fixed home arches remain usable without a key; preserve their exact Evertree arrival.'
        if line not in w['locations'][place].get('hiddenInfo',''):w['locations'][place]['hiddenInfo']=w['locations'][place].get('hiddenInfo','')+line
    w['itemTypes']['Glowhaven Portal Key']['description']='A reusable return key issued under an approved Evertree journey or by an authorized partner transit desk. At the established portal rooms in Drakenspire, Asterveil or Benitsuru, it identifies the passage to Evertree Base - Portal Room in Glowhaven. The key is retained after use and costs no passenger mana. It grants no private palace access or permission for another destination.'
    return {'newExperienceTraits':len(PAST),'newDrakenspireOrigins':len(DRAK),'foreignHomeKeyTrigger':key,'startDescriptions':len(descriptions),'adventurerMovedAboveAkitsuhara':True}

if __name__=='__main__':
    path=ROOT/'world-draft/WorldAlpha - World.json';w=json.loads(path.read_text(encoding='utf-8'));report=apply(w);dump(path,w)
    m=json.loads((HERE/'manifest.json').read_text(encoding='utf-8'))
    if report['foreignHomeKeyTrigger'] not in m['triggers']:m['triggers'].append(report['foreignHomeKeyTrigger'])
    dump(HERE/'manifest.json',m);dump(HERE/'start-and-creation-followup.json',report)
    from regression_delta import record
    record(w)
    print(json.dumps(report))
