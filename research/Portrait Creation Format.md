# NPC Portrait Creation Format

> **Character-creation portraits:** Use [current player portrait defaults](Player%20Portrait%20Creation%20-%20Current%20Defaults.md). That route permits waist-up or hip-up framing and optional styles/cameras/backgrounds, without the fixed headroom and standing recipe below. This document also covers the separate manual NPC portrait workflow.


**Purpose:** Create a consistent, colorful portrait collection for the Voyage NPC cast. Use this guide whenever generating a character portrait in this project, including in another project chat.

## Standard portrait brief

**Akitsuhara local practice:** Keep the established rendering style, varied clothing colors/patterns and setting-appropriate lighting. For characters trained in this nation's local traditions, favor flowing translucent magical forms, tapered brushlike edges and graceful directional motion while retaining clear affinity identity. This is a cultural technique profile across local peoples, not a rule for every Oni everywhere or every foreign visitor. Do not add a universal warm grade, muted palette or weaker effects. Unusual yōkai use their actual authored anatomy and species silhouette; a bell, crane or nonhuman beast is not automatically a humanoid in a costume.

- **Subject:** One NPC, based on their approved character note. Keep their species, face, hair color and style, eye color, build, signature features, and role-appropriate clothing accurate. Do not invent visual details that conflict with the note.
- **Species lore and apparent age:** Consult the current world lore and relevant species/type notes before interpreting another race's age, maturation, lifespan, anatomy, or visible aging. Do not treat an elf's or another long-lived person's chronological age as the same apparent human age. State the intended adult life stage explicitly in the image brief and use the user's appearance guidance where the lore leaves it open; do not invent a numerical age-conversion formula. Nozomi Kogusa (wood elf, 84), Itsuki Morino (wood elf, 72), and Meilin Suyama (half-elf, 52) should look like youthful adults rather than elderly humans, per the user's direction. Preserve authored details such as Meilin's silver hair strands without automatically adding wrinkles, sagging features, or frailty. Youthful appearance must still read as adult. Keep actual chronological ages and established conditions unchanged.
- **Affinity visibility:** If the character card lists one or more magical affinities, make every listed affinity visibly recognizable in the portrait through fitting magic, materials, motifs, or environmental interaction. This applies to adults as well as students. Let the character and scene determine how the affinity appears; it can be subtle or spectacular, but it must be clearly present. If no affinity is listed, do not invent one.
- **Framing and silhouette:** Use an upright vertical 2:3 image with a centered, hip-up portrait. Keep the hips and enough of the lower outfit visible to read the design, including a skirt when relevant. The pose may change the camera viewpoint and the character's body direction; do not impose one camera angle or facing direction across the cast. Target a clear top margin of 12.5–15% of canvas height **above the top of the character's head and complete hair silhouette**; measure to hair, ears, horns, or head adornments, not to props. Up to 17% is acceptable when needed to avoid cropping, but do not go below 12.5%. Keep the top of the head/hair 12.5–15% down from the canvas edge (17% maximum), with no foreground prop extending above it or entering this reserved band. Nothing may touch or crop against the top edge. Keep the subject within this range rather than pushing the head lower to create an oversized empty band, while preserving readable hips and outfit. Near-full-frame compositions are fine only when this headroom remains. Keep the character distinct from the background. Outfit and silhouette are part of the appeal and must stay readable. For unusual nonhumanoids use the closest coherent equivalent without changing anatomy.
- **Pose selection, posture, and orientation:** Select the applicable NPC role profile, then use its eligible pose pool and the randomized selection procedure below. Every selected pose must depict the character standing; do not use sitting, kneeling, crouching, reclining, or lying poses. Desk, ledge, wall, or prop support is used only while standing. For the default profile, read the character card's personality and choose the single archetype category that best matches how the character behaves in this scene. For an approved role profile, use its role-compatible pose pool. Use a uniform random-number draw to select one eligible pose; do not pick the pose manually, alternate through the list, or fall back to the same default gesture. A pose may set the body's angle, head turn, camera viewpoint, and gaze. Do not force every portrait to face image-left or look directly at the viewer. Keep the fixed composition requirements: vertical 2:3 canvas, centered character, hip-up framing, complete head and hair, 12.5–15% target headroom (17% maximum; never below 12.5%), and a clear readable face. Fit posture, hip line, spine, shoulders, and hands to the selected pose without changing that crop or pushing the character off-center. Filter out poses that conflict with the character's anatomy, card, essential prop, or depicted duty before drawing; if a conflict is discovered later, correct the eligible list and draw again before generating. **Check limb and hand anatomy:** unless the card specifies otherwise, show no more than two arms and two hands, each attached to the correct side. Keep left/right hand identity, palm direction, thumb placement, wrist rotation, and prop-holding hand consistent. Avoid duplicated or mirrored hands, extra limbs, fused or tangled fingers, and impossible joints. Simplify or naturally hide a hand if its shape is unclear.
- **Facial expression:** Inspect the approved character card and choose an expression that fits the NPC's described demeanor, personality, and the scene. Do not default to a generic smile or an emotion that conflicts with the card. If the card does not specify an expression, infer a restrained, role-appropriate one.
- **Style:** Use a premium fantasy RPG anime character illustration: expressive drawn anime eyes, simplified nose and mouth, clearly drawn facial contours and clean colored shadow shapes with selective soft transitions. Put intricate detail into clothing, hair and the setting. Keep the face distinctly 2D anime without sculpted facial planes, realistic skin modeling or a 3D finish; soft transitions need not become hard shadow blocks. Let each portrait have its own palette, expression and lighting. Presence comes from design and a convincing gesture, not obligatory glamour, ornate rank or a battle pose. **Exclude realism and semi-realism** from both the visual treatment and the image prompt. Avoid photorealistic or lifelike facial anatomy, skin pores or photographic skin texture, live-action appearance, and 3D-render aesthetics. Use supplied gallery images for anime rendering style and quality only; do not copy their character, pose, camera angle, facing direction, or gaze unless the user explicitly requests it.
- **Character focus:** The NPC is the clear focal point. Keep the face and defining details sharpest and most visually prominent. Use contrast, lighting, and silhouette to separate them from the setting. Avoid making every part of the image equally bright, detailed, or busy.
- **Background and location:** Show a recognizable place where this NPC is normally found, chosen from their established role and story. The setting is part of the portrait, not a generic gradient or unrelated symbolic collage: for example, an Archon might be shown in their academy’s council chamber, a professor in a relevant classroom or training area, and the Great Sage in the palace space where she tends the Evertree’s weave. Include a few specific environmental cues, then keep the background softer and less dominant than the character so it establishes place without competing with the face.
- **Color, whimsy, and light:** Let the NPC’s established colors and location inform the palette, while allowing lively, surprising, or richly varied color choices. Whimsy, playful details, bright magical effects, dramatic light, and expressive staging are welcome when they suit the character or scene; do not mute them or reduce them to a restrained formula by default. Keep the face readable and the subject distinct from the background, but let the art feel imaginative and specific to this character. Do not force every portrait into the same lighting, pose, palette, mood, or magical effect.
- **One-pass generation:** For each requested NPC, prepare the brief, make exactly one image-generation call, and use that single result as the portrait. Do not automatically create variants, reroll, restart, regenerate, or make another edit pass after reviewing it. If review finds a mismatch or defect, save/report the result and wait for the user's explicit request before another pass. Each explicit request to redo a portrait authorizes one new pass for that portrait. Always start from the approved character note; use an existing portrait as an edit target only when the user specifically requests an edit. Edits can soften fine detail even when pixel dimensions stay the same. If an edit visibly loses sharpness, report that limitation and do not chain more edits; make a fresh portrait only if the user explicitly requests another pass.
- **Text and output:** No text, lettering, labels, logos, UI, signature, or watermark anywhere in the image. Produce a single PNG portrait, not a character sheet or collage. Name the file exactly `[NPC full name].png` and place it in `world-draft/npc portraits/`.

