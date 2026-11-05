"""Deliver the prose correction and the approved image for manual Studio upload."""
import hashlib
import json
import shutil
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
DEST=ROOT/'output/crownwater-row-correction-2026-11-05'


def main():
    DEST.mkdir(parents=True,exist_ok=True)
    src=ROOT/'world-draft/WorldAlpha - World.json'
    w=json.loads(src.read_text(encoding='utf-8-sig'))
    full=DEST/'The Schools of Magic, Arise! - Crownwater Row Correction - Full World.json'
    shutil.copyfile(src,full)
    sections={'Crownwater Row - Location.json':{'Crownwater Row':w['locations']['Crownwater Row']},
              'A Door of Your Own - Story Start.json':{'🏠 Ardelis: A Door of Your Own':w['storyStarts']['🏠 Ardelis: A Door of Your Own']}}
    for name,data in sections.items():
        (DEST/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    art=json.loads((ROOT/'tools/ardelis-phantom/crownwater-art.json').read_text(encoding='utf-8'))
    shutil.copyfile(ROOT/art['file'],DEST/'Crownwater Row.png')
    manifest={p.name:dict(bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in [full,*(DEST/s for s in sections),DEST/'Crownwater Row.png']}
    (DEST/'files.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(dict(directory=str(DEST),files=len(manifest),imageUpload='manual; no hosted URL added to the JSON')))


if __name__=='__main__':main()
