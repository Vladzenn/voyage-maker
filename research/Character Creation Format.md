# Character Creation Format

**Status:** Working format for the Voyage NPC cast  
**Purpose:** Keep public character-card information concise while giving the narrator specific behavior, secrets, and combat guidance. Character portraits and other image assets are created separately from Voyage Studio.

## Delivery format — NPC JSON cards

When the user requests a character card, deliver an individual native Voyage NPC JSON object by default, matching their supplied Studio examples. For a batch, use separate copyable JSON blocks and optionally provide one keyed NPC-map file. The Markdown template below is a design framework, not the default delivery format. Use Markdown cards only when explicitly requested.

Map Appearance into visualDescription and retain the necessary narrated physical facts in basicInfo. Keep equipment and direct profile bullets in basicInfo, secrets in hiddenInfo, and labeled personality/ability entries in their native string arrays. Use supported current location, area, type, tier, level, faction, visibility and voice fields. Choose power values from the current world rather than copying an example character's combat bonuses. Leave portraitUrl empty until a real Voyage-hosted URL exists; never insert a local PNG path or invented upload. Add no schedule field. Review cards do not authorize automatic roster merging or scheduling.

## Roster Source of Truth

Maintain the NPC roster directly in `world-draft/WorldAlpha - NPCs.json`. Add and edit character entries in that file using its existing JSON structure. Do not create or update separate Markdown character files under `world-draft/npcs/`; that folder has been retired. The reusable structure below describes the information each character entry should contain and how it maps into the JSON fields.

For NPC journal visibility in the exported JSON, use **`initialKnown`**, never the obsolete `known` field. Set it to `true` for the Great Sage, the four Archons, the four headmasters, and any other character whose citywide public fame is explicitly established. Set it to `false` for ordinary students, professors, local workers, merchants, and other contacts unless their established fame warrants an exception. Wealth, noble birth, combat power, or being well known within one school is not enough by itself. Public recognition does not create a personal acquaintance, reveal hidden information, or grant a starting relationship. This is export/setup metadata; do not add a visibility section or profile bullet to the character card.

When creating an NPC portrait, follow [Portrait Creation Format](Portrait%20Creation%20Format.md). Save the finished PNG in `world-draft/npc portraits/` using the NPC’s full name as the filename.

## Design approach

For a settlement, region or realm population pass, also consult [Population Creation Guide](Population%20Creation%20Guide.md) for coverage, relationships, institutions, placement and portrait coordination. It supplements the existing card structure rather than adding character sections.

For fae, also consult [Fae Appearance and Variation Guide](Fae%20Appearance%20and%20Variation%20Guide.md) and the active world’s Fae — Bodies and Individual Variation lore. Record a coherent individual body in the existing Appearance paragraph; most are short adults, and a wingless satyr is as valid as a winged humanoid. Small stature must retain adult facial structure and proportions. Do not add universal wings, shrinking or a common lifespan. These appearance choices do not add new card headings or implement player-creation traits automatically.

Use Luxcellia's labeled, behavior-focused personality cues and relationship patterns, with Chikara's grounded daily routines and school-life details. Keep the public summary short; put undiscovered motives and history in hidden information. Keep an Appearance section in the authoring note, separate from the public summary. Do not repeat the same paragraph across fields: each section has a different job.

Use the reusable note below as the canonical structure. Keep its section headings; do not invent extra sections or profile fields unless the user asks for them. The template is a structure, not a limit on imagination: make characters vivid and specific within the existing sections, and omit optional entries when they do not fit.

For magic users, the Magic affinity entry lists only one-word elements or schools (for example: Arcane, Necromancy, Light, Void, Gravity). List multiple terms separated by commas when appropriate. Affinity makes that type easier to learn but does not restrict access to other types. Describe whether they generalize or specialize and their casting habits in Abilities and Combat Style; let those choices guide their abilities and usual magic-related equipment rather than adding generic magical gear.

