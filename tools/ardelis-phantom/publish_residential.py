"""Checked project publish scoped to the home correction and one approved PNG."""
import hashlib
import pathlib
import subprocess
import sys

ROOT=pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'tools'))
import project


def main():
    art=project.load(ROOT/'tools/ardelis-phantom/crownwater-art.json')
    exact=['docs/CURRENT_STATE.md','docs/DECISIONS.md','docs/asset-index.json','tools/test_ardelis_phantom.cjs']
    selected=exact+['tools/ardelis-phantom']+[p.relative_to(ROOT).as_posix() for p in (ROOT/'world-draft').glob('WorldAlpha - *.json')]
    staged=set(subprocess.check_output(['git','diff','--cached','--name-only','-z'],cwd=ROOT).decode('utf-8').split('\0'))-{''}
    assert all(p in selected or p==art['file'] or p.startswith('tools/ardelis-phantom/') for p in staged),'Unrelated staged work needs review'
    original=project.git
    def scoped(*args,**kwargs):
        if args==('add','--all'):return original('add','--',*selected,**kwargs)
        return original(*args,**kwargs)
    def asset():
        index=project.load(project.INDEX); p=ROOT/art['file']; stat=p.stat()
        assert hashlib.sha256(p.read_bytes()).hexdigest()==art['sha256'] and stat.st_size<95*1024*1024
        index['assets'][art['file']]=dict(size=stat.st_size,sha256=art['sha256'],mtimeNs=stat.st_mtime_ns)
        return [art['file']],index
    project.git=scoped;project.asset_changes=asset
    sys.argv=['tools/project.py','publish','-m','Correct Crownwater Row setting and add approved location art']
    return project.main()


if __name__=='__main__':raise SystemExit(main())
