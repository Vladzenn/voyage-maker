"""Read the live official contract and validate a draft; never write Studio."""
import datetime,hashlib,json,os,pathlib,sys
ROOT=pathlib.Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'tools'))
from voyage_portraits import Client,ApiError,write_json
c=Client('https://api-alpha.aidungeon.com/creator/v1',os.environ.get('VOYAGE_CREATOR_API_KEY'))
contract=c.contract()
world_path=ROOT/'output/ardelis-2026-11-05/The Schools of Magic, Arise! - Ardelis.json'
raw=world_path.read_bytes();world=json.loads(raw)
try:
 r=c.request('POST','/validate',body={'world':{'initialGameState':world},'stage':'draft'})
 write_json(ROOT/'tools/ardelis/official-validation.json',{'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'worldSHA256':hashlib.sha256(raw).hexdigest(),'contractSHA256':hashlib.sha256(json.dumps(contract,sort_keys=True).encode()).hexdigest(),'result':r})
 d=r.get('data',{});print(json.dumps({'errors':d.get('errors',[]),'warnings':d.get('warnings',[]),'requestId':r.get('requestId')},ensure_ascii=False)[:14000])
 if d.get('errors'):sys.exit(2)
except ApiError as e:
 print(json.dumps({'status':'failed','httpStatus':e.status,'code':e.code,'requestId':e.request_id}));sys.exit(1)