The current magical approach mapping is **Logic: Arcane, Metal, Gravity, Enchantment, Space; Passion: Fire, Lightning, Earth, Wind, Water; Empathy: Healing, Nature, Light, Summoning, Soul; Intuition: Divination, Void, Illusion, Ice, Sound**. These describe execution and learning contexts, not temperament or moral character. A selfish healer and a quiet Passion caster remain valid. Do not change an approved affinity merely to match personality.

Follow the current Schools of Magic lore inside the existing sections. Body casting is a normal trainable method; a suitable mana-bearing catalyst assists learned control and usually contains no spare reserve. Personalized spell blueprints may use words, gestures or materials as aids without requiring them universally. Intentional bodily enhancement is learned Enchantment, including powerful movement techniques, and does not require an added affinity. True Freeform and witnessed humanoid soul extraction are not default talents to assign. An ordinary animal cannot deliberately cast; mana beasts and summoned constructs are distinct. Describe an academy member's actual work and personality using its current civic mandate, rather than the retired Strength/Harmony/Study/Wonder labels. Add no new character-card heading or profile field for these rules.

The world also supports martial and occupational characters and noncasting player backgrounds. Describe a person's actual training rather than adding spellcasting solely to make them belong. Preserve the established competence of trained academy adults. An expedition requirement means travel beyond the entire Glowhaven region; local countryside and Wraith Island Prison do not qualify. New foreign characters should fit their actual authored destination and cultural background; Japanese-inspired naming for Glowhaven does not replace established French/Elvish or other foreign identities. Reuse the world's canonical full names and naming guidance without creating a duplicate person from a partial name.

Physical playstyles use Force and Finesse alongside those four magical approaches. Force includes physical power, resilience, sustained exertion, and guarded fighting; there is no separate Endurance attribute. In the existing Abilities and Combat Style prose, explain how the person delivers attacks, moves, holds position, and actually uses learned magic. A spellblade can fight through forceful, precise, or guarded technique; the weapon alone does not dictate it. Do not add an aptitude-score section, stat-profile bullets, extra affinity, or new numeric NPC schema fields. A combined magical strike is one action with real training and mana limits, not an automatic extra hit. Preserve an authored NPC's actual level, tier, equipment and abilities.

### Role-specific creation rules

The existing card structure remains the default. Apply the following approved role rules inside its current sections; these are authoring profiles, not new Voyage types, headings on each card, or JSON fields. A character may have more than one role, but their duties, equipment, personality, and combat training must agree. Do not retrofit already-approved NPCs or change their weapons merely because these guidelines have been added. The matching portrait rules are in [Portrait Creation Format](Portrait%20Creation%20Format.md).

**Adventurers: appropriate weapons and distinct combat identities**

- For each **new generic adventurer**, choose an appropriate primary weapon during character design and explicitly name it first in the existing Basic Info equipment paragraph. Even a magic-focused adventurer needs an appropriate combat weapon; a staff or other catalyst can qualify when it is actually designed and used as a weapon. An ordinary notebook, decorative crystal, or unexplained focus does not satisfy this requirement. Preserve an explicitly requested unarmed concept or an already-approved body-casting specialist rather than silently changing that identity.
- Match the weapon to their training, build and species anatomy, preferred range, travel demands, resources, and established culture. A beginner needs usable equipment, not an unexplained legendary armament. Do not infer affinity from the weapon or add affinities to justify it. A noncaster remains a valid adventurer.
- Compare recent adventurers and vary weapon families, reach, handedness of use, shield pairings, and tactical purpose. Where supported by the setting, consider thrusting or cutting blades, spears or other polearms, axes, maces or hammers, bows, paired short weapons, and combat staves. Vary design and fighting method within a family as well. Do not give everyone a sword, sword-and-shield, or staff, but do not force exotic weapons or a rigid distribution simply for novelty. Add a backup weapon only when it has a practical reason.
- In Abilities and Combat Style, explain the **preferred combat stance and how the weapon is used**: grip, guard, weight distribution, favored range, attack/defense pattern, and when they disengage. Describe these in the existing fighting-style prose, without an extra profile field. A poised stance must be specific enough to guide the portrait; saying only "expert swordsman" is insufficient. A magical weapon effect must follow an actual learned technique and its limits.
- Give the adventurer a practical expedition role and a few relevant travel or work items. Personality still governs their risk tolerance, teamwork, habits, and response to trouble; weapon class does not dictate temperament. The portrait will normally show their approved weapon drawn in a compatible stance with more prominent, ability-consistent effects.

