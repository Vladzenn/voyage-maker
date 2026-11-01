"""Build a minor patch from an explicitly supplied, current Studio export."""
import argparse
import copy
import hashlib
import json
import pathlib
import re
import statistics
from content import PROFESSIONS, OUTFITS, ACCESSORIES, BACKGROUNDS, ITEMS, KITS
from talents import definitions

ROOT=pathlib.Path(__file__).resolve().parents[2]
HERE=pathlib.Path(__file__).resolve().parent
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--source',type=pathlib.Path,required=True)
parser.add_argument('--output',type=pathlib.Path,required=True)
args=parser.parse_args()
w=json.loads(args.source.read_text(encoding='utf-8-sig'))
base=copy.deepcopy(w)
manifest=dict(sourceSHA256=hashlib.sha256(args.source.read_bytes()).hexdigest(),newTraits=[],changedTraits=[],newItems=[],newAbilities=[],newProfessions=[],newKits=[],talents=[],uiRenames={},deferred=['Runtime artwork backfill for existing catalogue items remains unverified; no bulk needsMediaGeneration change.'])

def write(path,data):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')

def trait(name,description,attributes=None,skills=None,resources=None,abilities=None,items=None,narrative=None):
    assert name not in w['traits'],name
    t=dict(name=name,description=description,traitNarrativeEffects=narrative or description,
        attributes=[dict(attribute=k,modifier=v) for k,v in (attributes or {}).items()],
        skills=[dict(skill=k,modifier=v) for k,v in (skills or {}).items()],
        resources=[dict(resource=k,modifier=v) for k,v in (resources or {}).items()],
        startingItems=[dict(item=k,quantity=v) for k,v in (items or {}).items()],
        abilities=abilities or [],unlockedBy=[],excludedBy=[],requirements=[])
    w['traits'][name]=t;manifest['newTraits'].append(name)
    return t

def bonuses(t):
    values=[]
    for key,label in [('attributes','attribute'),('skills','skill'),('resources','resource')]:
        for b in t[key]:values.append(f"{b['modifier']:+} {b[label]}"+(' capacity' if key=='resources' else ''))
    return ', '.join(values)

def visual(name,description):
    return trait(name,description,narrative=description+' This is a visual selection for the portrait and clothing description; it grants no item, stat bonus, institutional membership, property, travel or magical ability.')

# Optional affinities, independent studies and a physical alternative at the top.
c=w['traitCategories']['Natural Magical Affinity']
c['description']='Optional — choose zero to three natural affinities, or leave this section empty for no innate affinity. Affinity eases learning; it grants no discipline or spell. Starting Magical Study is separate, and other disciplines can be learned through study or mentorship. Space and Time are unavailable at creation.'
name='Physical Foundations'
trait(name,'Practical physical foundations instead of another starting magical study: +1 Force and +1 Finesse. This choice grants no spell, affinity or combat technique.',attributes={'force':1,'finesse':1})
c=w['traitCategories']['Starting Magical Study'];c['traits'].insert(0,name)
c['description']='Optional — choose up to two entries, or skip. Physical Foundations grants +1 Force and +1 Finesse without magic. Each magical study starts its discipline at skill level 3 and grants its two listed introductory techniques. Studies need not match affinities. Space and Time are unavailable at creation.'

