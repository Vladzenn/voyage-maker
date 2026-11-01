"""Install an explicitly validated Crucible candidate and package its review artifacts."""
import argparse, copy, csv, hashlib, json, pathlib, shutil, subprocess, sys, zipfile

ROOT=pathlib.Path(__file__).resolve().parents[2]
HERE=pathlib.Path(__file__).resolve().parent
DRAFT=ROOT/'world-draft';OUT=ROOT/'output/champions-of-the-crucible'
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--candidate',type=pathlib.Path)
args=parser.parse_args()
m=json.loads((HERE/'manifest.json').read_text(encoding='utf-8'))
path=args.candidate or DRAFT/'WorldAlpha - World.json'
w=json.loads(path.read_text(encoding='utf-8-sig'))
sys.path.insert(0,str(ROOT/'tools'))
from project import validate
validate(w)
subprocess.run(['node',str(ROOT/'tools/test_crucible.cjs'),str(path.resolve())],cwd=ROOT,check=True)
if args.candidate:
    current=DRAFT/'WorldAlpha - World.json'
    old=json.loads(current.read_text(encoding='utf-8-sig'))
    if 'cc1_register' not in old['triggerDefinitions']:
        assert hashlib.sha256(current.read_bytes()).hexdigest()==m['sourceSHA256'],'Canonical changed since explicit merge base; merge before installing.'
OUT.mkdir(parents=True,exist_ok=True)
def write(path,obj):
    path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
if args.candidate:write(DRAFT/'WorldAlpha - World.json',w)
release=DRAFT/'The Schools of Magic, Arise! Full World Update 5 - Champions of the Crucible.json'
write(release,w)
write(OUT/'New NPC Cards.json',{n:w['npcs'][n] for n in m['npcs']})
write(OUT/'New Abilities.json',{n:w['abilities'][n] for n in m['abilities']})
write(OUT/'New Dungeon and Creature Types.json',{'realms':{n:v for n,v in w['realms'].items() if n=='The Sepulchral Conservatory'},'regions':{n:v for n,v in w['regions'].items() if v.get('realm')=='The Sepulchral Conservatory'},'locations':{n:v for n,v in w['locations'].items() if v['region']=='Sepulchral Gardens'},'npcTypes':{n:w['npcTypes'][n] for n in m['types']}})

# One-pass image ledger is authoritative. Never regenerate missing images implicitly.
done=json.loads((HERE/'art-results.json').read_text(encoding='utf-8'))
assert len({x['name'] for x in done})==43,'Portrait batch is incomplete; recover existing jobs first.'
assert set(m['npcs'])=={x['name'] for x in done}
flags={
 'Threnvoss':'Antler tips approach/crop top edge; retained under one-pass rule.',
 'Nene Inui':'Tall ear silhouette reaches/crops top; review before upload.',
 'Rena Kogetsu':'Androgynous/masculine presentation may not match intended female card; author review.',
 'Fuyumi Hase':'Generated face reads masculine against female card; author review, no unrequested regeneration.',
}
art=[]
with zipfile.ZipFile(OUT/'Crucible Portraits.zip','w',compression=zipfile.ZIP_STORED) as z:
    for row in done:
        p=ROOT/row['file'];assert p.is_file(),str(p)
        z.write(p,arcname=p.name)
        art.append(dict(name=row['name'],kind='NPC',file=row['file'],review=flags.get(row['name'],'One-pass image; inspect headroom, anatomy and crop in Studio.'),upload='Upload in Studio; no hosted URL was fabricated.'))
env=json.loads((HERE/'environment-results.json').read_text(encoding='utf-8')) if (HERE/'environment-results.json').exists() else []
for row in env:
    assert (ROOT/row['file']).is_file()
    art.append(dict(name=row['name'],kind='Map' if 'Map' in row['name'] else 'Location',file=row['file'],review='One-pass environment; arrange/crop in Studio.',upload='Upload in Studio; existing media preserved.'))
write(OUT/'Artwork Manifest.json',art)
with (OUT/'Artwork Manifest.csv').open('w',encoding='utf-8-sig',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=['name','kind','file','review','upload']);writer.writeheader();writer.writerows(art)
native=copy.deepcopy(w);native['death']['permadeath']=True
mode='💀 Permadeath Mode';native['gameModes']={mode:native['gameModes'][mode]}
native['gameModes'][mode]['description']='Solo native permanent death after a genuine lethal outcome. Regulated nonlethal Crucible contests retain their sporting intent; verify stoppage behavior in Voyage before relying on tournament safety.'
write(OUT/'The Schools of Magic, Arise! - Native Permadeath - Solo.json',native)
for src,dest in [('Champions of the Crucible - Patch Notes.md','Patch Notes.md'),('Champions of the Crucible - Mechanics and Playtest Guide.md','Mechanics and Playtest Guide.md')]:
    if (DRAFT/src).exists():shutil.copyfile(DRAFT/src,OUT/dest)
write(OUT/'Release Summary.json',{'fullWorld':str(release.relative_to(ROOT)),'worldSHA256':hashlib.sha256(release.read_bytes()).hexdigest(),'newNPCs':len(m['npcs']),'newAbilities':len(m['abilities']),'newQuests':len(m['quests']),'newTriggers':len(m['triggers']),'portraits':len(done),'environmentImages':len(env),'liveStudioValidation':False})
print(json.dumps({'release':str(release),'portraits':str(OUT/'Crucible Portraits.zip'),'cards':str(OUT/'New NPC Cards.json'),'output':str(OUT)},ensure_ascii=False))
