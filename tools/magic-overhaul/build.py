"""Build the reviewed Magic Overhaul from an explicit current Studio export.

No network access, media changes or Studio writes. --apply is explicit; without
it this writes a candidate, its exact inverse review and a scroll catalogue.
"""
import argparse
import copy
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
import project

WORLD = ROOT / 'world-draft/WorldAlpha - World.json'
OUT = ROOT / 'output/magic-overhaul-2026-11-06'
TIER_NAMES = ['Spectacular Blunder', 'Unfortunate Mishap', 'Imperfect Result',
              'Little Triumph', 'Splendid Work', 'Stroke of Brilliance', 'Storybook Triumph']
OLD_NAMES = ['Critical Failure', 'Failure', 'Mixed Results', 'Basic Success',
             'Success', 'Great Success', 'Critical Success']
ATTUNED = 'Elemental Resonance'
RECEIPT = 'Gathered Resonance'
GRADES = ['Quiet Resonance'] + [f'Resonance: {n}' for n in range(1, 20)] + ['Resonant']


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'))


def digest(value):
    return hashlib.sha256(canonical(value).encode()).hexdigest()


def changes(before, after, path=()):
    rows = []
    if isinstance(before, dict) and isinstance(after, dict):
        for key, value in before.items():
            p = (*path, key)
            if key not in after:
                rows.append(dict(path=list(p), kind='removed', before=value))
            elif value != after[key]:
                # Keep individual definition records reviewable and reversible.
                if len(path) >= 1:
                    rows.append(dict(path=list(p), kind='changed', before=value, afterHash=digest(after[key])))
                else:
                    rows += changes(value, after[key], p)
        for key, value in after.items():
            if key not in before:
                rows.append(dict(path=[*path, key], kind='added', afterHash=digest(value)))
    elif before != after:
        rows.append(dict(path=list(path), kind='changed', before=before, afterHash=digest(after)))
    return rows


def condition(kind, value, operator='contains', **extra):
    return dict(type=kind, operator=operator, value=value, **extra)


def trait_condition(value, has=True):
    return condition('player-traits', value, 'contains' if has else 'notContains')


def effect(kind, value=None, **extra):
    out = dict(type=kind, **extra)
    if value is not None:
        out['value'] = value
    if kind.startswith('player-') or kind == 'item-remove':
        out['target'] = 'satisfyingPlayers'
    return out


def rule(name, conditions, effects=(), script=None, phase='state', scope='player'):
    out = dict(name=name, recurring=True, scope=scope, phase=phase,
               conditions=conditions, effects=list(effects))
    if script:
        out['script'] = script
    return out


def make_trait(name, description, guidance, cap):
    return dict(name=name, description=description, traitNarrativeEffects=guidance,
                attributes=[], skills=[], resources=[], abilities=[], startingItems=[],
                unlockedBy=[], excludedBy=[], requirements=[dict(type='characterLevel', amount=cap + 1)])


def reactions():
    # Exact approved planning table; the runtime prompt is deliberately compact.
    return [
        ['fire','ice','Thermal Shock',20,'','Frost cracks and bursts into luminous vapor.'],
        ['water','lightning','Conduction',20,'','Blue-white filaments converge in one discharge.'],
        ['earth','sound','Faultsong',20,'','A low chord fractures a stone-colored lattice.'],
        ['wind','metal','Silver Shear',20,'','Metallic ribbons whistle along a cutting gust.'],
        ['nature','poison','Bitterbloom',20,'','A dark green flower of motes opens and collapses.'],
        ['arcane','void','Nullbloom',20,'','A violet mana knot folds into silence and snaps outward.'],
        ['light','dark','Eclipse',20,'','A bright corona closes around a dark center.'],
        ['gravity','psychic','Mindfall',20,'','A pressure note and inward mental ripple coincide.'],
        ['fire','lightning','Flashburst',10,'-3 next footing-dependent defense','A hot report unsettles balance.'],
        ['water','wind','Sprayveil',10,'-3 next visually aimed attack','Sparkling spray interrupts aim.'],
        ['ice','nature','Frostflower',10,'-3 next movement-dependent check','Leaf-shaped frost catches at a joint.'],
        ['earth','gravity','Burdenfall',10,'-5% next grounded physical attack damage','A heavy dust-ring settles.'],
        ['metal','sound','Bellshock',10,'-5% next attack damage with the affected metal implement','A bright note vibrates the implement.'],
        ['arcane','light','Prismwink',10,'-3 next visually aimed check','A prismatic afterimage offsets contact.'],
        ['dark','poison','Nightshade',10,'-5% next physical attack damage in a susceptible living body','A numb dark tracery spreads briefly.'],
        ['void','psychic','Hollow Echo',10,'-3 next concentration check of an actual mind','Uncanny silence jars focus.'],
        ['fire','nature','Cinderbloom',0,'-10% next physical attack damage in a susceptible body','A bloom of warm ash saps exertion.'],
        ['water','ice','Rimebind',0,'-5 next movement-dependent block/evade check','Frost tugs at joints or footing.'],
        ['earth','metal','Ironburr',0,'-10% next attack damage with an existing metal weapon','Grit and metallic burrs foul the weapon.'],
        ['lightning','arcane','Sparkstitch',0,'-10% next damaging spell output','The mana imprint crackles and sputters.'],
        ['wind','poison','Bitterwake',0,'-5 next visually aimed attack if eyes are susceptible','A sharp draft of stinging motes spoils aim.'],
        ['sound','psychic','Echochatter',0,'-5 next hearing/concentration-dependent check of a mind','A displaced echo troubles concentration.'],
        ['gravity','dark','Nightweight',0,'-5 next movement-dependent check of a grounded target','A dark tether of weight drags at movement.'],
        ['void','light','Afterglow',0,'-5 next concealment-dependent defense or hiding check','A pale outline lingers on an already perceived target.'],
    ]


