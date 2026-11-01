"""Package the current canonical patch, or install an explicitly validated candidate."""
import argparse
import copy
import json
import pathlib
import shutil

ROOT=pathlib.Path(__file__).resolve().parents[2]
DRAFT=ROOT/'world-draft';OUT=ROOT/'output/phantom-patch';OUT.mkdir(parents=True,exist_ok=True)
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--candidate',type=pathlib.Path)
args=parser.parse_args()
w=json.loads((args.candidate or DRAFT/'WorldAlpha - World.json').read_text(encoding='utf-8'))
m=json.loads((ROOT/'tools/phantom/manifest.json').read_text(encoding='utf-8'))
def write(path,data):path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
if args.candidate:write(DRAFT/'WorldAlpha - World.json',w)
release=DRAFT/'The Schools of Magic, Arise! Minor Patch - Character Creation and Polish.json'
write(release,w)
native=copy.deepcopy(w);mode='💀 Permadeath Mode'
native['death']['permadeath']=True
native['death']['instructions']='This separate solo Permadeath world uses native permanent death. After the sole player actually dies, give a brief final epilogue grounded in their real choices. No routine revival, invented final words or knockout return after a lethal result. Nonlethal training, capture and sleep keep their actual outcomes. Empty Mana or Stamina is never death by itself.'
native['gameModes']={mode:native['gameModes'][mode]}
native['gameModes'][mode]['description']='Native permanent death. Start this separate world solo: one life, no ordinary return after a genuine lethal defeat. Includes the current character creation and polish patch.'
write(OUT/'The Schools of Magic, Arise! - Native Permadeath - Solo.json',native)
guide='# Character creation patch — review guide\n\nThese are creation choices, not automatically awarded content. The full world is the import source; native bonuses apply once. Visual options do not grant stat-bearing equipment.\n\n## Special Talents\n\nOptional, one choice. Each listed technique is actually granted by its talent; no Space or Time starting gift is supplied.\n\n| Talent | Benefits and trade-offs | Technique |\n|---|---|---|\n'
for name in m['talents']:
    t=w['traits'][name];effects=[]
    for field,target in [('attributes','attribute'),('skills','skill'),('resources','resource')]:
        effects.extend(f"{x['modifier']:+} {x[target]}"+(' capacity' if field=='resources' else '') for x in t[field])
    effects.extend('Resistance: '+x for x in t.get('resistances',[]))
    effects.extend('Vulnerability: '+x for x in t.get('vulnerabilities',[]))
    guide+='| '+name+' | '+', '.join(effects)+' | '+', '.join(t['abilities'])+' |\n'
guide+='\n## Professions\n\nOptional, one prior profession. No current job, licence, workshop or free work kit is implied.\n\n'
for g in w['traitCategories']['Profession & Useful Skills']['subcategories']:
    guide+='### '+g['name']+'\n\n'
    for name in g['traits']:guide+='- **'+name+':** '+w['traits'][name]['description']+'\n'
    guide+='\n'
guide+='## Equipment additions\n\nNew catalogue objects can appear through actual appropriate shopping or acquisition. The separate starting-kit selection still permits at most one kit.\n\n'
guide+='\n'.join('- '+name for name in m['newItems'])+'\n'
(DRAFT/'Phantom Patch - Creation Guide.md').write_text(guide,encoding='utf-8',newline='\n')
shutil.copyfile(DRAFT/'Phantom Patch - Patch Notes.md',OUT/'Patch Notes.md')
print(json.dumps(dict(world=str(release),nativePermadeath=str(OUT/'The Schools of Magic, Arise! - Native Permadeath - Solo.json'),guide=str(DRAFT/'Phantom Patch - Creation Guide.md')),ensure_ascii=False))
