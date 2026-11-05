import pathlib,json,csv,hashlib,math,shutil
from PIL import Image,ImageDraw,ImageFont
ROOT=pathlib.Path('R:/VoyageMaker'); WORK=ROOT/'tools/drakenspire-map-2026-11-05'; ART=ROOT/'world-draft/maps/Drakenspire Highlands 2026-11-05'
data=json.loads((WORK/'canonical-descriptions.json').read_text(encoding='utf-8'))
points=json.loads((WORK/'pin-input.json').read_text(encoding='utf-8'))
src=ART/'Drakenspire - High Stone City and Highlands.png'
im=Image.open(src).convert('RGB'); iw,ih=im.size
assert len(points)==len(data['locations'])==59
width,height=3420,1920
out=Image.new('RGB',(width,height),'#edf1f4'); d=ImageDraw.Draw(out)
def font(n,bold=False): return ImageFont.truetype('C:/Windows/Fonts/'+('segoeuib.ttf' if bold else 'segoeui.ttf'),n)
title=font(46,True); sub=font(25); leg=font(23); head=font(28,True); small=font(22); num=font(21,True)
d.text((36,24),'DRAKENSPIRE  /  LANDMARK LOCATOR',font=title,fill='#20394d')
d.text((36,88),'59 canonical locations - proposed visual placements on the new map',font=sub,fill='#4c6375')
box=(36,166); mw,mh=2304,1536
out.paste(im.resize((mw,mh),Image.Resampling.LANCZOS),box)
d=ImageDraw.Draw(out)
for y in (154,1717): d.line((36,y,2340,y),fill='#bac7d0',width=2)
scale=mw/iw
markers=[]
for i,((name,loc),point) in enumerate(zip(data['locations'].items(),points),1):
 x,y,note=point; ax=box[0]+x*scale; ay=box[1]+y*scale
 color='#84533b' if 6<=i<=14 else '#215e7b' if i<=40 else '#3d6b5b'
 if not loc.get('initialKnown'): color='#8b4a70'
 markers.append(dict(number=i,name=name,anchorX=ax,anchorY=ay,x=ax,y=ay,color=color,note=note,initialKnown=loc.get('initialKnown'),sourcePixelX=x,sourcePixelY=y))
# Move number disks just enough to avoid collisions; leaders retain exact artwork anchors.
for iteration in range(150):
 moved=0
 for i,a in enumerate(markers):
  for b in markers[i+1:]:
   dx=b['x']-a['x']; dy=b['y']-a['y']; dist=math.hypot(dx,dy); minimum=43
   if dist<minimum:
    if dist<.01: dx,dy,dist=1,0,1
    push=(minimum-dist)*.52
    a['x']-=dx/dist*push; a['y']-=dy/dist*push; b['x']+=dx/dist*push; b['y']+=dy/dist*push; moved+=1
 for a in markers:
  a['x']=max(box[0]+22,min(box[0]+mw-22,a['x'])); a['y']=max(box[1]+22,min(box[1]+mh-22,a['y']))
 if not moved: break
for a in markers:
 if math.hypot(a['x']-a['anchorX'],a['y']-a['anchorY'])>4:
  d.line((a['anchorX'],a['anchorY'],a['x'],a['y']),fill='white',width=5)
  d.line((a['anchorX'],a['anchorY'],a['x'],a['y']),fill=a['color'],width=2)
  r=4; d.ellipse((a['anchorX']-r,a['anchorY']-r,a['anchorX']+r,a['anchorY']+r),fill=a['color'],outline='white',width=1)
for a in markers:
 x,y=a['x'],a['y']; r=19
 d.ellipse((x-r,y-r,x+r,y+r),fill=a['color'],outline='white',width=3)
 s=f"{a['number']:02d}"; bb=d.textbbox((0,0),s,font=num); tw=bb[2]-bb[0]; th=bb[3]-bb[1]
 d.text((x-tw/2,y-th/2-bb[1]-1),s,font=num,fill='white')
