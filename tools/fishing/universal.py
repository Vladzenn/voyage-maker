"""Universal water eligibility and finite regional catch pools; no new realm setup."""
from pathlib import Path
import json
from data import FISH, EXTRA_FISH, REALM_CODES, SITES, runtime_fish

HERE=Path(__file__).resolve().parent

def js(v):return json.dumps(v,ensure_ascii=False,separators=(',',':'))
def compact_script(s):return '\n'.join(line.strip() for line in s.splitlines() if line.strip() and not line.lstrip().startswith('//'))

def apply(w):
    assert 'Fishing' in w['skills'],'Apply after the initial fishing setup'
    added=[]
    for name,habitat,weight,weather,low,high,price,desc,code in EXTRA_FISH:
        item=dict(name=name,category='Consumable',tier='mundane',estimatedValue=price,description=desc,bonuses=[],needsMediaGeneration=True)
        assert name not in w['itemTypes'] or w['itemTypes'][name]==item,'Existing item collision: '+name
        w['itemTypes'][name]=item;added.append(name)
    t=w['triggerDefinitions']
    # Cheap lexical prefilter only; the native semantic condition judges actual
    # fishing, water/ownership/feasibility and mode. Never parse an AI Boolean
    # out of script-side raw action text.
    intent={
        'type':'action-text',
        'operator':'regex',
        'value':r'\b([Ff]ish|[Aa]ngling|[Rr]eel|[Ll]ure|[Bb](ait|obber))\w*|\b([Cc]ast|[Ll]ower).*\b(line|rod|hook)\b',
    }
    rod={'type':'player-item','item':'Angler’s Rod','operator':'greaterThan','value':0}
    bait={'type':'player-item','item':'Angler’s Bait Portion','operator':'greaterThan','value':0}
    water='There is actual physically reachable water in this scene that plausibly supports fish, or an established stocked fishing pond. Respect the actual fiction: a place name, a picture, a drinking vessel, an empty fountain, a cloud gap, solid unbroken ice, lava, or an uninhabitable pool supplies no fish. Do not invent a water body or its access. This applies in any realm, including newly created ones. '
    casting=water+'The player actually casts or lowers a fresh line to fish here with their own real Angler’s Rod. Exclude discussion, shopping, old catches, attacks, handling an already hooked fish, and attempts to capture a named NPC, pet or companion. '
    t['fsh_basics']['conditions']=[intent,rod,{'type':'skill-value','skill':'Fishing','operator':'equals','value':0},{'type':'action','query':water+'The player actually rigs and practices their first cast with that rod, or receives a real introductory angling lesson beside the water. Mere possession, intentions and watching another angler do not qualify.'}]
    t['fsh_basics'].pop('script',None)
    context=(HERE/'context.js').read_text(encoding='utf-8').replace('__HINTS__',js(SITES)).replace('__REALMS__',js(REALM_CODES))
    fish=runtime_fish()
    for baited in [False,True]:
        name='fsh_cast_bait' if baited else 'fsh_cast_lure'
        t[name]['conditions']=[intent,rod,bait if baited else {'type':'player-traits','operator':'notContains','value':'Rare Fish on the Line'},{'type':'action-success-level','operator':'greaterThanOrEqual','value':'mixed results'},{'type':'action','query':casting+('They deliberately expend one Angler’s Bait Portion from their own inventory on this cast.' if baited else 'They use a reusable lure. Treat the rod’s built-in spinner as the default when they do not choose to spend bait.')}]
        t[name]['script']=compact_script((HERE/'cast.js').read_text(encoding='utf-8').replace('__FISH__',js(fish)).replace('__CONTEXT__',context).replace('__BAITED__',js(baited)))
    t['fsh_bait_miss']['conditions']=[intent,rod,bait,{'type':'action-success-level','operator':'lessThan','value':'mixed results'},{'type':'action','query':casting+'They actually expend one Angler’s Bait Portion on this committed cast; an aborted setup or hooked-fish handling action is insufficient.'}]
    # Success and failure can target different anglers on the same turn.
    t['fsh_bait_miss']['script']=compact_script(context+"""
const tick=Number(check({type:'game-tick'}))||0;
if(!storage.fshCasts||typeof storage.fshCasts!=='object')storage.fshCasts={};
if(tick<=0||storage.fshCasts.baitMiss===tick){
    skip=true;
}else{
    storage.fshCasts.baitMiss=tick;
    if(habitat==='d'&&weather==='storm'){
        effects.length=0;
        effects.push({type:'story',instruction:'The exposed water is too rough for this cast. Keep the bait and show the option to wait safely; grant no catch.'});
    }
}
""")
    rare=[r[0] for r in fish if r[2]==2]
    for mode in ['land','miss','release','cleanup']:
        name='fsh_rare_'+mode
        t[name]['conditions']=[c for c in t[name]['conditions'] if c['type'] not in ['party-realm','party-area']]
        t[name]['script']=compact_script((HERE/'rare.js').read_text(encoding='utf-8').replace('__MODE__',js(mode)).replace('__RARE__',js(rare)))

    # Carry forward the exact field-name correction already given to the author.
    quests=['A Fisher’s First Lesson','Supper before the Tide Turns','A Color beneath the Scales']
    for name in quests:
        q=w['parties']['']['quests'][name]
        if 'description' in q:q['questStatement']=q.pop('description')
    lore=w['worldLore'].pop('Angling around Glowhaven',None) or w['worldLore'].get('Angling and Regional Waters')
    assert lore
    text=lore['text'].split('\n\nBeyond Glowhaven')[0]
    w['worldLore']['Angling and Regional Waters']={'text':text+'\n\nBeyond Glowhaven, practical anglers adapt to the water they find. Cold Drakenspire lakes and streams support Glassmere Char, Rimefin Whitefish, Copperwhisker Sculpin and Snowmelt Grayling; Amberheart Burbot are scarce. Asterveil’s fresh waters hold Cloudscale Carp, Petalwash Loaches, Rainthread Minnows and Violetfin Gourami, with the occasional Horizon Koi. Akitsuhara’s rivers and lakes are known for Sakura Ayu, Goldleaf Carp, Bamboo Loaches, Redleaf Salmon and rare Moonbell Koi. Common Silverfin and other adaptable fish are found across many ordinary waters. Local knowledge, real access and the actual inhabitants of a pool matter more than its name. Unfamiliar waters can be worth a cast without being a guarantee of safety.'}
    w['aiInstructions']['ItemGenerationAndUsage']['Fishing Stock and Catches']='Fishmongers sell canonical tackle. Apply supplied fish grants and bait costs once. Release, sale, cooking and study transfer real fish once. Fish restore no resources.'
    for name in ['fsh_basics','fsh_cast_lure','fsh_cast_bait','fsh_bait_miss','fsh_rare_land','fsh_rare_miss','fsh_rare_release','fsh_rare_cleanup']:
        tr=t[name]
        assert len(tr['conditions'])<=5,name
        assert len(js(tr).encode('utf-16-le'))//2<=10000,(name,len(js(tr)))
        for c in tr['conditions']:
            if isinstance(c.get('value'),str):assert len(c['value'].encode('utf-16-le'))//2<=100
    return {'species':[r[0] for r in fish],'regionalFishAdded':added,'realmCodes':REALM_CODES,'universalWater':True,'sitesAreCatchHintsOnly':True,'regionalSpecies':{realm:[r[0] for r in EXTRA_FISH if r[8]==code] for realm,code in REALM_CODES.items() if code!='g'},'sharedSpecies':[r[0] for r in EXTRA_FISH if r[8]=='*']}

if __name__=='__main__':
    root=HERE.parents[1];path=root/'world-draft/WorldAlpha - World.json'
    w=json.loads(path.read_text(encoding='utf-8-sig'))
    meta=apply(w)
    path.write_text(json.dumps(w,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    manifest_path=HERE/'manifest.json';m=json.loads(manifest_path.read_text(encoding='utf-8'));m.update(meta)
    manifest_path.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'totalSpecies':len(meta['species']),'newSpecies':len(meta['regionalFishAdded']),'universalWater':True}))
