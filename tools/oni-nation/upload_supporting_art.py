"""Resumable official uploads of generated supporting portraits; no Studio save."""
import argparse,hashlib,json,pathlib,sys
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
from voyage_portraits import Client,upload,image_info,write_json,valid_url

ROOT=pathlib.Path(__file__).resolve().parents[2]
HERE=pathlib.Path(__file__).resolve().parent

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--key-file',type=pathlib.Path,required=True);ap.add_argument('--apply',action='store_true');ap.add_argument('--limit',type=int);args=ap.parse_args()
    world=json.loads((ROOT/'world-draft/WorldAlpha - World.json').read_text(encoding='utf-8'))
    briefs=json.loads((HERE/'supporting-portrait-briefs.json').read_text(encoding='utf-8'))
    art=json.loads((HERE/'supporting-generated-art.json').read_text(encoding='utf-8'))
    redos=json.loads((HERE/'requested-redo-results.json').read_text(encoding='utf-8'))
    selected_major=next(r for r in redos if r['name']=='Shōen Kagetsuna')
    assets=art['assets']+[selected_major]
    ledger=HERE/'supporting-hosted-art.json'
    receipts=json.loads(ledger.read_text(encoding='utf-8')) if ledger.exists() else []
    known={r['name']:r for r in receipts}
    statepath=ROOT/'tmp/creator-api/oni-supporting-upload-state.json'
    state=json.loads(statepath.read_text(encoding='utf-8')) if statepath.exists() else {}
    client=Client('https://api-alpha.aidungeon.com/creator/v1',args.key_file.read_text(encoding='utf-8-sig').strip())
    contract=client.contract();constraints=contract['x-media-constraints']
    report={'apiBase':client.base,'worldShortId':'0kL8UR7rgsu2','contractSHA256':hashlib.sha256(json.dumps(contract,sort_keys=True).encode()).hexdigest(),'rows':[],'studioSaved':False,'studioPublished':False}
    attempts=0;failed=False
    for asset in assets:
        name=asset['name'];assert (name in briefs or name=='Shōen Kagetsuna') and name in world['npcs']
        p=ROOT/asset['target'];assert p.stem==name
        data=p.read_bytes();mime,width,height=image_info(data);digest=hashlib.sha256(data).hexdigest()
        assert digest==asset['sha256']
        if name in known:
            assert known[name]['sha256']==digest;continue
        if valid_url(world['npcs'][name].get('portraitUrl')) and name!='Shōen Kagetsuna':
            report['rows'].append({'name':name,'status':'preserved_existing'});continue
        if args.limit and attempts>=args.limit:break
        row={'name':name,'file':str(p),'sha256':digest,'mimeType':mime,'width':width,'height':height,'bytes':len(data),'target':'NPC_PORTRAIT'}
        if args.apply:
            attempts+=1
            try:
                url,status=upload(client,'0kL8UR7rgsu2',row,state,lambda:write_json(statepath,state),constraints,'NPC_PORTRAIT')
                receipt={'name':name,'target':'NPC_PORTRAIT','url':url,'sha256':digest,'file':asset['target']}
                receipts.append(receipt);known[name]=receipt;write_json(ledger,receipts)
                row.update(status=status,url=url)
            except Exception as e:row.update(status='failed',error=str(e));failed=True
        else:row['status']='planned'
        report['rows'].append(row);write_json(HERE/'supporting-upload-report.json',report)
        print(json.dumps({'name':name,'status':row['status']},ensure_ascii=False),flush=True)
    print(json.dumps({'hosted':len(receipts),'generated':len(assets),'expected':len(briefs)+1,'explicitMajorReplacement':'Shōen Kagetsuna','studioSaved':False}))
    if failed:raise SystemExit(1)

if __name__=='__main__':main()
