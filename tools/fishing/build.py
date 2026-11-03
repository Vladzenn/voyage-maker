"""Apply the approved Fishing patch to the current world, never an older export."""
from pathlib import Path
import copy, hashlib, json, re, subprocess
from data import FISH, SITES, GEAR

ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parent
WORLD=ROOT/'world-draft/WorldAlpha - World.json'
OUT=ROOT/'output/fishing-2026-11-04'

def js(v): return json.dumps(v,ensure_ascii=False,separators=(',',':'))
def digest(v): return hashlib.sha256(js(v).encode()).hexdigest()
def write(path,v): path.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def trait(name,desc,skills=None,items=None):
    return dict(name=name,description=desc,traitNarrativeEffects=desc,attributes=[],skills=skills or [],resources=[],startingItems=items or [],abilities=[],unlockedBy=[],excludedBy=[],requirements=[])
def trigger(name,conditions,script='',effects=None,scope='player',phase=None):
    d=dict(name=name,recurring=True,scope=scope,conditions=conditions,effects=effects or [])
    if script:d['script']=script
    if phase:d['phase']=phase
    return d
def itemcond(name): return dict(type='player-item',item=name,operator='greaterThan',value=0)

def repair_offers(w):
    # A declared semantic condition is AI-evaluated. Script-side check(action)
    # only reads raw text. Eight native offers retain native acceptance/rewards.
    report=json.loads((ROOT/'tools/glowhaven-expansion/merge-review.json').read_text(encoding='utf-8'))
    rows=report['contents']['localOffers']
    w['triggerDefinitions'].pop('ghx_local_commissions',None)
    names=[]
    for i,(title,client,destination,home) in enumerate(rows):
        name='ghx_local_commissions'+('' if i==0 else '_'+str(i+1))
        places=list(dict.fromkeys([destination,home]))
        location={'type':'party-location','operator':'equals','value':places[0]} if len(places)==1 else {'type':'party-location','operator':'regex','value':'^('+ '|'.join(re.escape(p) for p in places)+')$'}
        query=f'The player deliberately asks {client} about {title}, asks that actual client for suitable local work, or investigates the actual notice for {title}. The real client or notice is involved here. A greeting, arrival, rumor alone, unrelated business or another person’s completed job does not qualify.'
        effects=[dict(type='quest-init',operator='set',value=title),dict(type='story',instruction=f'Offer {title} through {client} or its real local notice. Explain its public situation and stated reward, then wait for acceptance or refusal. Destination: {destination}. This offer grants no acceptance, payment, licence, recruitment or completed work.')]
        script="const tick=Number(check({type:'game-tick'}))||0;if(storage.ghxOfferTick===tick){skip=true}else{storage.ghxOfferTick=tick}"
        w['triggerDefinitions'][name]=trigger(name,[dict(type='party-realm',operator='equals',value='Glowhaven'),location,dict(type='quest-status',questId=title,operator='equals',value='hidden'),dict(type='action',query=query)],script,effects,scope='party')
        names.append(name)
    return names

