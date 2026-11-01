"""Prepare and upload a precisely addressed environment-art batch; no Studio save/publish."""
import argparse,copy,hashlib,json,os,pathlib,sys
from voyage_portraits import Client,ApiError,upload,image_info,write_json,valid_url
ROOT=pathlib.Path(__file__).resolve().parents[1]
OUT=ROOT/'output/academy-area-art-2026-11-02';META=ROOT/'tools/location-art';WORLD=ROOT/'world-draft/WorldAlpha - World.json'
ACADEMIES=['Phoenix Wing Academy','Hydra Head Academy','Gryffin Tail Academy','Dragon Hoard Academy'];GUILD="Adventurer's Guild - Glowhaven Branch";PORTAL='Evertree Base - Portal Room'
PALETTES={
 'Phoenix Wing Academy':'ivory Gothic stone, pointed red-tiled arches, polished warm wood, crimson and brass accents, small phoenix motifs already established in the existing campus art, climbing ivy, practical well-used spaces and lively warm sunlight',
 'Hydra Head Academy':'ivory pointed arches and mullioned windows, lavender and violet cloth, delicate warm brass, leafy trellises and pale flowers, an elegant welcoming garden-campus atmosphere with lilac magic lamps',
 'Gryffin Tail Academy':'orderly ivory Gothic arcades, cyan and deep teal panels with modest gold edging, blue-glass lanterns, dark polished desks, neat planted niches and calm clear daylight',
 'Dragon Hoard Academy':'high ivory arcades and gold-framed windows, yellow and honey-gold textiles, amber glass lamps, rich practical wood and carefully arranged models or expedition-related display objects',
 GUILD:'honey-colored timber beams and cream stone, teal-and-ochre floor tiles, warm geometric stained glass, solid oak furniture and welcoming practical adventurer equipment',
 'Evertree Base':'root-embraced pale stone vaults beneath the palace, living gold-blue mana veins, deep teal shadow, luminous amber and restrained royal brass details',
}
SCENES={
 'Dining Hall':('A generous three-quarter interior view across occupied meal tables toward a real serving counter. Include cups, bowls, bread baskets, folded cloths and a few secondary adult students in the academy colors. Windows and hanging lamps produce an inviting midday atmosphere. Keep a clear central aisle, benches and table spacing readable.', 'The functional meal tables and serving counter occupy the central crop-safe composition.'),
 'Faculty Offices':('Look down a quiet, human-scaled staff corridor to a modest reception desk, with several private office doors and one partly open workroom. Include appointment trays, closed files, coat hooks, a kettle and work-worn chairs. No throne room, giant council chamber, exposed secret research or prominent named character.', 'The reception desk and nearby office doors form the focal group at center.'),
 'Dormitory Wing':('A residential corridor opens into a shared lounge with reading chairs, a low table and a noticeboard. Clearly show several closed student bedroom doors, shoe racks, a coat stand, a potted plant and personal mugs. This is a comfortable student residence, not an inn lobby or endless ballroom.', 'A central shared lounge anchors the converging corridor and room entrances.'),
 'Sun Terrace':('A sheltered upper terrace with warm stone benches, planted boxes and a balustrade looks across red-roofed academy buildings. Ivy shadows, a half-finished board game and a small hovering warm light make an ordinary quiet afternoon feel magical. A few tiny adult students relax at a distance.', 'The nearest bench and planters form a readable center, with the campus view secondary.'),
 'Music Room':('An intimate comfortable music practice room contains a modest upright stringed keyboard, a lute, a bowed string instrument, a small drum and wooden music stands. Comfortable stools and open floor space support informal practice. Sunlight and subtle warm magical lamplight; no concert stage or modern electronics.', 'Arrange the central instrument group and open practice floor to remain readable in tall and wide crops.'),
 'Lecture Hall':('A large tiered academic room with rows of wooden benches descends toward a broad teaching floor and slate board. Include safe demonstration objects, chalk, plain workbooks and a teacher’s lectern. Geometric chalk traces are abstract and illegible. The scene is an ordinary beginning of class with a few small adult students, no named professor portrait or explosion.', 'Keep the broad teaching floor and central bench aisle visible through the middle of the composition.'),
 'Confluence Pavilion':('A small sheltered garden tea pavilion stands beside a leafy campus path. An ordinary tea tray, two cups, comfortable chairs and flowering planters establish a private break between colleagues. Violet cloth and warm patterned shade, quiet and graceful, no diplomatic ceremony or invented magical altar.', 'The tea table beneath the pavilion roof is central, with paths and flowering garden visible beyond.'),
 'Training Court':('An outdoor stone practice court has marked dueling circles, modest spectator benches and training targets, with open safe space between them. A few small adult students prepare for supervised practice. Bring in low controlled magical light without depicting a battle or destructive spell.', 'The primary practice circle and nearby targets occupy the central safe area.'),
 'Puzzle Parlor':('A relaxed game room with comfortable upholstered seating, small tables, several wooden board games, geometric logic puzzles and a shelf of puzzle boxes. A few adult students lean over a game while an untouched chesslike set sits nearer the viewer. Rich colored afternoon light and a small enchanted desk lamp, not a classroom or laboratory.', 'The nearest puzzle table and comfortable chairs are the central focal group.'),
 'Reception Counter':('An inviting oak reception counter has carefully sorted ledgers, a stamp, small paper trays and neatly arranged colored tabs. Show the low staff gate and a visitor chair. Warm honey light crosses teal floor tiles. A distant anonymous staff silhouette may work behind a side desk; no close-up clerk or named NPC portrait.', 'The counter, staff gate and visitor chair form the clear central composition.'),
 'Request Board':('A wall of framed quest notices in a busy guild side bay has rows divided by bronze, silver, gold and pale platinum metal tabs, without readable rank words or writing. Individual paper slips, wax seals, a nearby waiting bench and a few small adult adventurers inspecting the board. Make paper textures non-alphabetic, no readable letters or numbers.', 'The rank-tabbed noticeboard and nearby bench remain centered and legible as physical objects, not a UI.'),
 'Common Hall':('Sturdy communal oak tables hold cups, field notebooks and modest travel equipment. A kettle station and warm patterned windows invite adventurers to compare a sword belt, a shield strap or a casting staff. A few tiny adult patrons, no beds, bar nightclub or prominent named adventurer.', 'A broad central meeting table with surrounding chairs is the focal group.'),
 'Appraisal Bench':('A quiet side workbench is fitted with a balance scale, magnifying lens, cloth-lined trays and a locked cabinet. A few ordinary ore samples, a damaged buckle, a wrapped focus and a half-unrolled inventory sheet suggest practical examination. A small steady task light; no priceless named relic or glowing all-knowing identification machine.', 'The scale and inspection tray sit centrally on the bench, with the locked cabinet behind.'),
 'Briefing Room':('A quieter practical briefing room has a broad route-planning table, a wall chart with abstract unlabeled topographic contours, a slate surface, rope samples, packed bags and spare stools. Warm geometric glass light, a few adult adventurers discussing a route. No new nation labels, real-world map, written exam answers or magical portal.', 'The table and wall chart are the central functional pair, viewed obliquely from the doorway.'),
 'Training Yard':('A modest walled rear practice yard contains padded targets, a rope-climbing rig, weighted bundles and marked sparring space. Rear guild doors and warm timber eaves are visible. A few secondary adult adventurers perform safe, ordinary drills with swords, shields or staves; no battle or arena crowd.', 'The training apparatus and clear sparring floor sit in the central safe area.'),
 'Staff Office':('A modest staff records office has compact oak desks, labeled-looking but entirely unreadable file drawers, a secure badge cupboard, inkstands and folded correspondence. Four small sample badges in bronze, silver, gold and platinum rest on a cloth inside the staff area. Quiet warm light, no visitor taking a badge and no grand administrative palace.', 'The desk and closed secure records cupboard are central and recognizable.'),
 'Portal Room':('An impressive vaulted transit chamber beneath the Evertree has thick living roots embracing stone arches and blue-gold mana gently threading through the room. Exactly TWO permanent stone-framed outbound portal arches stand along the far wall, with restrained sealed magical surfaces: one carries cold snowy-blue light, the other fresh green and sky-blue light. A broad clear central landing floor receives return traffic. A controlled entrance, a discreet route-key pedestal and ordinary guard station sit to one side. No third active portal, anomalous spider webs, invented destination, throne, giant dragon or readable labels.', 'The two portal arches and clear central return landing are centered, framed by roots and stone vaults.'),
}
REUSE={
 'Phoenix Wing Academy - Arrival Court':'world-draft/location images/Phoenix Wing Academy/phoenix-wing-academy-arrival-court-v2.png',
 'Hydra Head Academy - Arrival Court':'world-draft/location images/Hydra Head Academy/hydra-head-academy-arrival-court-v2.png',
 'Gryffin Tail Academy - Arrival Steps':'world-draft/location images/Gryffin Tail Academy/gryffin-tail-academy-arrival-steps-v2.png',
 'Dragon Hoard Academy - Arrival Gallery':'world-draft/location images/Dragon Hoard Academy/dragon-hoard-academy-arrival-gallery-v2.png',
}

