"""Persist one completed built-in image and its exact location/area identity."""
import argparse,hashlib,json,pathlib,shutil,sys
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
from voyage_portraits import image_info,write_json
ROOT=pathlib.Path(__file__).resolve().parents[2]
ART=pathlib.Path(__file__).resolve().parent/'location-art'
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--id',required=True);ap.add_argument('--source',required=True,type=pathlib.Path);a=ap.parse_args()
    jobs=json.loads((ART/'jobs.json').read_text(encoding='utf-8'));job=next(j for j in jobs if j['id']==a.id)
    source=a.source.resolve();assert 'generated_images' in source.parts and source.suffix.lower()=='.png'
    data=source.read_bytes();mime,width,height=image_info(data);digest=hashlib.sha256(data).hexdigest()
    assert mime=='image/png' and min(width,height)>=600 and abs(width-height)<=2
    target=(ROOT/job['file']).resolve();assert ROOT in target.parents
    if target.exists():assert hashlib.sha256(target.read_bytes()).hexdigest()==digest,'A different selected image already exists'
    else:target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source,target)
    row={k:job[k] for k in ['id','location','area','target','file']}
    row.update(source=str(source),sha256=digest,mimeType=mime,width=width,height=height,bytes=len(data),generator='built-in image_gen',review='pending',generationPass=1)
    (ART/'generated').mkdir(exist_ok=True);write_json(ART/'generated'/(a.id+'.json'),row)
    print(json.dumps({'id':a.id,'saved':True,'dimensions':[width,height]},ensure_ascii=False))
if __name__=='__main__':main()
