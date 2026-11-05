"""Build the planning inventory and reading PDF without changing the playable world."""
from __future__ import annotations
import csv, hashlib, json, pathlib, re, shutil, textwrap, zipfile
from collections import Counter
from html import escape
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.platypus.tableofcontents import TableOfContents
from pypdf import PdfReader

ROOT = pathlib.Path(__file__).resolve().parents[2]
HERE = pathlib.Path(__file__).resolve().parent
PLAN = ROOT / 'world-draft/authoring/plans'
WORLD = ROOT / 'world-draft/WorldAlpha - World.json'
STEM = 'Glowhaven - World Overhaul'
MD = PLAN / (STEM + ' Implementation Handoff.md')
PDF = PLAN / (STEM + ' Implementation Handoff.pdf')
OUT = ROOT / 'output/glowhaven-world-overhaul-planning-2026-11-05'


def compact(v): return json.dumps(v, ensure_ascii=False, separators=(',', ':'))
def units(v): return len((v if isinstance(v,str) else compact(v)).encode('utf-16-le'))//2
def digest(v): return hashlib.sha256(compact(v).encode()).hexdigest()
def pointer(parts): return '/' + '/'.join(str(p).replace('~','~0').replace('/','~1') for p in parts)
def excerpt(v):
    if isinstance(v,dict):
        text = next((v[k] for k in ('basicInfo','description','text','questStatement','storyStart','theme','name') if isinstance(v.get(k),str) and v[k]), '')
    else: text = str(v)
    return re.sub(r'\s+',' ',text).strip()[:260]