lx=2383
d.text((lx,163),'EXACT-NAME KEY',font=head,fill='#20394d')
d.text((lx,210),'* Initially unknown site',font=small,fill='#8b4a70')
def wrap(text,f,maxw):
 words=text.split(); rows=[]; row=''
 for w in words:
  test=(row+' '+w).strip()
  if row and d.textlength(test,font=f)>maxw: rows.append(row); row=w
  else: row=test
 if row: rows.append(row)
 return rows
for a in markers:
 col=0 if a['number']<=30 else 1; row=a['number']-1 if col==0 else a['number']-31
 x=lx+col*510; y=264+row*49
 d.rounded_rectangle((x,y+2,x+36,y+34),radius=8,fill=a['color'])
 n=f"{a['number']:02d}"; d.text((x+5,y+4),n,font=font(19,True),fill='white')
 text=a['name']+(' *' if not a['initialKnown'] else '')
 for j,line in enumerate(wrap(text,leg,454)):
  d.text((x+47,y-3+j*24),line,font=leg,fill='#20394d')
d.text((36,1762),'The map uses a new perspective. Markers refer to this artwork; original JSON coordinates were not used.',font=small,fill='#3c566a')
d.text((36,1802),'Small shops may share blocks. Minor-building and remote-terrain anchors are proposals, not verified game placements.',font=small,fill='#3c566a')
d.text((36,1842),'Author reference includes the four initially unknown sites. World data and hosted map remain unchanged.',font=small,fill='#3c566a')
locator=ART/'Drakenspire - Landmark Locator.png'
out.save(locator,optimize=True)
records=[]
for a in markers:
 records.append({'number':a['number'],'name':a['name'],'xPercent':round(a['sourcePixelX']/iw*100,5),'yPercent':round(a['sourcePixelY']/ih*100,5),'initialKnown':a['initialKnown'],'interpretation':a['note'],'status':'proposed placement; not applied'})
placement={'map':str(src.relative_to(ROOT)).replace('\\','/'),'coordinateConvention':'Image-relative percentages from top-left; not Voyage world coordinates','sourceWidth':iw,'sourceHeight':ih,'locations':records}
(WORK/'suggested-placements.json').write_text(json.dumps(placement,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with (WORK/'suggested-placements.csv').open('w',newline='',encoding='utf-8-sig') as f:
 writer=csv.DictWriter(f,fieldnames=list(records[0])); writer.writeheader(); writer.writerows(records)
prompts=json.loads((WORK/'brief-input.json').read_text(encoding='utf-8-sig'))
(WORK/'Standalone Prompt.txt').write_text(prompts['cleanMapPrompt']+'\n',encoding='utf-8')
manifest={'date':'2026-11-05','status':'fresh art proposal for review; not installed or accepted as final canon','canonicalSource':data['source'],'canonicalSourceSha256':data['sha256'],'locations':59,'areas':251,'worldModified':False,'skillDeletion':'build-voyage-maps removed at author request; no longer applied','tool':'built-in image_gen','artReferences':prompts['references'],'selectedGeneratedSource':prompts['latestGeneratedSource'],'promptFile':'tools/drakenspire-map-2026-11-05/brief-input.json','mapNotes':'New fortress-left viewpoint; denser high-elevation stone town above nearby wilderness. Regional scene scale is visual, not a surveyed distance.','locatorNotes':'Deterministic numbered overlay of the exact clean map. All 59 anchors are proposed; no canonical coordinates changed.','files':[]}
for p in [src,locator,ROOT/'world-draft/authoring/plans/Drakenspire - Standalone Fresh Map Prompt.pdf']:
 b=p.read_bytes(); row={'path':str(p.relative_to(ROOT)).replace('\\','/'),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)}
 if p.suffix.lower()=='.png': row['dimensions']=list(Image.open(p).size)
 manifest['files'].append(row)
(WORK/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'mapSize':[iw,ih],'locatorSize':[width,height],'pins':len(records),'map':str(src),'locator':str(locator)},indent=2))

