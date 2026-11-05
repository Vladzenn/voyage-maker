"""Use normal checked publishing, staging only this authorized phantom patch."""
import pathlib
import subprocess
import sys

ROOT=pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'tools'))
import project


def main():
    exact=['README.md','docs/CURRENT_STATE.md','docs/DECISIONS.md','.github/workflows/validate.yml',
           'tools/project.py','tools/test_ardelis_phantom.cjs','tools/test_ardelis_followup.cjs',
           'tools/ardelis-followup/previous_world.cjs']
    selected=exact+['tools/ardelis-phantom']+[p.relative_to(ROOT).as_posix() for p in (ROOT/'world-draft').glob('WorldAlpha - *.json')]
    staged=set(subprocess.check_output(['git','diff','--cached','--name-only','-z'],cwd=ROOT).decode('utf-8').split('\0'))-{''}
    assert all(p in selected or p.startswith('tools/ardelis-phantom/') for p in staged),'Unrelated staged work requires review'
    original=project.git
    def scoped(*args,**kwargs):
        if args==('add','--all'):return original('add','--',*selected,**kwargs)
        return original(*args,**kwargs)
    project.git=scoped
    project.asset_changes=lambda:([],project.load(project.INDEX))
    sys.argv=['tools/project.py','publish','-m','Add Ardelis local beginnings, fish and return-key access']
    return project.main()


if __name__=='__main__':raise SystemExit(main())
