"""Verify selected bytes, exact target names and official URL assignments."""
import argparse
import hashlib
import json
from pathlib import Path
from urllib.parse import urlparse

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]

def load(name):
    return json.loads((HERE / name).read_text(encoding='utf-8'))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--complete', action='store_true')
    args = ap.parse_args()
    world_path = ROOT / 'output/ardelis-2026-11-05/The Schools of Magic, Arise! - Ardelis.json'
    world = json.loads(world_path.read_text(encoding='utf-8'))
    review = load('review.json')
    receipts = load('upload-receipts.json')
    portraits = load('portrait-files.json')
    scenes = load('location-files.json')
    jobs = load('location-jobs.json')
    # The canonical everyday name can remain a longer approved full name.
    vladimir = [name for name in portraits if name not in review['contents']['majorNPCs']]
    assert len(vladimir) == 1, vladimir
    expected_portraits = set(review['contents']['majorNPCs']) | set(vladimir)
    assert set(portraits) == expected_portraits
    assert len(jobs) == 86 and len({j['id'] for j in jobs}) == 86
    if args.complete:
        assert set(scenes) == {j['id'] for j in jobs}, 'Location images remain unfinished.'
    results = []
    seen_paths = set()
    seen_hashes = set()
    for kind, entries in [('portrait', portraits), ('scene', scenes)]:
        for key, entry in entries.items():
            file = ROOT / entry['file']
            raw = file.read_bytes()
            digest = hashlib.sha256(raw).hexdigest()
            assert digest == entry['sha256'], f'Changed bytes: {file.name}'
            assert entry['file'] not in seen_paths, 'Duplicate selected filename'
            assert digest not in seen_hashes, 'Same image assigned twice'
            seen_paths.add(entry['file']); seen_hashes.add(digest)
            if kind == 'portrait':
                target = 'NPC_PORTRAIT'; address = key
                url = world['npcs'][key].get('portraitUrl')
            else:
                target = entry['target']
                if entry['kind'] == 'location':
                    address = entry['name']
                    url = world['locations'][address].get('images', {}).get('establishingShot', {}).get('imageUrl')
                else:
                    address = entry['location'] + '::' + entry['area']
                    url = world['locations'][entry['location']]['areas'][entry['area']].get('images', {}).get('establishingShot', {}).get('imageUrl')
            receipt = receipts.get(target + '::' + address)
            if receipt:
                assert receipt.get('imageUrl') and receipt.get('sha256') == digest, address
                assert url == receipt['imageUrl'], 'World not rebuilt with current receipt: ' + address
                parsed = urlparse(url)
                assert parsed.scheme == 'https' and parsed.hostname in {'images.aidungeon.com', 'latitude-standard-pull-zone-1.b-cdn.net'}, address
            elif args.complete:
                raise AssertionError('Official upload missing: ' + address)
            results.append({'target': target, 'address': address, 'file': entry['file'], 'sha256': digest, 'imageUrl': url})
    result = {'complete': args.complete, 'worldSHA256': hashlib.sha256(world_path.read_bytes()).hexdigest(), 'portraits': len(portraits), 'locationImages': sum(e['kind'] == 'location' for e in scenes.values()), 'areaImages': sum(e['kind'] == 'area' for e in scenes.values()), 'assignments': results}
    if args.complete:
        (HERE / 'art-verification.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k != 'assignments'}))

if __name__ == '__main__':
    main()
