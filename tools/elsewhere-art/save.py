"""Save one selected built-in image per requested asset; no world or API writes."""
import argparse,hashlib,json,pathlib,shutil
from PIL import Image
ROOT=pathlib.Path(__file__).resolve().parents[2];HERE=pathlib.Path(__file__).resolve().parent

def save(kind,name,source):
    brief=json.loads((HERE/'brief.json').read_text(encoding='utf-8'))
    allowed={'map':{'The Lantern Circuit'},'location':{l['name'] for l in brief['locations']},'portrait':set(brief['npcs'])}
    assert name in allowed[kind]
    ledger_path=HERE/'manifest.json';ledger=json.loads(ledger_path.read_text(encoding='utf-8')) if ledger_path.exists() else {}
    key=kind+'::'+name;assert key not in ledger,'Already generated; do not repeat a selected image'
    folder={'map':'region maps/Elsewhere','location':'location images/Elsewhere','portrait':'npc portraits/Rebirth'}[kind]
    dest=ROOT/'world-draft'/folder/(name+'.png');assert not dest.exists()
    src=pathlib.Path(source);assert src.is_file() and src.suffix.lower()=='.png'
    shutil.copy2(src,dest)
    with Image.open(dest) as img:width,height=img.size;img.verify()
    ledger[key]=dict(kind=kind,name=name,file=dest.relative_to(ROOT).as_posix(),sha256=hashlib.sha256(dest.read_bytes()).hexdigest(),width=width,height=height,source=str(src),generationPasses=1,uploaded=False)
    ledger_path.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'saved':name,'kind':kind,'dimensions':[width,height],'savedCount':len(ledger)},ensure_ascii=False))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('kind',choices=['map','location','portrait']);p.add_argument('name');p.add_argument('source');a=p.parse_args();save(a.kind,a.name,a.source)
