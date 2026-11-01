"""Official Creator API portrait uploader. Dry-run by default; never saves/publishes Studio."""
import argparse,copy,datetime as dt,hashlib,json,os,pathlib,struct,time,unicodedata,urllib.error,urllib.parse,urllib.request,uuid

class ApiError(Exception):
 def __init__(self,status,code,request_id=None,retry_after=None):
  self.status,self.code,self.request_id,self.retry_after=status,code,request_id,retry_after
  super().__init__(f'HTTP {status}; {code}; requestId={request_id or "unknown"}')

class NoRedirect(urllib.request.HTTPRedirectHandler):
 def redirect_request(self,*args,**kwargs):return None

def write_json(path,value):
 path=pathlib.Path(path);path.parent.mkdir(parents=True,exist_ok=True)
 temp=path.with_name(path.name+'.tmp');temp.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');os.replace(temp,path)

def image_info(data):
 if data[:8]==b'\x89PNG\r\n\x1a\n' and data[12:16]==b'IHDR':return ('image/png',*struct.unpack('>II',data[16:24]))
 if data[:2]==b'\xff\xd8':
  i=2
  while i<len(data):
   if data[i]!=255:i+=1;continue
   while i<len(data) and data[i]==255:i+=1
   marker=data[i];i+=1
   if marker in [0xd8,0xd9] or 0xd0<=marker<=0xd7:continue
   length=struct.unpack('>H',data[i:i+2])[0]
   if marker in [0xc0,0xc1,0xc2,0xc3,0xc5,0xc6,0xc7,0xc9,0xca,0xcb,0xcd,0xce,0xcf]:
    h,w=struct.unpack('>HH',data[i+3:i+7]);return ('image/jpeg',w,h)
   i+=length
 raise ValueError('Unsupported or malformed image; use a valid PNG or JPEG.')

def valid_url(url):
 try:p=urllib.parse.urlsplit(url);return p.scheme=='https' and bool(p.hostname) and not p.username and not p.password
 except (ValueError,TypeError):return False

class Client:
 def __init__(self,base,key=None):
  self.base=base.rstrip('/');p=urllib.parse.urlsplit(self.base)
  if p.scheme!='https' or p.hostname not in {'api.aidungeon.com','api-alpha.aidungeon.com','api-beta.aidungeon.com'} or p.path!='/creator/v1':raise ValueError('Use an explicitly selected official Creator API host and /creator/v1.')
  self.key=key;self.opener=urllib.request.build_opener(NoRedirect())
 def request(self,method,path,body=None,idempotency=None,authenticated=True,raw=None,mime=None):
  url=self.base+path if path.startswith('/') else path
  headers={};payload=raw
  if authenticated:
   if not url.startswith(self.base+'/'):raise ValueError('Refusing to attach the API key to a non-API URL.')
   if not self.key:raise ValueError('Set VOYAGE_CREATOR_API_KEY in the process environment.')
   headers['Authorization']='Bearer '+self.key
  if body is not None:payload=json.dumps(body,ensure_ascii=False).encode();headers['Content-Type']='application/json'
  if mime:headers['Content-Type']=mime
  if idempotency:headers['Idempotency-Key']=idempotency
  if not valid_url(url):raise ValueError('Only HTTPS upload URLs are accepted.')
  for attempt in range(3):
   try:
    with self.opener.open(urllib.request.Request(url,data=payload,headers=headers,method=method),timeout=90) as r:
     data=r.read();return json.loads(data) if 'json' in r.headers.get('Content-Type','') else data
   except urllib.error.HTTPError as e:
    try:obj=json.loads(e.read());code=obj.get('error',{}).get('code','http_error');rid=obj.get('requestId')
    except (ValueError,TypeError):code='http_error';rid=None
    retry=e.headers.get('Retry-After');delay=float(retry) if retry and retry.isdecimal() else 2**attempt
    if attempt<2 and e.code in [408,429,500,502,503,504] and delay<=25:time.sleep(delay);continue
    raise ApiError(e.code,code,rid,retry) from None
   except (urllib.error.URLError,TimeoutError):
    if attempt<2:time.sleep(2**attempt);continue
    raise ApiError(0,'network_failure') from None
 def contract(self):
  o=self.request('GET','/openapi.json',authenticated=False)
  if '/uploads' not in o['paths'] or '/worlds/{shortId}/uploads/{uploadId}/moderate' not in o['paths']:raise ValueError('Live API no longer exposes the reviewed upload flow.')
  if 'NPC_PORTRAIT' not in o['x-media-constraints']['targets']:raise ValueError('Live contract has no NPC_PORTRAIT target.')
  return o