# Native ancestry and temperament bonuses; no compulsive personality or species powers.
ancestries={
 'Human':('A human with individually chosen features, upbringing and profession. Humans are common in Glowhaven and vary widely.',{'intuition':1},{'investigation':2},{'Stamina':10}),
 'Elf':('An elven adult with their chosen ears, features and cultural background. Elvish is represented as French; actual language knowledge still follows the character.',{'finesse':1},{'Perception':2},{'Mana':10}),
 'Dwarf':('A dwarf with individually chosen build, features and ordinary life. Compact stature is common without prescribing a craft or temperament.',{'force':1},{'Guarded Combat':2},{'Stamina':20}),
 'Dragonkin':('A humanoid dragonkin with a human face, horns, slit pupils, selected scales and a thick tail. Ancestry alone supplies no wings, breath weapon or affinity.',{'passion':1},{'athletics':2},{'Health':15}),
 'Fae':('An adult fae with their actual chosen stature and animal or woodland features. Wings, horns, hooves and other details vary; no universal flight or tiny form is assumed.',{'intuition':1},{'acrobatics':2},{'Mana':10}),
 'Beastfolk':('A mostly human adult with selected animal features, such as ears, horns or a tail. More extensively animal-like bodies are rare explicit choices; bird-featured people belong here.',{'finesse':1},{'Perception':2},{'Stamina':15}),
 'Oni':('A humanlike adult oni with distinctive horns and individually chosen hair, eyes and complexion. The ancestry implies no demonic allegiance, compulsory behavior or invented homeland.',{'force':1},{'intimidation':2},{'Health':15}),
 'Mixed Ancestry':('A coherent combination of two established playable ancestries, including a half-elf if chosen. This is one ancestry choice rather than both parents\' mechanical packages.',{'empathy':1},{'Insight':2},{'Health':10}),
}
for name,(desc,attrs,skills,res) in ancestries.items():
    t=w['traits'][name]
    t['attributes']=[dict(attribute=k,modifier=v) for k,v in attrs.items()]
    t['skills']=[dict(skill=k,modifier=v) for k,v in skills.items()]
    t['resources']=[dict(resource=k,modifier=v) for k,v in res.items()]
    t['description']=desc+' Starting benefits: '+bonuses(t)+'.'
    t['traitNarrativeEffects']=t['description']+' These are the actual native modifiers; do not award them again in narration. Preserve the individual body. Ancestry grants no additional affinity, spell, title or compulsory disposition.'
    manifest['changedTraits'].append(name)
w['traitCategories']['Species & Ancestry']['description']='Choose one ancestry, with the listed attributes, skills and resource capacity. Individual anatomy and culture still matter. Profession, personality and magical affinity remain separate choices.'
temperaments={
 'Reserved':('intuition','Insight'),'Outgoing':('empathy','persuasion'),
 'Blunt':('force','intimidation'),'Curious':('logic','investigation'),
 'Competitive':('passion','Tactics'),'Patient':('logic','Medicine'),
 'Restless':('finesse','acrobatics'),'Ambitious':('passion','Trade'),
 'Idealistic':('empathy','persuasion'),'Pragmatic':('logic','Trade'),
 'Playful':('finesse','performance'),'Disciplined':('force','Guarded Combat'),
 'Rebellious':('passion','Deception'),'Warm':('empathy','Medicine'),
 'Sarcastic':('intuition','Deception'),'Cautious':('intuition','Perception'),
 'Expressive':('passion','performance'),'Observant':('intuition','Perception'),
 'Proud':('force','Etiquette'),'Independent':('finesse','survival'),
}
for name,(att,skill) in temperaments.items():
    t=w['traits'][name];desc=t['description'].replace(' (Narrative only.)','')
    t['attributes']=[dict(attribute=att,modifier=1)];t['skills']=[dict(skill=skill,modifier=1)]
    t['description']=desc+' Starting benefits: '+bonuses(t)+'.'
    t['traitNarrativeEffects']=t['description']+' The modifiers apply once through the trait. Actual speech, choices, feelings and relationships remain the player\'s; this tendency is not compulsory behavior or a hidden moral alignment.'
    manifest['changedTraits'].append(name)
w['traitCategories']['Temperament']['description']='Optional — choose up to two tendencies or skip. Each grants its listed small attribute and skill benefit. Actual speech, feelings and decisions remain yours.'
# Leave room for the now-meaningful ancestry, temperament and talent selections.
w['attributeSettings']['maxStartingAttribute']=20

