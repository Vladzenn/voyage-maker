"""Package selected manual-upload artwork; never mutate coordinates or hosted URLs."""
import csv,hashlib,json,pathlib,shutil,zipfile
from PIL import Image
ROOT=pathlib.Path(__file__).resolve().parents[2];HERE=pathlib.Path(__file__).resolve().parent
OUT=ROOT/'output/elsewhere-art-2026-11-05'


def main():
    brief=json.loads((HERE/'brief.json').read_text(encoding='utf-8'))
    ledger=json.loads((HERE/'manifest.json').read_text(encoding='utf-8'))
    assert len(ledger)==12 and len({r['sha256'] for r in ledger.values()})==12
    assert hashlib.sha256((ROOT/'world-draft/WorldAlpha - World.json').read_bytes()).hexdigest()==brief['canonicalSHA256'],'Manual artwork must not edit world data'
    expected={'map':1,'location':8,'portrait':3}
    for k,total in expected.items():assert sum(r['kind']==k for r in ledger.values())==total
    for r in ledger.values():
        file=ROOT/r['file'];assert hashlib.sha256(file.read_bytes()).hexdigest()==r['sha256']
        with Image.open(file) as im:
            assert im.size==(r['width'],r['height']);im.verify()
        assert r['uploaded'] is False
    OUT.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(OUT/"Vladimir's Elsewhere - Map, Locations and Missing Portraits.zip",'w',compression=zipfile.ZIP_STORED) as z:
        for r in ledger.values():
            sub={'map':'Map','location':'Locations','portrait':'Portraits'}[r['kind']]
            z.write(ROOT/r['file'],sub+'/'+pathlib.Path(r['file']).name)
    # Visual centers estimated on the selected creative map. Positive native y is north.
    percent={'Shifting Gallery':(64,82),'Glassroot Gardens':(19,70),'Inverted Court':(85,16),'Porcelain Workshops':(18,37),'The Little Kingdom':(79,51),'Tilt Court':(59,37),'The Rainward Orchard':(22,17),'The Cabinet of Evenings':(55,14)}
    pins=[dict(name=n,region='The Lantern Circuit',leftPercent=x,topPercent=y,suggestedX=x-50,suggestedY=50-y,status='Optional visual estimate; not applied') for n,(x,y) in percent.items()]
    (HERE/'suggested-pins.json').write_text(json.dumps(pins,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    with (OUT/'Elsewhere - Suggested Pins.csv').open('w',encoding='utf-8-sig',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(pins[0]));writer.writeheader();writer.writerows(pins)
    with (OUT/'Upload Guide.csv').open('w',encoding='utf-8-sig',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=['filename','StudioSection','canonicalKey','usage','dimensions']);writer.writeheader()
        for r in ledger.values():
            sec,usage={'map':('Regions','The Lantern Circuit map image, in Vladimir\'s Elsewhere'), 'location':('Locations','Location establishing shot'), 'portrait':('NPCs','NPC portrait')}[r['kind']]
            writer.writerow(dict(filename=pathlib.Path(r['file']).name,StudioSection=sec,canonicalKey=r['name'],usage=usage,dimensions=f"{r['width']} x {r['height']}"))
    notes=ROOT/'world-draft/Rebirth - Complete Update Patch Notes.md';shutil.copy2(notes,OUT/notes.name)
    shutil.copy2(ROOT/'world-draft/region maps/Elsewhere/The Lantern Circuit.png',OUT/'The Lantern Circuit.png')
    (OUT/'README.md').write_text(
        '# Vladimir\'s Elsewhere artwork and complete update notes\n\n'
        'The ZIP has one map, eight location establishing shots and the three missing portraits. Upload Guide.csv gives exact Studio keys. '
        'The map belongs to Regions → The Lantern Circuit within Vladimir\'s Elsewhere. The scene images belong to the eight parent Locations, not every area. '
        'The portraits are The Ash-Cloaked Courier, The Reed-Cloaked Courier and The Brass Usher.\n\n'
        'All files are prepared for your manual upload. No Creator API request, hosted URL change, coordinate change or world-JSON edit was performed. '
        'The selected map is the creative second pass using the original Glowhaven map as a style-only reference; the rejected rigid layout is excluded. '
        'The direct imagegen workflow follows your explicit override of the staged map skill. Location scenes reference the selected map.\n\n'
        'The map rearranges the locations as authorized. Suggested Pins.csv offers approximate native x/y values with positive y north. '
        'These are optional visual estimates rather than exact registration or automatic migration. Move pins after installing the map. '
        'Only one return gate exists in the world; the Cabinet\'s sky windows are observational scenery.\n\n'
        'The complete update notes cover additions since Universal Fishing commit 48445de, including Rebirth, Shadowspire, Ardelis and the approved follow-up. '
        'The announcement assumes you install this manual artwork before publishing it. It excludes proposed Gemini repairs, an encounter rewrite and unfinished port/map expansion work.\n',encoding='utf-8')
    with zipfile.ZipFile(OUT/"Vladimir's Elsewhere - Complete Manual Upload Pack.zip",'w',compression=zipfile.ZIP_DEFLATED) as z:
        with zipfile.ZipFile(OUT/"Vladimir's Elsewhere - Map, Locations and Missing Portraits.zip") as source:
            for name in source.namelist():z.writestr(name,source.read(name))
        for name in ['README.md','Upload Guide.csv','Elsewhere - Suggested Pins.csv',notes.name]:z.write(OUT/name,name)
    (HERE/'verification.json').write_text(json.dumps({'selectedAssets':12,'counts':expected,'allLocalHashesMatch':True,'allReadablePNG':True,'canonicalUnchangedSHA256':brief['canonicalSHA256'],'manualUploadOnly':True,'noHostedURLsChanged':True,'visualReview':'Map inspected; inspect every returned scene and portrait before final delivery.','scopeSinceCommit':'48445de'},indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'package':str(OUT),**expected,'worldUnchanged':True}))


if __name__=='__main__':main()