def plan(world,folder,selection=None,replace_selected=False):
 if replace_selected and selection is None:raise ValueError('Replacing existing portraits requires an explicit --select list.')
 canonical={unicodedata.normalize('NFC',k):k for k in world['npcs']};groups={};rows=[]
 if len(canonical)!=len(world['npcs']):raise ValueError('Canonical NPC keys collide after Unicode normalization; resolve them before matching files.')
 for p in sorted(pathlib.Path(folder).rglob('*')):
  if p.suffix.lower() not in {'.png','.jpg','.jpeg'}:continue
  groups.setdefault(unicodedata.normalize('NFC',p.stem).casefold(),[]).append(p)
 for paths in groups.values():
  if len(paths)>1:
   rows.append({'status':'duplicate_filename','files':[str(p) for p in paths]});continue
  p=paths[0];name=canonical.get(unicodedata.normalize('NFC',p.stem))
  if not name:rows.append({'status':'missing_npc','file':str(p)});continue
  if selection is not None and name not in selection:continue
  old=world['npcs'][name].get('portraitUrl');row={'name':name,'file':str(p),'oldUrl':old}
  if valid_url(old) and not replace_selected:row['status']='preserved_existing';rows.append(row);continue
  try:
   b=p.read_bytes();mime,width,height=image_info(b)
   row.update(status='planned',sha256=hashlib.sha256(b).hexdigest(),mimeType=mime,width=width,height=height,bytes=len(b))
  except (ValueError,IndexError,struct.error) as e:row.update(status='invalid_image',error=str(e))
  rows.append(row)
 if selection is not None:
  found={r.get('name') for r in rows}
  for name in sorted(selection-found):rows.append({'name':name,'status':'missing_selected_file' if name in world['npcs'] else 'missing_npc'})
 return rows

