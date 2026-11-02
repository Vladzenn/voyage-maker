"""Resumable official location uploads, exact image-only merge and local delivery."""
import argparse,copy,csv,hashlib,json,pathlib,sys,zipfile
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
from voyage_portraits import Client,upload,image_info,write_json,valid_url
ROOT=pathlib.Path(__file__).resolve().parents[2]
HERE=pathlib.Path(__file__).resolve().parent
ART=HERE/'location-art'
WORLD=ROOT/'world-draft/WorldAlpha - World.json'
BASE='https://api-alpha.aidungeon.com/creator/v1'
SHORT='0kL8UR7rgsu2'
OUT=ROOT/'output/steel-and-spirits-art-2026-11-03'
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def record(w,j):return w['locations'][j['location']]['areas'][j['area']] if j['area'] else w['locations'][j['location']]
def run_upload(key):
    jobs=load(ART/'jobs.json');w=load(WORLD)
    client=Client(BASE,key.read_text(encoding='utf-8-sig').strip());contract=client.contract();constraints=contract['x-media-constraints']
    for kind in ['LOCATION_IMAGE','AREA_IMAGE']:assert kind in constraints['targets']
    write_json(ART/'official-media-contract.json',{'apiBase':BASE,'contractSHA256':hashlib.sha256(json.dumps(contract,sort_keys=True).encode()).hexdigest(),'constraints':constraints,'studioSaved':False})
    statepath=ROOT/'tmp/creator-api/oni-location-upload-state.json';state=load(statepath) if statepath.exists() else {}
    (ART/'hosted').mkdir(exist_ok=True);failed=[];uploaded=0
    for j in jobs:
        generated=ART/'generated'/(j['id']+'.json');receipt=ART/'hosted'/(j['id']+'.json')
        if not generated.exists():continue
        g=load(generated);data=(ROOT/g['file']).read_bytes();mime,width,height=image_info(data)
        assert hashlib.sha256(data).hexdigest()==g['sha256']
        if receipt.exists():assert load(receipt)['sha256']==g['sha256'];continue
        existing=record(w,j).get('images',{}).get('establishingShot',{}).get('imageUrl')
        assert not valid_url(existing),'An existing valid image requires explicit replacement selection: '+j['id']
        row={**g,'name':j['area'] or j['location'],'file':str(ROOT/g['file'])}
        try:
            url,status=upload(client,SHORT,row,state,lambda:write_json(statepath,state),constraints,j['target'])
            write_json(receipt,{**g,'url':url,'status':status});uploaded+=1
            print(json.dumps({'id':j['id'],'status':status},ensure_ascii=False),flush=True)
        except Exception as e:
            failure={'id':j['id'],'status':'failed','error':str(e)};failed.append(failure)
            write_json(ART/('failed-'+j['id']+'.json'),failure);print(json.dumps(failure,ensure_ascii=False),flush=True)
    report={'generated':len(list((ART/'generated').glob('*.json'))),'hosted':len(list((ART/'hosted').glob('*.json'))),'expected':len(jobs),'uploadedThisRun':uploaded,'failures':failed,'studioSaved':False,'studioPublished':False}
    write_json(ART/'upload-report.json',report);print(json.dumps(report))
    if failed:raise SystemExit(1)
