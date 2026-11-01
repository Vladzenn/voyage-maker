"""Release preservation audit. Not a live Studio or semantic-model test."""
import hashlib
import json
import pathlib
import sys

ROOT=pathlib.Path(__file__).resolve().parents[2]
w=json.loads(pathlib.Path(sys.argv[1] if len(sys.argv)>1 else ROOT/'world-draft/WorldAlpha - World.json').read_text(encoding='utf-8'))
m=json.loads((ROOT/'tools/phantom/manifest.json').read_text(encoding='utf-8'))
p=m['preservation'];count=0
def ck(ok,message):
    global count
    count+=1
    if not ok:raise AssertionError(message)
def digest(v):return hashlib.sha256(json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode('utf-8')).hexdigest()
for row in p['media']:
    value=w
    for k in row['path']:value=value[k]
    ck(value==row['value'],'Retain supplied media/voice state '+str(row['path']))
for k,expected in p['npcs'].items():ck(digest(w['npcs'][k])==expected,'Unchanged supplied NPC '+k)
for field in ['locations','realms','regions']:ck(digest(w[field])==p[field],'Keep supplied maps, images and region settings '+field)
for field,collection in [('originalItems','itemTypes'),('originalAbilities','abilities'),('triggers','triggerDefinitions')]:
    for k,expected in p[field].items():ck(digest(w[collection][k])==expected,'Protected existing '+collection+'/'+k)
for k,expected in p['quests'].items():ck(digest(w['parties']['']['quests'][k])==expected,'Unrelated quest unchanged '+k)
for k,variants in p['musicVariants'].items():ck(w['gameplayMusicSettings']['tracks'][k]['variants']==variants,'Supplied audio preserved '+k)
for name in m['newTraits']:
    t=w['traits'][name]
    for field in ['skills','attributes','resources','abilities','startingItems','requirements','unlockedBy','excludedBy']:
        ck(isinstance(t[field],list),'Required new trait array '+name+'/'+field)
    if name.startswith(('Hair Style','Outfit','Accessory','Portrait')):
        ck(not any(t[k] for k in ['skills','attributes','resources','abilities','startingItems']),'Visual choice has no grant '+name)
for name in m['talents']:
    t=w['traits'][name]
    ck(any(t[k] for k in ['skills','attributes','resources','abilities']),'Talent has actual mechanics '+name)
    for s in t['skills']:ck(s['skill'] not in ['Space Magic','Time Magic'],'No reserved starting discipline '+name)
for name in m['newAbilities']:
    a=w['abilities'][name]
    ck(len(a['requirements'])==1 and a['requirements'][0]['type']=='trait' and a['requirements'][0]['variable'] in m['talents'] and a['requirements'][0].get('amount')==1,'Complete talent-only technique requirement '+name)
    ck('Costs ' in a['description'] and a['cooldown']>=4,'Finite new technique '+name)
for old,new in m['uiRenames'].items():
    ck(new in w['storyStarts'] and w['storyStarts'][new]['name']==new,'Exact compatible menu ID '+new)
    ck(old not in json.dumps(w,ensure_ascii=False),'No stale start reference '+old)
ck(w['npcs']['Marika Hoshino']['level']==30,'User Marika edit retained')
ck(w['npcs']['Ragnar Leonhart']['level']==67 and w['npcs']['Ilyra Stillglass']['level']==100,'Named power exceptions retained')
ck(w['progressionSettings']['attributePointEveryLevels']==3,'User attribute cadence retained')
ck(w['resourceSettings']['Stamina']['initialValue']==100 and w['resourceSettings']['Stamina']['maxValue']==100,'Requested Stamina baseline')
ck(w['resourceSettings']['Stamina']['restRechargeMultiplier']==0.8,'User rest fraction retained')
ck('💀 Permadeath Mode' in w['gameModes'],'User mode rename retained')
ck('Bronze Guild Badge' not in w['itemTypes'],'Do not create the erroneous badge alias')
print(json.dumps(dict(status='passed',checks=count,preservedNPCs=len(p['npcs']),preservedItems=len(p['originalItems']),preservedAbilities=len(p['originalAbilities']),preservedTriggers=len(p['triggers']),liveStudioValidation=False,livePlaytest=False)))
