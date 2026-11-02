"""Package the reviewed canonical world; no network calls or Studio mutations."""
import csv,hashlib,json,pathlib,shutil,zipfile

ROOT=pathlib.Path(__file__).resolve().parents[2]
HERE=pathlib.Path(__file__).resolve().parent
OUT=ROOT/'output/oni-nation-2026-11-02'

def main():
    candidate=ROOT/'world-draft/WorldAlpha - World.json'
    w=json.loads(candidate.read_text(encoding='utf-8'))
    m=json.loads((HERE/'manifest.json').read_text(encoding='utf-8'))
    validation=json.loads((HERE/'official-validation.json').read_text(encoding='utf-8'))
    assert validation['data']['valid'] and not validation['data']['errors'] and not validation['data']['warnings']
    full=OUT/'The Schools of Magic, Arise! - Steel and Spirits.json'
    shutil.copyfile(candidate,full)
    shutil.copyfile(candidate,OUT/'The Schools of Magic, Arise! - Portal to Akitsuhara.json')
    (OUT/'Akitsuhara - New NPC Cards.json').write_text(json.dumps({n:w['npcs'][n] for n in m['npcs']},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    rows=[]
    for name in m['locations']:
        loc=w['locations'][name];region=w['regions'][loc['region']]
        rows.append({'realm':region['realm'],'region':loc['region'],'region_x':region['x'],'region_y':region['y'],'location':name,'x':loc['x'],'y':loc['y'],'level_min':loc['npcLevelRange']['min'],'level_max':loc['npcLevelRange']['max'],'areas':'; '.join(loc['areas']),'residents':'; '.join(n for n in m['npcs'] if w['npcs'][n]['currentLocation']==name)})
    with (OUT/'Location Placement Index.csv').open('w',encoding='utf-8-sig',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    guide=['# Akitsuhara location placement index','',
      'The supplied twelve map images, crops and grid coordinates are preserved. Location coordinates use the author’s latest placed-map export, including the approved onsen at its original marker. Native area paths stay within each parent location; roads between locations are described in their actual setting text. These roads are ordinary travel, not hard movement locks.','',
      'Akitsuhara has 102 locations and 335 areas. The Veiled Beyond has seven locations and 21 areas. The CSV includes every address, level band and initially placed resident.','']
    for region in [*m['regions'].values(),'Veiled Cedar Reach']:
        r=w['regions'][region];guide+=['## '+region,'',f"Realm: {r['realm']}; map tile ({r['x']}, {r['y']}).",'', '| Location | Position | Level band | Initial residents |','| --- | --- | --- | --- |']
        for row in rows:
            if row['region']==region:guide.append(f"| {row['location']} | {row['x']}, {row['y']} | {row['level_min']}–{row['level_max']} | {row['residents'] or 'No named initial resident'} |")
        guide+=['']
    (OUT/'Location Placement Guide.md').write_text('\n'.join(guide),encoding='utf-8')
    with zipfile.ZipFile(OUT/'Akitsuhara - Major Portraits and Spirit Map.zip','w',zipfile.ZIP_DEFLATED) as z:
        for name in m['majorNpcs']:
            p=ROOT/'world-draft/npc portraits/Akitsuhara'/(name+'.png')
            z.write(p,'NPC Portraits/'+p.name)
        p=ROOT/'world-draft/maps/The Veiled Beyond/Veiled Cedar Reach.png'
        z.write(p,'Spirit Map/'+p.name)
        z.write(OUT/'Location Placement Index.csv','Location Placement Index.csv')
        z.write(OUT/'Location Placement Guide.md','Location Placement Guide.md')
    with zipfile.ZipFile(OUT/'Akitsuhara - Complete NPC Portraits.zip','w',zipfile.ZIP_DEFLATED) as z:
        for name in m['npcs']:
            p=ROOT/'world-draft/npc portraits/Akitsuhara'/(name+'.png')
            assert p.is_file(),name
            z.write(p,p.name)
    (OUT/'Locations - Akitsuhara Placed and Corrected.json').write_text(json.dumps(w['locations'],ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    shutil.copyfile(ROOT/'world-draft/Steel and Spirits - Patch Notes.md',OUT/'Steel and Spirits - Patch Notes.md')
    proof={'candidateSHA256':hashlib.sha256(candidate.read_bytes()).hexdigest(),'officialDraftValidation':validation,'newNPCs':len(m['npcs']),'majorPortraits':len(m['majorNpcs']),'supportingPortraitsPending':sum(not w['npcs'][n].get('portraitUrl') for n in m['npcs']),'newLocations':len(m['locations']),'newAreas':sum(len(w['locations'][n]['areas']) for n in m['locations']),'nativeQuests':len(m['quests'])+1,'nativeArcs':2,'newTypes':len(m['npcTypes']),'newItems':len(m['items']),'newAbilities':len(m['abilities']),'newStarts':len(m['storyStarts']),'newOrigins':21,'newPastExperienceChoices':14,'newProfessions':len(m['professions']),'newFactions':8,'newTriggers':len(m['triggers']),'existingChangedTriggers':len(m['guildPlaytestFix']['changedTriggers']),'questGenerationCharacters':len(w['storySettings']['questGenerationGuidance'].encode('utf-16-le'))//2,'notes':'Official draft validation and local fixtures only. No Studio save/publication or live AI playtest.'}
    (HERE/'release-review.json').write_text(json.dumps(proof,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in proof.items() if k!='officialDraftValidation'},ensure_ascii=False))

if __name__=='__main__':main()
