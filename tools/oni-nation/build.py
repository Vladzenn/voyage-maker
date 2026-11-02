#!/usr/bin/env python3
"""Build the approved expansion from the explicitly supplied current Studio export."""
import argparse, copy, hashlib, json, pathlib, random, re, sys
from geography import NATION, CAPITAL, SPIRIT, REGIONS, SITES, SPIRIT_SITES, AREA_DETAILS
from cast import PEOPLE, YOKAI
from quests import JOBS, ARCS
from equipment import GEAR, TECHNIQUES, TALENTS

ROOT=pathlib.Path(__file__).resolve().parents[2]
HERE=pathlib.Path(__file__).resolve().parent
def dump(p,v):
    p=pathlib.Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
def digest(v):return hashlib.sha256(json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def lines(s):return [x.split('|') for x in s.strip().splitlines() if x.strip()]
def story(text):return {'type':'story','instruction':text}
def put(k,v,collection):
    if k in collection:raise ValueError('Existing key would be replaced: '+k)
    collection[k]=v

def areas_for(name, labels, public):
    out={}
    for i,label in enumerate(labels):
        detail=AREA_DETAILS.get(label)
        if not detail:
            if any(x in label.lower() for x in ['store','shed','rack','supply']):detail=f'The {label.lower()} holds the actual goods and tools used at {name}. Kept passages let workers reach the supplies without disturbing the whole place.'
            elif any(x in label.lower() for x in ['path','trail','walk','lane','steps','stair']):detail=f'The {label.lower()} connects the nearby parts of {name}. Changes of surface and sightline make the approach readable; the route remains available for an ordinary return.'
            elif any(x in label.lower() for x in ['court','yard','hall','room','veranda','porch']):detail=f'The {label.lower()} is a usable part of {name}, with work surfaces or clear standing space fitted to the people who use it. Voices and activity from the adjoining space carry across its entrance.'
            else:detail=f'{label} is a distinct stopping point at {name}. The ground, visible approach and nearby cover make it possible to observe before committing to the next stretch.'
            # Carry the unique concrete local scene into each place's presentation.
            detail += ' '+public.split('. ')[0].rstrip('.')+'.'
        key=name+' - '+label
        near=[labels[j] for j in range(len(labels)) if j!=i and (i==0 or j==0 or abs(j-i)==1)]
        out[key]={'description':detail,'paths':[name+' - '+x for x in near]}
    return out

def add_geography(w):
    source_realm=w['realms']['New Realm']
    realm=copy.deepcopy(source_realm)
    realm.update(name=NATION,initialKnown=True,basicInfo='Akitsuhara is an inland Oni-majority country of one great capital, two smaller castle towns and broad inhabited countryside. Benitsuru stands below Mount Shiun; Mizuhara serves the western lake country and Koganedai the eastern terraces. A Shogun governs alongside powerful territorial households, civic officers and independent institutions. Ordinary roads, fields, ferries, shrines, trades and homes continue through their disagreements. Some clans import expensive magitech crossbows, swords and armor; most daily life remains traditional. The authorized capital transit torii connects with the Evertree. A different old torii near Lanternwood opens onto fog-shrouded spirit wilderness after a local way bell is restored.')
    w['realms']={NATION if k=='New Realm' else k:realm if k=='New Realm' else v for k,v in w['realms'].items()}
    region_ids={f'Region {i+1}':v[0] for i,v in enumerate(REGIONS)}
    w['regions']={region_ids.get(k,k):({**v,'name':region_ids[k],'realm':NATION,'basicInfo':REGIONS[int(k.split()[1])-1][2],'initialKnown':True,'npcLevelRange':dict(zip(['min','max'],REGIONS[int(k.split()[1])-1][1]))} if k in region_ids else v) for k,v in w['regions'].items()}
    put(SPIRIT,{'name':SPIRIT,'initialKnown':False,'basicInfo':'A fog-shrouded spirit wilderness reached through the local Soul Torii in Akitsuhara. Towering trees, dark reeds, pale flowers and abandoned festival ways disappear into moving mist. Enormous half-seen shapes and borrowed voices make the landscape unsettling; inhabitants are not uniformly friendly or hostile. A dependable threshold leads back to Moonless Torii. Raised paths and a dry refuge permit cautious observation, while deeper approaches shelter real danger.'},w['realms'])
    put('Veiled Cedar Reach',{'name':'Veiled Cedar Reach','realm':SPIRIT,'x':0,'y':0,'initialKnown':False,'basicInfo':'Dense fog layers a compact wilderness of cedar roots, wet low ground and an old festival road. The western threshold and Bellroot Refuge are usable staging places. Lantern Marsh and the listening woods lead toward a crane crossing and a more dangerous pale grove. These sites share physical paths; voices and fog do not transport someone without actual movement.','npcLevelRange':{'min':15,'max':35}},w['regions'])
    added=[];groups={}
    for number,data in [*SITES.items(),(0,SPIRIT_SITES)]:
        region='Veiled Cedar Reach' if number==0 else REGIONS[number-1][0]
        groups[region]=[]
        for name,x,y,band,public,labels,types in lines(data):
            lo,hi=map(int,band.split('-'));labels=labels.split(';')
            hidden=f'LOCAL PLAY: {"Safe inhabited services; ordinary visits do not spawn a fight." if lo<=5 else "Respect signs, actual occupants and an available retreat. The local band describes ordinary new encounters, not a required fight."} '
            if types:hidden+='Habitats can use these actual npcTypes when appropriate: '+types+'. Generate a finite encounter, preserve its actual outcome, and do not replace cleared creatures on a return. '
            if lo<=5:hidden+='For voluntary beginner work use a level 1–3 weak nuisance, one active hostile initially, not an elite or a concealed pack. '
            hidden+='Use the specific current local situation, actual cast and agreed scope. Public news is not automatic acceptance, recruitment or permission. Existing residents and resolved outcomes persist.'
            loc={'name':name,'basicInfo':public,'hiddenInfo':hidden,'x':int(x),'y':int(y),'radius':1.5,'region':region,'complexityType':'complex','detailType':'detailed','areas':areas_for(name,labels,public),'initialKnown':lo<=15,'npcLevelRange':{'min':lo,'max':hi},'factions':[NATION] if number else []}
            put(name,loc,w['locations']);groups[region].append(name);added.append(name)
    # Nearest-neighbor spanning routes within a tile, plus authored province crossings.
    roads=[]
    def join(a,b):
        if [a,b] not in roads and [b,a] not in roads:roads.append([a,b])
    for region,names in groups.items():
        reached=[names[0]];remaining=names[1:]
        while remaining:
            a,b=min(((a,b) for a in reached for b in remaining),key=lambda p:(w['locations'][p[0]]['x']-w['locations'][p[1]]['x'])**2+(w['locations'][p[0]]['y']-w['locations'][p[1]]['y'])**2)
            join(a,b);reached.append(b);remaining.remove(b)
    for a,b in [('Western Watch Road','Quarry Exchange'),('Cedarfall Hamlet','Mizuhara Castle'),('Quarry Exchange','Bamboo Crossing'),('Scree Lantern Pass','Cloudbell Monastery'),('Shiun Pilgrim Lodge','Benitsuru Castle'),('Frost-Eave Approach','Snowcedar Refuge'),('Rime Bridge','Koganedai Muster Ground'),('Mizuhara Landing','Bamboo Crossing'),('Reedshore Hamlet','Mirror-Reed Ferry'),('Bamboo Crossing','Benitsuru Transit Shrine'),('Rainsong Mill','Hoshina Village'),('South Gate Caravan Yard','Redleaf Bridge'),('Lantern Canal Market','Goldleaf Arcade'),('Koganedai Muster Ground','Lanternwood Root Shrine'),('Saltwind Causeway','South River Bridge'),('Low Meadow Paddies','Redleaf Guest Village'),('Evening Maple Shrine','Moonless Torii')]:join(a,b)
    # Explicit safe approach, not a mandatory transit through the monster's hollow.
    join('Evening Maple Shrine','River Lantern Mooring');join('Moonless Torii','Lanternwood Field Shelter')
    # Native area paths remain within one parent location. Ordinary roads between
    # locations are expressed in the setting text, not unsupported area links.
    for name in added:
        neighbors=[b if a==name else a for a,b in roads if name in [a,b]]
        w['locations'][name]['basicInfo']+=' Nearby routes lead toward '+', '.join(neighbors)+'.'
    return added,region_ids,roads

def add_factions(w):
    factions={
      NATION:('major','Akitsuhara is an independent Oni-majority country of towns, farms, shrines, trades and forests. Citizenship does not prescribe a profession, personal loyalty or magical discipline.'),
      'Kagetsuna Shogunate':('major','The Shogunal government under Shōen Kagetsuna coordinates national roads, external agreements and common law. Territorial houses retain real rights; clerks, magistrates and watch officers have defined public duties.'),
      'House Saionoma':('major','Masazane Saionoma’s western household has agricultural, ferry and granary interests. Its relatives and retainers disagree over obligations, access and the extent of local exemptions.'),
      'House Tsubakiri':('major','Kureha Tsubakiri’s eastern household sponsors trade and a small imported magitech workshop. Legitimate apprentices and ordinary relatives are not automatically party to every private scheme.'),
      'Reed Veil Fellowship':('minor','Independent scouts and shinobi train observation, fieldcraft, message work and withdrawal. Yuzuri Kageura negotiates commissions and refuses some orders; membership is neither an ancestry nor universal assassination authority.'),
      'Maple Lantern Custodians':('minor','A loose association of shrine attendants maintains local rites, practical boundaries and public shelters. Custodians disagree about custom and scholarship; they neither own every spirit nor command a single mandatory religion.'),
      'Morning Crane School':('minor','Chinatsu Hanegi’s martial school teaches measured blade work, control and safe practice. Fees and actual training do not grant a household office or permanent allegiance.'),
      'Broken Kite Band':('minor','Renga Itsuzaki’s road band lives on intimidation, stolen goods and opportunistic tolls. Its members can be funny, loyal, frightened or cruel; a joke does not make their victims’ losses harmless.')}
    for name,(kind,text) in factions.items():put(name,{'name':name,'factionType':kind,'basicInfo':text,'hiddenInfo':'Use the actual members, remit, resources and unresolved disputes. Rank is not omniscience; ordinary cooperation does not recruit a person or bind the player to a faction.','initialKnown':kind=='major'},w['factions'])

def design_draws():
    path=HERE/'design-draws.json'
    if path.exists():return json.loads(path.read_text(encoding='utf-8'))
    rng=random.SystemRandom();out={};disciplines=['Arcane','Fire','Water','Earth','Wind','Lightning','Ice','Light','Metal','Nature','Sound','Gravity','Void','Healing','Enchantment','Summoning','Illusion','Divination','Soul']
    for p in PEOPLE:
        roll=rng.randint(1,100);count=1 if roll<=65 else 2 if roll<=90 else 3
        text=p['method'].lower();hits=[(m.start(),k) for k in disciplines if (m:=re.search(r'\b'+k.lower()+r'\b',text))]
        first=min(hits)[1] if hits else rng.choice(['Arcane','Earth','Wind','Nature','Fire','Water'])
        aff=[first]+rng.sample([x for x in disciplines if x!=first],count-1)
        out[p['name']]={'affinityRoll':roll,'affinities':aff,'poseRoll':rng.randint(1,6),'skin':rng.choice(['light','warm tan','medium brown','light olive'])}
    for p,aff in zip(YOKAI,['Void','Illusion','Sound','Soul']):out[p['name']]={'affinities':[aff],'fixedCreatureConcept':True,'poseRoll':rng.randint(1,6)}
    dump(path,out);return out

MAJOR_OUTFITS={
 'Shōen Kagetsuna':'a richly woven deep-blue layered court robe, a patterned russet shoulder mantle and a plain sword at his hip',
 'Ayame Kagetsuna':'a vivid scarlet short haori over dark practical lamellar, white cords and riding trousers',
 'Masazane Saionoma':'a bright green patterned robe under a mustard household coat, with a broad sash',
 'Kureha Tsubakiri':'an elegant white-and-violet patterned court ensemble with dark red layered sleeves',
 'Shigure Tsubakiri':'a black and emerald silk coat with silver geometric panels and a dark magitech wrist fitting',
 'Hiyori Mitsuba':'a bright coral-and-cream kosode, blue patterned short jacket and practical guild waist pouch',
 'Sae Kagurazaka':'white layered shrine clothing with saturated violet and vermilion cords and worn working sleeves',
 'Tōma Sagiri':'a teal traveling haori with a bold cloud pattern over cream layers and worn dark trousers',
 'Yuzuri Kageura':'a fitted plum and charcoal field outfit with patterned sleeves, practical wraps and a loose green shoulder cloth',
 'Genzaburō Kanemori':'an open dark red work coat over a sturdy charcoal apron and indigo working trousers',
 'Kinu Amakusa':'a brilliant orange, turquoise and cream dance ensemble with large floral panels and layered flowing sleeves',
 'Renga Itsuzaki':'a patched yellow-green traveling coat, dark work trousers and mismatched bright sashes'}

def add_cast(w):
    draws=design_draws();added=[]
    level_overrides={'Shōen Kagetsuna':42,'Ayame Kagetsuna':32,'Masazane Saionoma':30,'Kureha Tsubakiri':34,'Shigure Tsubakiri':38,'Tōma Sagiri':30,'Yuzuri Kageura':31,'Genzaburō Kanemori':29,'Sae Kagurazaka':28,'Renga Itsuzaki':27,'Hiyori Mitsuba':18,'Kinu Amakusa':24}
    for index,p in enumerate(PEOPLE):
        name=p['name'];d=draws[name];aff=d['affinities'];g=p['gender'];he='She' if g=='female' else 'He'
        clothing=MAJOR_OUTFITS.get(name,'colorful layered local clothing fitted to '+p['role']+' work')
        appearance=f"An adult {p['species'].lower()} with {d['skin']} skin, {p['look']}. {he} generally wears {clothing}."
        equipment=(p['weapon']+', ' if p['weapon'] else '')+'the working tools of the trade, a small purse and one useful travel or household keepsake'
        basic=f"{name} is {p['role']} in Akitsuhara. {p['public']}\n\n{appearance}\n\n**Equipment:** {equipment[0].upper()+equipment[1:]}.\n\n- **Gender:** {g.title()}\n- **Age:** {p['age']}\n- **Species:** {p['species']}\n- **Role in faction:** {p['role']}\n- **Magic affinity:** {', '.join(aff)}"
        hidden=f"**Private motive:** {p['want']}\n\n**What they conceal:** {p['flaw']}\n\n**Concealment and knowledge:** People directly involved know their own part; acquaintances know the public role and observed behavior. A stranger has not been told the private motive.\n\n**Pressure point:** A choice between the stated ambition and the real cost of the habit or conduct described above.\n\n**Relationships:** {p['ties'] or 'Ordinary colleagues and neighbors know the public work. No additional named close relationship is established.'}\n\n**How it surfaces:** {p['quirk']} Let real work, a disagreement or earned private conversation reveal the rest."
        pressure=p['flaw']+' Under pressure this tendency becomes more visible; the person can reconsider after a concrete consequence.'
        personalities=[f"**Core:** {p['want']}",f"**Default behavior:** {p['public']}",f"**Under pressure:** {pressure}",f"**Speaking Style:** {p['voice']}",
         '**Courtship Style:** '+['Offers time together through an ordinary shared interest, then asks clearly without treating courtesy as reciprocation.','Uses teasing and a specific invitation; rejection can sting without creating a claim on the other person.','Makes practical room in a busy routine and shows interest through attentive conversation.','Reserved at first; a direct invitation matters more than public performance.'][index%4],
         '**Jealousy Style:** '+['Becomes curt and asks an uncomfortable question privately rather than silently acquiring authority over a partner.','Makes a pointed joke, then struggles to admit the insecurity beneath it.','Pulls back and watches too closely before naming the concern.','Gets competitive about a shared interest; a real conversation can expose the hurt.'][index%4],f"**Routine or Quirk:** {p['quirk']}"]
        level=level_overrides.get(name,12+(index*7%13))
        if any(x in p['role'] for x in ['instructor','examiner','teacher','guide','officer']):level=max(level,25)
        weapon=p['weapon'].lower()
        tactic=('Keeps a clear firing lane, uses real cover and moves before a close opponent can pin the shot.' if 'bow' in weapon else 'Uses the weapon’s reach to hold a clear approach and gives ground rather than let an opponent crowd the grip.' if any(x in weapon for x in ['spear','naginata','staff','pole']) else 'Keeps a controlled close line and commits to a single opening before recovering the guard.' if weapon else 'Protects a usable exit, warns nearby people and seeks qualified help rather than prolonging a fight.')
        abilities=[f"**Practiced Method:** {p['method']}",f"**Everyday Magic:** Familiar minor {aff[0]} workings assist appropriate daily tasks.",f"**Fighting Style:** {tactic}"]
        npc={'name':name,'properName':name,'currentLocation':p['place'],'currentArea':next(iter(w['locations'][p['place']]['areas'])),'type':'Resident','detailType':'detailed','tier':'strong' if level>=30 else 'average','level':level,'gender':g,'visualDescription':appearance,'basicInfo':basic,'hiddenInfo':hidden,'personality':personalities,'abilities':abilities,'faction':p['faction'] or NATION,'initialKnown':name in ['Shōen Kagetsuna','Masazane Saionoma','Kureha Tsubakiri'],'portraitUrl':''}
        put(name,npc,w['npcs']);added.append(name)
    for p in YOKAI:
        name=p['name'];aff=draws[name]['affinities'][0]
        npc={'name':name,'properName':name,'currentLocation':p['place'],'currentArea':next(iter(w['locations'][p['place']]['areas'])),'type':p['type'],'detailType':'detailed','tier':'boss' if name=='Hagire' else 'strong','level':p['level'],'gender':p['gender'],'visualDescription':p['look'],'basicInfo':p['public']+'\n\n'+p['look']+f"\n\n- **Species:** {p['species']}\n- **Magic affinity:** {aff}",'hiddenInfo':f"**Private motive:** {p['want']}\n\n**What they conceal:** {p['flaw']}\n\n**Concealment and knowledge:** Direct witnesses know only what they survived or observed.\n\n**Pressure point:** {p['flaw']}\n\n**Relationships:** No unearned bond with the player.\n\n**How it surfaces:** {p['quirk']}",'personality':[f"**Core:** {p['want']}",f"**Default behavior:** {p['public']}",f"**Under pressure:** {p['flaw']}",f"**Speaking Style:** {p['voice']}",'**Courtship Style:** No romantic route is established.','**Jealousy Style:** Responds to rivalry through the particular pride and wants described in this card.',f"**Routine or Quirk:** {p['quirk']}"],'abilities':[p['method']],'initialKnown':False,'initialRelationship':-90 if name=='Hagire' else 0,'portraitUrl':''}
        if name=='Hagire':npc.update(healthMultiplier=1.1,successBonus=5,damageModifier=5,damageReductionModifier=0)
        put(name,npc,w['npcs']);added.append(name)
    # Identify the people who actually handle services, rather than inventing replacements.
    for name in added:
        npc=w['npcs'][name];loc=w['locations'][npc['currentLocation']]
        loc['hiddenInfo']+=' '+name+' is an established local participant; reuse this actual record when the role is needed. Presence follows actual placement, not an automatic party invitation.'
    return added,draws

def add_equipment(w):
    added=[];abilities=[]
    for name,category,tier,price,slot,kind,var,value,desc in GEAR:
        item={'name':name,'category':category,'description':desc,'bonuses':[],'needsMediaGeneration':True}
        if price:item.update(tier=tier,estimatedValue=price)
        if slot:item['slot']=slot
        if kind:item['bonuses']=[{'type':kind,'variable':var,'value':value}]
        put(name,item,w['itemTypes']);added.append(name)
    for name,skill,minimum,bonus,cd,cost,description in lines(TECHNIQUES):
        resource,amount=cost.split(':')
        a={'name':name,'description':description+f' Costs {amount} {resource} on commitment, including a failed attempt. The bonus applies to this single action.','requirements':[{'type':'skill','variable':skill,'amount':int(minimum)}],'bonus':int(bonus),'cooldown':int(cd)}
        put(name,a,w['abilities']);abilities.append(name)
    talents=[]
    for name,desc,attribute,skill,amount in TALENTS:
        tr={'name':name,'description':desc,'traitNarrativeEffects':desc,'attributes':[{'attribute':attribute,'modifier':2 if name=='Borrowed Storm Nerve' else 1}],'skills':[{'skill':skill,'modifier':amount}],'resources':([{'resource':'Stamina','modifier':-10}] if name=='Borrowed Storm Nerve' else []),'startingItems':[],'abilities':[],'unlockedBy':[],'excludedBy':[],'requirements':[]}
        put(name,tr,w['traits']);w['traitCategories']['Special Talent']['traits'].append(name);talents.append(name)
    w['traitCategories']['Special Talent']['subcategories'].append({'name':'Roads and Forms','traits':talents})
    # A few additional optional starting kits; no household membership or mastery implied.
    kits=[('Yari Road Kit','Ash-Shaft Yari'),('Naginata Practice Kit','Garden-Guard Naginata'),('Yumi Road Kit','Maplewood Yumi'),('Watch Hook Kit',"Watchman's Jitte"),('Reinforced Fan Kit','Lacquer-Rib Combat Fan'),('Shrine Staff Kit','Cedar Bell Staff')]
    for name,item in kits:
        desc='Begin with '+item+' and ordinary familiarity with carrying it. This is equipment, not a new office, affinity or automatic martial mastery.'
        put(name,{'name':name,'description':desc,'traitNarrativeEffects':desc,'attributes':[],'skills':[],'resources':[],'startingItems':[{'item':item,'quantity':1}],'abilities':[],'unlockedBy':[],'excludedBy':[],'requirements':[]},w['traits'])
        w['traitCategories']['Starting Equipment']['traits'].append(name)
    return added,abilities,talents

def add_quests(w):
    added=[];catalog=[]
    for title,client,location,level,rank,fee,outcome,scene in lines(JOBS):
        level,rank,fee=int(level),int(rank),int(fee)
        if client not in w['npcs']:raise ValueError('Quest client '+client)
        brief=scene+f' Recommended level about {level}; actual method and risk matter. '
        if rank:brief+='Required badge '+['','Bronze','Silver','Gold','Platinum'][rank]+'. The existing international rank applies; no second licensure or guild fee. '
        brief+='Offer this voluntarily through its actual client or a suitable board. Acceptance is a real agreement. Use the typed native completion and effects as the sole reward owner. No extra required return report unless delivery/report is part of the stated outcome. Do not duplicate money, experience or service credit in prose. Preserve real partial progress and a concluded result.'
        effects=[]
        if fee:effects.append({'type':'item-add','item':'Mark','quantity':fee,'target':'allPlayers'})
        effects.append({'type':'player-experience','operator':'add','value':min(1500,150+level*25),'target':'allPlayers'})
        if rank:effects.append({'type':'item-add','item':'Guild Service Credit','quantity':1,'target':'allPlayers'})
        if title=='A Bell for the Mist':effects.append({'type':'item-add','item':'Restored Way Bell','quantity':1,'target':'allPlayers'})
        if 'Hagire among' in title:effects.append({'type':'write-boolean','key':'oni_hagire_route_safe','operator':'set','value':True})
        effects.append(story('Conclude the agreed undertaking with its real method and consequences. Apply its configured rewards once. Keep returned goods with their actual owner and any further work optional.'))
        q={'name':title,'questSource':client,'questLocation':location,'detailType':'detailed','status':'hidden','questStatement':outcome+(' Posted reward: '+str(fee)+' marks.' if fee else ''),'mainObjective':outcome,'questDesignBrief':brief,'conclusive':True,'completionCondition':{'type':'story','query':'For the accepted undertaking '+title+', actual events have achieved this outcome: '+outcome+' Count a feasible alternative that genuinely accomplishes it. A plan, arrival, boast, another person’s unrelated work or a prior different job is insufficient. Preserve completed work after travel and do not add an unstated compulsory stage.'},'onCompleteEffects':effects}
        put(title,q,w['parties']['']['quests']);added.append(title)
        catalog.append({'title':title,'level':level,'rank':rank,'client':client,'location':location})
        if location in w['locations'] and w['regions'][w['locations'][location]['region']]['realm'] in [NATION,SPIRIT]:
            w['locations'][location]['hiddenInfo']+=' Potential unresolved situation: '+scene+' The associated voluntary undertaking is '+title+'.'
    for arc in ARCS:put(arc['id'],arc,w['parties'][''].setdefault('arcs',{}))
    return added,catalog

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--base',required=True);ap.add_argument('--output',required=True);args=ap.parse_args()
    base=json.loads(pathlib.Path(args.base).read_text(encoding='utf-8-sig'));w=copy.deepcopy(base)
    locations,regions,roads=add_geography(w);add_factions(w)
    from types_and_lore import add_types,add_lore
    types=add_types(w);names,draws=add_cast(w);items,abilities,talents=add_equipment(w);quests,catalog=add_quests(w)
    from creation_patch import apply as apply_creation
    professions=apply_creation(w)
    from guild_patch import apply as apply_guild,add_native_choice
    guild_fix=apply_guild(w)
    from systems import add_systems,add_starts
    triggers=add_systems(w,catalog);starts=add_starts(w);add_lore(w)
    triggers.append(add_native_choice(w,guild_fix['legacyAcceptances']))
    manifest={'baseSha256':hashlib.sha256(pathlib.Path(args.base).read_bytes()).hexdigest(),'scope':'Approved complete Akitsuhara content plus a small fog-shrouded spirit wilderness; major portraits first.','npcs':names,'majorNpcs':[p['name'] for p in PEOPLE+YOKAI if p['major']],'locations':locations,'regions':regions,'items':items,'abilities':abilities,'talents':talents,'npcTypes':types,'quests':catalog,'triggers':triggers,'storyStarts':starts,'preservation':{s:{k:digest(v) for k,v in base[s].items()} for s in ['npcs','locations','npcTypes','triggerDefinitions','abilities','itemTypes','factions','worldLore','storyStarts']},'allowedExistingChanges':{'locations':['Evertree Base'],'worldLore':['Oni — Arcane and Soul Magitech']},'sourceRegionImages':{k:v.get('images') for k,v in base['regions'].items() if v.get('realm')=='New Realm'},'livePlaytest':False}
    # Existing routes, their anomaly owner and all Spider data remain exactly the supplied base.
    for k,v in base['triggerDefinitions'].items():
        if k not in guild_fix['changedTriggers']:assert w['triggerDefinitions'][k]==v,k
    for k,v in base['npcs'].items():assert w['npcs'][k]==v,k
    for k,v in base['locations'].items():
        if k!='Evertree Base':assert w['locations'][k]==v,k
    assert w['aiInstructions']==base['aiInstructions']
    assert w['imagePromptConfiguration']==base['imagePromptConfiguration']
    assert 80<=len(names)<=100,len(names)
    manifest['professions']=professions
    manifest['roads']=roads
    manifest['guildPlaytestFix']=guild_fix
    manifest['allowedExistingChanges']['triggerDefinitions']=guild_fix['changedTriggers']
    manifest['allowedExistingChanges'].update(traits=['Physical Foundations'],traitCategories=['Origin & Upbringing','Profession & Useful Skills','Special Talent','Starting Equipment'],itemSettings=['startingItems'],storySettings=['questGenerationGuidance'],quests=['Guild: Adventurer Licensure'])
    # Verified media receipts can be reapplied on a rebuild; never touch an old portrait.
    hosted=HERE/'hosted-art.json'
    if hosted.exists():
        for r in json.loads(hosted.read_text(encoding='utf-8')):
            if r['target']=='NPC_PORTRAIT':
                assert r['name'] in names
                w['npcs'][r['name']]['portraitUrl']=r['url']
            elif r['target']=='REGION_MAP_IMAGE':
                assert r['name']=='Veiled Cedar Reach'
                w['regions'][r['name']]['images']={'map':{'crop':{'focus':{'x':50,'y':50},'zoom':100},'imageUrl':r['url']}}
    from regression_delta import record
    record(w)
    dump(args.output,w);dump(HERE/'manifest.json',manifest)
    print(json.dumps({'npcs':len(names),'majorPortraits':len(manifest['majorNpcs']),'locations':len(locations),'quests':len(quests),'types':len(types),'abilities':len(abilities),'triggers':len(triggers),'output':args.output},ensure_ascii=False))

if __name__=='__main__':main()
