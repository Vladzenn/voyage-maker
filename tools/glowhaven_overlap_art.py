"""Genuine shared-overlap circular map refinement, checkpointing and delivery."""
import argparse,csv,hashlib,json,pathlib,shutil,zipfile
from PIL import Image,ImageDraw,ImageFont
ROOT=pathlib.Path(__file__).resolve().parents[1]
ART=ROOT/'tools/glowhaven-panel-art'
OUT=ROOT/'output/glowhaven-panels-2026-11-03'
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def write(p,v):
 p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def save(job_id,source):
 j=next(j for j in read(ART/'jobs.json')['jobs'] if j['id']==job_id);source=pathlib.Path(source);target=ROOT/j['file'];digest=hashlib.sha256(source.read_bytes()).hexdigest()
 with Image.open(source) as im:
  size=im.size;assert im.format=='PNG' and size[0]==size[1] and size[0]>=1000
 target.parent.mkdir(parents=True,exist_ok=True)
 if target.exists():assert hashlib.sha256(target.read_bytes()).hexdigest()==digest
 else:shutil.copy2(source,target)
 receipt={k:j.get(k) for k in ['id','set','panel','direction','file','sourceBounds']};receipt.update(source=str(source),dimensions=list(size),sha256=digest,status='generated, awaiting visual review')
 write(ART/'generated'/(job_id+'.json'),receipt);print(json.dumps({'saved':job_id,'dimensions':size}))
def prepare():
 m=read(ART/'jobs.json');assert not m.get('overlapPrepared'),'Already prepared; preserve checkpoints'
 history=[];previous={};archive=OUT/'Provisional - No Overlap';archive.mkdir(parents=True,exist_ok=True)
 for j in m['jobs']:
  receipt=ART/'generated'/(j['id']+'.json')
  if receipt.exists():
   r=read(receipt);old=(ROOT/r['file']).resolve();dest=(archive/(j['id']+' - '+old.name)).resolve()
   assert old.is_relative_to(ROOT) and dest.is_relative_to(ROOT) and not dest.exists()
   shutil.move(str(old),str(dest));r['previousFile']=r['file'];r['file']=dest.relative_to(ROOT).as_posix();r['status']='superseded no-overlap draft' if j['id'].startswith('a') else 'rejected asymmetrical study; cancelled by author'
   previous[j['id']]=r['file'];write(receipt,r)
  history.append(j)
 write(ART/'history-no-overlap.json',{'jobs':history,'note':'Author requested genuine shared overlap and cancelled asymmetrical set. No more asymmetrical generation.'})
 bounds=[(0,0,720,720),(534,0,1254,720),(0,534,720,1254),(534,534,1254,1254)]
 inputs=ROOT/'tmp/glowhaven-panel-art/overlap-inputs';inputs.mkdir(parents=True,exist_ok=True)
 with Image.open(m['sourceMaster']) as im:
  assert im.size==(1254,1254)
  for i,b in enumerate(bounds,1):im.crop(b).save(inputs/f'{i}.png')
 common='''REFINE IMAGE 1 ONLY: an EXTENDED SQUARE MAP QUADRANT WITH SHARED OVERLAP. Image 2 is the full sparse master for context only. Images 3,4,5 are already refined tight-quadrant detail references for the same place and its immediate neighbors. Preserve the FIRST image's larger exact extent, crop, camera, scale, horizon, river and shoreline. Return only its extended quadrant, not the tight crop of references 3-5 and not a complete map.
The first reference is 720 by 720 source pixels. Its inner-facing strips share 186 source pixels (about 26% of the panel) with adjacent extended panels. Fully draw that shared terrain: no transparent margins, blank padding, borders or baked fading. Preserve geometry, wall positions, roofs, roads and water in these strips so the author can align and soft-mask layers. Partial source-edge features remain partial; whole features visible in this expanded reference remain whole. Do not complete/recenter a city from full-map context.
Use the original crisp saturated high-fantasy JRPG painted cartography, coherent miniature architectural planes, natural warm sunlight, jewel-blue water and soft atmospheric distance. Match the refined neighbors' detail, palette and light. Improve definition inside existing footprints, without enlarging buildings or changing distances. Preserve the circular wall and principal radial routes. Keep sparse natural mountains/woods; no new big cave, cabin, ruin, stone circle or icon attractions. No text, labels, grid, symbols, frames or watermark.
'''+m['districtDesign']
 local=[
 'NORTHWEST: RIGHT and BOTTOM 26% are shared. Preserve sky, western mountains, small Greywatch ruin and modest existing hot spring. The expanded crop contains more of the Evertree and central city than the tight input. Preserve exactly what it shows, including the red academy. Refine northern civic/mansion blocks and west craft roofs. Do not enlarge or recenter the city.',
 'NORTHEAST: LEFT and BOTTOM 26% are shared. Preserve the shown Evertree/court, violet academy, harbor, coast, tiny Asterveil hint and islets. Coastal/island communities retain tiny ordinary roofs and docks. Wraith is a very small low prison on a remote crag, not a large skull fortress. Match shared tree, streets, sea and harbor to the refined neighbors.',
 'SOUTHWEST: RIGHT and TOP 26% are shared. Preserve the river, falls, green ridges, woods and shown blue academy/city wall. Greyfield immediately beyond the southwest/southern wall is cramped patched slum housing with muddy lanes. Farther farm villages remain maintained communities. Tiny regional roofs, no large cabin or cave additions. Keep source gate-road and river crossings aligned in the overlap.',
 'SOUTHEAST: LEFT and TOP 26% are shared. Preserve the shown gold academy/city wall, coastal water, farms, villages and hidden small Shadowspire. Near the southern gate use Greyfield slum housing; farther villages remain maintained farm settlements. Country tracks stay thin and unpaved. Match the central avenue/wall and farmland to neighbor references, with no enlarged suburbs or extra monuments.'
 ]
 neighbors=[['a2','a3'],['a1','a4'],['a1','a4'],['a2','a3']];jobs=[]
 for i,d in enumerate(['Northwest','Northeast','Southwest','Southeast'],1):
  jobs.append({'id':f'ao{i}','set':'Circular With Overlap','panel':i,'direction':d,'file':f'world-draft/map-variations/Glowhaven Panel Refinement/Circular With Overlap/0{i} - {d}.png','sourceBounds':list(bounds[i-1]),'references':[f'tmp/glowhaven-panel-art/overlap-inputs/{i}.png',m['sourceMaster'],previous[f'a{i}']]+[previous[n] for n in neighbors[i-1]],'prompt':common+'\n'+local[i-1]})
 m.update(jobs=jobs,scope='One circular set of four genuinely overlapping refinements; asymmetrical set cancelled',overlapPrepared=True,sourcePanelSize=[720,720],sharedSourcePixels=186,sourceStep=534)
 write(ART/'jobs.json',m);print(json.dumps({'overlapInputs':4,'sourceSharedPixels':186,'overlapFraction':186/720,'asymmetricalCancelled':True}))
