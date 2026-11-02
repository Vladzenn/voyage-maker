"""Copy completed built-in outputs to exact canonical NPC filenames; JSON on stdin."""
import hashlib,json,pathlib,shutil,sys
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
from voyage_portraits import image_info,write_json

ROOT=pathlib.Path(__file__).resolve().parents[2]
HERE=pathlib.Path(__file__).resolve().parent
briefs=json.loads((HERE/'supporting-portrait-briefs.json').read_text(encoding='utf-8'))
ledger=HERE/'supporting-generated-art.json'
state=json.loads(ledger.read_text(encoding='utf-8')) if ledger.exists() else {'generator':'built-in image_gen','onePass':True,'assets':[]}
known={r['name']:r for r in state['assets']}
for row in json.load(sys.stdin):
    name=row['name'];assert name in briefs
    source=pathlib.Path(row['source']).resolve()
    assert 'generated_images' in source.parts and source.suffix.lower()=='.png',source
    target=(ROOT/briefs[name]['target']).resolve()
    assert target.parent==(ROOT/'world-draft/npc portraits/Akitsuhara').resolve() and target.stem==name
    data=source.read_bytes();mime,width,height=image_info(data);digest=hashlib.sha256(data).hexdigest()
    assert width>=600 and height>=600 and mime=='image/png'
    if target.exists():assert hashlib.sha256(target.read_bytes()).hexdigest()==digest,'Existing image differs: '+name
    else:target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source,target)
    item={'name':name,'source':str(source),'target':briefs[name]['target'],'sha256':digest,'width':width,'height':height,'pose':briefs[name]['pose'],'profile':briefs[name]['profile'],'onePass':True,'review':'pending'}
    if name in known:assert known[name]['sha256']==digest,'Already saved a different generation for '+name
    else:state['assets'].append(item);known[name]=item
    briefs[name]['generationStatus']='generated'
write_json(ledger,state);write_json(HERE/'supporting-portrait-briefs.json',briefs)
print(json.dumps({'saved':len(known),'remaining':len(briefs)-len(known)},ensure_ascii=False))
