"""One reviewed establishing shot per new location; official uploads, no Studio save."""
import argparse,copy,getpass,hashlib,json,os,shutil,struct,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent;ART=HERE/'location-art'
sys.path.insert(0,str(ROOT/'tools'))
from voyage_portraits import Client,upload,image_info,write_json

# Visual interpretation only; scene facts are added verbatim from the current JSON.
TREATMENTS={
 'The Gilded Albatross':('A broad three-quarter exterior from just above the nearby water, showing the complete ornate, hard-used sailing vessel at anchor. Deep navy, oxblood and warm gilded trim, cream furled sails, coherent masts and rigging, a raised quarterdeck, timber rails, the working main deck and a small tender secured alongside. Three tiny indistinct sailors mend canvas and handle supplies; no foreground character. A decorative carved albatross at the bow, worn polished wood and restrained enchanted lamps. Sheltered blue water, distant low coastal greenery and scattered white clouds. Impressive but seaworthy, not a palace on water. No guns, cannon, engines, floating modern machinery or oversized magical sails.',None),
 'Starlark Abbey':('A modest complete white-stone abbey beside the southern river, viewed across its approach garden. A small bell tower, welcoming pilgrim court, covered walkway linking chapel and hospice, plain guest-wing windows, useful kitchen garden and a water basin. Ivory stone, faded blue-gray roof slates, lilac flowers and warm small brass lamps; the established star-and-lantern image appears once above the chapel door, without lettering. Two tiny travelers and an indistinct attendant provide lived-in scale. Gentle morning light and a calm working religious household, with ordinary linen drying near the hospice. No vast cathedral, fortified citadel, angel, deity apparition or magical portal.',None),
 'Greenrush Estuary':('A broad inhabited wetland landscape from a low raised bank: pale sandbars divide a winding shallow river where it meets the sea, green and gold reeds, a small timber skiff landing, a raised wooden reedwalk, fish traps, tide stakes and a plain roofed field shelter with drying nets and sample jars. Small working skiffs remain in actual water. A few distant field workers, wading birds and subtle fish glints; bright turquoise shallows with deeper channels visibly darker. Fresh breezy daylight, irregular natural banks and clear useful routes. No large harbor, enormous fishing town, jungle, paved waterfront or unsafe dock blending into dry land.',None),
 'Splinterwake Wreck':('An atmospheric view from a safe rocky approach toward a single old wooden shipwreck wedged across eastern shoal rocks. Broken spars, a tilted weathered hull, torn dark canvas and pale barnacles distinguish it from the intact Gilded Albatross. Shallow turquoise water over the nearest rocks changes to a very dark deepwater edge beyond. A low access shelf is legible without implying easy swimming through the whole wreck. Cool blue late-afternoon light, warm amber cloud breaks, scattered driftwood and an uneasy broad swell. No visible kraken: it is a roaming animal and must not appear permanently in this establishing image. No spectral ship, treasure pile, giant new fortress or captive people.',None),
 'Moonarch Isle':('A small uninhabited rocky island with a surviving broken pale-stone arch, a low weathered plinth, salt grass and sea flowers. View across its quiet pebble landing toward the modest ruin; an accessible stone rise and the darker flooded undercroft are distinct but part of the same small structure. Clear shallow water, sea-worn blocks, patches of lichen and a few faded geometric marks without readable text. One side drops to darker offshore water. Lavender-gray stone, sea-green water, gentle silver-blue morning light. This is a ruin, not an active portal: the arch is empty open air with no luminous gateway. No great temple complex, city, kraken or giant moon.',None),
 'Stillback Isle':('A broad shoreline establishing view of a small quiet rock-and-sand island and its peaceful giant sea turtle Mauruun. The environment is primary: an unoccupied landing pebble bank on one side, clear shallow sea, a warm sheltered nesting shelf and low rocks. Mauruun rests farther across the center, head gently raised, weathered slate shell with modest moss and harmless shell growth; four-flippered sea-turtle anatomy, no buildings on the shell. The reference turtle portrait supplies species, scale color and face only; recompose into a wide environment, not a cropped creature portrait. Separate every rock from the animal with visible water or clear contact surfaces; no stone through flesh. Earth-green, slate and warm sand, softly luminous daylight. No people, saddle, chains, eggs being stolen or combat.', 'world-draft/npc portraits/Glowhaven Expansion/Mauruun.png'),
 'Thistlebank Alchemy Cottage':('A small lived-in rural plaster-and-timber cottage beside a wooded valley track, with moss-green roof tiles and a patched awning. A half-open copper workroom door shows a sturdy bench and condenser, modest glass jars and a cooling basin; raised herb beds, plant trays, drying bundles, clean boots and a few copper pots occupy sensible places around the entrance. Sage green, muted plum, warm copper and flower colors distinguish it from a tavern or academy. Soft patterned afternoon sun, a little harmless steam and two quietly glowing sample jars. No resident close-up, giant mushroom roof, mechanical factory, major magical artifact or unstable explosion.',None),
 'Wrenhill Windmill':('A working traditional timber-and-stone windmill on open grassy downs, seen from its mill yard with four coherent cloth-covered wooden sails, a real central hub, modest sail gallery and entrance. Grain plots lie beyond; two waiting small carts, tied sacks, a weighing platform and a covered timber repair bench show the work. Cream canvas, warm weathered oak, slate blue and ripe wheat gold, fresh late-morning light with turning clouds. Three tiny customers and workers stand safely clear of moving machinery. Thin packed-earth farm tracks, not a paved boulevard. No giant factory, ornate palace, electric power lines or impossible interlocking sails.',None),
 'Old Southwatch':('A small partly ruined stone lookout on a southern wooded rise, seen from the root-crossed forest steps. Its lower room remains habitable with a modest door, faint warm stove light and stacked maintained tools, while broken upper masonry and an incomplete parapet show its age. One narrow intact lookout walk looks beyond pines to open grassland. Mossy gray stone, deep forest green, fern and amber light through foliage; a quiet used refuge rather than an active garrison. No resident portrait, enormous fortress, siege, multiple towers, newly occupied barracks, glowing dungeon gate or excessive ruins.',None),
 'Bluecoil Rest':('An EMPTY sunlit reef habitat with a distant mooring rock, a small distant boat, wet dark ledges, a few disconnected naturally shed blue scales and clear turquoise tidal channels. A broad smooth empty inner resting ledge suggests the scale of the animal that rests here without depicting its presence. No serpent, head, body, coil, creature-shaped rock, statue or ghost silhouette; no electrical arcs or floating spell crystals. Nerathyl appears only in its separate NPC portraits so this location image remains valid whether it is asleep, awake, fighting or absent. Deep blue sea, coral, distant low islands and white clouds. No live animal, people, battle, magical portal or monumental new ruin.',None),
 'Beaconrest Lighthouse':('A red-capped white lighthouse on a modest offshore rock, viewed from a small practical supply jetty across the clear channel. The whole coherent tower, glazed lantern room, signal balcony with shutters and a few simple flags, attached warm keeper cottage and sheltered kitchen window are readable. Barrels, supply crates and a drying line show regular use. White plaster, dark sea-worn rock, restrained red roof and brass fittings, sparkling blue coastal daylight; a faint maintained magical lamp inside the lens, not an enormous laser. A tiny approaching supply skiff is optional background scale. No huge harbor town, giant coastal fort, modern antenna or giant beacon beam.',None),
 'Gullwatch Reefs':('A low coastal reef landscape at receding tide, close enough to read clear pools, kelp, shell fragments and small crabs yet broad enough to show a shallow boat shelf and high gull nesting ledges beyond. Two small white-gray gulls and a safely moored plain fishing skiff are secondary; unoccupied wet stone in the foreground. Sea-green pools, blue open water, rust-colored seaweed and pale sunlit rock with salt flowers. Keep an obvious navigable channel between reef shelves and distinct wet/dry tide lines. A modest useful gathering place, not a boss arena. No giant sea monster, city, temple, towering fantasy arch or permanent named character.',None),
 'Longgrass Crossroads':('Three narrow packed-earth country roads meet in open grassy downs between river country and village approaches. A plain timber way shelter with a bench and covered water jar, modest unreadable notice board, a cart verge with one resting wagon and a weathered direction post form one small practical roadside stop. The riverward path winds away through grazing land; no wide paving. Straw gold, soft grass green, small wildflowers and warm oak under bright moving clouds. Two tiny travelers quietly compare routes rather than addressing the viewer. Do not add a village, toll fortress, giant bridge, ornate ruin, huge market or magical shrine.',None),
 'Seaward Overlook':('An unoccupied quiet grassy coastal cliff seen from its sheltered sitting bank, where a low grassy rise and a few wind-shaped trees protect a natural patch of ground. The foreground grass is inviting, the exposed unguarded edge clearly separate and beyond; far below, bright coastal water and distant tiny sails stretch toward the horizon. Sky blue, silver-green grass, soft pink wildflowers and warm late-afternoon light, graceful wind movement and spacious calm. Place the view and bank centrally for useful crops. No gazebo, bench-shaped throne, resident host, couple, building, tower, ruins, glowing portal or obligatory monster.',None)
}

