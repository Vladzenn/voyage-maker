"""Make labeled review sheets without altering any delivered portrait pixels."""
import json,math,pathlib
from PIL import Image,ImageDraw,ImageFont
from build import ROOT,HERE

art=json.loads((HERE/'supporting-generated-art.json').read_text(encoding='utf-8'))
byname={r['name']:r for r in art['assets']}
selection=json.loads((HERE/'supporting-portrait-selection.json').read_text(encoding='utf-8'))
assert set(selection)==set(byname) and len(selection)==83
out=ROOT/'output/oni-nation-2026-11-02';out.mkdir(parents=True,exist_ok=True)
font=ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf',15)
for page in range(math.ceil(len(selection)/24)):
    names=selection[page*24:(page+1)*24]
    sheet=Image.new('RGB',(6*210,math.ceil(len(names)/6)*342),'#16191c');draw=ImageDraw.Draw(sheet)
    for i,name in enumerate(names):
        im=Image.open(ROOT/byname[name]['target']).convert('RGB');im.thumbnail((200,300))
        x=(i%6)*210+5;y=(i//6)*342+5;sheet.paste(im,(x,y))
        draw.text((x,y+305),name,font=font,fill='white')
    sheet.save(out/f'Supporting Portrait Review {page+1}.jpg',quality=90)
print(json.dumps({'reviewSheets':math.ceil(len(selection)/24),'portraits':len(selection),'originalImagesModified':False}))
