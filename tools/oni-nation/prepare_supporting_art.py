"""Prepare one accurate, randomized portrait brief per unillustrated existing NPC."""
import json,pathlib,random,re
from cast import PEOPLE,YOKAI
from build import ROOT,HERE,dump

CATEGORIES={'Atsuha Yunokawa':'W',
 'Rin Saionoma':'S','Tadayoshi Kurebayashi':'T','Mika Fuyuse':'R','Nobu Senda':'U','Akane Natsukawa':'T','Kensuke Ayahara':'W',
 'Naoe Futami':'A','Chiyo Matsukaze':'W','Tetsu Obana':'R','Fūka Suzumori':'D','Renjirō Usami':'P','Maho Kanemori':'S','Hatsu Kanesue':'T',
 'Iori Kagurazaka':'G','Yūhei Toba':'P','Natsuko Tsumura':'A','Kōichi Aratani':'U','Yae Mizuno':'L','Haru Tomisaka':'E',
 'Sachi Morisawa':'A','Kazuma Ebisawa':'R','Mina Kurusu':'G','Osamu Kariya':'F','Tae Ishihama':'E','Shunji Dobashi':'S','Ruri Nabatame':'T','Hokuto Mizusawa':'R',
 'Shizue Amakawa':'A','Dōgen Hanamori':'P','Fusa Minase':'U','Naohiro Umemoto':'T','Sana Kuroiwa':'E','Rei Tsunemori':'R','Yoriko Abe':'A',
 'Tomoe Masuda':'E','Kayo Yagiri':'S','Yasuo Natori':'L','Shin Watarai':'W','Mitsue Harada':'T','Kentarō Maeba':'U','Suzuha Hoshikawa':'S',
 'Mayu Enomoto':'W','Takuro Namiki':'T','Nene Moriyama':'A','Isao Tsuge':'D','Yumi Sawatari':'P','Gorō Fushimi':'A','Aya Takino':'S',
 'Mutsumi Hosaka':'A','Tōru Fukada':'F','Rika Ogata':'E','Kenji Morita':'W','Yōko Sanada':'E','Kae Sumida':'D','Chihiro Noda':'L','Makiya Utsugi':'R',
 'Hajime Niwa':'G','Asa Kogure':'L','Yukina Tsuribe':'P','Léonie Vauclair':'U','Jin Lin':'S','Duncan Rusk':'A','Akihisa Manabe':'T',
 'Katsuho Enoki':'W','Kohina Beppu':'S','Hiroto Sakuma':'F','Nana Saionoma':'A','Koma':'D','Suzu-no-Ura':'P'}
PALETTES=['indigo and coral with cream accents','jade and rust with gold-thread details','plum and turquoise with ivory accents','cobalt and saffron with scarlet accents','moss green and persimmon with dark brown layers','violet and pale blue with vermilion cords','crimson and teal with charcoal layers','ochre and navy with patterned cream cloth','rose and bottle green with dark red trim','sky blue and burgundy with leaf-patterned ivory cloth']
AFFINITY={
 'Arcane':'a small clean raw-mana curve hovering near an appropriate prop',
 'Fire':'a narrow controlled flame curling beside a hand or working tool',
 'Water':'a clear ribbon of water with a few separate droplets',
 'Earth':'a few small grains of earth and pebble fragments in a slow curved path',
 'Wind':'a translucent directional current stirring a sleeve or a loose ribbon',
 'Lightning':'a small branching electric arc clearly distinct from fire',
 'Ice':'a few crystalline frost petals and a short breath of cold mist',
 'Light':'a narrow luminous ray illuminating an actual detail in the scene',
 'Metal':'a few fine metallic filings following a controlled bright arc',
 'Nature':'a small living leafy shoot or curling green tendril',
 'Sound':'delicate concentric vibration ripples near a relevant object',
 'Gravity':'a few tiny objects suspended in an unusual curved orbit',
 'Void':'a clean dark shadow ribbon that absorbs some surrounding light',
 'Healing':'a gentle restorative glow around a small ordinary wrapped dressing',
 'Enchantment':'a faint luminous pattern settling into a real wearable or tool',
 'Summoning':'a small translucent summoned construct shaped like a simple origami animal',
 'Illusion':'a small playful translucent duplicate of an inanimate prop',
 'Divination':'a small reflective aura with a second glimmer suspended above it',
 'Soul':'a pale spiritlight thread winding gently around a simple charm'}