# Thirty-six additional professions and comparable breadth for preceding choices.
supports={'Merchant Apprentice':'Insight','Research Assistant':'Perception','Medical Assistant':'Insight','Alchemist Apprentice':'investigation','Magitech Technician':'investigation','Field Scout':'Perception','Cook':'Trade','Perfumery Apprentice':'Trade','Animal Caretaker':'survival','Performer':'Etiquette','Courier':'survival','Community Coordinator':'persuasion'}
for name,skill in supports.items():
    t=w['traits'][name]
    t['skills'].append(dict(skill=skill,modifier=1))
    t['description']=t['description'].rstrip('.')+f'; +1 {skill}.'
    manifest['changedTraits'].append(name)
groups={'Craft and Workshop':[],'Study, Care and Records':[],'Trade, Hospitality and Performance':[],'Fieldwork and Public Service':[]}
for name,history,primary,support in PROFESSIONS:
    desc=f'Prior experience with {history}. Begin with +2 {primary} and +1 {support}.'
    trait(name,desc,skills={primary:2,support:1},narrative=desc+' This is prior practical experience, not a current appointment, professional licence, owned premises, free tools, fame or an automatic academy subject. Language work uses only languages actually learned.')
    manifest['newProfessions'].append(name)
c=w['traitCategories']['Profession & Useful Skills'];c['traits']+=manifest['newProfessions']
for name in c['traits']:
    if name in ['Blacksmith Apprentice','Armorer','Carpenter','Mason','Tailor','Jeweler','Glassblower','Bookbinder','Magitech Technician']:g='Craft and Workshop'
    elif name in ['Scribe','Archivist','Interpreter','Tutor','Research Assistant','Medical Assistant','Alchemist Apprentice','Perfumery Apprentice','Herbalist']:g='Study, Care and Records'
    elif name in ['Merchant Apprentice','Accountant','Appraiser','Innkeeper','Tavern Worker','Baker','Tea Blender','Cook','Performer','Stage Magician','Dancer','Musician']:g='Trade, Hospitality and Performance'
    else:g='Fieldwork and Public Service'
    groups[g].append(name)
c['subcategories']=[dict(name=g,traits=ns) for g,ns in groups.items()]
c['description']='Optional — choose one prior profession or practical background. Each grants +2 in its main skill and +1 in a supporting skill. These are starting experiences, not current employment, official licences, owned workplaces or free professional equipment.'

# Forty-eight talents share one optional choice; stronger benefits carry actual costs.
talent_groups={}
for row in definitions():
    abilities=[];ability=row['ability'];name=row['name']
    if ability:
        assert ability['name'] not in w['abilities'],ability['name']
        record={**ability,'requirements':[dict(type='trait',variable=name,amount=1)]}
        w['abilities'][ability['name']]=record;abilities=[ability['name']]
        manifest['newAbilities'].append(ability['name'])
    t=trait(name,row['description'],row['attributes'],row['skills'],row['resources'],abilities,
        narrative=row['description']+' Apply only the listed native bonuses and explicitly granted technique. This gift creates no additional affinity, unlimited resource, visible divine mark, god\'s personal acquaintance, social authority or automatic success. Actual costs and cooldowns apply. Its origin may be a blessing, unusual birth or exceptional practice compatible with the player\'s chosen background.')
    for field in ['resistances','vulnerabilities']:
        if row[field]:t[field]=row[field]
    details=bonuses(t)
    if abilities:details+='; technique: '+abilities[0]
    if row['resistances']:details+='; resistance: '+', '.join(row['resistances'])
    if row['vulnerabilities']:details+='; vulnerability: '+', '.join(row['vulnerabilities'])
    t['description']+=' Benefits and trade-offs: '+details+'.'
    talent_groups.setdefault(row['group'],[]).append(name);manifest['talents'].append(name)
category=dict(name='Special Talent',maxSelections=1,traits=manifest['talents'],
 description='Optional — choose one unusual gift, blessing or exceptional aptitude, or skip. Benefits are substantial but bounded; stronger gifts have the listed trade-offs. A granted discipline or technique is learned as stated without adding an affinity. No Space, Time, automatic authority or compulsory deity relationship is included.',
 subcategories=[dict(name=g,traits=ns) for g,ns in talent_groups.items()])
