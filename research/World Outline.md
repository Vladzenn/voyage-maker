# World Outline

**Status:** first-pass outline from user-established canon, with draft decisions labeled separately. The matching JSON is [WorldAlpha - World.json](../world-draft/WorldAlpha%20-%20World.json). No city, kingdom, founder, or school-founder proper names have been settled beyond the names already listed below.

## Established canon

The setting is a kingdom whose culture revolves around magic. Its central city is a major place for study and training because the Evertree grows there and enhances local magic. Legend says four great archmages founded the city and planted the Evertree together. Their followers later founded four rival academies based on the archmages' philosophies. The schools provide broadly comparable education; their institutional cultures do not define every student's personality, beliefs, talents, or interests.

The four academies are Phoenix Wing Academy, Hydra Head Academy, Gryffin Tail Academy, and Dragon Hoard Academy. Their cultures are respectively shaped by strength, harmony, study, and wonder. These are cultural reference points rather than complete one-word ideals: each academy provides a broadly comparable education, and its culture does not define every student's personality, beliefs, talents, or interests. Phoenix Wing has strict teachers and a notably aggressive dueling club. Further school customs are open.

Each academy has one Archon on the Conclave of Archons. A larger council elects the Great Sage, and a candidate does not have to belong to the Conclave or the council. The Great Sage governs the city, manages the magical weave in the Evertree, and commands an elite strikeforce against dangerous threats. A term ends at the incumbent's death or after one hundred years unless the larger council reelects the incumbent for another term.

The current Great Sage is Ilyra Stillglass, also called the White Lotus. She is an elf who has held office for 254 years over three terms and has been reelected twice. The council has repeatedly judged her to be the best available choice. No one knows which academy she attended; a common rumor says her talent earned the respect of all four schools. She appears young, but is nearing the end of her lifespan, has grown slower, and is losing her sight. Her age cannot readily be remedied by magic. She still manages the Evertree's magical weave, while servants handle and read paperwork aloud. When the story opens, the academies are already maneuvering for the succession.

Ilyra's established appearance: petite, long blond hair, calm eyes, flowing white robes, delicate glass accessories, elegant heels, and a tall staff that looks oversized beside her. She is serene, composed, and wise.

The player begins as a student at one of the four academies. The chosen school is conveyed through one of four academy-specific story starts. No separate academy-selection trait is assumed in this draft.

## Proposed student-life loop

This is a gameplay proposal, not locked canon: begin in an immediate school-life situation; decide how to engage with a class, club, practice, exam, discovery, or social invitation; build or complicate relationships with students and faculty; then choose whether to follow personal goals into the wider city. Academy politics and the Great Sage succession can enter through people and events, but ordinary school life should remain playable and the opening should not require a crisis.

## Current JSON implementation choices

- The realm and region are temporarily called **The Kingdom** and **The City Region**; the complex map location is **The City**. These are functional labels, not settled setting names.
- The city is represented as one complex Voyage location with named school, civic, and Evertree areas, connected by an initial path graph. This is a compact authoring model; it is not a final map transcription.
- **The Council** and **The Elite Strikeforce** are descriptive faction keys for now. Their official names, membership, authority, and internal structure are open.
- Each story start opens on a small, choice-forward student scene: Phoenix Wing's dueling-club schedule; Hydra Head's group exercise; Gryffin Tail's unresolved seminar question; or Dragon Hoard's student exhibition. These opening incidents are draft prompts, not canon events.
- Ilyra is the only authored NPC in this first pass. The story-start prompt asks the narrator to introduce a small number of generated students or faculty; no named classmates have been established.
- The draft currently has no authored classes, traits, attributes, resources, quests, narrative events, or triggers. It establishes the opening structure and references first.

## Open questions

- What are the kingdom and city called, and what is the city's political/legal status within the kingdom?
- Who were the four archmages? What did each believe, and what did they actually do when planting the Evertree?
- What are the Archons' titles, selection rules, and individual academy roles? What body elects the Great Sage, and what is its formal name and membership?
- How does succession work when the Great Sage reaches a hundred years, becomes unable to serve, or dies? Can the incumbent resign?
- What are the elite strikeforce's name, structure, limits, and relationship to the council and Sage?
- What is the practical cost, risk, or boundary of magic, and what exactly does the Evertree enhance?
- What are each academy's curriculum, student traditions, clubs, rivalries, and approach to comparable qualifications?
- How do students progress through school years, classes, exams, clubs, and graduation? What parts should be tracked mechanically?
- What are the first-session tone, intended play scope, character creation choices, and content boundaries?
- What are Ilyra's age, elf lifespan, health details, private motives, personal relationships, and succession preference? Which of these should remain unknown to players?

## Draft boundaries

Treat the established-canon section as current user-provided facts. Treat the proposed loop and implementation choices as editable design decisions. Resolve open questions collaboratively before turning them into permanent lore, mechanics, or named characters.
