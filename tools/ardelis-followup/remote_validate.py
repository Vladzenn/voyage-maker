"""Validate exact current bytes against the live official draft contract; no Studio writes."""
import datetime
import hashlib
import json
import os
import sys
import update
sys.path.insert(0,str(update.ROOT/'tools'))
from voyage_portraits import Client,ApiError


def main():
    client=Client('https://api-alpha.aidungeon.com/creator/v1',os.environ.get('VOYAGE_CREATOR_API_KEY'))
    contract=client.contract()
    raw=update.WORLD.read_bytes();world=json.loads(raw)
    try:
        result=client.request('POST','/validate',body={'world':{'initialGameState':world},'stage':'draft'})
        report=dict(at=datetime.datetime.now(datetime.timezone.utc).isoformat(),worldSHA256=hashlib.sha256(raw).hexdigest(),
          contractSHA256=hashlib.sha256(json.dumps(contract,sort_keys=True).encode()).hexdigest(),result=result)
        update.write(update.HERE/'official-validation.json',report)
        data=result.get('data',{})
        print(json.dumps({'valid':data.get('valid'),'errors':data.get('errors',[]),'warnings':data.get('warnings',[]),'requestId':result.get('requestId')},ensure_ascii=False)[:14000])
        return 0 if data.get('valid') and not data.get('errors') else 2
    except ApiError as exc:
        print(json.dumps({'status':'failed','httpStatus':exc.status,'code':exc.code,'requestId':exc.request_id}));return 1


if __name__=='__main__':raise SystemExit(main())
