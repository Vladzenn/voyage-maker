const node=id=>(c.rounds||[]).flat().find(x=>x.id===id);
const fit=n=>n&&n!=='@'&&check({type:'npc-location',npc:n})===venue&&check({type:'npc-in-party',npc:n})!==true&&!(typeof health(n)==='number'&&health(n)<=0)&&(!check({type:'npc-in-combat',npc:n})||(current()?.opponent===n&&current()?.result?.winner==='opponent'));
const settleNPC=()=>{
 for(const round of c.rounds||[])for(const m of round){
  if(m.done)continue;
  if(m.parents){const a=node(m.parents[0]),b=node(m.parents[1]);if(!a.done||!b.done)continue;m.players=[a.winner,b.winner];}
  if(m.players.includes('@'))continue;
  const ok=m.players.filter(fit);let winner=null,reason='both unavailable';
  if(ok.length===1){winner=ok[0];reason='administrative advance; other slot unavailable';}
  if(ok.length===2){const lv=n=>roster.find(x=>x.name===n)?.level||1;winner=rnd()<lv(ok[0])/(lv(ok[0])+lv(ok[1]))?ok[0]:ok[1];reason='official NPC bout result';}
  m.done=true;m.winner=winner;m.reason=reason;m.resolvedTick=tick;
 }
};
const schedule=()=>{
 settleNPC();const m=(c.rounds||[]).flat().find(x=>!x.done&&x.players?.includes('@'));
 if(!m)return false;
 const opponent=m.players.find(x=>x!=='@');if(!opponent)return false;
 const round=c.rounds.findIndex(x=>x.includes(m)),label=round===c.rounds.length-1?'Final':round===c.rounds.length-2?'Semifinal':'Opening bout';
 c.card.push({id:m.id,node:m.id,opponent,level:roster.find(x=>x.name===opponent)?.level,arena:rings[(round+c.edition)%rings.length],label});c.index=c.card.length-1;return true;
};
const recordNode=(winner,reason)=>{const m=current(),n=node(m?.node);if(!n||n.done)return;n.done=true;n.winner=winner==='player'?'@':winner==='opponent'?m.opponent:null;n.reason=reason;n.resolvedTick=tick;};
const finishField=()=>{settleNPC();const last=c.rounds?.at(-1)?.[0];c.champion=last?.done?(last.winner==='@'?c.entrant:last.winner):null;};
