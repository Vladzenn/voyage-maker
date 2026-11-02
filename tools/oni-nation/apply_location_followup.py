"""Merge the author's placed locations, then apply the approved forest/onsen correction."""
import ast,copy,hashlib,importlib,json,pathlib,random,re,sys
from build import ROOT,HERE,dump

SOURCE=pathlib.Path(r'C:\Users\VladCodes\.codex\attachments\43fe08da-66f0-451e-bf62-281d8f699479\Pasted text.txt')
RENAMES={
 'Benitsuru Guildhall':"Adventurer's Guild - Benitsuru Branch",
 'Mirror-Reed Ferry':'Mirror-Reed Bridge',
 'Reedglass Fishing Village':'Reedglass Woodland Hamlet',
 'White Heron Islets':'White Heron Grove',
 'Singing Reed Marsh':'Singing Cedar Hollow',
 'Old Ferry Shrine':'Old Bridge Shrine',
 'Saltwind Causeway':'Mossbank Ridgeway',
 'Reed Dye Workshop':'Woodland Dye Workshop',
 'Akitsuhara Guild: Cloth on the Other Bank':'Akitsuhara Guild: Cloth on the Forest Road',
 'Akitsuhara Guild: Missing Along the Reeds':'Akitsuhara Guild: Missing on the Ridge',
 'Put an onsen and an npc here':'Hinoki Hollow Onsen'}
REGION_TEXT='Wooded low ridges, cedar paths and a narrow river descending beneath an arched bridge. Reeds gather along the northern water margin, but most of this province is forest, rocky slopes and clearings. Small hamlets, dye gardens and roadside shrines serve walkers and pack traffic; the principal crossing is a bridge.'
SITES={
 'Mirror-Reed Bridge':('A red-lacquered timber bridge crosses a clear river between wooded banks. A path-keeper’s shelter and a broad waiting verge serve walkers, pack animals and the occasional small cart. Ferns hide the older footpath beneath the stone approach.',[
  ('Woodland Approach','A maintained forest path widens beside a dry stone bench. Travelers can see the near end of the red bridge before committing to the crossing.'),
  ('Bridge Span','Timber rails follow a single arched span above the narrow river. The deck is wide enough for a pack animal, with passing bays at either end.'),
  ('Path-Keeper Shelter','A roofed shelter holds trail ropes, a broom, spare bridge pegs and Yumi Sawatari’s kettle. A shaded track leaves the clearing for the hamlet.')],[]),
 'Reedglass Woodland Hamlet':('A few timber homes occupy a sunny clearing above the river, linked by stone steps and garden paths. Firewood, cultivated mushrooms and baskets of herbs wait under deep eaves; the common yard hosts meals and loud card games.',[
  ('Clearing Lane','A lane skirts vegetable beds and the doors of occupied timber cottages. Stacked split wood stays beneath the eaves rather than blocking the walking space.'),
  ('Common Yard','A shared table and a sheltered hearth face a little mushroom-drying rack. Gorō Fushimi often settles village business here between fiercely argued card games.'),
  ('Wood and Herb Store','A dry communal shed holds bundled firewood, hand tools and labeled herb baskets. Borrowing a tool still means asking its owner.')],[]),
 'White Heron Grove':('White birds nest in a stand of pale-barked trees above a shallow river bend. Smooth stones, old roots and pockets of reeds break the bank; the higher path stays within the trees.',[
  ('Riverbank Path','A narrow path follows the wooded bank. Shallow water and a visible return track let cautious visitors observe before approaching.'),
  ('Nesting Trees','Pale trunks support a noisy heron colony. Fallen feathers and scored bark show where other creatures have crossed beneath the nests.'),
  ('Rooted Pool','Tree roots arch over one shaded pool beside the river. A dry ledge overlooks the water; disturbing its occupant is a choice rather than a compulsory ambush.')],['Reed-Jaw Kappa','Whitefall Crane']),
 'Singing Cedar Hollow':('A wind funnel carries wavering notes through a wooded hollow between rocky slopes. Strips of old trail cloth catch among cedar branches, and root hollows conceal the source of some replies.',[
  ('Cedar Descent','Switching steps descend through cedar shade. The upper trail remains visible behind the visitor, while sounds gather below.'),
  ('Windfall Glade','A fallen cedar opens a patch of light among the trees. Its cracked trunk amplifies wind and smaller noises from the undergrowth.'),
  ('Root Hollow','Dry roots frame a deep sheltered recess beneath a boulder. Marks and disturbed leaf litter reward examination before anyone reaches inside.')],['Moss-Tongue Kodama','Antler-Moss Boar']),
 'Old Bridge Shrine':('A small roadside shrine stands where an earlier footbridge met the wooded ridge path. Travelers leave repaired walking sandals and little carved charms beneath its eaves. An upright tanuki in a patched saffron coat is often inspecting something with immense self-importance.',[
  ('Trail Approach','Mossy boundary stones border the maintained approach. The present bridge can be reached by the lower path without entering the shrine court.'),
  ('Charm Shelter','A little roof shelters carved tokens, spare walking cords and a bench. Koma likes to occupy the driest corner while judging other people’s preparations.'),
  ('Shrine Steps','Three old stone steps lead to the small shrine. A low retaining wall, cedar shade and a clear path back keep the space welcoming to ordinary travelers.')],['Moss-Tongue Kodama']),
 'Mossbank Ridgeway':('A maintained ridge path winds between moss-covered rocks and cedar trunks. Low stone walls stabilize the steeper bends, and small shelters mark sensible places to rest a load before the road reaches open grain country.',[
  ('Ridge Approach','Packed earth climbs past a low waymarker into the trees. The grade is manageable with a balanced load and patience.'),
  ('Rest Shelter','A roofed stone platform offers a dry place to retie a pack or wait out a passing shower. The trail ahead remains visible through the trunks.'),
  ('Southward Bend','The ridge bends toward the farm roads beyond the forest. A short repaired wall keeps loose stones from spilling across the track.')],['Moss-Tongue Kodama']),
 'Woodland Dye Workshop':('A timber workshop and drying yard sit beside a clean stream below the trees. Aya Takino steeps bark, roots and gathered leaves into vivid dyes; cloth bundles arrive by pack trail, and the rinsing channel turns a different color with each batch.',[
  ('Dye Yard','Covered vats stand on a level stone apron beside stacked bark and root baskets. Workers keep clear lanes between the hot vessels and the rinse channel.'),
  ('Cloth Racks','Long racks support bright fabric under an open-sided roof. A low rail separates clean drying cloth from muddy deliveries.'),
  ('Ledger Bench','A standing-height bench holds sample swatches, a balance and the day’s consignment notes. Aya Takino compares colors here with little patience for vague requests.')],[])}