def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))

def prepare():
    path=ART/'jobs.json'
    if path.exists():return read(path)
    w=read(ROOT/'world-draft/WorldAlpha - World.json');jobs=[]
    shared='Polished colorful 2D fantasy-anime environment illustration for a high-fantasy JRPG: fine deliberate drawing, stylized believable architecture, softly layered painterly shading, rich varied local colors, luminous light and material detail. The image is an environment establishing shot, never a character portrait or an overhead world map. Square 1:1 composition at high native detail. Keep its main identifying feature comfortably within the central crop-safe area for both wide screen banners and tall arrival cards; foreground and sky may extend around it. Do not enforce the same palette, architecture or lighting on every location. No photorealistic camera look or plastic CGI.'
    for i,(name,(treatment,reference)) in enumerate(TREATMENTS.items(),1):
        loc=w['locations'][name];assert not loc.get('images',{}).get('establishingShot',{}).get('imageUrl'),name
        facts=loc['basicInfo']+'\n'+'\n'.join(k+': '+a['description'] for k,a in loc['areas'].items())
        prompt=shared+'\n\nCreate ONE LOCATION establishing image for '+name+'.\nSCENE FACTS from the approved world (do not write the names as text in the image): '+facts+'\n\nVISUAL DIRECTION: '+treatment+'\n\n'+('The supplied image is an identity reference for the single existing animal, not a composition to copy.' if reference else 'Small functional props and contextual background life must remain subordinate to the actual place.')+' No readable text, lettering, labels, map pins, interface, logos, signatures, watermark, collage, inset panels or decorative border. Return one finished PNG only.'
        jobs.append({'id':f'{i:02d}','location':name,'target':'LOCATION_IMAGE','prompt':prompt,'reference':str(ROOT/reference) if reference else None,'file':(Path('world-draft/location images/Glowhaven Expansion 2026-11-04')/(name+'.png')).as_posix(),'originalImages':copy.deepcopy(loc.get('images'))})
    write_json(path,jobs);return jobs

