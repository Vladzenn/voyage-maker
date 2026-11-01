if(active()){
 if(!solo||c.entrant!==names[0]){close('cancelled','human roster changed');say('The individual entry is cancelled because its human-player roster or identity changed. Preserve the actual entrant and previously earned uncollected prizes; do not transfer their entry or title to somebody else.');}
 else if(here&&c.phase==='live'){
  const m=current(),p=playerHealth(),h=m?health(m.opponent):undefined;
  if(!m||typeof m.startedTick!=='number'){close('cancelled','missing actual start');say('An inconsistent unstarted bout is closed without a victory or trophy.');}
  else if(!m.result&&tick>m.startedTick){const pd=typeof p==='number'&&p<=0,nd=typeof h==='number'&&h<=0;if(pd&&nd)finish('draw','simultaneous knockout');else if(pd)finish('opponent','actual player incapacity');else if(nd)finish('player','actual opponent incapacity');}
 }
}
mirror();
