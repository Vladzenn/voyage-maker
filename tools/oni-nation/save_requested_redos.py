"""Install only the two explicitly requested regeneration results, retaining provenance."""
import argparse,hashlib,json,pathlib,shutil
from build import ROOT,HERE,dump
from sys import path
path.insert(0,str(ROOT/'tools'))
from voyage_portraits import image_info

ap=argparse.ArgumentParser();ap.add_argument('--names',nargs='+',choices=['Sana Kuroiwa','Shōen Kagetsuna','Misao Shingū'],default=['Sana Kuroiwa','Shōen Kagetsuna']);args=ap.parse_args()
previous_results=HERE/'requested-redo-results.json'
known={x['name']:x for x in json.loads(previous_results.read_text(encoding='utf-8'))} if previous_results.exists() else {}
rows=[]
for name in args.names:
    event=json.loads((ROOT/'tmp/oni-generated-events'/(name+'.json')).read_text(encoding='utf-8-sig'))
    source=pathlib.Path(event['source']);assert source.is_file() and 'generated_images' in source.parts
    target=ROOT/'world-draft/npc portraits/Akitsuhara'/(name+'.png')
    previous=hashlib.sha256(target.read_bytes()).hexdigest()
    backup=ROOT/'output/oni-nation-2026-11-02/Previous Portraits'/(name+'.png');backup.parent.mkdir(parents=True,exist_ok=True)
    if not backup.exists():shutil.copy2(target,backup)
    data=source.read_bytes();mime,width,height=image_info(data);assert mime=='image/png'
    shutil.copy2(source,target)
    row={'name':name,'source':str(source),'target':str(target.relative_to(ROOT)).replace('\\','/'),'sha256':hashlib.sha256(data).hexdigest(),'width':width,'height':height,'previousSHA256':previous,'explicitlyRequested':True,'generationAttempt':2,'review':'pending'}
    rows.append(row)
    ledger=HERE/('generated-art.json' if name=='Shōen Kagetsuna' else 'supporting-generated-art.json')
    d=json.loads(ledger.read_text(encoding='utf-8'))
    item=next(x for x in d['assets'] if x['name']==name);item.update(row)
    dump(ledger,d)
for row in rows:known[row['name']]=row
dump(HERE/'requested-redo-results.json',list(known.values()))
print(json.dumps({'installed':[r['name'] for r in rows],'newPasses':len(rows)},ensure_ascii=False))
