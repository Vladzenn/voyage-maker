"""Internal contact sheet only; never alters deliverable portrait PNGs."""
import json,math
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
jobs=json.loads((HERE/'portrait-jobs.json').read_text(encoding='utf-8'))
jobs=[j for j in jobs if Path(j['destination']).exists()]
state=ROOT/'world-draft/npc portraits/Glowhaven Expansion/States/Nerathyl - Awake.png'
if state.exists():jobs.append({'name':'Nerathyl — Awake','destination':str(state)})
font=ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf',18)
sheet=Image.new('RGB',(4*256,math.ceil(len(jobs)/4)*416),'#15191f');d=ImageDraw.Draw(sheet)
for i,j in enumerate(jobs):
    p=Image.open(j['destination']).convert('RGB');p.thumbnail((256,384))
    x=(i%4)*256;y=(i//4)*416;sheet.paste(p,(x+(256-p.width)//2,y));d.text((x+8,y+388),j['name'],font=font,fill='white')
out=ROOT/'output/glowhaven-expansion-2026-11-03/Portrait Contact Sheet.jpg';out.parent.mkdir(parents=True,exist_ok=True);sheet.save(out,quality=93)
print(str(out))