cats={}
for name,c in w['traitCategories'].items():
    if name=='Starting Equipment':cats['Special Talent']=category
    cats[name]=c
w['traitCategories']=cats

# Appearance expansion. All visual choices remain mechanically empty.
appearance=w['traitCategories']['Appearance Builder']
hair=next(x for x in appearance['subcategories'] if x['name'].startswith('Hair Style'))
name='Hair Style — Bald'
visual(name,'A visibly bald scalp, with no head hair. Preserve chosen facial hair if any. Hair-color choices do not create head hair or hidden long strands.');hair['traits'].insert(0,name)
outfit=next(x for x in appearance['subcategories'] if x['name'].startswith('Outfit'))
for label,desc in OUTFITS:
    name='Outfit — '+label;visual(name,'Wear '+desc+'.');outfit['traits'].append(name)
access_groups=[];access_names=[]
for g,entries in ACCESSORIES.items():
    names=[]
    for label,desc in entries:
        name='Accessory — '+label;visual(name,'Add '+desc+'. Keep it compatible with the actual body, outfit and selected framing.');names.append(name);access_names.append(name)
    access_groups.append(dict(name=g,traits=names))
access_cat=dict(name='Accessories & Outer Layers',maxSelections=4,traits=access_names,subcategories=access_groups,
 description='Optional — add up to four compatible visual details over your selected outfit, or skip. Hats, outer layers, glasses and jewelry are appearance choices. They grant no equipment bonuses, possessions, official insignia or magical powers. Avoid incompatible duplicate hats or layers unless explicitly intended.')
cats={}
for name,c in w['traitCategories'].items():
    cats[name]=c
    if name=='Appearance Builder':cats['Accessories & Outer Layers']=access_cat
w['traitCategories']=cats
frames=[
 ('Bust portrait','A close bust portrait showing the complete head, shoulders and upper chest, with expressive face and coherent costume details.'),
 ('Face close-up','A dramatic face-focused close-up with the whole face legible. A deliberate selected close crop may trim hair or hat edges; do not stretch the body to force a waist-up view.'),
 ('Three-quarter body','A vertical three-quarter-body portrait extending to roughly the knees, with a readable face and coherent proportions.'),
 ('Full-body illustration','A full-body character illustration with coherent anatomy, readable face and feet in frame. Keep the established crisp 2D anime style.'),
 ('Seated portrait','A seated character portrait with a clear face, hands placed coherently and a readable upper-body silhouette.'),
 ('Wide action portrait','A wider action-oriented portrait with a dynamic pose grounded in the actual body and gear. It does not depict an unearned power or completed fight.'),
]
c=w['traitCategories']['Portrait Framing'];defaults=c['traits'].copy();extra=[]
for label,desc in frames:
    name='Portrait Frame — '+label;visual(name,desc);extra.append(name)
c['traits']+=extra;c['subcategories']=[dict(name='Default',traits=defaults),dict(name='Eccentric Choices',traits=extra)]
c['description']='Optional — skip for a fitting waist-up or hip-up portrait. Default contains our usual framing. Eccentric Choices offers deliberately different crops and poses; an explicit selection takes priority over the default.'
angles=[
 ('Dramatic low angle','View the character from a dramatic low angle, preserving coherent face and body proportions.'),
 ('Dramatic high angle','View the character from a dramatic high angle with a clear face and intentional perspective.'),
 ('Bird\'s-eye view','Use a steep overhead viewpoint with a deliberately composed readable character silhouette.'),
 ('Ground-level view','Use a low ground-level viewpoint with intentional foreshortening and a readable face.'),
 ('Strong Dutch angle','Use an emphatic tilted camera composition while preserving coherent anatomy and a legible face.'),
 ('Side profile','Use a clean deliberate side-profile view of the actual face and body.'),
 ('Over-the-shoulder','View the character over one shoulder, with the head turned enough to reveal the face.'),
 ('Foreshortened gesture','Use a dynamic near-to-far gesture and controlled foreshortening, with hands and gear connected correctly.'),
 ('Distant observer','Use a slightly distant observational viewpoint suited to the selected frame, with the person still clearly identifiable.'),
 ('Intimate eye line','Use a close, direct eye line and quietly expressive face without imposing romance or player emotion.'),
]
c=w['traitCategories']['Portrait Camera'];defaults=c['traits'][:2];extra=c['traits'][2:]
for label,desc in angles:
    name='Portrait Camera — '+label;visual(name,desc);c['traits'].append(name);extra.append(name)