def make_inventory():
    w=json.loads(WORLD.read_text(encoding='utf-8-sig'))
    source_hash=hashlib.sha256(WORLD.read_bytes()).hexdigest()
    def realm_for(loc):
        location=w['locations'].get(loc,{})
        return w['regions'].get(location.get('region'),{}).get('realm','Unplaced or not geographic')
    def context(section,key,value):
        if section=='realms': return key
        if section=='regions': return value.get('realm','')
        if section=='locations': return realm_for(key)
        if section=='areas': return realm_for(key[0])
        if section=='npcs': return realm_for(value.get('currentLocation'))
        if section=='quests': return realm_for(value.get('questLocation'))
        if section=='storyStarts':
            return '; '.join(dict.fromkeys(realm_for(x) for x in value.get('locations',[])))
        return ''
    assignments={
      'npcs':'Individual character pass: voice, want, competence, consequential flaw, ordinary pleasure, knowledge and specific ties; respect entity kind.',
      'locations':'Review function, atmosphere, actual contacts, activities and coherent area use; preserve media and coordinates.',
      'areas':'Review distinctive scene use, description and internal connections; preserve images and addresses.',
      'factions':'Develop constituency, means, project, methods, disagreements, limits and concrete playable stakes.',
      'worldLore':'Reconcile retcons and factual ownership; distinguish lore from runtime instructions.',
      'quests':'Audit discovery/acceptance/completion/payout ownership, methods, closure and refusal/failure.',
      'arcs':'Review premises and conclusions; localize/gate surfacing and avoid duplication with finite quests.',
      'storyStarts':'Review immediate activity, role fidelity, manageable cast and player stopping point.',
      'gameModes':'Review available activities and emphasis; preserve continuity and numerical settings.',
      'abilities':'Review function, distinctiveness, prerequisites and teaching links; retain current numbers.',
      'itemTypes':'Shorten redundancy within collection budget; retain ownership meaning and mechanics.',
      'traits':'Review identity/presentation and actual grants; retain current numerical balance.',
      'triggerDefinitions':'Classify dependencies, phase, exact state and reward owner; change only justified affected logic.',
      'aiInstructions':'Assign rule owner; consolidate repetition; keep facts in scoped records and preserve safeguards.',
      'npcTypes':'Review encounter identity, use and factual consistency; retain numerical anchors.',
      'skills':'Review routing and available learning opportunities; preserve numerical configuration.',
      'regions':'Review geographic identity and opportunities; preserve map metadata.',
      'realms':'Review identity and scope; preserve geographic/media configuration.',
      'authorSeeds':'Review generated-content direction against the revised authored world.',
      'encounterElements':'Review varied supported opportunities and avoid compulsory scene interruption.',
      'characterArchetypes':'Review specificity and diversity without blanket personality defaults.',
      'locationArchetypes':'Review useful activity and place differentiation.',
      'regionArchetypes':'Review geographical and cultural specificity.',
      'traitCategories':'Review creation coherence and references; preserve selections and numerical grants.',
      'storySettings':'Review overview/guidance within current field caps; keep handoff outside runtime.',
    }
    rows=[]
    def add(section,key,value,parts):
        display=key if isinstance(key,str) else ' / '.join(key)
        realm=context(section,key,value) if isinstance(value,dict) or section in ('realms','areas') else ''
        protected=realm=='The Silken Descent'
        dependency=section=='triggerDefinitions' and re.search(r'Spider|Silken|Vhalessra|Silver Web|anomalous passage',compact(value),re.I)
        rows.append({'collection':section,'key':display,'source_pointer':pointer(parts),'realm_context':realm,
          'source_sha256':digest(value),'baseline_excerpt':excerpt(value),'protection':'protected exact' if protected else ('protected dependency review' if dependency else 'mutable narrative / protected configuration'),
          'assignment':'Preserve exact record and related protected behavior; verify source comparison.' if protected else assignments.get(section,'Review consistency and affected references; preserve configuration unless explicitly scoped.'),
          'status':'pending','retcon_ids':'','related_records':'','review_evidence':'','validation_result':''})
    top_maps=['realms','regions','locations','npcs','factions','worldLore','storyStarts','itemTypes','abilities','skills','traits','traitCategories','npcTypes','triggerDefinitions','gameModes','authorSeeds','encounterElements','characterArchetypes','locationArchetypes','regionArchetypes','unassignedAreas','worldVoices','nameFilterSettings','randomNames']
    for section in top_maps:
        for key,value in w.get(section,{}).items(): add(section,key,value,[section,key])
    for loc,value in w['locations'].items():
        for area,record in value.get('areas',{}).items(): add('areas',(loc,area),record,['locations',loc,'areas',area])
    for party,value in w['parties'].items():
        for section in ('quests','questTriggers','arcs','narrativeEvents'):
            for key,record in value.get(section,{}).items(): add(section,key,record,['parties',party,section,key])
    for task,notes in w['aiInstructions'].items():
        for name,value in notes.items(): add('aiInstructions',task+' / '+name,value,['aiInstructions',task,name])
    used=set(top_maps)|{'parties','aiInstructions'}
    for section,value in w.items():
        if section in used: continue
        if isinstance(value,dict):
            for key,record in value.items(): add(section,key,record,[section,key])
        else: add(section,section,value,[section])
    path=PLAN/(STEM+' Coverage.csv')
    with path.open('w',encoding='utf-8-sig',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    numeric=[];media=[]
    def visit(v,parts):
        if isinstance(v,dict):
            for k,x in v.items(): visit(x,parts+[k])
        elif isinstance(v,list):
            for i,x in enumerate(v):visit(x,parts+[i])
        elif isinstance(v,(int,float)) and not isinstance(v,bool):numeric.append([pointer(parts),v])
        elif isinstance(v,str) and v.startswith(('https://','http://')):media.append([pointer(parts),v])
    visit(w,[])
    baseline={'date':'2026-11-05','sourceCommit':'7f11579','sourceSHA256':source_hash,
      'planningOnly':True,'canonicalChanged':False,'inventoryRows':len(rows),'counts':dict(Counter(r['collection'] for r in rows)),
      'compactWorldUTF16Units':units(w),'collectionUTF16Units':{k:units(w[k]) for k in ('npcs','locations','itemTypes','traits','aiInstructions','triggerDefinitions')},
      'protectedRecordHashes':{r['source_pointer']:r['source_sha256'] for r in rows if r['protection']=='protected exact'},
      'protectedDependencyCandidates':{r['source_pointer']:r['source_sha256'] for r in rows if r['protection']=='protected dependency review'},
      'numericBaseline':numeric,'urlBaseline':media,
      'settingsBaseline':{k:w[k] for k in ('progressionSettings','attributeSettings','skillSettings','resourceSettings','combatSettings','death','locationSettings','itemSettings','relationshipStages','gameplayMusicSettings','worldVoices')},
      'note':'Inventory is not an editorial audit. All implementation rows begin pending. Exact protected dependency scope must be verified against existing regression fingerprints.'}
    (PLAN/(STEM+' Baseline.json')).write_text(json.dumps(baseline,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    ledgers={
      'Relationships':['person_a','person_b','shared_fact','a_interpretation','b_interpretation','who_knows','affected_records','status','review'],
      'Retcons':['retcon_id','old_fact','proposed_replacement','rationale','affected_records','mechanical_dependencies','migration_boundary','status','review'],
      'Undertakings':['undertaking_key','discovery_owner','acceptance_owner','completion_evidence','payout_owner','follow_up','refusal_failure','status','review'],
      'Live Checks':['scenario','build_sha256','steps','expected','observed','result','tester_date']}
    for name,fields in ledgers.items():
        p=PLAN/(STEM+' '+name+'.csv')
        if not p.exists():
            with p.open('w',encoding='utf-8-sig',newline='') as stream:
                writer=csv.writer(stream);writer.writerow(fields)
    return baseline


def rich(text):
    value=escape(text)
    value=re.sub(r'`([^`]+)`',lambda m:'<font name="PlanMono">'+m.group(1)+'</font>',value)
    value=re.sub(r'\*\*([^*]+)\*\*',r'<b>\1</b>',value)
    value=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'<link href="\2" color="#174D5B">\1</link>',value)
    return value


class PlanDoc(BaseDocTemplate):
    def afterFlowable(self,f):
        if isinstance(f,Paragraph) and f.style.name=='Section':
            key='section-'+str(self.seq.nextf('section'))
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(f.getPlainText(),key,0,False)
            self.notify('TOCEntry',(0,f.getPlainText(),self.page,key))


def make_pdf():
    fonts=pathlib.Path('C:/Windows/Fonts')
    pdfmetrics.registerFont(TTFont('Plan',str(fonts/'arial.ttf')))
    pdfmetrics.registerFont(TTFont('PlanBold',str(fonts/'arialbd.ttf')))
    pdfmetrics.registerFont(TTFont('PlanItalic',str(fonts/'ariali.ttf')))
    pdfmetrics.registerFont(TTFont('PlanMono',str(fonts/'consola.ttf')))
    pdfmetrics.registerFontFamily('Plan',normal='Plan',bold='PlanBold',italic='PlanItalic',boldItalic='PlanBold')
    ink=colors.HexColor('#17262F');muted=colors.HexColor('#52636B');tint=colors.HexColor('#EDF3F4')
    styles={
      'body':ParagraphStyle('Body',fontName='Plan',fontSize=10.1,leading=14.6,textColor=ink,spaceAfter=7,splitLongWords=True,allowWidows=0,allowOrphans=0),
      'title':ParagraphStyle('Title',fontName='PlanBold',fontSize=26,leading=31,textColor=ink,spaceAfter=12),
      'h2':ParagraphStyle('Section',fontName='PlanBold',fontSize=17,leading=22,textColor=ink,spaceBefore=14,spaceAfter=9,keepWithNext=True),
      'h3':ParagraphStyle('Subsection',fontName='PlanBold',fontSize=11.7,leading=16,textColor=ink,spaceBefore=9,spaceAfter=6,keepWithNext=True),
      'small':ParagraphStyle('Small',fontName='Plan',fontSize=8.3,leading=11.3,textColor=muted,spaceAfter=5),
      'table':ParagraphStyle('Table',fontName='Plan',fontSize=8.5,leading=11.8,textColor=ink,spaceAfter=0),
      'toc':ParagraphStyle('TOC',fontName='Plan',fontSize=10,leading=14.3,textColor=ink,spaceBefore=0,leftIndent=0,rightIndent=22),
    }
    width,height=A4;margin=20*72/25.4;usable=width-2*margin
    doc=PlanDoc(str(PDF),pagesize=A4,leftMargin=margin,rightMargin=margin,topMargin=45,bottomMargin=42,
       title='Glowhaven World Overhaul Implementation Handoff',author='Voyage Maker',subject='World-wide authoring plan and implementation coverage')
    frame=Frame(margin,42,usable,height-87,leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)
    def decorate(canvas,d):
        canvas.saveState();canvas.setFillColor(muted);canvas.setFont('Plan',7.5)
        canvas.drawString(margin,height-27,'GLOWHAVEN  /  WORLD OVERHAUL IMPLEMENTATION')
        canvas.drawString(margin,24,'5 NOVEMBER 2026  |  PLANNING HANDOFF')
        canvas.drawRightString(width-margin,24,str(d.page));canvas.restoreState()
    doc.addPageTemplates(PageTemplate(id='main',frames=[frame],onPage=decorate))
    story=[Spacer(1,12),Paragraph('Glowhaven World Overhaul<br/>Implementation Handoff',styles['title']),
      Paragraph('A complete redevelopment plan for characters, communities, magic, exploration and player ambitions',styles['body']),
      Paragraph('Major personality and lore retcons permitted. Numerical balance retained initially. Canonical gameplay unchanged by this planning delivery.',styles['small']),Spacer(1,13),
      Paragraph('Document navigation',styles['h3'])]
    toc=TableOfContents();toc.levelStyles=[styles['toc']];toc.tableStyle=TableStyle([('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0),('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),3)]);story.append(toc);story.append(PageBreak())
    lines=MD.read_text(encoding='utf-8').splitlines();i=0
    while i<len(lines):
        line=lines[i].strip()
        if not line or line.startswith('# ') or line.startswith('Prepared '):i+=1;continue
        if line.startswith('## '):
            title=line[3:]
            story.append(Paragraph(rich(title),styles['h2']));i+=1;continue
        if line.startswith('### '):story.append(Paragraph(rich(line[4:]),styles['h3']));i+=1;continue
        if line.startswith('|'):
            block=[]
            while i<len(lines) and lines[i].strip().startswith('|'):
                raw=lines[i].strip();i+=1
                cells=[x.strip() for x in raw.strip('|').split('|')]
                if all(re.fullmatch(r':?-+:?',x) for x in cells):continue
                block.append(cells)
            cols=len(block[0])
            if cols==5:fractions=[.44,.14,.14,.14,.14]
            elif cols==3:fractions=[.25,.10,.65]
            else:fractions=[.29,.71]
            rows=[[Paragraph(rich(c),styles['table']) for c in row] for row in block]
            t=Table(rows,colWidths=[usable*f for f in fractions],repeatRows=1,hAlign='LEFT')
            t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),tint),('VALIGN',(0,0),(-1,-1),'TOP'),
             ('LINEBELOW',(0,0),(-1,0),.6,colors.HexColor('#A8BDC4')),('LINEBELOW',(0,1),(-1,-1),.25,colors.HexColor('#D6E1E4')),
             ('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]))
            story.extend([t,Spacer(1,9)]);continue
        parts=[line];i+=1
        while i<len(lines) and lines[i].strip() and not lines[i].lstrip().startswith(('#','|')):parts.append(lines[i].strip());i+=1
        story.append(Paragraph(rich(' '.join(parts)),styles['body']))
    doc.multiBuild(story)
    reader=PdfReader(PDF);extracted='\n'.join(p.extract_text() or '' for p in reader.pages)
    expected=[line[3:] for line in lines if line.startswith('## ')]
    missing=[s for s in expected if s not in extracted]
    if missing: raise ValueError('Missing sections in PDF: '+str(missing))
    return {'pdfPages':len(reader.pages),'sectionCount':len(expected),'markdownWords':len(MD.read_text(encoding='utf-8').split()),'missingSections':missing}


def main():
    PLAN.mkdir(parents=True,exist_ok=True);OUT.mkdir(parents=True,exist_ok=True)
    expected='49088ccf50e7f4df2f7e44295681bf0abce9a9e7e79b0877318c3c393a7e46d2'
    if hashlib.sha256(WORLD.read_bytes()).hexdigest()!=expected:
        raise ValueError('Frozen planning source differs. Create a new implementation baseline; preserve this historical inventory.')
    coverage=PLAN/(STEM+' Coverage.csv')
    if coverage.exists():
        with coverage.open(encoding='utf-8-sig',newline='') as f:
            if any(r['status']!='pending' for r in csv.DictReader(f)):
                raise ValueError('Coverage contains implementation progress. Preserve it instead of regenerating pending rows.')
    baseline=make_inventory();review=make_pdf()
    assert hashlib.sha256(WORLD.read_bytes()).hexdigest()==baseline['sourceSHA256'],'Canonical world changed'
    files=[MD,PDF]+sorted(PLAN.glob(STEM+' *.csv'))+[PLAN/(STEM+' Baseline.json')]
    for p in files:shutil.copyfile(p,OUT/p.name)
    archive=OUT/(STEM+' Implementation Package.zip')
    with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
        for p in files:z.write(p,p.name)
    review.update(sourceSHA256=baseline['sourceSHA256'],inventoryRows=baseline['inventoryRows'],inventoryCounts=baseline['counts'],worldChanged=False,
       files=[{'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size} for p in files])
    (HERE/'review.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in review.items() if k!='files'},ensure_ascii=False))

if __name__=='__main__':main()
