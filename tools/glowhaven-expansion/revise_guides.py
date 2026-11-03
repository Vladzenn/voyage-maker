"""One-time rendering-language clarification; preserve NPC composition rules."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/'research/Player Portrait Creation - Current Defaults.md'
s=p.read_text(encoding='utf-8-sig')
s=s.replace('Default to a polished, colorful hand-drawn 2D fantasy-anime illustration with crisp variable linework, expressive anime eyes, clear hair shapes and graphic cel shadows.','Default to a premium fantasy RPG anime character illustration: fine confident linework, expressive individual anime eyes, layered painted shading with soft gradients, detailed illustrated hair and clothing, luminous directional light and atmospheric depth. Give the player the visual care of a leading cast member without changing their body, age, status, equipment or power.')
if '3 November gallery review' not in s:s+='\n\nThe 3 November gallery review refines rendering without changing the flexible player crop/camera policy. Resolve academy outfits into actual colors and an embroidered pictorial creature crest before producing the final image brief. Explicit school-uniform options identify the school directly; generic student/faculty choices use the selected school start or established affiliation. See [the review](Portrait%20Style%20and%20Academy%20Uniform%20Review%20-%202026-11-03.md).\n'
p.write_text(s,encoding='utf-8')
p=ROOT/'research/Portrait Creation Format.md';s=p.read_text(encoding='utf-8-sig')
old='- **Style:** The image must read unmistakably as a polished **2D anime illustration**: stylized anime facial proportions, expressive anime eyes, deliberate clean linework, graphic shape design, and anime-style hair, fabric, and light rendering. Use crisp details and a pristine finish, while allowing each portrait a distinct palette and mood; let the cast feel colorful and varied without prescribing one saturation level.'
new='- **Style:** Use a premium fantasy RPG anime character illustration: fine confident linework, expressive individual anime eyes, layered painted shading with soft gradients, intricate clothing and illustrated materials, luminous directional light and atmospheric depth. Keep the face distinctly anime. Clear contours and softly modeled color can coexist; do not flatten every surface into hard graphic shadow blocks. Let each portrait have its own palette, expression and lighting. Presence comes from design and a convincing gesture, not obligatory glamour, ornate rank or a battle pose.'
s=s.replace(old,new).replace('Create a single polished **2D fantasy-anime illustration** of **[NPC full name]**','Create a single premium **fantasy RPG anime character illustration** of **[NPC full name]**').replace('clean deliberate linework, graphic shapes, and anime-style hair, fabric, and lighting.','fine confident linework, layered painted shading with soft gradients, detailed illustrated hair and clothing, and luminous setting-appropriate light.')
p.write_text(s,encoding='utf-8')
p=ROOT/'tools/glowhaven-expansion/cast.py';s=p.read_text(encoding='utf-8')
replacements={
 'Fighting Style: A dangerous level-45 animal that uses jaws, coils and water. It remains at this authored resting site unless an actual scene changes that state. Sleep is not a guarantee that an attacker can kill it without a response.':'Fighting Style: Defends its familiar reef with sweeping coils, a powerful bite and gathered water. A slow warning movement can become a sudden strike when a threat persists.',
 'Deep Surge: Gathers and redirects local water; it cannot erase an island or reach inland by narration.':'Deep Surge: Gathers water around its body into a forceful local current, destabilizing nearby hulls and obstructing a close escape.',
 'Fighting Style: A formidable level-55 sea boss. It roams only between the authored eastern deepwater addresses while offstage and alive, never moving through a current scene, combat or a recorded defeat.':'Fighting Style: Tests a hold with one arm before committing its weight, using wreckage and deep water for leverage. Its reach is immense but still bodily, leaving room to cut free or rescue someone caught.',
 'A dangerous animal predator with a persistent individual identity.':'A territorial deepwater predator, patient before a sudden committed strike.',
 'an actual attack can bring a forceful level-60 defense.':'an attack can bring a forceful defensive response.',
 'an actual attack can bring a forceful level-60 defense':'an attack can bring a forceful defensive response',
 'a forceful level-60 defense':'a forceful defensive response',
}
for old,new in replacements.items():s=s.replace(old,new)
p.write_text(s,encoding='utf-8')
print('Updated rendering guides and removed public creature-control prose.')
