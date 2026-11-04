"""Select compatible poses once and record the four principal portrait prompts."""
import json
import pathlib
import random
import re

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
world = json.loads((ROOT/'output/rebirth-2026-11-05/The Schools of Magic, Arise! - Rebirth.json').read_text(encoding='utf-8'))
guide = (ROOT/'research/Portrait Creation Format.md').read_text(encoding='utf-8-sig')
poses = {m[0]:(m[1],m[2]) for m in re.findall(r'- \*\*([A-Z]+\d+) — ([^*]+):\*\*\s*([^\n]+)',guide)}
configs = [
    ("Valkazathoth'dmir", 'default, reserved serious public demeanor', ['R01','R03','R04','R05','R06'], 'At Shadowspire’s threshold with the curved stair, brass ward inlay and woodland light. Quiet fatherly gravity and a trace of offended amusement. Arcane geometric mana, a narrow teal spatial fold at the doorway and restrained golden enchantment threads remain distinguishable. His ageless adult face is expressive and handsome; his plum coat has a memorable silhouette.'),
    ('Mihana Orihara', 'default, warm and practical', ['W01','W02','W03','W05','W06'], 'In her cottage workshop off Brookmeadow Mill Lane, in warm ordinary daylight. Painted lamp covers and brushes stand behind her. A small real lantern flame glows with her modest Fire affinity. She looks candid, capable and warm with limits. Plain working clothes have individually drawn fabric and a blue apron.'),
    ('Reika Kurose', 'governing investigator', ['GV01','GV02','GV04','GV05','GV07'], 'In the Court administrative wing, with pale stone, tall window light, work folios and a small broken toy boat on a standing-height desk. Her sword stays sheathed. A restrained golden Light thread and a separate indigo divination reflection at the folio suggest her expertise. An adult freckled face, alert and forthright, without a generic cute smile.'),
    ('Kazunari Shiba', 'governing delegation officer', ['GV02','GV03','GV04','GV07','GV08'], 'At a quiet Brookmeadow lane, rural stone walls, leafy sunlight and distant cottage roofs. No other figures. His celestial gold clasp and ordinary service mail mark a seasoned officer. Use a compact white-gold Light shimmer and a distinct geometric Enchantment lattice at a glove or saber fitting. No fire or lightning.')]
base = 'One vertical 2:3 Voyage NPC portrait, in the established polished colorful 2D fantasy-anime illustration style. Drawn expressive adult anime face, fine illustrated hair, controlled layered cel shading and painterly environmental depth. Rich material design and memorable individual silhouette. No photorealistic skin, pores, live-action look, 3D render or plastic surfaces. Center one standing person, framing from upper thighs through the complete head. Leave 12.5–15 percent clear headroom above all hair. Real hips and upper thighs must show. Exactly two arms and natural hands, with the face readable. No foreground people, letters, nameplate, border or watermark. One final generation pass. '
output = HERE/'portrait-prompts.json'
if output.exists():
    raise SystemExit('Portrait prompts already exist. Reuse the recorded selection.')
rows = []
used = set()
rng = random.SystemRandom()
for name,profile,eligible,scene in configs:
    choices = [p for p in eligible if p not in used] or eligible
    index = rng.randrange(len(choices))
    pose = choices[index]
    used.add(pose)
    npc = world['npcs'][name]
    prompt = (base+'\nIdentity: '+npc['visualDescription']+'\nEquipment: '+npc['basicInfo'].split('Equipment: ')[1].split('\n\n')[0]
              +'\nScene: '+scene+'\nPose profile: '+profile+'. Chosen '+pose+' — '+poses[pose][0]+'. '+poses[pose][1]
              +'\nUse slightly flashier presentation for this principal character, with coherent light and readable affinity effects. Keep every staff or weapon shaft continuous, aligned through the hands; a long prop can leave the lower or side edge naturally.')
    rows.append(dict(name=name,profile=profile,eligible=choices,drawnIndex=index+1,pose=pose,prompt=prompt,file='world-draft/npc portraits/Rebirth/'+name+'.png'))
output.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(rows,ensure_ascii=False))
