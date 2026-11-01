// Reproduce review claims with the actual emitted world scripts and shared fixture.
const fs=require('fs'),path=require('path'),vm=require('vm'),{createRequire}=require('module');
const root=path.resolve(__dirname,'..'),file=path.join(__dirname,'test_crucible.cjs');
const prelude=fs.readFileSync(file,'utf8').split('// VERSION DISPATCH:')[0];
const ctx={require:createRequire(file),__dirname,process:{...process,argv:process.argv.slice(0,2)},console,structuredClone,module:{exports:{}}};
vm.runInNewContext(prelude+'\nmodule.exports={harness,w};',ctx);
const {harness,w}=ctx.module.exports,results=[];
for(const victim of ['opponent','player']){
 const h=harness();h.enter();h.run('cc1_ready');const m=h.c().card[h.c().index];
 h.s.area='The Eternal Crucible - Competitor Lounge';h.s.tick++;
 if(victim==='opponent')h.s.npcs[m.opponent].hp=0;else h.s.hp.Player=0;
 h.run('cc1_observe');results.push({case:'Incapacity outside arena: '+victim,phase:h.c().phase,outcome:h.c().outcome,result:m.result||null});
}
{
 const h=harness();h.enter();h.s.players.Spectator=20;h.s.hp.Spectator=100;h.run('cc1_observe');
 results.push({case:'A second human joins',phase:h.c().phase,outcome:h.c().outcome,entrant:h.c().entrant});
}
const out={controller:w.triggerDefinitions.cc1_initialize.script.match(/v:(\d+)/)?.[1],scope:'Actual emitted scripts in isolated fixture; semantic answers supplied, not live Voyage.',results};
console.log(JSON.stringify(out,null,2));
if(process.argv.includes('--save')){
 const dir=path.join(root,'research/crucible-audit-2026-11-02');fs.mkdirSync(dir,{recursive:true});
 fs.writeFileSync(path.join(dir,'second-audit-v'+out.controller+'.json'),JSON.stringify(out,null,2)+'\n');
}
