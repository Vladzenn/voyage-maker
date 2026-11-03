// One persistent regional forecast. No wall clock, calendar rewrite or combat effects.
const tick=Number(check({type:'game-tick'}))||0;
const traits=check({type:'player-traits'})||{};
if(storage.fshHook&&!Object.values(traits).some(t=>Array.isArray(t)&&t.includes('Rare Fish on the Line')))delete storage.fshHook;
if(!storage.fshWeather||typeof storage.fshWeather!=='object')storage.fshWeather={};
const states=['clear','overcast','rain','fog','wind','storm'];
const transitions={clear:[45,30,5,8,11,1],overcast:[20,30,25,10,13,2],rain:[8,43,28,12,7,2],fog:[18,48,12,15,6,1],wind:[22,32,10,2,30,4],storm:[0,25,35,0,40,0]};
function pick(weights){let n=Math.random()*weights.reduce((a,b)=>a+b,0);for(let i=0;i<weights.length;i++){n-=weights[i];if(n<0)return states[i]}return 'overcast'}
let changed=false;
for(const zone of ['inland','coast']){
 let f=storage.fshWeather[zone];
 if(!f||!states.includes(f.kind)||!Number.isFinite(f.until))f={kind:zone==='coast'?'overcast':'clear',until:tick+12+Math.floor(Math.random()*13)};
 else if(tick>=f.until){f={kind:pick(transitions[f.kind]),until:tick+12+Math.floor(Math.random()*13)};changed=true}
 storage.fshWeather[zone]=f;
}
const region=String(check({type:'party-region'})||'');
const zone=/Harbor|Coast|Isles|Shoals|Reach|Bluffs|Marshes/.test(region)?'coast':'inland';
const f=storage.fshWeather[zone],place=String(check({type:'party-location'})||'');
const context=zone+':'+f.kind+':'+place;
if(tick>0&&(changed||storage.fshWeatherContext!==context)){
 const detail={clear:'clear skies and ordinary visibility',overcast:'cloud cover and soft light',rain:'steady ordinary rain and wet exposed surfaces',fog:'patches of mist and reduced outdoor visibility',wind:'brisk wind, rippled water and moving foliage',storm:'a passing squall, rough exposed water and an evident reason to seek shelter'}[f.kind];
 effects.push({type:'story',instruction:'Glowhaven '+zone+' weather: '+detail+'. Keep this forecast consistent until it changes. Show only what this scene can perceive; interiors remain sheltered. Do not move anyone, invent injuries, start combat, cancel work or change the time of day. Storms are plainly warned; fishing may be postponed. This is local Glowhaven weather, not the climate of another realm.'});
 storage.fshWeatherContext=context;
}else skip=true;
