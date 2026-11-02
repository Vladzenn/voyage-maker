// One existing dispatcher offers native quests. No new acceptance/completion controllers.
const jobs=JOBS;
const n=Number(check({type:'game-tick'}))||0;
let rank=0;
for(const [i,b]of ['Bronze','Silver','Gold','Platinum'].entries())if(Object.values(check({type:'player-item',item:'Guild Badge: '+b})||{}).some(v=>v>0))rank=Math.max(rank,i+1);
if(!rank){effects.push({type:'story',instruction:'Explain the actual licensure route and Bronze starting badge if the applicant asks about taking work. No badge, payment, key or examination pass is given merely for browsing.'});}
else{
 const levels=Object.values(check({type:'player-level'})||{}).filter(v=>typeof v==='number'&&Number.isFinite(v));
 const level=levels.length?Math.min(...levels):1;
 const text=String((check({type:'action-text'})||[]).join(' ')).toLocaleLowerCase();
 const qualified=jobs.filter(j=>{const s=check({type:'quest-status',questId:j.title});return rank>=j.rank&&(['hidden','planned','available','expired','abandoned','rejected'].includes(s)||(j.repeatable&&s==='completed'&&n-Number(storage['q20_'+j.slug+'_paid_tick']??n)>=20));});
 const named=qualified.find(j=>text.includes(j.title.toLocaleLowerCase())||text.includes(j.title.replace(/^Guild: /,'').toLocaleLowerCase()));
 const pool=qualified.filter(j=>j.recommendedLevel<=level+(level<10?2:5)&&(!j.band||j.band<=level));
 const band=level>=15?15:level>=7?7:1;
 const cursor=Math.max(0,Number(storage.q20_board_cursor)||0);
 const picked=named?[named]:[];
 if(!named){
  for(const lane of ['combat','other']){
   const candidates=pool.filter(j=>(j.lane||'other')===lane);
   const current=candidates.filter(j=>(j.band||1)===band);
   const choices=current.length?current:candidates;
   if(choices.length)picked.push(choices[Math.floor(cursor/2)%choices.length]);
  }
 }
 for(let i=0;i<pool.length&&picked.length<2&&!named;i++){const j=pool[(cursor+i)%pool.length];if(!picked.includes(j))picked.push(j);}
 storage.q20_board_cursor=cursor+2;
 for(const j of picked){
  if(j.slug){storage['q20_offered_'+j.slug]=true;storage['q20_offer_tick_'+j.slug]=n;}
  if(check({type:'quest-status',questId:j.title})!=='completed')effects.push({type:'quest-init',operator:'set',value:j.title});
 }
 effects.push({type:'story',instruction:picked.length?'Present only these eligible choices with their real short premises, scope and full posted rewards: '+picked.map(j=>j.title+' (recommended level '+j.recommendedLevel+'+)').join('; ')+'. Offer a real choice and wait. A concluded recurring contract needs fresh terms and actual new work. If a specifically requested job exceeds this party’s experience, explain its actual danger before any acceptance; the request only opens the offer. Browsing does not accept a quest or grant money, credit, companions or portal permission. Stronger contracts do not raise the danger of unrelated streets or novice jobs.':'No fresh authored posting is selected now. Preserve accepted jobs and completed outcomes. If wanted, offer a couple of distinct suitable generated commissions using actual badge, travel permission and the least experienced human’s level; never substitute a high-level fight or reopen a resolved personal crisis.'});
}
