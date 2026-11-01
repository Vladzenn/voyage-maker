"""Package the canonical release; optionally install an explicitly supplied validated candidate."""
import argparse
import copy
import csv
import json
import pathlib
import shutil
import zipfile

ROOT=pathlib.Path(__file__).resolve().parents[2]
TEMP=ROOT/'tmp/adventurers'
DRAFT=ROOT/'world-draft'
OUT=ROOT/'output/adventurers-of-glowhaven'
OUT.mkdir(parents=True,exist_ok=True)
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--candidate',type=pathlib.Path,help='Explicit validated candidate to install; omitted packages the current canonical world.')
args=parser.parse_args()
w=json.loads((args.candidate or DRAFT/'WorldAlpha - World.json').read_text(encoding='utf-8'))
m=json.loads((ROOT/'tools/adventurers/manifest.json').read_text(encoding='utf-8'))
write=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
for name in m['npcs']:
    path=DRAFT/'npc portraits'/(name+'.png')
    assert path.exists(), 'Missing actual portrait: '+name
if args.candidate:write(DRAFT/'WorldAlpha - World.json',w)
release=DRAFT/'The Schools of Magic, Arise! Full World Update 4 - Adventurers of Glowhaven.json'
write(release,w)
cards={name:w['npcs'][name] for name in m['npcs']}
write(OUT/'New Character Cards.json',cards)
card_text='# Adventurers of Glowhaven — new character cards\n\nNative NPC objects for review or individual copying. The canonical roster remains in the full world. Upload each accompanying portrait in Studio before filling its portraitUrl.\n\n'
for name,npc in cards.items():
    card_text+='## '+name+'\n\n```json\n'+json.dumps(npc,ensure_ascii=False,indent=2)+'\n```\n\n'
(DRAFT/'Adventurers of Glowhaven - New Character Cards.md').write_text(card_text,encoding='utf-8',newline='\n')
with (DRAFT/'Adventurers of Glowhaven - Cast Rebalance.csv').open('w',encoding='utf-8-sig',newline='') as handle:
    writer=csv.DictWriter(handle,fieldnames=['name','old','new','tier']);writer.writeheader();writer.writerows(m['levelChanges'])
native=copy.deepcopy(w)
native['death']['permadeath']=True
native['death']['instructions']='This separate solo Ironman world uses native permanent death. After the sole player actually dies, give a brief final epilogue grounded in established people and choices. No routine resurrection, knockout return or invented final words. Ordinary nonlethal practice and actual capture remain their real outcomes rather than an invented death. Never invoke death for empty Mana or Stamina.'
native['gameModes']={'💀 Ironman Mode':native['gameModes']['💀 Ironman Mode']}
native['gameModes']['💀 Ironman Mode']['description']='Native permanent death. Start this separate world solo: one life, with no ordinary return after a genuine lethal defeat. All other Adventurers of Glowhaven content is included.'
write(OUT/'Adventurers of Glowhaven - Native Ironman - Solo.json',native)
with zipfile.ZipFile(OUT/'Adventurers of Glowhaven - Portraits.zip','w',compression=zipfile.ZIP_DEFLATED,compresslevel=5) as bundle:
    for name in m['npcs']:bundle.write(DRAFT/'npc portraits'/(name+'.png'),arcname=name+'.png')
shutil.copyfile(DRAFT/'Adventurers of Glowhaven - Patch Notes.md',OUT/'Patch Notes.md')
print(json.dumps({'world':str(release),'nativeIronman':str(OUT/'Adventurers of Glowhaven - Native Ironman - Solo.json'),
                 'portraits':str(OUT/'Adventurers of Glowhaven - Portraits.zip'),'newCards':str(OUT/'New Character Cards.json')},ensure_ascii=False))
