"""Run the normal checked publisher, staging only this task's records and selections."""
import hashlib
import subprocess
import sys
from pathlib import Path
import update
project=update.project
ROOT=update.ROOT


def main():
    proof=update.load(update.HERE/'art-verification.json')
    validation=update.load(update.HERE/'official-validation.json')
    assert proof['complete'] and hashlib.sha256(project.WORLD.read_bytes()).hexdigest()==proof['worldSHA256']
    assert validation['worldSHA256']==proof['worldSHA256']
    data=validation['result']['data'];assert data['valid'] and not data['errors'] and not data['warnings']
    selected=[r['file'] for r in proof['assignments']]
    assert len(selected)==len(set(selected))==202
    old=[]
    for label in ['portrait-files.json','location-files.json']:
        old += [e['file'] for e in update.load(ROOT/'tools/ardelis'/label).values() if not (ROOT/e['file']).exists()]
    assert len(old)==23,'Only the twenty approved character and three house file renames are removed'
    paths=['.github/workflows/validate.yml','README.md','docs/CURRENT_STATE.md','docs/DECISIONS.md','docs/asset-index.json',
      'tools/project.py','tools/ardelis/previous_world.cjs','tools/test_ardelis.cjs','tools/test_ardelis_followup.cjs',
      'tools/ardelis-followup','research/Gemini Audit Review - 2026-11-05.md',
      'world-draft/Ardelis - Development Notes.md','world-draft/Ardelis - Patch Notes.md','world-draft/Ardelis - Map and Landmark Handoff.md']
    paths += [p.relative_to(ROOT).as_posix() for p in (ROOT/'world-draft').glob('WorldAlpha - *.json')]
    original_git=project.git
    def git_paths(*args):
        return set(subprocess.check_output(['git',*args,'-z'],cwd=ROOT).decode('utf-8').split('\0'))-{''}
    staged=git_paths('diff','--cached','--name-only')
    assert all(p in paths or p in selected or p in old or p.startswith('tools/ardelis-followup/') for p in staged),'Unrelated staged work needs review'
    def scoped_git(*args,**kwargs):
        if args==('add','--all'):
            result=original_git('add','--',*paths,**kwargs)
            pending=[p for p in old if p in git_paths('ls-files')]
            if pending:return original_git('add','--update','--',*pending,**kwargs)
            return result
        return original_git(*args,**kwargs)
    def scoped_assets():
        index=project.load(project.INDEX);changed=[]
        tracked=git_paths('ls-files')
        for path in old:index['assets'].pop(path,None)
        for row in proof['assignments']:
            file=ROOT/row['file'];stat=file.stat();digest=hashlib.sha256(file.read_bytes()).hexdigest()
            assert digest==row['sha256'] and stat.st_size<95*1024*1024
            previous=index['assets'].get(row['file'])
            if not previous or previous['sha256']!=digest or row['file'] not in tracked:
                changed.append(row['file']);index['assets'][row['file']]=dict(size=stat.st_size,sha256=digest,mtimeNs=stat.st_mtime_ns)
        return changed,index
    project.git=scoped_git;project.asset_changes=scoped_assets
    sys.argv=['tools/project.py','publish','-m','Complete Ardelis portraits, shared heritage and paced Rebirth pursuit']
    return project.main()


if __name__=='__main__':raise SystemExit(main())
