import json, pathlib, hashlib, re, html, shutil
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether, Image as RLImage
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image
from pypdf import PdfReader
ROOT=pathlib.Path('R:/VoyageMaker')
WORK=ROOT/'tools/drakenspire-map-2026-11-05'
data=json.loads((WORK/'canonical-descriptions.json').read_text(encoding='utf-8'))
brief=json.loads((WORK/'brief-input.json').read_text(encoding='utf-8-sig'))
out=ROOT/'world-draft/authoring/plans/Drakenspire - Standalone Fresh Map Prompt.pdf'
out.parent.mkdir(parents=True,exist_ok=True)
for name,file in [('Segoe','segoeui.ttf'),('SegoeBold','segoeuib.ttf'),('SegoeItalic','segoeuii.ttf')]:
 pdfmetrics.registerFont(TTFont(name,'C:/Windows/Fonts/'+file))
pdfmetrics.registerFontFamily('Segoe',normal='Segoe',bold='SegoeBold',italic='SegoeItalic',boldItalic='SegoeBold')
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='BodyA',fontName='Segoe',fontSize=9.7,leading=13.9,textColor=colors.HexColor('#273746'),spaceAfter=7))
styles.add(ParagraphStyle(name='SmallA',parent=styles['BodyA'],fontSize=8.2,leading=11.5,textColor=colors.HexColor('#586a7b')))
styles.add(ParagraphStyle(name='StatusA',parent=styles['SmallA'],keepWithNext=True))
styles.add(ParagraphStyle(name='KickerA',fontName='SegoeBold',fontSize=9.2,leading=13,textColor=colors.HexColor('#9a622e'),spaceAfter=10))
styles.add(ParagraphStyle(name='TitleA',fontName='SegoeBold',fontSize=32,leading=37,textColor=colors.HexColor('#18344c'),spaceAfter=18))
styles.add(ParagraphStyle(name='H1A',fontName='SegoeBold',fontSize=20,leading=25,textColor=colors.HexColor('#18344c'),spaceBefore=4,spaceAfter=13,keepWithNext=True))
styles.add(ParagraphStyle(name='H2A',fontName='SegoeBold',fontSize=13,leading=17,textColor=colors.HexColor('#234e67'),spaceBefore=17,spaceAfter=8,keepWithNext=True))
styles.add(ParagraphStyle(name='AreaA',fontName='SegoeBold',fontSize=9.8,leading=13.5,textColor=colors.HexColor('#365b70'),spaceBefore=5,spaceAfter=3,keepWithNext=True))
styles.add(ParagraphStyle(name='QuoteA',parent=styles['BodyA'],leftIndent=12,borderColor=colors.HexColor('#cad5dd'),borderWidth=1,borderPadding=8,spaceBefore=4,spaceAfter=11))
W,H=A4
def norm(s):
 return str(s).replace('\u2014',' - ').replace('\u2013','-').replace('\u2011','-').replace('\u2010','-').replace('\u2212','-')
def para(s,st='BodyA'):
 return Paragraph(html.escape(norm(s)).replace('\n','<br/>'),styles[st])
def paras(s,st='BodyA'):
 return [para(x,st) for x in str(s).split('\n\n') if x.strip()]
story=[]
def add(s,st='BodyA'): story.extend(paras(s,st))
def head(s): story.append(para(s,'H1A'))
def picture(path,maxh=350):
 im=Image.open(path); iw,ih=im.size
 scale=min((W-96)/iw,maxh/ih)
 story.append(RLImage(str(path),width=iw*scale,height=ih*scale))
 story.append(Spacer(1,10))
sections=[]
class Doc(SimpleDocTemplate):
 def afterFlowable(self,flowable):
  if isinstance(flowable,Paragraph) and flowable.style.name in ('H1A','H2A'):
   txt=flowable.getPlainText()
   key='b'+str(len(sections))
   self.canv.bookmarkPage(key)
   self.canv.addOutlineEntry(txt,key,0 if flowable.style.name=='H1A' else 1,False)
   sections.append({'heading':txt,'page':self.page})
def decorate(c,doc):
 c.saveState()
 c.setStrokeColor(colors.HexColor('#d7e0e7')); c.line(48,42,W-48,42)
 c.setFont('Segoe',8); c.setFillColor(colors.HexColor('#617386'))
 c.drawString(48,H-28,'DRAKENSPIRE  /  STANDALONE MAP PROMPT')
 c.drawString(48,27,'Canonical descriptions + author art direction | 5 November 2026')
 c.drawRightString(W-48,27,str(doc.page))
 c.restoreState()
