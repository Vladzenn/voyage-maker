// Appended to the existing rb_clock; the preceding code supplies tick,
// traits, levels, fighting and location from actual native checks.
const concluded = storage.arReceivingConcluded === true ||
  check({type:'quest-status',questId:'Rebirth: What the Crown Received'}) === 'completed';
storage.rbPursuitClosed = concluded;
storage.rbHuntDue = false;
storage.rbHuntCandidate = null;
if (Number(storage.rbPhase) >= 5 && !concluded) {
  if (!storage.rbHuntByName || typeof storage.rbHuntByName !== 'object') storage.rbHuntByName = {};
  const qualified = Object.keys(traits).filter(name => Array.isArray(traits[name]) &&
    traits[name].includes('Summoned one') && traits[name].includes('Traced Shore Record') &&
    Number(levels[name]) >= 15);
  for (const name of qualified) {
    if (!storage.rbHuntByName[name]) storage.rbHuntByName[name] = {attempts:0,next:tick+100};
  }
  const nextPartyAttempt = Number(storage.rbHuntLastResolvedTick ?? tick) + 100;
  if (storage.rbHuntLastResolvedTick === undefined) storage.rbHuntLastResolvedTick = tick;
  const realm=String(check({type:'party-realm'})||'');
  const protectedPlace=/Academy|Crucible|Portal|Cathedral|Hospice/.test(location) ||
    ["The Grand Sage's Court",'Caelrath Palace','Caelrath Institute of Magic','Shadowspire','Evertree Base'].includes(location);
  if (!storage.rbHuntActive && !fighting && !protectedPlace && tick >= nextPartyAttempt &&
      ['Glowhaven','Ardelis','Drakenspire Mountains','Asterveil Sky Archipelago','Akitsuhara'].includes(realm)) {
    const due = qualified.filter(name => tick >= Number(storage.rbHuntByName[name].next));
    due.sort((a,b)=>Number(levels[a])-Number(levels[b]) || a.localeCompare(b));
    if (due.length) {
      const name=due[0], level=Number(levels[name]);
      const attempt=Number(storage.rbHuntByName[name].attempts||0)+1;
      storage.rbHuntCandidate={name,level,attempt,
        primaryMin:Math.max(1,Math.min(45,level-2)),
        primaryMax:Math.max(1,Math.min(45,level+2)),
        supportLevel:Math.max(1,Math.min(35,Math.floor(level*0.7))),
        count:attempt>=3?2:1};
      storage.rbHuntDue=true;
    }
  }
}