def scroll_catalogue(w):
    old = project.load(ROOT / 'tools/item-regression-manifest.json')['scrolls']
    rows = []
    for row in old:
        gates = w['triggerDefinitions'][row['trigger']]['conditions']
        unexpected = [c for c in gates if c['type'] not in ('player-item', 'player-traits', 'story', 'skill-value')]
        assert not unexpected, unexpected
        space = any(c['type']=='skill-value' for c in gates)
        assert not space or any(c.get('skill')=='Gravity Magic' and c.get('value')==25 for c in gates)
        study = row['study']
        rows.append([row['ability'], 'm' if study in ('master', 'masterwork') else 'a' if study=='advanced' else 'p', space])
    for name, t in w['triggerDefinitions'].items():
        if name.startswith('rb_scroll_registry_'):
            data = json.loads(re.search(r'const catalogue = (.*?);\n', t['script'], re.S).group(1))
            for row in data:
                rows.append([row['ability'], {'masterwork':'m','advanced':'a','practical':'p'}[row['difficulty']], row['space']])
    assert len(rows)==130 and len({r[0] for r in rows})==130
    for ability, _, _ in rows:
        assert 'Teaching Scroll: '+ability in w['itemTypes']
        assert 'Formula: '+ability in w['traits'] and ability in w['abilities']
    return rows


def install_scrolls(w, rows):
    t = w['triggerDefinitions']
    removed = [k for k in t if k.startswith(('item31_study_', 'rb_scroll_registry_'))]
    assert len(removed)==40
    for k in removed:
        del t[k]
    bootstrap = 'storage.mxScrollCatalogue='+json.dumps(rows,ensure_ascii=False,separators=(',',':'))+';\nstorage.mxCatalogueVersion=1;\n'
    bootstrap += "for(const name of Object.keys(triggers)){if(/^item31_study_\\d+$|^rb_scroll_registry_\\d+$|^rb_study_\\d+$/.test(name))delete triggers[name];}"
    t['mx_scroll_catalogue'] = rule('mx_scroll_catalogue', [condition('read-number',1,'notEquals',key='mxCatalogueVersion')], script=bootstrap, scope='party')
    t['mx_scroll_learn'] = rule('mx_scroll_learn', [condition('read-boolean',True,'equals',key='mxScrollReady'),
        dict(type='player-item',item='Teaching Scroll: '+rows[0][0],operator='greaterThan',value=0),
        trait_condition('Formula: '+rows[0][0],False),
        dict(type='story',query='This player actually completes deliberate first-time study of their held teaching scroll and a successful controlled test. A label, intention, failed attempt or another reader does not qualify.')])
    t['mx_scroll_schedule'] = rule('mx_scroll_schedule',[condition('game-tick',0,'greaterThan')],
        script=(HERE/'scroll_scheduler.js').read_text(encoding='utf-8'),scope='party')
    return removed


