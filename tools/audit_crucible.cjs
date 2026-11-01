// Diagnostic reproduction of known v1 edge cases. This does not fix them or model live AI.
const fs=require('fs'),path=require('path'),vm=require('vm');
const root=path.resolve(__dirname,'..');
const source=fs.readFileSync(path.join(__dirname,'test_crucible.cjs'),'utf8');
const boundary=source.indexOf('\nfor(const name of manifest.triggers)');
if(boundary<0)throw Error('Harness boundary changed; inspect rather than silently testing different code.');
const header=source.slice(0,boundary),rows=[];
function probe(id,body){
 let result;
 vm.runInNewContext(header+'\n'+body,{require,__dirname,process:{argv:['node','audit']},structuredClone,console:{log:v=>{result=v}}},{timeout:10000});
 rows.push({id,...result});
}
probe('unstarted_opponent_incapacity',`
 const h=harness();h.enter();const m=h.c().matches.find(x=>x.id===h.c().match),op=m.players.find(x=>x!=='@');
 h.s.npcs[op].hp=0;h.run('cc1_ready');const before={phase:h.c().phase,startedTick:m.startedTick??null};
 h.run('cc1_review');console.log({before,after:{phase:h.c().phase,winner:m.winner??null,reason:m.reason??null},reproduced:m.startedTick===undefined&&m.winner==='@'});
`);
probe('double_knockout_review',`
 const h=harness();h.enter();h.run('cc1_ready');const m=h.c().matches.find(x=>x.id===h.c().match),op=m.players.find(x=>x!=='@');
 h.s.tick++;h.s.hp.Player=0;h.s.npcs[op].hp=0;h.run('cc1_observe');h.run('cc1_review');h.run('cc1_review');
 const stopped={phase:h.c().phase,winner:m.winner??null,pendingCare:Object.keys(h.c().care).length};
 h.run('cc1_withdraw');console.log({stopped,explicitWithdrawalPhase:h.c().phase,reproduced:stopped.phase==='review'&&stopped.pendingCare===0});
`);
probe('return_during_grace',`
 const h=harness();h.enter();h.run('cc1_ready');h.s.location='Four Sages Bazaar';h.run('cc1_observe');const phases=[h.c().phase];
 h.s.tick++;h.s.location='The Eternal Crucible';h.run('cc1_observe');phases.push(h.c().phase);
 h.s.tick++;h.run('cc1_observe');phases.push(h.c().phase);console.log({phases,outcome:h.c().outcome,reproduced:phases.join(',')==='away,away,closed'});
`);
probe('incapacitated_player_starts',`
 const h=harness();h.enter();h.s.hp.Player=0;h.run('cc1_ready');const m=h.c().matches.find(x=>x.id===h.c().match);
 console.log({phase:h.c().phase,recordedStartingHealth:m.startHealth,reproduced:h.c().phase==='live'&&m.startHealth===0});
`);
probe('unfit_offscreen_champion',`
 const h=harness();h.enter();h.run('cc1_ready');const m=h.c().matches.find(x=>x.id===h.c().match),op=m.players.find(x=>x!=='@');
 for(const n of h.c().roster)if(n!=='@'&&n!==op)h.s.npcs[n].hp=0;
 h.run('cc1_result_loss');const champion=h.c().champion;
 const invalidWins=h.c().matches.filter(x=>x.winner&&x.winner!=='@'&&h.s.npcs[x.winner]?.hp<=0).map(x=>({match:x.id,winner:x.winner}));
 console.log({champion,championHealth:h.s.npcs[champion]?.hp,invalidWins,reproduced:invalidWins.length>0});
`);
probe('benches_before_call',`
 const h=harness();h.enter();const match=h.c().match;h.s.action=['I leave to the benches to watch until my turn.'];
 h.s.area='The Eternal Crucible - Grand Stands';h.s.tick++;h.run('cc1_observe');h.run('cc1_withdraw',false);h.run('cc1_ready',false);
 console.log({phase:h.c().phase,sameMatch:h.c().match===match,location:h.s.location,area:h.s.area,nativeMovementPreservesEntry:h.c().phase==='ready',semanticScope:'Withdrawal/readiness answers supplied false; this does not test the model understanding leave.'});
`);
probe('benches_between_bouts',`
 const h=harness();h.enter();h.win();const match=h.c().match;h.s.area='The Eternal Crucible - Grand Stands';h.s.tick++;h.run('cc1_observe');
 console.log({phase:h.c().phase,sameMatch:h.c().match===match,nativeMovementPreservesEntry:h.c().phase==='between'});
`);
probe('benches_during_live_bout',`
 const h=harness();h.enter();h.run('cc1_ready');h.s.area='The Eternal Crucible - Grand Stands';h.s.tick++;h.run('cc1_observe');
 console.log({phase:h.c().phase,scope:'Current mechanical observer watches venue exit, not ring boundaries; a referee/ring-out ruling remains semantic.'});
`);
const result={worldSHA256:require('crypto').createHash('sha256').update(fs.readFileSync(path.join(root,'world-draft/WorldAlpha - World.json'))).digest('hex'),scope:'Diagnostic executions of emitted scripts using the existing harness and supplied semantic answers; not live Voyage or proof of language recognition.',rows};
if(process.argv[2])fs.writeFileSync(path.resolve(process.argv[2]),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify(result,null,2));
