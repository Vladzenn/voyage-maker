"""Merge the author's newer complete section exports, with approved name aliases."""
import hashlib,json
from pathlib import Path
import update
w=update.load(update.WORLD)
fn=update.replacer({**update.names(),**update.FAMILIES})
first=update.replacer({a.split()[0]:b.split()[0] for a,b in update.names().items()})
inputs={
 'locations':Path('C:/Users/VladCodes/.codex/attachments/0ca4ed96-fe6d-4391-86e4-f24e8da6b88c/Pasted text.txt'),
 'regions':Path('C:/Users/VladCodes/.codex/attachments/4e9fcc70-3dd8-4045-993c-f4e468737be4/Pasted text.txt')}
report={}
for section,path in inputs.items():
 raw=path.read_bytes();data=json.loads(raw.decode('utf-8-sig'));incoming=update.walk(data,fn)
 if section=='locations':
  for k,v in incoming.items():
   if w['regions'][v['region']]['realm']=='Ardelis':incoming[k]=update.walk(v,first)
 assert set(incoming)==set(w[section]),'Unexpected removed/new records need review'
 changed=[k for k in incoming if incoming[k]!=w[section][k]]
 w[section]=incoming
 report[section]={'sourceSHA256':hashlib.sha256(raw).hexdigest(),'normalizedSectionHash':update.digest(incoming),'count':len(incoming),'changed':changed}
update.write(update.HERE/'section-merge.json',report)
pins=update.load(update.HERE/'placements.json')
for pin in pins:
 loc=w['locations'][pin['name']]
 for key in ['region','x','y']:pin[key]=loc[key]
 pin['placementStatus']='Author-corrected Studio export, 5 November'
update.write(update.HERE/'placements.json',pins)
update.write(update.WORLD,w);update.proof(w)
print(json.dumps({s:{'count':v['count'],'updated':len(v['changed'])} for s,v in report.items()}))