def install_resonance(w):
    cap=w['progressionSettings']['maxCharacterLevel']
    w['resourceSettings']['Resonance'] = dict(name='Resonance',initialValue=0,maxValue=20,rechargeRate=0,
        restRechargeMultiplier=0,color='#8b5cf6',gainPerLevel=0,isHealth=False,
        usageInstructions='Resonance is earned through real elemental reactions, from 0 to 20. The earned charge condition is authoritative; a level-up or recovery cannot create charge. Supplied charge updates are applied once, without an additional narrative award. No gain from rain, displays, practice dummies, retelling, an ally\'s reaction or an enemy\'s reaction. At full charge, Resonant empowers the next landed damaging spell or trained combat technique: aim for 50% increased ordinary damage. Misses, healing and utility leave it ready. A reaction on the empowered hit begins the next charge. Charge persists between battles; no passive/rest/day refill. No currently authored item lowers the threshold.')
    w['traits'][ATTUNED]=make_trait(ATTUNED,'Different elements can answer one another, gathering echoes that build toward a resonant surge.','Elemental reactions can gather Resonance without teaching a new spell, affinity or skill. Actual learned methods and ordinary costs remain.',cap)
    w['traits'][RECEIPT]=make_trait(RECEIPT,'The last elemental combination still hums through your mana.','One genuine elemental reaction has left one earned spark. This is energy from the completed combination, not a second attack or an additional gain.',cap)
    for n,name in enumerate(GRADES):
        desc='Your resonance is quiet.' if n==0 else 'Your resonance is full. The next landed damaging spell or combat technique can release the stored surge.' if n==20 else f'You have gathered {n} of 20 points of Resonance through elemental reactions.'
        guidance=f'Exactly {n} earned Resonance. No passive, rest, daily or level-up refill.'
        if n==20:
            guidance+=' A damaging technique that begins with this readiness can gain 50% ordinary damage once on landing. A miss or nondamaging action retains readiness; no free hit or extra Mana. Newly reached readiness never enhances an already resolved action.'
        w['traits'][name]=make_trait(name,desc,guidance,cap)
    t=w['triggerDefinitions']
    t['mx_resonance_init']=rule('mx_resonance_init',[trait_condition(ATTUNED,False)],
        [effect('player-traits',ATTUNED,operator='add'),effect('player-traits',GRADES[0],operator='add'),
         effect('player-resource',0,operator='set',resource='Resonance')],phase='planning')
    # Native player-scoped groups are essential: no invented per-player target.
    # Descending states and receipt removal prevent same-phase cascades.
    for n in range(20,-1,-1):
        next_n=min(20,n+1)
        effects=[effect('player-traits',RECEIPT,operator='remove')]
        if n<20:
            effects += [effect('player-traits',GRADES[n],operator='remove'),effect('player-traits',GRADES[next_n],operator='add')]
        effects += [effect('player-resource',next_n,operator='set',resource='Resonance')]
        if next_n==20 and n<20:
            effects.append(dict(type='story',instruction='Earned Resonance reaches its full chorus. It is ready for the next landed damaging technique, not an action already resolved. Do not create an extra attack.'))
        name=f'mx_resonance_earn_{n:02}'
        t[name]=rule(name,[trait_condition(GRADES[n]),trait_condition(RECEIPT)],effects,phase='planning')
        name=f'mx_resonance_mirror_{n:02}'
        t[name]=rule(name,[trait_condition(GRADES[n]),trait_condition(RECEIPT,False),
            condition('player-resource',n,'notEquals',resource='Resonance')],
            [effect('player-resource',n,operator='set',resource='Resonance')],phase='planning')
    t['mx_resonance_gain']=rule('mx_resonance_gain',[
        condition('game-tick',0,'greaterThan'),trait_condition(ATTUNED),trait_condition(RECEIPT,False),
        dict(type='story',query='In the latest completed turn this player personally finished a genuine combat elemental reaction from the configured 24-pair table on an actual opposed target. A real prior eligible elemental hit on that exact target came from a separate action no earlier than the preceding party turn, and the compatible finisher actually landed despite defenses. Count at most one reaction for this player this turn. A miss, immunity, harmless display, training farm, same-action fusion, rain alone, merely naming a reaction, an old retelling or another character finishing is false. Respect actual supplied combat results.')],
        [effect('player-traits',RECEIPT,operator='add')])
    t['mx_resonance_spend']=rule('mx_resonance_spend',[
        condition('game-tick',0,'greaterThan'),trait_condition(GRADES[20]),
        dict(type='story',query='In the latest completed turn this player began an actual damaging spell or trained combat technique already Resonant, then landed that paid or ordinarily valid attack and released the ready surge. The readiness existed before this action; acquiring it after an already resolved action is false. A miss, fully immune hit, insufficient cost, healing, crafting, conversation, utility, hypothetical attack or another player\'s attack does not consume this player\'s surge.')],
        [effect('player-traits',GRADES[20],operator='remove'),effect('player-traits',GRADES[0],operator='add'),
         effect('player-resource',0,operator='set',resource='Resonance')])