OLD_LABELS={
 'Mirror-Reed Ferry':['Near Landing','Ferry Deck','Boat Shelter'],
 'Reedglass Fishing Village':['Raised Lane','Smoking Yard','Boat Shed'],
 'White Heron Islets':['Shallow Shore','Deadwood Stand','Root Channel'],
 'Singing Reed Marsh':['Raised Bank','Reed Mat','Deep Channel'],
 'Old Ferry Shrine':['Dry Landing','Oar Shelter','Shrine Steps'],
 'Saltwind Causeway':['Near Causeway','Refuge Platform','Far Gate'],
 'Reed Dye Workshop':['Dye Yard','Cloth Racks','Ledger Bench']}
PEOPLE_CHANGES={
 'Yumi Sawatari':{'role':('ferry pilot','bridge keeper and trail guide'),'want':('Buy her own ferry share.','Open her own little outfitter’s lodge beside the woodland road.'),'flaw':('She places a private bet against a passenger’s boasting.','She places a private bet against a traveler’s boasting.'),'quirk':('Spins a mooring knot before setting it.','Reties a trail rope while listening to an implausible story.'),'weapon':('a boat hook','a hooked walking staff'),'method':('Water assists a real pole stroke; she keeps an escape bank in view.','Water redirects a little surface flow away from the footing; her hooked staff and a prepared return path provide practical defense.')},
 'Gorō Fushimi':{'role':('fishing village headman','woodland hamlet headman'),'public':('Gorō hosts vigorous card games and knows the lake’s moods better than his children’s.','Gorō hosts vigorous card games and knows the ridge weather better than his children’s moods.'),'want':('Keep a shared landing free of private tolls.','Keep the communal woodland path free of private tolls.'),'method':('Practical boats and a sturdy ward.','Prepared trail markers, practical rope work and a sturdy ward.')},
 'Aya Takino':{'role':('reed dyer','bark-dye artisan'),'method':('Water and ordinary dyes produce the actual cloth.','Water rinses real cloth steeped in dyes made from bark, roots and gathered leaves.')},
 'Koma':{'public':('Koma insists he is a retired ferry inspector, changes his account when challenged and knows every dry landing. He loves dice, river songs and payment in a particularly good lunch.','Koma insists he is a retired boundary inspector, changes his account when challenged and knows every dry woodland shortcut. He loves dice, traveling songs and payment in a particularly good lunch.'),'method':('Small Illusion disguises and clever use of the bank aid a retreat; he cannot turn leaves into permanent money, erase a debt or command every river spirit.','Small Illusion disguises and clever use of the wooded trail aid a retreat; he cannot turn leaves into permanent money, erase a debt or command every forest spirit.')}}
