# Official portrait uploads

`tools/voyage_portraits.py` uploads local PNG/JPG portraits through Latitude's Creator API. It does not generate images, install third-party code, replace the Studio draft or publish the world.

Set `VOYAGE_CREATOR_API_KEY` in the process environment. Never put its value in a tracked configuration file, CLI argument, report or source file. The tool reads it only to authenticate official API requests. No credential is attached to the returned signed image-upload URL. Redirects are not followed.

The default API host is production. This batch explicitly used the author's requested Alpha host and verified owned world **0kL8UR7rgsu2**, The Schools of Magic, Arise! Never automatically retry a mutation against another environment.

Dry-run a selected roster:

```sh
python tools/voyage_portraits.py --short-id 0kL8UR7rgsu2 --api-base https://api-alpha.aidungeon.com/creator/v1 --select tools/crucible/manifest.json --replace-selected
```

Add `--apply --remote-validate` to upload and apply the returned URLs. Use `--world` and `--output` for a separate candidate, `--images` for another directory, and `--state`/`--report` for named resumable runs. A selection file can be an array of exact NPC names or an object containing a `npcs` array. Without `--replace-selected`, existing HTTPS portraits are preserved. Replacing valid artwork requires an explicit selection.

Names use exact canonical keys after Unicode NFC normalization. Duplicate stems, missing NPCs, absent selected files, invalid images and upload failures are reported rather than guessed. PNG/JPEG signatures supply the actual MIME and dimensions. Current live limits are obtained from OpenAPI.

Each name/file-hash/target/world combination retains independent allowance and moderation idempotency keys in the ignored resume ledger. A completed receipt supplies its URL without reuploading. Partial byte uploads and moderation can resume; changed files get separate receipts. Settled moderation rejection is not silently retried with the same picture. Rate limits and server failures use bounded backoff. The API key and signed PUT URL are absent from logs and ledgers.

The uploader proves that its only world edits are the selected `npcs[name].portraitUrl` values, performs local validation, and can request official draft validation. Source-file drift aborts the merge while retaining receipts. Reports contain a reviewable before/after URL diff. Never treat successful upload as a saved or published Studio revision.

Current receipt: [43 uploaded replacements](portrait-uploads-2026-11-02.json). Current portraits have 43 distinct official hosted URLs, each checked against its exact filename and SHA-256. Existing location/map URLs were retained; no location image was replaced by this batch.

Official contract: [OpenAPI](https://api-alpha.aidungeon.com/creator/v1/openapi.json), [agent guide](https://api-alpha.aidungeon.com/creator/v1/agent-guide.md). The reviewed World Puppeteer uploader was read as reference only; our Python implementation has no third-party dependencies.

## Area and location artwork

The shared upload routine also accepts the live contract's `AREA_IMAGE` and `LOCATION_IMAGE` targets. These have separate receipt identities from portraits, even for an identical name and image file. The portrait CLI keeps its portrait-only default.

`tools/location_area_art.py` prepares this explicitly scoped academy/guild batch from a supplied locations section. Its manifest gives each image an exact parent location and, for areas, an exact nested area key. It retains existing valid area images; only the three explicitly selected recent Conservatory location shots are replacements. Uploaded shots receive the official URL, existing crops remain intact, and newly illustrated areas receive a centered default crop.

```sh
python tools/location_area_art.py prepare --source "path/to/current-locations.json"
python tools/location_area_art.py upload --short-id 0kL8UR7rgsu2 --api-base https://api-alpha.aidungeon.com/creator/v1
```

Generate/review the missing files listed by preparation before uploading. As with portraits, supply credentials only through the process environment. A changed canonical file aborts the merge. Successful uploads are resumable from the ignored ledger; the final report records each exact address, target, SHA-256, hosted URL and before/after diff. The helper rejects changes to other fields or existing crops, checks all required areas have images, and runs local and official draft validation before writing a separate full-world candidate and locations-only export. Installing that candidate and GitHub publication remain separate local workflow steps; no Studio save or publication occurs.
