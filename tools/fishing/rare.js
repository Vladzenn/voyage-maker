const tick=Number(check({type:'game-tick'}))||0,area=String(check({type:'party-area'})||'');
const h=storage.fshHook;
const valid=check({type:'party-realm'})==='Glowhaven'&&h&&__RARE__.includes(h.fish)&&Number.isFinite(h.cm)&&h.area===area&&tick<=h.until;
const mode=__MODE__;
if(!storage.fshRareActions||typeof storage.fshRareActions!=='object')storage.fshRareActions={};
if(mode!=='cleanup'&&storage.fshRareActions[mode]===tick){skip=true}else if(mode==='cleanup'){
 if(valid)skip=true;
 else{
  effects.push({type:'player-traits',operator:'remove',value:'Rare Fish on the Line',target:'satisfyingPlayers'});
  effects.push({type:'story',instruction:'The unattended fishing line has gone slack; its unlanded catch escaped. Clear that fishing moment quietly without a fine, broken equipment, lost unrelated items or monster encounter.'});
  delete storage.fshHook;
 }
}else if(!valid){skip=true}else if(mode==='release'||mode==='miss'){
 effects.push({type:'player-traits',operator:'remove',value:'Rare Fish on the Line',target:'satisfyingPlayers'});
 effects.push({type:'story',instruction:mode==='release'?'The angler deliberately lets the hooked fish go. Give a brief fitting release; no fish enters inventory and no unrelated property is lost.':'The actual handling attempt failed to land the fish; it slips free. Give the concrete local result without an extra attack, invented injury or automatic broken rod. No fish enters inventory.'});
}else{
 effects.push({type:'item-add',item:h.fish,quantity:1,target:'satisfyingPlayers'});
 effects.push({type:'player-traits',operator:'remove',value:'Rare Fish on the Line',target:'satisfyingPlayers'});
 effects.push({type:'story',instruction:'The angler’s successful handling lands one '+h.fish+', about '+h.cm+' cm. Its inventory grant is already applied. Give the chosen approach a satisfying short payoff; do not add a second fish or another reward. The angler can keep it, make an actual handover, or release the real held specimen through ordinary item handling.'});
 if(!storage.fshRecords||typeof storage.fshRecords!=='object')storage.fshRecords={};
 const old=storage.fshRecords[h.fish]||{best:0,landings:0};
 storage.fshRecords[h.fish]={best:Math.max(old.best,h.cm),landings:old.landings+1};
}
if(!skip&&mode!=='cleanup')storage.fshRareActions[mode]=tick;
// Retain the shared species record for other simultaneous hooked anglers until
// their traits clear. This sweep runs on the following planning tick.
