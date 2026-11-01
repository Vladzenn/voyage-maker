"""Targeted rules and cast recalibration; no broad text substitution in world data."""
import copy


def apply(world, baseline, manifest):
    ai = world['aiInstructions']
    ai['generateStory']['custom'] = '''Use the actual attributes, skills, abilities, resources and relevant lore. Force includes resilience; no Endurance exists. Approaches are methods, not temperaments. Affinity eases study, not mastery. Trained body casting and personal blueprints are ordinary; catalysts usually hold no spare Mana. Bodily enhancement uses Enchantment; elemental propulsion differs. True Freeform remains rare and demanding. Empty usable Mana leaves a conscious person unable to cast normally, not automatically dying. Never invent routine Health payment, humanoid soul extraction, perfected transfusion, resurrection or a cure for age. Actual requirements, costs, cooldowns and resolved learning govern; a focus, observed lesson or shouted move name grants no power.'''
    ai['generateActionInfo']['custom'] = '''RESOLVE IN ORDER
1. Identify actor, objective, actual method, target, range, access, usable ability/equipment and stated limits. Preserve nonlethal intent and exact quoted speech. A gesture is not dialogue; a claim is not acquisition.
2. Routine feasible movement, conversation, browsing, agreed payment, rest, showing an item, refusal and authorized travel need no check. Meaningful danger, opposition, deception, investigation, crafting and challenging work do. Safe deliberate practice can use a real learning check; trivial repetition guarantees no XP.
3. Name exactly one actual governing skill, spelled as configured. Never return an attribute, None, blank or a profession label. An untrained appropriate skill remains appropriate; do not substitute a higher unrelated skill.
4. Use the task, actual opposition, environment and preparation. A powerful observer does not rescale an ordinary object or the world's residents.
5. Apply actual requirements, bonus, cooldown, scope and cost once. An infused physical hit uses one physical accuracy resolution; a detached spell uses its discipline. Never sum two skills, choose the highest unrelated one or demand two successful hits for one action.
6. Define the feasible result and consequence. A successful finite task finishes its scope; diagnosis alone is not repair. Do not invent a fresh fault or impossibility to cancel success.

NO EXTRA ACTIONS
Supporting movement, a flourish or elemental visual does not add an attack. Follow the engine's actual action budget and supplied outcomes without a fresh parry or invented universal two-attack allowance. Return only the requested output fields.'''
    ai['generateActionInfo']['Exact Skill Routing'] = '''PHYSICAL DELIVERY
Force Combat resolves power, leverage, heavy entries and committed grapples. Finesse Combat resolves precise or quick weapon/unarmed delivery, aimed physical shots and timed footwork. Guarded Combat resolves bracing, shield position and contested defensive exchanges. Training and actual delivery select the lane, not weapon shape or an exciting verb. Swords, glaives, halberds, lances, tridents, quarterstaffs, javelins, slings, sai, katars, gauntlets and tonfa all follow that distinction. A weapon-led charge, rush, leap or dive stays a physical weapon delivery; a body tackle or horn ram is a bodily Force action. A leap does not automatically turn a sword hit into acrobatics. 'Charge' is not a request to use a similarly named ability. A genuinely used named technique keeps its actual requirements, cost and scope. Room, footing and committed momentum can affect a supported result, never grant invented damage or an extra hit.

MAGIC AND INVENTION
A detached or remotely shaped spell uses its actual learned discipline. An infused weapon strike still resolves physical delivery once. Spellcraft resolves invention or substantial redesign, not an extra roll for every learned spell. Affinity supplies no proficiency. Space retains its Gravity foundation; Time remains reserved.

PRACTICAL AND SOCIAL
athletics: exertion and heavy movement. acrobatics: balance and agile navigation. Stealth: concealment. survival: wilderness judgment. investigation: systematic evidence. Perception: noticing. Insight: inference, not mind-reading. persuasion, intimidation, Deception, Etiquette, performance and Trade govern their actual resisted tasks; ordinary conversation, purchases and refusal need no check.

CRAFT, CARE AND ORDERS
Medicine treats without magic; Healing Magic casts restoration. Alchemy prepares mixtures; Magitech works equipment, foci and mechanisms; Enchantment changes properties. Cooking, Perfumery and Animal Handling keep their scopes. A routine understood order needs no check. Contested tactical coordination uses Tactics; controlling a summoned being uses the actual Summoning working, raised undead their actual Soul working, and an animal Animal Handling. Ordering an ally to attack is not the player's personal attack and gives no automatic damage boost. The ally's actual action resolves its own effect. No invented Command, weapon-family skill or second accuracy roll.'''
    ai['generateNPCIntents']['Teamwork, Companions and Bystanders'] = '''ALLY PARTICIPATION
Capable allies actually engaged on the player's side contribute useful attacks, control, protection, healing or rescue within the real action budget. This includes agreed companions, active summons, trained pets and present helpers whose allegiance is established. Do not apply an enemy's self-preservation instruction indiscriminately to every ally or leave a front-line companion merely advising for several exchanges. A healer with the actual ability, Mana and opportunity treats a relevant injury; finite healing and real priorities still apply.

ORDERS AND CONTINUITY
An understood feasible order can guide this round at the named target. A controlled summon or raised body keeps its last continuing order within the actual duration, control and ability until changed or impossible. Human allies retain judgment and may question an unsafe or incompatible demand. A direction to wait, protect, stop or retreat matters. Orders do not produce the player's own attack or an automatic extra action. A decoy is not another fighter; a projectile is not a pet.

LIMITS AND WITHDRAWAL
Hold space, flank, interrupt or cover a coordinated withdrawal when a straightforward attack is poor. Intelligence is not universal desertion, but loyalty is not forced suicide. Civilians, downed people, restrained allies, broken control and explicit refusals retain their limits. No teleporting absent companions or automatic recruitment of every friendly person. Combat Results alone establish damage, healing and incapacitation.'''
    ai['generateStory']['Combat Narration'] = '''RESOLVED RESULTS
Combat Results determine source, action, target, modifiers, hit/miss, damage, status and end state. Narrate their actual scope. Never change a miss into a hit, complete an unresolved strike, add a fresh parry or cancel success with a hidden immunity. An order to an ally is not the player's own attack.

READABLE METHODS
Establish range, approach, cover, line of force and resulting position. Show what the actual blade, fist, shield, construct or spell does. Force pressure, Finesse precision and Guarded resistance differ from detached spellcasting. An infused physical hit is one resolution; speed and spectacle add no attack, stun, turn or support bonus. Use actual equipment, training, condition, Mana and techniques. A hand caster need not acquire a weapon and a boring professor remains a trained adult.

ALLIES AND TARGETS
Show participating allies' actual resolved attacks, healing, protection and control rather than replacing them with commentary. If an ally received no resolved action, preparation or attempted support cannot manufacture damage, healing or a bonus. Keep beneficiary and enemy targets distinct; a command is not an offensive hit on the commanded ally. Quietly covering a retreat can be useful.

CONSEQUENCES
Use bounded recoil, light, sound and material interaction without invented collateral casualties, structural collapse, permanent terrain or additional injuries. Honor nonlethal intent, actual subdual, retreat, surrender and a negotiated stop. A downed enemy stops acting. No new ultimate, endless phase, army, blocked exit or soul trick cancels victory. Costs and cooldowns remain real; a recovery paragraph adds no free refill. Apply the selected death rules without turning every setback into death.'''
    ai['generateNPCIntents']['when_to_generate'] = ai['generateNPCIntents']['when_to_generate'].replace(
        'A level-70 administrator can be average tier; a level-50 frontline professor can be strong.',
        'A level-30 administrator can be average tier while a level-30 frontline professor is strong.')
    ai['generateStory']['Quest Scenes and Lasting Outcomes'] = '''When accepted work reaches its stated end, show the decisive deed plainly using the actual full identity of the relevant person, object and place. Match its stated final objective so the completion judge has concrete evidence. Do not invent success, retcon a failed action, add another return report or re-open a solved fault. A public situation is an opportunity, not consent to a quest. A native arc can produce meaningful next work after a consequence; do not turn each conversation into a chapter. Out-of-character quest-repair commands are never spoken by NPCs and create no fictional achievement.'''
    ai['generateStory']['Work, Trade and Property'] = '''Work, loans, shopping and property use actual terms and supported transactions. A quote is not payment, a repair target is not loot and a viewing key is not ownership. After real room access or property acquisition, retain its location, owner, agreement and ordinary key/deed. Do not charge ongoing rent while the player is away, invent eviction or passive income, fill the home with unbought specialist tools or conscript the household into the party. Ordinary private interiors can be areas within existing residential locations; they are not new nations or realms. Successful services and paid bills remain settled.'''
    # Replace existing leaves rather than pushing the already near-full task over its cap.
    ai['ItemGenerationAndUsage']['Crafting, Enchantment and Repairs'] = '''REPAIR AND REFINEMENT
Inspect the actual owned item, explain the proposed result, quote the real labor/materials and obtain agreement. Ordinary maintenance restores function; it adds no bonus pick, tier or resource refill. A genuine refinement changes that inventory instance rather than creating a duplicate and leaving the old one equipped. Keep its identity, images, history, condition and existing legitimate properties unless the agreed alteration changes one. Apply actual payment and consumed materials once, then one supported inventory change. No successful result without the needed tools, materials, method and resolved work.
Generated and refined gear follows itemSettings.tiers bonusPolicy: permitted targets and per-pick ranges, initialMaximumPicks/refinedMaximumPicks, and no more than two picks of one bonus type on refinement. Do not fill every possible pick automatically. No generated Time bonus, new spell, infinite charge, passive healing or sale value loophole. Bonuses on equipment affect the supported equipped statistic; they are not consumable doses. Authored catalogue records retain their defined bonuses and are not retroactively rewritten by generation policy.'''
    ai['ItemGenerationAndUsage']['Property, Custody and Recovery'] = '''ROOMS AND PROPERTY
On an actually completed rental, purchase or grant of a private room, supply one appropriate key/deed with a distinct natural name identifying the actual place. Its description records the real recipient, arrangement and any agreed paid term in ordinary language. Reuse an existing matching key instead of duplicating it. A viewing, quoted price, promise or remembered old purchase is no acquisition. Fixed named property transactions have native payment/key effects; do not duplicate those changes. For a genuinely different property, use the supported normal item-generation/update workflow, not an invented dynamic trigger effect.
A key remembers an arrangement; it gives no stats, master access, clan membership, ownership of neighbors' rooms, free stock or income. Losing a physical key is not a magical reversal of a legal deed. Rent is paid for the agreed stay, with no unattended background money drain. A new extension needs its actual agreement.
CUSTODY
Deposit only actual seized property and retain its custody receipt and recovery terms. A knockout does not restore unavailable equipment or grant prison release. Actual authorized recovery returns the deposited belongings once, without a second fresh set.'''
    ai['ItemGenerationAndUsage']['Item History and Final Review'] = '''Keep the actual object's owner, custody, alterations, distinctive condition and real transaction history. Show newly acquired objects in inventory only after acquisition. A resource dose applies its defined actual effect once; a better description adds no extra healing or Mana. Keep quoted stock, entrusted work and a promised reward separate from possessions. Public inventory prose describes the object and its use naturally, never triggers, save records, authored content, identifiers or narrator instructions. Review exact configured names, tier, slot, targets and price before returning supported item operations.'''
    ai['generateNewNPC']['Power Anchors and Professional Breadth'] = '''FIXED POWER ANCHORS
Generate for the actual role, place, training and threat rather than the player's level or the highest NPC nearby. Ordinary untrained adults are often level 8–20; practiced workers and guards 15–28; trained professors and headmasters about 28–32. Headmaster is an administrative job, not a power promotion. Use about 40–45 for genuinely exceptional specialists and court elites, and 50–55 for the four exceptionally powerful Archons. Do not generate a random level-70 professional, 87 shopkeeper or hidden demigod to fill an ordinary role. Ilyra Stillglass at 100, Ragnar Leonhart at 67 and established legendary creatures are authored exceptions, not templates for generated people.
Rank, office, age, wealth, portrait flair and species do not confer mastery. A lazy graduate still knows magic; a good researcher can be poor in a fight; an elderly worker need not be an elite combatant. Native tier, level and actual bonuses all affect power. Use a modest actual tier and avoid stacking unexplained multipliers. Preserve existing authored levels, including the Spider Realm. Ordinary generated jobs fit the least experienced human; powerful NPC companions do not raise the routine encounter band. Harder territories and named threats retain real power when knowingly chosen, with useful warning.'''
    world['storySettings']['questGenerationGuidance'] = '''OPPORTUNITIES AND AGREEMENT
Start with a person, concrete want and circumstance the player can act on. Reuse nearby authored people and acquaintances. A posting needs a client, terms and return contact. Offer two or three suitable possibilities when work is requested. Public news, overheard disagreements and visible problems can invite investigation without accepting or creating a journal entry. Ignore an unpursued lead rather than repeating it. Ordinary kindness and conversations need not become quests.

LOCAL CHARACTER
Academies: actual courses, teachers, years, experiments, contests, favors and rivalries. Their civic duties suggest work without dictating personality. The academic sequence keeps its own readiness and invitations.
Guild: finite contracts, hunts, escorts, recovery, repairs and professional disputes. Check the actual Bronze/Silver/Gold/Platinum badge. Pay the full posted fee; court keys and property permission remain separate.
Drakenspire: mountain routes, craft, clans, households, ancestors, pit contests and winter supplies. Terrain, promises and material needs create pressure; rare beings are not guaranteed appointments.
Asterveil: crossings, rescue, specimens, materials, research and competing expeditions. Distinguish Cloudbloom woodland, Rimeglass exposure, Mirrorwater channels and Amethyst acoustic terrain. Follow actual local bands and npcTypes; this remains midgame.
Everyday Glowhaven: food, music, neighbors, shopping, repairs and personal trouble. Simple work can end simply. Lawful prison work uses actual permission and never grants release just for finishing an errand.

PLAYABLE RESISTANCE
For substantial work, identify the obstacle, its location, how it blocks success and what resolves it. Use an actual rescue, contest, magical working, hazardous crossing, negotiation, fight or demonstrated result. Deliberately entering occupied dangerous ground produces the real encounter, not tracks forever. Tools, preparation, training and cooperation matter. Vary physical, magical, social and investigative approaches; animals are not negotiators by default.

QUESTS AND NATIVE ARCS
Most generated work is a finite standalone episode. Use configured arcs only for their actual premises, participants, secrets and expected conclusions; generated chapters belong to the runtime arc rather than an invented authored arcId. One meaningful development and its consequences justify another chapter. Preserve discoveries after a setback. Do not force every arc onto one player or split several simultaneous errands serving one goal into separate quests. Arc participants retain independent lives and motives. Respect credible alternative conclusions and do not restart a resolved arc merely to supply more content.

CHECKABLE ENDINGS
Give a generated quest a concrete final objective and a typed completionCondition repeating that final step's wording with the full relevant person, item and place names. Allow the stated alternatives and genuine imperfect results when appropriate. A proposal, quoted objective or unperformed promise does not qualify. Once achieved, let the scene show the deed plainly; no extra signatures, report loops or new mastermind are required. Failure can change cost, approach or relationships without erasing every clue.

CONTINUITY AND REWARDS
Compare active, planned, completed, declined and abandoned work by people, site and problem, not title alone. Preserve solved conditions; recurring work needs a fresh instance and terms. First thesis is once per playthrough, including transfers. Academic milestones, field tests, expeditions, the anomaly and Silken investigation retain separate conditions. No automatic calendar jump, acceptance, pass, recruitment or absent-participant credit.
State known risk, scope and payment before commitment. Respect refusal and withdrawal. Use one supported completion and reward owner; authored effects settle their fixed reward once. No duplicate prose payment or credit for unrelated work. Loans, salvage and customer property follow real agreements. Access, lessons and company can matter beside money; no generic reward grants affinity, mastery, court keys or affection.

INFORMED RISK
Routine work fits the least experienced human, excluding powerful NPC companions. Introductory Bronze work normally uses one level 1–3 weak hostile. Substantially harder work needs explicit player interest and concrete warning before acceptance. Offer a safer option instead of a surprise lethal mission. Existing scripted events, authored encounters and their conditions remain unchanged.'''

    level_overrides = {
        'Akane Todo':55, "Gen'ichirō Mizuhara":55, 'Tōru Shizunami':55, 'Reika Saionji':52,
        'Kōhei Sanada':32,'Norio Shibata':30,'Miyu Asahina':30,'Kiyoko Fujinami':30,
        'Ritsu Kurogane':32,'Haruki Saitō':29,'Ranka Kagari':30,'Ririka Kujō':29,'Kei Aoki':30,
        'Sōichirō Takamine':32,'Madoka Narukami':31,'Genzō Iwakura':32,'Noriaki Takatsuki':31,
        'Kaoruko Hanazono':30,'Reon Fujisaki':31,'Kana Fujimoto':28,'Tetsuya Samejima':31,
        'Seiran Yukitsugu':45,'Gōtarō Iwamine':44,'Ayame Kazehara':43,'Shion Kurobane':42,
        'Daizen Iwatsugu':52,'Gōki Shishido':44,'Tomoe Arashimine':45,'Karia Morino':42,
        'Natsume Hibari':39,'Benjirō Kanemori':38}
    protected = {'Ilyra Stillglass','Ragnar Leonhart','Rovakthuun','Orrum','Orivelle'}
    spider_regions = {k for k,v in baseline['regions'].items() if v['realm']=='The Silken Descent'}
    spider_locations = {k for k,v in baseline['locations'].items() if v['region'] in spider_regions}
    level_changes = []
    for name, old in baseline['npcs'].items():
        if name in protected or old.get('currentLocation') in spider_locations: continue
        npc = world['npcs'][name]
        level = old.get('level',1)
        if name in level_overrides: new = level_overrides[name]
        elif old.get('type') == 'Student': new = min(level,24)
        elif old.get('type') in ['Resident','Merchant','Artisan','Court Official','Prison Officer','Guild Staff','Healer','Academy Staff','Performer']: new=min(level,28)
        elif old.get('type') in ['Teacher','Headmaster','City Guard','Researcher','Field Guide']: new=min(level,32)
        elif old.get('type') == 'Noble': new=min(level,40)
        elif old.get('type') == 'Adventurer': new=min(level,40)
        else: new=level
        if new != level:
            npc['level'] = new
            level_changes.append(dict(name=name,old=level,new=new,tier=npc.get('tier')))
        # Do not compensate a lower level with inflated numeric bonuses.
        if new <= 32:
            for key, ceiling in [('healthMultiplier',1.25),('successBonus',5),('damageModifier',10),('damageReductionModifier',10)]:
                if key in npc and npc[key] > ceiling:npc[key]=ceiling
    world['npcs']['Ragnar Leonhart']['hiddenInfo'] = world['npcs']['Ragnar Leonhart']['hiddenInfo'].replace('Radan wants','Ragnar Leonhart wants')
    reciprocal = {
      'Akemi Fushida':'Daigo Kisaragi and the Bellwether Company are current paying lodge guests. She knows their room and practical supply needs, not every private disagreement or the source of the cold they are investigating.',
      'Natsume Hibari':'Tomoe Inukai trades practical mountain route reports with Natsume Hibari. Neither is obliged to guide a new expedition without an actual agreement.',
      'Kureha Kazahana':'Suzuha Midorise has asked for a review of properly obtained sky-organism observations. Kureha Kazahana respects careful field evidence and is not committed to validating the student\'s favored theory.',
      'Kana Fujimoto':'Suzuha Midorise is an adult fourth-year student who finds Kana Fujimoto approachable for practical faculty questions. That contact is neither automatic expedition support nor a promise of graduation.',
      'Kiyoko Fujinami':'Suzuha Midorise has approval for properly supervised field research. The approval does not guarantee a finding, waive court travel authorization or complete her thesis.',
      'Honoka Hazukawa':'Honoka Hazukawa has given Suzuha Midorise practical local cautions about collecting sky-organism samples. Familiarity does not make either person the other\'s keeper.',
      'Komugi Hanabishi':'Marika Hoshino visits as a qualified field assessor; Komugi Hanabishi retains registration and records. Tetsuya Kanamori takes actual equipment commissions at the appraisal bench, and Renpei Sugita is a recently licensed Bronze adventurer. Iona Hayashida is a useful independent supply contact when available.',
      'Mai Kajiwara':'Tetsuya Kanamori has exchanged practical repair notes with Mai Kajiwara. Each keeps ownership of their own work and can disagree about an equipment recommendation.',
      'Akira Oritsu':'Masaru Hasebe is an approved civilian maintenance contractor. Akira Oritsu knows the background disclosed during contracting and retains actual case and access authority; the worker cannot grant a release.'}
    for name, text in reciprocal.items():
        assert name in world['npcs'], name
        hidden = world['npcs'][name]['hiddenInfo']
        marker='**Relationships:**'
        if marker in hidden:
            start=hidden.index(marker)+len(marker)
            end=hidden.find('\n\n',start)
            end=len(hidden) if end<0 else end
            hidden=hidden[:end]+' '+text+hidden[end:]
        else:
            hidden+='\n\n'+marker+' '+text
        world['npcs'][name]['hiddenInfo']=hidden
    manifest['relationshipUpdates']=list(reciprocal)
    # Named new specialists fit the same scale; not every new face is an elite.
    for name, level in {'Daigo Kisaragi':32,'Chisato Akamine':32,'Tomoe Inukai':30,'Gaku Shindō':28,
                        'Jōta Kamezaki':28,'Beni Tsunoda':31,'Riko Kanehara':27,'Sōta Tobisawa':25,
                        'Marika Hoshino':40,'Ysolenne':46}.items():world['npcs'][name]['level']=level
    manifest['levelChanges'] = level_changes
    # Town services should not generate office workers at wilderness-champion levels.
    city_locations = []
    for name,loc in world['locations'].items():
        if name in spider_locations: continue
        if name.endswith('Academy') and loc['region']=='Glowhaven':
            loc['npcLevelRange']={'min':12,'max':32};city_locations.append(name)
    manifest['generationBandChanges']=city_locations
    world['tipSettings']['tips'].extend([
        'An overheard problem is an opportunity, not an accepted quest. Ask for the terms or leave it alone.',
        'A room key or deed records your actual lodging or property agreement. A viewing does not buy the building.',
        'Ordinary repairs restore function. Refinement needs an agreed improvement, suitable materials and real work.',
        'If a genuinely finished quest stays active, type quest done: followed by its exact journal name. This optional repair works on your honor and applies its normal rewards.',
        'A weapon-led charge still uses your actual physical combat method. Giving an ally an order is not your own attack.',
        'Headmasters administer schools. Their office does not automatically make them stronger than their experienced faculty.'
    ])
    lore = {
      'Adventuring Companies and Ordinary Lives':'Small adventuring companies share work, expenses, arguments and reputations within the international guild. Their private banners are not extra guild ranks. A company can hire a specialist or cooperate with a stranger without making that person a permanent member. Friends keep appointments, own belongings, enjoy meals and take days off as well as undertaking danger.',
      'Homes, Workrooms and Agreements':'Glowhaven and its partner settlements offer paid guest rooms, modest homes and small workspaces. Rental terms are agreed with the actual host; a purchase names its buyer and property. Tagged keys and deeds identify those arrangements. Viewing keys, borrowed tools and household hospitality are not ownership. A workspace supplies the agreed room, not an inexhaustible business, free specialist equipment or authority over neighbors.',
      'The Stillwind Pearl':'Travel accounts describe a pale pearl in the spent chambers of certain sky nautiluses. Most stories disagree about its usefulness. Careful field study can distinguish a real rare object from the impressive properties people have attributed to it.',
      'Improving Familiar Equipment':'Skilled craftspeople inspect and maintain familiar equipment, and some can undertake a substantial refinement with the right materials and a clear commission. Replacing a worn grip is not the same work as changing an enchanted property. Owners often value a well-understood tool or weapon more than a fashionable replacement.'}
    world['worldLore'].update({k:{'text':v} for k,v in lore.items()})