c['subcategories']=[dict(name='Default',traits=defaults),dict(name='Eccentric Choices',traits=extra)]
c['description']='Optional — choose a viewpoint or skip. Default uses a natural eye-level or three-quarter view. Eccentric Choices offers dramatic and unusual perspectives; keep the actual face and anatomy coherent.'
c=w['traitCategories']['Portrait Style']
c['subcategories']=[dict(name='Default',traits=c['traits'][:1]),dict(name='Alternate Illustration Styles',traits=c['traits'][1:])]
c=w['traitCategories']['Portrait Background'];defaults=c['traits'][:1]
for label,desc in BACKGROUNDS:
    name='Portrait Background — '+label;visual(name,'Set the portrait against '+desc+'. This is picture scenery rather than a claim about your current location.');c['traits'].append(name)
c['subcategories']=[dict(name='Default',traits=defaults),dict(name='Places and Atmosphere',traits=c['traits'][1:])]

# Real catalogue objects and separately selected starting kits.
for name,desc,category,slot,tier,value,bonus in ITEMS:
    assert name not in w['itemTypes'],name
    it=dict(name=name,description=desc,category=category,tier=tier,estimatedValue=value,bonuses=[])
    if slot:it['slot']=slot
    if bonus:it['bonuses']=[dict(type=bonus[0],variable=bonus[1],value=bonus[2])]
    w['itemTypes'][name]=it;manifest['newItems'].append(name)
for name,items in KITS.items():
    desc='Begin with '+', '.join(items)+'. This is ordinary usable equipment; it grants no skill, spell, affiliation or mastery.'
    trait(name,desc,items={i:1 for i in items},narrative=desc+' Supply only the configured startingItems once. No second narrative grant or extra purse accompanies the kit.')
    w['traitCategories']['Starting Equipment']['traits'].append(name);manifest['newKits'].append(name)
oldkits=w['traitCategories']['Starting Equipment']['traits']
w['traitCategories']['Starting Equipment']['subcategories']=[
 dict(name='Casting Implements',traits=[n for n in oldkits if n in ['Wand Kit','Staff Kit','Grimoire Kit','Hand-Casting Practice','Focus Cord Kit','Crystal Focus Kit','Casting Card Kit']]),
 dict(name='Martial Equipment',traits=[n for n in oldkits if n not in ['Wand Kit','Staff Kit','Grimoire Kit','Hand-Casting Practice','Focus Cord Kit','Crystal Focus Kit','Casting Card Kit','Field Survey Kit','Workshop Starter Kit','First Aid Kit','Technical Inspection Kit']]),
 dict(name='Practical Work',traits=[n for n in oldkits if n in ['Field Survey Kit','Workshop Starter Kit','First Aid Kit','Technical Inspection Kit']])]

# The user's explicit text requests 100; their exported 80% rest recovery is retained.
st=w['resourceSettings']['Stamina'];st['initialValue']=100;st['maxValue']=100
st['usageInstructions']=st['usageInstructions'].replace('A genuinely completed rest restores the pool through restRechargeMultiplier 1.','A genuinely completed rest restores 80% of the current maximum through restRechargeMultiplier 0.8, capped at that maximum.')
st['usageInstructions']=st['usageInstructions'].replace('Capacity starts at 80','Capacity starts at 100')

