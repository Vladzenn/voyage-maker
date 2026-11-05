"""Copy the exact canonical full world and complete changed sections for Studio."""
import hashlib
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEST = ROOT / 'output/ardelis-phantom-2026-11-05'
SECTIONS = ['Items', 'Locations', 'NPCs', 'Regions', 'Story Starts', 'Triggers', 'World Lore']


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    files = [('WorldAlpha - World.json', 'The Schools of Magic, Arise! - Ardelis Local Beginnings - Full World.json')]
    files += [(f'WorldAlpha - {s}.json', f'{s}.json') for s in SECTIONS]
    manifest = {}
    for source, target in files:
        src = ROOT/'world-draft'/source; dst = DEST/target
        shutil.copyfile(src, dst)
        json.loads(dst.read_text(encoding='utf-8'))
        manifest[target] = dict(bytes=dst.stat().st_size, sha256=hashlib.sha256(dst.read_bytes()).hexdigest())
    (DEST/'files.json').write_text(json.dumps(manifest, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(dict(files=len(files), directory=str(DEST))))


if __name__ == '__main__':
    main()
