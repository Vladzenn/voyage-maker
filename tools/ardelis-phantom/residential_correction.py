"""Correct the home's immediate setting; preserve its identity, pin and mechanics."""
import copy
import hashlib
import json
from pathlib import Path
from build import ROOT, HERE, WORLD, changes, digest, write


def main():
    before=json.loads(WORLD.read_text(encoding='utf-8-sig')); w=copy.deepcopy(before)
    loc=w['locations']['Crownwater Row']
    loc['basicInfo']=(
        'A narrow residential street sits among the closely fitted neighborhoods inside Caelrath’s city walls. '
        'Pale two-storey houses have violet-tiled roofs, painted shutters, small front gardens and iron gates. '
        'Number 14 has a ground-floor sitting room and a modest upper bedroom. Bread deliveries, washing lines '
        'and conversations across low garden walls give the row its everyday rhythm.'
    )
    edits={
        'Lane':'A gently bending paved lane runs between pale houses with violet roofs, window boxes and low garden walls. Small iron gates open onto the street; neighbors leave room for handcarts, deliveries and pedestrians.',
        'Number 14 Bedroom':'The upper room has a bed, empty shelves and a wardrobe with one squeaking hinge. Its window looks across neighboring tiled roofs and admits morning light, the call of a street vendor and the occasional rattle of a handcart.',
        'Number 14 Garden':'A small enclosed garden has a washing line, an unplanted bed and a rain barrel. Beyond the low rear wall lie neighboring gardens and house backs; it gives no public passage through the house.',
    }
    for area,text in edits.items():loc['areas']['Crownwater Row - '+area]['description']=text
    start=w['storyStarts']['🏠 Ardelis: A Door of Your Own']
    old='Water glints beyond the terrace parapet. Far below, a bell sounds in Kingsward, where the Portal Hall handles travel to Glowhaven.'
    new='Violet roofs crowd the view beyond the low garden walls. A handcart rattles past toward the next junction, where a sign points through the city streets to Kingsward and the Portal Hall’s Glowhaven passage.'
    assert old in start['storyStart'], 'Apply once to the approved home opening'
    start['storyStart']=start['storyStart'].replace(old,new)
    rows=changes(before,w)
    expected={('locations','Crownwater Row','basicInfo'),('storyStarts','🏠 Ardelis: A Door of Your Own','storyStart')}
    expected|={('locations','Crownwater Row','areas','Crownwater Row - '+a,'description') for a in edits}
    assert {tuple(r['path']) for r in rows}==expected
    assert before['parties']==w['parties'] and before['triggerDefinitions']==w['triggerDefinitions']
    assert before['itemTypes']==w['itemTypes'] and before['regions']==w['regions']
    report=dict(baseHash=digest(before),afterHash=digest(w),rows=rows,
                scope='Five prose fields only; address, key/deed, pin, region, quests and mechanics unchanged.',
                publicPatchNotes=False)
    write(HERE/'residential-correction.json',report); write(WORLD,w)
    print(json.dumps(dict(changedFields=len(rows),worldSHA256=hashlib.sha256(WORLD.read_bytes()).hexdigest())))


if __name__=='__main__':main()