# Exact ownership for badge grants. Do not create an alternate catalogue entry to remove it.
key='Keys, Credentials and Information Items'
w['aiInstructions']['ItemGenerationAndUsage'][key]='''CREDENTIALS AND SINGLE GRANTS
Guild badges have exactly four catalogue identities: Guild Badge: Bronze, Guild Badge: Silver, Guild Badge: Gold and Guild Badge: Platinum. All are Documents. Their typed licensure/promotion effects own issuance and exchange. This item task must not add another badge for a narrated ceremony or define an alias such as Bronze Guild Badge, Adventurer Badge or a Relic version. An existing badge shown or mentioned is the same object. High level, a profession or a claimed licence grants none. Preserve actual images and quantities. Ordinary new unrelated objects can still be generated.

KEYS AND RECORDS
Use the exact existing type for keys, route tokens, admission packets, appointment letters, custody receipts and installed-goods receipts. State the actual place, issuer, holder and agreement. A receipt records the installed object; it is not a portable duplicate. Authorization and supported issuance determine acquisition. Status, a claim, a drawing or a mention grants no court key. Follow actual destinations, return points and reuse; do not consume reusable keys or grant a fresh copy on each trip. A lost credential needs a real replacement agreement.

An acquisition is applied once by its owner. When a typed effect supplies an item, this task neither grants a second copy nor invents a new definition for the narrated handover. Preserve actual transfers and custody.'''
t=w['triggerDefinitions']['gh_guild_exam_certify']
for e in t['effects']:
    if e['type']=='story':e['instruction']='Describe the clerk completing the actual licensure and handing over the already-granted Document Guild Badge: Bronze. The typed grant is the sole inventory award; no item-generation task should add a badge, redefine it as a Relic or create an alias. Bronze work is now available by its actual rules. No portal key, weapon, extra payment or automatic promotion accompanies the ceremony.'
q=w['parties']['']['quests'].get('Guild: Adventurer Licensure')
if q:
    q['questDesignBrief']=q.get('questDesignBrief','')+'\nThe certification trigger exclusively awards the existing Document Guild Badge: Bronze. Do not also put a badge in generated quest rewards or create a renamed Relic for the same licence.'

# Music uses native scene cues for sharp state changes, not ambiguous topic words.
tracks=w['gameplayMusicSettings']['tracks']
for name,cue in [('Fighting','combat'),('Dead','dead'),('Travelling','travel')]:
    tracks[name]['matchTags']=[]
    tracks[name]['cues']=[cue]
tracks['Pursued']['matchTags']=['active pursuit','being chased','fleeing immediate danger','hunted']
tracks['Triumphant']['matchTags']=['victory','triumph','achievement','winning','victorious']
tracks['Apprehensive']['matchTags']=['dread','ominous','lurking','threatening','tense','anxious','uneasy','foreboding','suspicious','nervous']
tracks['Distraught']['matchTags']=['distress','turmoil','betrayal','anguish','desperate','troubled','accusation','rejection','bitter']
tracks['Awestruck']['matchTags']=['wonder','magnificent','revelation','overwhelming','majestic','breathtaking','awe','mystical','grandeur']
tracks['Eulogizing']['matchTags']=['mourning','memorial','funeral','grave']
tracks['Morose']['matchTags']=['melancholy','somber','gloomy','lonely','bleak','sorrowful','resigned','regret','desolate']
tracks['Unconscious']['matchTags']=['unconscious','trance','sleep','dreamlike']
w['aiInstructions']['generateStory']['Present Scene and Music']='Music-related mood/context describes what is happening now. Calm discussion of a battle, combat lesson, weapon purchase, hypothetical threat or remembered fight is not current combat. Describe ordinary instruction, conversation and aftermath in their actual present tone. Reserve active-combat context for actual fighting; travel for actual travel; death for an actual death; pursuit for an actual chase. Do not insert a fight, chase, tragedy or announcement to justify a soundtrack. Mood descriptions add no victory, damage, movement or other game-state change.'
w['aiInstructions']['generateNewNPC']['Power Anchors and Professional Breadth']+='\nOrdinary working adventurers commonly occupy levels 20–30. Badge rank alone does not require level 40 or a stronger tier. Preserve specifically authored exceptional veterans.'

