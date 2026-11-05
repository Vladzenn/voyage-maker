"""Build the reviewed capital expansion; no network calls or credentials here."""
import argparse, copy, hashlib, json, pathlib, random, re, sys
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
import project

BASE = ROOT / 'world-draft/WorldAlpha - World.json'
OUT = ROOT / 'output/ardelis-2026-11-05'
GUILD = "Adventurer's Guild - Caelrath Branch"
VLAD = "Valkazathoth'dmir"
PALACE = 'Caelrath Palace'
KEY = 'Ardelis Portal Key'

def compact(v): return json.dumps(v, ensure_ascii=False, separators=(',', ':'))
def digest(v): return hashlib.sha256(json.dumps(v, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
def lines(file): return [l.split('|') for l in (HERE / file).read_text(encoding='utf-8').splitlines() if l and not l.startswith('#')]
def C(t, value, **kw): return dict(type=t,operator='equals',value=value,**kw)
def E(t, value, **kw): return dict(type=t,operator='set',value=value,**kw)
def S(s): return dict(type='story',instruction=s)
def item(name, amount=1, target='allPlayers'): return dict(type='item-add',item=name,quantity=amount,target=target)
def Q(w, name, giver, loc, statement, done, brief, reward=0):
    w['parties']['']['quests'][name] = dict(name=name,status='planned',detailType='detailed',conclusive=True,
        questSource=giver,questLocation=loc,questStatement=statement,
        objectives={'task':dict(id='task',text=done,status='active')},
        completionCondition=dict(type='story',query=f"For {name}, the participating party has actually done this: {done} Plans, merely accepting, other people's unrelated work and hypothetical outcomes are false. Preserve an already verified result after travel."),
        questDesignBrief=brief+' Offer only for an actual relevant inquiry or agreement; hearing gossip is not acceptance. Use real people, supplied outcomes and actual possessions. One native completion owns its configured payment; do not pay again in narration.',
        onCompleteEffects=([item('Mark',reward)] if reward else []))
def rule(w,name,conditions,effects=(),script=None,scope='party',phase=None):
    r=dict(name=name,recurring=True,scope=scope,conditions=conditions,effects=list(effects))
    if script is not None:r['script']=script
    if phase:r['phase']=phase
    w['triggerDefinitions'][name]=r

def area_text(label, loc):
    specific={
      'Receiving Cellar':'Padded restraints lie beside a wheeled receiving frame. A service stair leads up; calibrated brass conduits continue toward the lower galleries. Someone has scrubbed the floor more thoroughly than the shelving.',
      'Calibration Gallery':'Marked test plates and disconnected practice housings line the passage. Scorch traces end at grounding posts. The next stairs follow thick cooling pipes down toward a locked work landing.',
      'Cooling Vault':'Cold pipes crowd a low stone chamber above a grated overflow. A cracked bypass and a separate ward feed can be examined without entering the final apparatus. Irregular pulses make careless work dangerous.',
      'Warded Crossing':'A narrow service bridge crosses a deep apparatus shaft. Its ward plates face inward toward a sealed cradle door. Damaged conduits and old warning scars make the danger beyond plain.',
      'Resonance Cradle':'A deep circular chamber holds a suspended articulated vessel within brass support rings. Ivory ceramic plates catch violet light from a fractured crown regulator. The bridge behind the entrance remains a real route out; heavy piers provide cover.',
      'Audience Hall':'Tall white piers frame a royal dais, with petition benches set well below it. Violet banners and gold celestial work emphasize the long approach. Attendants keep a clear working lane beside the formal route.',
      'Council Chamber':'A long standing map table shares the room with high-backed seats and a practical writing desk. Open shutters admit cold mountain air. Cups and unfinished dispatches make the room look used.',
      'Royal Apartments':'Layered violet textiles soften pale walls around a private sitting room. Fresh flowers stand beside correspondence trays and a screened inner doorway. Household attendants know when to knock.',
      'Portal Room':'A stone-framed transit arch stands beyond the staffed waiting floor. Its stable view leads to the Evertree Portal Room in Glowhaven. A brass rail separates the arch approach from the officer’s desk; ordinary stairs lead back into Caelrath.',
      'Practice Court':'A worn level court has blunted training weapons, moveable targets and a rack of shields. Observers stand behind a low rail. Water and bandages wait in a sheltered corner.',
      'Quiet Room':'A plain bed, water jug and screened window make a sparse patient room. A chair stands beyond reach of the bed, beside a monitored clasp circuit. The door opens onto the receiving corridor.',
      'Field Chapel':'A small high-star lamp hangs above plain benches. Medical rolls and repaired cloaks share a shelf with prayer books. The chapel is used by tired people rather than arranged as a museum.',
    }
    if label in specific:return specific[label]
    low=label.lower()
    if any(x in low for x in ['kitchen','bakery','oven']): body='Worktables bear knife marks and flour at the edges. Warm ovens, water crocks and hung utensils leave a narrow lane for cooks carrying trays.'
    elif any(x in low for x in ['garden','orchard','herb','flower']):body='Beds of cultivated plants follow low stone borders. Water channels, clipped paths and a few untidy tools show the work needed to keep the growing spaces healthy.'
    elif any(x in low for x in ['dock','landing','quay','pier','boat']):body='Wet ropes loop around worn mooring posts beside a narrow working edge. Boat traffic and the height of the water determine where it is sensible to stand.'
    elif any(x in low for x in ['study','reading','library','archive','copy','records','office','counting']):body='Shelves, a worked-in desk and a clear reading surface leave space for a visitor. Daylight falls across bound books, tools and the small personal belongings of the person who works here.'
    elif any(x in low for x in ['work','forge','kiln','fitting','repair','tool','assay']):body='A clear central working space sits between tool racks and secured materials. Repairs, unfinished pieces and well-used benches show the difference between a display and a functioning trade.'
    elif any(x in low for x in ['dorm','bed','guest','lodg','room','apartments']):body='Practical furniture, folded cloth and a window toward the neighboring terrace give the room a lived-in scale. Personal storage stays separate from the shared walking space.'
    elif any(x in low for x in ['stair','walk','bridge','crossing','approach','path']):body='Stone footing follows the terrace edge, with a low parapet and narrower service recesses. The neighboring entrances are visible from the main walking line; water and mountain air carry through the gaps.'
    elif any(x in low for x in ['court','square','yard','green','lawn']):body='An open working space sits between pale walls and smaller doorways. Worn paving, a few benches and practical delivery access show where people gather and where traffic must keep moving.'
    elif any(x in low for x in ['chapel','nave','shrine','vestry','bell']):body='Pale stone, a violet hanging and a small celestial lamp frame a place of ordinary devotion. Foot-worn approaches and everyday service objects keep it distinct from a royal chamber.'
    else:body='Pale masonry and violet-painted wood enclose a compact, practical space. Its furnishings suit the establishment around it; the neighboring passage remains clear for people going about their work.'
    return f'{label} forms part of {loc}. {body}'

def places(w, source):
    mapping={a:b for a,b,c in lines('regions.txt')}
    descriptions={a:(b,c) for a,b,c in lines('regions.txt')}
    for old in source['regions']:
        name,desc=descriptions[old]
        r=copy.deepcopy(source['regions'][old]);r.update(name=name,basicInfo=desc,npcLevelRange={'min':1,'max':30})
        w['regions'][name]=r
    w['realms']['Ardelis']=dict(name='Ardelis',initialKnown=False,basicInfo='Caelrath, capital of the Empire of Ardelis: inhabited mountain terraces, pale towers, working waterways and deep lower harbors. The empire extends beyond this capital into other provinces and cities. Bridges, service stairs and canals connect these districts; the city is not floating in the sky.')
    pins=[]
    for name,reg,xy,old,desc,labels in lines('locations.txt'):
        if old!='NEW':
            rec=copy.deepcopy(source['locations'][old]);assert rec['region']==reg
        else:rec=dict(x=int(xy.split(',')[0]),y=int(xy.split(',')[1]),radius=2)
        labels=labels.split(';'); names=[name+' - '+a for a in labels]
        areas={n:dict(description=area_text(a,name),paths=[names[j] for j in [i-1,i+1] if 0<=j<len(names)]) for i,(n,a) in enumerate(zip(names,labels))}
        # Establishment circulation is a hub; only the palace descent is a true chain.
        if name not in [PALACE,'Caelrath Sewers']:
            for i,n in enumerate(names):areas[n]['paths']=names[1:] if i==0 else [names[0]]
        rec.update(name=name,region=mapping[reg],basicInfo=desc,areas=areas,initialKnown=False,complexityType='complex',detailType='detailed')
        rec['npcLevelRange']={'min':1,'max':28}
        if name==PALACE:rec['npcLevelRange']={'min':20,'max':35}
        if name=='Caelrath Sewers':rec['npcLevelRange']={'min':7,'max':18}
        rec['hiddenInfo']='Residents, work and ordinary travel occupy this site. Use its actual rooms and neighbors. Private spaces need actual access; public attendance does not imply friendship, a quest agreement or jurisdiction.'
        w['locations'][name]=rec
        pins.append(dict(source=old,name=name,sourceRegion=reg,region=mapping[reg],x=rec['x'],y=rec['y'],placement='preserved Studio pin' if old!='NEW' else 'new approximate pin for author adjustment'))
    name='Starward Commandery'; labels=['Gate Court','Chapter Hall','Practice Court','Field Chapel','Equipment Room']
    w['locations'][name]=dict(name=name,region='Starfall Heights',x=32,y=16,radius=2,complexityType='complex',detailType='detailed',initialKnown=False,npcLevelRange={'min':22,'max':35},basicInfo='A working paladin chapterhouse stands beside the sacred terrace, with a plain gate court, practice yard and field chapel. Ivory plate is repaired here between ceremonial duties. The order serves the crown and the celestial faith; its members do not always agree about what either service requires.',hiddenInfo='The Starward Oath has its own command and witnesses. It is distinct from the city watch, the palace household guard and the cult. A membership or a white cloak does not prove universal complicity.',areas={name+' - '+a:dict(description=area_text(a,name),paths=[name+' - '+b for b in (labels[1:] if i==0 else labels[:1])]) for i,a in enumerate(labels)})
    pins.append(dict(source='NEW',name=name,sourceRegion='chapel',region='Starfall Heights',x=32,y=16,placement='new approximate pin for author adjustment'))
    # Keep the author's supplied eighteen locations in their incoming relative order.
    source_names={p['source']:p['name'] for p in pins if p['source']!='NEW'}
    new_names={p['name'] for p in pins};old_order=[k for k in w['locations'] if k not in new_names]
    ordered=old_order+[source_names[k] for k in source['locations']]+[p['name'] for p in pins if p['source']=='NEW']
    w['locations']={k:w['locations'][k] for k in ordered}
    return pins

def factions(w):
    rows=[
    ('Ardelis','major','The empire around Caelrath contains provincial cities, farms and many ordinary households. The crown’s war ambitions and costly magical projects compete with civic needs. Its King and Queen rule from the capital, but neither speaks for every citizen.','Royal prestige hides uneven supply and competing offices; nationality alone does not make a person hostile.'),
    ('Imperial Court of Ardelis','major','King Cedran, Queen Isabeau and their households govern from Caelrath Palace. Three adult princesses have military, artistic and scholarly interests. Nobles, civic officials and the court mage compete for access and resources.','Cedran authorized the receiving program for war. Isabeau concealed coercion and pursues independent control. Severin controls the apparatus but is not her mindless servant.'),
    ('Ivory Guard','minor','The royal household guard protects palace rooms, escorts official movements and trains in the capital. Corvin Hale commands its daily service. Its remit differs from the city watch.','Conflicting transfer orders have reached the officers. Real evidence can divide loyalty; one friendly guard cannot command every patrol.'),
    ('Order of the Starward Oath','major','Ardelis’s paladins combine trained arms with celestial devotion and crown service. Aurélian Vauss leads the capital commandery; Séraphine Duvray commands a field detachment, while Osmond Verain serves as chaplain and healer.','Its leaders differ over the receiving operation. Zeal, personal courage and genuine public service coexist with cruelty and compromised obedience. Do not equate the whole order with the cult.'),
    ('Church of the High Star','major','Astraeon, the High Star, is the celestial deity honored in Ardelis’s temples. Laurent Bellegarde oversees the cathedral. Worship, relief work, ceremonies and institutional influence meet among ordinary believers with different convictions.','Sabine’s splinter circle is not the entire church. Laurent’s delay helped it grow; evidence can force accountability without pretending all worship is fraudulent.'),
    ('House Montrevel','minor','A landed house whose grain estates and credit sustain royal supply. Hector prizes authority and hospitality; Lucille runs much of its practical work.','Double-pledged grain and tenant hardship threaten its reputation.'),
    ('House Dalcourt','minor','A commercial house funding trade, workshops and imperial contracts. Julienne values clear terms and reliable delivery.','Marcel’s private guarantees expose family and workers to court debts.'),
    ('House Veymont','minor','A military family whose officers sponsor equipment, horses and frontier service. Armand expects discipline and loyalty.','Supply fraud and Adrien’s royal affair are separate liabilities.'),
    ('House Orselle','minor','An old elven household patronizing performance, scholarship and skilled crafts. Mireille uses salons to shape taste and public access.','Selective generosity protects friends and can exclude talented enemies.'),
    ('The Glass Knives','minor','A discreet Caelrath organization trading in stolen goods, protection, debt leverage and information. Lucan Voss prizes profit and a usable neighborhood.','Not all members share Lucan’s limits. They sometimes serve court intermediaries but have independent interests and no general cult allegiance.'),
    ('The Unveiled Star','minor','A private devotional circle known among a small number of seekers for intimate vigils and promises of extraordinary communion.','Sabine and her inner circle seek a physical vessel for Astraeon through coercive spirit-binding. Sincerity does not make their promises true or their victims willing.')]
    for name,typ,pub,hidden in rows:w['factions'][name]=dict(name=name,factionType=typ,basicInfo=pub,hiddenInfo=hidden,initialKnown=False)

def people(w):
    majors=[json.loads(l) for f in ['major-people.jsonl','paladins.jsonl'] for l in (HERE/f).read_text(encoding='utf-8').splitlines() if l]
    seeds=list(majors)
    for name,bio,loc,role,look,manner,private,hobby,pool in lines('people.txt'):
        gender,age,species,level=bio.split()
        seeds.append(dict(name=name,gender=gender,age=int(age),species=species,level=int(level),faction='Ardelis',location=loc,area='',look=look,public=f'{name} works as {role}. {manner}',equipment='Well-kept tools appropriate to this trade, a small purse and practical personal belongings.',want=manner,secret=private,pressure='Concrete evidence, fair terms and the safety of people they actually know matter more than flattery.',temperament=[manner,hobby,'Speaking Style: Speak from this person’s actual experience, with their own priorities and limits.'],pastime=hobby,combat='Uses actual training to protect themselves or withdraw; a civilian occupation grants no combat mastery.',affinityPool=pool.split(','),major=False))
    saved=HERE/'selections.json'
    selections=json.loads(saved.read_text(encoding='utf-8')) if saved.exists() else {}
    rng=random.SystemRandom()
    public_magic=[k.removesuffix(' Magic') for k in w['skills'] if k.endswith(' Magic') and k!='Time Magic']
    for n in seeds:
        if n['name'] not in selections:
            if n.get('affinities')=='ALL_PUBLIC':a=public_magic;draw='authored exceptional all-public affinity; finite learned techniques'
            elif isinstance(n.get('affinities'),list):a=n['affinities'];draw='authored special anatomy'
            else:
                r=rng.randrange(100);count=1 if r<65 else 2 if r<90 else 3
                a=rng.sample(n['affinityPool'],count);draw=r
            selections[n['name']]={'affinities':a,'weightedDraw':draw,'source':'one saved SystemRandom draw; counts 65/25/10'}
        a=selections[n['name']]['affinities'];loc=w['locations'][n['location']]
        area=n['location']+' - '+n['area'] if n['area'] else next(iter(loc['areas']))
        if area not in loc['areas']:
            # Some authoring labels have a longer native name; choose by exact suffix or record the actual fallback.
            match=[k for k in loc['areas'] if n['area'].lower() in k.lower()]
            area=match[0] if len(match)==1 else next(iter(loc['areas']))
        n['actualArea']=area
        typ='Construct' if n['name']=='Thaurivex' else 'Adventurer' if any(x in n.get('public','').lower() for x in ['adventurer','shield fighter','paladin']) else 'Court Official' if n['major'] else 'Resident'
        affin=', '.join(a)
        card=dict(name=n['name'],properName=n['name'],type=typ,detailType='detailed',gender=n['gender'],tier='boss' if n['name']=='Thaurivex' else 'strong' if n['level']>=28 else 'average',level=n['level'],currentLocation=n['location'],currentArea=area,healthMultiplier=1,successBonus=0,damageModifier=0,damageReductionModifier=0,initialKnown=False,initialRelationship=0,visualDescription=n['look'],faction=n['faction'],basicInfo=n['public']+'\n\n'+n['look']+'\n\nEquipment: '+n['equipment']+f"\n\n- Gender: {n['gender']}\n- Species: {n['species']}\n- Magic affinity: {affin}\n- Age: {n['age']}",hiddenInfo='Private motive: '+n['want']+'\n\nConcealment and knowledge: '+n['secret']+'\n\nPressure point: '+n['pressure'],personality=n['temperament'],abilities=[n['combat'], 'Affinity practice: '+affin+'. Affinity supports learning; use only finite actual techniques and the person’s level.'])
        w['npcs'][n['name']]=card
    project.write_json(saved,selections)
    project.write_json(HERE/'people-manifest.json',[dict(name=n['name'],major=n['major'],location=n['location'],area=n['actualArea'],affinities=selections[n['name']]['affinities']) for n in seeds])
    return seeds

def vladimir(w):
    n=w['npcs'][VLAD];oldlook=n['visualDescription']
    look='An ordinary-looking, well-aged human man appearing in his mid-forties, with warm brown eyes, medium-length brown hair and a handsome expressive face. A very large dark plum wizard hat shades his brow. His expensive ink-blue and violet coat has unusual brass fastenings and an old soft scarf.'
    n['visualDescription']=look;n['basicInfo']=n['basicInfo'].replace(oldlook,look).replace('A plain ash staff,','An extravagantly expensive, large ornate glass staff with a continuous clear shaft, faceted glasswork and gold fittings that he permits no one else to touch,').replace('apparent age around forty','apparent age in his mid-forties')
    n['personality'][2]='Declines routine lessons, supplies and rescue requests. He never joins a traveling party; an agreed diplomatic meeting is his own independent visit. He is extremely possessive of his expensive ornate glass staff and does not let other people touch it.'

def equipment(w):
    rows=[
      (KEY,'Key','Reusable permission for the Evertree–Caelrath route. Issued by the authorized transit officers after verified bilateral sponsorship. Fixed returns from Caelrath Portal Hall lead to the Evertree without a key.'),
      ('Ardelis Transit Writ','Document','A verified limited travel sponsorship naming its permitted bearer and purpose. It records permission to request the route key, not royal rank or unrestricted palace access.'),
      ('Receiving Transfer Record','Document','Authenticated copied dates, weights and signatures connecting a specific Caelrath patient transfer to the receiving house. It supports only what the entries actually show.'),
      ('Command Circuit Diagram','Document','A verified diagram of the clasp and relay actually examined. It explains a finite isolation procedure, not universal control over souls or foreign devices.'),
      ("Thaurivex's Broken Diadem",'Relic','The fractured regulator recovered after Thaurivex was defeated or safely disabled beneath Caelrath Palace. Its inert fittings recall the end of that apparatus; no bound soul or new spell is stored in it.'),
      ('Violet Court Saber','Weapon','A balanced cavalry-style saber with a plain blue grip. Useful in narrow terrace streets.'),
      ('Starward Shield','Armor','A service shield with a gold celestial device, strong straps and a replaceable inner pad.'),
      ('Canal Hook','Tool','A blunt working hook on one intact pole, for ropes and floating debris. It is not a grappling device that can lift any weight.'),
      ('Caelrath Practice Foil','Weapon','A flexible guarded practice blade for controlled fencing. Its safety depends on actual restraint.'),
      ('Quarry Wedge Kit','Tool','Matched wedges and a small hammer for careful stonework, carried in oiled cloth.'),
      ('Glasswright Lenses','Tool','Protective fitted lenses for ordinary workshop glare and flying fragments.'),
      ('Violet Weather Cloak','Armor','A sturdy wool cloak with a treated outer shoulder and a deep practical hood.'),
      ('Crownwater Survey Cord','Tool','A marked cord and small plummet for short ordinary measurements.'),
      ('Pilgrim Meal Parcel','Consumable','Bread, cheese and preserved fruit wrapped for one ordinary meal.'),
      ('Starflower Salve','Consumable','A modest locally prepared salve for minor skin irritation. Proper treatment and actual item consumption still matter.'),
      ('Palewick Field Notebook','Tool','A tough small notebook with replaceable leaves and a waterproof cover.'),
      ('Brass Clasp Probe','Tool','A fine insulated probe for compatible small mana circuits. Identifying the circuit and using Magitech skill remain necessary.'),
      ('Harbor Rescue Line','Tool','A coiled sound rope with a throwing weight for reachable rescue work.'),
      ('Dalcourt Travel Case','Armor','A robust close-fitting shoulder case that keeps papers dry during ordinary journeys.'),
      ('Amethyst Ward Focus','Tool','A prepared focus for a learned defensive working. It supplies no spell or inexhaustible Mana.'),
      ('Ivory Service Spear','Weapon','One continuous hardwood shaft with a securely attached steel head, built for a trained two-handed guard.'),
      ('Borrowed Institute Lens','Document','A particular borrowed laboratory lens in its labeled case. Return it to its actual owner; the label is a record, not ownership transfer.'),
      ('Glassworks Color Rods','Consumable','A small matched set of colored glass rods for a bounded workshop job.'),
      ('Starward Field Roll','Tool','Clean dressings and practical treatment tools for a trained medic. Ordinary contents do not instantly restore all resources.')]
    for name,cat,desc in rows:
        r=dict(name=name,category=cat,description=desc,bonuses=[])
        if cat in ['Weapon','Armor','Tool','Consumable']:
            r.update(tier='mundane',estimatedValue=65 if cat in ['Weapon','Armor'] else 18)
            if cat=='Weapon':r.update(slot='weapon',bonuses=[dict(type='stat',variable='damage',value=1)])
            elif cat=='Armor':r.update(bonuses=[dict(type='stat',variable='armor',value=3)])
        w['itemTypes'][name]=r

def techniques(w):
    rows=[
    ('Starward Catch','Light Magic',5,'A brief light ward catches one visible incoming line of attack; it does not cancel unrelated threats.',6,2),
    ('Terrace Step','Wind Magic',5,'A controlled gust assists a short deliberate step across sound reachable footing. It is not flight.',5,1),
    ('Canal Brace','Earth Magic',7,'Brace a small existing bank or foothold for one practical crossing; respect loose ground and actual load.',6,2),
    ('Lens Glimmer','Light Magic',12,'Direct a compact glare through a prepared lens toward one visible opponent, allowing a resisted opening.',8,2),
    ('Quiet Bell','Sound Magic',10,'Dampen a small chosen sound source briefly without silencing a whole occupied building.',7,2),
    ('Glass Thread Ward','Enchantment Magic',15,'Anchor a fragile warning thread across one prepared doorway. Breaking it gives a local audible signal.',9,3),
    ('Drowned Breath','Water Magic',20,'Maintain a short-lived pocket of breathable air around the caster’s mouth in calm reachable water; no pressure immunity or unlimited dive.',12,3),
    ('Star Lantern','Light Magic',5,'Shape a small steady light beside a held focus, with controllable brightness and no truth detection.',4,0),
    ('Chain of Measure','Metal Magic',18,'Tension an existing short chain into a temporary brace or binding; an actual target can resist or break it.',10,2),
    ('Waking Echo','Soul Magic',20,'Listen for a recent residual emotional impression at a specific examined site. This is fragmentary evidence, not a compelled confession.',12,3),
    ('Cradle Stillness','Soul Magic',30,'Briefly steady a damaged compatible spirit binding while someone performs actual containment work. It cannot enslave an unwilling person.',18,4),
    ('Crownlight Intercept','Light Magic',35,'Meet one visible hostile spell with a focused light screen. Opposed power and the supplied result decide how much it stops.',20,4),
    ('Silver Pivot','Finesse Combat',5,'Turn a close weapon bind into one measured countering attack or escape, using actual reach and footing.',4,1),
    ('Gatekeeper Brace','Guarded Combat',7,'Set a shield and supported stance against one approaching impact. It does not make the fighter immovable.',5,1),
    ('Service Spear Line','Force Combat',12,'Present one intact long weapon on a compact intercepting line; resolve one committed attack.',6,2),
    ('Under the High Guard','Finesse Combat',18,'Change line beneath a high guard and make one close thrust. Awareness and supplied success determine the opening.',8,2),
    ('Hold the Landing','Guarded Combat',23,'Use a supported stance and shield to contest one narrow landing for a brief exchange, without taunting or controlling everyone nearby.',10,3),
    ('Regulator Isolation','Magitech',15,'Isolate one identified compatible circuit with actual tools and a sound shutdown sequence. Unknown machines still require investigation.',6,2),
    ('Measured Overload','Magitech',30,'Use a prepared bounded discharge to disable one understood exposed circuit, risking the device itself on failure.',12,4),
    ('Falling Star Cut','Light Magic',28,'Infuse one committed descending weapon attack with a narrow light edge; the light is part of the same resolved hit.',16,3)]
    for name,skill,req,body,cost,cd in rows:
        resource='Stamina' if 'Combat' in skill or skill=='Magitech' else 'Mana'
        requirements=[dict(type='skill',variable=skill,amount=req)]
        if name=='Falling Star Cut':requirements.append(dict(type='skill',variable='Force Combat',amount=20))
        w['abilities'][name]=dict(name=name,description=body+f' Costs {cost} {resource} on commitment, including a failed attempt. No automatic second hit or invented damage total.',requirements=requirements,bonus=min(7,max(1,req//6)),cooldown=cd)

def encounters(w):
    rows=[
    ('Cellar Grain Rat','A small grain-fed rat in a food cellar. Weak tier, level 1-2, successBonus -20, damageModifier -50, healthMultiplier 0.6. One initially, no sudden pack or lethal poison.'),
    ('Orchard Gnawer','A fist-sized hard-shelled beetle chewing young fruit trees. Weak tier, level 1-3, successBonus -20, damageModifier -45, healthMultiplier 0.65. Nets, trapping and removing spoiled fruit are useful.'),
    ('Culvert Scavenger','A low long-bodied territorial animal drawn to dumped food. Level 7-10. Tracks, smell and chewed waste warn before its cramped resting place; it can be lured away.'),
    ('Quarry Skitter','A stone-colored six-legged lizard on warm quarry faces. Level 8-13; one adult or a visible pair. It guards a crevice rather than hunting the entire city.'),
    ('Glass Shardling','A finite cluster of animated workshop glass. Level 15-20. A damaged focus sustains it, with a physical shutoff and fragments that do not multiply infinitely.'),
    ('Intake Crawler','A plated mineral-feeding creature in neglected water intakes. Level 18-25. Its heavy body is visible before engagement; clearing its food can draw it away.'),
    ('Drowned Harness','A limited spirit remnant tangled in old wreck equipment. Level 22-28. It guards one compartment or repeats a past task; naming it does not automatically free it.'),
    ('Crown Ward Sentinel','A decommissioned civic guard construct at a bounded post. Level 30-38. Its control plate, warning light and activation range can be studied. It is not Thaurivex.'),
    ('Receiving Attendant Construct','A purpose-built wheeled restraint assistant in the palace laboratory, level 25-32. It follows a finite apparatus circuit and can be jammed or disabled; not a ubiquitous city patrol.'),
    ('Cradle Ward Husk','An incomplete brass-and-ceramic laboratory guard, level 30-38. Telegraph its grounded cable and guarded line before a fight. A controlled shutdown can neutralize it.'),
    ('Glass Knives Enforcer','A mortal criminal who intimidates, steals and protects a limited local operation. Usually level 18-27. Individual motives, fear, witnesses and actual local law matter.'),
    ('Glass Knives Lookout','A local adult paid to watch one approach, usually level 10-18. A lookout can flee, lie or bargain; not every hired watcher is a skilled assassin.'),
    ('Imperial Deserter','An armed former soldier, usually level 20-30, avoiding or exploiting the crown. Finite camps and real supplies; some want escape, others prey on travelers.'),
    ('Starward Paladin','A trained celestial knight of the Starward Oath, normally level 28-35. A finite Light-supported sword, shield or spear style, with actual orders and individual judgment. Not automatically hostile or a cultist.'),
    ('Unveiled Star Adept','An adult inner-circle cultist using practiced Light, Soul or Enchantment workings, usually level 22-30. Some knowingly coerce recruits; others can doubt. No infinite summons or compelled divine appearance.'),
    ('Terrace Cliffcat','A wary mountain cat on uninhabited escarpments, level 5-10. It avoids busy streets and warns around its den. A hungry animal can remain an animal.'),
    ('Harbor Snapper','A large aggressive fish near exposed pilings, level 4-8. It does not leap into a market to force combat; fishing and boat access still use actual water.'),
    ('Lantern Gull','An ordinary coastal gull with faintly luminous throat feathers. Usually nonhostile, level 1. It steals food, nests and flees; not a secret dungeon boss.')]
    for name,desc in rows:w['npcTypes'][name]=dict(name=name,description=desc,vulnerabilities=[],resistances=[],immunities=[])
    extra=[('Caelrath Courtier','An adult noble, retainer or well-connected visitor with an individual family, taste, obligations and limits. Usually level 12-24; rank is not combat mastery. An extravagant outfit does not prove villainy, wealth without limit or royal access.'),('Caelrath Boutique Artisan','An adult jeweler, perfumer, milliner, embroiderer or luxury seller with actual goods, craft knowledge and prices in marks. Usually level 10-22. Distinguish the working maker from wealthy clients; clothing and patterns vary richly.'),('Caelrath Bard','A working adult singer, instrumentalist, composer or storyteller, usually level 12-25. Performances have their own audience, program and payment. Sound affinity is possible, not mandatory; a beautiful voice is not compelled affection.'),('Caelrath Street Performer','An adult acrobat, puppeteer, comic, dancer or small illusionist, usually level 8-20. They have a routine, a place to work and their own audience; do not make every act a quest or a theft.'),('Sewer Lamplighter','An adult civic maintenance worker with a lamp, sound boots and practical drain knowledge, usually level 12-22. They warn about water rises and distinguish a safe inspection walk from a closed branch. Not automatically a criminal or enemy.'),('Drain Slime','A small slime eating residue in a disused drain. Usually weak tier, level 7-12, damageModifier -25 and healthMultiplier 0.8. One visible body initially; no instant splitting swarm, acid death or hidden palace origin.'),('Copperback Rat','A larger ordinary sewer rat with a copper-colored coat, level 4-8. Signs of nesting precede a finite group. It avoids bright busy inspection routes and is not a carrier of invented instant disease.'),('Cistern Eel','A territorial eel in old flooded maintenance channels, level 10-16. It threatens someone who enters its actual water; it cannot attack through dry walls or teleport between drains.')]
    for name,desc in extra:w['npcTypes'][name]=dict(name=name,description=desc,vulnerabilities=[],resistances=[],immunities=[])
    # Native NPC cards reference these established semantic type labels as well.
    for name in ['Resident','Construct']:
        if name not in w['npcTypes']:w['npcTypes'][name]=dict(name=name,description='Use the individual’s actual anatomy, occupation, intentions and learned capabilities. This type alone grants no hostility, powers or political authority.',vulnerabilities=[],resistances=[],immunities=[])
    w['encounterElements']['Caelrath — Streets and Terraces']='In Ardelis only: market bargaining, a delayed repair, musicians rehearsing, workers disputing a water allocation, pilgrims, a returning adventuring company, a lost delivery or a local celebration. Public circumstances reveal opportunities without automatically accepting quests or exposing private motives. Most ordinary streets remain safe; civilian crowds are not enemy packs.'
    w['encounterElements']['Caelrath — Outer Works and Water']='In Ardelis only: a quarry survey, an orchard pest, a boat waiting on the current, a damaged service line, a wary Cliffcat, or a specific rumor of deserters. Match the actual undertaking and beginner risk; higher threats need visible warning and a deliberate approach. The lower palace is separate optional danger, not a random city encounter.'

def quests(w):
    rows=lines('quests.txt')
    for name,giver,loc,pub,done,brief,reward in rows:Q(w,name,giver,loc,pub,done,brief,int(reward))
    qs=w['parties']['']['quests']
    qs['Ardelis: Passage under Seal'].update(questSource='Reika Kurose')
    qs['Ardelis: Passage under Seal']['objectives']['task']['text']='Have Reika or the informed Glowhaven court representative authenticate a real bilateral Ardelis invitation and agree the named traveler’s purpose. Henri’s remote invitation may be verified by actual court correspondence; no prior Ardelis entry is needed.'
    qs['Ardelis: Passage under Seal']['completionCondition']['query']='The informed Glowhaven court representative actually authenticates a genuine bilateral Ardelis invitation and grants this participating traveler a limited named sponsorship for a credible agreed purpose. Correspondence with Henri may establish the foreign authorization without prior Ardelis entry. The completed local relay case is sufficient grounds to request it, but merely owning evidence, status or an unverified letter is not issuance.'
    chains=[['Rebirth: The Receiving Address','Rebirth: A Voice behind Glass','Rebirth: The Command Circuit','Rebirth: When the Order Comes','Rebirth: What the Crown Received'],['Below the Crown: A Missing Assistant','Below the Crown: The Cooling Galleries','Below the Crown: The Unfinished Sovereign'],['The Star behind the Veil','The Vessel\'s Consent','The Shape of a Miracle']]
    gated=set()
    for chain in chains:
        for first,nxt in zip(chain,chain[1:]):qs[first]['onCompleteEffects'].append(E('quest-init',nxt));gated.add(nxt)
    qs['Below the Crown: The Cooling Galleries']['onCompleteEffects'].append(E('write-boolean',True,key='arLowerReady'))
    qs['Below the Crown: The Unfinished Sovereign']['onCompleteEffects'].append(E('write-boolean',True,key='arCradleResolved'))
    for name in ['Ardelis: Passage under Seal','Ardelis: An Unhelpful Sponsor']:
        qs[name]['onCompleteEffects'] += [E('write-boolean',True,key='arTransitAuthorized')]
    qs['Rebirth: The Receiving Address']['onCompleteEffects'].append(item('Receiving Transfer Record'))
    qs['Rebirth: The Command Circuit']['onCompleteEffects'].append(item('Command Circuit Diagram'))
    qs['Rebirth: When the Order Comes']['onCompleteEffects'].append(E('write-boolean',True,key='arDeploymentStopped'))
    qs['Rebirth: What the Crown Received']['onCompleteEffects'].append(E('write-boolean',True,key='arReceivingConcluded'))
    old=qs['A Second Receiving Station']
    old['questDesignBrief']=old['questDesignBrief'].replace('The remaining lead points to future travel in Ardelis. Do not invent an already accessible Ardelis realm, launch the controlled rival’s attack, claim that the foreign program has ended or leave this undertaking perpetually incomplete. The player can continue ordinary play while preparations beyond the border remain unresolved.','The next lead lies inside Caelrath, Ardelis’s capital. Close this local investigation honestly; it is not proof that the foreign program has ended. Further travel needs actual bilateral sponsorship, available through the independent court route or Vladimir. No immediate rival attack or automatic crossing follows.')
    old['onCompleteEffects'].append(E('quest-init','Ardelis: Passage under Seal'))
    gated.add('Ardelis: Passage under Seal')
    for i,(name,giver,loc,pub,done,brief,reward) in enumerate(rows):
        if name in gated or name.startswith('Rumor:'):continue
        conditions=[C('party-location',loc),C('quest-status','planned',questId=name)]
        if name=='Rebirth: The Receiving Address':conditions.append(C('quest-status','completed',questId='A Second Receiving Station'))
        if name.startswith('Guild:'):
            rank='Gold' if 'Gold badge' in brief else 'Silver' if 'Silver badge' in brief else 'Bronze'
            # The native semantic check evaluates actual held higher ranks too, without rewriting old badge logic.
            query=f"A genuinely licensed {rank}-or-higher participant deliberately asks for, examines or discusses this particular live contract now: {pub} This is not a licensure sample, an unrelated request, generic greetings or indiscriminate board browsing. Do not offer it above the party's experience without an explicit harder-work request. Offer at most one contract this turn. No acceptance is inferred."
            qs[name]['onCompleteEffects'].append(item('Guild Service Credit'))
            # One mechanically selected offer below serves this board. Do not spend
            # thirteen simultaneous semantic evaluations on thirteen planned jobs.
            continue
        else:query=f"The party deliberately follows up this particular actual opportunity with its source or a credible local representative: {pub} Mere arrival, a greeting, incidental gossip or a request about another job is false. Offer at most one undertaking this turn; do not accept it for the player."
        conditions.append(dict(type='action',query=query))
        script="const t=check({type:'game-tick'});if(storage.arOfferTick===t)skip=true;else storage.arOfferTick=t;"
        rule(w,f'ar_offer_{i+1:02}',conditions,[E('quest-init',name),S('Present the particular opportunity '+name+' through the actual source and circumstances. The player may ask questions, refuse or accept. This offers only; no other contract, reward, companion or journey is committed.')],script)
    board=[]
    for name,giver,loc,pub,done,brief,reward in rows:
        if not name.startswith('Guild:'):continue
        m=re.search(r'Suggested levels (\d+)-(\d+)',brief);assert m,name
        board.append(dict(name=name,min=int(m[1]),max=int(m[2]),rank=3 if 'Gold badge' in brief else 2 if 'Silver badge' in brief else 1,premise=pub))
    script="""const rows=BOARD,t=check({type:'game-tick'});
if(storage.arOfferTick===t){skip=true;}else{
const vals=v=>typeof v==='number'?[v]:v&&typeof v==='object'?Object.values(v):[];
const levels=vals(check({type:'player-level'})).filter(v=>typeof v==='number'&&v>0),level=levels.length?Math.min(...levels):1;
const ranks=['Bronze','Silver','Gold','Platinum'];let rank=0;
for(let i=0;i<ranks.length;i++)if(vals(check({type:'player-item',item:'Guild Badge: '+ranks[i]})).some(v=>v>0))rank=i+1;
const raw=[].concat(check({type:'action-text'})||[]).filter(v=>typeof v==='string').join(' ').toLowerCase();
const status=n=>check({type:'quest-status',questId:n});
const available=rows.filter(r=>status(r.name)==='planned'&&rank>=r.rank);
const requested=available.find(r=>raw.includes(r.name.toLowerCase())||raw.includes(r.name.replace(/^Guild: /,'').toLowerCase()));
const harder=/harder|more dangerous|higher.level|challenging/.test(raw);
const suitable=available.filter(r=>level>=r.min&&(level<=r.max+5||r.rank===1));
const pool=suitable.length?suitable:harder?available:[];
const chosen=requested?requested:pool.sort((a,b)=>Math.abs((a.min+a.max)/2-level)-Math.abs((b.min+b.max)/2-level))[0];
if(!chosen){skip=true;}else{storage.arOfferTick=t;effects.push({type:'quest-init',operator:'set',value:chosen.name},{type:'story',instruction:'Aveline presents one actual eligible notice: '+chosen.premise+' This is an offer only; no acceptance, journey or payment occurs. Answer questions and allow refusal. Do not add other jobs or present an assessment sample as a live contract.'});}
}""".replace('BOARD',compact(board))
    rule(w,'ar_guild_board',[C('party-location',GUILD),dict(type='action',query='A genuinely licensed participant deliberately asks Aveline or the live board for actual available guild work, a further notice or a particular contract now. Greetings, an assessment sample, fictional client discussion, first-time registration, hypothetical plans, merely passing the board and a current job report do not qualify. The configured selection offers one eligible live contract, never accepts it. Respect the actual participating party and any explicit harder-work request.')],[],script)
    # Existing saves with a finished Glowhaven chapter get the same follow-up, without replaying its rewards.
    rule(w,'ar_existing_lead',[C('quest-status','completed',questId='A Second Receiving Station'),C('quest-status','planned',questId='Ardelis: Passage under Seal'),C('party-location',"The Grand Sage's Court")],[E('quest-init','Ardelis: Passage under Seal')])
    lic=copy.deepcopy(qs['Guild: Adventurer Licensure']);name='Guild: Caelrath Licensure';lic.update(name=name,questSource='Aveline Marchand',questLocation=GUILD,status='planned');lic['questDesignBrief']=lic['questDesignBrief'].replace('Komugi Hanabishi','Aveline Marchand')+' Existing genuine badges are recognized. A partially completed assessment from another branch can be resumed using its actual pass records, without re-awarding an old badge.';qs[name]=lic
    for suffix in ['register','judgment','practical','certify']:
        r=copy.deepcopy(w['triggerDefinitions']['gh_guild_exam_'+suffix]);r['name']='ar_guild_exam_'+suffix
        r=json.loads(json.dumps(r,ensure_ascii=False).replace("Adventurer's Guild - Glowhaven Branch",GUILD).replace('Guild: Adventurer Licensure',name))
        w['triggerDefinitions'][r['name']]=r
    return [r[0] for r in rows]+[name]

def portals(w):
    r=copy.deepcopy(w['triggerDefinitions']['gh_portal_to_drakenspire'])
    r=json.loads(json.dumps(r,ensure_ascii=False).replace('gh_portal_to_drakenspire','ar_portal_to').replace('Drakenspire Portal Key',KEY).replace('Drakenspire Mountains','Ardelis').replace('Drakenspire Highlands','Kingsward Gate').replace('Drakenspire Portals','Caelrath Portal Hall').replace('Drakenspire - Portal Room','Caelrath Portal Hall - Portal Room'))
    # Retains the actual shared transit lock and the unchanged once-only anomaly branch.
    w['triggerDefinitions']['ar_portal_to']=r
    r=copy.deepcopy(w['triggerDefinitions']['gh_portal_from_drakenspire']);r['name']='ar_portal_from';r['conditions'][0]['value']='Caelrath Portal Hall';w['triggerDefinitions'][r['name']]=r
    rule(w,'ar_issue_key',[C('party-location','Evertree Base'),C('party-area','Evertree Base - Portal Room'),C('player-item',0,item=KEY),C('read-boolean',True,key='arTransitAuthorized'),dict(type='story',query='The authorized Evertree transit delegate actually verifies this traveler’s named bilateral Ardelis sponsorship and hands them the Ardelis Portal Key now. A sponsorship for someone else, merely asking, declaring oneself a noble or student, a forged invitation, or conversation about a future issue is false. Vladimir may vouch for the actual traveler at the agreed meeting; the independent court invitation is equally valid.')],[item(KEY,target='satisfyingPlayers'),S('The authorized delegate hands over the reusable Ardelis route key already recorded by the item effect. It opens the matching Evertree arch for a permitted journey; it grants no palace access or automatic travel. Do not create a second key or a fee.')],scope='player')
    rule(w,'ar_vladimir_meeting',[C('quest-status','accepted',questId='Ardelis: An Unhelpful Sponsor'),C('party-location','Shadowspire'),C('read-boolean',False,key='arVladMeeting'),dict(type='story',query='Vladimir has actually agreed to arrange an authorized Ardelis transit meeting and names the Evertree Portal Room as its place. A request he has declined or an imagined future agreement is false.')],[E('write-boolean',True,key='arVladMeeting'),S('Vladimir arranges his own visit to the Evertree Portal Room with an authorized transit delegate. He does not join the party or teleport them there; their journey remains theirs.')])
    rule(w,'ar_vladimir_arrives',[C('read-boolean',True,key='arVladMeeting'),C('read-boolean',False,key='arVladPlaced'),C('party-area','Evertree Base - Portal Room')],[E('write-boolean',True,key='arVladPlaced'),dict(type='npc-placement',npc=VLAD,operation='moveTo',location='Evertree Base',area='Evertree Base - Portal Room'),S('Vladimir arrives independently for the arranged meeting. The delegate can verify a genuine limited sponsorship after hearing the actual purpose; no one grants a key merely because the party entered the room.')])
    rule(w,'ar_vladimir_departs',[C('read-boolean',True,key='arVladPlaced'),C('read-boolean',False,key='arVladDeparted'),dict(type='player-item',operator='greaterThan',value=0,item=KEY),dict(type='story',query='Vladimir’s actual arranged Evertree meeting has finished after the sponsored key handover, and he takes his own leave. Continuing an unfinished conversation or a key issued through the unrelated independent route is false.')],[E('write-boolean',True,key='arVladDeparted'),dict(type='npc-placement',npc=VLAD,operation='moveTo',location='Shadowspire',area='Shadowspire - Upper Study'),S('Vladimir returns independently to his own study, protecting his expensive glass staff from a too-helpful attendant. The party keeps its actual permission and chooses when to travel.')])
    # One semantic authorization record is shared by these alternate routes. Key issue stays per actual recipient.
    rule(w,'ar_writ_record',[C('read-boolean',True,key='arTransitAuthorized'),C('player-item',0,item='Ardelis Transit Writ'),dict(type='story',query='This participant actually receives their verified limited Ardelis transit sponsorship from the relevant court or authorized delegate. It names their genuine purpose and bearer; permission for a different traveler does not qualify.')],[item('Ardelis Transit Writ',target='satisfyingPlayers')],scope='player')
    area=w['locations']['Evertree Base']['areas']['Evertree Base - Portal Room']
    area['description']=area['description'].replace('Stone-framed arches serve the Drakenspire and Asterveil routes.','Stone-framed arches serve the established distant routes.').replace('The room receives return traffic from both routes. Destination keys select the two ordinary outbound arches.','The room receives return traffic at fixed arches. Issued destination keys select their matching outbound passages.')+' A separate ivory-and-violet arch serves Caelrath in Ardelis. Its route key requires verified bilateral sponsorship; ordinary academy status is not sufficient. Its fixed return leads to this same room.'

def dungeon(w):
    outside=PALACE+' - Warded Crossing';heart=PALACE+' - Resonance Cradle'
    deny=[E('party-location',PALACE),E('party-area',outside),dict(type='npc-placement',npc='allPartyNPCs',operation='moveTo',location=PALACE,area=outside),S('The cradle approach is still unsafe: the cooling feed and warded crossing have not actually been made passable. The party stays at the warded crossing, with a real route back up the service galleries. Describe the warning and obstacle, not a successful entry, boss attack or reward.')]
    early="const raw=[].concat(check({type:'action-text'})||[]).filter(v=>typeof v==='string').join(' ').trim();if(!/^(?:(?:i|we)\\s+)?(?:attempt to\\s+)?(?:go|head|walk|move|enter|descend|jump|teleport|cross)\\b/i.test(raw)||!/resonance cradle|thaurivex|cradle door|boss (?:room|chamber)/i.test(raw))skip=true;"
    rule(w,'ar_cradle_guard',[C('party-location',PALACE),C('read-boolean',False,key='arLowerReady')],deny,early,phase='planning')
    rule(w,'ar_cradle_backstop',[C('party-area',heart),C('read-boolean',False,key='arLowerReady')],deny,phase='state')
    rule(w,'ar_diadem_recovery',[C('party-area',heart),C('read-boolean',False,key='arDiademRecovered'),dict(type='story',query='The actual party safely recovers Thaurivex’s detached broken diadem after its real defeat or a completed safe containment and regulator shutdown. It has been physically made inert and taken, not merely seen or promised. The construct remains one persistent individual. Do not recover it through an active hostile body or call a still-active vessel defeated.')],[E('write-boolean',True,key='arDiademRecovered'),item("Thaurivex's Broken Diadem"),S('Record the inert broken regulator already granted. It is a physical reminder of this actual outcome, not a new bound soul or spell. Honor Thaurivex’s fate and any surviving fragments; do not respawn it or duplicate the relic through the quest reward.')])

def lore(w):
    entries={
    'Ardelis — Crown, Country and Provinces':'Ardelis is a large predominantly human empire with agricultural provinces, older administrative cities and competing military frontiers. Caelrath is its capital, not the whole country. Its rulers retain the familiar titles King and Queen while governing an imperial realm. Cedran Aurevain wants to restore imperial influence during his remaining years; different provinces bear different costs. The capital’s elegant stonework and elaborate water infrastructure depend on ordinary farmers, masons, boat crews and clerks. This map contains Caelrath and its immediate working approaches. Distant imperial cities remain part of the wider world rather than additional destinations on this capital map.',
    'Ardelis — Celestial Worship':'Astraeon, called the High Star, is the ancient celestial deity prominently honored in Ardelis. His existence does not establish the correctness of every priest, royal order or interpretation. Public worship includes ordinary services, memorials, music, relief work and family observances. Laurent Bellegarde leads the capital cathedral. Paladins serve the crown and faith through a distinct order, with differing loyalties. A secret splinter circle, the Unveiled Star, seeks physical communion through a coercive vessel rite; its ambitions are not the doctrine or knowledge of every believer. The deity is not automatically compelled to appear because someone finishes a diagram.',
    'Ardelis — Provinces and Ordinary Life':'The empire’s other cities and provinces supply grain, livestock, timber, mineral work, harbors and workshop labor. Their interests do not always match Caelrath’s court. Within the capital, tenants organize repairs, apprentices argue over credit, merchants extend risky loans and families make practical plans. Ordinary residents are not uniformly cruel, religious, military or interested in the receiving project. Civilian trades and public services remain playable after any royal scandal.',
    'Ardelis — Caelrath Geography':'Caelrath occupies connected mountain terraces above coastal and river-fed lower water. North is up: Starfall Heights, Crownwater Terraces, the Imperial Crown and High Arcana Ward form the upper row; Westbridge, Violet Market, Celestial and Eastwater wards the middle; Windmill Escarpment, Kingsward Gate, Southbank and Lantern Harbors the lower. Water descends through reservoirs, controlled channels and cascades. Bridges, streets, locks and service stairs connect the levels. They are physical terrain, not automatic teleporters. The palace and Hall of Mirrors belong to the same high royal complex. The waterways are not bottomless sky gaps; the city is not a floating island.',
    'Ardelis — Houses and Succession':'House Aurevain’s adult daughters have separate lives: Lysandra is an officer concerned with military competence; Marielle wants artistic independence and has made dangerous financial promises; Céleste is a novice researcher who wants her work taken seriously. The crown has not announced a new succession settlement. Montrevel controls grain and landed credit, Dalcourt commercial finance, Veymont military patronage and Orselle cultural access. These are influences, not compulsory careers for every relative. Marriages, contracts, rivalries and personal loyalties can matter without making every conversation a succession crisis.',
    'Ardelis — Starward Paladins':'The Order of the Starward Oath combines formal arms, celestial devotion and crown service. Its capital commandery has three particularly visible figures: Aurélian Vauss, a proud protective commander; Séraphine Duvray, a courageous zealot willing to excuse coercion; and Osmond Verain, a field chaplain troubled by what he has treated. A paladin may protect a crowd, investigate a threat or obey a bad order. The order is distinct from Corvin Hale’s palace household guard, the ordinary watch and Sabine’s secret cult. Named leaders retain their levels and identities; routine detachments use the Starward Paladin type and finite numbers.',
    'Ardelis — Guild and Local Work':'The Caelrath Branch belongs to the same Adventurer’s Guild as Glowhaven and Benitsuru. Genuine existing badges and partial assessment results are recognized. Aveline Marchand handles reception and Bastien Rochefort runs the branch. Judgment uses a labeled hypothetical sample; the practical is a bounded onsite demonstration. Neither is a live work contract. Certification alone grants the canonical Bronze Document badge, with no duplicate Relic, key or fee. Offer one relevant real contract after licensing or a deliberate later request. Beginner work includes rats, orchard pests, deliveries and repairs; Silver and Gold work can be declined. Prices and wages use marks only, and configured native payouts are not paid again in dialogue.',
    'Ardelis — Passage and Jurisdiction':'The Evertree and Caelrath Portal Hall are the fixed endpoints of a restricted bilateral route. A reusable Ardelis Portal Key works like the existing destination keys after an authorized actual handover. Genuine named sponsorship and a credible purpose matter; academy membership or a claim to nobility is insufficient. Vladimir can arrange an independent meeting at the Evertree without joining a party. Glowhaven’s court and Henri Valcour provide an earned alternative route. Physical return from Caelrath’s sole fixed return arch always reaches the Evertree Portal Room and does not need a key. An Ardelis start grants no automatic international permit. Local offenses do not use Glowhaven’s Wraith Island automatic custody system.',
    'Ardelis — Schools and Visitors':'Caelrath Institute of Magic teaches local adult apprentices through practical demonstrations, observed experiments and scholarly work. It is not a fifth Glowhaven academy and does not share their academic clock or grant their credentials. Glowhaven academies do not assign expeditions into Ardelis. A student may independently visit with valid travel permission for personal or civilian purposes, which does not become automatic expedition credit. Noelle’s unusual affinity range is exceptional: affinities allow study, while finite actual learned techniques and current resources govern casting. Time remains restricted.',
    'Ardelis — Everyday Access and Housing':'Public squares, market lanes, ordinary quays and open service counters are everyday civic places. Private homes, workshops after hours, royal rooms and controlled institutes require the real occupant’s agreement or another feasible means of access. The ordinary housing convention applies: a genuine completed rent or purchase can create a specific key naming the actual room/address, owner or renter and terms. The key remembers a real agreement; it is not a second payment, blanket deed or claim on the entire ward. Never invent recurring away-time rent charges beyond the terms.',
    'Ardelis — Receiving Program and Outcomes':'The linked receiving investigation follows actual authenticated evidence from Glowhaven. Noelle is a separately summoned adult from a nonmagical alternate Earth, not automatically the player’s compatriot or enemy. The apparatus constrains particular actions through a painful command link; it does not make her whole personality evil. A valid interruption must affect the actual circuit, command or protective situation. Do not spring her attack on every visitor or erase the player’s court evidence when they decline Vladimir. Different outcomes can protect her, suppress or expose evidence and leave different people in power. Resolving one operation does not conquer the whole empire or end every war.',
    'Ardelis — Lower Palace Expedition':'Below Caelrath Palace, the Service Stair leads through the Receiving Cellar, Calibration Gallery, Cooling Vault and Warded Crossing to the Resonance Cradle. Upper service and warning rooms precede the optional level-35–45 danger. A genuine cooling-feed and crossing solution establishes a passable final approach; a credible technical or practical method can work without killing every guard. Earlier discoveries persist across retreat. Thaurivex is one fabricated sovereign vessel containing damaged war-spirit remnants, not a summoned god. Its regulator can be disabled or its body defeated. Its broken diadem becomes a finite inert relic only after a real safe recovery; the undertaking does not pay a second copy.',
    'Ardelis — People and Relationships':'Cedran and Isabeau are married, and Lysandra, Marielle and Céleste are their adult daughters. Isabeau has separate adult affairs with Adrien Veymont and Elise Vaubert; secrecy and jealousy do not imply anyone’s blanket consent. Adrien is Armand’s adult son. Julienne and Marcel are mother and adult son. Hector is Lucille’s uncle. Mireille and Isaline are adult cousins. Félicien and Léonie are adult cousins. Aveline and Luc are siblings; she is tired of rescuing him from poor plans. Lydie and Hervé Valette are married, affectionate and able to quarrel about real household decisions. Léonie and Denis are fellow adult students with a competitive friendship. Coralie trusts Matthieu’s careful work when he actually checks it. Do not invent romantic ties for everyone else or infer that a single character is available.',
    'Ardelis — Public Opportunities':'Let a queue, visible faulty work, a returning expedition, a missing delivery or a local performance expose a public circumstance. It can lead to an optional question rather than an automatic quest acceptance. Local people work, rest, see relatives and refuse requests on their own terms. Named residents begin at credible home or work sites; their ordinary movement follows established local routines, not a fabricated exact global schedule. A street vendor knows observed gossip, not royal hidden information. Distinguish seeing a problem, accepting work, performing it and receiving its actual configured reward.'
    }
    for k,t in entries.items():w['worldLore'][k]={'text':t}
    w['worldLore']['Ardelis — Luxury, Performance and the Underworks']={'text':'Caelrath is a wealthy imperial capital. Opaline Arcade has jewelers, perfume salons and couture boutiques, while the Violet Market and ordinary neighborhood trades serve different budgets. Noble households patronize bards, instrumentalists, actors and dancers at the Velvet Lyre Hall, amphitheatre, theatre and private salons; performers also have wages, rivals and artistic choices. Colors, fabrics and patterns vary rather than making every resident a violet-uniformed courtier. Most local human names follow the capital’s established European-style naming; foreign residents keep their own names. Beneath the polished streets, Agathe’s maintenance crew tends the sewers from Eastwater access stairs. Storm drains and foul-water channels are separate from sealed drinking-water conduits. Raised inspection walks, sluices, closed branches and a tide outlet make a connected bounded work site, not a magical shortcut to every private cellar. Some abandoned branches shelter small wildlife, slimes or occasional smugglers; maintained streets do not become dangerous merely because drains run below them.'}
    for k in ['Ardelis — Glowhaven and the Former Connection','Ardelis — Delegations and Jurisdiction']:
        w['worldLore'][k]['text']=w['worldLore'][k]['text'].replace('the kingdom','the empire').replace('kingdom authority','imperial authority')
    w['parties']['']['arcs']['ar_civic_water']=dict(id='ar_civic_water',title='A City Fed from Above',status='active',minQuestsForConclusion=2,surfacePremise='In Caelrath, actual lower-ward residents complain that ornamental channels run while their working taps fail; a real disagreement between Coralie, reservoir staff and estate suppliers draws attention to who bears the cost of the capital’s ambitions.',theme='Develop a bounded civic conflict around actual Caelrath water and supply work. Coralie, René, Clément and local households have their own interests. Use generated developments only beyond the already configured Water for the Lower Steps and grain contracts; never duplicate their completion or payment. No foreign academy expedition, automatic revolution, hidden cult behind every leak or forced rescue.',expectedConclusion='A real workable allocation, safe repair or enforceable settlement changes the affected households’ supply and records who paid or lost influence. A technically sound compromise can leave people angry. Preserve the actual outcome after travel.',secrets=['The feeder was initially closed for a genuine structural fault, then privileged allocations continued.','Montrevel’s grain-credit crisis increases pressure on officials but does not mean every noble is in one conspiracy.'])

def starts(w):
    rows=[
    ('🛡️ Ardelis: The Caelrath Counter',GUILD,'Reception Counter','Rumor: Work beneath the Stars','Begin in Caelrath, capital of the Empire of Ardelis. A returning company is arguing over its last job while you approach the local Adventurer’s Guild. Apply, bring an existing badge or ask about work.',
     'A shield hits the floor with a tired wooden knock. Its owner lowers himself onto a bench while the archer beside him shakes water from her coat.\n\n“You said the lower passage was dry,” Romane says.\n\n“It was,” Quentin replies. “When I asked.”\n\nA woman at the counter finishes counting a small payment into another adventurer’s hand. Behind her, real notices cover a board beneath a violet guild banner. She looks past the wet footprints, then toward you.\n\n“Aveline Marchand. Existing badge, first application, or a question?”\n\nThrough the open door, a cart clatters across the bridge between terraces. The city carries on around the queue.'),
    ('🏘️ Ardelis: A Place in Southbank','Southbank Homes','Front Lane','Rumor: A Room and a Living','Begin among the households of Southbank in Caelrath, Ardelis’s capital. Potters, repairers and neighbors have work to finish and opinions about the water supply. Your reason for being here is yours.',
     'Water arrives at the shared tap in a reluctant cough. Lydie Valette holds a basin beneath it while her husband leans a repaired cart wheel against the wall.\n\n“If you tell me the upper fountains are running again,” she says, “I’m carrying this bucket uphill myself.”\n\nHervé opens his mouth, considers it, and begins checking the wheel instead.\n\nBeyond the little yard, white roofs climb toward a palace bright with gold. Here the morning smells of damp clay and somebody’s bread. Lydie notices you by the lane.\n\n“You looking for a particular door?”'),
    ('🔬 Ardelis: An Institute Place','Caelrath Institute of Magic','Reading Room','An Experiment with Witnesses','Begin at Caelrath’s own magical institute in Ardelis, as an adult apprentice or visiting learner. A demonstration slot is open; you decide what question your actual training can answer.',
     'A small lens rolls across a table. Denis catches it before it reaches the edge, then sees Léonie watching him.\n\n“That one is mine,” she says.\n\n“I know.”\n\n“You put your name on the case.”\n\nOlivier Nacre places a kettle on the warmer and lets the silence do some work. Outside the reading-room windows, water spills from the next terrace in a steady silver sheet.\n\nHe turns to you. “You’ve arrived in time for the demonstration list. Tell me what you actually know how to do, and what you want to find out.”'),
    ('🎭 Ardelis: An Orselle Invitation','House Orselle Salon','Reception Salon','The Player of Small Parts','Begin in Caelrath, Ardelis’s capital, with an appointment at House Orselle. You might be a hired specialist, performer, guest or petitioner. The household has its own disputes before you arrive.',
     'A musician stops halfway through a phrase behind the salon doors.\n\n“Again,” says a woman inside.\n\n“The instrument needs tuning.”\n\n“Then we agree about the problem.”\n\nIsaline Orselle meets you beneath a painted garden screen, an appointment card in her hand. The room beyond is bright with violet cloth, pale wood and the unhurried expense of people who expect things to be ready.\n\n“Mireille is listening to the rehearsal,” she says. “Before I interrupt her—what name should I announce, and what have you come to discuss?”')]
    for name,loc,label,q,desc,story in rows:
        areas=w['locations'][loc]['areas'];area=loc+' - '+label
        if area not in areas:area=next(iter(areas))
        instruction='[Begin in Ardelis, in the named existing room. Preserve the selected background, real badge or novice status and actual skills. These adults attend to their own business. End before the player answers or commits to a task. No free rank, key, royal access, main-story knowledge or automatic romance.]\n\n'
        w['storyStarts'][name]=dict(name=name,description=desc,storyStart=instruction+story,locations=[loc],locationAreas=[area],startingQuests=[q],startingItems=[dict(item='Mark',quantity=1000)],startingPartyNPCs=[],isDefault=False,questGenerationGuidance='This is Caelrath in Ardelis, with its own local lives and institutions. Keep the opening opportunity optional. Only actual agreement begins a live job; the institute exercise is not an expedition. Restricted international travel follows a real authorization and crossing. Continue after the player’s chosen action.')
    new_names=[r[0] for r in rows];ordered={};inserted=False
    for name,value in w['storyStarts'].items():
        if name in new_names:continue
        if not inserted and 'First Day of Work' in name:
            ordered.update({k:w['storyStarts'][k] for k in new_names});inserted=True
        ordered[name]=value
    if not inserted:ordered.update({k:w['storyStarts'][k] for k in new_names})
    w['storyStarts']=ordered

def review(before,after,contents):
    rows=[]
    def walk(a,b,path):
        if a==b:return
        if isinstance(a,dict) and isinstance(b,dict):
            for k in a.keys()|b.keys():
                if k not in a:rows.append(dict(path=path+[k],kind='added',afterHash=digest(b[k])))
                elif k not in b:rows.append(dict(path=path+[k],kind='removed',before=a[k]))
                else:walk(a[k],b[k],path+[k])
        else:rows.append(dict(path=path,kind='changed',before=a,afterHash=digest(b)))
    walk(before,after,[])
    return dict(baseHash=digest(before),afterHash=digest(after),contents=contents,rows=sorted(rows,key=lambda r:compact(r['path'])))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--install',action='store_true');args=ap.parse_args()
    source=project.load(HERE/'source.json');raw=BASE.read_bytes()
    assert hashlib.sha256(raw).hexdigest()==source['baseWorldSHA256'],'Canonical changed; merge the new export before building, never overwrite it.'
    before=json.loads(raw);w=copy.deepcopy(before)
    pins=places(w,source);factions(w);seeds=people(w);vladimir(w);equipment(w);techniques(w);encounters(w);questnames=quests(w);portals(w);dungeon(w);lore(w);starts(w)
    # Apply only a successful exact-name official receipt from this batch, never a guessed URL.
    receipt=HERE/'portrait-urls.json'
    if receipt.exists():
        for name,url in project.load(receipt).items():
            assert name in [n['name'] for n in seeds if n['major']]+[VLAD]
            assert url.startswith('https://')
            w['npcs'][name]['portraitUrl']=url
    images=HERE/'location-urls.json'
    if images.exists():
        for name,url in project.load(images).items():
            assert name in [p['name'] for p in pins] and url.startswith('https://')
            w['locations'][name].setdefault('images',{})['establishingShot']={'imageUrl':url,'crop':{'focus':{'x':50,'y':50},'zoom':100}}
    areas=HERE/'area-urls.json'
    if areas.exists():
        for address,url in project.load(areas).items():
            loc,area=address.split('::',1);assert area in w['locations'][loc]['areas'] and url.startswith('https://')
            w['locations'][loc]['areas'][area].setdefault('images',{})['establishingShot']={'imageUrl':url,'crop':{'focus':{'x':50,'y':50},'zoom':100}}
    project.write_json(OUT/'The Schools of Magic, Arise! - Ardelis.json',w)
    contents=dict(npcs=[s['name'] for s in seeds],majorNPCs=[s['name'] for s in seeds if s['major']],quests=questnames,locations=[p['name'] for p in pins],regions=[b for a,b,c in lines('regions.txt')],newItems=[k for k in w['itemTypes'] if k not in before['itemTypes']],newAbilities=[k for k in w['abilities'] if k not in before['abilities']],newTypes=[k for k in w['npcTypes'] if k not in before['npcTypes']])
    project.write_json(HERE/'review.json',review(before,w,contents));project.write_json(HERE/'placements.json',pins)
    project.write_json(OUT/'Ardelis - NPCs.json',{k:w['npcs'][k] for k in contents['npcs']+[VLAD]})
    project.write_json(OUT/'Ardelis - Locations.json',{k:w['locations'][k] for k in contents['locations']})
    print(compact(dict(candidate=str(OUT),counts={k:len(v) for k,v in contents.items()},units={k:project.units(compact(w[k])) for k in ['itemTypes','npcs','triggerDefinitions']},afterHash=digest(w))))
    if args.install:project.write_json(BASE,w)

if __name__=='__main__':main()
