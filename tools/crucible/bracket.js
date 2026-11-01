const fill=()=>{
 for(const m of c.matches){
  if(m.parents&&m.players.length===0){const p=m.parents.map(id=>c.matches.find(x=>x.id===id));if(p.every(x=>x.winner))m.players=p.map(x=>x.winner);}
  if(m.players.length===2&&!m.players.includes('@')&&!m.winner){
   const power=n=>(roster.find(x=>x.name===n)||{level:1}).level;
   const a=power(m.players[0])*(.8+rnd()*.4),b=power(m.players[1])*(.8+rnd()*.4);
   m.winner=m.players[a>=b?0:1];m.loser=m.players[a>=b?1:0];m.reason='recorded NPC bracket result';m.resultTick=tick;
  }
 }
};
const archive=()=>{
 c.closedTick=tick;c.nextTick=tick+100;
 c.history.push({edition:c.edition,title:c.title,winner:c.champion,outcome:c.outcome,closedTick:tick,matches:JSON.parse(JSON.stringify(c.matches))});
 c.history=c.history.slice(-8);storage.gh_lore_tournament_active=false;setPhase('closed');
};
const finish=(winner,reason)=>{
 const m=current();if(!m||m.resultTick!==undefined)return;
 m.winner=winner;m.loser=m.players.find(n=>n!==winner);m.reason=reason;m.resultTick=tick;
 const n=opponent(m),h=health(n);
 if(typeof m.opponentStartHealth==='number'&&m.opponentStartHealth>0&&typeof h==='number'&&h<m.opponentStartHealth){
  effects.push({type:'npc-health',npc:n,operator:'set',value:m.opponentStartHealth});
  say('After the official stop and recorded result, arena medics stabilize '+n+' from the actual nonlethal bout. The native health recovery does not reverse the defeat or permit another attack. The player is separately offered appropriate optional care; do not invent their injuries.');
 }
 c.care[c.edition+':'+m.id+':'+(m.attempt||1)]={owner:c.entrant,edition:c.edition};
 storage.gh_lore_tournament_active=false;
 if(c.exhibition){c.outcome=winner==='@'?'exhibition win':'exhibition loss';setPhase('closed');say('The friendly bout is settled: '+c.outcome+'. This is not a championship and gives no championship trophy or purse. Offer appropriate optional care or rest without inventing injuries.');mirror();return;}
 fill();
 if(winner!=='@'){
  c.outcome=/withdraw|departure/.test(reason)?'withdrawn':'eliminated';for(let j=0;j<4;j++)fill();c.champion=c.matches[c.matches.length-1].winner;archive();
  say('The registered fighter has lost this edition by '+reason+'. Preserve that result despite later healing or celebration. The remaining bracket is settled once; its champion is '+c.champion+'. No more title bouts remain for this entry. Offer optional medical care, rest or ordinary company.');
 }else{
  fill();const next=c.matches.find(x=>x.players.includes('@')&&x.resultTick===undefined);
  if(next){c.match=next.id;setPhase('between');say('The current bout is won and recorded. Offer optional care or rest appropriate to the actual condition; an unharmed fighter needs no invented injury or compulsory treatment. The next opponent is '+opponent(next)+' in '+next.arena+'. Let the player talk, rest or declare readiness; do not start the next fight automatically.');}
  else{c.outcome='champion';c.champion=c.entrant;c.prizes[c.edition]={owner:c.entrant,title:c.title,marks:c.purse};archive();say('The championship final is settled. '+c.entrant+' is the champion of '+c.title+'. Announce the agreed '+c.purse+'-mark purse and championship trophy as available for collection, not already granted. No further final or opponent belongs to this edition. Optional care and ordinary company remain available.');}
 }
 mirror();
};
const withdraw=reason=>{
 if(c.exhibition){const m=current();if(m&&m.resultTick===undefined)finish(opponent(m),reason);else setPhase('closed');return;}
 const m=current();if(m&&m.players.includes('@')&&m.resultTick===undefined){finish(opponent(m),reason);return;}
 c.outcome='withdrawn';for(let j=0;j<4;j++)fill();c.champion=c.matches[c.matches.length-1].winner||'the remaining eligible finalist';archive();mirror();
};

