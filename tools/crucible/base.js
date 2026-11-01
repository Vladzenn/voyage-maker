const tick=check({type:'game-tick'}), venue='The Eternal Crucible';
const levels=check({type:'player-level'})||{}, names=Object.keys(levels), solo=names.length===1;
const c=storage.cc1=storage.cc1||{v:1,phase:'idle',edition:0,nextTick:0,history:[],prizes:{},care:{}};
const here=check({type:'party-location'})===venue;
const say=s=>effects.push({type:'story',instruction:s});
const setPhase=p=>{c.phase=p;storage.cc1_phase=p;storage.cc1_live=p==='live';storage.cc1_active=['ready','live','between','review','away'].includes(p);};
const roster=ROSTER, rings=RINGS;
const rnd=()=>{c.seed=((c.seed||1931)*1664525+1013904223)>>>0;return c.seed/4294967296;};
const health=n=>check({type:'npc-health',npc:n});
const playerHealth=()=>{const h=check({type:'player-resource',resource:'Health'})||{};return h[c.entrant]===undefined&&solo?h[names[0]]:h[c.entrant];};
const current=()=>c.matches&&c.matches.find(m=>m.id===c.match);
const opponent=m=>m&&m.players.find(n=>n!=='@');
const mirror=()=>{storage.cc1_phase=c.phase;storage.cc1_live=c.phase==='live';storage.cc1_active=['ready','live','between','review','away'].includes(c.phase);storage.cc1_due=Object.keys(c.prizes).length>0;storage.cc1_care=Object.keys(c.care).length>0;};