# Portrait overrides apply only to an explicitly customized player picture.
notes=w['aiInstructions']['generateCharacterBackground']
notes['Appearance Construction and Support']='''APPEARANCE SOURCES
Use selected hair, eyes, skin, build, outfit, accessories, Beastfolk/Fae form and stature. Written appearance resolves conflicts. Bald or shaved scalps override hair-color selections: do not invent head hair. Optional choices that are skipped invite compatible design, not powers, items, affiliation or property. Preserve the adult body and actual species anatomy.

PLAYER OUTPUT ROUTE
Begin Appearance with exactly: ## GLOWHAVEN PLAYER PORTRAIT
Write one concise complete image brief: art direction, identity, clothing and selected accessories, gesture, framing, viewpoint and background. It is an image prompt, not a new history. No visible headings or writing in the picture.

DEFAULT AND SELECTED COMPOSITION
The default is a polished colorful hand-drawn 2D fantasy-anime key visual, with crisp varied ink lines, expressive anime eyes, clean hair shapes and graphic cel shadows. Without a framing selection, use a full head and a fitting waist-up or hip-up portrait. Without camera/background choices, use a natural eye-level or three-quarter view and fitting opening-place cues.
An explicit Portrait Framing or Camera choice takes priority: a bust, face close-up, full-body or dramatic viewpoint should actually look different. A deliberate close-up can crop outer hair/hat edges; do not force every selected composition back to waist-up. Preserve coherent anatomy, face identity and any visible real gear. Accessories layer over the outfit; optional visual props create no stat-bearing inventory or unearned mastery.

FINISH
Use drawn faces, crisp cel shadows and selective painted accents. Avoid CGI, beveled 3D facial edges, plastic skin, pores, photographic hair, unwanted blur, extra limbs, text, logos, watermark, borders and UI. A background styles the picture and never moves the character or establishes ownership.'''
notes['Appearance Depth and Visual Continuity']='Design one memorable 2D anime silhouette and individual face. Selected colors, outfit and accessories anchor the palette. Keep facial edges drawn and shadows graphic. Show enough costume for the selected framing; close-up and full-body selections override the usual waist/hip-up default. Preserve the actual body, age, species, hair, eyes and visible gear. Hats and layered accessories fit the chosen anatomy. Picture style, pose, viewpoint and backdrop do not grant possessions, magic, affiliations or travel. Existing approved portraits retain their identity and URL unless regeneration is requested.'
notes['custom']+='\nOptional affinity left empty means no chosen innate affinity, not permission to invent one. Physical Foundations grants only its actual Force/Finesse bonuses. Honor a selected Special Talent and its exact listed skills, resources, trade-offs and granted technique; it is not blanket mastery or another affinity. A personality choice may change listed mechanics without authorizing invented player actions or feelings.'
notes['Attribute and Skill Fidelity']=notes['Attribute and Skill Fidelity'].replace('Logic: Arcane, Metal, Gravity, Enchantment.','Logic: Arcane, Metal, Gravity, Enchantment, Space.').replace('Empathy: Healing, Nature, Light, Summoning.','Empathy: Healing, Nature, Light, Summoning, Soul.')
notes['prompt']=notes['prompt'].replace('Deliver its complete art direction, frame and lighting brief;','Deliver its complete art direction and chosen composition;')
prompt=w['imagePromptConfiguration']['npcs']
prompt=prompt.replace('Vertical waist-up or hip-up portrait, complete head and hairstyle visible, a clear expression and enough costume to read the silhouette.','Default to a vertical waist-up or hip-up portrait, complete head and hairstyle visible, a clear expression and enough costume to read the silhouette. For a marked player portrait, an explicit selected crop or viewpoint overrides this default, including bust, face close-up, full-body and dramatic perspective.')
prompt=prompt.replace('hair colors, hairstyle, build, outfit and species anatomy.','hair colors, hairstyle, build, outfit, selected accessories and species anatomy. A selected bald or shaved scalp has no invented head hair.')
prompt=prompt.replace('clipped head, distant full-body view.','unintentional face clipping or an unrequested distant view. Explicit player framing can deliberately crop outer hair or hat edges, or show the whole body.')
w['imagePromptConfiguration']['npcs']=prompt

