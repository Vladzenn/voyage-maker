const c=storage.rbHuntCandidate;
const traits=check({type:'player-traits'})||{},levels=check({type:'player-level'})||{};
const tick=Number(check({type:'game-tick'}))||0;
const terminal=storage.arReceivingConcluded===true ||
 check({type:'quest-status',questId:'Rebirth: What the Crown Received'})==='completed';
if(terminal || storage.rbHuntActive || !c ||
 !Array.isArray(traits[c.name]) || !traits[c.name].includes('Summoned one') ||
 !traits[c.name].includes('Traced Shore Record') || Number(levels[c.name])<15 ||
 tick<Number(storage.rbHuntByName?.[c.name]?.next) ||
 tick<Number(storage.rbHuntLastResolvedTick||0)+100){skip=true;}
else {
 const level=Number(levels[c.name]),attempt=Number(storage.rbHuntByName[c.name].attempts||0)+1;
 const lo=Math.max(1,Math.min(45,level-2)),hi=Math.max(1,Math.min(45,level+2));
 const helper=Math.max(1,Math.min(35,Math.floor(level*0.7)));
 const tactic=attempt===1?'One trace construct tests the mana trail and makes a cautious capture approach.':
 attempt===2?'One retrieval proxy uses a finite ward-net or a prepared distraction, with visible tells and an escape route.':
 'One retrieval proxy and one weaker trace construct attempt a coordinated cutoff. Desperation shows in riskier orders and imperfect preparation, not an endless army.';
 storage.rbHuntActive=true;
 storage.rbHuntCase={target:c.name,attempt,start:tick,location:String(check({type:'party-location'})||'')};
 storage.rbHuntByName[c.name].attempts=attempt;
 storage.rbHuntDue=false;
 effects.push({type:'story',instruction:
 'An occasional Ardelian retrieval attempt follows the actual mana trace of '+c.name+'. '+tactic+
 ' Use newly generated Ardelian Trace Construct / Ardelian Retrieval Proxy instances; never resurrect the two named cloaked couriers or alter an established NPC level.'+
 ' Primary opponent native level '+lo+'-'+hi+', average tier, healthMultiplier at most 1, successBonus at most 0 and damageModifier at most 0.'+
 (attempt>=3?' At most one support opponent, level '+helper+', weak tier and healthMultiplier at most 0.7.':' Exactly one opposing individual, not a concealed pack.')+
 ' These are finite capture tools. Give a readable warning, actual contested actions and room to fight, hide, deceive, negotiate or escape.'+
 ' Agents reached this place by a real usable route and a recent trace; no GPS knowledge, private-thought reading, automatic capture, instant counterspell, whole-city attack or surprise second wave.'+
 ' Companions may act but never raise this target-based level band. Create actual combatants when the encounter becomes a fight; scene setup awards no damage, victory, loot or XP.'+
 ' A discarded outer cloak does not become a unique named character. Proxies hold only the information actually supplied to them; a local sample is not a report channel to their employer.'});
}
