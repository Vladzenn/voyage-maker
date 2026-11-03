"""Prepare stable, actually randomized one-pass portrait jobs and save receipts."""
import argparse,hashlib,importlib.util,json,random,re,shutil,struct,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'tools'))
from portrait_style_refresh import STYLE
from cast import PEOPLE,CREATURES

def write(p,x):
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

MAGIC={
 'Arcane':'a small violet raw-mana construct', 'Metal':'a few curved iron filings suspended in a controlled arc',
 'Gravity':'small nearby pebbles floating in a slow orbit','Enchantment':'a subtle luminous woven pattern in a real working tool',
 'Fire':'a small lively amber flame with translucent warm light','Lightning':'a vivid compact violet electrical arc',
 'Earth':'a few small stone fragments moving above the ground','Wind':'a clear translucent teal wind ribbon moving cloth',
 'Water':'a coherent ribbon of clear blue water with illustrated droplets','Healing':'a soft restorative green-gold light around a careful hand',
 'Nature':'a small sprig unfurling fresh leaves','Light':'a delicate luminous gold ray reflecting through the setting',
 'Summoning':'a small recognizable temporary elemental familiar near the lower frame',
 'Divination':'a small constellation of pale indigo glimpses in an actual viewing medium',
 'Void':'a contained deep-violet absence rimmed with thin pale light','Illusion':'a faint translucent duplicate of a harmless nearby object',
 'Ice':'small suspended ice crystals and a cool curling trace of mist','Sound':'thin blue-violet concentric sound ribbons',
 'Space':'a small tightly controlled distortion of nearby space','Soul':'a pale softly glowing spirit-light near a warding gesture',
}