# Use established, widely supported emoji for affected menu titles and exact references.
renames={name:name.replace('🪶','📘').replace('🪻','💜').replace('🪙','💰') for name in w['storyStarts'] if any(c in name for c in ['🪶','🪻','🪙'])}
def rename_refs(value):
    if isinstance(value,dict):return {renames.get(k,k):rename_refs(v) for k,v in value.items()}
    if isinstance(value,list):return [rename_refs(v) for v in value]
    if isinstance(value,str):
        for old,new in renames.items():value=value.replace(old,new)
    return value
w=rename_refs(w);manifest['uiRenames']=renames

# Preservation evidence and a role-aware, non-prescriptive level comparison.
def digest(x):return hashlib.sha256(json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode('utf-8')).hexdigest()
media=[]
def visit(value,path):
    if isinstance(value,dict):
        for k,v in value.items():
            if k in ['imageUrl','portraitUrl','narrationUrl','gameplayUrl','url','voiceTag']:media.append(dict(path=path+[k],value=v))
            else:visit(v,path+[k])
    elif isinstance(value,list):
        for i,v in enumerate(value):visit(v,path+[i])
visit(base,[])
manifest['uiReferenceTriggers']=[k for k,v in base['triggerDefinitions'].items() if v!=rename_refs(v)]
manifest['preservation']=dict(media=media,npcs={k:digest(v) for k,v in base['npcs'].items()},locations=digest(base['locations']),realms=digest(base['realms']),regions=digest(base['regions']),musicVariants={k:v['variants'] for k,v in base['gameplayMusicSettings']['tracks'].items()},originalItems={k:digest(v) for k,v in base['itemTypes'].items()},originalAbilities={k:digest(v) for k,v in base['abilities'].items()},triggers={k:digest(rename_refs(v)) for k,v in base['triggerDefinitions'].items() if k!='gh_guild_exam_certify'},quests={k:digest(rename_refs(v)) for k,v in base['parties']['']['quests'].items() if k!='Guild: Adventurer Licensure'})
manifest['levelAudit']={}
for title,path in [('Glowhaven',args.source),('Luxcellia',ROOT/'sources/Luxcellia.json'),('Chikara',ROOT/'sources/ChikaraOld.json')]:
    data=json.loads(path.read_text(encoding='utf-8-sig'));ns=data['npcs']
    levels=[n['level'] for n in ns.values() if isinstance(n.get('level'),(int,float)) and n['level']>0]
    bytype={}
    for name,n in ns.items():
        if n.get('type')=='Adventurer':bytype[name]=n.get('level')
    manifest['levelAudit'][title]=dict(positiveLevelCount=len(levels),median=statistics.median(levels),adventurerType=bytype)
manifest['artwork']=dict(imageGenerationEnabled=w['itemSettings'].get('imageGenerationEnabled'),needsMediaGenerationChanges=0,tooltip='Controls whether needs media generation applies to this item.',browserInspection='Failed before page access: Windows sandbox helper lock/access error. No live runtime test performed.')
write(args.output,w);write(HERE/'manifest.json',manifest)
print(json.dumps({k:len(manifest[k]) for k in ['newTraits','changedTraits','newItems','newAbilities','newProfessions','newKits','talents']},ensure_ascii=False))