add('AUTHORING BRIEF  /  5 NOVEMBER 2026','KickerA')
add('Drakenspire','TitleA')
add('A fresh stone-built mountain city and its surrounding highlands','H1A')
add('A complete prompt package for an image AI with no prior chat context. Includes the author brief, a copy-ready prompt, two actual art references, and the full current public descriptions of the realm, region, 59 locations and 251 areas.')
add('LATEST DIRECTION','KickerA')
add('The compact city sits HIGH on a rocky mountain, above nearby wilderness. The fortress sits higher still. Add more densely packed stone buildings while leaving generous space for outlying locations. Use a genuinely new composition and camera, not a redraw of an older Drakenspire map.')
add('REQUESTED OUTPUTS','KickerA')
add('1. One clean unlabelled regional map.\n2. A separate locator picture using the same artwork, with clear markers and an exact-name key.')
add('SOURCE BOUNDARY','KickerA')
add('The current canonical world supplies setting facts. Author instructions supply the new art direction. Numerical location coordinates are intentionally absent. No old Drakenspire artwork or rejected draft is included, so it cannot become an accidental composition template.')
add('Contents: author brief; copy-ready prompt; art references; canon summary; exact location index; full location and area descriptions.','SmallA')
story.append(PageBreak())
head('The author brief')
add('These statements are preserved in the order given. Later clarifications control earlier ambiguity.','SmallA')
for i,text in enumerate(brief['userBrief'],1):
 add(str(i).zfill(2),'KickerA'); add(text,'QuoteA')
add('Interpretation for the next image','H2A')
add('“Match the scale” means comparable regional rendering and individual building scale. It does not mean giving this small fortress-city the population or urban footprint of Ardelis or all of Akitsuhara. “More buildings” means greater density and more inhabited blocks within a compact high-elevation town. “Higher than wilderness” means visibly above the adjoining valley and lower surrounding countryside; it does not mean every distant mountain peak must be lower.')
story.append(PageBreak())
head('Copy-ready image prompt')
for block in brief['cleanMapPrompt'].split('\n\n'): add(block)
story.append(PageBreak())
head('Art reference 1 - Ardelis')
add('Role: primary reference for finish, coherent architecture, visual hierarchy, material separation and readable city detail. Match its illustrated quality. Do not copy its city size, geography, palace, gold ornament or formal plan.','BodyA')
picture(ROOT/'output/ardelis-detail-atlas-2026-11-05/master.png',355)
add('This overview corresponds to the current Ardelis map family. The installed central tile below confirms the same painted architectural treatment. The reference is a quality guide; Drakenspire must remain smaller, snowier and more strongly built from practical stone.','SmallA')
picture(ROOT/'tmp/drakenspire-map-2026-11-05/ardelis-current-center.jpg',250)
story.append(PageBreak())
head('Art reference 2 - Akitsuhara')
add('Role: primary reference for layered terrain, clear regional scale, connected routes, purposeful buildings and controlled vivid color. Do not copy its Japanese architecture, seasons, ricefields, shrines or geography.','BodyA')
picture(ROOT/'world-draft/map-variations/Oni Nation/Oni Nation - Master Map v1.png',365)
add('The installed Benitsuru Basin tile below supplies a closer sample of the current map family. Use the crisp illustrated construction and depth treatment in a snowy alpine vocabulary.','SmallA')
picture(ROOT/'tmp/drakenspire-map-2026-11-05/akitsuhara-current-center.png',235)
story.append(PageBreak())
head('Canon summary and design checks')
checks=[
('City and elevation','One compact inhabited mountain city on a high rocky shelf, with a still-higher fortress shelf to its geographic northeast. The rotated camera may put them anywhere on screen. Nearby wilderness and lower settlements sit below the city.'),
('The main landmark','Crescent Crown Fortress and one enormous ancestral dragon skeleton form the defining landmark. The Jarl\'s Hall, assembly and sanctuary belong to this one precinct. Bones are distinct from masonry.'),
('Ordinary life','Markets, homes, small shops, three clanholds, schoolhouse, playhouse, modest fighting venue and practice grounds. Use many useful small buildings, not a collection of huge monuments.'),
('Production and services','Metallurgy, crystal craft, freight, enclosed portal hall, one onsen, practical waterworks, stores, livestock and pasture folds. Functional roads and yards should make their relationships readable.'),
('Surrounding country','Inland frozen lake, sparse sheltered pines, hamlet, lodge/watchpost, trails, working mine and amber cave, abandoned haul works and settlement, rocky peaks, ravine, ruins and remote habitats.'),
('Unknown sites','First Shelter Ruins, The White Silence, Coldglass Galleries and The Fallen Pass Shrine are initially unknown. Keep their clean-map cues subtle. Their suggested positions may appear on the author locator.'),
('Protected uncertainties','No confirmed guardian-dragon lair or visible named boss. Skeleton is not heat/mana infrastructure. Cave mouths do not reveal underground floor plans.'),
('Current inventory','The canonical full world has 59 Drakenspire locations and 251 areas. Dusklamp Quarter occurs in historical plans, but is absent from the current canonical location collection. It is not part of this brief.'),
]
for label,text in checks:
 add(label,'H2A'); add(text)
