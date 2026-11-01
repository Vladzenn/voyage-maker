const loc=check({type:'party-location'}),area=check({type:'party-area'}),tick=check({type:'game-tick'}),heart='Sepulchral Conservatory - Grafting Heart',outside='Sepulchral Conservatory - Ossuary Greenhouse';
const open=storage.cc1_grove_root===true&&storage.cc1_grove_mourning===true;
const raw=[].concat(check({type:'action-text'})||[]).filter(x=>typeof x==='string').join(' ').toLowerCase();
const directed=/^(?:(?:i|we)\s+)?(?:attempt to\s+)?(?:go|head|walk|move|enter|travel|descend|jump|teleport|find|approach|proceed|cross)\b/.test(raw);
const requested=typeof statePass==='undefined'&&directed&&/grafting heart|threnvoss|boss (?:room|chamber)/.test(raw);
if(area&&area!==heart)storage.cc1GroveSafe={location:loc,area};
if(!open&&(area===heart||requested)){
 const saved=storage.cc1GroveSafe,valid=saved&&['Sepulchral Portal House','Sepulchral Conservatory','Mourning Garden'].includes(saved.location)&&typeof saved.area==='string'&&saved.area.startsWith(saved.location+' - ')&&saved.area!==heart;
 const retained=valid?saved.area:outside,retainedLocation=valid?saved.location:'Sepulchral Conservatory';
 storage.cc1GroveBlockedTick=tick;
 effects.push({type:'party-location',operator:'set',value:retainedLocation},{type:'party-area',operator:'set',value:retained},{type:'npc-placement',npc:'allPartyNPCs',operation:'moveTo',location:retainedLocation,area:retained},{type:'story',instruction:'The inner lattice is still closed: both tending circuits must actually be settled. The party remains at '+retained+'. A requested jump did not reach Threnvoss. Describe the real obstacle and connected routes; no boss introduction, offscreen progress, attack or loot follows from this rejected move. Backtracking remains possible.'});
}else if(open&&area===heart&&!storage.cc1_grove_heart_seen){storage.cc1_grove_heart_seen=true;effects.push({type:'known-entity',entity:'Threnvoss',operator:'set',value:true},{type:'story',instruction:'Threnvoss confronts the actual party in the Grafting Heart. Show finite Grafted Sentinel support only after real generated actors exist, plus the chest knot, roots, cover and retreat route. Combat or an actually achieved release can resolve this encounter; arrival is not victory and grants no free hit.'});}