def rename_types_and_tiers(w):
    def visit(x):
        if isinstance(x,dict):
            out={('poison' if k=='poisoning' else k):visit(v) for k,v in x.items()}
            if out.get('type')=='action-success-level':
                mapping={a.casefold():b.casefold() for a,b in zip(OLD_NAMES,TIER_NAMES)}
                out['value']=mapping.get(str(out.get('value')).casefold(),out.get('value'))
            return out
        if isinstance(x,list):return [visit(v) for v in x]
        return 'poison' if x=='poisoning' else x
    w=visit(w)
    for key in ['description','traitNarrativeEffects']:
        w['traits']['Venom-Hardened'][key]=w['traits']['Venom-Hardened'][key].replace('poisoning','poison')
    c=w['combatSettings']
    assert 'soul' not in c['damageTypes']
    c['damageTypes'].append('soul')
    icons=['🏹','🗡️','🔨','🧪','🔥','⚡','🌪️','💧','✨','☀️','🌑','🧠','🪨','❄️','⚙️','🌿','🎵','🪐','🕳️','👻']
    for name,icon in zip(c['damageTypes'],icons):
        c.setdefault('damageTypePresentation',{}).setdefault(name,dict(emoji=icon))
    prompts=[
        '{{characterName}} fails severely within the action\'s actual stakes. Show the concrete cause, including capable opposition or bad circumstances; do not force slapstick, incompetence or death.',
        '{{characterName}} does not achieve the intended task. Show the actual obstacle or opposing response, without inventing consequences beyond the action\'s risk.',
        '{{characterName}} achieves a meaningful partial result with a concrete limitation, compromise or cost. Do not narrate either a complete failure or an unqualified success.',
        '{{characterName}} achieves the intended task modestly and within scope. Add no invented complication or extra prize.',
        '{{characterName}} achieves a clean, confident success with a concrete useful result within the action\'s scope.',
        '{{characterName}} executes the action especially well. Render the supplied benefit vividly without adding unsupported attacks, damage, items or abilities.',
        '{{characterName}} achieves an exceptional, memorable result within the actual action and supplied mechanics. No automatic plot victory, free ability or additional critical multiplier.',
    ]
    for tier,name,prompt in zip(w['successLevelSettings']['tiers'],TIER_NAMES,prompts):
        tier['name']=name;tier['prompt']=prompt
    return w