story.append(PageBreak())
head('Canonical realm and region')
add(data['realm']['name'],'H2A'); add(data['realm']['basicInfo'])
add(data['region']['name'],'H2A'); add(data['region']['basicInfo'])
add('Source provenance','H2A')
add('File: '+data['source']+'\nSnapshot date: '+data['date']+'\nSHA-256: '+data['sha256'],'SmallA')
add('The following source catalogue preserves public basicInfo and area descriptions. HiddenInfo, scripts, mechanics, image URLs and numerical coordinates are excluded. Source text can mention ordinary access or ownership rules; these do not become new visual landmarks. No world edits are applied by this document.','SmallA')
story.append(PageBreak())
head('Exact current location index')
add('Numbers identify catalogue entries and the later locator key. They are not game coordinates.','SmallA')
rows=[]
items=list(data['locations'].items())
for i in range(20):
 row=[]
 for col in range(3):
  n=i+20*col
  row.append(para(f'{n+1:02d}  {items[n][0]}' if n<len(items) else '', 'SmallA'))
 rows.append(row)
table=Table(rows,colWidths=[(W-96)/3]*3,hAlign='LEFT')
table.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),12),('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),5)]))
story.append(table)
story.append(PageBreak())
head('Full location and area descriptions')
add('The canonical text below is the detailed setting reference. Use ordinary exterior cues for interior areas. Keep the latest author art direction separate from these source facts.','SmallA')
for i,(name,loc) in enumerate(items,1):
 add(f'{i:02d}. {name}','H2A')
 add('Initially known' if loc.get('initialKnown') else 'Initially unknown','StatusA')
 add(loc.get('basicInfo',''))
 for area,details in loc.get('areas',{}).items():
  add(area,'AreaA'); add(details.get('description',''))
doc=Doc(str(out),pagesize=A4,leftMargin=48,rightMargin=48,topMargin=48,bottomMargin=55,title='Drakenspire - Standalone Fresh Map Prompt',author='Voyage Maker',pageCompression=1)
doc.build(story,onFirstPage=decorate,onLaterPages=decorate)
reader=PdfReader(out)
extracted='\n'.join(p.extract_text() or '' for p in reader.pages)
missing=[name for name in data['locations'] if norm(name) not in extracted]
missing_areas=[name for loc in data['locations'].values() for name in loc['areas'] if norm(name) not in extracted]
if missing or missing_areas: raise RuntimeError({'missing_locations':missing,'missing_areas':missing_areas})
for term in ['xPercent','yPercent','npcLevelRange']: assert term not in extracted,term
copy=ROOT/'output/pdf/Drakenspire - Standalone Fresh Map Prompt.pdf'
shutil.copy2(out,copy)
qa={'pdf':str(out),'pageCount':len(reader.pages),'locationCount':len(items),'areaCount':data['areaCount'],'missingLocationNames':missing,'missingAreaNames':missing_areas,'sourceSha256':data['sha256'],'pdfSha256':hashlib.sha256(out.read_bytes()).hexdigest(),'textCharacters':len(extracted),'headings':sections}
(WORK/'pdf-verification.json').write_text(json.dumps(qa,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(ROOT/'tmp/pdfs/drakenspire/extracted.txt').write_text(extracted,encoding='utf-8')
print(json.dumps({k:v for k,v in qa.items() if k!='headings'},indent=2))

