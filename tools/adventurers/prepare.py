import json
import pathlib
from cast import build_cast, CAST

ROOT = pathlib.Path(__file__).resolve().parents[2]
world = json.loads((ROOT / 'world-draft/WorldAlpha - World.json').read_text(encoding='utf-8'))
cast, briefs = build_cast(world)
directory = ROOT / 'tmp/adventurers'
directory.mkdir(parents=True, exist_ok=True)
for filename, data in [('baseline.json', world), ('new-npcs.json', cast)]:
    path = directory / filename
    if filename != 'baseline.json' or not path.exists():
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
pose_text = {
 'CB02':'Present the approved thrusting weapon on an off-center target line, with compact elbow and free hand or shield balancing near the ribs.',
 'CB03':'Hold the approved cutting weapon outside the near shoulder, point angled down and outward; turn the torso slightly with the other hand ready.',
 'CB04':'Support the actual heavy weapon with both hands across the lower torso, elbows bent and shoulders over a grounded hip line.',
 'CB05':'Angle the actual shield outward beside the torso, holding the drawn weapon ready in the other hand; show both coherent grips and the face.',
 'CB07':'Hold the actual polearm or staff in a compact two-handed diagonal guard across the lower torso, with the shaft exiting a side or lower edge.',
 'CB08':'Angle the actual bow to one side and begin a modest controlled draw, with readable string hand and face.',
 'CB10':'Show a standing counterturn, hips angled away and shoulders returning toward the target, weapon in a compact guard; no extreme twist.',
 'CB11':'Show recovery from a controlled technique to a stable standing guard, actual weapon and fitting effects settling.',
 'T02':'Hold an open notebook in one hand and turn a page with the other, shoulders angled toward the text and face visible.',
 'T04':'Hold the actual small specimen or work tool near the chest and turn the head toward it, elbows close and face visible.',
 'U05':'Hold an open notebook at the waist and raise the pen in a standing, inquisitive pause.',
 'U01':'Lean slightly to inspect a small actual work detail held low, with hips anchored and face visible.',
 'F02':'While standing, adjust one glove or cuff with the other hand, precise but not stiff.',
 'F04':'Support the actual staff at lower-chest height, other hand poised near the wrist; keep the prop below the top headroom band.',
 'W01':'Offer a small actual relevant object at chest height, elbow soft and a slight forward lean.',
 'W06':'Present the actual work object with both hands in front of the waist, standing with inviting shoulders.',
 'P05':'Display a small relevant object in one open palm beside the torso, amused and confident.',
 'S01':'Use an elegant standing contrapposto, one hand at the waist and the other relaxed with the approved prop.',
 'S05':'Rest one hand lightly over the opposite forearm, with long spine, angled hips and poised expression.',
 'S06':'Turn into a graceful three-quarter standing introduction, one open hand extended and head turned toward the room.',
 'L03':'Hold an actual mug low near the waist with one relaxed hand, standing with one hip and shoulder settled.'}
effects = {
 'Earth':'a restrained ribbon of lifted grit or steadying stones near the working hand',
 'Metal':'fine metallic glints and a small controlled iron fitting or reinforced metal edge',
 'Wind':'clear flowing wind ribbons moving loose cloth or a light line',
 'Water':'a small clean curl of existing water held in controlled motion',
 'Ice':'beautiful sharp frost geometry and cold blue ice filaments',
 'Nature':'small bright living leaf or temporary plant-fiber shapes',
 'Fire':'a compact ember flare appropriate to a controlled small working',
 'Enchantment':'a few precise luminous reinforcement marks around an actual object',
 'Light':'a small clear gold-white light that leaves the face readable',
 'Sound':'delicate visible resonant rings from an actual small tone or metal fitting',
 'Illusion':'a subtle duplicate color shimmer around a small object, not a second person',
 'Lightning':'a compact controlled spark around a fitting, never obscuring the face',
 'Divination':'a faint uncertain pattern in a held sample, not time travel or cosmic prophecy',
 'Summoning':'a tiny translucent paperlike helper construct beside a work item',
 'Healing':'a small controlled restorative glow around the open supporting hand, distinct from a weapon strike'}
backgrounds = {
 'Whitepass Caravan Lodge':'a warm alpine timber lodge with snowy mountains beyond its open yard and a few practical ropes or drying coats',
 'Coldglass Galleries':'an elegant natural ice cavern, deep blue glacial glass, mirrorlike frost surfaces and distant cold mineral lights',
 'Asterveil Canopy':'a small fae settlement on floating green islands, flowering boughs, a specimen table and distant clouds',
 'Tetherroot Chain':'floating green sky-island ledges linked by real vine and rope spans above bright cloud gaps',
 "Adventurer's Guild - Glowhaven Branch":'the warm timber-and-stone Glowhaven guild hall, teal-and-ochre accents, a practice yard or practical appraisal workbench, and blurred stained glass',
 'Willowbend Residential District':'a comfortable fantasy-city residential courtyard with willow shade, tiled roofs and warm lamps',
 "Wayfarer's Goods":'a warm travel outfitter shop with rope coils, canvas packs and a packing counter',
 'Prison Work Yard':'a coastal stone prison maintenance yard with drying racks, a safe workbench and cool sea light'}
for row, brief in zip(CAST, briefs):
    portrait = ('Use case: illustration-story. Asset: one finished fantasy RPG NPC portrait, single vertical 2:3 PNG. '
      + ('Major character: memorable, flashy composition and vivid coherent magic, pristine dramatic 2D anime key art. ' if brief['major'] else 'Supporting character: polished colorful 2D anime illustration with an individual palette and expressive crisp lines. ')
      + 'Identity: ' + row['visual'] + ' Usual equipment: ' + row['equipment']
      + ' Scene: ' + backgrounds[row['location']] + '. '
      + 'Pose: ' + pose_text[brief['pose']] + ' Expression follows the card: ' + row['personality'][1]
      + ' Visible actual trained magic: ' + '; '.join(effects[x] for x in brief['affinity']) + '. '
      + 'Composition: one adult standing, centered hip-up, hips and lower outfit readable. Entire head, hair, ears and horns intact, with 12.5–15 percent canvas height of unobstructed setting above the complete head silhouette, never an empty flat band. Weapons do not enter that top band. Distinct silhouette and face, softer contextual background. '
      + 'Rendering: unmistakable hand-drawn 2D anime, expressive stylized eyes, clean ink contours, graphic cel-shaded planes, beautiful flat-color design and crisp fine details. No semi-realism, lifelike skin, pores, photographic anatomy, 3D rendering or plasticky edges. '
      + 'Exactly two coherent arms and hands, no extra limbs, correct grips, no mirrored hands or fused fingers. No other people, no text, names, lettering, interface, logos, borders, signature or watermark. No child proportions. One final portrait, not variants or a collage.')
    brief['prompt'] = portrait
    brief['file'] = 'world-draft/npc portraits/' + row['name'] + '.png'
(ROOT / 'tools/adventurers/portrait-briefs.json').write_text(json.dumps(briefs, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'newNPCs':len(cast), 'portraits':len(briefs), 'affinityCounts':{str(x):sum(b['affinityCount']==x for b in briefs) for x in [1,2,3]}},ensure_ascii=False))