def instructions(w, recipes):
    a=w['aiInstructions']['generateActionInfo']
    a['impact']='Existing impact scale: about 100 ordinary; 50–90 constrained scope/execution or restraint; 120–150 real preparation/leverage or paid stronger work; 150–200 exceptional committed output with actual cost/scope. Honor resolved force. Adjectives or large target Health grant no accuracy, second hit or extra outcome. Apply only the explicit reaction/Resonance adjustments below.'
    # Preserve the existing operations while removing duplicate examples so this
    # task stays below its native 20,000-character ceiling.
    a['custom']='''RESOLVE IN ORDER
Identify actor, objective, actual method/target/range/access, usable equipment/ability and limits. Preserve nonlethal intent and exact quoted speech. A gesture is not speech; a claim is not acquisition.
Routine feasible movement, conversation, browsing, agreed payment, rest, showing an item, refusal and authorized travel need no check. Danger, opposition, deception, investigation, crafting and challenging work do; safe deliberate practice can use a learning check, but trivial repetition guarantees no XP.
Name one actual configured governing skill, never an attribute, blank, None or profession. Use the appropriate skill even if untrained; an observer's power does not rescale an ordinary task. Consider real opposition, environment and preparation.
Apply actual requirements, bonus, cooldown, scope and cost once. Infused physical delivery uses one physical accuracy resolution; a detached spell uses its discipline. Never sum skills or demand two hits for one action. Supporting motion/flair adds no attack, parry or universal second action.
Resolve the finite achievable task. Diagnosis is not repair; do not invent a fault or impossibility to erase success. Follow supplied results and the actual action budget. Return only requested fields.'''
    a['Exact Skill Routing']='''Force Combat: power, leverage, heavy entries, committed grapples and bodily tackles/rams. Finesse Combat: precise/quick weapon or unarmed delivery, aimed physical shots and timed footwork. Guarded Combat: bracing, shields and contested defense. Choose by training and actual delivery, not weapon shape, an exciting verb or the word charge. A weapon-led rush/leap/dive remains weapon delivery, not automatically acrobatics or a similarly named ability. Named techniques retain requirements/cost/scope; room and momentum grant no free hit.
A detached/remotely shaped spell uses its actual learned discipline. Infusion retains physical delivery. spellcraft is invention/substantial redesign, not an extra check for each learned spell. Affinity grants no proficiency; Space retains its Gravity foundation and Time stays reserved.
athletics: exertion/heavy movement; acrobatics: balance/agile navigation; Stealth: concealment; survival: wilderness judgment; investigation: systematic evidence; Perception: noticing; Insight: inference, never mind-reading. persuasion, intimidation, Deception, Etiquette, performance and Trade resolve their actual resisted tasks, not routine conversation, purchases or refusal.
Medicine treats without magic; Healing Magic restores magically; Alchemy prepares mixtures; Magitech works devices/foci/mechanisms; Enchantment changes properties. Cooking, Perfumery and Animal Handling keep their scopes. Routine understood orders need no check. Tactics resolves contested coordination; actual Summoning controls summons, actual Soul working raised undead, Animal Handling animals. An ally's ordered attack resolves its own effect, never the player's attack or an automatic damage boost. Invent no Command or weapon-family skill.
Fishing/Intuition: rod casts and landing fish.'''
    a['Mana, Casting and Exhaustion']='''Use authored costs/cooldowns first. New undefined workings use minor 1–3, basic 6, moderate 14, powerful 30, extreme 55 Mana, adjusted only for real scope/limits. Released misses normally spend the commitment. No double infusion charge, miss refund or second passive recovery.
Zero usable Mana leaves the caster conscious and ordinary casting fails. Rare forced last casting needs exceptionally difficult authoritative resolution, never routine Health/vital-mana payment. Humanoid extraction below usable mana remains unobserved theory, not standard Void; refilling Mana does not cure established soul shock.
Personal blueprints, trained body casting and optional words/gestures are ordinary. Suitable mana-bearing catalysts assist; a real external reserve must actually exist. Enchanted does not automatically mean magitech. Rare Freeform is difficult and usually slower; familiar creativity bypasses no training.
Healing respects real injury and scope, without automatic reversal of age, lasting damage, death or shock. Mana transfusion remains unsolved with weak prototypes. Regulated medicines use their actual effect once; potion implies no universal dose/price/refill. Overuse can cause vomiting/migraine and poor return, not automatic fatal overdose. Research-only stronger formulations need actual authorization/provenance.
Basic physical actions cost no Stamina; special exertion pays once. Pure casting has no automatic Stamina tax; demanding mixed work can spend both. Zero Stamina leaves routine defense and consciousness intact.'''
    a['Creative Methods and Practical Alternatives']='''Classify the actual operation beneath colorful phrasing: heating, cooling, light, movement, reinforcement, concealment, sensing, growth, stabilization or negotiation use the actual trained method. Familiar creativity need not create a new ability, but scope/training/uncertainty remain.
Allow viable physical, magical, social and occupational solutions. A blocked route may be cleared, bypassed, repaired or opened by agreement; these are not equally feasible and not all need checks. Resolve the chosen method, never automatically the strongest school. Noncasters use keys; casters can lift boxes by hand.
Small learned workings can aid ordinary reading, washing, heating, moving light objects or finite protection without becoming battlefield powers or granting spells. Use actual untrained rules rather than treating affinity as universal mastery.
A diagram, measured material, safe test or relevant observation can solve real uncertainty. Honor that preparation through resolution, without compulsory difficulty, generic bonuses per detail or fresh drawbacks after success.'''
    a['Local Movement and Explicit Commitment']='''Before classification identify the current parent/area, own present action, local referent and selected destination. Questions, wishes, quotations, negations and future plans do not move anyone. Asking about a mine is not entering its actual nearby entrance.
Searching, pursuing, fleeing or following without a chosen mapped endpoint stays local. An indicated adjacent door remains usable; stop at a real exit choice. Never map an improvised camp/tower/vault/cave onto a distant authored place by shared words. Resolve shortened area names inside the current parent; clarify material ambiguity.
Explicit distant travel begins the real journey with actual access, route and transport. Existing movement retains its range: no short blink becomes a realm crossing, and no invented portal/mount removes distance. Real authored forced transfer takes precedence, once.
Asterveil's adjacent pins may be separated by sky. Use actual paths, maintained spans or stated carriers/water routes; personal flight needs real capacity and landing. A visible island is not automatically blink range. Booking is not arrival.'''
    a['Targets, Practice and Supported Modifiers']='''Target the actual recipient: hostile pressure/distraction/taunts the foe; ward/block/buff/heal the beneficiary; testing an object the object, never its owner. Cover protects an ally against the enemy. Sides follow actual participation/allegiance, not party membership alone; betrayal or aiding an enemy needs that intent.
Damage follows what lands, not school/name: a magically hurled stone is bludgeoning, not psychic. Use a registered channel, including poison and offensive soul, never invent a label. Practice uses the exact configured skill even if unowned, including dummy/lesson/study attempts; native learning/XP decides progress, not unchanged trivial repetition.
Use actual modifiers and supported resolved conditions. No hunger/sleep-debt meter, arbitrary low-Mana exhaustion or higher difficulty for mastery. Injury, terrain and active reaction debuffs count where relevant, once; never also lower difficulty for the same numerical opening. Safe routine actions need no filler roll.'''
    a['Approach Mapping and Mixed Techniques']='''Logic: Arcane, Metal, Gravity, Enchantment, Space. Passion: Fire, Lightning, Earth, Wind, Water. Empathy: Healing, Nature, Light, Summoning, Soul. Intuition: Divination, Void, Illusion, Ice, Sound. Reserved Time uses Logic, with no starting study/affinity. Force covers power/resilience; Finesse timing/precision. No Endurance attribute. These are capabilities, not personalities.
Infusion resolves physical delivery once; detached spells their discipline. Prerequisites add no skill total, hit or attack. Ordinary physical work costs no Mana; demanding mixed techniques can spend both Mana/Stamina. Intentional bodily enhancement uses learned Enchantment; elemental propulsion its element. Neither adds a turn.
Ice needs no Water prerequisite, Metal no Earth, Sound no Wind. Space requires Gravity; Time also requires its exceptional actual teaching route. Affinity waives neither.'''
    a['Difficulty and Outcome Scope']='''Use allowed difficulties from the actual challenge/opposition, never desired drama or the player's best stat. Preparation matters when it solves a real constraint; names/compliments grant no bonus. Equipment/abilities give supported bonuses only.
Objects are their own targets: dummy/plank/lock/barrier/instrument, not the owner. Controlled demonstrations need not be lethal. Heals and protection identify beneficiaries/positions. Collateral harm, splash, theft and witnesses need real support.
Social success achieves a feasible concession within knowledge/authority, not an authentic key from nowhere, true false-evidence, forced desire or universal authority. Honor a won concession; do not repeat refusal under a technicality. Accepted evidence persists until real contrary evidence.
Perception senses, investigation infers from accessible evidence, Insight detects mismatches without hiddenInfo, and Divination follows actual limits. An NPC believing a lie does not change history. Asking to kill an absent boss grants no reachable target or skipped travel. Zero Health is defeat; further lethal action needs a real living target and outcome.'''
    a['Portals and Movement — Current Input']='''Public portal travel requires actual route effects and fixed endpoints; description or a view through an arch does not move the party. Evertree Base - Portal Room connects to Drakenspire - Portal Room inside Drakenspire Portals, or Cloudbloom Landing - Portal Room inside Cloudbloom Landing. Keep their parent rooms/realms distinct.
Outbound public travel needs its issued destination key and operating arch. Enrollment, approved trade, court duties or credible sponsorship can support court approval; status alone issues no key. Approval needs no repeated persuasion/passenger incantation. Inspecting/approaching/asking is not crossing. Testing a named portal commits to one crossing, never an automatic return; an unmistakably selected arch can be 'I go in.'
All external fixed returns lead directly to Evertree Base - Portal Room without another key, approval, exact arch-area phrase or landing choice. The reusable Glowhaven Portal Key documents that route, not anywhere recall. Resolve clear Gloomhaven typos locally. Move actual traveling companions, not bystanders. Apply real one-time route effects independently of briefings/exams, once; this classifier selects no anomaly outcome or duplicate item.
Private Space teleportation is separate difficult learned work with actual range and existing endpoint. Match successful travel to its native location/area update; do not announce arrival while state stays at origin or invent a route/spell.'''
    a['Practice, Crafting and Learning']='''Dummy strikes, forms, coached exercise, first sparks and applied study are relevant exact-skill attempts even if unowned. Carrying a book/chatting is not practice. Failure may teach; this classifier grants no XP, rank, affinity, level or ability.
Spell invention/substantial redesign uses spellcraft; familiar simple designs can be tried quickly, difficult work needs preparation/tests. Corrections cause no automatic injury/consolation power. Learned blueprints cast on their discipline without another compulsory Spellcraft check.
Teaching-scroll decoding uses spellcraft, a practical test its discipline. Difficulty follows complexity and real preparation; research can compensate for low skill, not opening a master scroll. The shared learning transaction grants the formula.
Magitech needs real tools, parts, design and ownership. Mundane mechanisms need no Spellcraft; invented magical operation does. Diagnosis, consent, work and handover differ; joint techniques require present willing partners and real methods.'''
    a['Law, Competition and Final Check']='''Active tournament duels forbid mana medicine/external reserves; ordinary legal focuses remain permitted. Discover cheating through evidence, not universal detection. Emergency medical care after a stop differs. Guards normally seek proportionate arrest/subdual, not execution for insult; crime, resistance, jurisdiction and authority govern response.
No crime teleports an undefeated suspect. Prison workers, visitors and prisoners have different access. Ordinary shifts, knockouts or mode changes do not release custody; actual short-term release or choosing to serve the remainder can. Held Wanted Poster switches the solo Glowhaven arrest loop; discarding it cancels pursuit. Require surrender/resolved capture before transfer. No extra poster or arrest inferred from low Health. Honor death/resource rules.
Final check: real command/target, feasible scope, one governing skill/accuracy resolution, cost once, no invented travel/reward or routine movement roll. Return requested fields only.'''
    table=[]
    for x,y,name,bonus,debuff,flair in recipes:
        table.append(f'{x}+{y}: {name}; +{bonus}%'+(f'; {debuff}' if debuff else '')+'. '+flair)
    a['Elemental Reaction Table']='ONLY THESE 24 ORDER-INDEPENDENT PAIRS REACT. First percentage is extra hit damage; any following penalty is the single debuff.\n'+'\n'.join(table)
    a['Reaction Resolution and Resonance']='''Recognize actual resolved hits, not declared success. A damaging eligible elemental hit leaves one imprint on its exact target through the following completed party turn. Only a later separate action with a listed compatible channel can consume it for one reaction; it leaves no new imprint. Same element refreshes; unlisted eligible element replaces. Physical slashing/piercing/bludgeoning and soul neither prime nor consume an imprint. Misses, full immunity, weather alone, harmless display and same-action fusion do not prime/react. Reaction damage cannot re-prime. Maximum one reaction per target and one earned charge per human finisher per party turn. Enemies use the same reactions; no automatic NPC Resonance pool.
Use the table's ordinary-hit damage uplift plus its one listed debuff. Each target has at most one reaction debuff: newer replaces older. It ends after its next applicable resolution or the end of the following party turn. An attack-output penalty expires on the qualifying attempt even if it misses; a defense penalty waits for a relevant defense. Respect real anatomy, senses, surfaces, equipment and immunities; do not invent missing conditions. No skipped turns, automatic disarm/fall, permanent stat loss or extra targets. -5 to defense accuracy is not -5 armor; -10% output is a 0.90 multiplier, not 10 extra damage taken. Do not also award another contextual advantage for the same effect.
A technique begun already Resonant aims for +50% ordinary damage on its next landed damaging spell/trained combat action. A miss, unaffordable or nondamaging action retains readiness. The final charging hit never boosts itself. Combine the custom damage layer additively: 100+reaction(0/10/20)+burst(50), at most 170%, before ordinary target mitigation. Typed charge/consumption updates own the gauge; do not award another point in prose. No training/display farm, passive/rest/day/level refill. No free extra Health subtraction after combat results.
Offensive soul is its own non-reacting channel. Where the resolver can distinguish ordinary worn armor's contribution, treat only that contribution as 90% for this hit; never bypass immunity, wards or all defense, invent an armor stat, or substitute +10% final damage. Support/restoration Soul work causes no automatic harm.'''
    story=w['aiInstructions']['generateStory']
    story['Combat Narration']='''Combat Results determine actual source, action, target, modifiers, hit/miss, damage and end state. Render that scope: no miss-to-hit rewrite, invented immunity, fresh parry, unresolved strike or double damage. An ally's ordered attack is not the player's attack.
Show range, approach, cover, line of force and resulting position. Blades, fists, shields, constructs and spells act concretely; Force/Finesse/Guarded delivery differs from detached casting. One infusion is one resolution, not another attack, stun or turn. Use actual equipment, training, condition, Mana and costs. Hand casters need no weapon; ordinary professors remain trained adults.
Show allies' actual attacks, healing/protection/control, not just commentary. No supplied ally action means no invented damage/healing/bonus; attempted cover can still be preparation. Keep beneficiary and enemy distinct.
When a listed elemental reaction really resolves, name it naturally and show its brief elemental interaction, exact finisher/target and relevant aftermath. A label or a player's claim is not proof. Preserve the prior hit's actual element/target and turn; never carry an imprint/debuff past its one-turn window or across combat/scene departure. A newer reaction debuff replaces older; show recovery when it expires. Cosmetic recoil grants no second penalty. Charge updates arrive through the actual supplied effects; a completed successful scroll study awaits its one learning transaction, never a second narrative grant.
Honor nonlethal intent, subdual, retreat, surrender and negotiated stops. Downed enemies stop acting. No invented collateral deaths, structural collapse, permanent terrain, endless phase, army, blocked exit, ultimate or soul trick cancels victory. Apply real costs/cooldowns/death rules; aftermath and recovery prose add no refill.'''
    # Keep the task below 30k by tightening a redundant aftermath paragraph.
    story['Victory and Downtime']='A real victory ends its resolved danger. Honor surrender, escape, nonlethal defeat and completed finite work without inventing a replacement threat or extra phase. Give room for treatment, conversation, repair, loot actually present and the player\'s next choice. Describe native rewards once; no invented payout or compulsory follow-up. Injury, obligations, costs and lasting consequences persist as established; quiet narration supplies no additional restoration or resurrection.'
    item=w['aiInstructions']['ItemGenerationAndUsage']
    item['Teaching Scrolls and Learned Formulas']='Teaching Scrolls are finite Documents, not spells granted by inspection. Deliberate first study needs a real successful controlled test: practical formulas can use one focused exercise; advanced work solves a genuine difficulty; masterwork needs substantive research, correction and a final success. Excellent study can compensate for low discipline, not an unwitnessed claim. Space retains Gravity Magic 25; Time has no scroll. Failed study retains the item.\nThe shared learning transaction alone grants the exact Formula trait and ability and consumes one copy from the successful holder. Different formulas may verify on successive turns; preserve completed study and continue naturally. Do not duplicate inventory/ability changes, spend an ability point, grant a rank/affinity, or consume a known formula again. A recipient must actually study. Learning written instructions is not personal spell invention or automatic completion of the first-original-spell quest. Casting retains real skill, Mana, scope and cooldown.'
    learned=w['aiInstructions']['generateLearnedAbilities']
    learned['Teaching Scroll Discoveries']='All 130 authored Teaching Scroll formulas are scroll-exclusive. Their exact Formula traits and abilities are awarded by the shared successful-study transaction, not ordinary ability-point purchases or a renamed grant. Substantial research may compensate for low school skill; retain Space\'s Gravity Magic 25 foundation and Time restrictions. Failed or unfinished study keeps the scroll. Known formulas consume no duplicate. Independent Spellcraft may develop related workings through its own real invention process. Written study alone is not a first-original-spell quest completion; casting retains actual school, Mana, scope and cooldown.'
    learned['Damage Identity']='For an offensive created technique, state the actual registered damage channel plainly in its description, with its concrete effect, limits and cost. A burning projectile deals fire; a magically hurled rock deals bludgeoning. A school prerequisite or decorative aura does not determine the channel. Support/restoration abilities need no damaging label. Use poison, not the retired poisoning label; offensive soul is distinct and non-reacting. A single fused technique is still one action and cannot react with its own elements. Do not add an unsupported damageType member or grant access to a school through a name.'
    summary=w['aiInstructions']['summarization']
    summary['Brief Combat Continuity']='Keep only a still-live elemental imprint: actual target, landed element and turn. One imprint per target; a separate compatible hit consumes it. Keep a reaction debuff\'s affected action and next-use/one-turn expiry, then drop it after expiry, combat end or departure. No historical reaction becomes an active mark. Earned Resonance and readiness follow the actual character state, not an inferred refill. Preserve recent genuine scroll-study completion awaiting shared verification and its reader/formula; do not invent ownership, a learned formula or consumption.'


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base',type=pathlib.Path,required=True)
    parser.add_argument('--apply',action='store_true')
    args=parser.parse_args()
    raw=args.base.read_bytes();base=json.loads(raw.decode('utf-8-sig'))
    current=project.load(WORLD)
    assert not base['triggerDefinitions'].get('mx_scroll_catalogue'),'Supply the unmodified current Studio merge base.'
    rows=scroll_catalogue(base)
    w=rename_types_and_tiers(copy.deepcopy(base))
    removed=install_scrolls(w,rows)
    install_resonance(w)
    recipes=reactions();instructions(w,recipes)
    project.validate(w)
    for key in ['npcs','itemTypes','abilities','regions','storyStarts','parties','gameplayMusicSettings','progressionSettings','locationSettings']:
        assert w[key]==base[key], 'Unexpected change to '+key
    assert w['locations']==base['locations'],'Incoming Studio positions/art must remain exact.'
    baseline=current
    existing=HERE/'review.json'
    if existing.exists():
        old=project.load(existing)
        if digest(current)==old['afterHash']:
            # Recover only the already reviewed inverse, never an ignored world snapshot.
            baseline=copy.deepcopy(current)
            for r in old['rows']:
                p=baseline
                for k in r['path'][:-1]:p=p[k]
                k=r['path'][-1]
                if r['kind']=='added':del p[k]
                else:p[k]=r['before']
            assert digest(baseline)==old['baseHash']
    review=dict(inputSHA256=hashlib.sha256(raw).hexdigest(),baseHash=digest(baseline),afterHash=digest(w),
                rows=changes(baseline,w),recipes=recipes,removedScrollTriggers=removed,
                scrollCount=len(rows),hybridApproved=True,livePlaytest=False,
                changedFromIncoming=changes(base,w))
    project.write_json(HERE/'scroll-catalogue.json',rows)
    project.write_json(HERE/'review.json',review)
    project.write_json(HERE/'reactions.json',recipes)
    project.write_json(OUT/'The Schools of Magic, Arise! - Magic Overhaul.json',w)
    if args.apply:
        assert digest(current) in (review['baseHash'],review['afterHash'])
        project.write_json(WORLD,w)
        project.sync()
    print(json.dumps(dict(candidate=str(OUT),scrolls=len(rows),reactions=len(recipes),
                          semantic=sum(any(c['type'] in ('story','action') for c in t['conditions']) for t in w['triggerDefinitions'].values()),
                          triggers=len(w['triggerDefinitions']),applied=args.apply),ensure_ascii=False))


if __name__=='__main__':main()