def save(name,source,hint):
    j=next(j for j in prepare() if j['location']==name);dest=ROOT/j['file'];assert not dest.exists(),name
    dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(source,dest);data=dest.read_bytes();width,height=struct.unpack('>II',data[16:24])
    r={k:j[k] for k in ['id','location','target','file']};r.update(source=source,sha256=hashlib.sha256(data).hexdigest(),width=width,height=height,method='built-in image_gen; one requested establishing shot',outputHint=hint)
    write_json(ART/'generated'/(j['id']+'.json'),r);return {'location':name,'width':width,'height':height,'file':j['file']}

def apply(w):
    hosted=read(ART/'hosted.json') if (ART/'hosted.json').exists() else {}
    for name,r in hosted.items():
        assert name in TREATMENTS and r['location']==name and r['target']=='LOCATION_IMAGE',name
        assert hashlib.sha256((ROOT/r['file']).read_bytes()).hexdigest()==r['sha256'],name
        loc=w['locations'][name];old=loc.get('images',{}).get('establishingShot',{}).get('imageUrl')
        assert not old or old==r['url'],'Refusing to replace a valid existing shot: '+name
        loc.setdefault('images',{})['establishingShot']={'imageUrl':r['url'],'crop':{'focus':{'x':50,'y':50},'zoom':100}}
    return {'count':len(hosted),'locations':list(hosted),'jobsFile':'tools/glowhaven-expansion/location-art/jobs.json','hostedFile':'tools/glowhaven-expansion/location-art/hosted.json','existingImagesPreserved':True}

