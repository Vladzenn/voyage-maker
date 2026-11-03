const fish=__FISH__;
__CONTEXT__
const tick=Number(check({type:'game-tick'}))||0;
const baited=__BAITED__,key=baited?'bait':'lure';
if(!storage.fshCasts||typeof storage.fshCasts!=='object')storage.fshCasts={};
const holders=check({type:'player-traits'})||{};
if(storage.fshHook&&!Object.values(holders).some(t=>Array.isArray(t)&&t.includes('Rare Fish on the Line')))delete storage.fshHook;
if(tick<=0||storage.fshCasts[key]===tick){skip=true}else{
 if(weather==='storm'&&habitat==='d'){
  effects.push({type:'story',instruction:'Exposed offshore fishing is unsafe in this squall. Keep the line stowed and show the rough water; offer waiting or a genuinely sheltered fishing ground. No bait is spent and no catch is awarded. Do not move the player or summon a monster.'});
  storage.fshCasts[key]=tick;
 }else{
  const pool=fish.filter(f=>(f[6]==='*'||f[6]===realmCode)&&f[1].includes(habitat)&&(!storage.fshHook||f[2]>2));
  const weights=pool.map(f=>f[2]*(f[6]===realmCode?1.5:1)*(f[3]===weather?2.2:1)*(baited&&(f[2]<=9||/Loach|Bream|Tench|Eel|Goby/.test(f[0]))?1.6:1));
  let roll=Math.random()*weights.reduce((a,b)=>a+b,0),chosen=pool[pool.length-1];
  for(let i=0;i<pool.length;i++){roll-=weights[i];if(roll<0){chosen=pool[i];break}}
  const cm=chosen[4]+Math.floor(Math.random()*(chosen[5]-chosen[4]+1));
  // The same local shoal roll is shared by simultaneous qualifying anglers.
  // Native scope/conditions, not script-side text parsing, select the recipients.
  if(baited)effects.push({type:'item-remove',item:'Angler’s Bait Portion',quantity:1,target:'satisfyingPlayers'});
  if(chosen[2]===2){
   storage.fshHook={fish:chosen[0],cm,area,location,realm,until:tick+6};
   effects.push({type:'player-traits',operator:'add',value:'Rare Fish on the Line',target:'satisfyingPlayers'});
   effects.push({type:'story',instruction:'A rare '+chosen[0]+' is hooked, not landed or acquired. Describe its distinctive movement and let the angler choose a response: ease the line and tire it, guide it away from cover, take a risk, or release it. One actual next handling attempt can settle the catch using Fishing. No mandatory wording, extra fight, automatic damaged tackle or inventory fish yet. Waiting for up to six turns is possible; leaving this fishing ground loses the line’s catch.'});
  }else{
   effects.push({type:'item-add',item:chosen[0],quantity:1,target:'satisfyingPlayers'});
   effects.push({type:'story',instruction:'The qualifying angler lands one '+chosen[0]+', about '+cm+' cm, in '+(weather==='neutral'?'the actual local':weather)+' conditions. The inventory grant is already handled; do not duplicate it, invent another catch or add separate XP/resource rewards. A mixed action result can mean an awkward landing. Keep this a short fishing moment unless the player engages further.'});
   if(!storage.fshRecords||typeof storage.fshRecords!=='object')storage.fshRecords={};
   const old=storage.fshRecords[chosen[0]]||{best:0,landings:0};
   storage.fshRecords[chosen[0]]={best:Math.max(old.best,cm),landings:old.landings+1};
  }
  storage.fshCasts[key]=tick;
 }
}
