"""Package only the reviewed Ardelis selections; never bundle draft rerolls."""
import hashlib
import json
import shutil
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUT = ROOT / 'output/ardelis-2026-11-05'

def load(path):
    return json.loads(path.read_text(encoding='utf-8'))

def main():
    proof = load(HERE / 'art-verification.json')
    assert proof['complete'] and (proof['portraits'], proof['locationImages'], proof['areaImages']) == (24, 84, 2)
    full = OUT / 'The Schools of Magic, Arise! - Ardelis.json'
    assert hashlib.sha256(full.read_bytes()).hexdigest() == proof['worldSHA256']
    for ledger_name, archive_name in [('portrait-files.json', 'Ardelis - Principal Portraits.zip'), ('location-files.json', 'Ardelis - Location and Area Artwork.zip')]:
        entries = load(HERE / ledger_name)
        with zipfile.ZipFile(OUT / archive_name, 'w', compression=zipfile.ZIP_STORED) as archive:
            for entry in entries.values():
                path = ROOT / entry['file']
                assert hashlib.sha256(path.read_bytes()).hexdigest() == entry['sha256']
                archive.write(path, path.name)
    documents = ['Ardelis - Patch Notes.md', 'Ardelis - Development Notes.md', 'Ardelis - Map and Landmark Handoff.md']
    for name in documents:
        shutil.copy2(ROOT / 'world-draft' / name, OUT / name)
    readme = (
        '# Ardelis delivery\n\n'
        'Import **The Schools of Magic, Arise! - Ardelis.json** as the full world. It includes all existing content plus this expansion and the successful official artwork URLs.\n\n'
        'The files named **Ardelis - NPCs.json** and **Ardelis - Locations.json** contain only additions (and the updated Vladimir card). Do not replace an entire Studio section with those partial files. The canonical WorldAlpha section exports in world-draft contain complete sections.\n\n'
        'The portrait archive contains the twenty-three new principals and the authorized Vladimir replacement. The ninety-two supporting NPC cards have no new portraits under the approved principal-first scope. The scene archive contains one establishing image for each of eighty-four new locations and two additional area views. It excludes discarded rival drafts.\n\n'
        'Map tile images/crops and eighteen author-supplied pins are preserved exactly. Sixty-six added pins are approximate and are identified in the map handoff.\n\n'
        'Official asset uploads and draft validation are not a Studio world save, publication or live playtest. Import and test the listed routes and outcomes in the Development Notes before release.\n'
    )
    (OUT / 'README.md').write_text(readme, encoding='utf-8')
    with zipfile.ZipFile(OUT / 'Ardelis - World and Guides.zip', 'w', compression=zipfile.ZIP_DEFLATED) as archive:
        for name in [full.name, 'README.md', *documents]:
            archive.write(OUT / name, name)
        archive.write(HERE / 'placements.csv', 'Ardelis - Placements.csv')
    print(json.dumps({'delivery': str(OUT), 'portraits': 24, 'sceneImages': 86, 'worldSHA256': proof['worldSHA256']}))

if __name__ == '__main__':
    main()