def prepare():
    path=HERE/'portrait-jobs.json'
    if path.exists():return json.loads(path.read_text(encoding='utf-8'))
    guide=(ROOT/'research/Portrait Creation Format.md').read_text(encoding='utf-8-sig')
    poses={m[0]:{'title':m[1],'text':m[2]} for m in re.findall(r'- \*\*([A-Z]+\d\d) — ([^*\n]+):?\*\*:? ([^\n]+)',guide)}
    if not poses:
        for line in guide.splitlines():
            m=re.match(r'- \*\*([A-Z]+\d\d) — ([^*]+)\*\*:? (.+)',line)
            if m:poses[m[1]]={'title':m[2].rstrip(':'),'text':m[3]}
    rng=random.SystemRandom();jobs=[];recent=[]
    for p in PEOPLE+CREATURES:
        count=rng.choices([1,2,3],weights=[65,25,10])[0]
        affinities=[p['primary']]+rng.sample(p['extra'],count-1)
        if p in CREATURES:
            pose={'category':'special anatomy','id':None,'eligible':[],'title':'Resting animal' if p['name']!='Ghorvath' else 'Surfacing ocean predator','text':'Use the authored animal body plan; no humanoid stance.'}
        else:
            cat='CB' if p.get('special') else p['pose']
            eligible=[k for k in poses if re.fullmatch(cat+r'\d\d',k)]
            if not eligible:raise ValueError('Missing pose pool '+cat)
            # A raised weapon, combat grapple or forceful stance must fit the real prop.
            if p['name']=='Mio Tatsunami':eligible=[k for k in eligible if not any(t in poses[k]['text'].lower() for t in ['shield','bow','scythe','punch','unarmed','dagger','dual'])]
            if p['name']=='Reina Kazehara':eligible=[k for k in eligible if not any(t in poses[k]['text'].lower() for t in ['shield','bow','scythe','spear','staff','unarmed','dual','two-handed'])]
            if not eligible:raise ValueError('Empty compatible pose pool '+p['name'])
            pool=[k for k in eligible if k not in recent[-3:]] or eligible
            index=rng.randrange(len(pool));key=pool[index];recent.append(key)
            pose={'category':cat,'eligible':pool,'uniformIndex':index,'id':key,**poses[key]}
        scene=p['location']+' — '+str(p.get('area') or 'a fitting public working area')
        if p['name']=='Nerathyl':scene='Bluecoil Rest: a tiny remote sunlit reef; the immense serpent sleeps with its complete head on wet stone and coils continuing into the sea. Keep its eye peacefully closed; amber eye color belongs to its established identity, not a reason to wake it. No ship or person beside it for scale.'
        elif p['name']=='Mauruun':scene='Stillback Isle: a quiet sunlit rocky shore and clear shallow sea. The immense four-flippered sea turtle rests peacefully, complete gentle head visible and weathered shell rising behind. No buildings on its shell and no people.'
        elif p['name']=='Ghorvath':scene='Splinterwake Wreck, the dark blue Deepwater Edge: a colossal eight-armed kraken surfaces beside distant broken spars. Its mantle, two eyes and coherent arm roots are legible; several arms can remain submerged. Spectacular ocean spray, indigo Water magic and a dangerous animal silhouette. No humanoid anatomy.'
        framing=('An imposing unusual-anatomy portrait. Use the animal’s real proportions in a vertical 2:3 composition, complete readable head and an unoccupied 15% upper margin. Adapt body crop to show its scale without shrinking the face into an aerial landscape.' if p in CREATURES else 'Centered standing hip-up portrait, vertical 2:3. Complete head, hair, horns and ears; keep the topmost head silhouette 15% down from the top, with clear empty headroom above it. Show readable hips, face and outfit. Props remain outside the reserved top band. Do not crop the hair or enlarge into a bust.')
        effects='; '.join(MAGIC[x] for x in affinities)
        if p in CREATURES:effects+='; integrate this naturally into the animal’s existing environment, not human casting gestures'
        prompt=(STYLE+'\n\nCreate a completely NEW distinct character, '+p['name']+'. The supplied gallery portrait is a STYLE reference only: borrow the fine illustrated finish, material detail and atmospheric light, never its face, sex, clothing, pose, anatomy or location.\n\nIDENTITY: '+p['appearance']+' Apparent life stage: '+p['age']+'. Personality/expression: '+p['core']+' '+p['habit']+'\n\nACTUAL EQUIPMENT: '+p['gear']+' Do not add unrelated inventory or ornate rank.\n\nCOMPOSITION: '+framing+'\nPOSE: '+pose['text']+' For humanoids keep two coherent arms and hands, plausible grip, readable expression and body weight. Any spear/staff is one continuous straight shaft connecting aligned hands to its firmly attached head.\n\nSETTING: '+scene+'. It establishes place while remaining less prominent than the character.\nMAGICAL AFFINITIES, ALL VISIBLE: '+', '.join(affinities)+'. Show '+effects+'. '+('Bold, character-specific visual flair is appropriate.' if p.get('special') else 'This is the standard NPC portrait profile: thoughtful character presence and clearly visible modest affinity effects within a natural working/social moment, not an obligatory battle poster.')+' Keep light, color and materials richly varied and the face focal. Clothing is properly opaque.\n\nNo text, captions, signatures, watermark, interface, frame, character sheet, extra foreground people, duplicate limbs, plastic CGI or photographic skin. Fine anime drawing and soft illustrated shading. Return one PNG only.')
        jobs.append({'name':p['name'],'affinities':affinities,'pose':pose,'profile':'special' if p.get('special') else 'default','prompt':prompt,'reference':'C:/Users/VladCodes/Downloads/Voyage/CharacterPortraits/Adventurers update/Riko Kanehara.png','destination':str(ROOT/'world-draft/npc portraits/Glowhaven Expansion'/ (p['name']+'.png'))})
    write(path,jobs);write(HERE/'affinity-and-pose-draws.json',{j['name']:{k:j[k] for k in ['affinities','pose','profile']} for j in jobs})
    return jobs

def save(name,source,hint):
    jobs=prepare();j=next(x for x in jobs if x['name']==name);dest=Path(j['destination'])
    if dest.exists():raise ValueError('Already saved; no silent replacement: '+name)
    dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(source,dest)
    data=dest.read_bytes();width,height=struct.unpack('>II',data[16:24])
    write(HERE/'generated'/(name+'.json'),{'name':name,'file':str(dest.relative_to(ROOT)).replace('\\','/'),'source':source,'sha256':hashlib.sha256(data).hexdigest(),'width':width,'height':height,'method':'built-in image_gen, one pass','outputHint':hint})
    return {'name':name,'width':width,'height':height,'sha256':hashlib.sha256(data).hexdigest()}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('command',choices=['prepare','save']);p.add_argument('--name');p.add_argument('--source');p.add_argument('--hint',default='');a=p.parse_args()
    print(json.dumps({'jobs':len(prepare())} if a.command=='prepare' else save(a.name,a.source,a.hint),ensure_ascii=False))