## NPC role profiles

The existing portrait style is the **default profile**. Apply an approved role profile when the character's actual occupation and the activity depicted call for it. These are portrait-authoring rules, not new Voyage NPC types or JSON fields. Read Equipment, Abilities and Combat Style, personality, and current lore before selecting a profile. A title alone does not determine temperament, combat power, or main/major status.

Role profiles change pose selection, props, staging, and effects. They retain the common requirements: polished 2D anime, accurate identity and species aging, centered standing hip-up framing for ordinary humanoids, vertical 2:3 canvas, 12.5–15% headroom (17% maximum), readable face, coherent anatomy, every listed affinity, and one generation pass. The special-anatomy exception below can still adapt the crop while preserving its mandatory portrait requirements. For a character with multiple roles, choose the role being shown; a governing adventurer addressing a council uses the governing profile, while the same person preparing to fight uses the adventurer profile. Do not stack incompatible gestures or props.

### Adventurers — weapon ready, combat identity visible

- Use this profile for generic adventurers, expedition fighters, and other NPCs portrayed in their established adventuring role. Favor a **drawn weapon in the character's preferred combat stance**, rather than a sheathed weapon decorating an otherwise idle social pose. Read the approved fighting style first: guarded fighters brace, precise fighters present a controlled line, mobile fighters show poised weight transfer, and heavy fighters show supported leverage. Keep them standing; the lower-body stance can be implied through hips, shoulders, and weight without changing the hip-up crop.
- Use the actual approved weapon, shield, or combat catalyst and its correct grip. A bow, polearm, heavy weapon, paired weapons, and casting focus need different handling. Do not invent a weapon during portrait generation or replace a signature weapon with a generic sword. An already-approved unarmed/body-casting specialist keeps that identity and uses the compatible unarmed stance; the new-card weapon requirement is handled in the Character Creation Format, before approval.
- **Spear, staff and polearm continuity:** Draw one continuous rigid shaft, with an attached head and aligned visible sections through every grip. Hands may occlude a short section but must not create offsets, disconnected rods, floating tips or accidental fractures. Favor a readable broadside diagonal with modest foreshortening when the weapon is important; let the intact shaft leave a side or lower edge rather than compressing or breaking it to fit the crop. An intentionally damaged weapon requires an explicit card or user instruction.
- Use **more prominent special effects than the default profile**, tied to their listed affinities and actual techniques: an elemental edge, directed spell trail, ward breaking around a shield, or another characteristic combat effect. Make every affinity distinguishable. For noncasters, use motion trails, disturbed dust, sparks from contact, wind-tossed fabric, or environmental movement without implying unauthored spellcasting. Effects may be colorful and dramatic, but must leave the eyes, grip, weapon silhouette, and headroom readable. Spectacle must not imply abilities or a power tier the NPC does not have.
- Choose a recognizable established expedition, training, or encounter location. Show a poised combat moment or the controlled follow-through of a technique, with no need for an opponent, gore, or a full battle scene. Convey personality through expression, tension, hip/shoulder relationship, and the way they hold their guard.
- Filter the **CB combat pose pool** below by weapon, fighting style, anatomy, and personality, then make the uniform random draw using the selection procedure. This replaces the default social-pose draw for this profile.

