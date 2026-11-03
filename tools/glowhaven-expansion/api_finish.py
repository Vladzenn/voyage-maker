"""Upload the selected state portrait or validate a local draft; never save Studio."""
import argparse,getpass,hashlib,json,os,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'tools'))
from voyage_portraits import Client,upload,image_info,write_json

def main():
    p=argparse.ArgumentParser();p.add_argument('command',choices=['upload-state','validate']);a=p.parse_args()
    key=os.environ.get('VOYAGE_CREATOR_API_KEY') or getpass.getpass('Creator key: ')
    if not key:raise ValueError('No key received; no request made')
    c=Client('https://api-alpha.aidungeon.com/creator/v1',key);del key
    contract=c.contract()
    if a.command=='upload-state':
        r=json.loads((HERE/'generated/Nerathyl - Awake.json').read_text(encoding='utf-8'))
        file=ROOT/r['file'];data=file.read_bytes();assert hashlib.sha256(data).hexdigest()==r['sha256']
        mime,width,height=image_info(data)
        statepath=ROOT/'tmp/creator-api/glowhaven-serpent-state-upload.json'
        state=json.loads(statepath.read_text()) if statepath.exists() else {}
        row={'name':'Nerathyl / Awake','file':str(file),'sha256':r['sha256'],'mimeType':mime,'width':width,'height':height,'bytes':len(data)}
        url,status=upload(c,'0kL8UR7rgsu2',row,state,lambda:write_json(statepath,state),contract['x-media-constraints'],'NPC_PORTRAIT')
        write_json(HERE/'hosted-serpent-state.json',{'name':'Nerathyl','state':'Awake','file':r['file'],'sha256':r['sha256'],'target':'NPC_PORTRAIT','url':url})
        print(json.dumps({'state':'Awake','status':status,'studioSaved':False}))
    else:
        world=json.loads((ROOT/'world-draft/WorldAlpha - World.json').read_text(encoding='utf-8-sig'))
        result=c.request('POST','/validate',body={'world':{'initialGameState':world},'stage':'draft'})
        write_json(HERE/'official-draft-validation.json',{'worldFile':'world-draft/WorldAlpha - World.json','worldFileSha256':hashlib.sha256((ROOT/'world-draft/WorldAlpha - World.json').read_bytes()).hexdigest(),'result':result,'studioSaved':False,'studioPublished':False})
        print(json.dumps(result,ensure_ascii=False))
if __name__=='__main__':main()
