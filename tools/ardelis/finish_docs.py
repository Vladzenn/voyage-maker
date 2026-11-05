"""Mark this task complete only after exact artwork and official draft checks."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]

def load(name):
    return json.loads((HERE / name).read_text(encoding='utf-8'))

def main():
    art = load('art-verification.json')
    validation = load('official-validation.json')
    assert art['complete'] and validation['worldSHA256'] == art['worldSHA256']
    assert validation['result']['data']['valid'] and not validation['result']['data']['errors']
    assert not validation['result']['data']['warnings']
    path = ROOT / 'world-draft/Ardelis - Development Notes.md'
    text = path.read_text(encoding='utf-8')
    old = '**Delivery status while building:** content candidate and principal portraits exist; location artwork, final receipts, final validation and canonical installation are being completed. Do not treat this checkpoint as a published Studio update. The finished receipts and CURRENT_STATE entry supersede this line.'
    new = ('**Delivery status:** the completed local world includes twenty-four officially uploaded selected portraits '
           '(twenty-three new principals and Vladimir), eighty-four location images and two additional area images. '
           'Exact name/hash/URL assignments pass `art-verification.json`. The exact full file passed official draft validation '
           'with zero errors and warnings. Local regression checks pass. This is a local import package and GitHub project update, '
           'not a saved or published Studio world or a live gameplay test.')
    assert old in text or new in text
    text = text.replace(old, new)
    path.write_text(text, encoding='utf-8')
    current = ROOT / 'docs/CURRENT_STATE.md'
    text = current.read_text(encoding='utf-8')
    marker = '**In progress - Ardelis capital implementation' if '**In progress - Ardelis capital implementation' in text else '**Implemented locally — Ardelis capital'
    begin = text.index(marker)
    end = text.index('\n\n**Map documentation only', begin)
    status = ('**Implemented locally — Ardelis capital (5 November):** built from the approved Rebirth world plus the eighteen supplied '
              'unfinished location pins and twelve complete Ardelis map regions. The four-by-three grid, all incoming map URLs/crops '
              'and the eighteen x/y pins remain exact. Caelrath adds 84 sites, 115 NPC cards, 64 native quests, eleven factions, '
              '24 items, twenty techniques, 27 encounter/population types and four local beginnings. The royal family, noble houses, '
              'three major paladins, ordinary city life, serious adventurers, independent criminals and a celestial splinter cult '
              'support the Rebirth continuation and optional palace descent. The later requested luxury arcade, concert hall '
              'and bounded sewer site are included. Capital only: no Glowhaven port expansion or academy expedition assignment.\n\n'
              'Restricted sponsorship issues a real reusable route key; transit shares the existing endpoint, anomaly and same-turn '
              'lock pattern, with a fixed keyless return. Vladimir remains optional and independent. Noelle’s final selected portrait '
              'has lowered empty hands, direct gaze and an angled stance; her card describes a hand caster. All twenty-three new '
              'principals and the authorized Vladimir replacement have official portrait URLs. Supporting portraits remain deferred '
              'under the approved principal-first scope. Every new site has an uploaded establishing shot, with two extra area shots '
              'for the portal and empty experimental chamber.\n\n'
              '[Public Markdown notes](../world-draft/Ardelis%20-%20Patch%20Notes.md) · '
              '[mechanics, limits and live checklist](../world-draft/Ardelis%20-%20Development%20Notes.md) · '
              '[map and pin handoff](../world-draft/Ardelis%20-%20Map%20and%20Landmark%20Handoff.md). '
              'The full import is `world-draft/WorldAlpha - World.json`; named JSON, selected-art ZIPs and guides are in '
              '`output/ardelis-2026-11-05/`. `tools/ardelis/review.json` is the reversible preservation proof; '
              '`art-verification.json` binds selected bytes to exact target records. The exact final candidate passed official '
              'draft validation with zero errors and warnings, plus local structure and emitted-script regression checks. '
              'No Studio save, world publication, crop preview or live gameplay test is claimed. GitHub synchronization is reported '
              'only after the publish command succeeds. All old triggers, other NPCs, music, progression and Spider content remain exact; '
              'reviewed existing edits are the Evertree room wording, Vladimir’s visual description/portrait, the old relay chapter’s next '
              'lead and related Ardelis lore. Sixty-six new pins are approximate placements for the author’s later adjustment.')
    current.write_text(text[:begin] + status + text[end:], encoding='utf-8')
    readme = '''# Ardelis capital implementation

Completed local build on 5 November 2026. The actual delivery status and later edits live in `docs/CURRENT_STATE.md`.

The approved merge base is the canonical Rebirth world from `eda234f`, raw SHA-256 `77d47b4384db822c6021fb5c9ef29bde3daabfb557bf948b62f2a3bd3ccf8b59`. The supplied Locations section preserves all 307 old locations and adds eighteen unfinished pins. `source.json` retains those complete incoming records and the twelve author-supplied map regions, including exact images, crops, grid coordinates and original names. The grid is four columns by three rows. `placements.json` and its CSV distinguish preserved pins from sixty-six new approximate placements.

The final expansion contains 115 NPC cards (twenty-three new principals), 84 locations, 64 native quests, eleven factions, 24 items, twenty techniques, 27 type definitions, one developing arc and four beginnings. The capital's supporting cast includes workers, households, nobles, performers and serious adventurers. Ordinary church, paladins, household guards, the independent criminal group and the splinter cult have different interests and knowledge. Rebirth continues through Noelle and her command apparatus. The separate palace descent and sewer site remain optional. The earlier port proposal and Glowhaven academy expeditions are excluded.

## Files and rebuild boundaries

- `build.py`: guarded historical builder. It accepts only the verified original Rebirth base and refuses to overwrite a newer canonical world. After installation, do not reset the current world merely to rerun this builder. Future edits must use the then-current canonical world or a newly supplied Studio export.
- `review.json` / `previous_world.cjs`: exact reversible preservation manifest and historical test projection. Original reference fingerprints are not weakened.
- `major-people.jsonl`, `paladins.jsonl`, `people.txt`, `locations.txt`, `quests.txt`: reviewed authoring seeds, separate from the native output schema.
- `portrait-jobs.json`, `portrait-revisions.json`, `location-jobs.json`, `art-directions.txt`: saved built-in image-generation prompts. Final Noelle and Vladimir requests supersede their earlier drafts. No unrequested portrait rerolls.
- `portrait-files.json`, `location-files.json`: exact selected filenames and byte hashes. Twenty-four portraits and eighty-six scenes; no discarded portrait draft is packaged.
- `upload_art.py`: reviewed official upload sequence, resumable by target/name/hash. Credential comes from process environment only. It never writes Studio world data. `watch_uploads.py` picks up newly saved scenes without parallel receipt writers.
- `upload-receipts.json`, `portrait-urls.json`, `location-urls.json`, `area-urls.json`: successful official hosted URLs, with no API key or signed direct-upload URL. Exact rejected image moderation is not blindly retried.
- `verify_art.py --complete`: checks all twenty-four portrait and eighty-six scene assignments against actual PNG bytes and the candidate world; emits `art-verification.json`.
- `remote_validate.py`: reads the live official contract and sends only the draft candidate to `/validate`. `official-validation.json` identifies the exact full-file SHA and response. This is not a Studio save or publication.
- `landmarks.py`: regenerates the map handoff and complete placement CSV from actual records.
- `delivery.py`: packages the reviewed full world, guides and selected artwork in ignored `output/ardelis-2026-11-05/`.

## Mechanics and verification

Ordinary undertakings use typed native completion conditions and one reward owner. The local guild has one semantic board request check and offers one planned eligible job per actual request; it never automatically accepts a notice. Restricted key issuance verifies the actual recipient. Transit preserves existing route/anomaly behavior and fixed keyless return. The palace gate uses a narrow planning guard plus state backstop, with native semantic completion recognizing an actual feasible technical solution. These checks are not a state machine for every conversation.

`node tools/test_ardelis.cjs` executes real emitted scripts with supplied semantic answers. All historical behavior suites continue through exact reviewed projections. Local tests verify configuration and selected logic, not live AI interpretation, combat timing, multiplayer or Studio crop previews. The development notes contain the release playtest checklist. The final candidate passed official draft validation with zero errors and warnings.

The item catalogue remains close to its 250,000-unit cap. Do not expand it by copying verbose policy into every item. The historical worst-scene trigger budget reaches the documented limit; there is no claim of spare live scheduling capacity.
'''
    (HERE / 'README.md').write_text(readme, encoding='utf-8')
    print('Updated final delivery status and historical build boundaries.')

if __name__ == '__main__':
    main()
