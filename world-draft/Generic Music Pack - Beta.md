> Musical direction superseded on 2026-10-30 by [Soundtrack Bible - Beta](Soundtrack%20Bible%20-%20Beta.md). Keep this document as a reference for the stock family mapping; use the newer song-led, warm jazz/hip-hop direction and contextual sets for production.
# Generic music replacement briefs - Glowhaven Beta

2026-10-30. These are composition/generation briefs for an initial generic soundtrack, not audio files or imported music replacements. Ordinary combat is included; boss themes are deferred.

## How Voyage organizes the files

Each music entry is a track family. Its variants are alternative recordings. A single Main mix URL works across contexts; optional narration/gameplay URLs provide separate versions. Cues and mood tags select families contextually, while triggers can pin one. Variant choice and duration belong to the running game. One variant per family is valid.

The active export has 21 families and 43 variants. Character creation selects CharacterCreationFantasy, whose three default recordings are FantasyCharacterSelectA, B and C. CharacterCreationFuturistic is not the selected creation family. No authored music-pin triggers are present.

Technical reference: [community music schema](https://wiki.unofficial.voyage/other/gameplayMusicSettings). Official [Patch 2.45.3](https://voyage.io/whats-new/patch/patch%3A100001203) confirms Studio upload, preview, replacement and removal.

## Initial replacement workflow

1. Start with one finished instrumental per family. Three variants are optional variety, not a requirement.
2. Keep the existing family IDs, cues and mood tags while changing their audio.
3. Upload a new track into the remaining Main mix card.
4. Remove unwanted alternative cards as each family is replaced; otherwise those default variants remain configured.
5. Inspect Advanced. When using a single Main mix for everything, clear the old optional narration/gameplay audio fields so the default Latitude recordings are not left configured alongside it.
6. Preview both narrated playback and ordinary play after replacing a paired default.
7. Keep CharacterCreationFantasy as the selected creation family. CharacterCreationFuturistic can be removed from this fantasy-only catalogue when desired.
8. Retain at least one valid audio variant for every family you keep.

This pass proposes 20 generic briefs covering the fantasy-used families. If making fewer recordings first, one sad cue can temporarily cover Dead/Eulogizing; one fragile cue can cover Near_Dead/Dying; and one melancholy cue can cover Morose/Distraught. Those are production shortcuts, not a request to make three identical tracks.

## Shared musical direction

Instrumental fantasy JRPG background music for an adult magic-academy adventure with ordinary city life, study, friendship, exploration and occasional danger. A coherent acoustic palette: chamber strings, flute/clarinet/oboe, piano, harp, celesta, acoustic guitar and restrained percussion. Match each cue's mood without making every scene grand or urgent.

Suggested production target: roughly 2-3 minutes, a short unobtrusive entrance, a stable musical bed and a loop-friendly ending that can be edited into a clean loop. Keep melodies and transients comfortable under spoken dialogue. No lyrics, spoken words, vocal chops, choir, abrupt trailer hits, jump scares, long silence, huge final chord, or lengthy build to a drop. A generator's loop claim still needs an actual listening/edit check.

The tempo values below are composition suggestions, not Voyage settings. Paste the shared direction together with the individual brief, or use the standalone prompts file.

## Family-to-track mapping

| Existing family | Proposed track title | Direction |
| --- | --- | --- |
| CharacterCreationFantasy | A New Beginning | Warm anticipation and light magical wonder |
| Investigatory | Following a Clue | Curious, precise, lightly playful mystery |
| Apprehensive | Something Amiss | Restrained unease and unresolved tension |
| Awestruck | Beyond the Gate | Spacious beauty and discovery |
| Calm | Quiet Hours | Rest, study and peaceful interiors |
| Dead | A Quiet Farewell | Gentle, subdued grief |
| Distraught | Words Left Unsaid | Emotional friction and hurt |
| Eulogizing | Lanterns in Remembrance | Respectful reflection and remembrance |
| Exuberant | Town Festival | Lively celebration and busy social scenes |
| Fighting | Crossed Blades | Ordinary encounters and training combat |
| Happy | Familiar Faces | Warm daily life and friendship |
| Morose | Rain at the Window | Loneliness, regret and introspection |
| Pursued | Keep Running | Chases and escape |
| Spooked | An Unlit Corridor | Eerie spaces and uncertainty |
| Triumphant | A Small Victory | Earned success without a grand finale |
| Unconscious | Between Dreams | Soft, floating dreamlike passages |
| Travelling | Open Roads | Exploration and forward movement |
| Near_Dead | Faltering Breath | Fragility and restrained urgency |
| Dying | Holding On | Fading strength and vulnerable stillness |
| Recover | Morning After Rain | Relief and a gradual return of warmth |

## Individual composition briefs

### CharacterCreationFantasy - A New Beginning

About 88 BPM in a gentle 6/8. A small piano theme passes between flute, warm strings and a few celesta notes, supported by harp arpeggios. Convey a new chapter, curiosity and the inviting scale of a magical city. Let the melody breathe so players can read and customize comfortably. A subtle recurring motif, modest dynamic movement and a calm return to the opening. No battle rhythm or triumphant fanfare.

### Investigatory - Following a Clue

About 92 BPM. Pizzicato strings, bass clarinet, muted piano and light wooden percussion create patient forward motion. Curious and quietly clever, suitable for comparing notes, searching shelves, following evidence or inspecting an unfamiliar object. A small question-and-answer motif develops through changes in texture. Keep the tension light and the pulse steady; avoid horror stingers, comedy sound effects or urgent chase energy.

### Apprehensive - Something Amiss

About 68 BPM. Low cello, soft piano, a restrained string pulse and thin woodwind tones suggest that something needs attention. Unresolved harmony and carefully spaced notes create unease without announcing an attack. Useful for suspicious conversations, uncertain negotiations or approaching a risky place. Sustain a readable, quiet texture without a giant crescendo, pounding heartbeat or jump scare.

### Awestruck - Beyond the Gate

About 72 BPM with spacious phrasing. Harp, celesta, warm sustained strings and a clear flute melody open into a broad luminous harmony. Convey the beauty of seeing a remarkable magical landscape or impressive architecture for the first time. Wonder can swell gently before settling into a flowing background texture. Keep percussion minimal and preserve intimacy; no choir, sacred vocal effect or world-ending spectacle.

### Calm - Quiet Hours

About 66 BPM. A warm piano, breathy flute and soft bowed strings share a simple relaxed motif over slow harp figures. Suitable for reading, recovery, a quiet garden, an inn room or the end of a class. Stable harmony, small variations and generous space between phrases. Peaceful rather than sleepy-sad, with no dramatic rise or attention-demanding solo.

### Dead - A Quiet Farewell

About 48 BPM. Sparse piano and a restrained solo cello carry a small descending motif, with low warm strings underneath. Convey silence after loss and private grief without melodrama. Let notes decay naturally, retaining enough movement for a background loop. No funeral march, choir, sound effects, flatline tone or violent emotional climax.

### Distraught - Words Left Unsaid

About 84 BPM. Piano figures and an expressive cello line sit over restrained pulsing strings. Emotional disagreement, a painful realization or strained trust; the energy comes from unsettled harmony and interrupted phrases. Maintain a measured tempo and a human scale. Avoid turning the cue into physical combat, horror, a romantic song with vocals or a huge tragic climax.

### Eulogizing - Lanterns in Remembrance

About 60 BPM. Gentle oboe, low strings, piano and occasional harp notes create a reflective, dignified atmosphere. A clear simple melody evokes remembering a person and acknowledging what remains. More tender and resolved than immediate shock, with quiet warmth inside the sadness. No heavy church organ, military march, choir or excessive sentimentality.

### Exuberant - Town Festival

About 116 BPM. Nimble fiddle, bright flute, strummed acoustic guitar and light hand percussion suggest a cheerful town celebration. Buoyant interlocking phrases and a dancing pulse, with small textural changes rather than constant escalation. Suitable for crowded social scenes, lively games and festivities. Keep the mix light enough for dialogue; no rowdy vocal shouts, electronic drop or huge orchestral finale.

### Fighting - Crossed Blades

About 138 BPM. Rhythmic chamber strings, a firm acoustic bass line, controlled toms and short woodwind phrases support an energetic fantasy encounter. Convey quick decisions, movement and determined resistance. A memorable compact motif and stable rhythmic drive keep it useful for repeated ordinary battles and supervised sparring. Moderate scale throughout: no boss choir, apocalyptic brass, cinematic trailer impacts or multi-phase escalation.

### Happy - Familiar Faces

About 96 BPM. Warm acoustic guitar, clarinet, light piano and softly articulated strings form a friendly everyday theme. Suitable for classmates talking, welcoming shops, a shared meal or a pleasant afternoon. A gently buoyant rhythm and small conversational melodic exchanges. Cheerful and affectionate without becoming childish, overly comic, saccharine or dominated by a soloist.

### Morose - Rain at the Window

About 64 BPM. Soft piano and viola trace a falling motif over muted strings, with a little harmonic uncertainty. Quiet loneliness, regret and reflection rather than immediate crisis. Let occasional warm notes suggest that the mood can change. Keep the texture steady and unobtrusive; no literal rain recording, sobbing, choir or dramatic film-score climax.

### Pursued - Keep Running

About 152 BPM. Short string ostinatos, nimble woodwind fragments and tightly controlled hand drums create clear forward momentum. A fantasy chase through streets or a desperate retreat, with urgency maintained through rhythm rather than sheer volume. Brief changes of register keep it alive without breaking the pulse. No vocals, sirens, heavy trailer hits, sudden silence or boss-battle grandeur.

### Spooked - An Unlit Corridor

About 60 BPM with a sparse irregular-feeling surface. Low flute, quiet string harmonics, delicate piano and a faint glassy timbre suggest unfamiliar movement in a dim place. Eerie and watchful, built around uncertainty rather than a revealed monster. Keep dynamics narrow and sounds musical. No whispers, screams, jump scares, loud dissonant stabs or a climactic attack section.

### Triumphant - A Small Victory

About 104 BPM. Bright strings, rounded French horn, piano and light percussion give a compact theme a sense of earned accomplishment. Suitable for finishing a difficult lesson, resolving a job or winning an ordinary encounter. Uplifting and confident without implying that the entire story is over. Settle into an easy continuation; no huge finale, victory chant, choir or bombastic fanfare.

### Unconscious - Between Dreams

About 56 BPM with little audible percussion. Celesta, harp harmonics, very soft strings and distant flute fragments drift around a slow modal pattern. Gentle, ambiguous and floating, suitable for sleep, dreams or a quiet liminal passage. Preserve an underlying musical shape so it remains listenable in repetition. No voices, breathing effects, frightening stingers or rhythmic pounding.

### Travelling - Open Roads

About 108 BPM. A clear woodwind melody rides over pizzicato strings, acoustic guitar and light hand percussion. Steady movement, curiosity and the pleasure of heading somewhere new. Flexible enough for roads, city walks and a prepared expedition. Use an easy walking pulse, small changes of instrumentation and a returning motif. No vast war march, battle climax or compulsory heroic fanfare.

### Near_Dead - Faltering Breath

About 58 BPM. Muted low strings, sparse piano and a soft irregular string pulse convey danger and depleted strength. Tense but restrained, with long spaces between a few fragile melodic fragments. Suitable for a badly hurt character awaiting help. Do not overwhelm dialogue with frantic percussion, literal heartbeats, medical beeps, horror effects or an automatic death-resolution chord.

### Dying - Holding On

About 46 BPM. A very small piano figure and low strings hover around an unresolved harmony, with occasional thin flute notes. Intimate, vulnerable and suspended, as though every small movement matters. Keep the music low, sparse and continuous, without deciding the scene's outcome through a grand ending. No vocals, flatline sound, cinematic death hit or enormous sorrowful crescendo.

### Recover - Morning After Rain

About 76 BPM. An ascending piano motif gradually meets warm flute, gentle strings and harp, moving from uncertainty toward quiet reassurance. Suitable for waking after rest, receiving care or returning to ordinary life after danger. Let relief emerge gradually and remain modest. No instant victory fanfare, ecstatic celebration, dramatic climax or vocal element.

## Listening and upload checks

These are audio-production checks to perform on the actual finished files, not validations already completed:
- Listen to the whole track, including its entrance and ending.
- Check that the intended mood is stable instead of changing genre halfway through.
- Test the track beneath ordinary narration volume.
- Check for unwanted vocals, sudden loud hits, distortion and uncomfortable high tones.
- Edit the start/end if needed for a smooth repeated listening experience.
- After upload, verify the intended family, remaining variants and optional mix fields in Studio.
- Keep the selected character-creation family pointing at an existing family ID.

The world JSON currently retains its supplied audio URLs. This document records the replacement plan; no audio was generated, uploaded, removed or auditioned by Codex in this pass.