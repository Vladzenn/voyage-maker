"""Verify exact selected artwork and package the current world, never rebuild it."""
import argparse
import csv
import hashlib
import json
import shutil
import zipfile
import update


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--contact-sheets',action='store_true');args=ap.parse_args()
    update.apply_urls()
    w=update.load(update.WORLD);content=update.load(update.HERE/'contents.json')
    portraits=update.load(update.HERE/'portrait-files.json')
    scenes=update.load(update.HERE/'location-files.json')
    receipts=update.load(update.HERE/'upload-receipts.json')
    urls=update.load(update.HERE/'portrait-urls.json')
    assert len(portraits)==116 and len(scenes)==86
    assert set(portraits)==set(content['npcs'])|{"Valkazathoth'dmir"}
    assignments=[]
    for name,e in portraits.items():
        r=receipts['NPC_PORTRAIT::'+name]
        assert r['target']=='NPC_PORTRAIT' and r['name']==name
        assert r['imageUrl']==urls[name]==w['npcs'][name]['portraitUrl']
        assert sha(update.ROOT/e['file'])==e['sha256']==r['sha256']
        assignments.append(dict(name=name,target=r['target'],file=e['file'],sha256=e['sha256'],imageUrl=r['imageUrl']))
    for e in scenes.values():
        address=e['location']+('::'+e['area'] if e['kind']=='area' else '')
        r=receipts[e['target']+'::'+address]
        site=w['locations'][e['location']]
        if e['kind']=='area':site=site['areas'][e['area']]
        assert site['images']['establishingShot']['imageUrl']==r['imageUrl']
        assert sha(update.ROOT/e['file'])==e['sha256']==r['sha256']
        assignments.append(dict(name=e['name'],target=e['target'],file=e['file'],sha256=e['sha256'],imageUrl=r['imageUrl']))
    assert len({e['file'] for e in assignments})==202
    assert len({e['sha256'] for e in assignments})==202,'Duplicate selected image bytes'
    world_sha=sha(update.WORLD)
    proof=dict(complete=True,worldSHA256=world_sha,portraits=116,locationImages=84,areaImages=2,assignments=assignments,
      note='Exact local file hashes, canonical target keys and official hosted URLs verified. Not a live Studio crop or gameplay test.')
    update.write(update.HERE/'art-verification.json',proof)
    update.OUT.mkdir(parents=True,exist_ok=True)
    full=update.OUT/'The Schools of Magic, Arise! - Ardelis Complete.json'
    assert sha(full)==world_sha
    # Complete native sections are safe replacements; these are never additions-only.
    for section,label in [('npcs','NPCs'),('locations','Locations'),('regions','Regions'),('triggerDefinitions','Triggers')]:
        update.write(update.OUT/('Ardelis Complete - '+label+'.json'),w[section])
    for ledger,archive_name in [(portraits,'Ardelis - Complete Portraits.zip'),(scenes,'Ardelis - Location and Area Artwork.zip')]:
        with zipfile.ZipFile(update.OUT/archive_name,'w',compression=zipfile.ZIP_STORED) as archive:
            for e in ledger.values():
                file=update.ROOT/e['file'];archive.write(file,file.name)
        with zipfile.ZipFile(update.OUT/archive_name) as archive:
            assert len(archive.namelist())==len(ledger)==len(set(archive.namelist()))
    pins=update.load(update.HERE/'placements.json')
    with (update.HERE/'placements.csv').open('w',encoding='utf-8-sig',newline='') as f:
        cols=['name','region','x','y','placementStatus','source','sourceRegion']
        writer=csv.DictWriter(f,fieldnames=cols,extrasaction='ignore');writer.writeheader();writer.writerows(pins)
    docs=['Ardelis - Patch Notes.md','Ardelis - Development Notes.md','Ardelis - Map and Landmark Handoff.md']
    for name in docs:shutil.copy2(update.ROOT/'world-draft'/name,update.OUT/name)
    shutil.copy2(update.HERE/'placements.csv',update.OUT/'Ardelis - Corrected Placements.csv')
    shutil.copy2(update.ROOT/'research/Gemini Audit Review - 2026-11-05.md',update.OUT/'Gemini Audit Review - 2026-11-05.md')
    (update.OUT/'README.md').write_text(
        '# Ardelis complete follow-up\n\n'
        'Import **The Schools of Magic, Arise! - Ardelis Complete.json** as the complete current world. '
        'The NPCs, Locations, Regions and Triggers JSON files here are complete sections, not partial additions.\n\n'
        'The portrait ZIP contains exactly 116 selected named PNGs: all 115 Ardelis characters and Vladimir. '
        'It excludes superseded and rejected versions. Kaede has one selected corrected rapier image; '
        'Jōji retains his original. Rumi has the single author-approved replacement. '
        'The scene ZIP contains 84 location and two area images. Official hosted URLs are already assigned.\n\n'
        'The latest complete Studio section exports supply all location positions and region images. '
        'Approved human names and the shared independence history are integrated; Noelle and Elven names remain. '
        'Two focused Rebirth progression repairs and the requested 100-turn recurring pursuit are included.\n\n'
        'The Gemini review is findings only: its proposed repairs and an encounter rewrite are not applied. '
        'See Development Notes for live test limits. Official draft validation is not a Studio save or publication.\n',encoding='utf-8')
    with zipfile.ZipFile(update.OUT/'Ardelis - World and Guides.zip','w',compression=zipfile.ZIP_DEFLATED) as archive:
        for file in [full,update.OUT/'README.md',*[update.OUT/n for n in docs],update.OUT/'Ardelis - Corrected Placements.csv',update.OUT/'Gemini Audit Review - 2026-11-05.md']:
            archive.write(file,file.name)
    if args.contact_sheets:
        # QA thumbnails only. Original selected PNGs are never edited.
        from PIL import Image,ImageDraw,ImageFont,ImageOps
        font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',17)
        folder=update.ROOT/'tmp/ardelis-followup/contact-sheets';folder.mkdir(parents=True,exist_ok=True)
        entries=list(portraits.items())
        for page,start in enumerate(range(0,len(entries),16),1):
            sheet=Image.new('RGB',(1040,1600),'#1d2026');draw=ImageDraw.Draw(sheet)
            for i,(name,e) in enumerate(entries[start:start+16]):
                pic=Image.open(update.ROOT/e['file']).convert('RGB');pic.thumbnail((248,360))
                x=(i%4)*260+(260-pic.width)//2;y=(i//4)*400
                sheet.paste(pic,(x,y));draw.text(((i%4)*260+8,y+364),name,font=font,fill='white')
            sheet.save(folder/f'portraits-{page:02}.jpg',quality=90)
    print(json.dumps(dict(complete=True,selectedPortraits=116,sceneImages=86,worldSHA256=world_sha,output=str(update.OUT)),ensure_ascii=False))


if __name__=='__main__':main()
