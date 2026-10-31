# Patch Note Creation Guide

Use this guide for every future world update. Keep the release post in a standalone `.md` file and provide its exact contents in a fenced `markdown` block when the author wants to copy it into Voyage. Screenshots are tone and layout references, not a request to repeat their old changes.

## Public release post

Aim for about 150–250 words for a major update and 60–130 for a small patch. Use an emoji and clear update title, a short welcoming introduction, and two to four grouped lists. Prefer concrete player benefits over implementation detail. A final friendly line is optional.

State what actually shipped. Include the main feature, useful creation/start changes and visible fixes. Mention an important scope restriction plainly, such as solo-only automatic custody. Preserve mystery rather than publishing an encounter's hidden condition or the easiest exploit.

Do not include trigger IDs, storage keys, counters, schema limits, JSON paths, fixture counts, source hashes, internal drafting history, or speculative future features. Do not say “flawless,” “fully tested,” “fixed all bugs,” or claim live testing that did not happen. Do not repeat prior soundtrack or balance changes merely because the newest source contains them.

Keep bullets parallel and readable. Emojis identify groups rather than decorate every sentence. Avoid a full NPC roster, exact menu inventory, legal code or exhaustive list of edge cases. Public patch notes are an invitation to play, not the implementation manual.

## Separate development notes

Record the source export and hash, actual changed sections, retained user edits, mechanics and ownership, references consulted, validation performed, fresh-game versus existing-save implications, and a short manual test checklist. These notes can name IDs and counters because they are author-facing.

Keep the downloadable world, canonical world and standalone section replacements synchronized. Provide the full export first when several sections depend on one another. Preserve the incoming source as a rollback reference without creating redundant media archives.

## Suggested public structure

```markdown
## [emoji] [Update title]

[One or two sentences about the experience this update adds.]

### [emoji] [Main feature]
- [Concrete addition.]
- [Player-visible benefit.]

### [emoji] [Creation, story or quality improvements]
- [Grouped additions.]
- [Visible fixes or refinements.]

[Short closing line, if it adds something.]
```
