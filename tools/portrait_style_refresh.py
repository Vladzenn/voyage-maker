"""Apply the November portrait direction without changing gameplay or existing media.

Import apply(world) from an expansion builder, or use --world/--output for a
reviewable standalone merge. This never generates or replaces a portrait.
"""
import argparse
import copy
import json
from pathlib import Path

STYLE = (
    'Premium fantasy RPG anime character illustration, with the presence and finish of a main-character key visual: '
    'fine, confident linework, expressive individually designed anime eyes, layered painted shading with soft gradients, '
    'richly detailed hair and clothing, luminous directional light and atmospheric depth. '
    'Combine clear drawn contours with delicate transitions of light across skin, fabric, leather and metal. '
    'Keep the face distinctly anime and the materials beautifully illustrated.'
)

ACADEMIES = {
    'Phoenix Wing': ('crimson red', 'a phoenix bird with spread wings'),
    'Hydra Head': ('violet purple', 'a many-headed hydra'),
    'Gryffin Tail': ('cyan blue', 'a winged gryffin'),
    'Dragon Hoard': ('yellow and gold', 'a dragon'),
}
UNIFORMS = '; '.join(f'{n}: {color}, {emblem} emblem' for n,(color,emblem) in ACADEMIES.items()) + '.'

IMAGE = '''ART DIRECTION
''' + STYLE + '''
Design one memorable individual: a readable silhouette, a personality-specific expression and a convincing gesture. Give player characters the same visual care as the leading authored cast, whether civilian, warrior or mage. Detail, lighting and costume design create presence; ornate rank, huge weapons and powerful magic are not required. A chosen alternative illustration style can change the finish. Maintain the actual person and avoid a compulsory glamorous face, smile, warm palette or battle pose.

PLAYER BRIEF AND SOURCE ORDER
If Appearance begins with ## GLOWHAVEN PLAYER PORTRAIT, use the complete supplied visual brief, including explicit style, framing, camera and background choices. Carry its concrete identity and clothing details into the image rather than restating a vague category label. Otherwise use visualDescription, selected visual traits and the NPC Type's anatomy; use role and setting only to fill genuine gaps. Honor a written appearance over conflicting cosmetic selections. Existing portraits keep their identity unless a new generation is requested.

IDENTITY AND ANATOMY
Preserve the actual age presentation, body, skin, hair, eyes, clothing and selected accessories. Bald means no head hair. Long-lived adults do not become elderly merely through a large chronological age or senior job. Short adult fae retain adult proportions. Beastfolk usually have human faces and bodies with the selected animal features; use more animal-like anatomy only when specified. Preserve individual horns, wings, tails, scales and limb count; do not add universal fae wings. Keep hands anatomically coherent. A spear or staff has a single continuous shaft, aligned grips and an attached head.

COMPOSITION AND LIGHT
Without a selected alternative, use a vertical waist-up or hip-up portrait with the complete head and hair, comfortable headroom and a natural eye-level or three-quarter view. Explicit close-up, full-body, seated or dramatic-camera selections override that default. Keep face and eyes the focal point, with enough outfit to read the design. A subtle weight shift, moving hair or a purposeful hand can give life to a quiet character. Use a specific supplied backdrop or an appropriate opening-place setting, rendered more softly behind the subject. Lighting and colors vary with person and place; do not blur away all environmental detail.

CLOTHING AND MAGIC
Academy uniforms must state and show the chosen school's color and embroidered creature crest: ''' + UNIFORMS + ''' Use its color as a substantial part of the uniform, not just a tiny ribbon; put one readable creature badge on the breast, collar or shoulder. A pictorial academy crest is permitted; no written school name, letter crest or commercial logo. Resolve the school from an explicit school-specific outfit, otherwise the selected academy start or established affiliation. If none identifies a school, use ordinary scholarly clothing without inventing enrollment. Faculty wear an instructor's cut; students a practical uniform. Preserve individual tailoring and selected accessories.
Use only supplied magic and actual gear. When magical effects are indicated, make them vivid, translucent and spatially integrated with hand, weapon or environment; keep the face clear. Their scale fits actual training. A civilian can have a striking portrait without a spell effect. Picture styling never grants equipment, powers, status, affiliations, property or travel.

AVOID
Photographs, live action, CGI/3D renders, plastic skin, realistic pores, doll faces, beveled facial planes, muddy overpainting, duplicate limbs or hands, disconnected weapons, substituted identity, unrequested crowd foregrounds, text, lettering, signatures, watermarks, poster borders, UI and character sheets. One focal character. Illustrated metal highlights and softly modeled anime shading are welcome; do not flatten every surface into hard shadow blocks.
'''