**Governing characters: a real remit and an individual way of exercising it**

- In Basic Info and the existing role bullets, state the office, the work they actually perform, the people or institution they serve, and the scope and limits of their authority. Consult the current government, faction, and location lore. Distinguish civic rule, academy administration, judicial duties, and diplomacy rather than treating every official as a ruler. Do not invent laws, titles, appointment powers, or access rights to make a character seem important.
- In Equipment, choose recognizable tools or symbols that fit the actual office and daily routine, such as an appropriate seal, dispatch case, planning folio, or authored ceremonial staff. Vary these rather than giving every official the same book and quill. A weapon is optional and must follow their established training and duties; public office alone grants no combat mastery.
- Use the existing Personality entries to show how they listen, make decisions, negotiate, delegate, and respond to a challenge. Preserve individual warmth, humor, informality, vanity, or fatigue where appropriate; authority does not require a stern expression. In Hidden Info, give them a specific private stake and relevant relationships without making every official corrupt or secretly omniscient.
- Abilities and Combat Style must reflect actual training. A noncombatant official can seek protection, negotiate, withdraw, or summon help through an established channel. Their title does not grant spells, invulnerability, unlimited resources, or knowledge of every private affair. Their portrait should convey a specific public duty through posture, setting, and appropriate equipment, while retaining their affinities and personality.

### Affinity Count: Weighted Random Selection

Randomly choose the number of affinities for each new NPC before selecting the actual elements or schools: **one affinity 65%**, **two affinities 25%**, and **three affinities 10%**. Make an independent weighted draw for each character. Do not add affinities just to account for every ability, a rare species, a visual theme, or a character quirk; affinity affects ease of learning, not access or power. Use the result as rolled rather than quietly adding extra affinities to make a character seem more special.

The labels below are an authoring aid, not separate Voyage schema fields. Voyage's `personality` field is an array of strings, so each labeled personality cue becomes one string in that array. For NPCs whose authored details must remain stable, use `detailType: "detailed"`; the community schema guide says `basic` NPC details may be generated or overwritten dynamically. [NPC field guide](https://wiki.unofficial.voyage/world/npcs)

Time is never an affinity for any character, including oracles. It is a configured reserved skill, absent from ordinary character creation, starting studies and automatic developer grants; do not supply a casual teacher, manual or awakening. Divination can observe past or future impressions without manipulating time. Space needs prior Gravity preparation; the Water/Ice, Earth/Metal and Wind/Sound relationships are historical rather than compulsory parent studies. Magitech and Spellcraft are technical skills, not affinities.

Spell invention or substantial blueprint redesign requires an actual Spellcraft check. Casting a learned spell uses its discipline; martial techniques do not require Spellcraft. Describe training and limits inside the existing sections. Necromancy belongs to Soul and specifies whether a spell animates remains or involves a conscious spirit. Ordinary physical actions remain useful; demanding techniques can spend Stamina, spells use Mana and injuries affect Health. Add no resource section or new profile bullet to an NPC card.

## Name Order

For humanoid people, write names as **First name Last name**, regardless of language or cultural inspiration. Keep this order consistent in notes and Voyage entries; do not switch to family-name-first order for Japanese-inspired names.

