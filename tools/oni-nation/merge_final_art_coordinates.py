"""Apply only the author's three later spirit-map coordinate edits."""
import hashlib,json,pathlib
from build import ROOT,HERE,dump
from prepare_location_art import OLD,NEW,rename
def main():
    source=pathlib.Path(r'C:/Users/VladCodes/.codex/attachments/f940372c-656b-461b-9bd6-1625c8088cd4/Pasted text.txt')
    previous=pathlib.Path(r'C:/Users/VladCodes/.codex/attachments/23da8cc9-d365-41ab-8dde-4aacbe87a199/Pasted text.txt')
    a=json.loads(source.read_text(encoding='utf-8-sig'));b=json.loads(previous.read_text(encoding='utf-8-sig'))
    assert set(a)==set(b)
    path=ROOT/'world-draft/WorldAlpha - World.json';w=json.loads(path.read_text(encoding='utf-8'));changes=[]
    for name,loc in a.items():
        fields=[k for k in set(loc)|set(b[name]) if loc.get(k)!=b[name].get(k)]
        if not fields:continue
        assert set(fields)<=set(['x','y']),(name,fields)
        key=rename(name);changes.append({'name':key,'before':{k:b[name][k] for k in fields},'after':{k:loc[k] for k in fields}})
        for k in fields:
            assert w['locations'][key][k] in [b[name][k],loc[k]]
            w['locations'][key][k]=loc[k]
    assert len(changes)==3
    for name,loc in a.items():
        actual=w['locations'][rename(name)]
        assert all(actual[k]==loc[k] for k in ['x','y','region'])
        assert actual.get('images')==loc.get('images')
    dump(path,w)
    proof={'source':str(source),'sourceSHA256':hashlib.sha256(source.read_bytes()).hexdigest(),'previousSource':str(previous),'coordinateChanges':changes,'sourcePins':{rename(n):{k:loc[k] for k in ['x','y','region']} for n,loc in a.items()},'all285SourceImagesPreserved':True,'shrineRenamePreserved':NEW in w['locations']}
    dump(HERE/'location-art/latest-placement.json',proof)
    from regression_delta import record
    record(w)
    print(json.dumps({'latestCoordinateEdits':len(changes),'allPinsVerified':len(a),'shrineName':NEW}))
if __name__=='__main__':main()
