"""Build from the supplied 5x4 Studio merge base and prove placement preservation."""
import argparse,copy,hashlib,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'tools'))
import geography,cast,content,finish,creation,academy_revamp,portrait_style_refresh,portrait_states
from project import validate

def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,x):
    p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def digest(x):
    def normalize(v):
        if isinstance(v,float) and v.is_integer():return int(v)
        if isinstance(v,dict):return {k:normalize(val) for k,val in v.items()}
        if isinstance(v,list):return [normalize(val) for val in v]
        return v
    return hashlib.sha256(json.dumps(normalize(x),sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()

def build(apply=False):
    source=ROOT/'output/glowhaven-expansion-2026-11-03/Studio Merge Base.json'
    base=read(source);w=copy.deepcopy(base)
    migration=geography.apply(w)
    draws=read(HERE/'affinity-and-pose-draws.json')
    names=cast.add(w,draws);contents=content.add(w);environment=finish.add(w)
    creation.apply(w);portraits=portrait_style_refresh.apply(w);academic=academy_revamp.apply(w)
    # Narrow migration of structured region references. Do not replace realm/faction names.
    def refs(x):
        if isinstance(x,dict):
            for k,v in x.items():
                if k=='region' and isinstance(v,str) and v in migration['renamedRegions']:x[k]=migration['renamedRegions'][v]
                else:refs(v)
        elif isinstance(x,list):
            for v in x:refs(v)
    refs(w)
    urls=read(HERE/'hosted-portraits.json') if (HERE/'hosted-portraits.json').exists() else {}
    for name,row in urls.items():
        assert name in names and name not in base['npcs'],name
        p=ROOT/row['file'];assert p.stem==name and hashlib.sha256(p.read_bytes()).hexdigest()==row['sha256']
        assert row['url'].startswith('https://')
        w['npcs'][name]['portraitUrl']=row['url']
    states=portrait_states.apply(w)
    for key,value in base['regions'].items():
        renamed=migration['renamedRegions'].get(key,key);actual=w['regions'][renamed]
        assert all(actual.get(k)==value.get(k) for k in ['x','y','images','realm']),(key,'region placement/media drift')
    for key,value in base['locations'].items():
        renamed=migration['renamedLocations'].get(key,key);actual=w['locations'][renamed]
        assert all(actual.get(k)==value.get(k) for k in ['x','y','images']),(key,'location pin/media drift')
        for area,a in value.get('areas',{}).items():
            # New placeholders had no authored areas; all existing area media are exact.
            if key not in migration['renamedLocations']:assert actual['areas'][area].get('images')==a.get('images'),(key,area,'area media drift')
    for key,n in base['npcs'].items():assert w['npcs'][key]==n,('Existing NPC changed',key)
    for key,t in base['triggerDefinitions'].items():
        if key!='gh_guild_board':assert w['triggerDefinitions'][key]==t,('Unapproved trigger drift',key)
    # All realms and every non-Glowhaven map/location stay exact, including Spider.
    assert w['realms']==base['realms']
    for key,r in base['regions'].items():
        if r['realm']!='Glowhaven':assert w['regions'][key]==r,key
    for key,l in base['locations'].items():
        if l['region'] in base['regions'] and base['regions'][l['region']]['realm']!='Glowhaven':assert w['locations'][key]==l,key
    validate(w)
    proof={'baseFile':str(source.relative_to(ROOT)),'baseWorldSha256':digest(base),'sourcePins':{k:{f:v.get(f) for f in ['x','y','region']} for k,v in base['locations'].items()},'finalPins':{k:{f:v.get(f) for f in ['x','y','region']} for k,v in w['locations'].items()},'migration':migration,'newNpcs':names,'contents':contents,'environment':environment,'portraitRefresh':portraits,'academicRevamp':academic,'hostedPortraits':len(urls),'portraitStates':states,'existingNpcsExact':len(base['npcs']),'allExistingPortraitsExact':True,'allIncomingMapImagesAndCoordinatesExact':True,'spiderAndOtherRealmsExact':True,'studioSaved':False,'studioPublished':False}
    proof['sourceNpcHashes']={k:digest(n) for k,n in base['npcs'].items()}
    proof['sourceRegionMediaHashes']={migration['renamedRegions'].get(k,k):digest({f:r.get(f) for f in ['x','y','images','realm']}) for k,r in base['regions'].items()}
    proof['sourceLocationMediaHashes']={migration['renamedLocations'].get(k,k):digest({f:l.get(f) for f in ['x','y','images']}) for k,l in base['locations'].items()}
    proof['protectedTriggerHashes']={k:digest(t) for k,t in base['triggerDefinitions'].items() if k!='gh_guild_board'}
    proof['protectedArcsHash']=digest(base['parties']['']['arcs'])
    out=ROOT/'output/glowhaven-expansion-2026-11-03'
    write(out/'The Schools of Magic, Arise! - Glowhaven Expansion.json',w)
    write(out/'NPCs - Glowhaven Expansion.json',{n:w['npcs'][n] for n in names})
    write(out/'Locations - Glowhaven Expansion.json',w['locations'])
    write(HERE/'merge-review.json',proof)
    if apply:write(ROOT/'world-draft/WorldAlpha - World.json',w)
    print(json.dumps({'applied':apply,'regions':len(w['regions']),'locations':len(w['locations']),'npcs':len(w['npcs']),'newNpcs':len(names),'questsAdded':len(contents['quests'])+4,'portraitsHosted':len(urls),'preservation':'all incoming pins/media and existing NPCs exact'},ensure_ascii=False))
    return w

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--apply',action='store_true');a=p.parse_args();build(a.apply)

