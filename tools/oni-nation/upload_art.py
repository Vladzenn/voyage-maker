#!/usr/bin/env python3
"""Upload only this update's selected new art; never save or publish a Studio world."""
import argparse,hashlib,json,pathlib,sys
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
from voyage_portraits import Client,upload,image_info,write_json,valid_url

ROOT=pathlib.Path(__file__).resolve().parents[2]
HERE=pathlib.Path(__file__).resolve().parent
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--key-file',type=pathlib.Path,required=True);ap.add_argument('--short-id',default='0kL8UR7rgsu2');ap.add_argument('--apply',action='store_true');a=ap.parse_args()
    key=a.key_file.read_text(encoding='utf-8-sig').strip()
    client=Client('https://api-alpha.aidungeon.com/creator/v1',key)
    contract=client.contract();constraints=contract['x-media-constraints']
    if 'REGION_MAP_IMAGE' not in constraints['targets']:raise ValueError('Current contract has no supported map target')
    source=json.loads((HERE/'generated-art.json').read_text(encoding='utf-8'))
    world=json.loads((ROOT/'output/oni-nation-2026-11-02/Akitsuhara - Candidate.json').read_text(encoding='utf-8'))
    manifest=json.loads((HERE/'manifest.json').read_text(encoding='utf-8'))
    statepath=ROOT/'tmp/creator-api/oni-upload-state.json'
    state=json.loads(statepath.read_text(encoding='utf-8')) if statepath.exists() else {}
    save=lambda:write_json(statepath,state)
    receipts=[];report={'apiBase':client.base,'worldShortId':a.short_id,'contractSha256':hashlib.sha256(json.dumps(contract,sort_keys=True).encode()).hexdigest(),'rows':[],'studioSaved':False,'studioPublished':False}
    failed=False
    for asset in source['assets']:
        p=ROOT/asset['target'];data=p.read_bytes();mime,width,height=image_info(data)
        if hashlib.sha256(data).hexdigest()!=asset['sha256']:raise ValueError('Local art drift: '+asset['name'])
        ismap=asset['name']=='Veiled Cedar Reach Map'
        name='Veiled Cedar Reach' if ismap else asset['name']
        if not ismap:
            if name not in manifest['majorNpcs'] or p.stem!=name:raise ValueError('Unapproved name/filename: '+name)
            if valid_url(world['npcs'][name].get('portraitUrl')):raise ValueError('Refusing to replace an existing valid portrait: '+name)
        target='REGION_MAP_IMAGE' if ismap else 'NPC_PORTRAIT'
        row={'name':name,'file':str(p),'sha256':asset['sha256'],'mimeType':mime,'width':width,'height':height,'bytes':len(data),'target':target}
        if not a.apply:row['status']='planned'
        else:
            try:
                url,status=upload(client,a.short_id,row,state,save,constraints,target)
                receipts.append({'name':name,'target':target,'url':url,'sha256':asset['sha256'],'file':asset['target']});row.update(status=status,url=url)
            except Exception as e:
                row.update(status='failed',error=str(e));failed=True
        report['rows'].append(row)
        write_json(HERE/'art-upload-report.json',report)
        if a.apply:write_json(HERE/'hosted-art.json',receipts)
        print(json.dumps({'name':name,'status':row['status']},ensure_ascii=False),flush=True)
    if failed:raise SystemExit(1)
    print(json.dumps({'uploadedOrResumed':len(receipts),'oldPortraitsReplaced':0,'studioSaved':False}))
if __name__=='__main__':main()
