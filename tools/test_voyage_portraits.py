"""Portable uploader tests. Uses a fake API, never network or live credentials."""
import copy,json,pathlib,struct,tempfile,unittest
from voyage_portraits import plan,upload,image_info,ApiError,Client

class Fake:
 base='https://api-alpha.aidungeon.com/creator/v1'
 def __init__(self,fail=False):self.calls=[];self.fail=fail
 def request(self,method,path,**kw):
  self.calls.append((method,path,copy.deepcopy(kw)))
  if path=='/uploads':return {'data':{'uploadId':'abc','directUploadUrl':'https://uploads.example.test/signed','expiresAt':None}}
  if method=='PUT':return b''
  if self.fail:raise ApiError(503,'studio_unavailable')
  return {'data':{'success':True,'imageUrl':'https://images.aidungeon.com/test.png'}}

class PortraitTests(unittest.TestCase):
 def setUp(self):
  self.temp=tempfile.TemporaryDirectory();self.root=pathlib.Path(self.temp.name)
  self.png=b'\x89PNG\r\n\x1a\n'+struct.pack('>I',13)+b'IHDR'+struct.pack('>II',1024,1536)+b'\x08\x06\x00\x00\x00'
  (self.root/'Kōta Mibu.png').write_bytes(self.png)
  self.world={'npcs':{'Kōta Mibu':{'name':'Kōta Mibu','portraitUrl':'https://images.aidungeon.com/old.png','level':1}}}
  self.constraints={'maxFileSizeBytes':5242880,'targets':{'NPC_PORTRAIT':{'minimumWidth':600,'minimumHeight':600}}}
 def tearDown(self):self.temp.cleanup()
 def row(self):return plan(self.world,self.root,{'Kōta Mibu'},True)[0]
 def test_default_preserves(self):self.assertEqual(plan(self.world,self.root)[0]['status'],'preserved_existing')
 def test_explicit_replace(self):self.assertEqual(self.row()['status'],'planned');self.assertEqual(self.row()['width'],1024)
 def test_no_global_replace(self):
  with self.assertRaises(ValueError):plan(self.world,self.root,None,True)
 def test_duplicate_is_not_guessed(self):
  (self.root/'Kōta Mibu.jpg').write_bytes(self.png)
  self.assertEqual(plan(self.world,self.root)[0]['status'],'duplicate_filename')
 def test_unknown_name(self):
  (self.root/'Unknown.png').write_bytes(self.png)
  self.assertIn('missing_npc',[r['status'] for r in plan(self.world,self.root)])
 def test_utf8_name(self):self.assertEqual(self.row()['name'],'Kōta Mibu')
 def test_canonical_unicode_collision(self):
  self.world['npcs']['Ko\u0304ta Mibu']={'name':'Ko\u0304ta Mibu'}
  with self.assertRaises(ValueError):plan(self.world,self.root)
 def test_jpeg(self):
  jpg=b'\xff\xd8\xff\xc0'+struct.pack('>H',17)+b'\x08'+struct.pack('>HH',1200,896)+b'\x03'+b'\x00'*9
  self.assertEqual(image_info(jpg),('image/jpeg',896,1200))
 def test_exact_flow_and_resume(self):
  f=Fake();s={};row=self.row();url,status=upload(f,'world',row,s,lambda:None,self.constraints)
  self.assertEqual(status,'uploaded');self.assertEqual(len(f.calls),3)
  self.assertEqual(f.calls[0][2]['body'],{'target':'NPC_PORTRAIT','mimeType':'image/png','width':1024,'height':1536})
  self.assertFalse(f.calls[1][2]['authenticated']);self.assertNotIn('idempotency',f.calls[1][2])
  self.assertTrue(f.calls[0][2]['idempotency']);self.assertTrue(f.calls[2][2]['idempotency'])
  self.assertNotIn('directUploadUrl',json.dumps(s))
  self.assertEqual(upload(f,'world',row,s,lambda:None,self.constraints),(url,'resumed'));self.assertEqual(len(f.calls),3)
 def test_partial_retry_reuses_moderation(self):
  f=Fake(True);s={};row=self.row()
  with self.assertRaises(ApiError):upload(f,'world',row,s,lambda:None,self.constraints)
  key=f.calls[-1][2]['idempotency'];g=Fake();upload(g,'world',row,s,lambda:None,self.constraints)
  self.assertEqual(len(g.calls),1);self.assertEqual(g.calls[0][2]['idempotency'],key)
 def test_changed_file_blocked(self):
  row=self.row();(self.root/'Kōta Mibu.png').write_bytes(self.png+b'changed')
  with self.assertRaises(ValueError):upload(Fake(),'world',row,{},lambda:None,self.constraints)
 def test_unofficial_api_rejected(self):
  with self.assertRaises(ValueError):Client('https://example.test/creator/v1','unused')

if __name__=='__main__':unittest.main()
