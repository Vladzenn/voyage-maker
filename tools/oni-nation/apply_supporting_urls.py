"""Apply exact verified portrait receipts, preserving every unrelated world value."""
import copy,hashlib,json
from build import ROOT,HERE,dump
from sys import path
path.insert(0,str(ROOT/'tools'))
from voyage_portraits import valid_url

worldpath=ROOT/'world-draft/WorldAlpha - World.json'
before=json.loads(worldpath.read_text(encoding='utf-8'));w=copy.deepcopy(before)
briefs=json.loads((HERE/'supporting-portrait-briefs.json').read_text(encoding='utf-8'))
rows=json.loads((HERE/'supporting-hosted-art.json').read_text(encoding='utf-8'))
expected=set(briefs)|{'Shōen Kagetsuna'}
assert len(rows)==84 and {r['name'] for r in rows}==expected
assert len({r['url'] for r in rows})==len(rows),'Hosted URLs must be one-to-one'
changes=[]
for row in rows:
    name=row['name'];assert name in w['npcs'] and row['target']=='NPC_PORTRAIT' and valid_url(row['url'])
    p=ROOT/row['file'];assert p.stem==name and hashlib.sha256(p.read_bytes()).hexdigest()==row['sha256']
    old=w['npcs'][name].get('portraitUrl','')
    assert not valid_url(old) or old==row['url'] or name=='Shōen Kagetsuna','Unselected replacement: '+name
    w['npcs'][name]['portraitUrl']=row['url'];changes.append({'name':name,'oldUrl':old,'newUrl':row['url'],'sha256':row['sha256']})
probe=copy.deepcopy(w)
for c in changes:probe['npcs'][c['name']]['portraitUrl']=c['oldUrl']
assert probe==before,'Non-portrait mutation'
hosted=json.loads((HERE/'hosted-art.json').read_text(encoding='utf-8'))
merged={(r['target'],r['name']):r for r in hosted}
for r in rows:merged[(r['target'],r['name'])]=r
dump(HERE/'hosted-art.json',list(merged.values()));dump(worldpath,w)
m=json.loads((HERE/'manifest.json').read_text(encoding='utf-8'));m['supportingArtComplete']=True;m['supportingPortraits']=83
assert len(m['npcs'])==97 and all(valid_url(w['npcs'][n].get('portraitUrl')) for n in m['npcs'])
assert len({hashlib.sha256((ROOT/'world-draft/npc portraits/Akitsuhara'/(n+'.png')).read_bytes()).hexdigest() for n in m['npcs']})==97
dump(HERE/'manifest.json',m)
dump(HERE/'supporting-portrait-merge-report.json',{'changedFields':['npcs.'+c['name']+'.portraitUrl' for c in changes],'changes':changes,'nonPortraitChanges':0,'newCastPortraits':97,'oldPortraitsReplacedByExplicitRequest':['Shōen Kagetsuna'],'studioSaved':False,'studioPublished':False})
from regression_delta import record
record(w)
print(json.dumps({'newCast':97,'newCastWithPortraits':97,'appliedReceipts':84,'nonPortraitChanges':0}))
