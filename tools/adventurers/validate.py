"""Portable preservation checks for the released update, including latest user artwork."""
import hashlib
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
path = pathlib.Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/'world-draft/WorldAlpha - World.json'
w = json.loads(path.read_text(encoding='utf-8'))
m = json.loads((ROOT/'tools/adventurers/manifest.json').read_text(encoding='utf-8'))
p = m['preservation']
checks=0


def ck(ok, label):
    global checks
    checks += 1
    if not ok: raise AssertionError(label)


def digest(value):
    return hashlib.sha256(json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode('utf-8')).hexdigest()


for row in p['media']:
    value=w
    for key in row['path']:value=value[key]
    ck(value==row['value'],'Existing hosted media preserved: '+str(row['path']))
for name, fields in p['locationFields'].items():
    for key,value in fields.items():ck(w['locations'][name][key]==value,'Map/state field preserved '+name+'/'+key)
ck(digest(w['realms'])==p['realmsHash'],'Realm maps and order preserved')
ck(digest(w['regions'])==p['regionsHash'],'Region maps, bounds and level bands preserved')
for name,expected in p['questHashes'].items():ck(digest(w['parties']['']['quests'][name])==expected,'Existing quest unchanged '+name)
for name,expected in p['itemHashes'].items():ck(digest(w['itemTypes'][name])==expected,'Existing item and image unchanged '+name)
for name,expected in p['triggerHashes'].items():ck(digest(w['triggerDefinitions'][name])==expected,'Unrelated event unchanged '+name)
for collection, section in [('protectedNPCs','npcs'),('spiderNPCs','npcs'),('spiderLocations','locations')]:
    for name,expected in p[collection].items():ck(digest(w[section][name])==expected,'Protected record unchanged '+name)
for name,voice in p['voices'].items():ck(w['npcs'][name].get('voiceTag')==voice,'User voice retained '+name)
for name in m['npcs']:
    n=w['npcs'][name]
    ck(n['detailType']=='detailed' and n['initialKnown'] is False,'Stable new person and visibility '+name)
    for label in ['Private motive','Concealment and knowledge','Relationships','How it surfaces']:
        ck('**'+label+':**' in n['hiddenInfo'],'Card structure '+name+'/'+label)
    ck('**Pronouns:**' not in n['basicInfo'] and 'Structured Profile' not in n['basicInfo'],'No retired profile fields '+name)
    ck(n['currentArea'] in w['locations'][n['currentLocation']]['areas'],'Exact new person placement '+name)
    for word in ['authored quest','trigger','save file','game engine','initialKnown']:
        ck(word.lower() not in n['basicInfo'].lower(),'No public implementation leakage '+name)
for name in m['arcs']:
    a=w['parties']['']['arcs'][name]
    ck(a['id']==name and a['status']=='active','Native arc identity '+name)
    ck(a['minQuestsForConclusion']>0 and bool(a['expectedConclusion']),'Arc has conclusion '+name)
    ck(not a['surfacePremise'].startswith(a['title']),'Premise is an actual circumstance '+name)
for title in m['quests']:
    q=w['parties']['']['quests'][title]
    ck(q['questLocation'] in w['locations'],'Real job location '+title)
    ck(q['questSource'] in w['npcs'],'Existing actual client '+title)
    ck('arcId' not in q,'No fabricated authored arc link '+title)
    ck(q['completionCondition']['query'].find(q['mainObjective'])>=0,'Finishing condition names stated final step '+title)
    for word in ['authored','trigger','save file']:
        ck(word not in q['questStatement'].lower(),'Natural public quest '+title)
for change in m['levelChanges']:
    ck(w['npcs'][change['name']]['level']==change['new'],'Approved cast anchor '+change['name'])
ck(w['npcs']['Ilyra Stillglass']['level']==100 and w['npcs']['Ragnar Leonhart']['level']==67,'Explicit level exceptions')
for tier, t in w['itemSettings']['tiers'].items():
    policy=t['bonusPolicy']
    ck(policy['refinedMaximumPicks']>=policy['initialMaximumPicks'],'Native refinement cap '+tier)
    ck(len(policy['allowedBonuses'])<=100,'Native permitted-bonus count '+tier)
    ck(len((t['description']+t['rarityGuidance']).encode('utf-16-le'))//2<=2000,'Tier text cap '+tier)
for name in m['triggers']:
    t=w['triggerDefinitions'][name]
    for c in t['conditions']:
        if 'value' in c and isinstance(c['value'],str):ck(len(c['value'].encode('utf-16-le'))//2<=100,'Trigger condition value cap '+name)
    for e in t['effects']:
        if e['type']=='story':ck(len(e['instruction'].encode('utf-16-le'))//2<=1000,'Story effect cap '+name)
print(json.dumps({'status':'passed','checks':checks,'preservedMediaURLs':len(p['media']),
                 'preservedExistingItems':len(p['itemHashes']),'preservedExistingQuests':len(p['questHashes']),
                 'preservedUnrelatedTriggers':len(p['triggerHashes']),
                 'liveStudioValidation':False,'livePlaytest':False}))
