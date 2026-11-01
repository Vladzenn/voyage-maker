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
