"""Resume exact-name official uploads; only local URL receipts are changed."""
import argparse,hashlib,json,os,pathlib,sys
HERE=pathlib.Path(__file__).resolve().parent;ROOT=HERE.parents[1]
sys.path.insert(0,str(ROOT/'tools'))
from voyage_portraits import Client,ApiError,upload,image_info,write_json

def main():
 ap=argparse.ArgumentParser();ap.add_argument('kind',choices=['portraits','locations']);ap.add_argument('--limit',type=int,default=200);a=ap.parse_args()
 c=Client('https://api-alpha.aidungeon.com/creator/v1',os.environ.get('VOYAGE_CREATOR_API_KEY'));contract=c.contract();constraints=contract['x-media-constraints']
 ledgerpath=HERE/('portrait-files.json' if a.kind=='portraits' else 'location-files.json');ledger=json.loads(ledgerpath.read_text(encoding='utf-8')) if ledgerpath.exists() else {}
 statepath=ROOT/'tmp/ardelis/upload-state.json';state=json.loads(statepath.read_text(encoding='utf-8')) if statepath.exists() else {};save=lambda:write_json(statepath,state)
 candidate=json.loads((ROOT/'output/ardelis-2026-11-05/The Schools of Magic, Arise! - Ardelis.json').read_text(encoding='utf-8'))
 reportpath=HERE/'upload-receipts.json';report=json.loads(reportpath.read_text(encoding='utf-8')) if reportpath.exists() else {};count=0;failed=0
 for key,entry in ledger.items():
  name=key if a.kind=='portraits' else entry['name'];target='NPC_PORTRAIT' if a.kind=='portraits' else entry['target'];file=ROOT/entry['file'];raw=file.read_bytes();sha=hashlib.sha256(raw).hexdigest();assert sha==entry['sha256']
  address=name if a.kind=='portraits' or entry['kind']=='location' else entry['location']+'::'+entry['area']
  identity=target+'::'+address
  if report.get(identity,{}).get('sha256')==sha and report[identity].get('imageUrl'):continue
  if a.kind=='portraits':assert name in candidate['npcs']
  elif entry['kind']=='location':assert name in candidate['locations']
  else:assert entry['area'] in candidate['locations'][entry['location']]['areas']
  if count>=a.limit:break
  count+=1;mime,width,height=image_info(raw);row=dict(name=address,file=str(file),sha256=sha,mimeType=mime,width=width,height=height,bytes=len(raw))
  try:
   url,status=upload(c,'0kL8UR7rgsu2',row,state,save,constraints,target)
   report[identity]=dict(name=name,address=address,target=target,sha256=sha,imageUrl=url,status=status,width=width,height=height)
   dest=HERE/('portrait-urls.json' if a.kind=='portraits' else 'location-urls.json' if entry['kind']=='location' else 'area-urls.json')
   urls=json.loads(dest.read_text(encoding='utf-8')) if dest.exists() else {};urls[address]=url;write_json(dest,urls);write_json(reportpath,report)
   print(json.dumps({'name':name,'status':status},ensure_ascii=False),flush=True)
  except (ApiError,ValueError) as e:
   failed+=1;report[identity]=dict(name=name,address=address,target=target,sha256=sha,status='failed',error=str(e));write_json(reportpath,report)
   print(json.dumps({'name':name,'status':'failed','error':str(e)},ensure_ascii=False),flush=True)
 print(json.dumps({'attempted':count,'failed':failed,'receiptEntries':len(report)}))
 if failed:sys.exit(1)
if __name__=='__main__':main()