def upload(client,short_id,row,state,save,constraints):
 b=pathlib.Path(row['file']).read_bytes()
 if hashlib.sha256(b).hexdigest()!=row['sha256']:raise ValueError('File changed after planning; refusing mismatched upload.')
 if row['bytes']>constraints['maxFileSizeBytes']:raise ValueError('Image exceeds live upload byte limit.')
 target=constraints['targets']['NPC_PORTRAIT']
 if row['width']<target['minimumWidth'] or row['height']<target['minimumHeight']:raise ValueError('Image is smaller than the live NPC portrait minimum.')
 identity='|'.join([client.base,short_id,'NPC_PORTRAIT',row['name'],row['sha256']]);rid=hashlib.sha256(identity.encode()).hexdigest()
 record=state.setdefault('uploads',{}).setdefault(rid,{'name':row['name'],'sha256':row['sha256'],'target':'NPC_PORTRAIT','allowanceKey':str(uuid.uuid4()),'moderateKey':str(uuid.uuid4()),'stage':'new'})
 if record.get('imageUrl'):return record['imageUrl'],'resumed'
 if record.get('stage')=='rejected':raise ValueError('This exact image was rejected; correct the image before requesting another allowance.')
 if record.get('expiresAt') and record['stage']!='bytes_uploaded':
  expiry=dt.datetime.fromisoformat(record['expiresAt'].replace('Z','+00:00'))
  if expiry<=dt.datetime.now(dt.timezone.utc):record.update(stage='new',allowanceKey=str(uuid.uuid4()),moderateKey=str(uuid.uuid4()))
 save()
 if record['stage']!='bytes_uploaded':
  allowance=client.request('POST','/uploads',body={'target':'NPC_PORTRAIT','mimeType':row['mimeType'],'width':row['width'],'height':row['height']},idempotency=record['allowanceKey'])['data']
  record.update(uploadId=allowance['uploadId'],expiresAt=allowance.get('expiresAt'),stage='allowance');save()
  # The signed URL and API key are deliberately absent from the persisted ledger/log.
  client.request('PUT',allowance['directUploadUrl'],raw=b,mime=row['mimeType'],authenticated=False)
  record['stage']='bytes_uploaded';save()
 try:
  result=client.request('POST','/worlds/'+urllib.parse.quote(short_id,safe='')+'/uploads/'+urllib.parse.quote(record['uploadId'],safe='')+'/moderate',body={'target':'NPC_PORTRAIT'},idempotency=record['moderateKey'])['data']
 except ApiError as e:
  if e.code=='studio_media_failed':record['stage']='rejected';save()
  raise
 if result.get('success') is not True or not valid_url(result.get('imageUrl')):raise ValueError('Moderation did not return a successful hosted HTTPS URL.')
 record.update(stage='moderated',imageUrl=result['imageUrl']);save();return record['imageUrl'],'uploaded'

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--world',type=pathlib.Path,default=pathlib.Path('world-draft/WorldAlpha - World.json'));p.add_argument('--images',type=pathlib.Path,default=pathlib.Path('world-draft/npc portraits'));p.add_argument('--select',type=pathlib.Path);p.add_argument('--replace-selected',action='store_true');p.add_argument('--short-id',required=True);p.add_argument('--api-base',default='https://api.aidungeon.com/creator/v1');p.add_argument('--apply',action='store_true');p.add_argument('--remote-validate',action='store_true');p.add_argument('--output',type=pathlib.Path);p.add_argument('--state',type=pathlib.Path,default=pathlib.Path('tmp/creator-api/upload-state.json'));p.add_argument('--report',type=pathlib.Path,default=pathlib.Path('output/portrait-upload-report.json'));p.add_argument('--limit',type=int);a=p.parse_args()
 original=a.world.read_bytes();world=json.loads(original.decode('utf-8-sig'));before=copy.deepcopy(world);selection=None
 if a.select:
  selection=json.loads(a.select.read_text(encoding='utf-8-sig'));selection=set(selection.get('npcs',[]) if isinstance(selection,dict) else selection)
 rows=plan(world,a.images,selection,a.replace_selected);client=Client(a.api_base,os.environ.get('VOYAGE_CREATOR_API_KEY'));contract=client.contract();constraints=contract['x-media-constraints']
 state=json.loads(a.state.read_text(encoding='utf-8')) if a.state.exists() else {};save=lambda:write_json(a.state,state)
 report={'mode':'apply' if a.apply else 'dry-run','apiBase':a.api_base,'worldShortId':a.short_id,'contractSHA256':hashlib.sha256(json.dumps(contract,sort_keys=True).encode()).hexdigest(),'rows':rows,'diff':[]};attempts=0;failed=False
 for row in rows:
  if row['status']!='planned':continue
  if row['bytes']>constraints['maxFileSizeBytes'] or min(row['width'],row['height'])<600:row['status']='invalid_image';failed=True;continue
  if not a.apply:continue
  if a.limit and attempts>=a.limit:row['status']='deferred';continue
  attempts+=1
  try:
   url,status=upload(client,a.short_id,row,state,save,constraints);row.update(status=status,newUrl=url);world['npcs'][row['name']]['portraitUrl']=url
   report['diff'].append({'path':['npcs',row['name'],'portraitUrl'],'before':row['oldUrl'],'after':url,'fileSHA256':row['sha256']});print(json.dumps({'name':row['name'],'status':status},ensure_ascii=False),flush=True)
  except (ApiError,ValueError) as e:
   row.update(status='failed',error=str(e));failed=True;print(json.dumps({'name':row['name'],'status':'failed','error':str(e)},ensure_ascii=False),flush=True)
   if isinstance(e,ApiError) and e.status in [401,403,429]:break
  finally:write_json(a.report,report)
 # Verify that the uploader changed no field except the selected portrait URLs.
 probe=copy.deepcopy(world)
 for diff in report['diff']:
  n=diff['path'][1]
  if 'portraitUrl' in before['npcs'][n]:probe['npcs'][n]['portraitUrl']=before['npcs'][n]['portraitUrl']
  else:probe['npcs'][n].pop('portraitUrl',None)
 assert probe==before,'Unexpected non-portrait mutation.'
 if a.apply:
  if a.world.read_bytes()!=original:raise ValueError('Source world changed during upload. Receipts are saved; rerun against the current world to merge URLs safely.')
  from project import validate
  validate(world)
  if a.remote_validate:
   rv=client.request('POST','/validate',body={'world':{'initialGameState':world},'stage':'draft'});report['remoteValidation']=rv;write_json(a.report,report)
   if not rv['data']['valid']:raise ValueError('Official draft validation failed; receipts/report retained, source world unchanged.')
  write_json(a.output or a.world,world)
 report['summary']={s:sum(r['status']==s for r in rows) for s in sorted({r['status'] for r in rows})};write_json(a.report,report)
 md=['# Portrait URL changes','',f'World: `{a.short_id}`. Uploaded artwork only; Studio was not saved or published.','']
 for d in report['diff']:md.extend([f'- **{d["path"][1]}**',f'  - Before: {d["before"] or "empty"}',f'  - After: {d["after"]}'])
 a.report.with_suffix('.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
 print(json.dumps({'summary':report['summary'],'report':str(a.report),'output':str(a.output or a.world) if a.apply else None},ensure_ascii=False))
 if failed:raise SystemExit(1)

if __name__=='__main__':
 try:main()
 except (ValueError,ApiError) as e:raise SystemExit(str(e))
