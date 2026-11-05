"""Narrow current-world naming/lore migration and selected portrait handoff."""
import argparse, copy, hashlib, json, pathlib, re, shutil, sys, os, time
from contextlib import contextmanager
HERE=pathlib.Path(__file__).resolve().parent
ROOT=HERE.parents[1]
sys.path.insert(0,str(ROOT/'tools'))
import project
WORLD=ROOT/'world-draft/WorldAlpha - World.json'
OUT=ROOT/'output/ardelis-followup-2026-11-05'
BASE=ROOT/'tmp/ardelis-followup/base.json'

def load(p):return json.loads(pathlib.Path(p).read_text(encoding='utf-8-sig'))
def write(p,v):project.write_json(pathlib.Path(p),v)
@contextmanager
def selected_ledger():
    lock=HERE/'portrait-files.lock';deadline=time.monotonic()+15
    while True:
        try:
            fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY);os.close(fd);break
        except FileExistsError:
            if time.monotonic()>=deadline:raise TimeoutError('Portrait ledger is being updated; retry after its writer finishes')
            time.sleep(.05)
    try:
        ledger=load(HERE/'portrait-files.json')
        yield ledger
        temp=HERE/'portrait-files.pending.json';write(temp,ledger);temp.replace(HERE/'portrait-files.json')
    finally:
        lock.unlink()
