"""Resume only this approved new cast, with credentials supplied through stdin.

Never saves/publishes a Studio world. The secret is process-only, not a CLI
argument, environment export, receipt field or source file. This can watch for
the remaining generated files while the one-pass portrait batch is running.
"""
import argparse,getpass,hashlib,json,os,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'tools'))
from voyage_portraits import Client,upload,image_info,write_json,valid_url

def main():
    p=argparse.ArgumentParser();p.add_argument('--watch',action='store_true');p.add_argument('--short-id',default='0kL8UR7rgsu2');a=p.parse_args()
    key=os.environ.get('VOYAGE_CREATOR_API_KEY')
    if not key:
        print('Ready for Creator key on stdin (contents will not be printed).',flush=True)
        key=getpass.getpass('Creator key: ') if sys.stdin.isatty() else sys.stdin.readline().strip()
    if not key:raise ValueError('No key received. Use a terminal session or the process environment; no uploads attempted.')
    client=Client('https://api-alpha.aidungeon.com/creator/v1',key);contract=client.contract();constraints=contract['x-media-constraints']
    del key
    jobs=json.loads((HERE/'portrait-jobs.json').read_text(encoding='utf-8'))
    base=json.loads((ROOT/'output/glowhaven-expansion-2026-11-03/Studio Merge Base.json').read_text(encoding='utf-8-sig'))
    assert len({j['name'] for j in jobs})==len(jobs)
    assert all(j['name'] not in base['npcs'] for j in jobs),'Existing portrait requires explicit replacement'
    statepath=ROOT/'tmp/creator-api/glowhaven-expansion-upload-state.json'
    state=json.loads(statepath.read_text()) if statepath.exists() else {}
    save=lambda:write_json(statepath,state)
    receipts=HERE/'hosted-portraits.json';hosted=json.loads(receipts.read_text(encoding='utf-8')) if receipts.exists() else {}
    report={'apiBase':client.base,'worldShortId':a.short_id,'contractSha256':hashlib.sha256(json.dumps(contract,sort_keys=True).encode()).hexdigest(),'rows':{},'studioSaved':False,'studioPublished':False}
    failures=set();deadline=time.monotonic()+7200
    while True:
        for j in jobs:
            name=j['name'];file=Path(j['destination']);receipt=HERE/'generated'/(name+'.json')
            if name in hosted or name in failures or not receipt.exists():continue
            meta=json.loads(receipt.read_text(encoding='utf-8'));data=file.read_bytes();sha=hashlib.sha256(data).hexdigest()
            assert file.stem==name and meta['name']==name and meta['sha256']==sha,'Name or hash mismatch'
            mime,width,height=image_info(data)
            row={'name':name,'file':str(file),'sha256':sha,'mimeType':mime,'width':width,'height':height,'bytes':len(data)}
            try:
                url,status=upload(client,a.short_id,row,state,save,constraints,'NPC_PORTRAIT')
                hosted[name]={'name':name,'file':str(file.relative_to(ROOT)).replace('\\','/'),'sha256':sha,'target':'NPC_PORTRAIT','url':url}
                write_json(receipts,hosted);report['rows'][name]={'status':status,'sha256':sha,'url':url}
            except Exception as e:
                failures.add(name);report['rows'][name]={'status':'failed','error':str(e),'sha256':sha}
                if getattr(e,'status',None) in [401,403]:raise
            write_json(HERE/'upload-report.json',report)
            print(json.dumps({'name':name,'status':report['rows'][name]['status']},ensure_ascii=False),flush=True)
        if len(hosted)+len(failures)==len(jobs) or not a.watch or time.monotonic()>deadline:break
        time.sleep(10)
    print(json.dumps({'hosted':len(hosted),'failed':len(failures),'expected':len(jobs),'studioSaved':False,'studioPublished':False}),flush=True)
    return 1 if failures else 0
if __name__=='__main__':raise SystemExit(main())