def main():
    w=json.loads((ROOT/'world-draft/WorldAlpha - World.json').read_text(encoding='utf-8'))
    draws=json.loads((HERE/'design-draws.json').read_text(encoding='utf-8'))
    guide=(ROOT/'research/Portrait Creation Format.md').read_text(encoding='utf-8')
    poses={k:d.replace('**','') for k,d in re.findall(r'- \*\*([A-Z]+\d\d) — ([^\n]+)',guide)}
    target=HERE/'supporting-portrait-briefs.json'
    old=json.loads(target.read_text(encoding='utf-8')) if target.exists() else {}
    rng=random.SystemRandom();out={};recent=[]
    for p in PEOPLE+YOKAI:
        name=p['name'];npc=w['npcs'][name]
        if npc.get('portraitUrl') and name not in old:continue
        if p['major']:continue
        if name in old:
            out[name]=old[name];recent.append(old[name]['pose'])
            if old[name]['generationStatus']!='generated' and 'CONTINUOUS WEAPON' not in out[name]['prompt']:
                out[name]['prompt']+='\nCONTINUOUS WEAPON: Any spear, staff or polearm is one straight rigid shaft with its head attached. Keep the shaft collinear through both hands and every visible section. No accidental break, bend, offset, missing length or floating section. A hand may hide a small section, but its two visible ends must align.'
            continue
        role=p.get('role','unique yokai');weapon=p.get('weapon','');low=role.lower()
        if name in ['Koma','Suzu-no-Ura']:
            pool=['SPECIAL01','SPECIAL02'];profile='special anatomy';activity='Show this specific nonhuman inhabitant in its established place, with the exact anatomy and expressive character in the card.'
        elif any(t in low for t in ['adventurer','rōnin','archer','spear escort','shinobi','sword instructor','spear teacher','archery instructor','watch officer']):
            profile='adventurer';activity='Show the actual approved weapon drawn and in a stable ready stance, with its correct real grip and more prominent ability-consistent effects. No opponent is needed.'
            if 'bow' in weapon:pool=['CB08','CB11']
            elif 'shield' in weapon:pool=['CB05']
            elif any(t in weapon for t in ['staff','spear','naginata']):pool=['CB01','CB07','CB11']
            elif any(t in weapon for t in ['wand','focus']):pool=['CB09']
            elif not weapon:pool=['CB12']
            else:pool=['CB03','CB10','CB11']
        elif any(t in low for t in ['magistrate','advocate','captain of','branch master','headman']):
            profile='governing';pool=['GV01','GV02','GV03','GV05','GV06'];activity='Show a particular listening, negotiating or explaining moment in their real remit, standing at an appropriate work rail. One relevant office prop; no invented crown, throne or extra jurisdiction.'
        else:
            profile='default';cat=CATEGORIES.get(name,'F');pool=[cat+str(i).zfill(2) for i in range(1,7)]
            # Avoid gestures that imply books/tools not suited to the actual scene.
            if cat=='T' and not any(t in low for t in ['teacher','archive','research','clerk','keeper','surveyor','specialist','physician']):pool=['T01','T03','T04','T06']
            activity='A specific ordinary moment in their own work or social life. Their face and actual personality matter more than generic glamour or battle spectacle. Keep any desk at the side or low enough to reveal hips.'
        filtered=[x for x in pool if x not in recent[-3:]] or pool
        index=rng.randrange(len(filtered));pose=filtered[index];recent.append(pose)
        pose_desc=poses.get(pose,'A centered, coherent upright nonhuman silhouette turned slightly toward a nearby sound, with the characteristic face fully readable.' if pose=='SPECIAL01' else 'A centered upright nonhuman silhouette presenting one actual small prop with a playful head tilt; preserve exact creature anatomy.')
        category=CATEGORIES.get(name,'role pool')
        palette=rng.choice(PALETTES)
        apparel=f'Role-appropriate layered Japanese-inspired daily clothing in {palette}, with one individual textile pattern; practical construction appropriate to {role}. Keep the clothing specific and colorful, without giving a common worker court regalia.'
        if name=='Léonie Vauclair':apparel=f'A traveling elven buyer’s carefully tailored coat and practical specimen satchel in {palette}; understated foreign cut, immaculate boots implied below frame.'
        if name=='Jin Lin':apparel=f'A brilliantly patterned Yunhai traveling merchant jacket in {palette}, fitted to the bird-beastfolk anatomy stated in the card, with a small mechanism case.'
        if name=='Duncan Rusk':apparel=f'A sturdy dwarven metalworker’s coat and leather apron in {palette}, the actual tall hat he enjoys, broad shoulders and substantial braided beard.'
        species=p['species'];anatomy='An adult '+species.lower()+'. '+p['look']+'.'
        if species=='Oni':anatomy+=' Human face and human body with ONLY the specified Oni horns; no dragon tail or scales, no monster muzzle, no generic demon wings.'
        if species in ['Fae','High Elf']:anatomy+=' Long-lived adult: youthful adult face and fully adult proportions, not an elderly human age conversion and not a child. Keep the exact stated wings, antlers, scales, ear shape and height when present.'
        if species=='Human':anatomy+=' Human ears and no invented horns, wings, tail or pointed elven ears.'
        if name=='Koma':apparel='His approved patched saffron coat and absurdly large folded reed hat, held below head height. Chestnut fur, dark raccoon mask, amber eyes, upright animal posture and a fluffy tail; no human face.'
        if name=='Suzu-no-Ura':apparel='No human outfit. The source description supplies the bell body, cord legs and actual little face; preserve those exactly. It is a unique animated bell, not a human holding a bell.'
        aff=draws[name]['affinities'];effects='; '.join(a+': '+AFFINITY[a] for a in aff)
        native=name not in ['Léonie Vauclair','Jin Lin','Duncan Rusk','Akihisa Manabe']
        local='Use flowing translucent forms, tapered brushlike edges and graceful directional motion for this local technique, while keeping every discipline recognizable and vivid.' if native else 'Use the character’s own learned technique and travel background; do not force the native regional effect profile on this foreign visitor.'
        expression=p['public']+' '+p.get('voice','')
        setting=w['locations'][p['place']]['basicInfo'].split(' Nearby routes')[0]
        prompt=f'''Use case: stylized-concept. Asset: ONE finished NPC portrait PNG for {name} in The Schools of Magic, Arise!
SUBJECT: {npc['visualDescription']}
ANATOMY / ADULT LIFE STAGE: {anatomy}
CLOTHING: {apparel}
PERSONALITY / EXPRESSION: {expression} Let that demeanor determine the expression; do not automatically smile.
ROLE PROFILE: {profile}. {activity}
RANDOMIZED POSE: {category}, {pose} — {pose_desc} All humanoids are STANDING, not seated or kneeling. Keep actual prop and hand mechanics coherent. EQUIPMENT / METHOD: {weapon}. {p['method']}
AFFINITIES, ALL VISIBLE: {effects}. Show each listed affinity in a distinct fitting minor effect, motif or real environmental interaction. Ordinary residents have everyday control, not unearned powerful spells. {local}
ACTUAL BACKGROUND: {p['place']}. {setting} Use two or three distinctive spatial cues; keep the face sharpest and the setting less dominant.
RENDERING: polished colorful unmistakably TWO-DIMENSIONAL fantasy ANIME illustration, crisp deliberate lines, graphic cel shadows, stylized anime face, expressive eyes and detailed fabric. Rich varied colors and scene-specific lighting, not a mandatory warm grade. NO photorealism, realistic facial anatomy, semi-realism, skin pores, plastic or 3D shading.
MANDATORY COMPOSITION: upright vertical 2:3. Centered HIP-UP humanoid portrait with waist and full hip line readable. The COMPLETE highest hair, horn, hat or ear point begins at 15% of image height BELOW the top edge: about y=230 on a 1536-tall canvas. Preserve a clean 12.5–15% top margin (up to 17% if necessary). Show background in that top band; NEVER crop or touch the top with the head silhouette or a prop. Do NOT zoom in to fill the band. Keep the face readable and hands below the face; exactly two attached arms and two hands for humanoids. For the named nonhuman bell or tanuki, adapt the body crop to real anatomy but keep vertical format and full upper silhouette with the same headroom.
OUTPUT: ONE portrait, no other people, no panels, collage or character sheet. NO text, writing, labels, lettering, logo, watermark, frame, signature or UI.'''
        out[name]={'name':name,'profile':profile,'category':category,'eligiblePoses':filtered,'drawnIndex':index+1,'pose':pose,'prompt':prompt,'target':f'world-draft/npc portraits/Akitsuhara/{name}.png','generationStatus':'not-started','callsAuthorized':1}
    for name,entry in out.items():
        if entry['generationStatus']!='generated' and 'CONTINUOUS WEAPON' not in entry['prompt']:
            entry['prompt']+='\nCONTINUOUS WEAPON: Any spear, staff or polearm is one straight rigid shaft with its head attached. Keep the shaft collinear through both hands and every visible section. No accidental break, bend, offset, missing length or floating section.'
    assert len(out)==83,len(out)
    dump(target,out);dump(HERE/'supporting-portrait-selection.json',list(out))
    print(json.dumps({'portraits':len(out),'names':list(out)},ensure_ascii=False))

if __name__=='__main__':main()
