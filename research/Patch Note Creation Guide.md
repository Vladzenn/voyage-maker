# Patch Note Creation Guide

Use this guide for every future world update. Keep the release post in a standalone `.md` file and provide its exact contents in a fenced `markdown` block when the author wants to copy it into Voyage. Screenshots are tone and layout references, not a request to repeat their old changes.

## Public release post

Minor patches are simple and compact; major updates are fuller, more descriptive announcements. Aim for about 60–150 words for a small patch, allowing more when several distinct changes need grouping. For a substantial major release, roughly 400–700 words is a useful starting range, adjusted to the content rather than treated as a quota. Give the main additions room to explain what players can experience, how they fit the world and why they are worth exploring. Do not compress a major expansion into the same short checklist used for a minor patch.

Use an emoji and clear update title, a welcoming introduction, and thematic sections with breathing room. Major posts can mix short descriptive paragraphs with selected grouped bullets; they do not need a bullet for every sentence or a fixed limit of two to four groups. Keep minor posts quick to scan. Prefer concrete player benefits and inviting detail over implementation detail or padding. A final friendly line is optional.

For minor patches, the title is exactly **an unrelated animal emoji + Minor Patch n**, for example `## 🐙 Minor Patch 3`. Choose the animal independently of the content; do not use a feature-themed icon or append a descriptive subtitle to the title. Continue the existing minor-patch sequence across major releases. The author's confirmed published sequence is Minor Patch 1, Minor Patch 2 and Minor Patch 3; the next new minor release is **Minor Patch 4**. An import correction within the same release does not automatically increment that number. Thematic feature names and suitable emojis belong in the body as optional subheadings. An introduction is optional when the grouped bullets already read naturally.

State what actually shipped. Include the main feature, useful creation/start changes and visible fixes. Mention an important scope restriction plainly, such as solo-only automatic custody. Preserve mystery rather than publishing an encounter's hidden condition or the easiest exploit.

When the author asks for unlock guidance, include a brief, accurate player-facing explanation of the relevant achievement, carried item or place. That explicit request takes precedence over the default preference to withhold hidden conditions. Explain how to find the content without revealing its later surprises or internal checks.

Honor any explicit “don't mention” instructions for a release. Record those implemented details in private development notes instead. Do not imply that a deferred engine investigation is a shipped fix merely because it was bundled into the work request.

Do not include trigger IDs, storage keys, counters, schema limits, JSON paths, fixture counts, source hashes, internal drafting history, or speculative future features. Do not say “flawless,” “fully tested,” “fixed all bugs,” or claim live testing that did not happen. Do not repeat prior soundtrack or balance changes merely because the newest source contains them.

Keep bullets parallel and readable. Emojis identify groups rather than decorate every sentence. Avoid a full NPC roster, exact menu inventory, legal code or exhaustive list of edge cases. Public patch notes are an invitation to play, not the implementation manual.

Use the author's release screenshots as the layout reference: an emoji title, a short conversational introduction, bold or heading-style feature groups, and concise bullets. Prefer broad descriptions over exact counts of NPCs, quests, triggers or adjustments. Reserve numbers for a headline addition whose scale matters, such as **300 new items**, or a gameplay value the player needs. A major label reflects a substantial expansion of playable experiences and systems; it does not require inflating the post with counts or claiming that all behavior has been playtested.

## Separate development notes

Record the source export and hash, actual changed sections, retained user edits, mechanics and ownership, references consulted, validation performed, fresh-game versus existing-save implications, and a short manual test checklist. These notes can name IDs and counters because they are author-facing.

Keep the downloadable world, canonical world and standalone section replacements synchronized. Provide the full export first when several sections depend on one another. Preserve the incoming source as a rollback reference without creating redundant media archives.

## Suggested public structure

Minor patch title:

```markdown
## 🦦 Minor Patch 4

### 🌟 [Feature group]

- [Concrete addition or player-visible improvement.]
```

Major update structure:

```markdown
## [emoji] [Update title]

[A welcoming introduction establishing the new experience and its place in the world.]

### [emoji] [Main feature]

[A short paragraph explaining the main feature through something the player can actually do.]

- [A meaningful part of that experience.]
- [A second feature or choice, with enough detail to be interesting.]

### [emoji] [People, places or new adventures]

[Describe the new setting, cast or opportunities without spoiling hidden outcomes.]

- [Specific player-facing addition.]
- [Different approaches or reasons to revisit.]

### [emoji] [Combat, creation or other improvements]

- [Grouped additions.]
- [Visible fixes or refinements.]

[Short closing line, if it adds something.]
```

For a large package, add further thematic sections as needed. Elaborate through concrete experiences and useful context, not internal mechanics, repeated praise, exhaustive counts or promises of perfect reliability.