APPEARANCE = '''APPEARANCE SOURCES
Use selected hair, eyes, skin, build, outfit, accessories and individual Beastfolk/Fae anatomy. Written appearance resolves conflicts. Bald or shaved scalps override hair-color selections. Preserve actual age presentation and species. Skipped choices invite compatible visual design, not new possessions, powers or affiliations.

FINAL PLAYER IMAGE BRIEF
Begin Appearance with exactly: ## GLOWHAVEN PLAYER PORTRAIT
Write one coherent, self-contained image brief in this order: art direction; individual identity and expression; concrete clothing and accessories; gesture and framing; camera; setting and light. This is the visual handoff, not a new biography. Replace labels such as "academy clothes" with actual colors, garment cut and emblem. Do not assume the image generator has access to the selected start, lore or other fields.

DEFAULT ART DIRECTION
''' + STYLE + '''
Make the player the unmistakable focal character through silhouette, expression, costume detail and light. An ordinary outfit can be thoughtfully designed. Do not invent a noble title, expensive gear, an altered body or a spectacular spell merely to make the picture impressive. Follow an explicit alternative Portrait Style.

ACADEMY CLOTHES
''' + UNIFORMS + '''
For an explicit school-specific outfit use that school; for the generic academy student/faculty outfit resolve the selected academy Story Start or established school. Include the full school name, substantial uniform-color panels, and one embroidered pictorial creature crest on breast, collar or shoulder in the final brief. Use a student uniform or instructor's coat/robes as selected; preserve the chosen person's build, individual tailoring and accessories. An emblem has no letters or school-name text. If no school is established, use ordinary scholarly clothing without inventing affiliation. Cosmetic uniform selection alone confers no membership.

COMPOSITION
Defaults: whole head and hair with comfortable breathing room, waist-up or hip-up, natural eye-level or three-quarter view. Explicit Portrait Framing, Camera and Background choices override those defaults, including deliberate close-ups and full-body pictures. A close-up may trim outer hair or hat edges while preserving the face. A picture backdrop never moves the character or grants ownership. Layer selected accessories over the outfit; use actual held gear only.

FINISH
Favor fine linework, dimensional illustrated materials, soft layered shading, lively hair and fabric, and lighting appropriate to the actual setting. Keep the face anime; no photographic skin, plastic CGI, broken anatomy, text, watermark or UI. One focal person. Effects, when supported, are clear and expressive without obscuring face or clothing. Output only the final visual brief in the Appearance field; do not include save paths, internal validation steps or this instruction text.
'''

CONTINUITY = '''VISUAL CONTINUITY
Design one individual face and silhouette with the finish of a leading fantasy RPG character illustration: fine expressive drawing, soft layered shading, detailed illustrated materials and fitting atmospheric light. Selected identity, age presentation, body, clothing and accessories remain authoritative. Avoid a stock glamour face or mandatory combat pose. An explicit alternative style/crop/viewpoint takes priority over the defaults. Resolve academy uniforms into their actual colors and pictorial creature crests before handing off the final brief. Keep hats and accessories compatible with the person's anatomy. Visual choices do not grant possessions, magic, affiliation or travel. Existing approved portraits retain their identity and URL unless regeneration is requested.'''

STYLES = {
    'Crisp fantasy anime': ('Fantasy RPG illustration', 'A leading-character fantasy RPG illustration: fine anime linework, softly layered painted shading, detailed clothing and materials, expressive eyes and luminous light.'),
    'Dramatic gacha illustration': (None, 'A lavish anime character key visual with flowing costume, dimensional painted shading, dramatic light and vivid supported magical motifs. Preserve a clear face and an individual silhouette.'),
    'Elegant linework': (None, 'Fine, graceful anime drawing with intricate costume detail, delicate light transitions and softly painted materials. An elegant individual portrait with a clear face and purposeful gesture.'),
    'Watercolor accents': (None, 'A carefully drawn anime character with soft watercolor color transitions, delicate edges and atmospheric washes. Keep the face and costume readable while allowing the medium to shape the illustration.'),
}

