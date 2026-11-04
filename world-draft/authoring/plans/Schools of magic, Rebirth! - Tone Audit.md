# Rebirth tone audit

4 November 2026 · Planning review

## Direction

Make Rebirth feel like a lived-in fantasy world where people have work, loyalties and obligations that predate the player. Let kindness show in what someone does or gives up. Let dangerous decisions leave practical consequences that the player can address. Keep narration observant and economical. Reserve lavish description for things worth stopping to look at.

Brookmeadow can be peaceful and generous. The city can look splendid. Shadowspire can be ridiculous. Those moods come from the place, the people and the moment. The default voice can give a market morning, an official inquiry and a dangerous fight different emotional weight.

## What the current project is doing

| Surface | Finding | Direction for the release pass |
| --- | --- | --- |
| **Narration and openings** | The canonical `narratorStyle` calls for an inviting fantasy-anime ensemble. `generateInitialStart` repeats the invitation at the task level. The Story task already calls for concrete nouns, distinct voices, sincere danger and clean player agency. | Revise the shared default and the repeated opening wording together. Keep the useful prose rules. Lead scenes with what people are doing, what is known and what can change. |
| **Dialogue and encounter selection** | NPC dialogue already draws on a character's own priorities and register. The encounter task explicitly gives school comedy its own patterns, and it also protects grief, rest and aftermath. Location generation treats comfort and comedy as regular options. | Keep plain talk, refusals, silences and earned jokes. Let actual scene context pick the comic, tender or uneasy register. Use ordinary work, politics, investigation and aftermath as equally useful scene material. |
| **Starts and modes** | The current Brookmeadow village start gets much of its character from Haruho's work and tally slate. Phoenix Wing already gives students a practical duty to each other. The guild opening can put a damaged fastening beside a concrete contract. Comedy and Slice of Life are deliberate player-selected modes. | Keep that specificity. Review Balanced as the main baseline and check that selected modes can still do what they promise. Keep starting roles, facts, authority and real choices consistent across tone variations. |
| **Art direction** | Active location and area prompts emphasize colorful 2D fantasy anime. The Brookmeadow sample has sunny fields and visible labor. The Guild Appraisal Bench shows the function of the room through scales and repairable gear. The Shadowspire exterior already carries a restrained, uneasy mood through distance and woodland shadows. | Build on the existing illustration language with practical clothing, wear, believable working clutter and light that comes from the scene. Let daylight and color remain available. Carry the existing Shadowspire approach into the tower, then use selective excess in the pocket realm. Review a few representative images before deciding which launch scenes need new art. |
| **Music and atmosphere** | Active families include `Calm`, `Happy`, `Travelling`, `Investigatory` and `Apprehensive`. `Happy` matches broad terms such as warm, kind, welcome and tender. The story prompt already distinguishes active combat, travel, death and pursuit from related conversation. The earlier soundtrack bible deliberately favors warm jazz and hip-hop for ordinary days. | Audit cue selection before commissioning music. Check whether a kind gesture during recovery makes the score cheerier than the whole scene warrants. Keep everyday grooves for scenes that suit them. Audition sparser arrangements under testimony, grief and strained negotiations. This pass reviewed configuration and briefs. Listening and live cue selection are build checks. |

[Canonical world configuration](../../WorldAlpha%20-%20World.json) · [Writing guide](../../../research/Narrative%20Writing%20and%20Quest%20Craft%20Guide.md) · [Art guide](../../../research/Location%20and%20Area%20Image%20Creation%20Guide.md) · [Soundtrack Bible](../../Soundtrack%20Bible%20-%20Beta.md)

## Apply it to Rebirth

- **The shore rescue.** The first shock is the unfamiliar body and a whole life the player still remembers. Use the borrowed bed, sand on the floor and someone who took time away from work to help. The broth is enough to carry the care in the scene. Let the player decide how they feel and what they disclose. The [revised opening](Schools%20of%20magic%2C%20Rebirth!%20-%20Planning%20Brief.md#the-featured-start) is the first prose example.
- **Village and port.** An ordinary job can matter because someone needs to get flour across the river before a kitchen shuts. Care, friendship and humor grow through repeat encounters. Early life has time to settle before the Ardelis inquiry.
- **The delegation.** Show who can ask, who can refuse and who risks losing work if they refuse publicly. A soldier closing a ledger at his officer's signal can do more than a speech about the whole kingdom. Keep the identity of the summoned person as an actual knowledge problem.
- **Vladimir and the pocket realm.** In a serious scene he listens, asks a precise question and keeps his own counsel. An optional visit can reveal his childish pride through an overbuilt room or a petty argument. The archmage's sense of humor belongs to him. The realm can show the resources and attention he poured into a whim. Both boards remain idea banks for that contrast.
- **The field test and rival.** Give the attack concrete objectives, civilians with believable priorities and consequences that persist once the immediate fight ends. Let the player see how control limits the rival's choices and how she responds if freed. Her own decisions and viewpoint can carry the aftermath.

## Release review

Start with the shared narrator and the opening task. Check encounter selection, NPC dialogue, and location prompts against the same set of scenes before expanding the edit. Compare actual outputs in the same starting state and chosen mode. Keep the edits short and check the prompt-size limits alongside the general optimization review.

| Scenario | What to check |
| --- | --- |
| Rebirth awakening, Brookmeadow routine work, and a regular academy opening | Care, quiet work and excitement each have room. Adult characters speak in distinct registers. The player keeps their response. |
| An official refusal, a guild contract and a village delivery that goes wrong | People have authority and limits. Practical fallout follows the actual choice and outcome. A peaceful or successful resolution can stand on its own. |
| Vladimir's serious conversation and a voluntary visit to the realm | The scenes feel different while Vladimir remains recognizably the same person. Players can find the humor by paying attention. |
| A cloaked attack, the field test, then the aftermath | The action has a readable objective. The aftermath keeps the real state of the people, injuries and evidence. The score follows what is happening in each scene. |
| Balanced, Comedy and Slice of Life with the same underlying encounter | Tone and pacing respond to the selected mode. Authored premises, consent and authoritative outcomes stay consistent. |

The audit and sample prose are planning deliverables. The Rebirth build will verify the changes in Voyage before applying them broadly.