**CB — Combat-ready pose pool** (all standing, centered, and hip-up):

- **CB01 — Center Guard:** Hold a two-handed melee weapon in a supported diagonal guard below the chin, with shoulders turned slightly against the hips and the blade clear of the face.
- **CB02 — Point on Line:** Present a one-handed thrusting weapon toward an off-center target, with a compact elbow and the free hand balancing near the ribs; keep foreshortening modest.
- **CB03 — Outside Ward:** Set a cutting weapon outside the near shoulder with its point angled down and outward; turn the torso slightly while the free hand remains ready.
- **CB04 — Heavy Low Ready:** Support a heavy weapon with both hands across the lower torso, elbows comfortably bent and shoulders settled over a grounded hip line.
- **CB05 — Shield and Answer:** Angle the shield outward beside the torso while the other hand holds the drawn weapon ready to answer; show both grips without hiding the face.
- **CB06 — Paired Guard:** Hold one approved weapon in each hand, one guarding across the lower torso and the other covering the outer line; separate the hands and weapon silhouettes clearly.
- **CB07 — Long-Weapon Intercept:** Hold a polearm or combat staff in a compact two-handed diagonal guard across the lower torso; let the shaft extend beyond a side or lower edge rather than the headroom band.
- **CB08 — Archer's Set:** Angle a bow toward a target off to one side and begin a controlled draw using the character's established technique; keep the face and string hand readable and the bow outside the top margin.
- **CB09 — Focus and Cast:** Aim the approved combat catalyst from lower-chest height while the other hand shapes a learned spell; offset the shoulders and keep the cast below or beside the face.
- **CB10 — Counterturn:** Turn the hips away from an implied attack while the shoulders return toward it, with the weapon held in a compact counter guard; show readiness without an extreme twist or crouch.
- **CB11 — Guard Recovery:** Show the end of a controlled technique, weapon drawn back into a stable guard as cloth and a fitting effect trail settle; keep joints and grip mechanically coherent.
- **CB12 — Unarmed Measure:** For an approved unarmed or body-casting specialist, hold one open hand or fist forward and the other guarding the torso, with a standing weight shift appropriate to their training.

### Governing characters — authority expressed through actual work

- Use this profile for rulers, council members, civic administrators, judges, diplomats, and institutional leaders when depicted performing their governing duties. Show how this individual exercises authority: listening to a petition, weighing a decision, explaining a policy, negotiating, reviewing a plan, or directing a response. An easygoing leader may slouch; a welcoming official may invite discussion. Do not turn every office holder into the same stern, arms-folded ruler.
- Let attire, posture, and **one relevant focal prop** establish their real office and remit. A seal, dispatch, council folio, planning map, or authored ceremonial staff can work when appropriate; vary the choices. Do not add a crown, throne, military command, luxury, omniscience, or extra jurisdiction merely because they govern. Public office alone does not require a weapon. Keep any approved weapon sheathed or secondary unless this portrait specifically depicts a combat duty, in which case use the combat profile.
- Use a recognizable established council chamber, office, hearing room, diplomatic setting, or place of public work. Affinities remain visibly present through character-specific magic, motifs, materials, or an interaction with the setting. They may be luminous and imaginative without becoming a battle barrage. Preserve whimsy and personality rather than reducing the profile to paperwork and muted colors. Do not reveal a hidden allegiance or private scheme through invented insignia.
- Filter the **GV governing pose pool** below by the individual's actual duty, equipment, and personality, then draw uniformly. A role-compatible pose from their default personality category may also be included in the eligible pool; it must still depict a specific governing activity. Record the chosen pool and activity.

**GV — Governing pose pool** (all standing, with any supporting furniture at standing height):

