"""Nerathyl's two native named portraits, switched only by actual scene changes."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parent

def apply(w):
    receipt=HERE/'hosted-serpent-state.json'
    if not receipt.exists():return {'ready':False}
    r=json.loads(receipt.read_text(encoding='utf-8'))
    assert r['name']=='Nerathyl' and r['state']=='Awake' and r['target']=='NPC_PORTRAIT'
    assert hashlib.sha256((ROOT/r['file']).read_bytes()).hexdigest()==r['sha256']
    n=w['npcs']['Nerathyl']
    assert n['portraitUrl'].startswith('https://') and r['url'].startswith('https://')
    n['portraits']={'Asleep':n['portraitUrl'],'Awake':r['url']}
    common=[{'type':'party-location','operator':'equals','value':'Bluecoil Rest'},
            {'type':'npc-in-scene','npc':'Nerathyl','operator':'equals','value':True},
            {'type':'npc-health','npc':'Nerathyl','operator':'greaterThan','value':0}]
    for awake,query in [(True,'In the latest actual scene at Bluecoil Rest, Nerathyl has genuinely woken or is already awake: its eyes open and it raises or actively moves its head, warns, feeds or fights. A plan to wake it, a hypothetical warning, a dream, distant observation or a description of its usual habits does not qualify.'),
                        (False,'In the latest actual scene at Bluecoil Rest, the living Nerathyl has genuinely settled back into sleep, eyes closed and head resting. Merely calming it, leaving, arriving again, remembering its earlier sleep, knocking it unconscious or killing it does not qualify.')]:
        key='ghx_serpent_wakes' if awake else 'ghx_serpent_sleeps'
        w['triggerDefinitions'][key]={'name':key,'recurring':True,'phase':'state',
          'conditions':common+[{'type':'read-boolean','key':'ghxSerpentAwake','operator':'equals','value':not awake},{'type':'story','query':query}],
          'effects':[{'type':'npc-portrait','npc':'Nerathyl','operator':'set','value':'Awake' if awake else 'Asleep'},
                     {'type':'write-boolean','key':'ghxSerpentAwake','operator':'set','value':awake}]}
    return {'ready':True,'npc':'Nerathyl','initial':'Asleep','variants':list(n['portraits']),'triggers':['ghx_serpent_wakes','ghx_serpent_sleeps']}