def merge(key):
    jobs=load(ART/'jobs.json');original=WORLD.read_bytes();before=json.loads(original.decode('utf-8'));w=copy.deepcopy(before);diff=[]
    receipts=[load(ART/'hosted'/(j['id']+'.json')) for j in jobs]
    assert len(jobs)==110 and len({j['id'] for j in jobs})==110
    assert len({r['sha256'] for r in receipts})==110,'Each selected image must be distinct'
    assert len({r['url'] for r in receipts})==110,'Each selected image must have its own hosted URL'
    for j in jobs:
        r=load(ART/'hosted'/(j['id']+'.json'));assert r['location']==j['location'] and r['area']==j['area'] and r['target']==j['target']
        assert hashlib.sha256((ROOT/j['file']).read_bytes()).hexdigest()==r['sha256'];assert valid_url(r['url'])
        old=record(before,j).get('images',{}).get('establishingShot',{}).get('imageUrl')
        assert not valid_url(old) or old==r['url'],'Preserve unrelated existing artwork'
        shot=record(w,j).setdefault('images',{}).setdefault('establishingShot',{});shot.setdefault('crop',{'focus':{'x':50,'y':50},'zoom':100});shot['imageUrl']=r['url']
        diff.append({'path':['locations',j['location']]+(['areas',j['area']] if j['area'] else [])+['images','establishingShot'],'before':record(before,j).get('images',{}).get('establishingShot'),'after':copy.deepcopy(shot),'sha256':r['sha256']})
    # Undo only the selected additions: exact equality proves all other fields survived.
    restored=copy.deepcopy(w)
    for j in jobs:
        r=record(restored,j);old=record(before,j)
        if 'images' in old:r['images']=copy.deepcopy(old['images'])
        else:r.pop('images',None)
    assert restored==before,'Unexpected non-art edit'
    pins=load(ART/'latest-placement.json')['sourcePins']
    for name,pin in pins.items():assert all(w['locations'][name][k]==v for k,v in pin.items())
    from project import validate
    validate(w)
    client=Client(BASE,key.read_text(encoding='utf-8-sig').strip())
    validation=client.request('POST','/validate',body={'world':{'initialGameState':w},'stage':'draft'})
    write_json(ART/'official-validation.json',validation)
    assert validation['data']['valid'] and not validation['data']['errors'],validation['data']
    assert WORLD.read_bytes()==original,'Canonical changed during validation; receipts remain safe'
    write_json(WORLD,w)
    from regression_delta import record as delta
    delta(w)
    write_json(ART/'merge-report.json',{'imagesApplied':len(jobs),'allSourcePinsPreserved':len(pins),'onlySelectedImageFieldsChanged':True,'diff':diff,'officialValidation':validation,'studioSaved':False,'studioPublished':False})
    print(json.dumps({'imagesApplied':len(jobs),'validation':validation['data']},ensure_ascii=False))
def review():
    from PIL import Image,ImageDraw,ImageFont
    jobs=load(ART/'jobs.json');OUT.mkdir(parents=True,exist_ok=True)
    font=ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf',15);available=[j for j in jobs if (ROOT/j['file']).exists()]
    for start in range(0,len(available),20):
        batch=available[start:start+20];sheet=Image.new('RGB',(5*246,((len(batch)+4)//5)*278),'#13191e');d=ImageDraw.Draw(sheet)
        for i,j in enumerate(batch):
            im=Image.open(ROOT/j['file']).convert('RGB');im.thumbnail((236,236));x=(i%5)*246+5;y=(i//5)*278+5;sheet.paste(im,(x,y));label=(j['area'] or j['location']).replace('Benitsuru Portal Shrine - ','')
            d.text((x,y+240),label,font=font,fill='white')
        sheet.save(OUT/f'Location Art Review {start//20+1}.jpg',quality=92)
    print(json.dumps({'reviewedFiles':len(available),'originalPixelsModified':False}))
def package():
    jobs=load(ART/'jobs.json');OUT.mkdir(parents=True,exist_ok=True);w=load(WORLD)
    (OUT/'The Schools of Magic, Arise! - Steel and Spirits.json').write_bytes(WORLD.read_bytes())
    write_json(OUT/'Locations - Steel and Spirits.json',w['locations'])
    with zipfile.ZipFile(OUT/'Steel and Spirits - Location Artwork.zip','w',zipfile.ZIP_DEFLATED) as z:
        for j in jobs:z.write(ROOT/j['file'],('Areas/' if j['area'] else 'Locations/')+pathlib.Path(j['file']).name)
    with (OUT/'Location Artwork Index.csv').open('w',encoding='utf-8-sig',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=['id','location','area','target','file','region','x','y','url']);writer.writeheader()
        for j in jobs:
            r=load(ART/'hosted'/(j['id']+'.json'));l=w['locations'][j['location']];writer.writerow({**{k:j[k] for k in ['id','location','area','target','file']},**{k:l[k] for k in ['region','x','y']},'url':r['url']})
    print(json.dumps({'images':len(jobs),'worldSHA256':hashlib.sha256(WORLD.read_bytes()).hexdigest(),'output':str(OUT)},ensure_ascii=False))
def main():
    p=argparse.ArgumentParser();p.add_argument('command',choices=['upload','merge','review','package']);p.add_argument('--key-file',type=pathlib.Path);a=p.parse_args()
    if a.command in ['upload','merge']:assert a.key_file; (run_upload if a.command=='upload' else merge)(a.key_file)
    elif a.command=='review':review()
    else:package()
if __name__=='__main__':main()