- **GV01 — Petition Listener:** Turn toward an unseen petitioner with one palm gently open at waist height and the other resting beside a relevant document or office tool; let the expression show how they listen.
- **GV02 — Point of Decision:** Indicate one detail on a plan or folio held low, with shoulders angled toward the problem and a decisive or questioning expression fitted to the character.
- **GV03 — Measured Address:** Open one hand beside the torso as if explaining a decision, while the other rests naturally at the waist or holds an authored symbol of office.
- **GV04 — Seal in Hand:** Hold an appropriate office seal or dispatch near the waist while the free hand steadies the document; catch the pause before an official action rather than filling the image with writing.
- **GV05 — Negotiator's Offer:** Extend an open hand in a compact negotiating gesture, balancing the hips and shoulders with the other arm relaxed or holding a relevant prop.
- **GV06 — Deliberation at the Rail:** Rest one hand on a standing-height council rail or desk and bring the other near the chin or collar, with an attentive standing lean suited to their temperament.
- **GV07 — Dispatch Review:** Hold a dispatch or report at lower-chest height and glance toward an unseen speaker, with the free hand marking a pause or keeping the page steady.
- **GV08 — Steward's Survey:** Turn three-quarter toward the place or system they actually oversee, one hand indicating a relevant feature while the head turns enough to retain a readable face.

## Creative exceptions and cast prominence

- **Special NPCs and unusual anatomy:** For monsters, monster-people, NPCs with signature creatures, or characters whose anatomy, scale, equipment, or role would lose its impact in the standard crop, choose a compelling composition within a usable Voyage portrait. The upright vertical 2:3 canvas, clear face and complete head silhouette, and 12.5–15% headroom target (17% maximum) still apply. Creative freedom may change the crop, pose, randomized pose-library choice, viewpoint, and effects; it does not permit a landscape illustration or removal of headroom. For an arachne, frame the human torso, upper spider body, and enough legs to establish the anatomy; let some lower limbs or abdomen extend naturally beyond the lower/side crop instead of shrinking the face or flattening the whole creature into a wide scene. Preserve correct total anatomy even when limbs are naturally occluded or cropped. Use judgment without requesting separate approval. Preserve the approved identity, appropriate opaque clothing coverage, every listed affinity, polished 2D anime style, and one-pass generation. Keep a short note of the chosen composition and why it suits the NPC.
- **User-marked main or major characters:** When the user explicitly identifies a character as a main character or major character, give the portrait a slightly flashier presentation: a more memorable silhouette, richer lighting or color, and a distinctive affinity effect or visual motif suited to that character. Keep the increase measured and preserve personality; a reserved character can remain reserved. Do not infer main/major status from a name, level, rarity, or job title, invent powers or contradictory costume details, or impose a clutter quota. Ordinary cast portraits may still be imaginative and colorful.

## Pose library and randomized selection

First choose the applicable role profile above. For the default profile, choose the category below from the character card's core traits and default behavior, not from appearance or role alone. When the scene brings out a different side of the character, use the archetype shown in that scene. Pick one primary personality category; use a secondary category only when the pose clearly combines both traits. Categories are visual-language guides, not fixed personality rules. Adventurer and governing profiles use their role-compatible pools as specified above, with personality shaping eligibility and execution.

Build the eligible pose list before drawing. For the default profile, use the selected personality category; for a role profile, use its specified pool. Remove poses incompatible with the approved equipment, fighting style or duty, anatomy, or personality, and avoid IDs used in the last three portraits of the batch when another compatible choice exists. Let `n` be the eligible list length and draw an integer uniformly from `1` through `n` with an actual random-number generator. On Windows PowerShell, use:

```powershell
Get-Random -Minimum 1 -Maximum ($n + 1)
```

The upper bound is exclusive. Use the returned item's position in the eligible list, not necessarily its original ID number. Keep a short selection record while generating a cast batch (`NPC | role profile | personality category | eligible pose IDs | drawn index | pose ID | pose name`). If a conflict is discovered after selection, fix eligibility and draw again before generating; record the reason. These are pre-generation pose-selection steps, not extra image passes. Do not silently substitute a familiar pose. Put the selected profile, category or role pool, pose ID, name, and description directly into the image prompt.

All poses in this library are standing poses; any desk, ledge, wall, or prop used for support is at standing height. Do not reinterpret a pose as sitting, kneeling, crouching, reclining, or lying down. Poses may vary body angle, shoulder and hip relationship, arm placement, head turn, gaze, and camera viewpoint, but must leave the full head and hair silhouette in frame and preserve the established headroom. Keep hands natural and visible only when their gesture reads clearly. The user's pose-sketch references are gesture studies only: do not reproduce their sketch style, blank mannequins, grids, labels, or multi-pose sheets.

### R — Reserved / self-contained

- **R01 — Folded Forearms:** Cross the forearms loosely low across the torso; keep the hips settled and shoulders slightly drawn inward.
- **R02 — Cuff Hold:** One hand lightly holds the opposite sleeve cuff near the waist; tilt one hip slightly lower and keep the standing pose contained.
- **R03 — Hands Behind:** Place both hands behind the back so they are hidden; keep elbows close and the spine quietly upright.
- **R04 — Folio Shelter:** Hold a closed book or folio vertically against the torso with elbows tucked and a small inward curve through the shoulders.
- **R05 — Wrist Clasp:** One hand gently clasps the opposite wrist at waist level; distribute weight evenly and keep the expression calm.
- **R06 — Turned-Away Pause:** Turn the torso partly away, with one shoulder nearer the camera and hands resting behind the hip; let the head turn only enough to keep the face readable.

### A — Confident / assertive