def apply(w):
    w['skills']['Fishing']={'name':'Fishing','type':'utility','attribute':'intuition','description':'Reading a fishing ground, choosing tackle, presenting bait or a lure, judging a bite and landing an actual fish. Better technique improves a genuine fishing action; rare catches demand a thoughtful response to their movement. An observed shoal is not an acquired catch. Fishing never supplies a boat, bait, safe footing or knowledge of every species.','startingItems':[]}
    w['traits']['Fisher']['skills']=[{'skill':'Fishing','modifier':2},{'skill':'Perception','modifier':1}]
    w['traits']['Fisher']['description']='Experience reading water, tending lines, choosing bait and bringing a useful catch home. Begin with +2 Fishing and +1 Perception.'
    w['traits']['Fisher']['traitNarrativeEffects']=w['traits']['Fisher']['description']+' This background is prior experience, not a current job, boat, licence or free equipment.'
    w['traits']['Angling Basics']=trait('Angling Basics','Familiar with rigging a rod, feeling a bite and bringing a small fish safely to hand.',[{'skill':'Fishing','modifier':1}])
    w['traits']['Rare Fish on the Line']=trait('Rare Fish on the Line','Something unusual is pulling at your fishing line. Keep its movements in mind: patience, a change of angle or a well-timed pull may bring it within reach. You can also let it go.')
    w['traits']['Fishing Starter Kit']=trait('Fishing Starter Kit','An ash rod with reusable spinner, eight portions of bait and a waterproof field ledger for a quiet afternoon beside the water.',items=[{'item':'Angler’s Rod','quantity':1},{'item':'Angler’s Bait Portion','quantity':8},{'item':'Angler’s Field Ledger','quantity':1}])
    cat=w['traitCategories']['Starting Equipment']
    cat['traits']=list(dict.fromkeys(cat['traits']+['Fishing Starter Kit']))
    # Do not add a second hidden equipment pick through subcategories.
    if cat.get('subcategories'):cat['subcategories'].append({'name':'Fishing','traits':['Fishing Starter Kit']})
    for tier in w['itemSettings']['tiers'].values():
        policy=tier['bonusPolicy']['allowedBonuses']
        exemplar=next(b for b in policy if b['type']=='skill' and b['variable']=='Perception')
        if not any(b['type']=='skill' and b['variable']=='Fishing' for b in policy):policy.append({**exemplar,'variable':'Fishing'})
    for name,habitat,weight,weather,low,high,price,desc in FISH:
        w['itemTypes'][name]={'name':name,'category':'Consumable','tier':'mundane','estimatedValue':price,'description':desc,'bonuses':[],'needsMediaGeneration':True}
    for name,category,tier,price,slot,bonus,desc in GEAR:
        d={'name':name,'category':category,'tier':tier,'estimatedValue':price,'description':desc,'bonuses':[],'needsMediaGeneration':True}
        if slot:d['slot']=slot
        if bonus:d['bonuses']=[{'type':'skill','variable':bonus[0],'value':bonus[1]}]
        w['itemTypes'][name]=d
    for area in SITES:
        location=area.split(' - ')[0]
        assert area in w['locations'][location]['areas'],area

    realm=dict(type='party-realm',operator='equals',value='Glowhaven')
    water=dict(type='party-area',operator='regex',value='Pinewater|Saltmere|Whitecrest|Driftstone|Pinewake|Albatross|Moonarch|Greenrush|Gullwatch|Stillback')
    rod=itemcond('Angler’s Rod')
    outcome=dict(type='action-success-level',operator='greaterThanOrEqual',value='mixed results')
    casting='The player makes a real fresh rod-fishing cast into reachable water, with their own Angler’s Rod, rather than talking about fishing, buying gear, attacking, remembering a cast or already handling a rare hooked fish. '
    t=w['triggerDefinitions']
    t['fsh_weather']=trigger('fsh_weather',[realm],(HERE/'weather.js').read_text(),scope='party',phase='planning')
    t['fsh_basics']=trigger('fsh_basics',[realm,water,rod,dict(type='skill-value',skill='Fishing',operator='equals',value=0),dict(type='action',query='The player actually rigs their own rod and practices their first cast into reachable water, or receives a real introductory fishing lesson with that rod. Talking about lessons, receiving a rod or fishing elsewhere in memory does not qualify.')],script="const sites="+js(SITES)+";if(!sites[String(check({type:'party-area'})||'')])skip=true;",effects=[dict(type='player-traits',operator='add',value='Angling Basics',target='satisfyingPlayers')])
    data=[[r[0],r[1],r[2],r[3],r[4],r[5]] for r in FISH]
    for baited in [False,True]:
        name='fsh_cast_bait' if baited else 'fsh_cast_lure'
        conditions=[water,rod]
        conditions.append(itemcond('Angler’s Bait Portion') if baited else dict(type='player-traits',operator='notContains',value='Rare Fish on the Line'))
        conditions += [outcome,dict(type='action',query=casting+('They deliberately use one real Angler’s Bait Portion from their own inventory.' if baited else 'They use the reusable spinner or another real reusable lure, without using a consumable bait portion.'))]
        script=(HERE/'cast.js').read_text().replace('__SITES__',js(SITES)).replace('__FISH__',js(data)).replace('__BAITED__',js(baited))
        t[name]=trigger(name,conditions,script)
    missscript="const sites="+js(SITES)+";const tick=Number(check({type:'game-tick'}))||0,habitat=sites[String(check({type:'party-area'})||'')];if(!storage.fshCasts)storage.fshCasts={};if(check({type:'party-realm'})!=='Glowhaven'||!habitat||tick<=0||storage.fshCasts.bait===tick)skip=true;else{storage.fshCasts.bait=tick;if(habitat==='d'&&storage.fshWeather?.coast?.kind==='storm'){effects.length=0;effects.push({type:'story',instruction:'The exposed water is too rough for this cast. Keep the bait and show the option to wait safely; grant no catch.'})}}"
    t['fsh_bait_miss']=trigger('fsh_bait_miss',[water,rod,itemcond('Angler’s Bait Portion'),dict(type='action-success-level',operator='lessThan',value='mixed results'),dict(type='action',query=casting+'They actually expend one Angler’s Bait Portion on this cast; a baited rare-fish handling action is not a fresh cast.')],script=missscript,effects=[dict(type='item-remove',item='Angler’s Bait Portion',quantity=1,target='satisfyingPlayers'),dict(type='story',instruction='This genuine baited cast catches nothing; one bait portion was spent. Give a brief practical result without another item deduction, attack or invented injury.')])
    hook=dict(type='player-traits',operator='contains',value='Rare Fish on the Line')
    handling='The player actively attempts to land their already hooked rare fish by a deliberate handling choice, using their actual line and Fishing. They are not merely talking, waiting, casting a second line, releasing it or claiming a previous catch.'
    for mode,extra in [('land',[dict(type='action-success-level',operator='greaterThanOrEqual',value='basic success'),dict(type='action',query=handling)]),('miss',[dict(type='action-success-level',operator='lessThan',value='basic success'),dict(type='action',query=handling)]),('release',[dict(type='action',query='The player deliberately releases the rare fish currently hooked on their line, cuts that line, or explicitly abandons that live catch. Talking about release or releasing an already landed inventory fish does not qualify.')]),('cleanup',[])]:
        conditions=[hook]+([] if mode=='cleanup' else [water])+([rod] if mode in ['land','miss'] else [])+extra
        name='fsh_rare_'+mode
        t[name]=trigger(name,conditions,(HERE/'rare.js').read_text().replace('__MODE__',js(mode)).replace('__RARE__',js([r[0] for r in FISH if r[2]==2])),phase='planning' if mode=='cleanup' else None)
    t['fsh_records']=trigger('fsh_records',[dict(type='action-text',operator='regex',value='\\b([Ff]ishing (records?|journal|ledger)|[Cc]atch (records?|ledger)|[Bb]est (fish|catches))\\b')],script="const rows=Object.entries(storage.fshRecords||{}).sort((a,b)=>b[1].best-a[1].best);effects.push({type:'story',instruction:rows.length?'The shared travel party’s recorded species: '+rows.length+'. Best measured catches: '+rows.slice(0,8).map(([n,r])=>n+' '+r.best+' cm').join('; ')+'. These are past observations, not currently held fish or separate sales. Simultaneous anglers share the local shoal result; do not invent per-person records.':'There are no landed catches recorded yet. Give a short natural response; no blank journal purchase or fishing quest is required.'});")

    offers=repair_offers(w)
    quests=[]
    questdata=[
      ('A Fisher’s First Lesson','Makiho Akitsu','Gullwatch Reefs',15,60,'Makiho has a short lesson to offer anyone willing to bring a rod and pay attention to the water. She wants a beginner to feel the difference between a nibble and a snag.','Land a fish during Makiho’s practical lesson, or demonstrate a genuinely careful catch-and-release.','The participating player completes a real practical fishing lesson with Makiho and actually lands a fish or performs a successful careful catch-and-release. Buying a fish, watching another angler or promising to practice is insufficient.'),
      ('Supper before the Tide Turns','Nanae Kogure','The Gilded Albatross',18,60,'Nanae wants a couple of ordinary fresh fish for supper. Something modest and edible would be more useful than another sailor’s story about the one that got away.','Bring Nanae two fresh ordinary edible fish and settle the agreed handover.','Nanae actually receives two real ordinary edible fish suitable for the agreed supper from the participating party. Honest procurement or fishing both qualify. Ownership transfers once through ordinary item handling; a promise, a catalogue description or the same fish shown twice does not qualify.'),
      ('A Color beneath the Scales','Yorina Tsugawa','Thistlebank Alchemy Cottage',30,90,'Yorina wants to compare the natural sheen of an Amberfin Eel or Blueglass Needlefish with her waterproof pigments. A useful specimen matters more than a dramatic hunting story.','Provide an actual Amberfin Eel or Blueglass Needlefish for Yorina’s agreed pigment study.','Yorina actually receives a real agreed Amberfin Eel or Blueglass Needlefish specimen for the pigment study. Honest purchase, fishing or an agreed suitable specimen portion qualifies. A promise, an invented sample or an unsurrendered fish does not.'),
    ]
    for i,(name,client,place,fee,xp,desc,obj,query) in enumerate(questdata):
        w['parties']['']['quests'][name]={'name':name,'questStatement':desc,'status':'hidden','detailType':'detailed','conclusive':True,'questSource':client,'questLocation':place,'objectives':{'task':{'id':'task','text':obj,'status':'active'}},'questDesignBrief':'A small optional local commission. Keep the client’s ordinary personality and other work present. Explain the actual request and posted payment before agreement. No compulsory fight, portal permission or surprise boss. Real handovers use actual inventory once; native completion owns the stated reward.','completionCondition':{'type':'story','query':query},'onCompleteEffects':[{'type':'item-add','item':'Mark','quantity':fee,'target':'allPlayers'},{'type':'player-experience','operator':'add','value':xp,'target':'allPlayers'}]}
        tid='fsh_offer_'+str(i+1)
        t[tid]=trigger(tid,[realm,dict(type='party-location',operator='equals',value=place),dict(type='quest-status',questId=name,operator='equals',value='hidden'),dict(type='action',query=f'The player asks {client}, who is actually present, about {name} or asks that person for a fishing lesson, fish-supply request or suitable local work. A greeting, arrival or someone else’s completed contract is insufficient.')],script="const tick=Number(check({type:'game-tick'}))||0;if(storage.ghxOfferTick===tick){skip=true}else{storage.ghxOfferTick=tick}",effects=[dict(type='quest-init',operator='set',value=name),dict(type='story',instruction=f'Offer {name} through {client}. State the actual request and {fee}-mark reward. Wait for acceptance or refusal; the offer itself gives no payment, fish or completed lesson.')],scope='party')
        quests.append(name)

    w['worldLore']['Angling around Glowhaven']={'text':'Glowhaven’s rivers, estuary, harbor and rocky coast support a varied fishing trade. Makiho Akitsu sells ordinary tackle at Gullwatch Reefs and teaches practical angling; local fishmongers carry rods, bait and common catches, with finer reusable lures less common. A basic rod includes a reusable spinner, so worms and paste are a choice rather than a necessity. Rain brings loaches and eels toward feeding grounds; clear shallows favor brightly patterned reef fish. Mist sometimes reveals the strange sheen of a Moonmirror Dace. Open-water anglers speak of Crownfin Sailfish and the blue light of Lanternjaw Anglers. A boat and safe footing matter more than boasting. Mauruun is a protected resting animal to local fishers; Nerathyl’s ledge and the kraken’s approaches are serious hazards, not everyday fishing grounds.'}
    w['worldLore']['Glowhaven Weather and Water']={'text':'Glowhaven has coastal squalls, drifting sea fog, clear spells and ordinary inland rain. A change in the sky usually develops over time; different waters can remain under different conditions. Fog hides approaches, wind roughens exposed water, and a passing storm is a good reason to wait ashore. Buildings, sheltered coves and sensible local knowledge remain useful. These local patterns say nothing about the climate beyond the Evertree’s portals.'}
    w['aiInstructions']['generateActionInfo']['Exact Skill Routing']+='\nFishing/Intuition: rod casts and landing fish.'
    w['aiInstructions']['ItemGenerationAndUsage']['Fishing Stock and Catches']='Fishmongers sell canonical tackle. Fishing effects own fish grants and bait costs; never duplicate them. Release, sale and cooking transfer real fish once. Fish restore no resources.'
    # A focused correction of the player handoff and runtime style owner.
    direction='A richly designed 2D fantasy-anime character illustration with the presence of a main-character key visual. Use expressive drawn eyes, simplified anime nose and mouth, clearly drawn facial contours and smooth colored shadow shapes with selective soft transitions. Keep skin illustration-flat and clean; put intricate detail into hair, costume, embroidery and the setting. Luminous color and vivid supported effects give the picture energy. The face must read as anime drawing, without photographic skin, sculpted facial planes or a rendered 3D face.'
    prompt=w['imagePromptConfiguration']['npcs']
    start=prompt.index('Premium fantasy RPG anime');end=prompt.index('\nDesign one memorable individual',start)
    prompt=prompt[:start]+direction+prompt[end:]
    prompt=prompt.replace('a vertical waist-up or hip-up portrait with the complete head and hair, comfortable headroom and a natural eye-level or three-quarter view','a vertical hip-up portrait: complete head and hair, torso, full waist and both hips, with the bottom edge at the upper thighs below the belt and hip line. Pull the camera back enough to show the lower outfit; do not stop at the ribs or waist. Keep comfortable headroom and a natural eye-level or three-quarter view')
    prompt=prompt.replace('Illustrated metal highlights and softly modeled anime shading are welcome; do not flatten every surface into hard shadow blocks.','Keep illustrated material highlights, but no airbrushed realistic facial modeling, photographic hair strands or ray-traced surfaces.')
    w['imagePromptConfiguration']['npcs']=prompt
    bg=w['aiInstructions']['generateCharacterBackground']
    key='Appearance Construction and Support';s=bg[key]
    start=s.index('Premium fantasy RPG anime');end=s.index('\nMake the player',start)
    s=s[:start]+direction+s[end:]
    s=s.replace('waist-up or hip-up, natural eye-level or three-quarter view','hip-up with both hips and the top of the thighs visible below the waist and belt, natural eye-level or three-quarter view. Pull the camera back to include the lower outfit; a torso cropped at the waist is waist-up, not hip-up')
    s=s.replace('Favor fine linework, dimensional illustrated materials, soft layered shading, lively hair and fabric, and lighting appropriate to the actual setting.','Favor expressive anime drawing, clean smooth facial shadows, detailed illustrated costume, lively hair and fabric, and light appropriate to the setting.')
    bg[key]=s
    bg['Appearance Depth and Visual Continuity']=bg['Appearance Depth and Visual Continuity'].replace('fine expressive drawing, soft layered shading, detailed illustrated materials','expressive 2D anime drawing, simplified drawn facial features, clean smooth facial shadow shapes and detailed illustrated costume')
    for name in ['Portrait Style — Fantasy RPG illustration','Portrait Style — Dramatic gacha illustration','Portrait Style — Elegant linework']:
        d=w['traits'][name]
        desc=d['description'].replace('softly layered painted shading','clean anime facial shadow shapes').replace('dimensional painted shading','drawn anime features and clean facial shading').replace('softly painted materials','illustrated materials and clearly drawn anime facial features')
        d['description']=desc;d['traitNarrativeEffects']=desc
    d=w['traits']['Portrait Frame — Hip-up'];d['description']=d['traitNarrativeEffects']='A vertical portrait from the complete head through both hips to the top of the thighs. Show the full waist, belt and lower outfit; the crop ends below the hips, not at the waist.'
    w['traitCategories']['Portrait Framing']['description']='Optional — skip for a hip-up portrait showing the full waist, both hips and the top of the thighs. Choose Waist-up for a tighter crop. Explicit alternatives take priority.'
    w['traitCategories']['Portrait Style']['description']='Optional — skip for a detailed 2D fantasy-anime character illustration with expressive drawn features and clean facial shading. Alternative styles change the picture, not your abilities.'
    from universal import apply as universal_fishing
    meta={'species':[r[0] for r in FISH],'gear':[r[0] for r in GEAR],'sites':SITES,'quests':quests,'repairedLocalOffers':offers,'sharedRolls':'One local shoal/specimen roll per cast mode and turn; native player conditions select only actual qualifying anglers. Shared records count landing events, not individual fish totals.'}
    meta.update(universal_fishing(w))
    return meta