def digest(v):return hashlib.sha256(json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def strip_images(v):
 if isinstance(v,dict):return {k:strip_images(x) for k,x in v.items() if k!='images'}
 if isinstance(v,list):return [strip_images(x) for x in v]
 return v
def record(locations,job):return locations[job['location']]['areas'][job['area']] if job['kind']=='area' else locations[job['location']]

def verify_art_changes(before,after,jobs):
 """Only the selected shots may change; existing crops and other images stay exact."""
 expected=copy.deepcopy(before)
 for job in jobs:
  old=record(before,job);new=record(after,job)
  old_url=old.get('images',{}).get('establishingShot',{}).get('imageUrl')
  if valid_url(old_url) and not job['replace']:continue
  url=new.get('images',{}).get('establishingShot',{}).get('imageUrl')
  if not valid_url(url):raise ValueError('Missing hosted image: '+job['name'])
  shot=record(expected,job).setdefault('images',{}).setdefault('establishingShot',{})
  shot.setdefault('crop',{'focus':{'x':50,'y':50},'zoom':100});shot['imageUrl']=url
 if after!=expected:raise ValueError('The result changed an unselected field or existing crop.')
 if list(before)!=list(after):raise ValueError('Location order changed.')
 for key,l in before.items():
  if list(l.get('areas',{}))!=list(after[key].get('areas',{})):raise ValueError('Area order changed: '+key)
 for key in ACADEMIES+[GUILD]:
  for area,r in after[key]['areas'].items():
   if not valid_url(r.get('images',{}).get('establishingShot',{}).get('imageUrl')):raise ValueError('Unillustrated required area: '+area)
 if not valid_url(after['Evertree Base']['areas'][PORTAL].get('images',{}).get('establishingShot',{}).get('imageUrl')):raise ValueError('Unillustrated Evertree portal room.')

def prepare(source):
 data=json.loads(source.read_text(encoding='utf-8-sig'));locations=data.get('locations',data);w=json.loads(WORLD.read_text(encoding='utf-8'))
 jobs=[];preserved=[]
 for key in ACADEMIES+[GUILD,'Evertree Base']:
  for area,r in locations[key]['areas'].items():
   if key=='Evertree Base' and area!=PORTAL:continue
   if valid_url(r.get('images',{}).get('establishingShot',{}).get('imageUrl')):preserved.append(area);continue
   job={'name':area,'kind':'area','location':key,'area':area,'target':'AREA_IMAGE','replace':False}
   if area in REUSE:job.update(file=REUSE[area],generate=False,review='Previously generated, inspected entrance view; never linked in the incoming JSON.')
   else:
    room=area.split(' - ')[-1];scene,composition=SCENES[room]
    if key=='Hydra Head Academy' and room=='Dining Hall':scene+=' Use joined tables and a few smaller seating groups rather than one regimented refectory.'
    if key=='Gryffin Tail Academy' and room=='Dormitory Wing':scene+=' Give the shared space a small sheltered reading nook.'
    if key=='Dragon Hoard Academy' and room=='Training Court':scene+=' Include movable low barriers and padded shield-test obstacles, no cages of exotic beasts.'
    if key=='Dragon Hoard Academy' and room=='Dining Hall':scene+=' Tables can be rearranged for different groups; high ceilings and a central serving counter.'
    prompt=(f'Create ONE square 1:1 environment illustration for the exact playable area {area}, inside {key}. Polished colorful 2D fantasy-anime JRPG background art: crisp deliberate linework, stylized architecture, rich painterly color and light, clear depth and pristine detail. '
     f'Shared visual identity: {PALETTES[key]}. Exact scene and furnishings: {scene} Composition: {composition} '
     f'Current scene facts to preserve: {r["description"].split(" Use the actual assigned professor")[0].split(" A consultation grants")[0]} '
     'Use a spatially readable oblique room-level view, not an overhead map or character portrait. Furnish the space purposefully; keep the focal architecture near center so both a tall arrival crop and wide banner remain useful. '
     'Everyday magic fits the function, with subtle atmospheric whimsy and bright but controlled highlights. Background people, if appropriate, are small anonymous ADULTS aged 18 or older; no prominent faces, named NPC design or heroic foreground figure. '
     'No readable text, alphabetic lettering, labels, logos, UI, watermark or signature. No photorealism, live-action, 3D render, modern plastic furniture, electrical cables, computers or unsupported major landmark. One finished environment image, not a collage.')
    job.update(file='world-draft/location images/Academy and Guild Areas 2026-11-02/'+area+'.png',generate=True,prompt=prompt)
   jobs.append(job)
 for name in ['Sepulchral Portal House','Sepulchral Conservatory','Mourning Garden']:
  jobs.append({'name':name,'kind':'location','location':name,'target':'LOCATION_IMAGE','replace':True,'generate':False,'file':'world-draft/location images/'+name+'.png','review':'Explicitly requested official reupload of the recent location image; preserve existing crop.'})
 report={'sourceFile':str(source),'sourceSHA256':hashlib.sha256(source.read_bytes()).hexdigest(),'canonicalSHA256':hashlib.sha256(WORLD.read_bytes()).hexdigest(),'sourceLocations':len(locations),'preservedAreaImages':preserved,'jobs':jobs}
 write_json(META/'academy-area-batch-2026-11-02.json',report);write_json(ROOT/'tmp/location-art/incoming-locations.json',locations)
 print(json.dumps({'jobs':len(jobs),'generate':sum(j['generate'] for j in jobs),'reusedEntrances':len(REUSE),'preservedAreaImages':len(preserved)},ensure_ascii=False))

def run_upload(short_id,base):
 manifest=json.loads((META/'academy-area-batch-2026-11-02.json').read_text(encoding='utf-8'));locations=json.loads((ROOT/'tmp/location-art/incoming-locations.json').read_text(encoding='utf-8'));original=WORLD.read_bytes();world=json.loads(original.decode('utf-8-sig'));before=copy.deepcopy(locations)
 if hashlib.sha256(original).hexdigest()!=manifest['canonicalSHA256']:raise ValueError('Canonical changed since preparation; review and prepare a fresh merge base before uploading.')
 client=Client(base,os.environ.get('VOYAGE_CREATOR_API_KEY'));contract=client.contract();constraints=contract['x-media-constraints'];statefile=ROOT/'tmp/creator-api/academy-area-upload-state.json';state=json.loads(statefile.read_text(encoding='utf-8')) if statefile.exists() else {};save=lambda:write_json(statefile,state)
 report={'apiBase':base,'worldShortId':short_id,'contractSHA256':digest(contract),'rows':[],'diff':[]};failed=[]
 for job in manifest['jobs']:
  r=record(locations,job);existing=r.get('images',{}).get('establishingShot',{}).get('imageUrl');row={**job};row.pop('prompt',None);halt=False
  if valid_url(existing) and not job['replace']:row['status']='preserved_existing';report['rows'].append(row);continue
  try:
   row['file']=str(ROOT/job['file']);b=pathlib.Path(row['file']).read_bytes();mime,width,height=image_info(b);row.update(sha256=hashlib.sha256(b).hexdigest(),mimeType=mime,width=width,height=height,bytes=len(b))
   url,status=upload(client,short_id,row,state,save,constraints,job['target'])
   shot=r.setdefault('images',{}).setdefault('establishingShot',{});shot.setdefault('crop',{'focus':{'x':50,'y':50},'zoom':100});shot['imageUrl']=url
   row.update(status=status,newUrl=url);path=['locations',job['location']]+(['areas',job['area']] if job['kind']=='area' else [])+['images','establishingShot','imageUrl'];report['diff'].append({'path':path,'before':existing,'after':url,'fileSHA256':row['sha256']})
  except (ApiError,ValueError,OSError) as e:row.update(status='failed',error=str(e));failed.append(job['name']);halt=isinstance(e,ApiError) and e.status in [401,403,429]
  report['rows'].append(row);write_json(OUT/'Upload Results.json',report);print(json.dumps({'name':job['name'],'status':row['status']},ensure_ascii=False),flush=True)
  if halt:break
 assert strip_images(locations)==strip_images(before),'A non-image location field changed.'
 changed={j['name'] for j in manifest['jobs']}
 for key,l in before.items():
  for area,r in l.get('areas',{}).items():
   if area not in changed:assert locations[key]['areas'][area]==r,area
 if failed:raise ValueError('Incomplete batch; receipts are saved. Failed: '+', '.join(failed))
 verify_art_changes(before,locations,manifest['jobs'])
 if WORLD.read_bytes()!=original:raise ValueError('Canonical changed during upload; resume against current world before merging.')
 world['locations']=locations
 from project import validate
 validate(world);rv=client.request('POST','/validate',body={'world':{'initialGameState':world},'stage':'draft'});report['remoteValidation']=rv;write_json(OUT/'Upload Results.json',report)
 if not rv['data']['valid']:raise ValueError('Official draft validation failed; source world is unchanged.')
 write_json(ROOT/'tmp/location-art/World - Area Art Candidate.json',world);write_json(OUT/'Locations - Academies Guild and Portal Room.json',locations)
 write_json(META/'academy-area-upload-receipts-2026-11-02.json',report)
 print(json.dumps({'uploadedOrResumed':len(report['diff']),'locationsJSON':str(OUT/'Locations - Academies Guild and Portal Room.json'),'officialValidation':rv['data']},ensure_ascii=False))

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('command',choices=['prepare','upload']);p.add_argument('--source',type=pathlib.Path);p.add_argument('--short-id',default='0kL8UR7rgsu2');p.add_argument('--api-base',default='https://api-alpha.aidungeon.com/creator/v1');a=p.parse_args()
 if a.command=='prepare':prepare(a.source)
 else:run_upload(a.short_id,a.api_base)