- **A01 — Hip Anchor:** Set one hand on the hip with the elbow open; shift weight onto that side and lengthen the spine.
- **A02 — Grounded Brace:** While standing, rest one palm on a nearby standing-height desk, ledge, or table below the frame; lean forward slightly while keeping the hips grounded.
- **A03 — Lapel Set:** Hook one thumb at a lapel or vest edge near the chest; open the shoulders and lift the chin with controlled confidence.
- **A04 — Command Fold:** Fold the arms firmly but comfortably across the chest; angle the hips slightly and keep the shoulders level.
- **A05 — Point of Order:** Raise one finger, pen, or wand beside the chest as if making a decisive point; hold the other arm relaxed.
- **A06 — Open Claim:** Extend one arm outward with an open palm, as if claiming the room; counterbalance with a small hip shift.

### W — Warm / welcoming

- **W01 — Offering Hand:** Extend one hand with a small relevant object at chest height; soften the elbow and lean forward just a little.
- **W02 — Open-Palm Greeting:** Lift one hand in a gentle wave near shoulder level; keep the other arm relaxed and the shoulders open.
- **W03 — Hand to Heart:** Place one hand over the heart while the other rests low or holds a prop; use an open chest and gentle posture.
- **W04 — Soft Handclasp:** Clasp both hands loosely near the sternum; bring the shoulders forward slightly in a kind, attentive stance.
- **W05 — Lean-In Listener:** Angle the torso toward an unseen conversation partner, with one hand near the cheek or collar and the hips relaxed.
- **W06 — Shared-Object Presentation:** Support a book, tray, or sample with both hands in front of the waist; turn the shoulders toward the viewer in an inviting gesture.

### E — Energetic / competitive

- **E01 — Forward Challenge:** Shift weight forward and angle the torso into the scene; set the shoulders ready without beginning an attack.
- **E02 — Fist Pump:** Raise one compact fist beside the shoulder and keep the other hand at the waist; add a small twist through the hips.
- **E03 — Rally Fists:** Hold both fists near the chest with elbows bent outward; raise the shoulders slightly as if gearing up for a contest.
- **E04 — Cross-Body Swing:** Sweep one forearm across the torso while the other arm balances; counter-rotate the shoulders and hips.
- **E05 — Ready Grip:** Hold a training weapon or tool low near the hip with one hand; keep the other hand poised near the chest and weight balanced to pivot.
- **E06 — Momentum Reach:** Reach one arm forward at chest height and let the torso follow while the opposite shoulder draws back.

### T — Thoughtful / scholarly

- **T01 — Chin-Brace:** Rest fingertips at the chin while the other forearm supports the elbow; let one hip relax as the character considers a question.
- **T02 — Page Turn:** Hold an open book with one hand and catch a page with the other; angle the shoulders toward the text.
- **T03 — Temple Tap:** Touch one finger to the temple while the other hand holds notes low; keep the spine slightly inclined in thought.
- **T04 — Specimen Inspect:** Hold a small specimen, lens, or vial near the chest and turn the head toward it; keep elbows close and the face visible.
- **T05 — Pen Hover:** Hold a notebook at the waist and pause with the pen poised above the page; angle the torso forward attentively.
- **T06 — Folded Study:** Fold one arm across the body and rest the opposite hand at the chin; shift weight to one hip for a quiet thinking pose.

### P — Playful / mischievous

- **P01 — Finger to Lips:** Touch one fingertip lightly near the lips; tip the head and hip in opposite directions for a sly, contained gesture.
- **P02 — V-Sign Near Cheek:** Raise one hand in a small two-finger sign beside the cheek; let the opposite shoulder drop in a casual pose.
- **P03 — Over-Shoulder Tease:** Turn the torso away and glance back over one shoulder; add a small hand flick or lifted wrist.
- **P04 — Hidden Surprise:** Keep one hand and its object hidden behind the back while the other hand makes an innocent open gesture.
- **P05 — Tiny Ta-Da:** Present a small object in an open palm beside the torso; turn the shoulders and lift the chin as if revealing a trick.
- **P06 — Cheeky Shrug:** Raise one shoulder and open both palms at different heights; shift the hips sideways in a playful “who, me?” stance.

### F — Formal / disciplined

- **F01 — At Attention:** Stand with a straight spine, level hips, aligned shoulders, and arms resting neatly at the sides.
- **F02 — Glove Adjustment:** Use one hand to smooth or fasten the opposite glove or cuff; keep the back straight and weight even.
- **F03 — Centered Folio:** Hold a folio squarely in front of the torso with both hands; keep elbows close and shoulders precisely level.
- **F04 — Ceremony Prop:** Support a cane, staff, or closed book upright at the lower chest with one hand; the other hand rests neatly at the wrist.
- **F05 — Instructor's Stop:** Raise one palm at chest level in a measured stop or pause signal; keep the other hand low with a pen or wand.
- **F06 — Polite Introduction:** Angle the body modestly and extend one open hand in a formal introduction; keep the spine tall and the gesture compact.

### D — Dramatic / expressive