def digest(v):return hashlib.sha256(json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def names():return dict(l.split('|') for l in (HERE/'names.txt').read_text(encoding='utf-8').splitlines() if l and not l.startswith('#'))
FAMILIES={'Aurevain':'Shirogane','Montrevel':'Minazuki','Dalcourt':'Takamine','Veymont':'Kagetsu'}

def replacer(mapping):
    pattern=re.compile(r'(?<!\w)(?:'+ '|'.join(re.escape(k) for k in sorted(mapping,key=len,reverse=True))+r')(?!\w)')
    return lambda s:pattern.sub(lambda m:mapping[m[0]],s)

def walk(v,fn):
    if isinstance(v,str):return fn(v)
    if isinstance(v,list):return [walk(x,fn) for x in v]
    if isinstance(v,dict):
        out={fn(k):walk(x,fn) for k,x in v.items()}
        assert len(out)==len(v),'Rename collision'
        return out
    return v

def changes(old,new,path=()):
    rows=[]
    # Compare native records, not unordered fragments or guessed schema fields.
    if path in [(),('parties',),('parties','')]:
        for k in dict.fromkeys([*old,*new]):
            if k in old and k in new:rows+=changes(old[k],new[k],path+(k,))
            elif k in old:rows.append(dict(path=[*path,k],kind='removed',before=old[k]))
            else:rows.append(dict(path=[*path,k],kind='added',afterHash=digest(new[k])))
    elif isinstance(old,dict) and isinstance(new,dict):
        for k in dict.fromkeys([*old,*new]):
            if k not in old:rows.append(dict(path=[*path,k],kind='added',afterHash=digest(new[k])))
            elif k not in new:rows.append(dict(path=[*path,k],kind='removed',before=old[k]))
            elif old[k]!=new[k]:rows.append(dict(path=[*path,k],kind='changed',before=old[k],afterHash=digest(new[k])))
    elif old!=new:rows.append(dict(path=list(path),kind='changed',before=old,afterHash=digest(new)))
    return rows

def proof(w):
    b=load(BASE)
    write(HERE/'review.json',dict(baseCommit='1b42222',baseHash=digest(b),afterHash=digest(w),names=names(),rows=changes(b,w)))
    OUT.mkdir(parents=True,exist_ok=True)
    write(OUT/'The Schools of Magic, Arise! - Ardelis Complete.json',w)

def migrate():
    w=load(WORLD)
    assert hashlib.sha256(WORLD.read_bytes()).hexdigest()=='a070c777f601061fcef36d65cf94f557e9f6ee86e564cc48282a7ce869bac924','Use the current approved Ardelis world, never reset a later edit.'
    BASE.parent.mkdir(parents=True,exist_ok=True)
    assert not BASE.exists(),'Migration already started'
    write(BASE,w)
    old=copy.deepcopy(w);mapping=names();fn=replacer({**mapping,**FAMILIES})
    assert not set(mapping.values())&set(w['npcs'])
    r=load(ROOT/'tools/ardelis/review.json')
    w=walk(w,fn)
    first={a.split()[0]:b.split()[0] for a,b in mapping.items()}
    # First-name forms occur in the new cast's own prose. Do not globally alter
    # another established person who happens to share a first name.
    for section,key in [('npcs','npcs'),('locations','locations'),('abilities','newAbilities'),('itemTypes','newItems'),('npcTypes','newTypes')]:
        for name in r['contents'].get(key,[]):
            name=fn(name)
            if name in w[section]:w[section][name]=walk(w[section][name],replacer(first))
    for row in r['rows']:
        if row['kind']=='added' and row['path'][0] in ['factions','storyStarts']:
            section,name=row['path'];name=fn(name)
            w[section][name]=walk(w[section][name],replacer(first))
    for name,v in w['worldLore'].items():
        if name.startswith('Ardelis') or name.startswith('Rebirth'):
            w['worldLore'][name]=walk(v,replacer(first))
    for name in r['contents']['quests']:
        q=w['parties']['']['quests'][fn(name)]
        w['parties']['']['quests'][fn(name)]=walk(q,replacer(first))
    for name,t in w['triggerDefinitions'].items():
        if name.startswith('ar_'):w['triggerDefinitions'][name]=walk(t,replacer(first))
    for name,v in w['parties'][''].get('arcs',{}).items():
        if 'Caelrath' in json.dumps(v):w['parties']['']['arcs'][name]=walk(v,replacer(first))
    # Approved history, without fixing a date, founding ruler or battle roster.
    w['worldLore']['The Founding of Glowhaven']['text']=(
        "Glowhaven began as an Ardelis-backed settlement around the Evertree. The four great archmages whose followers established Phoenix Wing, Hydra Head, Gryffin Tail and Dragon Hoard became the founding fathers of its independent nation. Ardelis imposed heavy taxes and repeatedly compelled the settlement's mages to fight imperial wars. The founders united resistance and fought successfully for independence. Their followers included working families and craftspeople as well as mages. Four Sages Bazaar's monument commemorates that civic legacy.\n\n"
        "Glowhaven's declaration of independence established its claim to sovereignty, and Ardelis formally recognized the new nation after the successful struggle. Glowhaven no longer answers to the crown; the Great Sage and the city's own institutions govern it. Its extraordinary concentration of trained mages makes an open reconquest extremely dangerous. The Ardelian crown remains resentful and pursues influence despite that legal recognition.\n\n"
        "The legend that the founders planted the Evertree together remains part of civic memory. Its exact circumstances and the tree's deeper nature remain uncertain. The academies preserve different interpretations of their founders' legacies. The exact chronology, battles and individual founding-era office holders are not established by this account.")
    w['worldLore']['Ardelis — Names and Shared Heritage']={'text':
        "Ardelis and Glowhaven share human cultural and historical roots. Local Ardelian human names use the same broad Japanese-inspired given-name/family-name convention familiar in Glowhaven, written given name first. This naming tradition does not turn Caelrath into an Edo-style city: its white-and-gold architecture, violet roofs, court dress, celestial worship, noble households and imperial institutions retain their own identity. Local fae and beastfolk can share local naming customs. Elven residents retain French-influenced Elven names and the established Elvish language. Dwarven immigrants retain their own established cultural naming and speech traditions.\n\n"
        "A name reflects the actual person's heritage. Noelle Ashford retains the name she brought from her separate nonmagical Earth; her unusual name does not identify her origin to strangers automatically. Vladimir retains his established name. Do not translate or rename foreign visitors merely because they enter Ardelis.\n\n"
        "Independence is recognized law and lived civic history. Ardelis's crown resents losing taxes, military service and the power to demand obedience. Public diplomacy, family ties and commerce continue while royal ambitions and covert projects create friction. Ardelian people have varied opinions; neither national origin nor human ancestry determines a person's politics or morality."}
    k='Ardelis — Luxury, Performance and the Underworks'
    w['worldLore'][k]['text']=w['worldLore'][k]['text'].replace("Most local human names follow the capital’s established European-style naming; foreign residents keep their own names.","Local human names follow Ardelis's shared Japanese-inspired naming tradition; Elven and foreign residents retain their own heritage.")
    # Make the existing adventurers' ordinary weapons concrete before depicting
    # them. No numerical changes, added affinity or new learned spell.
    kits={
        'Izumi Morikawa':('A blunt training halberd, a drill whistle and a padded practice coat.','Keeps a compact two-handed diagonal guard; checks range and stops a drill before a dangerous overextension.'),
        'Akito Kagetsu':('A cavalry saber, riding gloves and a dispatch case.','Uses a compact one-handed outside guard, protecting the rein hand and disengaging rather than chasing an opening blindly.'),
        'Kaede Hanamura':('A narrow fencing rapier, a padded practice jacket and a small repair roll.','Presents a controlled point on line with a compact elbow; uses precise footwork and measured counters.'),
        'Jōji Aramaki':('A service spear, a watch whistle and an ordinary key ring.','Keeps both hands on a continuous spear shaft and protects the approach with a grounded intercepting guard.'),
        'Chisato Akahoshi':('A short war pick, a hooded lantern, rope and a practical tunnel kit.','Fights close to cover with a compact outside guard, preserving space for retreat along the actual tunnel.'),
        'Kenta Hinohara':('A flanged mace, a heater shield and a practical field pack.','Angles the shield outward and keeps the mace ready beside the lower torso; favors controlled answers over reckless pursuit.'),
        'Rumi Shirato':('A shortbow, a quiver of ordinary arrows and a scout\'s field kit.','Uses a measured standing draw toward an off-center target, then relocates rather than standing exposed.'),
        'Akari Mikumo':('A ring-headed combat staff and a small spirit-investigation kit.','Uses a compact two-handed staff guard and finite learned protective practice; no uncontrolled spirit-commanding power.'),
        'Tōru Koganei':('A practical longsword, a worn scabbard and a small whetstone.','Holds a supported two-handed diagonal guard and teaches patient distance control before a committed cut.'),
        'Maho Takamizu':('A broad combat staff, a field satchel and small warding supplies.','Holds the staff low across the torso while establishing a finite protective line; keeps a clear physical exit.')}
    for name,(kit,style) in kits.items():
        n=w['npcs'][name]
        n['basicInfo']=n['basicInfo'].replace('Equipment: Well-kept tools appropriate to this trade, a small purse and practical personal belongings.','Equipment: '+kit)
        n['abilities'][0]='Combat style: '+style
    # Preserve all selected bytes and hosted URLs. Rename only workspace-bound
    # files within their verified project folders; no regeneration of majors.
    for ledger_name in ['portrait-files.json','location-files.json']:
        ledger=walk(load(ROOT/'tools/ardelis'/ledger_name),fn)
        original=load(ROOT/'tools/ardelis'/ledger_name)
        for oldkey,entry in original.items():
            newentry=ledger[fn(oldkey)];oldfile=(ROOT/entry['file']).resolve();newfile=(ROOT/newentry['file']).resolve()
            assert oldfile.is_relative_to(ROOT.resolve()) and newfile.is_relative_to(ROOT.resolve())
            if oldfile!=newfile:
                assert not newfile.exists();oldfile.rename(newfile)
        write(HERE/ledger_name,ledger)
    for name in ['portrait-urls.json','location-urls.json','area-urls.json','upload-receipts.json','placements.json']:
        write(HERE/name,walk(load(ROOT/'tools/ardelis'/name),fn))
    write(HERE/'people-manifest.json',walk(load(ROOT/'tools/ardelis/people-manifest.json'),fn))
    write(HERE/'contents.json',walk(r['contents'],fn))
    write(HERE/'combat-kits.json',kits)
    write(WORLD,w);proof(w)
    print(json.dumps({'renamed':len(mapping),'remainingPortraits':92,'kept':'Noelle, Elven names, selected portrait bytes and URLs','migration':'installed locally'},ensure_ascii=False))

def prepare():
    target=HERE/'portrait-jobs.json'
    if target.exists():return load(target)
    w=load(WORLD);m=names();fn=replacer({**m,**FAMILIES})
    manifests={n['name']:n for n in load(HERE/'people-manifest.json')}
    guide=(ROOT/'research/Portrait Creation Format.md').read_text(encoding='utf-8')
    parsed=re.findall(r'\*\*([A-Z]+\d+) — ([^*]+):\*\* ([^\n]+)',guide)
    parsed+=re.findall(r'\*\*([A-Z]+\d+) — ([^*]+)\*\*: ([^\n]+)',guide)
    poses={a:(b,c) for a,b,c in parsed}
    assert len(poses)>=70
    import random
    rng=random.SystemRandom();jobs=[]
    groups={'A':[1,6,13,17,22,30,39,45,57,65], 'W':[4,5,8,11,33,40,50,60,67,70,73,74], 'T':[9,12,20,23,24,31,36,42,44,46,47,48,49,53,56], 'P':[18,26,52,58,75], 'F':[3,15,19,25,27,32,37,38,61,64,66,76,79,83], 'D':[2,16,21,51,62,68,71], 'G':[55,63,82,91], 'L':[54,59,69,78], 'U':[7,10,28,34,43,72,80,84,90], 'S':[0,14,29,35,41,77,81,85,86,87,88,89]}
    category={i:c for c,indices in groups.items() for i in indices}
    props={'perfumer':'a single faceted scent vial','bard and rehearsal director':'an ornate lute','sewer maintenance forewoman':'a brass inspection lantern','cathedral sacristan':'a folded ceremonial cloth','hospice attendant':'a small clean dressing tray','flower seller':'a small basket of cut flowers','bell keeper':'a brass tuning fork','memorial gardener':'a single pruning tool and a fresh cutting','senior cataloguer':'a closed archival folio','aqueduct surveyor':'a brass sighting instrument','reservoir keeper':'an ordinary valve key','royal falconer':'a leather falconry glove without a bird','head gardener':'a small pruning tool','court singer':'an elegant song folio','mint assayer':'a small assay weight','instrument master':'a small bowed string instrument','crystal fitter':'a fitted violet crystal in a padded holder','observatory astronomer':'a brass astronomical sight','receiving physician':'a small medicine case','infirmary orderly':'a folded clean blanket','bathhouse attendant':'a folded towel','apothecary':'a small sealed medicine vial','fruit and preserve seller':'a glass preserve jar','garden waterkeeper':'a water-gauge tool','bookseller':'a carefully bound book','tavern keeper':'a plain drinking mug','armorer':'a fitted steel bracer','tailor':'a folded patterned fabric sample','public letter writer':'a blank folio','magitech repairer':'a small disassembled mana fitting','glassblower':'a glass vessel','fisher and net mender':'a partly mended fishing net','miller':'a modest grain scoop','orchard keeper':'a small basket of fruit','quarry supervisor':'an ordinary inspection hammer','potter and neighborhood resident':'a glazed earthenware bowl','cart repairer and Lydie\'s husband':'a wheelwright\'s measuring tool','schoolteacher':'a closed lesson book','baker':'a small loaf on a folded cloth','community kitchen organizer':'a small serving tray','smith':'a short smithing hammer','working boat skipper':'a compact coil of rope','lighthouse keeper':'a brass lamp fitting','shipwright':'a short wooden shipwright\'s mallet','customs clerk':'a closed cargo folio','salvage diver':'a compact diver\'s hood held low','cult courier posing as a devotional copyist':'an ordinary devotional folio with no secret emblem'}
    magic={
      'Arcane':'precise violet geometric motes','Metal':'small silver-metal glints on a fitting','Gravity':'two small weightless pebbles in a quiet orbit','Enchantment':'fine luminous tracery across an ordinary tool','Space':'a small clearly bounded refractive fold','Fire':'a compact amber flame flourish','Lightning':'a few fine branching electric arcs','Earth':'a few tiny hovering stone fragments','Wind':'a curling ribbon of visible pale-green airflow','Water':'a small clear stream looping beside the hand or tool','Healing':'a soft mint-gold restorative glow','Nature':'a small fresh living vine with leaves','Light':'a distinct radiant gold-white gleam','Summoning':'a tiny nonhumanoid translucent familiar silhouette','Soul':'a gentle pale-blue wisp resembling a drifting soul-lantern','Divination':'a small luminous reflection suggesting branching possibilities','Void':'a tiny bounded dark-violet absorption halo','Illusion':'a clearly translucent prismatic duplicate of a small object','Ice':'a small branching frost-crystal flourish','Sound':'fine concentric ripples of visible resonance'}
    kits=load(HERE/'combat-kits.json')
    cb={'Izumi Morikawa':['CB07','CB11'],'Akito Kagetsu':['CB03','CB11'],'Kaede Hanamura':['CB02','CB03'],'Jōji Aramaki':['CB07','CB11'],'Chisato Akahoshi':['CB03','CB11'],'Kenta Hinohara':['CB05','CB11'],'Rumi Shirato':['CB08'],'Akari Mikumo':['CB07','CB11'],'Tōru Koganei':['CB01','CB11'],'Maho Takamizu':['CB07','CB11']}
    for index,line in enumerate(l for l in (ROOT/'tools/ardelis/people.txt').read_text(encoding='utf-8').splitlines() if l and not l.startswith('#')):
        a=line.split('|');oldname,demographic,location,occupation,look,manner=a[:6];name=m.get(oldname,oldname);n=w['npcs'][name];meta=manifests[name]
        assert not n.get('portraitUrl'),'Never replace a selected valid portrait'
        age=int(re.search(r'- Age: (\d+)',n['basicInfo'])[1]);species=re.search(r'- Species: ([^\n]+)',n['basicInfo'])[1]
        prop=fn(props.get(occupation,'one small relevant ordinary work tool'))
        if name in cb:profile='adventurer';eligible=cb[name]
        elif occupation in ['magistrate','deputy envoy','watch captain','authorized transit officer','harbormaster','petition clerk','gate registrar']:
            profile='governing';eligible=['GV01','GV03','GV04','GV06','GV07']
        else:
            profile='default';cat=category[index];eligible=[p for p in poses if p.startswith(cat) and re.fullmatch(cat+r'\d\d',p)]
            if 'tool' not in prop and 'folio' not in prop:eligible=[p for p in eligible if p not in ['T02','T03','T05','U02','U05','S03']]
        draw=rng.randrange(len(eligible));pid=eligible[draw];pname,pdesc=poses[pid]
        life='a youthful fully adult elf with mature adult proportions; chronological age is not human aging' if species=='Elf' else 'an adult dwarf with a compact sturdy build' if species=='Dwarf' else f'an adult {species}, age {age}'
        effects='; '.join(f'{x}: {magic[x]}' for x in meta['affinities'])
        equipment=n['basicInfo'].split('Equipment: ')[1].split('\n\n')[0]
        prompt=(f"One premium fantasy RPG ANIME character portrait, vertical 2:3 PNG. ONE character: {name}, {n['gender']}, {life}. Identity: {n['visualDescription']} Occupation: {fn(occupation)}. Expression from personality: {fn(manner)} Ordinary equipment: {equipment} "
          f"Role profile {profile}; selected standing pose {pid} {pname}: {pdesc} Practical focal prop: {prop}. For a civilian, the prop is a work tool, not an invented weapon. For a combat profile use the actual approved weapon and this actual technique: {' '.join(n['abilities'][:1])}. "
          "STANDING CENTERED HIP-UP through the upper thighs, enough lower clothing to read the design. Full head/hair/ears/horns/hats with a clean 13.5–15% canvas-height top margin; on a 1536-high canvas the topmost hair begins about 215 pixels down. Nothing including props touches the top margin. Do not enlarge into a waist-up crop. No seated or kneeling posture. "
          f"Setting: {meta['area']}, {fn(location)}, Caelrath capital of Ardelis: connected mountain terraces, white masonry, violet roofs, gold celestial accents and cascading water. Show a recognizable occupation-specific indoor room or yard with a few fitting props. Portrait is NOT a kimono/samurai redesign: preserve the person's already authored fantasy court, trade or travel clothing despite their Japanese-inspired name. Let background remain softer than the face. "
          f"Make ALL listed affinities distinctly visible, modest in scale for ordinary residents and stronger for real adventurers: {effects}. Use these as compatible finite practice or affinity motifs without inventing extra affinities or mass attacks. Keep effects off the face. "
          "Distinctly DRAWN 2D anime face, expressive stylized eyes, simplified drawn nose and mouth, fine confident contours and colored facial shadow shapes with selective softness. Detailed illustrated clothing, hair and setting; character-specific vivid palette and natural expression, not a generic glamour smile. No realistic skin, photographic facial anatomy, sculpted face or 3D finish. Coherent two arms/two hands, natural grip, complete attached fingers. Spears/staves have ONE continuous rigid shaft through all grips, attached head, no offsets or broken sections; modest foreshortening, shaft may leave side/bottom. One named subject only, no other foreground people. Opaque appropriate clothing. No text, lettering, symbols resembling text, labels, UI, watermark, collage, gore or character sheet.")
        jobs.append(dict(name=name,oldName=oldname,profile=profile,category=category.get(index),eligible=eligible,drawnIndex=draw+1,pose=pid,poseName=pname,affinities=meta['affinities'],prompt=prompt))
    assert len(jobs)==92
    write(target,jobs);return jobs

def save(name,source):
    assert name in {j['name'] for j in prepare()}
    with selected_ledger() as ledger:
        assert name not in ledger,'One pass already saved'
        src=pathlib.Path(source);assert src.is_file() and src.suffix.lower()=='.png'
        dest=ROOT/'world-draft/npc portraits/Ardelis'/(name+'.png');assert not dest.exists()
        shutil.copy2(src,dest)
        ledger[name]=dict(file=dest.relative_to(ROOT).as_posix(),sha256=hashlib.sha256(dest.read_bytes()).hexdigest(),generationPasses=1,source=str(src))
    print(json.dumps({'saved':name,'portraits':len(ledger)},ensure_ascii=False))

def apply_urls():
    w=load(WORLD);urls=load(HERE/'portrait-urls.json');before=copy.deepcopy(w)
    ledger=load(HERE/'portrait-files.json');receipts=load(HERE/'upload-receipts.json')
    base=load(BASE);inverse={v:k for k,v in names().items()}
    assert len(ledger)==116 and set(urls)==set(ledger),'Complete the selected batch before applying URLs'
    for name,url in urls.items():
        assert name in w['npcs'];old=w['npcs'][name].get('portraitUrl')
        entry=ledger[name];receipt=receipts['NPC_PORTRAIT::'+name]
        assert receipt['sha256']==entry['sha256'] and receipt['imageUrl']==url
        assert hashlib.sha256((ROOT/entry['file']).read_bytes()).hexdigest()==entry['sha256']
        if old and old!=url:
            original=base['npcs'][inverse.get(name,name)].get('portraitUrl')
            assert entry.get('authorRequestedReplacement') and old==original,'No unapproved replacement of a valid portrait'
        w['npcs'][name]['portraitUrl']=url
    write(WORLD,w);proof(w)
    print(json.dumps({'appliedURLs':len(urls),'newPortraits':sum(not before['npcs'][n].get('portraitUrl') for n in urls)}))

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('command',choices=['migrate','prepare','save','apply']);ap.add_argument('args',nargs='*');a=ap.parse_args()
    if a.command=='migrate':migrate()
    elif a.command=='prepare':print(json.dumps({'prepared':len(prepare())}))
    elif a.command=='save':save(*a.args)
    else:apply_urls()
