"""Produce reviewable, one-pass portrait briefs from the actual candidate cards."""
import json,pathlib,random,re
from cast import PEOPLE,YOKAI
from build import ROOT,HERE,dump

POSES={}
guide=(ROOT/'research/Portrait Creation Format.md').read_text(encoding='utf-8')
for code,description in re.findall(r'- \*\*([A-Z]+\d\d) — ([^\n]+)',guide):
    POSES[code]=description.replace('**','')

def main():
    world=json.loads((ROOT/'output/oni-nation-2026-11-02/Akitsuhara - Candidate.json').read_text(encoding='utf-8'))
    draws=json.loads((HERE/'design-draws.json').read_text(encoding='utf-8'))
    existing_path=HERE/'portrait-briefs.json'
    previous=json.loads(existing_path.read_text(encoding='utf-8')) if existing_path.exists() else {}
    prompts=[];rng=random.SystemRandom()
    for p in PEOPLE+YOKAI:
        if not p['major']:continue
        name=p['name'];npc=world['npcs'][name]
        if name in ['Shōen Kagetsuna','Masazane Saionoma','Kureha Tsubakiri','Shigure Tsubakiri']:
            eligible=['GV01','GV02','GV03','GV04','GV05','GV06'];activity='Show this official handling an actual petition, negotiation or decision while STANDING at a rail or standing-height table. Weapon remains secondary or sheathed. No automatic throne or crown.'
        elif name in ['Ayame Kagetsuna','Tōma Sagiri','Yuzuri Kageura','Renga Itsuzaki']:
            eligible=['CB01','CB04','CB07','CB11'] if name in ['Ayame Kagetsuna','Renga Itsuzaki'] else ['CB01','CB03','CB10','CB11'] if name=='Tōma Sagiri' else ['CB03','CB10','CB11']
            activity='Show the actual approved weapon DRAWN in a mechanically coherent combat-ready standing stance, preserving hand identity, leverage and a readable face. The weapon is not a decorative sheathed prop.'
        elif name=='Kinu Amakusa':eligible=['D01','D02','D03','D04','D05','D06'];activity='A confident standing performer with her actual reinforced dance fans, vivid costume and controlled flowing fire; no audience member steals the focus.'
        elif name=='Genzaburō Kanemori':eligible=['T01','T02','T03','T04','T05','T06'];activity='A master smith STANDING at his actual forge work, tool hammer held low and purposeful; a character portrait, not a close-up of a hand or a seated craftsman.'
        elif name in ['Hagire','Oroha']:eligible=['SPECIAL01','SPECIAL02'];activity='Use the closest coherent standing body portrait for this exact unusual anatomy. Do not humanize an animal or invent limbs. Retain a complete upper silhouette with generous headroom and a readable characteristic face.'
        else:eligible=['W01','W02','W03','W04','W05','W06'];activity='A warm or knowing standing interaction fitted to this actual character and work. Keep any desk low or to the side; show the hips and the actual outfit.'
        pose=previous.get(name,{}).get('pose') or rng.choice(eligible)
        if pose.startswith('SPECIAL'):pose_desc='A centered standing silhouette, turned slightly toward an implied nearby sound.' if pose.endswith('01') else 'A centered standing silhouette with the head turned back toward the viewer and the body held naturally.'
        else:pose_desc=POSES.get(pose,pose)
        aff=', '.join(draws[name]['affinities'])
        secret_exception='Do NOT show the concealed articulated prototype, secret allegiance or private land scheme. His public sword and one modest mechanism fitting are enough.' if name=='Shigure Tsubakiri' else ''
        setting=world['locations'][p['place']]['basicInfo']
        anatomy='The source card supplies all anatomy. An Oni is human-faced with the specified horns, NOT a full dragon or generic demon.'
        if name=='Hagire':anatomy='A disturbing adult woman-shaped forest beast, extremely tall and lanky, exactly TWO arms and TWO legs. The altered joint anatomy is intentional: one elbow can be unseated at an uncanny angle, while the other limbs remain clearly attached. Ragged split mouth and uneven teeth are visible without gore. No extra hands, spider legs or heroic human beauty makeover.'
        if name=='Oroha':anatomy='An immense intelligent CRANE SPIRIT: bird head, beak, long neck, exactly two feathered wings and two long bird legs. White plumage, black neck stripe and crimson crown. No human torso, human arms, Oni horns or humanoid face. Show its head, neck and substantial wing/body silhouette; a coherent bird portrait replaces a literal human hip crop.'
        prompt=f'''Create ONE finished upright 2:3 PNG fantasy-anime portrait for {name}, a major character in The Schools of Magic, Arise!\nIDENTITY: {npc['visualDescription']}\nPERSONALITY AND ACTIVITY: {p['public']} {activity}\nEQUIPMENT / METHOD: {p.get('weapon','')} {p['method']} {secret_exception}\nANATOMY: {anatomy}\nPOSE: {pose} — {pose_desc}\nAFFINITIES: {aff}. Make every listed affinity visibly recognizable through ability-consistent magic or a fitting distinct motif; do not give unlearned large powers to a desk worker. For these native techniques favor vivid, flowing translucent forms, tapered brushlike edges and graceful motion, with less hard glitter or crystalline sparkle unless intrinsic to the discipline. Strong combat effects can remain spectacular and should be clear.\nSETTING: {p['place']}. {setting} Pick a few characteristic spatial details; keep the background less dominant than the person. It must be an actual place, not a symbolic collage.\nRENDERING: our established polished colorful TWO-DIMENSIONAL fantasy-anime illustration. Clearly stylized anime face, crisp deliberate lines, graphic cel shadows, beautiful fabric and controlled luminous magic. Rich varied outfit colors and patterns; scene-appropriate lighting, NO imposed warm or muted palette. A major portrait should have memorable presence, expressive staging and well-chosen magical flair. No realistic face, pores, photographic skin, semirealism, plastic shading or 3D rendering.\nCOMPOSITION: centered standing HIP-UP portrait for humanoids, with waist, full hip line and upper lower-garment visible. Put the TOP of the COMPLETE hair/horns/crown silhouette about 14% below the top edge, leaving a clean 12.5–15% top margin (up to 17%, never less). This margin is above the highest part of the character, not merely above the eyes. Do not zoom in or crop hair, horns, head adornments, ears or the top of the head. Keep weapons and hands below the reserved top band. Readable eyes and face, coherent hands and shoulder attachment.\nOUTPUT: one finished image only, no collage or sheet. NO writing, calligraphy, labels, signature, watermark, border or UI.'''
        prompts.append({'name':name,'pose':pose,'eligiblePoses':eligible,'prompt':prompt,'target':f'world-draft/npc portraits/Akitsuhara/{name}.png','callsAuthorized':1,'generationStatus':'not-started'})
    dump(HERE/'portrait-briefs.json',{r['name']:r for r in prompts})
    dump(HERE/'portrait-selection.json',[r['name'] for r in prompts])
    print(json.dumps({'portraits':len(prompts),'poses':[r['pose'] for r in prompts]}))

if __name__=='__main__':main()
