# Portrait direction and academy uniforms

The author supplied four positive examples: the red-haired twin-sword portrait, Adoha’s singing portrait, Riko Kanehara and the dark-teal-haired moth-winged Asterveil resident. These are style references, not people to copy into new player characters.

All four combine a distinctly anime face with fine controlled drawing, layered soft shading, detailed garments and illustrated materials. The face remains the focus while architecture gives the person a place in the world. Hair, fabric, props and selective effects provide movement. The red-haired portrait is comparatively still; its presence comes from design, expression and light. Adoha has much stronger gesture and magic. Riko’s smaller effect and practical gear still make a memorable lead. The moth-winged resident shows that the same finish works for quieter working clothes.

Our previous instructions repeatedly required graphic cel shadows, clean hair masses and simplified cheek planes. Those are not inherently bad anime directions, but they overemphasize the flatter end of the range compared with the submitted gallery. This is a prompt diagnosis, not an A/B result proving one phrase caused the runtime output.

Luxcellia’s read-only source places a positive style anchor first, combines cel shading with soft gradients and atmosphere, then separates identity, framing and setting. Its exact prompt is 4,990 characters in the supplied export. We borrow that organization and balance, not its world lore, age assumptions or rigid crop defaults.

The new default is **Fantasy RPG illustration**: fine anime linework, layered painted shading, detailed illustrated materials, an individual expressive face and luminous, setting-appropriate light. Player characters receive the same visual care as the leading cast. This does not confer glamour, status, expensive equipment, new powers or narrative importance. Keep the actual body, age, anatomy and selected clothing. Alternate styles and explicit framing remain available; a civilian needs no compulsory aura or battle pose.

## The academy-clothes failure

The old outfit choices asked for the selected academy’s colors but supplied no actual mapping or crest. The final Appearance handoff did not require resolving that label. A downstream image generator cannot be assumed to know the selected start or lore.

The four existing academy lore records establish the following heraldic creatures. No exact numbered heads, crest geometry or official bitmap is defined, so do not invent those as canon.

| Academy | Uniform color | Pictorial embroidered crest |
|---|---|---|
| Phoenix Wing | Crimson red | Phoenix with spread wings |
| Hydra Head | Violet purple | Many-headed hydra |
| Gryffin Tail | Cyan blue | Winged gryffin |
| Dragon Hoard | Yellow and gold | Dragon |

Generic student/faculty clothing resolves the school from the selected academy opening or established affiliation. Four additional explicit school-uniform options carry their own color and creature. The final image brief spells out the school name, visible color panels, garment cut and one pictorial embroidered crest. The image has no written school name. A uniform alone does not enroll or employ someone.

## What changed and what still needs testing

Changed the NPC image instruction, both Appearance-related background leaves, the default style and three alternatives, the generic academy outfits, and four new cosmetic uniform choices. All old portraits and the player’s optional crop/camera choices remain intact. The manual portrait guide adopts the rendering description while retaining its separate NPC pose, headroom and one-pass rules.

The image instruction remains below 5,000 UTF-16 units; whole AI task limits are checked by the portable validator. Actual Voyage player generation still needs testing with one generic academy outfit per student start, a school-specific outfit, an explicit alternative style, a noncaster, and a written-appearance override. Inspect the final Appearance text if a uniform fails: it must contain the resolved colors and crest before blaming the image model. Offline new-NPC art uses the built-in generator and the gallery as a style reference; it is not proof that Voyage uses the same model or context.

Do not automatically regenerate any existing cast portrait to test this change.
