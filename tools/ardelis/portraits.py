"""Prepare one-pass briefs and preserve named image outputs; generation uses imagegen."""
import argparse, hashlib, json, pathlib, random, re, shutil, sys
HERE=pathlib.Path(__file__).resolve().parent;ROOT=HERE.parents[1]
sys.path.insert(0,str(ROOT/'tools'));import project
FOLDER=ROOT/'world-draft/npc portraits/Ardelis'
def prepare():
    target=HERE/'portrait-jobs.json'
    if target.exists():return project.load(target)
    w=project.load(ROOT/'output/ardelis-2026-11-05/The Schools of Magic, Arise! - Ardelis.json')
    seeds=[json.loads(l) for f in ['major-people.jsonl','paladins.jsonl'] for l in (HERE/f).read_text(encoding='utf-8').splitlines() if l]
    manifest={n['name']:n for n in project.load(HERE/'people-manifest.json')}
    guide=(ROOT/'research/Portrait Creation Format.md').read_text(encoding='utf-8')
    poses={m[0]:(m[1],m[2]) for m in re.findall(r'\*\*([A-Z]+\d+) — ([^*]+):\*\* ([^\n]+)',guide)}
    if not poses: # The heading's closing bold marker precedes the colon.
        poses={m[0]:(m[1],m[2]) for m in re.findall(r'\*\*([A-Z]+\d+) — ([^*]+)\*\*: ([^\n]+)',guide)}
    rng=random.SystemRandom();jobs=[];recent=[]
    for n in seeds:
        name=n['name'];card=w['npcs'][name]
        combat=name in ['Lysandra Aurevain','Noelle Ashford','Corvin Hale','Nerissa Vale','Aurélian Vauss','Séraphine Duvray','Osmond Verain']
        if name=='Thaurivex':profile='special anatomy';eligible=['SPECIAL'];poses['SPECIAL']=('Suspended Sovereign','A vertical composition of one suspended brass-and-ivory articulated construct, with its complete crown-like head and shoulders separated from the lower rings, a readable central vessel and no duplicate bodies.')
        elif combat:
            profile='adventurer / combat ready'
            eligible=['CB07','CB11'] if name in ['Nerissa Vale','Séraphine Duvray','Osmond Verain'] else ['CB05','CB11'] if name in ['Aurélian Vauss','Corvin Hale'] else ['CB02','CB03','CB11'] if name=='Lysandra Aurevain' else ['CB09','CB10']
        elif name in ['Marielle Aurevain','Céleste Aurevain','Noelle Ashford','Sabine Mauclerc','Coralie Brissot']:
            profile='default / individual work';eligible=['A01','A03','W06','R04']
        else:profile='governing / actual work';eligible=['GV01','GV03','GV04','GV05','GV06','GV07']
        eligible=[p for p in eligible if p in poses and p not in recent[-3:]] or [p for p in poses if p.startswith('GV')]
        assert eligible
        i=rng.randrange(len(eligible));chosen=eligible[i];recent.append(chosen);pname,pdesc=poses[chosen]
        affinity=manifest[name]['affinities']
        if name=='Noelle Ashford':magic='She has these twenty public affinities, shown as small distinct abstract magical fragments around her finite focus, not simultaneous attacks: '+', '.join(affinity)+'. Keep her face unobscured. No Time magic.'
        else:magic='Make ALL her/his listed affinities visibly recognizable with distinctive compatible magic or material motifs: '+', '.join(affinity)+'. Effects stay beside or below the face, appropriate to the actual finite technique.'
        expression='Expression and attitude: '+n['temperament'][0]
        prompt=f"One finished premium fantasy RPG ANIME character portrait, vertical 2:3 PNG. ONE adult character: {name}. {n['look']} Equipment: {n['equipment']} {expression} Role profile: {profile}; randomly selected pose {chosen} {pname}: {pdesc} Standing hip-up, hips and enough upper thighs/clothing visible, character centered. Place the COMPLETE head/hair/horns/adornments silhouette 13.5% below the top edge; clear 12.5–15% headroom, nothing including props intrudes into that upper margin. No seated portrait. Setting: {manifest[name]['area']} in Caelrath, Ardelis. A connected mountain-terrace city of white masonry, violet roofs, gold celestial decoration and cascading water; use appropriate actual indoor work room or outdoor yard, softer and less dominant than the character. {magic} Major character presentation: memorable silhouette, expressive lighting, vivid affinity effects and rich costume detail; avoid a generic smiling pose or repeated warm palette. Clearly DRAWN ANIME face, expressive stylized eyes, simple drawn nose and mouth, clean colored facial shadow shapes with selective softness. Intricate illustrated clothing, hair and background, distinctly 2D. No realistic facial planes, pores, photorealism, semi-realism, plastic or 3D render. Coherent adult anatomy, two arms and hands for humanoids, natural grip, intact weapons: spear/staff has ONE continuous rigid shaft aligned through all hands, attached head, no offset broken pieces, moderate broadside perspective; let lower end leave the side/bottom if needed. Opaque appropriate clothing, no other foreground people, no gore. No lettering, labels, UI, watermark, collage or character sheet. {n['combat']}"
        jobs.append(dict(name=name,prompt=prompt,profile=profile,eligible=eligible,drawnIndex=i+1,pose=chosen,poseName=pname,affinities=affinity))
    project.write_json(target,jobs);return jobs
def save(name,source):
    assert name in [n['name'] for n in prepare()]+["Valkazathoth'dmir"]
    source=pathlib.Path(source);assert source.is_file() and source.suffix=='.png'
    FOLDER.mkdir(parents=True,exist_ok=True);dest=FOLDER/(name+'.png')
    assert not dest.exists(),'One-pass result already saved; do not overwrite silently.'
    shutil.copy2(source,dest)
    p=HERE/'portrait-files.json';ledger=project.load(p) if p.exists() else {}
    ledger[name]=dict(file=str(dest.relative_to(ROOT)).replace('\\','/'),sha256=hashlib.sha256(dest.read_bytes()).hexdigest(),generationPasses=1,source=str(source))
    project.write_json(p,ledger);print(json.dumps({'name':name,'saved':str(dest)},ensure_ascii=False))
if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--save',nargs=2);args=a.parse_args()
    if args.save:save(*args.save)
    else:print(json.dumps({'prepared':len(prepare())}))