- **D01 — Grand Declaration:** Lift one arm in an emphatic declaration while the other hand rests over the chest; open the shoulders and raise the chin.
- **D02 — Hand to Brow:** Place fingertips at the brow or hairline as if struck by a revelation; curve the torso gently in the opposite direction.
- **D03 — Laugh Behind Hand:** Cover part of the mouth with fingertips, lift the shoulders slightly, and curl the upper spine in a natural laugh.
- **D04 — Heart and Flourish:** Press one hand to the chest and sweep the other arm outward; shift the hips to counterbalance the flourish.
- **D05 — Mantle Sweep:** Draw one arm across the torso as though sweeping a cloak or sleeve aside; rotate the shoulders against the hips.
- **D06 — Half-Bow:** Incline the upper body in a small theatrical bow, with one arm crossing the torso and the other opening outward.

### G — Guarded / wary

- **G01 — Forearm Shield:** Bring one forearm diagonally across the torso while the other hand stays low and ready; lean the hips slightly back.
- **G02 — Hands Near Sternum:** Hold the hands close together at the chest with elbows tucked; angle the shoulders inward but keep the face clear.
- **G03 — Look-Back Check:** Turn the torso away as if checking behind, then glance back over the near shoulder; keep one hand near a strap or collar.
- **G04 — Object Held Close:** Hold a book, pouch, or personal item close to the ribs with both hands; make the shoulders protective and the weight centered.
- **G05 — Weight-Back Pause:** Lean the torso away from an unseen stimulus while keeping the head attentive; let one arm brace lightly across the waist.
- **G06 — Self-Containment:** Rest each hand on the opposite upper arm in a loose self-hug; curve the shoulders inward without hiding the face.

### L — Relaxed / sleepy

- **L01 — One-Hip Slouch:** Let the weight rest on one hip, soften the spine, and lower one shoulder while the arms hang easily.
- **L02 — Cheek in Palm:** While standing, support the cheek with one palm as the opposite forearm supports that elbow, or rest the elbow lightly on a standing-height ledge; keep the other arm loose.
- **L03 — Low Mug Hold:** Hold a mug or flask low near the waist with one relaxed hand; let the free shoulder and hip settle.
- **L04 — Sleeve Hide:** Tuck both hands partly into long sleeves near the waist; round the shoulders gently and lower the head without closing the eyes completely.
- **L05 — Wall Rest:** Stand with one shoulder against a wall or pillar, bend the torso just a little, and let one arm hang while the other rests at the hip.
- **L06 — Loose Cross:** Cross the arms loosely and let the head tilt toward the lower shoulder; keep the stance comfortable rather than defensive.

### U — Curious / observant

- **U01 — Lean to Inspect:** Incline the torso toward a small object or detail held low; extend the neck slightly while keeping the hips anchored.
- **U02 — Listening Tilt:** Tilt the head toward a sound or speaker, raise one shoulder slightly, and hold the hands quietly around a notebook.
- **U03 — Shade-and-Scan:** Lift one hand near the brow as if scanning a distant detail; angle the shoulders and keep the other hand at the waist.
- **U04 — Point to Detail:** Point gently toward something just outside the frame, leaning the torso in that direction without stretching off-center.
- **U05 — Notebook Pause:** Hold an open notebook at the waist and raise the pen as if a new question has occurred; let the posture lean forward with interest.
- **U06 — Turn It to the Light:** Rotate a leaf, crystal, vial, or tool between both hands to examine it; keep elbows bent and shoulders slightly rounded.

### S — Elegant / social

- **S01 — Contrapposto Poise:** Set one hip outward and shift the shoulders gently the other way; keep one hand at the waist and one arm relaxed.
- **S02 — Wrist Display:** Bend one wrist gracefully near the shoulder to display a glove, bracelet, or sleeve; keep the other hand low and composed.
- **S03 — Compact-Mirror Check:** Hold a small mirror beside, not in front of, the face; angle the hips and lift the chin as if checking the light.
- **S04 — Hair Sweep:** Lift one hand to arrange a lock or hair ornament while the opposite shoulder turns slightly toward the viewer.
- **S05 — Arm Loop:** Rest one hand lightly over the opposite forearm and curve the free wrist outward; keep the spine long and the hips angled.
- **S06 — Over-Shoulder Introduction:** Turn the torso into a graceful three-quarter angle and extend one hand in a polished greeting while looking back toward the room.

## Prompt template

Use the standard composition below for ordinary humanoid portraits. Choose the default, adventurer, or governing profile from the approved card and the activity depicted, then include its role module below. Consult species lore before filling the age and appearance details, and state the intended apparent adult life stage explicitly. For a qualifying special NPC, adapt the crop, viewpoint, and pose under **Creative exceptions and cast prominence** while retaining the vertical 2:3 canvas and required headroom. For a user-marked main or major character, add a measured increase in visual flair to the brief.

