"""Validate the candidate through the existing official API without saving Studio."""
import hashlib
import json
import os
import pathlib
import sys

HERE=pathlib.Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent))
from voyage_portraits import Client

candidate=HERE.parents[1]/'output/rebirth-2026-11-05/The Schools of Magic, Arise! - Rebirth.json'
raw=candidate.read_bytes()
client=Client('https://api-alpha.aidungeon.com/creator/v1',os.environ.get('VOYAGE_CREATOR_API_KEY'))
result=client.request('POST','/validate',body={'world':{'initialGameState':json.loads(raw.decode('utf-8'))},'stage':'draft'})
record={'candidateSHA256':hashlib.sha256(raw).hexdigest(),'stage':'draft','result':result,'savedToStudio':False,'publishedToStudio':False,'livePlaytest':False}
(HERE/'official-validation.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
data=result['data']
print(json.dumps({'valid':data.get('valid'),'errors':data.get('errors'),'warnings':data.get('warnings')},ensure_ascii=False))
if not data.get('valid') or data.get('errors') or data.get('warnings'):
    raise SystemExit(1)
