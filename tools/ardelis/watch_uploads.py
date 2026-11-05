"""Upload each newly saved location batch once; credential stays in process env."""
import argparse
import json
import sys
import time
from pathlib import Path

import upload_art

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--expected', type=int, default=86)
    ap.add_argument('--poll-seconds', type=float, default=20)
    args = ap.parse_args()
    ledgerpath = Path(__file__).resolve().parent / 'location-files.json'
    previous = None
    while True:
        try:
            ledger = json.loads(ledgerpath.read_text(encoding='utf-8'))
        except (FileNotFoundError, json.JSONDecodeError):
            time.sleep(args.poll_seconds)
            continue
        signature = tuple(sorted((k, v['sha256']) for k, v in ledger.items()))
        if signature != previous:
            original_args = sys.argv
            sys.argv = ['upload_art.py', 'locations']
            try:
                upload_art.main()
            except SystemExit as exc:
                if exc.code not in (None, 0, 1):
                    raise
            finally:
                sys.argv = original_args
            previous = signature
        if len(ledger) >= args.expected:
            receipts = json.loads((ledgerpath.parent / 'upload-receipts.json').read_text(encoding='utf-8'))
            missing = []
            for entry in ledger.values():
                address = entry['name'] if entry['kind'] == 'location' else entry['location'] + '::' + entry['area']
                row = receipts.get(entry['target'] + '::' + address, {})
                if row.get('sha256') != entry['sha256'] or not row.get('imageUrl'):
                    missing.append(address)
            print(json.dumps({'watchComplete': True, 'scenes': len(ledger), 'missingUploads': missing}, ensure_ascii=False), flush=True)
            return 1 if missing else 0
        time.sleep(args.poll_seconds)

if __name__ == '__main__':
    raise SystemExit(main())