def package():
 m=read(ART/'jobs.json');jobs=m['jobs'];assert len(jobs)==4 and m['overlapPrepared'];OUT.mkdir(parents=True,exist_ok=True);rows=[]
 for j in jobs:
  r=read(ART/'generated'/(j['id']+'.json'));assert hashlib.sha256((ROOT/j['file']).read_bytes()).hexdigest()==r['sha256'];rows.append(r)
 assert len({r['sha256'] for r in rows})==4 and len({tuple(r['dimensions']) for r in rows})==1
 n=rows[0]['dimensions'][0];step=round(n*534/720);overlap=n-step;canvas=n+step;placements=[(0,0),(step,0),(0,step),(step,step)]
 guide=f'# Glowhaven — overlapping panel assembly\n\nCircular layout only. Four working quadrants; final Voyage map remains 3 × 3.\n\nNative panels: {n} × {n}. Each source crop is 720 × 720; neighbors share 186 source pixels on both central axes.\n\nStart with a {canvas} × {canvas} canvas. Place layer top-left corners here:\n\n| Panel | X | Y |\n| --- | --- | --- |\n'
 for r,(x,y) in zip(rows,placements):guide+=f"| {r['panel']} {r['direction']} | {x} | {y} |\n"
 guide+=f'\nShared output width is about {overlap} pixels along each inner edge, including the four-way center. Keep those bands; do not crop to quarters. Align matching river bends, roofs and wall towers, then use a soft eraser or layer mask to blend one layer into the other. Select one coherent version of a whole tree/building rather than blending through a doubled structure.\n\nThese are starting positions, not exact registration: generated geometry can shift. Alignment and seam repair remain necessary. After finishing the square, slice 3 × 3; at this starting canvas size, tiles would be {canvas/3:g} pixels.\n\nOriginal PNG pixels are unchanged. No fading/matte is baked in. World JSON, coordinates and hosted art are untouched.\n'
 (OUT/'Assembly Guide.md').write_text(guide,encoding='utf-8')
 with zipfile.ZipFile(OUT/'Glowhaven - Circular Panels With Overlap.zip','w',zipfile.ZIP_DEFLATED) as z:
  for j in jobs:z.write(ROOT/j['file'],pathlib.Path(j['file']).name)
  z.write(OUT/'Assembly Guide.md','Assembly Guide.md')
 with (OUT/'Panel Index.csv').open('w',encoding='utf-8-sig',newline='') as f:
  writer=csv.DictWriter(f,fieldnames=['panel','direction','file','dimensions','sourceBounds','sha256','startX','startY']);writer.writeheader()
  for r,(x,y) in zip(rows,placements):writer.writerow({**{k:r.get(k) for k in writer.fieldnames if k not in ['startX','startY']},'startX':x,'startY':y})
 thumb=520;sheet=Image.new('RGB',(1060,1120),'#151b22');draw=ImageDraw.Draw(sheet);font=ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf',20)
 for r in rows:
  i=r['panel']-1;x=10+(i%2)*530;y=10+(i//2)*560
  with Image.open(ROOT/r['file']) as im:sheet.paste(im.convert('RGB').resize((thumb,thumb),Image.Resampling.LANCZOS),(x,y))
  draw.text((x,y+524),str(r['panel'])+' '+r['direction'],font=font,fill='white')
 sheet.save(OUT/'Panel Review.jpg',quality=94)
 write(ART/'delivery.json',{'panels':4,'nativeDimensions':[n,n],'sourceSharedPixels':186,'approximateOutputOverlap':overlap,'startingCanvas':[canvas,canvas],'placements':placements,'canonicalEdited':False,'stitched':False,'asymmetricalCancelled':True})
 print(json.dumps({'panels':4,'dimensions':[n,n],'overlap':overlap,'startingCanvas':canvas,'output':str(OUT)}))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('command',choices=['save','prepare-overlap','package']);p.add_argument('job',nargs='?');p.add_argument('source',nargs='?');a=p.parse_args()
 if a.command=='save':save(a.job,a.source)
 elif a.command=='prepare-overlap':prepare()
 else:package()
