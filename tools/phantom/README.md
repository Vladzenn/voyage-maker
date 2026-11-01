# Character creation and polish patch

The full world remains canonical. These original content tables and portable helpers document one minor patch, not a second daily source of truth.

- `build.py --source PATH --output PATH` reads an explicit current Studio export and writes a candidate. It never silently rebuilds from an older Alpha.
- `content.py` contains professions, cosmetic choices, items and kits.
- `talents.py` contains forty-eight bounded gifts and their selected techniques. These are original setting adaptations rather than copies of another world's overpowered bonuses.
- `manifest.json` records additions, the incoming source hash, source-preservation fingerprints and the level comparison.
- `validate.py [PATH]` is this release's preservation audit. Its fingerprints must be revised deliberately when later authorized edits change protected records; it is not a permanent CI freeze.
- `export.py` packages the current canonical world, a native solo Permadeath variant and a review guide. `--candidate PATH` explicitly installs a separately validated candidate.

`node tools/test_creation.cjs` exercises creation arithmetic, actual trait grants, finite equipment grants, badge reward ownership and music routing data. These are local fixtures, not live UI, image-generation or semantic-AI tests. The ordinary project commands also validate all trait references and current size caps.

The optional media flag remains unchanged: the Studio tooltip was tautological, the browser helper failed, and neither proves automatic image backfill for authored catalogue items. Do not bulk-enable `needsMediaGeneration` on the basis of its label.
