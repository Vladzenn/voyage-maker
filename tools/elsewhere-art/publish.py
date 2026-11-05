"""Normal checked project publish, scoped to manual Elsewhere artwork and notes."""
import hashlib,json,pathlib,subprocess,sys
ROOT=pathlib.Path(__file__).resolve().parents[2];HERE=pathlib.Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'tools'));import project


def main():
    brief=project.load(HERE/'brief.json');ledger=project.load(HERE/'manifest.json')
    assert len(ledger)==12 and hashlib.sha256(project.WORLD.read_bytes()).hexdigest()==brief['canonicalSHA256']
    assert project.load(HERE/'verification.json')['manualUploadOnly']
    selected=[r['file'] for r in ledger.values()]
    paths=['README.md','docs/CURRENT_STATE.md','docs/DECISIONS.md','docs/asset-index.json','tools/elsewhere-art','world-draft/Rebirth - Complete Update Patch Notes.md']
    original_git=project.git
    def git_paths(*args):return set(subprocess.check_output(['git',*args,'-z'],cwd=ROOT).decode('utf-8').split('\0'))-{''}
    assert all(p in paths or p in selected or p.startswith('tools/elsewhere-art/') for p in git_paths('diff','--cached','--name-only')),'Unrelated staged work needs review'
    def scoped_git(*args,**kwargs):
        if args==('add','--all'):return original_git('add','--',*paths,**kwargs)
        return original_git(*args,**kwargs)
    def scoped_assets():
        index=project.load(project.INDEX);tracked=git_paths('ls-files');changed=[]
        for r in ledger.values():
            file=ROOT/r['file'];stat=file.stat();digest=hashlib.sha256(file.read_bytes()).hexdigest();assert digest==r['sha256'] and stat.st_size<95*1024*1024
            old=index['assets'].get(r['file'])
            if not old or old['sha256']!=digest or r['file'] not in tracked:
                changed.append(r['file']);index['assets'][r['file']]=dict(size=stat.st_size,sha256=digest,mtimeNs=stat.st_mtime_ns)
        return changed,index
    project.git=scoped_git;project.asset_changes=scoped_assets
    sys.argv=['tools/project.py','publish','-m','Add Elsewhere manual artwork and complete Rebirth patch notes']
    return project.main()


if __name__=='__main__':raise SystemExit(main())