def upload_all(watch=False):
    key=os.environ.get('VOYAGE_CREATOR_API_KEY') or getpass.getpass('Creator key: ')
    if not key:raise ValueError('No key received; no upload attempted')
    c=Client('https://api-alpha.aidungeon.com/creator/v1',key);del key
    contract=c.contract();constraints=contract['x-media-constraints'];assert 'LOCATION_IMAGE' in constraints['targets']
    jobs=prepare();statepath=ROOT/'tmp/creator-api/glowhaven-location-art-upload-state.json'
    state=read(statepath) if statepath.exists() else {};hosted=read(ART/'hosted.json') if (ART/'hosted.json').exists() else {}
    failures=set();deadline=time.monotonic()+5400
    while True:
        for j in jobs:
            name=j['location'];receipt=ART/'generated'/(j['id']+'.json')
            if name in failures or not receipt.exists():continue
            r=read(receipt);file=ROOT/j['file'];data=file.read_bytes();sha=hashlib.sha256(data).hexdigest()
            assert r['location']==name and sha==r['sha256'] and file.stem==name
            if name in hosted:
                if hosted[name]['sha256']==sha:continue
                assert r.get('replacementAuthorized') is True,'Changed image needs explicit replacement authorization: '+name
            mime,width,height=image_info(data);row={'name':name,'file':str(file),'sha256':sha,'mimeType':mime,'width':width,'height':height,'bytes':len(data)}
            try:
                url,status=upload(c,'0kL8UR7rgsu2',row,state,lambda:write_json(statepath,state),constraints,'LOCATION_IMAGE')
                hosted[name]={'location':name,'file':j['file'],'sha256':sha,'target':'LOCATION_IMAGE','url':url}
                write_json(ART/'hosted.json',hosted);print(json.dumps({'location':name,'status':status}),flush=True)
            except Exception as e:
                failures.add(name);write_json(ART/'failures'/(j['id']+'.json'),{'location':name,'error':str(e)})
                print(json.dumps({'location':name,'status':'failed'}),flush=True)
                if getattr(e,'status',None) in [401,403]:raise
        if len(hosted)+len(failures)==len(jobs) or not watch or time.monotonic()>deadline:break
        time.sleep(10)
    print(json.dumps({'uploaded':len(hosted),'failed':len(failures),'studioSaved':False,'studioPublished':False}),flush=True)
    return bool(failures)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('command',choices=['prepare','save','upload']);p.add_argument('--name');p.add_argument('--source');p.add_argument('--hint',default='');p.add_argument('--watch',action='store_true');a=p.parse_args()
    if a.command=='upload':raise SystemExit(upload_all(a.watch))
    print(json.dumps({'jobs':len(prepare())} if a.command=='prepare' else save(a.name,a.source,a.hint),ensure_ascii=False))