> Create a single premium **fantasy RPG anime character illustration** of **[NPC full name]**, upright in a vertical 2:3 composition. The render must read clearly as anime: stylized anime facial proportions, expressive anime eyes, fine confident linework, layered painted shading with soft gradients, detailed illustrated hair and clothing, and luminous setting-appropriate light. **Do not use realism, semi-realism, photorealism, lifelike facial anatomy, photographic skin texture, live-action styling, or 3D-render aesthetics.** Inspect the approved character card and choose a facial expression that fits the character's described demeanor, personality, and this scene; do not default to a generic smile. Use a centered, standing hip-up portrait composition. Do not use sitting, kneeling, crouching, reclining, or lying poses. Let the selected pose determine the camera viewpoint, body direction, head turn, and gaze; do not force a shared camera angle, image-left facing, or viewer-directed gaze across the cast. Keep the face readable and centered with the character. Target clear, unoccupied headroom of 12.5–15% of canvas height above the top of the character's head and complete hair silhouette; up to 17% is acceptable when needed to avoid cropping, but never go below 12.5%. Measure to hair, ears, horns, or head adornments, not to props. Position the topmost hair/ear silhouette about 15% down from the canvas edge (17% maximum), and keep all foreground props below it and outside the reserved band. Nothing may touch or crop against the top edge. State the placement concretely in the composition: on a 1536-pixel-high canvas, the topmost hair should begin around 230 pixels down (15%); 192 pixels is the minimum safe placement and 261 pixels (17%) is the maximum. Do not zoom in or enlarge the character to fill the frame. Keep the face and eyes sharp and focal. For an unusual nonhumanoid, use the closest coherent framing without changing its anatomy. Accurately depict [species, build, hair color and style, eye color, defining features, and appropriate clothing] from the character note. Make every listed affinity visibly recognizable through fitting motifs, materials, magic, or environmental interaction; choose a subtle or spectacular expression that suits this scene. **Role profile:** [default / adventurer / governing; the specific activity depicted]. **Randomly selected pose:** [personality category or role pool; pose ID and name; description drawn from the eligible list]. Follow this pose's body-language cues, including its weight distribution, hip line, spine, shoulders, and arm or hand placement. The pose description may specify a camera or facing direction; honor it while keeping the character centered and hip-up. Ensure anatomically coherent limbs and hands: confirm each hand connects to the correct arm, left and right are consistent, thumbs and wrists are oriented plausibly, and there are no duplicated hands, extra limbs, fused fingers, or impossible joints. If a gesture is unclear, simplify it or hide the hand naturally. If gallery images are supplied, use them for anime rendering style and quality only, not for pose, camera angle, facing direction, or gaze. Avoid a strict side profile or exaggerated lean unless the selected pose calls for it and the face remains readable. Set the portrait in [the specific established place where this NPC is normally found], with recognizable environmental details that establish the location while remaining softer and less prominent than the character. Let the colors, whimsy, and magical effects feel imaginative and specific to this character; bold palettes and bright effects are welcome when they suit the scene. Keep the character readable and distinct from the setting. **No realism, semi-realism, photorealism, text, letters, labels, logos, UI, signature, watermark, extra characters, collage, or character-sheet layout.** Save as `[NPC full name].png` in `world-draft/npc portraits/`.

Add the applicable role module to the filled prompt; omit the modules for the default profile:

- **Adventurer module:** "Show [approved weapon or explicit unarmed exception] in [the card's preferred stance and the selected CB pose], with [correct grip and guard]. Add prominent [specific effects grounded in listed affinities and actual techniques, or nonmagical motion/environmental effects]. Keep the face, hands, recognizable weapon, and headroom clear. Use [an established adventuring or training location]."
- **Governing module:** "Depict [specific duty within this NPC's actual remit] using [selected role-compatible pose] and [one fitting focal prop, if any]. Express [individual decision-making manner] through posture and expression in [established place of governance or public work]. Show all affinities through [fitting visible effects, materials, motifs, or environmental interaction]. Preserve colorful, character-specific staging without inventing rank, powers, regalia, or secret insignia."

## Editing an existing portrait

Treat the supplied portrait as the edit target. Name the requested change precisely and separate it from the details that must stay fixed. Change one focused feature at a time when possible, and repeat the preservation constraints in each follow-up.

> Edit Image 1, the portrait edit target. Change only [specific requested feature]. Preserve [identity, expression, body and head pose, hair, clothing, props, background, lighting, framing, and style as applicable]. State head direction and eye gaze separately: [head direction]; [gaze target]. If the request is to mirror the image, horizontally mirror [the entire image / the subject only] first, then apply [any additional requested change]. Do not alter other details or add new elements.

For directional edits, distinguish these instructions explicitly:

- **Mirror:** Specify whether the whole canvas or only the subject should be flipped horizontally.
- **Head direction:** State where the head and nose point relative to the image, such as “nose points toward image-left.”
- **Eye gaze:** State where the pupils look, such as “both eyes look directly at the camera.”

Do not use “look left” alone when both head orientation and eye gaze matter. A left-facing head can keep its orientation while the eyes look at the camera.

After an edit, inspect fine details and perceived sharpness, not just the pixel dimensions. If detail has softened, report it and do not use the softened edit as the input for another edit. A fresh portrait is a separate pass and requires the user's explicit request.

