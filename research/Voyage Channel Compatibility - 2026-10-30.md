# Voyage channel compatibility audit - 2026-10-30

## Finding

The screenshot's v37.13 is a game-state compatibility requirement, separate from the creator's Alpha/Beta project milestone and the legacy WorldAlpha filenames.

Public version constants read on 2026-10-30:
- Normal site: schema major 37, compatibility revision 10.
- Beta: schema major 37, compatibility revision 10.
- Alpha: schema major 37, compatibility revision 13.

Primary sources:
- [Beta constants](https://beta.voyage.io/_next/static/chunks/74709-494196431fa98374.js), module 98593.
- [Alpha constants](https://alpha.voyage.io/_next/static/chunks/26645-96706d03771e9187.js), module 98593.
- [Compatibility helper](https://voyage.io/_next/static/chunks/45738-704a875aa9c7a526.js), module 36966.
- [Editor version guard](https://voyage.io/_next/static/chunks/pages/create/world/[shortId]/edit-6eee64896eede473.js).

The compatibility helper blocks when the source major is newer, or when the major matches and the source compatibilityRevision exceeds the local revision. The editor also reads compatibilityRevision from the world metadata returned by the service. A helper can stamp state with the current environment's revision.

This establishes the mechanical reason for the screenshot. It does not establish which save, publication, import, migration or environment first assigned revision 13 to this particular world. A save/migration in the newer environment is a plausible explanation, not a verified event in the user's history.

## Supplied export

The latest user attachment is 94b1c88b-c704-457a-a372-fcd36b27ab80/Pasted text.txt. Its only version-like scalar field is heroesVersion: 37. It contains no compatibilityRevision. Therefore the exported authoring JSON alone does not expose the revision-13 marker shown by the client.

Compared semantically with the active local WorldAlpha - World.json, only itemSettings and gameplayMusicSettings differ. Preserve the latest user export as the basis for the next requested merge so these changes are retained.

The export comparison does not prove that every field is supported by every channel. No live Beta Studio import, full platform validation or gameplay test was performed in this audit.

## Publication guidance

Target the normal/Beta-compatible engine for a release intended for ordinary players. Alpha is suitable when intentionally testing the newer engine and accepting that players may be prompted to switch channels.

Publishing from Beta is not itself a downgrade operation for an existing newer-format world. A reviewable compatibility attempt is a separate Beta draft imported from the latest user export, followed by Beta Studio validation and preview. If it accepts and plays correctly, that copy is a candidate for the regular release. Preserve the existing world until that check succeeds. If the newer version remains required, identify the unsupported state/feature or await the corresponding engine release rather than relabeling a version marker.

No world configuration, remote draft, publication or release setting was changed during this audit.