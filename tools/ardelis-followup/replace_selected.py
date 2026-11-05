"""Install only an explicitly approved replacement, retaining the first selection."""
import argparse, hashlib, pathlib, shutil
import update

def replace(name, source, reason):
    with update.selected_ledger() as ledger:
        _replace(ledger,name,source,reason)
    print('Selected approved replacement: '+name)

def _replace(ledger,name,source,reason):
    previous=ledger[name]
    assert previous.get('generationPasses',1)==1, 'One authorized replacement already selected'
    dest=(update.ROOT/previous['file']).resolve()
    assert dest.is_relative_to((update.ROOT/'world-draft/npc portraits/Ardelis').resolve())
    assert hashlib.sha256(dest.read_bytes()).hexdigest()==previous['sha256']
    src=pathlib.Path(source)
    assert src.is_file() and src.suffix.lower()=='.png'
    backup=update.ROOT/'tmp/ardelis-followup'/(name+' - first selection.png')
    assert not backup.exists()
    shutil.copy2(dest,backup)
    shutil.copy2(src,dest)
    ledger[name]={**previous,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),
      'source':str(src),'generationPasses':2,'authorRequestedReplacement':True,
      'replacementReason':reason,'previousSelection':previous}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('name');p.add_argument('source');p.add_argument('reason')
    a=p.parse_args();replace(a.name,a.source,a.reason)
