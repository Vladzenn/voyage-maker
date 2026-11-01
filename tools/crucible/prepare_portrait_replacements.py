"""Prepare the explicitly requested ten replacement briefs; no image API calls."""
import json
import random
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'output/champions-of-the-crucible/portrait-replacements'
POSES = {
 'CB01': 'Center Guard: a supported two-handed diagonal weapon guard below the chin, shoulders slightly counterturned against the hips.',
 'CB04': 'Heavy Low Ready: support the weapon with both hands across the lower torso, elbows bent and shoulders grounded.',
 'CB05': 'Shield and Answer: angle the shield beside the torso and keep the drawn sword ready in the other hand; face unobscured.',
 'CB07': 'Long-Weapon Intercept: compact two-handed diagonal staff or spear guard across the lower torso, shaft continuing through a side edge.',
 'CB10': 'Counterturn: standing hip shift away from an implied attack, shoulders returning toward it, weapon in a compact counterguard.',
 'CB11': 'Guard Recovery: standing at the end of a controlled technique, recovering the weapon into a stable guard with an effect trail settling.',
 'CB12': 'Unarmed Measure: one fist forward, the other guarding the ribs, shoulders and hips indicating a grounded boxing weight shift.',
 'F01': 'At Attention: upright, composed standing posture, hands naturally lowered beside the waist.',
 'F02': 'Glove Adjustment: straighten the cuff of the opposite glove, back upright and weight even.',
 'F05': 'Instructor Stop: one open palm at lower chest height, the other hand low, conveying a restrained request to wait.',
}
ROWS = [
 ('Daichi Kawanobe', ['CB12','CB10','CB11'], 'adventurer',
  'A forty-year-old human man, lean but work-hardened, close-cropped black hair with a slightly unruly forelock, hazel eyes, strong brows, clean-shaven angular anime face. Ochre-gold short travel coat with navy cuffs and lining over a cream open-collar shirt; reinforced navy handwraps. Confident but a little impatient.',
  'Unarmed boxer; bare wrapped fists, no weapon. Earth magic: several angular stone fragments and a glowing ochre ground-bracing pattern rise around his lower forearms and hip line, a visibly directed earthy force rather than a huge explosion.',
  'Sunlit Crucible practice gallery, pale stone arcade and hanging warm-colored banners.'),
 ('Daisuke Kariya', ['CB01','CB04','CB11'], 'adventurer',
  'A thirty-two-year-old sturdy human dockworker, rough brown undercut, dark green eyes, short brown beard, broad shoulders. Cobalt-blue long work coat with tan lapels, rolled sleeves, leather belts over a cream shirt. Watchful, stubborn expression.',
  'One broad work axe, coherent two-handed grip. Show all three affinities at modest level-ten scale: Earth as a few orbiting stone chips, Metal as bright silver filings aligned along the steel axe head, Void as a narrow dark violet crescent absorbing light behind the blade. Effects remain below his face.',
  'Crucible stone arena, distant red and teal banners and a sunlit practice boundary.'),
 ('Eita Kuroda', ['CB10','CB11','CB04'], 'adventurer',
  'A twenty-seven-year-old sturdy human man, black hair shaved at the sides and swept over on top, gray eyes, short dark stubble. Forest-green tailored travel jacket with brass trim, fitted black shirt, dark leather belts and wrist guards. A self-assured challenging look; visibly enjoys dressing well.',
  'One short chain-linked club, the chain held compactly between his two hands with the club head beside his hip. Metal magic visibly stiffens several links into a bright silver arc; thin metallic particles gather in orderly luminous bands around the links. Small controlled beginner effect, not lightning.',
  'Crucible competitor passage opening onto a golden stone practice court.'),
 ('Genta Shishido', ['F01','F02','F05'], 'default',
  'A mature but vigorous adult male dragonkin, ninety-one years in a two-hundred-year species lifespan. Human face, iron-gray cropped crest of hair, green vertical-slit eyes, russet scales along cheekbones and arm backs, human palms, swept-back curved horns, a thick russet dragon tail. Neat brown waistcoat, cream shirt, brown work gloves. Wary, tightly polite expression.',
  'His heavy climbing pick hangs recognizably at his belt below chest level; no axe raised overhead. Earth affinity appears as three distinct small rough crystal-bearing rock samples floating beside the lower hand with amber earthen light and dust motes. This is controlled mineral handling at work, not a battle barrage.',
  'Redvein Mine surface office in snowy Drakenspire, warm wooden beams, sample trays and a window onto snowy mountain roofs; all ledger marks unreadable.'),
 ('Haruna Yashima', ['CB01','CB07','CB11'], 'adventurer',
  'An adult forty-four-year-old Oni woman, compact athletic build, warm human skin, two short ridged horns, crimson anime eyes, plum-purple hair in a long loose braid. Mint-green travel jacket worn open over a fitted black sleeveless top, charcoal trousers, practical belt and dark wristguards. A knowing, mildly provocative half-smile.',
  'One double-ended blade, long central grip held with two hands across the waist, each blade pointing outward to a side below shoulder level. Soul magic appears as distinct silver-violet spirit threads wrapped along the blade and a few small floating will-o-wisps beside the lower torso. No summoned human, extra face, skull pile or extra weapon.',
  'Crucible training court beneath pale stone arches, soft sun and mint/ochre banners.'),
 ('Kenta Ishizaki', ['CB01','CB04','CB11'], 'adventurer',
  'An adult thirty-seven-year-old male dwarf, short sturdy compact proportions and broad shoulders, dark auburn braided hair, a neat short braided auburn beard, amber anime eyes, a warm but competitive squint. Terracotta work coat with cream embroidered trim, leather shoulder guards and belts. Keep dwarf proportions, not a tall human.',
  'One compact war hammer in a mechanically coherent two-handed low guard. Metal affinity visibly reinforces its actual metal head with thin bright steel-colored geometric bands and a controlled orbit of tiny silver filings. Broad readable hammer head, straight handle, no deformed axe and no gigantic explosion.',
  'Crucible practice gallery with sandstone pillars, blurred equipment racks and cheerful daylight.'),
 ('Kōta Mibu', ['CB01','CB07','CB11'], 'adventurer',
  'A nineteen-year-old adult human man with a lean build, unevenly cropped russet hair, green anime eyes and an earnest slightly nervous grin. Terracotta and cream practical beginner training coat, dark undershirt, leather bracers and a plain belt. Clearly a young adult.',
  'One short ash-wood spear, simple steel point, two hands correctly spaced on its wooden shaft in a beginner guard. Earth affinity is visibly present as three small tile-like stone chips suspended beside the spear and a warm ochre brace line at the lower waist. Modest level-one magic, intimate and clear, no giant rocks or devastation.',
  'Crucible beginner practice court, low sandstone balustrade, distant colorful pennants and open blue sky.'),
 ('Masato Oda', ['CB10','CB11'], 'adventurer',
  'A twenty-three-year-old adult human parcel runner, sturdy build, soft tousled dark-blue hair, hazel anime eyes, clean-shaven face and a hesitant thoughtful expression. Cobalt and tan travel jacket over a cream shirt, delivery satchel at the hip, worn leather wrist guards.',
  'One ordinary leather sling held in a sensible compact sling stance, cord and loaded pouch readable and not tangled. Light affinity manifests as a small brilliant golden mote around the loaded pebble and a clean crescent of warm light tracing the sling motion beside the torso. Small level-two spell effect; no laser cannon, bow or sword.',
  'Crucible concourse opening onto a practice ring, warm sandstone, teal banners and afternoon sunlight.'),
 ('Ranmaru Tōdō', ['CB12','CB10','CB11'], 'adventurer',
  'An experienced fifty-five-year-old adult human household champion, lean trained build, black hair with silver temples tied high, emerald anime eyes, faint mature facial lines and dignified pride. Ochre-gold and navy fitted training jacket, cream collar, pair of articulated steel gauntlets. Mature handsome anime face, not a twenty-year-old.',
  'Unarmed gauntlet fighter, one open armored hand forward and the other near the ribs. Enchantment affinity appears as crisp luminous violet-gold reinforcement bands fitted closely to his actual gauntlets and forearms, with small angular runic light shapes without readable lettering. Elegant controlled technique, no extra weapon or disembodied fists.',
  'Crucible practice gallery, lacquered weapon racks, an understated small flower arrangement on a distant bench and shafts of sun.'),
 ('Seiji Makabe', ['CB05','CB10','CB11'], 'adventurer',
  'A fifty-one-year-old adult human guard trainer with a sturdy build, short steel-gray hair, brown anime eyes, faint age lines, square clean-shaven jaw and a patient stern expression. Cobalt-blue coat with tan panels, cream shirt, strong leather straps and brown bracers.',
  'One broad sword and one kite shield, correct single grip for each, shield angled outside the torso and sword held ready below the face. Earth affinity raises a few clearly defined rough stone plates beside the shield rim and an ochre bracing glow around the lower arm. No giant wall, no metal or lightning spell.',
  'Crucible training arena, pale stone walls, soft colored pennants and warm daylight.'),
]

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--extend-roster',action='store_true');args=parser.parse_args()
 OUT.mkdir(parents=True,exist_ok=True)
 if args.extend_roster:
  extend_roster();return
 rng=random.SystemRandom(); recent=[]; rows=[]
 for name,pool,role,identity,effect,scene in ROWS:
  eligible=[p for p in pool if p not in recent[-3:]] or pool
  index=rng.randrange(len(eligible)); pose=eligible[index]; recent.append(pose)
  prompt=(f'Create ONE brand-new PNG character portrait of {name} for a colorful fantasy-anime RPG gallery. '
   'Upright vertical 2:3 canvas. Crisp pristine 2D anime illustration: deliberate clean linework, stylized expressive anime face and eyes, graphic cel-shaded light, sharply drawn hair and clothes. '
   'Composition is important: centered STANDING HIP-UP figure. The topmost hair OR HORN begins 15 percent down the image; on a 1536-high canvas that is y=230. Reserve the upper 12.5–15 percent as open background above the complete silhouette. '
   'No hair, horn, weapon, hand, effect or foreground prop enters that reserved band. Do not zoom closer to fill it. Show hips and enough outfit at the bottom; entire head and horns in frame, face sharp and uncovered. '
   f'Identity and clothing: {identity} Role profile: {role}. Uniformly drawn pose {pose}: {POSES[pose]} '
   f'Equipment and affinity visibility: {effect} Background: {scene} '
   'Keep the person most prominent, background softer, effects bright and clearly recognizable but separated from face and hands. Anatomically coherent two arms and two hands only, sensible grip and wrist direction, no fused fingers. '
   'No text, letters, labels, logo, signature, border, UI, collage or extra person. No realism, semi-realism, photographic skin, skin pores, live-action facial anatomy, 3D render or painterly blurred edges. '
   'Preserve an appealing expressive 2D anime finish with clear top headroom and clearly visible character-appropriate magic.')
  rows.append(dict(name=name,profile=role,eligible=eligible,drawnIndex=index+1,pose=pose,prompt=prompt,file=f'world-draft/npc portraits/{name}.png',generationMode='built-in image_gen; one fresh pass authorized 2026-11-02'))
 (OUT/'Prompts and Pose Draws.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print(json.dumps([{'name':r['name'],'pose':r['pose']} for r in rows],ensure_ascii=False))

def extend_roster():
 p=OUT/'Prompts and Pose Draws.json';rows=json.loads(p.read_text(encoding='utf-8'))
 world=json.loads((ROOT/'world-draft/WorldAlpha - World.json').read_text(encoding='utf-8'))
 manifest=json.loads((ROOT/'tools/crucible/manifest.json').read_text(encoding='utf-8'))
 effects={
  'Arcane':'cyan geometric mana panels and a short luminous line of raw mana',
  'Fire':'a vivid controlled ribbon of flame along the actual weapon or beside the lower hand',
  'Water':'a clear curling ribbon of blue water with individually drawn droplets',
  'Earth':'small angular rough stones and ochre ground-bracing light below the torso',
  'Wind':'distinct pale turquoise curved air currents bending a sleeve or loose ribbon',
  'Lightning':'a few crisp branching blue-gold electrical arcs beside the approved weapon',
  'Ice':'a small hovering faceted ice screen with bright frost crystals',
  'Light':'a clean golden-white light arc and a concentrated star-like glint',
  'Metal':'bright silver filings arranged into thin curved bands around real metal',
  'Nature':'a small living vine with bright leaves curling below the hands',
  'Sound':'clearly visible concentric violet-gold vibration rings from the tool or weapon',
  'Gravity':'several tiny stones held in a distinct circular orbit with bent violet light',
  'Void':'a narrow dark violet light-absorbing crescent with a sharp luminous rim',
  'Healing':'a gentle luminous green restorative weave around a small clean bandage or palm',
  'Enchantment':'fitted golden-violet reinforcement patterns on the real equipment, no readable letters',
  'Summoning':'one tiny translucent moth-like geometric familiar below shoulder height',
  'Illusion':'a small prismatic floating mirror mote reflecting a displaced patch of the background',
  'Divination':'a translucent star-map lens floating beside the lower hand, no lettering',
  'Soul':'a few silver-lilac will-o-wisps and fine luminous spirit threads',
 }
 rng=random.SystemRandom();recent=[r['pose'] for r in rows[-3:]]
 for name in manifest['npcs']:
  if any(r['name']==name for r in rows):continue
  n=world['npcs'][name];fighter=name in [x['name'] for x in manifest['roster']][:32]
  affinity=n['basicInfo'].split('**Magic affinity:** ')[1].split('\n')[0].split(', ')
  if fighter:
   weapon=next(x['weapon'] for x in manifest['cast'] if x['name']==name)
   low=weapon.lower()
   pool=['CB01','CB04','CB11'] if any(x in low for x in ['axe','hammer','greatclub']) else ['CB07','CB11','CB01'] if any(x in low for x in ['staff','spear','halberd','scythe']) else ['CB10','CB11']
   if any(x in low for x in ['rapier','thrusting','dagger','saber','sword']):pool=['CB10','CB11']
   if 'shield' in low or 'buckler' in low:pool=['CB05','CB10','CB11']
   if any(x in low for x in ['gauntlet','glove','handwrap']):pool=['CB12','CB10','CB11']
   role='adventurer';category='CB'
  else:
   weapon='the actual work equipment stated below';pool=['F01','F02','F05'];role='default';category='formal at work'
  eligible=[x for x in pool if x not in recent[-3:]] or pool
  i=rng.randrange(len(eligible));pose=eligible[i];recent.append(pose)
  if name=='Threnvoss':
   role='special nonhumanoid dungeon boss';pose='CB07';eligible=['CB07'];i=0
  cues={
   'Shun Kurebayashi':'A pleased, insinuating smile: he knows gossip that might embarrass somebody.',
   'Yae Mitsuhara':'A cool appraising look; she enjoys having the last word.',
   'Riko Narumi':'A sharp, impatient look at an imperfect technique.',
   'Haruto Otsuki':'An attentive but intrusive, calculating half-smile.',
   'Midori Hozumi':'A theatrical competitive grin, eager for attention.',
   'Kojirō Tsunematsu':'Insufferably superior, chin slightly lifted and eyes assessing.',
   'Ayato Nikaidō':'An extravagant theatrical smile, a vain performer enjoying his own entrance.',
   'Kanna Tsuruno':'Proud and hotly competitive, showing a flash of irritation.',
   'Mizuki Kaneshiro':'A youthful adult high elf with an elegant, subtly patronizing smile; no elderly human aging.',
   'Reina Hazakura':'An older but vigorous adult woman with mature anime face lines and a dangerous delighted smile.',
   'Mika Koshimizu':'Defensive, sleepless annoyance and an assessing glance.',
   'Renjirō Suda':'A practiced, evasive smile while weighing an offer.',
   'Momo Shiratori':'A mischievous, calculating grin; candy-pink curls and very confident stage presence.',
   'Shiori Takase':'An acquisitive smile from a mature dragonkin woman, human face and thick tail.',
   'Koharu Mikazuki':'A confident, vindictive edge behind an easy commercial smile.',
  }.get(name,'Let the exact individual personality below guide a distinct expression rather than a universal smile.')
  scene=n['currentArea'] or n['currentLocation']
  magic='; '.join(a+': '+effects[a] for a in affinity)
  prompt=(f'Create ONE brand-new polished PNG portrait of {name} for a fantasy RPG ensemble. VERTICAL 2:3, standing HIP-UP, centered person, complete head and hair and ears and horns. '
   'IMPORTANT FRAMING: topmost head/hair/ear/horn begins at 15 percent canvas height (y=230 on a 1536-high image); reserve the upper 12.5–15 percent as open background. No prop or magic intrudes into that band. Keep hips visible, no closer crop. '
   'Crisp pristine colorful 2D fantasy ANIME: expressive stylized anime eyes and facial proportions, deliberate clean lineart, graphic cel shading, sharp detailed clothing and hair. No realism, semi-realism, photographic skin, 3D rendering or blurry painterly edges. '
   f'Approved identity: {n["visualDescription"]} Approved chronological age and species are in the card; respect long-lived species adult appearance. {cues} '
   f'Role profile {role}; category {category}; randomly selected pose {pose}: {POSES[pose]} '
   f'Actual equipment and technique: {n["abilities"][0]} Show {weapon} correctly, with mechanically coherent hands and grip; do not replace the weapon. '
   f'Make ALL listed affinities clearly visible, separated from the face: {magic}. '
   'For competitors, give this special recurring opponent a flashier, memorable effect composition, bold light and attractive costume silhouette, while keeping effects controlled and fitting actual level. For support staff, show work-related magic with equally crisp colorful staging. '
   f'Established scene: {scene}, within {n["currentLocation"]}. Background shows that actual place, softer than face, no unrelated giant landmarks. '
   f'Personality and public context: {n["basicInfo"].split(chr(10)+chr(10))[0]} '
   'Only two coherent arms and hands, thumbs and wrists plausible, no duplicate body, no extra person. No text, lettering, signature, watermark, UI or collage. Let effects and pose feel specific, not the same glow on every portrait.')
  rows.append(dict(name=name,profile=role,eligible=eligible,drawnIndex=i+1,pose=pose,prompt=prompt,file=f'world-draft/npc portraits/{name}.png',generationMode='built-in image_gen; one fresh pass authorized 2026-11-02'))
 p.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({'total':len(rows),'remaining':[r['name'] for r in rows[10:]]},ensure_ascii=False))

if __name__=='__main__':main()
