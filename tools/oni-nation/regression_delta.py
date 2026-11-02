"""Record exact approved changes without replacing older preservation baselines."""
import copy,json,subprocess
from build import ROOT,HERE,dump,digest

BASE_COMMIT='3f21ac1'
def record(w):
    result=subprocess.run(['git','show',BASE_COMMIT+':world-draft/WorldAlpha - World.json'],cwd=ROOT,check=True,stdout=subprocess.PIPE)
    before=json.loads(result.stdout.decode('utf-8-sig'))
    paths=[(k,) for k in w if k!='parties']
    paths += [('parties','',k) for k in ['quests','questTriggers','arcs']]
    rows=[]
    def get(v,path):
        for k in path:v=v[k]
        return v
    for path in paths:
        a,b=get(before,path),get(w,path)
        if a==b:continue
        if isinstance(a,dict) and isinstance(b,dict):
            added={k:digest(v) for k,v in b.items() if k not in a}
            changed={k:{'before':a[k],'afterSha256':digest(b[k])} for k in a if k in b and a[k]!=b[k]}
            removed={k:v for k,v in a.items() if k not in b}
            rows.append({'path':list(path),'added':added,'changed':changed,'removed':removed})
        else:rows.append({'path':list(path),'before':a,'afterSha256':digest(b)})
    dump(HERE/'approved-delta.json',{'baseCommit':BASE_COMMIT,'purpose':'Exact authorized expansion and requested live-playtest fixes; old fingerprints remain independently checked.','rows':rows})