Nonhumanoid individuals use names appropriate to their kind instead of being forced into a human given-name/surname pair. An ancient dragon can have an original resonant, compound-syllable draconic name; an isolated giant can have a short personal name or an established local epithet. Do not copy a named character or assert an invented name is an authentic translation from another franchise. Preserve each creature's exact canonical identity in factual references. A unique named creature merits an NPC record; ordinary interchangeable monsters remain npcTypes. Orrum is the authored yeti of Drakenspire, not a reusable yeti encounter template.

## References to Other Characters

Whenever an NPC note states a fact or relationship about another named character, use that character's complete canonical **First name Last name**. Role descriptions are fine when unambiguous. Canonical JSON keys, proper names, roster lists and state updates retain the full identity.

Spoken dialogue and ordinary narrative address are different: characters can naturally say a first name, surname, title or appropriate honorific, such as "Professor Saitō," "Sanada-sensei," or "Hinae." Dialogue examples may use those forms when the speaker and addressee are clear. A shortened address never creates another NPC, renames the stored character or grants a previously unknown identity. Use full names for introductions, formal identification and resolving ambiguity rather than every utterance.

## Reusable NPC card structure

### [First name Last name]

### Appearance

[A concise, stable description of physical appearance and presentation: species, build, face, **hair color and style**, **eye color**, and a distinctive feature or silhouette. Always explicitly state both hair color and eye color here; do not make them separate sections. General clothing style may be noted when useful, but do not imply the character wears the same outfit in every scene. Record visual facts for the character bible, not art style, camera framing, or an image-generation prompt. Portrait prompts and image assets are handled separately from this character note and are not written into Voyage Studio.]

### Basic Info

[First paragraph: a public-facing description of identity and role, public reputation, and current situation. Include only details a player could reasonably know or observe. A publicly known combat reputation can go here; private tactics and secrets do not. Avoid repeating the full Appearance section. When converting the NPC to Voyage, include the key narrated appearance details in `basicInfo`, because that is the field the story narrator reads.]

[Second paragraph: **Equipment:** describe the weapons, tools, work kit, and personal items the character normally carries or keeps close at hand, regardless of their current outfit. If the character has a weapon, mention it first; if they have no weapon, do not invent one and begin with their other usual gear. Focus on recognizable or story-relevant items rather than a full inventory. Keep capabilities in Abilities and clothing in Appearance.]

Immediately after the two Basic Info paragraphs, add the applicable profile bullets below directly, without a heading. These fields make the roster easy to scan; some are planning metadata rather than direct Voyage NPC fields, so map them to the current schema when building JSON instead of assuming every label is a valid JSON property.