def main():
    before=json.loads(WORLD.read_text(encoding='utf-8-sig'))
    if 'Fishing' in before['skills']:raise SystemExit('Fishing already exists; review current content rather than rebuilding on an old snapshot.')
    OUT.mkdir(parents=True,exist_ok=True);write(OUT/'Before Fishing - Private Merge Base.json',before)
    after=copy.deepcopy(before);meta=apply(after)
    changes=[]
    def walk(a,b,p):
        if a==b:return
        if isinstance(a,dict) and isinstance(b,dict):
            for k in dict.fromkeys([*a,*b]):
                if k not in a:changes.append({'path':p+[k],'kind':'added'})
                elif k not in b:changes.append({'path':p+[k],'kind':'removed'})
                else:walk(a[k],b[k],p+[k])
        else:changes.append({'path':p,'kind':'changed'})
    walk(before,after,[])
    meta.update({'baseCommit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'beforeSha256':digest(before),'afterSha256':digest(after),'changes':changes,'unchangedTopLevel':{k:digest(v) for k,v in before.items() if after.get(k)==v}})
    assert before['npcs']==after['npcs'] and before['locations']==after['locations'] and before['regions']==after['regions']
    assert len(prompt_units:=after['imagePromptConfiguration']['npcs'].encode('utf-16-le'))//2<=5000,len(prompt_units)//2
    for name,t in after['triggerDefinitions'].items():
        if name.startswith('fsh_') or name in meta['repairedLocalOffers']:
            assert len(t['conditions'])<=5,name
            assert len(js(t).encode('utf-16-le'))//2<=10000,(name,len(js(t)))
            for c in t['conditions']:
                if isinstance(c.get('value'),str):assert len(c['value'].encode('utf-16-le'))//2<=100,(name,c)
    write(WORLD,after);write(HERE/'manifest.json',meta)
    write(OUT/'The Schools of Magic, Arise! - Fishing.json',after)
    print(json.dumps({'fish':len(meta['species']),'gear':len(GEAR),'catchHints':len(SITES),'quests':len(meta['quests']),'changedLeaves':len(changes),'portraitPromptUnits':len(after['imagePromptConfiguration']['npcs'].encode('utf-16-le'))//2}))

if __name__=='__main__':main()
