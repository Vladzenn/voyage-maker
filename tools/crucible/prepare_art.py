"""Prepare reproducible one-pass portrait briefs from the actual candidate cards."""
import json,pathlib,random
ROOT=pathlib.Path(__file__).resolve().parents[2];HERE=pathlib.Path(__file__).resolve().parent
w=json.loads((ROOT/'tmp/crucible/candidate.json').read_text(encoding='utf-8'));m=json.loads((HERE/'manifest.json').read_text(encoding='utf-8'))
rng=random.Random(202611012);recent=[];out=[]
prior_path=HERE/'portrait-briefs.json'
prior={x['name']:x for x in json.loads(prior_path.read_text(encoding='utf-8'))} if prior_path.exists() else {}
done_path=HERE/'art-results.json'
done={x['name'] for x in json.loads(done_path.read_text(encoding='utf-8'))} if done_path.exists() else set()
poses={
 'CB01':'Center Guard: support the actual two-handed weapon diagonally below the chin, shoulders turned slightly against the hips.',
 'CB02':'Point on Line: present the one-handed thrusting weapon toward an off-center target with compact elbow and free hand balancing near the ribs.',
 'CB03':'Outside Ward: hold the actual cutting weapon outside the near shoulder, its point down and outward, torso slightly turned.',
 'CB04':'Heavy Low Ready: support the actual heavy weapon with both hands across the lower torso, grounded hips and relaxed bent elbows.',
 'CB05':'Shield and Answer: angle the actual shield outward beside the torso while holding the actual weapon ready with the other hand.',
 'CB06':'Paired Guard: hold one approved weapon in each hand with clearly separated guards and coherent grips.',
 'CB07':'Long-Weapon Intercept: hold the actual polearm or staff in a compact two-handed diagonal guard below the chest, shaft exiting a side or bottom.',
 'CB08':'Archer\'s Set: angle the actual bow to one side and begin a controlled modest draw with readable string hand and face; keep the bow out of top headroom.',
 'CB09':'Focus and Cast: aim the actual catalyst from lower-chest height while the free hand shapes the primary learned magic beside the torso.',
 'CB10':'Counterturn: turn hips away and shoulders toward an implied approach, actual equipment held in a compact guard; no extreme twist or crouch.',
 'CB11':'Guard Recovery: stand at the end of a controlled technique, actual equipment drawn into a stable compatible guard, cloth and fitting effect settling.',
 'CB12':'Unarmed Measure: use the actual approved gloves/handwraps, one fist or open hand forward and the other guarding the torso, poised standing weight shift.',
 'W01':'Offering Hand: offer one small actual work object near chest height, soft elbow and gentle standing forward lean.',
 'W06':'Shared-Object Presentation: support the actual small work object with both hands near the waist, shoulders turned invitingly.',
 'A05':'Point of Order: lift a finger or actual work tool beside the chest, other hand low, clear decisive standing posture.',
 'F02':'Cuff Adjustment: adjust one actual glove or sleeve cuff with the other hand in a precise standing pause.',
 'P05':'Small Display: stand with one actual small work object displayed on an open palm beside the torso, amused and confident.'}