- **Gender:** [Character's gender.]
- **Age:** [Exact age or approximate range, as appropriate.]
- **Species:** [Species or people.]
- **Role in faction:** [Position, responsibility, or standing within that faction.]
- **Occupation / public role:** [Optional, when different from the faction role.]
- **Academic standing:** [Optional for students: year, track, class, club, or other individual status; students do not need to be divided into cohorts.]
- **Magic affinity:** [One or more one-word elements or schools of magic, comma-separated.]

Do not add a **Faction** field to the NPC authoring note; keep **Role in faction** when it helps explain the character's position or responsibilities. Also leave runtime setup fields such as current location, current area, combat tier, and starting relationship out of the note. These are handled by Voyage's engine or world setup, not by this character-creation format.

### Hidden Info

**Private motive:** [What the character truly wants and what they are pursuing now.]

**What they conceal:** [A secret, contradiction, or important omission in their public story.]

**Concealment and knowledge:** [Who knows the concealed information, who suspects it, and how the character keeps it hidden.]

**Pressure point:** [What might change their choices, unsettle them, or earn their trust.]

**Relationships:** [Important ties to other characters, classes, academies, or factions.]

Named relationships are selective. Give the cast a few specific connections where they create useful scenes; do not pair every new NPC with another roster member or repeat the same friendship across the cast. Family, coworkers or ordinary acquaintances can remain unnamed when no authored individual is needed. Keep this existing field proportionate to what is actually established.

**How it surfaces:** [Behavior, clues, or earned circumstances through which the player can discover the information.]

### Personality

Write each item as a specific behavior or response pattern. Use the following labels where they give the character useful guidance; entries should be specific to the individual rather than filled with generic traits.

- **Core:** [A contradiction or tension that shapes their choices.]
- **Default behavior:** [What they reliably do in ordinary interactions.]
- **Under pressure:** [How they change when challenged, frightened, embarrassed, or losing.]
- **Speaking Style:** [Cadence, register, and how their voice changes when sincere or upset.]
- **Courtship Style:** [How they show interest, invite closeness, and respond to reciprocation or rejection. If romance does not apply, state that clearly.]
- **Jealousy Style:** [What provokes it, how it appears, and how they handle it. If jealousy is not relevant, define their non-romantic response to rivalry or attention rather than leaving the behavior ambiguous.]
- **Routine or Quirk:** [A small recurring habit that makes them feel lived-in.]
- **Bond Progression:** [Optional: how their behavior changes as trust deepens.]

The community guide recommends behavioral entries rather than adjective lists, and notes that a distinct speaking-style entry can help keep dialogue consistent. [NPC field guide](https://wiki.unofficial.voyage/world/npcs)

### Abilities and Combat Style

Include this section for NPCs whose combat may matter. Keep abilities as prose descriptions of what the NPC can do and how they use it. End the list with a fighting-style summary covering preferred range, tactics, emotional tone, adaptation, and when they disengage. For a noncombatant, state their practical response to danger—such as fleeing, hiding, negotiating, or surrendering—instead of inventing combat abilities.

- **[Ability name]:** [What it does and how the NPC uses it.]
- **[Ability name]:** [What it does and how the NPC uses it.]
- **Fighting Style:** [How the NPC approaches a fight and adapts when the situation changes.]

The community guide treats NPC abilities as narrative context for combat decisions, not player-usable abilities, and recommends varied capabilities for combat-relevant characters. [NPC field guide](https://wiki.unofficial.voyage/world/npcs)

## Quality check

- Basic Info contains no private reveal or hidden motivation.
- Appearance records stable visual facts without becoming an image prompt; Basic Info stays concise and public-facing.
- Appearance explicitly states both hair color and eye color, within the existing section.
- In the JSON export, established narrated appearance is included in basicInfo. visualDescription alone supplies image generation and is not a substitute for narrator-facing facts. Keep existing portrait URLs unchanged when repairing this omission.
- Hidden Info distinguishes what is true, what the NPC wants, who knows, and how the player could learn it.
- Factual character references and stored identities use canonical full names; spoken examples may use natural address with clear identity.
- Personality entries describe observable choices, not just adjectives or biography.
- Speaking, courtship, and jealousy styles give the narrator concrete behavior; irrelevant romance is explicitly ruled out.
- Combat style is supported by the abilities and role the NPC actually has.
- For a new generic adventurer, an appropriate primary weapon is named in Equipment, the existing fighting-style prose explains its preferred stance and use, and the choice adds meaningful variety among recent adventurers. Any explicit unarmed exception is preserved rather than silently rewritten.
- For a governing character, the actual remit, authority limits, relevant work equipment, and individual way of handling decisions are clear; the office grants no invented powers or automatic combat ability.
- The number of affinities follows the weighted random selection above; one affinity is the most common result.
- Keep engine-managed placement and starting-state fields out of the character note.
- Details are distinctive without requiring every roster character to have the same depth.

## References

- [Unofficial Voyage NPC field guide](https://wiki.unofficial.voyage/world/npcs) — community-maintained guidance on NPC fields and authoring.
- [NPC Chat Replies guide](https://wiki.unofficial.voyage/ai/generateDialogue) — guidance on NPC voice, tone, and conversational behavior.