Replace each bracketed instruction using the approved character note. If the NPC’s usual location is not established, choose the most natural location from their public role and use that consistently unless the user chooses another. If a long weapon or staff does not fit naturally in a hip-up frame, show a recognizable portion and coherent grip, with the rest extending beyond a side or lower edge. For the adventurer profile, keep the approved primary weapon visibly drawn and ready rather than omitting it. An optional prop in another profile may be omitted. Do not distort the composition, shrink the face, or invade headroom to force the whole weapon into view.

## Quick review before saving

- Was species lore consulted so apparent age, maturation, and anatomy fit the race and the user's directions rather than a human-age assumption?
- If using a special-NPC exception, does the chosen vertical 2:3 portrait reveal the distinctive anatomy, scale, companion, or equipment without distorting it, preserve required headroom, and record the reason for its crop?
- If the user marked this NPC as main or major, is the portrait slightly flashier while still fitting the character's personality and approved details?

- Is this unmistakably the intended NPC, with the correct eye and hair colors and species details?
- Was the character card checked so the facial expression fits the NPC's described demeanor, personality, and scene?
- If an affinity is listed, is every listed affinity visibly recognizable in the portrait?
- Was the correct role profile chosen from the actual card and activity, with an eligible pose pool shaped by personality, equipment, and the relevant fighting style or governing duty, then selected through a uniform random draw?
- Are the role profile, personality category, eligible pose IDs, drawn index, selected pose ID, and name recorded, avoiding a pose from the last three portraits when a compatible alternative exists?
- For an adventurer, is the approved weapon drawn in a compatible preferred combat stance, with more prominent effects grounded in actual abilities, and no invented weapon or spellcasting?
- For a governing character, does a specific duty, appropriate equipment, and their individual manner make the real office readable without invented status or jurisdiction?
- Does the pose suit the character and add variety to the portrait collection?
- Does the posture express the character's personality through a few compatible cues in hip line, weight distribution, spine, shoulders, and arms, without repeating the same stance across portraits?
- Are the visible arms and hands anatomically coherent: no duplicate or extra hands/limbs, each hand attached to the correct arm, left/right orientation consistent, thumbs and wrists plausible, and fingers distinct?
- Does the portrait keep the character centered and hip-up with the required headroom, while allowing the selected pose to vary the camera viewpoint, body direction, head turn, and gaze?
- Is the character clearly standing, with no sitting, kneeling, crouching, reclining, or lying posture?
- Do body angle, head direction, and eye gaze follow the selected pose and remain readable, without a forced direction shared by every portrait?
- For an edit, did only the requested feature change while the listed details stayed fixed?
- Is the image a single centered hip-up portrait, with the full head and hair silhouette, face, torso, hips, and enough of the lower outfit readable?
- Is there clear negative space of 12.5–15% of image height above the top of the character's head/hair silhouette (up to 17% maximum, never below 12.5%), with all foreground props below that level?
- Does the character fill most of the remaining image without clipping, and are the face and eyes sharp and focal?
- Does the background show where the NPC is normally found, rather than a generic backdrop?
- Does the setting support the portrait while staying visually secondary?
- Does the style feel crisp, pristine, colorful, and varied within the cast?
- Does the image read unmistakably as a 2D anime illustration? If it leans toward realism, semi-realism, photorealism, live-action, or 3D rendering, note the issue for the user; do not revise or regenerate without an explicit request.
- Are facial features, hair, costume details, and background edges still sharp at full size and thumbnail size? If an edit has softened them, report that limitation and wait for the user before making another pass.
- Is all text, watermarking, UI, and unrelated extra-character content absent?
- Is the PNG named with the NPC’s exact full name and saved in `world-draft/npc portraits/`?

## Basis for the composition rules

These are practical guidelines rather than rigid art laws. Clip Studio's character-art and composition guides discuss shot size, directing attention with background elements, and using contrast, depth, and negative space to keep a subject readable. For this portrait collection, hip-up is the default because it keeps the expression visible while showing more of the costume silhouette. Clip Studio’s background guidance notes that setting details can communicate where a character is and add information about them, while simplifying background treatment helps the character remain prominent. A character-design workflow from Creative Bloq similarly ties pose, costume, lighting, and rendering to the character’s lore.

- [Clip Studio TIPS: Make Your Character Illustrations Stand Out](https://tips.clip-studio.com/en-us/articles/8486)
- [Clip Studio TIPS: The Power of Arrangement — Mastering Composition](https://tips.clip-studio.com/en-us/articles/8526)
- [Clip Studio Paint: Effective Storytelling, Design Tips](https://www.clipstudio.net/en/comics-manga/design-tips/)
- [Creative Bloq: How to use lore to drive your character designs](https://www.creativebloq.com/art/digital-art/how-to-use-lore-to-drive-your-character-designs)

## Official image-editing guidance

OpenAI’s current image guidance recommends identifying each input image’s role, stating exactly what should change and what must remain fixed, and refining with focused edits. This portrait workflow applies that advice by treating body angle, head direction, and eye gaze as separate instructions, and by specifying whether a mirror operation affects the full canvas or only the subject.

- [OpenAI: Image prompting](https://developers.openai.com/api/docs/guides/image-prompting)
- [OpenAI Academy: Creating images with ChatGPT](https://openai.com/academy/image-generation/)