def apply(w):
    w['imagePromptConfiguration']['npcs'] = IMAGE.strip()
    ai=w['aiInstructions']['generateCharacterBackground']
    ai['Appearance Construction and Support']=APPEARANCE.strip()
    ai['Appearance Depth and Visual Continuity']=CONTINUITY.strip()
    for old,(new,description) in STYLES.items():
        key='Portrait Style — '+old
        if key not in w['traits'] and new:key='Portrait Style — '+new
        t=w['traits'][key]
        t['description']=description
        t['traitNarrativeEffects']=description+' Image direction only; preserve the actual identity, species, clothing and equipment. No powers, status or possessions are granted.'
        if new:
            nk='Portrait Style — '+new;t['name']=nk
            w['traits']={nk if k==key else k:v for k,v in w['traits'].items()}
            c=w['traitCategories']['Portrait Style']
            c['traits']=[nk if k==key else k for k in c['traits']]
            for s in c.get('subcategories',[]):s['traits']=[nk if k==key else k for k in s['traits']]
    w['traitCategories']['Portrait Style']['description']='Optional — skip for our default fantasy RPG character illustration: fine anime drawing, soft layered shading, detailed outfits and luminous lighting. Alternative styles change the picture, not the character’s abilities.'
    for role in ['student','faculty']:
        t=w['traits']['Outfit — Academy '+role]
        t['description']=('A practical student uniform' if role=='student' else 'An instructor’s tailored coat or robes')+' with your academy’s colors and embroidered creature crest.'
        t['traitNarrativeEffects']=t['description']+' Resolve the academy from the selected academy start or established affiliation and write its full name, color and emblem into the final Appearance brief: '+UNIFORMS+' If no school is identified, use ordinary scholarly clothes. A pictorial embroidered crest is permitted without lettering. Clothing alone grants no enrollment, employment, equipment or bonuses.'
    c=w['traitCategories']['Appearance Builder']; group=next(s for s in c['subcategories'] if s['name'].startswith('Outfit —'))
    at=group['traits'].index('Outfit — Academy faculty')+1
    added=[]
    for school,(color,emblem) in ACADEMIES.items():
        name='Outfit — '+school+' uniform'
        t=copy.deepcopy(w['traits']['Outfit — Academy student'])
        t['name']=name
        t['description']=f'{school} Academy’s {color} uniform with an embroidered {emblem} crest; choose an individual cut and accessories.'
        t['traitNarrativeEffects']=f'In the final portrait brief, explicitly describe {school} Academy clothing: substantial {color} cloth panels and one embroidered pictorial {emblem} crest on breast, collar or shoulder. Use a student cut, or an instructor’s coat/robes if the actual character is faculty. No lettering. Preserve the person and selected accessories. This is a cosmetic outfit, not membership, employment, inventory or a mechanical bonus.'
        w['traits'][name]=t;added.append(name)
    # Idempotent, retaining all preexisting outfit and category order.
    group['traits']=[x for x in group['traits'] if x not in added]
    group['traits'][at:at]=added
    if 'Outfit — Academy faculty' in c.get('traits',[]):
        c['traits']=[x for x in c['traits'] if x not in added]
        pos=c['traits'].index('Outfit — Academy faculty')+1
        c['traits'][pos:pos]=added
    assert len(w['imagePromptConfiguration']['npcs'].encode('utf-16-le'))//2<=5000
    return {'changedExistingTraits':6,'addedCosmeticOutfits':added,'imagePromptUtf16':len(IMAGE.strip().encode('utf-16-le'))//2}

def main():
    p=argparse.ArgumentParser();p.add_argument('--world',required=True);p.add_argument('--output',required=True)
    a=p.parse_args();w=json.loads(Path(a.world).read_text(encoding='utf-8-sig'));report=apply(w)
    Path(a.output).write_text(json.dumps(w,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False))
if __name__=='__main__':main()
