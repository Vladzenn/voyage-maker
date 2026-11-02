"""Merge the author's final pins, rename the portal shrine and prepare exact art jobs."""
import copy, hashlib, json, pathlib, sys
from build import ROOT, HERE, dump

SOURCE=pathlib.Path(r'C:/Users/VladCodes/.codex/attachments/23da8cc9-d365-41ab-8dde-4aacbe87a199/Pasted text.txt')
OLD='Benitsuru Transit Shrine'
NEW='Benitsuru Portal Shrine'
ART=HERE/'location-art'

def rename(v):
    if isinstance(v,str):return v.replace(OLD,NEW)
    if isinstance(v,list):return [rename(x) for x in v]
    if isinstance(v,dict):return {rename(k):rename(x) for k,x in v.items()}
    return v

def main():
    ART.mkdir(exist_ok=True)
    if (ART/'source-merge.json').exists():raise SystemExit('Merge already applied; use the persisted art jobs.')
    path=ROOT/'world-draft/WorldAlpha - World.json'
    before=json.loads(path.read_text(encoding='utf-8'))
    incoming=json.loads(SOURCE.read_text(encoding='utf-8-sig'))
    assert set(incoming)==set(before['locations'])
    changes=[]
    for name,loc in incoming.items():
        fields=[k for k in set(loc)|set(before['locations'][name]) if loc.get(k)!=before['locations'][name].get(k)]
        if fields:
            assert set(fields)<=set(['x','y']),(name,fields)
            changes.append({'name':name,'before':{k:before['locations'][name][k] for k in fields},'after':{k:loc[k] for k in fields}})
    assert len(changes)==5
    w=copy.deepcopy(before);w['locations']=incoming;w=rename(w)
    # Explicit solo shortcuts supplement semantic travel. Multiplayer keeps its consent gate.
    for key in ['oni_portal_to_direct','oni_portal_from_direct']:
        tr=w['triggerDefinitions'][key]
        tr['script']=tr['script'].replace("if(!new RegExp(","if(Object.keys(check({type:'player-level'})||{}).length!==1||!new RegExp(",1)
    tr=w['triggerDefinitions']['oni_portal_from_direct']
    old='(?:return|head back|go back) to (?:glowhaven|evertree(?: base)?))[.!]?$'
    new='(?:return|head back|go back) to (?:glowhaven|evertree(?: base)?)|use (?:my |the )?(?:glowhaven|gloomhaven)(?: portal)?(?: return)? key(?: to return(?: to (?:glowhaven|evertree(?: base)?))?)?)[.!]?$'
    assert old in tr['script'];tr['script']=tr['script'].replace(old,new)
    # The shortcut's key-use branch requires the actual key; entering the fixed arch stays free.
    tr['script']="const oniUse=check({type:'action-text'});if(/\\buse\\b/i.test(String(oniUse))&&!check({type:'player-item',item:'Glowhaven Portal Key',operator:'greaterThan',value:0})){skip=true;}else{\n"+tr['script']+'\n}'
    q=w['triggerDefinitions']['oni_portal_from']['conditions'][-1]
    q['query']+=' Deliberately using a held Glowhaven Portal Key here to return also qualifies; an absent key claim does not.'
    q=w['triggerDefinitions']['cc1_grove_return']['conditions'][-1]
    q['query']+=' Deliberately using a held Sepulchral Portal Key here to return also qualifies. The fixed return arch itself needs no key.'
    dump(path,w)
    manifest=rename(json.loads((HERE/'manifest.json').read_text(encoding='utf-8')))
    dump(HERE/'manifest.json',manifest)
    # Keep editable source names and fixtures aligned, retaining historical reports verbatim.
    for filename in ['geography.py','cast.py','systems.py','followup_preferences.py','types_and_lore.py','build.py','guild_patch.py','quests.py']:
        p=HERE/filename;p.write_text(p.read_text(encoding='utf-8').replace(OLD,NEW),encoding='utf-8')
    p=ROOT/'tools/test_oni.cjs';p.write_text(p.read_text(encoding='utf-8').replace(OLD,NEW),encoding='utf-8')
    proof={'source':str(SOURCE),'sourceSHA256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'beforeWorldSHA256':hashlib.sha256(json.dumps(before,ensure_ascii=False,sort_keys=True).encode()).hexdigest(),'coordinateChanges':changes,'rename':{OLD:NEW},'sourcePins':{rename(n):{k:loc[k] for k in ['x','y','region']} for n,loc in incoming.items()},'allSourceImagesPreserved':all(w['locations'][rename(n)].get('images')==loc.get('images') for n,loc in incoming.items()),'portalChanges':['Solo-only direct Oni shortcuts','Held Glowhaven key-use return from Benitsuru','Explicit held Sepulchral key return wording'],'spiderChanged':False}
    dump(ART/'source-merge.json',proof)
    from regression_delta import record
    record(w)
    styles={
      'Blackpine March':'Deep cedar greens, indigo cloth, silver streams and fern-grown pale stone; small roadside buildings and forest working life.',
      'Thundercrag Highlands':'Pale quarry stone, dark basalt, amber mineral accents and clean mountain daylight; practical stone terraces and timber hoists.',
      'Mount Shiun':'Mountain cedar greens, vermilion shrine accents, cloud-white falls and weathered stone stairs; sacred places remain properly furnished and human-scaled.',
      'Snowcedar Heights':'Clear cold blues, white snow, dark conifers and restrained warm refuge light; snow load, steep terrain and exposed rock are credible.',
      'Mizuhara Lake Country':'Blue-green freshwater, white plaster and dark Japanese roof tiles, bright patterned market awnings and reeds; inland lake setting, never an ocean port.',
      'Bamboo Veil Valleys':'Luminous green bamboo, turquoise river channels, ivory paper and small bright indigo or red accents; canals, mills and closely woven paths.',
      'Benitsuru Basin':'A lively Edo-inspired capital: tiled layered roofs, white plaster, patterned colored awnings, timber galleries and canal bridges. Castle buildings remain distant unless this is the castle itself.',
      'Koganedai Terraces':'Golden ginkgo foliage, slate roofs, cream plaster and emerald gardens; orderly terraces with selective workshops, not an industrial city.',
      'Mirror-Reed Lowlands':'FORESTED cedar ridges and narrow turquoise river channels, mossy rocks, footpaths and one ordinary bridge. Reeds fringe water; no broad lake, ferry terminal or fishing village.',
      'Golden Grain Plain':'Golden grain and green rice paddies, susuki grass, orchard foliage and flowing irrigation; small farm buildings and beautiful practical rural life.',
      'Redleaf River Country':'Vivid crimson and orange maples beside blue-green river water; red arched bridges, cream shrine plaster and warmly colored village buildings.',
      'Lanternwood Border':'Enormous forest trunks, dense emerald canopy, pale roots and little blue-green foxfire where the description supports it; an eerie wooded border, not a city.',
      'Veiled Cedar Reach':'Dense layered pale fog, immense dark cedars, pale exposed roots and dusky blue-violet water. An unsettling spirit wilderness; brief lantern glow never makes it a friendly theme park.'}
    jobs=[]
    for name in manifest['locations']:
        loc=w['locations'][name];region=w['regions'][loc['region']]
        role='A broad establishing view that communicates the whole place, not a map. Choose an exterior or open landscape for a site with multiple areas; a building may use its recognizable main public interior when that best expresses its actual function.'
        if name==NEW:role='EXTERIOR establishing view of the receiving shrine and its courtyard: clearly readable vermilion beams and tiled roofs, the transit torii glimpsed inside. Distinct from the separate interior Portal Hall image. The distant Shogunal castle must remain secondary.'
        facts=loc['basicInfo'].split(' Nearby routes lead toward')[0]
        areas='; '.join(k.split(' - ',1)[-1] for k in loc['areas'])
        prompt=f'''Use case: illustration-story. Create ONE finished SQUARE 1:1 location environment image for {name}, in The Schools of Magic, Arise!\nSCENE FACTS: {facts}\nPLAYABLE SPACES TO INFORM THE SETTING: {areas}. Do not turn these into panels or a montage.\nREGIONAL ART DIRECTION: {styles[loc['region']]}\nVIEW: {role} Scene-level eye height or a modest raised viewpoint, strong layered foreground/midground/background. Show several distinctive functional prop groups that fit this exact location. Avoid a distant aerial map view.\nRENDERING: polished, richly colored TWO-DIMENSIONAL fantasy-anime environment illustration, crisp intentional linework and readable architectural shapes, painterly color and light, stylized JRPG background detail. Everything feels hand illustrated; no photographic surfaces, 3D render, plastic edges or realism. Vary the local palette and lighting meaningfully for this place.\nWORLD: Japanese-inspired fantasy country, full of varied patterned fabrics and traditional timber, plaster, stone and tile; imported Magitech is rare and selective. No guns, modern cars, electrical poles, cyberpunk skyline or blanket industrial machinery. A tiny appropriate everyday magical detail can enrich an inhabited magical place; do not invent a plot artifact or unique landmark. Magic can have flowing translucent brushlike edges rather than uniform glitter.\nLIFE AND MOOD: Match the actual site: a few tiny ordinary background people for an inhabited establishment, never prominent faces or named character designs; no people at abandoned or isolated dangerous sites. Wilderness expresses its danger through terrain and traces, not a foreground monster portrait or a fight.\nCOMPOSITION: full-bleed single square image, detailed without clutter; defining feature in central 60% to survive wide and tall UI crops. No UI, frame, split screen, collage, readable text, lettering, calligraphy, signage words, labels, logos, signature or watermark.'''
        jobs.append({'id':f'loc-{len(jobs)+1:03}','location':name,'area':None,'target':'LOCATION_IMAGE','file':f'world-draft/location images/Akitsuhara/{name}.png','prompt':prompt,'status':'not-started'})
    hall=NEW+' - Portal Hall'
    prompt=f'''Use case: illustration-story. Create ONE finished SQUARE 1:1 AREA environment image for {hall}. A scene-level INTERIOR view, distinct from the parent shrine exterior. A single tall vermilion torii-shaped transit arch stands on a dry pale tiled floor under the receiving hall's dark timber roof; soft translucent blue-gold mana frames a restrained luminous view of Glowhaven's underground Evertree Portal Room, with root-bound stone vaults on the far side. The opening remains unobstructed and physically usable. Paper screens open toward Benitsuru's bright courtyard; a separate permit counter and orderly waiting benches sit to the side, baggage baskets neatly tucked away. No ritual altar or inaccessible decorative gate. Strong spatial depth, tall red beams, white screens, blue-gold portal light and daylight at the veranda. A couple of tiny waiting travelers may remain far in the background. Polished richly colored TWO-DIMENSIONAL fantasy-anime environment illustration, crisp deliberate linework, stylized architectural forms, painterly JRPG background color and lighting. Selective magical wonder, no photorealism, 3D render, plastic textures, futuristic machinery or firearms. Full-bleed single square composition, portal centered within the middle 60% for crop safety. No maps, collage, panels, UI, readable writing, symbols used as lettering, label, logo, watermark or signature.'''
    jobs.append({'id':'area-portal-hall','location':NEW,'area':hall,'target':'AREA_IMAGE','file':f'world-draft/area images/Akitsuhara/{hall}.png','prompt':prompt,'status':'not-started'})
    assert len(jobs)==110
    assert all(not w['locations'][j['location']].get('images',{}).get('establishingShot',{}).get('imageUrl') for j in jobs if not j['area'])
    dump(ART/'jobs.json',jobs)
    print(json.dumps({'mergedCoordinateChanges':len(changes),'locationImages':109,'areaImages':1,'name':NEW,'sourceImagesPreserved':proof['allSourceImagesPreserved']}))

if __name__=='__main__':main()
