// A typed-trigger fixture, not the Voyage engine or an AI evaluator.
// Runs the shipped scripts. Trigger rewrites become active on the next turn.
const vm=require('vm'),assert=require('assert');
const clone=x=>structuredClone(x);
function player(items={},traits=[],skills={}){
    return {items:{...items},traits:[...traits],skills:{...skills},abilities:[],abilityPoints:3,
        resources:{Health:100,Mana:100,Stamina:100,Resonance:0},level:1};
}
function compare(a,op,b){
    if(op==='contains')return Array.isArray(a)?a.includes(b):String(a).includes(b);
    if(op==='notContains')return !compare(a,'contains',b);
    return {equals:a===b,notEquals:a!==b,greaterThan:a>b,lessThan:a<b,greaterThanOrEqual:a>=b,lessThanOrEqual:a<=b}[op];
}
function fixture(world,{players={Alice:player()},snapshotConditions=false,reverse=false}={}){
    const s={tick:0,actions:[],story:'',storage:{},players:clone(players),fired:[],notes:[],semanticChecks:0,
        rules:clone(Object.fromEntries(Object.entries(world.triggerDefinitions).filter(([k])=>k.startsWith('mx_'))))};
    function raw(c,source=s.players){
        if(c.type==='game-tick')return s.tick;
        if(c.type==='action-text')return s.actions;
        if(c.type==='story-text')return s.story;
        if(c.type==='read-number')return typeof s.storage[c.key]==='number'?s.storage[c.key]:0;
        if(c.type==='read-boolean')return s.storage[c.key]===true;
        if(c.type==='player-traits')return Object.fromEntries(Object.entries(source).map(([k,p])=>[k,p.traits]));
        if(c.type==='player-item')return Object.fromEntries(Object.entries(source).map(([k,p])=>[k,p.items[c.item]||0]));
        if(c.type==='player-resource')return Object.fromEntries(Object.entries(source).map(([k,p])=>[k,p.resources[c.resource]||0]));
        if(c.type==='skill-value')return Object.fromEntries(Object.entries(source).map(([k,p])=>[k,p.skills[c.skill]||0]));
        throw Error('Unsupported fixture read '+c.type);
    }
    function check(c){
        const value=raw(c);
        if(!c.operator)return value;
        return value&&typeof value==='object'&&!Array.isArray(value)
            ?Object.values(value).some(v=>compare(v,c.operator,c.value)):compare(value,c.operator,c.value);
    }
    function recipients(rule,semantic,source){
        const found=[];
        for(const name of Object.keys(source)){
            let ok=true;
            // Model native mechanical-before-semantic gating explicitly.
            for(const c of rule.conditions.filter(c=>!['story','action'].includes(c.type))){
                let value=raw(c,source);
                if(['player-traits','player-item','player-resource','skill-value'].includes(c.type))value=value[name];
                if(!compare(value,c.operator,c.value)){ok=false;break;}
            }
            if(!ok)continue;
            for(const c of rule.conditions.filter(c=>['story','action'].includes(c.type))){
                s.semanticChecks++;
                if(!semantic(name,rule,c)){ok=false;break;}
            }
            if(ok)found.push(name);
        }
        return found;
    }
    function apply(effect,names){
        if(effect.type==='story'){s.notes.push({players:names,instruction:effect.instruction});return;}
        assert.strictEqual(effect.target,'satisfyingPlayers','No fabricated specific-player target');
        for(const name of names){
            const p=s.players[name];
            if(effect.type==='player-traits'){
                if(effect.operator==='add'&&!p.traits.includes(effect.value))p.traits.push(effect.value);
                if(effect.operator==='remove')p.traits=p.traits.filter(t=>t!==effect.value);
            }else if(effect.type==='player-abilities'){
                if(!p.abilities.includes(effect.value))p.abilities.push(effect.value);
            }else if(effect.type==='item-remove'){
                assert.ok((p.items[effect.item]||0)>=effect.quantity,'Cannot consume another player\'s absent copy');
                p.items[effect.item]-=effect.quantity;
            }else if(effect.type==='player-resource'){
                assert.strictEqual(effect.operator,'set');
                p.resources[effect.resource]=Math.max(0,Math.min(world.resourceSettings[effect.resource].maxValue,effect.value));
            }else throw Error('Unexpected fixture effect '+effect.type);
        }
    }
    function phase(name,semantic=()=>false){
        const source=clone(s.players), rules=Object.values(s.rules).filter(t=>t.phase===name);
        if(reverse)rules.reverse();
        const decisions=snapshotConditions?new Map(rules.map(r=>[r.name,recipients(r,semantic,source)])):null;
        for(const rule of rules){
            const names=decisions?decisions.get(rule.name):recipients(rule,semantic,s.players);
            if(!names.length)continue;
            const sandbox={check,storage:s.storage,triggers:s.pending,effects:clone(rule.effects),skip:false};
            if(rule.script)vm.runInNewContext(rule.script,sandbox,{timeout:100});
            if(sandbox.skip)continue;
            assert.ok(sandbox.effects.length<=10);
            for(const effect of sandbox.effects)apply(effect,names);
            s.fired.push({tick:s.tick,phase:name,name:rule.name,players:names});
        }
    }
    function turn({actions=[],story='',semantic=()=>false}={}){
        s.actions=actions;s.story=story;s.pending=clone(s.rules);
        phase('planning',semantic);phase('state',semantic);
        s.rules=s.pending;delete s.pending;s.tick++;
        return s;
    }
    return {s,turn};
}
module.exports={fixture,player};
