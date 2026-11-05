"""One sequential resumable uploader; no key or signed URL in persisted data."""
import hashlib,json,os,sys,time
from pathlib import Path
import update
sys.path.insert(0,str(update.ROOT/'tools'))
from voyage_portraits import Client,ApiError,upload,image_info

def main():
 c=Client('https://api-alpha.aidungeon.com/creator/v1',os.environ.get('VOYAGE_CREATOR_API_KEY'))
 contract=c.contract();constraints=contract['x-media-constraints']
 statefile=update.ROOT/'tmp/ardelis-followup/upload-state.json'
 state=update.load(statefile) if statefile.exists() else {}
 save=lambda:update.write(statefile,state)
 attempted=set();failed=[]
 while True:
  try:ledger=update.load(update.HERE/'portrait-files.json')
  except json.JSONDecodeError:time.sleep(2);continue
  report=update.load(update.HERE/'upload-receipts.json');urls=update.load(update.HERE/'portrait-urls.json')
  for name,e in ledger.items():
   identity='NPC_PORTRAIT::'+name
   raw=(update.ROOT/e['file']).read_bytes();sha=hashlib.sha256(raw).hexdigest();assert sha==e['sha256']
   attempt=(name,sha)
   if attempt in attempted or (report.get(identity,{}).get('imageUrl') and report[identity].get('sha256')==sha):continue
   attempted.add(attempt)
   mime,width,height=image_info(raw)
   row=dict(name=name,file=str(update.ROOT/e['file']),sha256=sha,mimeType=mime,width=width,height=height,bytes=len(raw))
   try:
    url,status=upload(c,'0kL8UR7rgsu2',row,state,save,constraints,'NPC_PORTRAIT')
    report[identity]=dict(name=name,address=name,target='NPC_PORTRAIT',sha256=sha,imageUrl=url,status=status,width=width,height=height)
    urls[name]=url;update.write(update.HERE/'portrait-urls.json',urls)
    print(json.dumps({'name':name,'status':status},ensure_ascii=False),flush=True)
   except (ApiError,ValueError) as exc:
    failed.append(name);report[identity]=dict(name=name,target='NPC_PORTRAIT',sha256=sha,status='failed',error=str(exc))
    print(json.dumps({'name':name,'status':'failed','error':str(exc)},ensure_ascii=False),flush=True)
   update.write(update.HERE/'upload-receipts.json',report)
  if '--once' in sys.argv or len(ledger)==116:
   print(json.dumps({'complete':len(ledger)==116 and not failed,'selectedUploadsComplete':not failed,'portraits':len(ledger),'failed':failed}),flush=True)
   return 1 if failed else 0
  time.sleep(15)

if __name__=='__main__':raise SystemExit(main())
