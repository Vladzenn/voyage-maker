# Runtime Content Boundary Checklist

Apply before publishing future world updates.

1. Identify the actual consumer of every new instruction: a local authoring tool, one Voyage generation task, a gameplay effect, a player tooltip or a lore reader.
2. Local guide paths, PNG saving/naming rules, file copying, Studio editing recipes, source-world comparisons, schema research and migration notes belong in research/authoring documentation. Runtime models cannot open those local files merely because a prompt names them.
3. Public appearance, location descriptions, item descriptions and ordinary tooltips should describe the person, place, object or choice. Keep authoring labels and record-maintenance instructions out of them.
4. Keep actual generation field contracts, identity resolution, knowledge limits, ownership rules and supported state operations in the tasks that consume them. Do not delete useful controls merely because they contain technical terms.
5. World lore should state stable world facts. Put limitations of the implementation in development notes, while retaining any necessary behavioral restriction in the appropriate runtime task or mechanical rule.
6. Every quest needs a completion owner. Prefer one native outcome check for a simple undertaking; preserve explicit stages for actual intermediate decisions, permissions, evidence or personal consequences. Do not add a final report unless the accepted scope calls for it.
7. Trace storage readers through both literal writes and computed script writes. Execute scripts with fixtures for dynamic keys; a text search alone cannot establish a missing producer.
8. Distinguish public shared outcomes from personal licenses, badges, credit, academic standing and reward recipients. An any-player check does not by itself identify the acting qualified player.
9. Validate the current field caps, including compact serialized AI-task size, encoded leaf size and both per-field and aggregate image-prompt limits after every addition.
10. Preserve IDs, actual cast/media, map coordinates and protected event behavior. Record exact edits, scenario checks and remaining live-test requirements. Do not call a local fixture a live playtest or treat a rewritten export as an existing-save migration.

11. Studio-observed requirement: each storyStarts key must exactly equal its name, including emoji and variation selectors. Use the shared story_start_names.py guard. Migrate typed start conditions and trait gates when renaming, retain Write Your Own’s native identity, and test custom input after import. Community documentation suggesting different IDs/display names does not override a live Studio rejection.