QUESTS={
 'Akitsuhara Guild: Cloth on the Forest Road':('Recover the real cloth consignment from the overturned pack cart and deliver it dry enough for its intended use.','A loose wheel and a sudden shower left the small cart tilted beside the forest path. Secure the load, repair or lighten the cart, or arrange willing porters. A torn bundle is a negotiable partial result; this is a practical recovery, not a pirate attack.'),
 'Akitsuhara Guild: Missing on the Ridge':('Find the overdue trail helper and bring the helper and the accompanied travelers back to a usable woodland route.','A turned ankle and an Antler-Moss Boar occupying the lower bend have stranded a trail party at a dry shelter. A supported walk, a distraction, an alternate marked path or a proportionate fight can work. The helper is alive unless actual events change that.')}

def replace(v,mapping):
    if isinstance(v,str):
        if 'Benitsuru Guildhall' in mapping:
            v=v.replace("'Benitsuru Guildhall'",json.dumps(mapping['Benitsuru Guildhall'],ensure_ascii=False))
        for a,b in sorted(mapping.items(),key=lambda x:-len(x[0])):v=v.replace(a,b)
        return v
    if isinstance(v,list):return [replace(x,mapping) for x in v]
    if isinstance(v,dict):return {replace(k,mapping):replace(x,mapping) for k,x in v.items()}
    return v

def replace_source(text,mapping):
    tree=ast.parse(text);parents={child:node for node in ast.walk(tree) for child in ast.iter_child_nodes(node)}
    edits=[]
    for node in ast.walk(tree):
        if isinstance(node,ast.Constant) and isinstance(node.value,str) and not isinstance(parents.get(node),ast.JoinedStr):
            new=replace(node.value,mapping)
            if new!=node.value:edits.append((ast.get_source_segment(text,node),repr(new)))
    for old,new in sorted(edits,key=lambda x:-len(x[0])):text=text.replace(old,new)
    ast.parse(text)
    return text

