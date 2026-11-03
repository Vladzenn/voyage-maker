"""Reproduce final fishing values from the exact supplied Studio merge base."""
import copy
import json
from pathlib import Path
import subprocess
import unittest
import build
import universal

ROOT=Path(__file__).resolve().parents[2]

class RebuildTest(unittest.TestCase):
    def test_exact_values_and_idempotent_follow_up(self):
        manifest=json.loads((build.HERE/'manifest.json').read_text(encoding='utf-8'))
        source=json.loads(subprocess.check_output(
            ['git','show',manifest['baseCommit']+':world-draft/WorldAlpha - World.json'],
            cwd=ROOT,encoding='utf-8'))
        merge=json.loads((build.HERE/'studio-merge.json').read_text(encoding='utf-8'))
        for row in merge['changes']:
            owner=source
            for key in row['path'][:-1]:owner=owner[key]
            key=row['path'][-1]
            if row['kind']=='removed':del owner[key]
            else:owner[key]=copy.deepcopy(row['after'])
        meta=build.apply(source)
        current=json.loads(build.WORLD.read_text(encoding='utf-8'))
        self.assertEqual(source,current,'The checked-in generator must reproduce current world values')
        self.assertEqual(len(meta['species']),51)
        universal.apply(source)
        self.assertEqual(source,current,'Reapplying the follow-up must be idempotent')

if __name__=='__main__':unittest.main()