colors={'Earth':'warm ochre stone and tiny lifted grit','Wind':'clear green-white air ribbons moving cloth','Light':'clear golden light on the actual working hand','Nature':'bright living leaf and root growth','Water':'a controlled blue water ribbon','Metal':'fine silver glints on actual metal','Ice':'clear blue frost filaments','Fire':'compact warm ember trails','Gravity':'small stones caught in a readable violet local orbit','Illusion':'a subtle false color glint, never a duplicate person','Enchantment':'fine reinforcement marks on the actual equipment','Soul':'pale blue spiritual threads around a small memorial motif','Sound':'clean visible resonant rings beside the actual tool','Lightning':'compact blue-white sparks','Arcane':'crisp cyan geometric force shapes','Void':'a small sharply bounded ink-violet shadow motif','Summoning':'a tiny harmless translucent helper motif, no second humanoid','Divination':'a faint gold constellation-like pattern on an actual small object'}
for row in m['cast']:
    name=row['name'];card=w['npcs'][name]
    if name=='Threnvoss':continue
    weapon=row['weapon'].lower();fighter=row['fighter']
    if not fighter:pool=['W01','W06','A05','F02','P05']
    elif any(x in weapon for x in ['handwrap','glove','gauntlet']):pool=['CB12','CB10','CB11']
    elif 'shield' in weapon or 'buckler' in weapon:pool=['CB05','CB10','CB11']
    elif 'pair' in weapon:pool=['CB06','CB10','CB11']
    elif 'bow' in weapon:pool=['CB08','CB11'] if 'crossbow' not in weapon else ['CB09','CB10','CB11']
    elif any(x in weapon for x in ['staff','spear','halberd']):pool=['CB01','CB07','CB10','CB11']
    elif any(x in weapon for x in ['wand','grimoire','fan']):pool=['CB09','CB10','CB11']
    elif any(x in weapon for x in ['axe','hammer','greatclub','club']):pool=['CB04','CB10','CB11']
    elif 'rapier' in weapon or 'thrusting' in weapon:pool=['CB02','CB10','CB11']
    elif 'sling' in weapon:pool=['CB10','CB11']
    else:pool=['CB03','CB10','CB11']
    eligible=[p for p in pool if p not in recent[-3:]] or pool
    pose=rng.choice(eligible);recent.append(pose)
    location=card['currentLocation']
    bg='the Eternal Crucible\'s warm ivory-stone competitor gallery, red and teal banners, golden afternoon light and the empty practice ring beyond'
    if location=='Four Sages Bazaar':bg='a colorful medieval magical bazaar counter with useful small tools, glassware, warm awnings and distant Evertree light'
    elif location=='Coppercrest Exchange':bg='an alpine dragonkin resource exchange, stone counters with amber samples, warm braziers and a snowy window'
    elif location=='Redvein Mine':bg='a snowy mountain mine office, practical timber beams, a tally board without readable text, crystal samples and warm lamplight'
    elif location=='Hearthmarket Square':bg='a bustling snowy alpine market arcade with timber stalls, wool coats and warm lanterns'
    if name in ['Nozomi Hayase','Gorō Azuma']:bg='the Crucible infirmary, clean cream curtains, green glass jars, folded cloths and warm recovery-room light'
    magic=' Primary affinity visibly suggested by '+colors.get(row['affinities'][0],'a fitting small magical motif')+'.'
    if len(row['affinities'])>1:magic+=' Secondary affinity motifs, not extra powers: '+', '.join(colors.get(a,a) for a in row['affinities'][1:])+'.'
    adult=' Show an unmistakably adult face and proportions.'
    if any(x in card['basicInfo'] for x in ['Species:** Half-elf','Species:** High Elf','Species:** Fae']):adult+=' This long-lived person looks like a youthful adult, not an elderly human; chronological age does not prescribe wrinkles.'
    prompt='Use case: illustration-story. One finished PNG vertical 2:3 fantasy RPG NPC portrait. '+('Major-character flair with a memorable silhouette and richer dramatic lighting. ' if row['major'] else 'Polished supporting cast portrait with individual lively colors. ')+card['visualDescription']+adult+' Equipment: '+row['weapon']+'. Backdrop: '+bg+'. '
    prompt+='Role profile '+('adventurer/combat-ready' if fighter else 'default/working professional')+', pose '+pose+' — '+poses[pose]+'. Expression and character: '+card['personality'][1]+'. '+magic
    prompt+=' Standing centered hip-up, visible hips and lower outfit, complete head/hair/ears/horns; 13–15 percent recognizable background above the entire head silhouette, no prop in that top band. Face and eyes are the sharp focal point. Exactly two coherent arms and hands, correct grips, no extra fingers; long weapons can leave a side/bottom edge. Unmistakable hand-drawn 2D anime: stylized expressive anime eyes and face, clean ink contours, flat-color shape design, graphic cel shading, crisp pristine fine details. No photorealism, semi-realism, lifelike skin, pores, 3D rendering or plastic surfaces. No text, lettering, names, logos, UI, borders, signature, watermark, additional people, collage or variants.'
    record=dict(name=name,prompt=prompt,pose=pose,eligible=eligible,major=row['major'],file='world-draft/npc portraits/'+name+'.png')
    out.append(prior[name] if name in done and name in prior else record)
(HERE/'portrait-briefs.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'portraits':len(out),'bossAlreadyGenerated':True,'majorPeople':sum(x['major'] for x in out)}))
