"""One establishing image per new site, plus portal and dungeon area views."""
import argparse,hashlib,json,pathlib,shutil,sys
HERE=pathlib.Path(__file__).resolve().parent;ROOT=HERE.parents[1]
sys.path.insert(0,str(ROOT/'tools'));import project
DEST=ROOT/'world-draft/location images/Ardelis'
SPECIAL={
 'Caelrath Palace':'A broad exterior three-quarter view of the one great upper royal palace on its actual mountain terrace: layered white spires, violet roof details and immense thin gold celestial rings suspended about its upper towers. Waterfalls descend beyond its retaining wall. A formal approach leads inward; do not show its hidden dungeon.',
 'Hall of Mirrors':'An exterior of the elegant ballroom wing attached to the same Caelrath royal palace complex, with high glass windows, a side terrace and subtle reflections. It is an annex, not a detached second palace.',
 'Caelrath Sewers':'Look from the base of a maintenance stair along an impressive but practical vaulted drainage gallery. Raised stone inspection walks, warm maintenance lamps, bronze sluice controls and a dark foul-water channel. Distinct sealed drinking-water pipes above. A controlled old side branch bends out of sight. No giant monster, skull architecture, glowing royal reactor or direct palace entrance.',
 'Opaline Arcade':'A lively richly colored luxury shopping arcade: glass canopy, gold brackets, white carved piers, peacock-blue jeweler displays, saffron perfume salon windows, colorful silks and elegant hats in couture showcases. Goods and fine work are the focus; it is not a shopping mall with modern brands.',
 'Velvet Lyre Hall':'A handsome concert house exterior beside a water terrace, vivid red and violet awnings, an open foyer revealing musical instrument cases and a warm performance floor. Celestial decorations are small tasteful accents, not royal insignia plastered everywhere.',
 'Caelrath Portal Hall':'A recognizable staffed transit-hall exterior at the Kingsward approach, ivory pointed arch, violet roof, modest gold celestial emblem and sheltered waiting gallery. The actual magical portal is inside, not a giant city-destroying beam.',
 'The Old Receiving House':'An austere private stone research-medical house with a closed side courtyard, screened windows and a guarded practical service door. Subtle unease through rigid order, no prisoners on display or public clues revealing the entire plot.',
 'The Sunken Bell':'A sea-level view across shallow wreck water, with a broken ship frame visible below clear blue water and a small bell entangled in beams. Shore approach remains visible. No permanent ghost, boss, kraken or person in the foreground.',
 'Starward Commandery':'A working celestial paladin chapterhouse: white stone exterior, violet pitched roofs, gold star motifs used selectively, a plain open practice yard, repair racks and a modest field chapel joined to the same building. An institution in a wealthy capital, not another royal palace.'}
def prepare():
    p=HERE/'location-jobs.json'
    if p.exists():return project.load(p)
    w=project.load(ROOT/'output/ardelis-2026-11-05/The Schools of Magic, Arise! - Ardelis.json');review=project.load(HERE/'review.json');jobs=[]
    for name in review['contents']['locations']:
        loc=w['locations'][name];desc=loc['basicInfo']
        brief=SPECIAL.get(name,'Show the distinctive whole-site exterior or main public space described below, with actual functional props, human-scale doorways and a readable approach. Avoid an aerial map view.')
        prompt=f"Create one square 1:1 location ESTABLISHING SHOT for {name} in Caelrath, the rich capital of Ardelis. {brief} Scene facts: {desc} Location areas for context, not a labeled diagram: {', '.join(k.split(' - ',1)[-1] for k in loc['areas'])}. Polished richly colored 2D fantasy-ANIME environment illustration, expressive deliberate drawn shapes, painterly color and clear depth, premium high-fantasy JRPG background. City identity: CONNECTED mountain terraces of pale white masonry, gold ornament and violet roof accents; waterfalls descend toward working coastal harbors, mountains far beyond, physically connected bridges and streets. This is NOT floating sky islands. Vary this particular place's textiles, wood, shop colors and lighting according to its purpose; no identical palace for every home or shop, no universal purple wash. A modest inhabited shop remains small against the royal skyline. Functional furniture, tools, maintained paths and subtle everyday magical lamps rather than random clutter. Ordinary secondary people may be tiny distant background silhouettes where public life fits, never a named prominent figure. No permanent boss, named NPC, combat scene or giant monster; preserve only durable habitat traces. Build a crop-safe scene: all defining architecture or functional focal objects remain in the middle 60% so both narrow arrival cards and wide desktop banners remain usable. No readable text, lettering, labels, city map, UI, logo, signature or watermark. No photography, 3D render or empty generic building. One finished PNG."
        jobs.append(dict(id=f'loc-{len(jobs)+1:03}',name=name,location=name,kind='location',target='LOCATION_IMAGE',prompt=prompt))
    for loc,area,scene in [('Caelrath Portal Hall','Portal Room','An impressive but human-scale vaulted transit chamber with ONE permanent stone-framed return portal, a clear floor, a modest officer desk beyond a low rail and a controlled ordinary entrance. Its subtle green-gold view suggests the Evertree rootward hall, not another Ardelis street. No second destination or surprise portal.'),('Caelrath Palace','Resonance Cradle','A deep circular stone laboratory chamber with suspended empty brass support rings, ivory ceramic fittings, a cracked calibration dais, conduits and a single service bridge. No experimental monster or fixed NPC in this static shot. The door and retreat bridge remain readable, with heavy cover piers and violet instrument light; technical rather than a generic evil throne.')]:
        name=loc+' - '+area
        jobs.append(dict(id=f'area-{len(jobs)+1:03}',name=name,location=loc,area=name,kind='area',target='AREA_IMAGE',prompt=f'One square 1:1 premium 2D fantasy-anime environment illustration, area image of {name} in Caelrath, Ardelis. {scene} Rich illustrated stone and metal, selective gold and violet, magical subtle lighting, readable functional objects, no people or creature. Keep the main focal apparatus or portal in the central 60% for safe tall and wide crops. No labels, text, logos, UI, map, photography, 3D render or watermark. One finished PNG.'))
    project.write_json(p,jobs);return jobs
def save(job_id,source):
    jobs=prepare();job=next(j for j in jobs if j['id']==job_id);source=pathlib.Path(source);assert source.is_file()
    DEST.mkdir(parents=True,exist_ok=True);file=DEST/(job['name']+'.png');assert not file.exists(),'Already saved: no unrequested reroll.'
    shutil.copy2(source,file);p=HERE/'location-files.json';state=project.load(p) if p.exists() else {}
    state[job_id]={**{k:v for k,v in job.items() if k!='prompt'},'file':file.relative_to(ROOT).as_posix(),'sha256':hashlib.sha256(file.read_bytes()).hexdigest(),'source':str(source)}
    project.write_json(p,state);print(json.dumps({'saved':job_id,'name':job['name']},ensure_ascii=False))
if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--save',nargs=2);args=a.parse_args()
    if args.save:save(*args.save)
    else:print(json.dumps({'prepared':len(prepare())}))