def main():
    marker=HERE/'location-followup-report.json'
    if marker.exists():raise ValueError('Already applied; review rather than replay this merge.')
    path=ROOT/'world-draft/WorldAlpha - World.json';before=json.loads(path.read_text(encoding='utf-8'))
    supplied=json.loads(SOURCE.read_text(encoding='utf-8-sig'));supplied=supplied.get('locations',supplied)
    assert set(before['locations'])<=set(supplied),'Location export omits current records'
    w=copy.deepcopy(before);w['locations']=copy.deepcopy(supplied)
    mappings=dict(RENAMES)
    for old,labels in OLD_LABELS.items():
        new=RENAMES[old]
        for oldlabel,(label,_) in zip(labels,SITES[new][1]):mappings[old+' - '+oldlabel]=new+' - '+label
    w=replace(w,mappings)
    m=replace(json.loads((HERE/'manifest.json').read_text(encoding='utf-8')),mappings)
    w['regions']['Mirror-Reed Lowlands']['basicInfo']=REGION_TEXT
    for name,(text,areas,types) in SITES.items():
        loc=w['locations'][name];neighbors=[b if a==name else a for a,b in m['roads'] if name in [a,b]]
        loc['basicInfo']=text+' Nearby routes lead toward '+', '.join(neighbors)+'.'
        ids=[name+' - '+label for label,_ in areas]
        loc['areas']={k:{'description':desc,'paths':[x for x in ids if x!=k]} for k,(_,desc) in zip(ids,areas)}
        residents=[n for n,v in w['npcs'].items() if v['currentLocation']==name]
        loc['hiddenInfo']='Use this actual forest-and-river setting and the placed residents. Ordinary visits to inhabited clearings do not create a fight. Respect owned tools, honest payment and actual completed outcomes. '
        if types:loc['hiddenInfo']+='Suitable encounter types: '+', '.join(types)+'. Use finite occupants and preserve a cleared encounter. '
        if residents:loc['hiddenInfo']+='Established local people: '+', '.join(residents)+'. Reuse their records rather than inventing replacements. '
    for title,(outcome,scene) in QUESTS.items():
        q=w['parties']['']['quests'][title];reward=next(e['quantity'] for e in q['onCompleteEffects'] if e['type']=='item-add' and e['item']=='Mark')
        q['mainObjective']=outcome;q['questStatement']=outcome+f' Posted reward: {reward} marks.'
        suffix=q['questDesignBrief'][q['questDesignBrief'].index(' Recommended level'):]
        q['questDesignBrief']=scene+suffix
        q['completionCondition']['query']='For the accepted undertaking '+title+', actual events have achieved this outcome: '+outcome+' Count a feasible alternative that genuinely accomplishes it. A plan, arrival, boast or unrelated work is insufficient. Preserve completed work after travel and do not add an unstated compulsory stage.'
        w['locations'][q['questLocation']]['hiddenInfo']+=' Potential unresolved situation: '+scene+' The voluntary undertaking is '+title+'.'
    # Update the reusable source data as well; do not rebuild the world from an older export.
    gp=HERE/'geography.py';g=gp.read_text(encoding='utf-8')
    oldregion=before['regions']['Mirror-Reed Lowlands']['basicInfo'];assert oldregion in g;g=g.replace(oldregion,REGION_TEXT)
    for old,loc in before['locations'].items():
        if old not in supplied:continue
        pat=re.compile(r'^'+re.escape(old)+r'\|[^\n]+$',re.M);match=pat.search(g)
        if not match:continue
        row=match.group().split('|');new=RENAMES.get(old,old);row[0]=new;row[1]=str(supplied[old]['x']);row[2]=str(supplied[old]['y'])
        if new in SITES:
            row[4]=SITES[new][0];row[5]=';'.join(x[0] for x in SITES[new][1]);row[6]=','.join(SITES[new][2])
        g=g[:match.start()]+'|'.join(row)+g[match.end():]
    gp.write_text(g,encoding='utf-8')
    cp=HERE/'cast.py';text=cp.read_text(encoding='utf-8')
    for changes in PEOPLE_CHANGES.values():
        for a,b in changes.values():assert a in text,a;text=text.replace(a,b)
    text=replace_source(text,RENAMES);cp.write_text(text,encoding='utf-8')
    qp=HERE/'quests.py';text=qp.read_text(encoding='utf-8')
    for old,new in RENAMES.items():
        if old!='Benitsuru Guildhall':text=text.replace(old,new)
    for title,(outcome,scene) in QUESTS.items():
        pat=re.compile(r'^'+re.escape(title)+r'\|[^\n]+$',re.M);match=pat.search(text);assert match
        row=match.group().split('|');row[6]=outcome;row[7]=scene;text=text[:match.start()]+'|'.join(row)+text[match.end():]
    qp.write_text(replace_source(text,RENAMES),encoding='utf-8')
    for filename in ['build.py','systems.py','guild_patch.py','types_and_lore.py','prepare_supporting_art.py']:
        p=HERE/filename;p.write_text(replace_source(p.read_text(encoding='utf-8'),RENAMES),encoding='utf-8')
    for filename in ['tools/test_oni.cjs','tools/test_adventurers.cjs']:
        p=ROOT/filename;p.write_text(replace(p.read_text(encoding='utf-8'),RENAMES),encoding='utf-8')
    # One approved new attendant and finished onsen at the author's exact pin.
    name='Atsuha Yunokawa';rng=random.SystemRandom();roll=rng.randint(1,100);count=1 if roll<=65 else 2 if roll<=90 else 3
    affinities=['Water']+rng.sample(['Fire','Earth','Nature','Healing'],count-1)
    draws=json.loads((HERE/'design-draws.json').read_text(encoding='utf-8'));draws[name]={'affinityRoll':roll,'affinities':affinities,'poseRoll':rng.randint(1,6),'skin':'light olive'};dump(HERE/'design-draws.json',draws)
    onsen="Hinoki Hollow Onsen|34|-45|1-12|Warm mineral water rises beneath a low cypress bathhouse at the wooded edge of Benitsuru. A covered washing court, small quiet pools and a garden rest veranda offer a break from the capital. A basic bath and clean towel cost 6 marks.|Reception Porch;Washing Court;Stone Pools;Rest Veranda|"
    with gp.open('a',encoding='utf-8') as f:f.write('\nSITES[7] += '+repr('\n'+onsen+'\n')+'\n')
    line="person('Atsuha Yunokawa','onsen proprietor','Hinoki Hollow Onsen','female',46,'Human','copper-brown hair in a low bun, amber-brown eyes and a sturdy adult build','Atsuha keeps a spotless bathhouse, collects dreadful travel excuses and sings old festival songs when she thinks the veranda is empty.','Buy the neglected garden next door and grow her own fragrant bath herbs.','She agrees too quickly with impressive guests, then makes a junior worker explain why the promised exception is impossible.','Warm, brisk and dryly funny; her polite refusal usually comes with a clean towel.','Tests the water with the same chipped cedar dipper she refuses to replace.','a short wooden wand','Small Water workings regulate an ordinary channel; careful inspection and a clear exit matter more than fighting.','Akitsuhara',ties='Aya Takino supplies sturdy bath cloth. Chiyo Matsukaze occasionally sends tired travelers her way.')\n"
    with cp.open('a',encoding='utf-8') as f:f.write('\n'+line)
    import build,cast
    importlib.reload(cast);build.PEOPLE=cast.PEOPLE;build.YOKAI=cast.YOKAI
    from build import areas_for,add_cast
    loc=w['locations']['Hinoki Hollow Onsen'];loc.update(basicInfo=onsen.split('|')[4]+' A short maintained lane leads toward South Gate Caravan Yard.',hiddenInfo='Atsuha Yunokawa runs this actual bathhouse. Establish ordinary fees and privacy before use. A bath is ordinary rest, not an automatic cure or duplicated resource grant. A guest may talk, wash or leave; do not infer intimacy from paying for a bath.',complexityType='complex',detailType='detailed',npcLevelRange={'min':1,'max':12},factions=['Akitsuhara'])
    loc['areas']=areas_for('Hinoki Hollow Onsen',onsen.split('|')[5].split(';'),loc['basicInfo'])
    m['locations'].append('Hinoki Hollow Onsen');m['roads'].append(['Hinoki Hollow Onsen','South Gate Caravan Yard'])
    w['locations']['South Gate Caravan Yard']['basicInfo']+=' A maintained side lane leads to Hinoki Hollow Onsen.'
    temp=copy.deepcopy(w);temp['npcs']={};add_cast(temp)
    fields=['currentLocation','currentArea','basicInfo','hiddenInfo','personality','abilities','visualDescription']
    for n in PEOPLE_CHANGES:
        for field in fields:w['npcs'][n][field]=temp['npcs'][n][field]
    w['npcs'][name]=temp['npcs'][name];m['npcs'].append(name)
    for filename in ['supporting-portrait-briefs.json','supporting-portrait-selection.json']:
        p=HERE/filename;obj=json.loads(p.read_text(encoding='utf-8'))
        if isinstance(obj,dict):
            for n in PEOPLE_CHANGES:obj.pop(n,None)
        else:obj=[n for n in obj if n not in PEOPLE_CHANGES]
        dump(p,obj)
    weapon_rule=' Spears and polearms have one straight continuous shaft aligned through both grips, with an attached head. No accidental breaks, offsets or floating sections.'
    w['imagePromptConfiguration']['npcs']+=weapon_rule
    assert len(w['imagePromptConfiguration']['npcs'].encode('utf-16-le'))//2<=5000
    # No old map IDs or retired water-village premise remains in the live configuration.
    flat=json.dumps(w,ensure_ascii=False)
    for old in RENAMES:assert old not in flat,old
    for n in PEOPLE_CHANGES:
        for a,b in PEOPLE_CHANGES[n].values():assert a not in json.dumps(w['npcs'][n],ensure_ascii=False),a
    for old,source in supplied.items():
        new=RENAMES.get(old,old);assert w['locations'][new]['x']==source['x'] and w['locations'][new]['y']==source['y']
        if 'images' in source:assert w['locations'][new]['images']==source['images']
    dump(path,w);dump(HERE/'manifest.json',m)
    from regression_delta import record
    record(w)
    dump(marker,{'sourceSHA256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'renames':RENAMES,'rewrittenLocations':list(SITES),'rewrittenNPCs':list(PEOPLE_CHANGES),'newNPC':name,'newOnsen':'Hinoki Hollow Onsen','coordinatesAndImagesPreserved':True,'newLocationImagesGenerated':0,'portraitRuleAdded':weapon_rule,'onsenAffinityRoll':roll,'onsenAffinities':affinities})
    print(json.dumps({'mergedLocations':len(supplied),'forestLocations':len(SITES),'updatedResidents':list(PEOPLE_CHANGES),'newNPC':name,'onsenAffinities':affinities,'totalNPCs':len(w['npcs'])},ensure_ascii=False))

if __name__=='__main__':main()
