"""Official read-only draft validation; credentials never enter reports/files."""
import argparse
import getpass
import hashlib
import json
import os
import pathlib
import sys

HERE=pathlib.Path(__file__).resolve().parent
ROOT=HERE.parents[1]
sys.path.insert(0,str(ROOT/'tools'))
from voyage_portraits import Client, ApiError, write_json


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--candidate',type=pathlib.Path,required=True)
    p.add_argument('--key-file',type=pathlib.Path)
    p.add_argument('--key-prompt',action='store_true')
    a=p.parse_args()
    key=os.environ.get('VOYAGE_CREATOR_API_KEY')
    if a.key_file:key=a.key_file.read_text(encoding='utf-8-sig').strip()
    if a.key_prompt:
        if not sys.stdin.isatty():raise SystemExit('A no-echo terminal is required for credential input.')
        key=getpass.getpass('Voyage Creator API key (hidden): ')
    if not key:raise SystemExit('No credential configured; use a process environment variable or an external secret file.')
    raw=a.candidate.read_bytes()
    client=Client('https://api-alpha.aidungeon.com/creator/v1',key)
    try:
        contract=client.request('GET','/openapi.json',authenticated=False)
        if '/validate' not in contract['paths']:raise SystemExit('Official contract no longer contains /validate.')
        result=client.request('POST','/validate',body={'world':{'initialGameState':json.loads(raw)},'stage':'draft'})
    except ApiError as e:
        print(json.dumps({'status':'failed','httpStatus':e.status,'code':e.code,'requestId':e.request_id}))
        return 1
    finally:
        client.key=None;key=None
    record=dict(clientDate='2026-11-06',candidateSHA256=hashlib.sha256(raw).hexdigest(),
        contractVersion=contract.get('info',{}).get('version'),stage='draft',result=result,
        savedToStudio=False,publishedToStudio=False,livePlaytest=False)
    write_json(HERE/'official-validation.json',record)
    data=result.get('data',{})
    print(json.dumps({'valid':data.get('valid'),'errors':data.get('errors',[]),
        'warnings':data.get('warnings',[]),'savedToStudio':False},ensure_ascii=False)[:9000])
    return 0 if data.get('valid') and not data.get('errors') else 2


if __name__=='__main__':raise SystemExit(main())
