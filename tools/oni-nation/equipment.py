"""Regional equipment, techniques and bounded optional talents."""
# name, category, tier, price, slot, bonus kind/variable/value, public description
GEAR = [
 ('Plain Uchigatana','Weapon','mundane',75,'weapon','stat','damage',1,'A reliable curved steel blade with a cord-wrapped grip and plain wooden scabbard.'),
 ('Roadside Wakizashi','Weapon','mundane',50,'weapon','stat','damage',1,'A short side sword easily worn while walking, working or sitting at a crowded table.'),
 ('Ash-Shaft Yari','Weapon','mundane',45,'weapon','stat','damage',1,'A straight spear with a replaceable ash shaft and a narrow steel head.'),
 ('Garden-Guard Naginata','Weapon','mundane',90,'weapon','stat','damage',1,'A well-balanced polearm with a curved blade and sturdy heel fitting.'),
 ('Long-Road Nodachi','Weapon','artisan',220,'weapon','stat','damage',2,'A long two-handed sword with a generously wrapped grip. Its reach is awkward in small rooms.'),
 ('Maplewood Yumi','Weapon','mundane',85,'weapon','stat','damage',1,'An asymmetrical laminated bow with a cloth cover and a practical field grip. Arrows remain separate supplies.'),
 ('Practice Bokken','Weapon','mundane',18,'weapon','skill','Finesse Combat',1,'A smooth wooden practice sword with a worn oval grip. It is useful for training and still capable of causing injury.'),
 ('Short-Chain Kusarigama','Weapon','artisan',260,'weapon','stat','damage',2,'A compact sickle joined to a weighted working chain. Tangled footing or confined allies can spoil its use.'),
 ('Watchman\'s Jitte','Weapon','mundane',38,'weapon','skill','Guarded Combat',1,'An iron baton with a short side hook, used for catches and close guarded work.'),
 ('Lacquer-Rib Combat Fan','Weapon','artisan',180,'weapon','skill','Finesse Combat',2,'A reinforced folding fan with lacquered metal ribs. Opening it is a practiced action, not an automatic shield.'),
 ('Cedar Bell Staff','Weapon','artisan',150,'weapon','skill','Soul Magic',2,'A sound cedar staff with a small replaceable bell and a mana-bearing fitting. It assists learned workings.'),
 ('Heavy Boat Hook','Weapon','mundane',30,'weapon','skill','Force Combat',1,'A long working hook with a stout grip for boats, loads and awkward leverage.'),
 ('Woven Road Coat','Armor','mundane',55,'body','stat','armor',3,'A layered travel coat reinforced at the shoulders, colorful enough to be recognized across a wet yard.'),
 ('Laced Lamellar Vest','Armor','artisan',260,'body','stat','armor',7,'Overlapping small plates laced to a flexible backing. The fittings need drying after hard rain.'),
 ('Archer\'s Finger Guard','Armor','mundane',20,'hands','skill','Finesse Combat',1,'A fitted leather guard and wrist wrap for a practiced bow hand.'),
 ('Rain-Reed Cape','Armor','mundane',25,'Back','skill','survival',1,'A woven reed cape that sheds ordinary rain and smells faintly of grass when damp.'),
 ('Quiet-Sole Sandals','Armor','artisan',110,'feet','skill','Stealth',2,'Soft-lined sandals with replaceable soles. They reward careful footwork rather than silencing every step.'),
 ('Workman\'s Forearm Plates','Armor','mundane',40,'hands','stat','armor',3,'Small fitted plates protect the backs of the forearms while leaving the hands free.'),
 ('Indigo Repair Satchel','Tool','mundane',45,'tool','skill','Magitech',1,'A waxed satchel holding clamps, spare wire, small files and inspection lenses; replacement components cost money.'),
 ('Pilgrim\'s Knot Cord','Tool','mundane',12,'tool','skill','survival',1,'A strong marked cord useful for measuring, tethering and remembering a route in poor visibility.'),
 ('Field Calligraphy Kit','Tool','mundane',25,'tool','skill','spellcraft',1,'Brush, ink stone, folding board and ordinary paper for recording observations or designing a spell.'),
 ('Lens of the Honest Cut','Tool','artisan',240,'tool','skill','investigation',2,'A close lens that makes scratches, grain and small defects easier to examine in good light.'),
 ('Pulse-Fold Katana','Weapon','special',1600,'weapon','stat','damage',3,'A scarce imported magitech sword with an articulated crystal feed along its spine. Its pulse assists one committed cut; heat and a depleted feed demand attention.'),
 ('Ginkgo Lever Crossbow','Weapon','special',1400,'weapon','stat','damage',3,'An expensive crossbow whose mana-driven lever helps span the bow. It fires actual bolts and needs reloading; its hot crystal housing must be allowed to cool.'),
 ('Braced Current Cuirass','Armor','special',1800,'body','stat','armor',10,'A fitted imported cuirass with powered brace joints. Its weight and finite charge make it a serious commitment for its owner.'),
 ('Rain-Test Inspection Frame','Tool','artisan',360,'tool','skill','Magitech',3,'A portable clamp frame for inspecting a real weapon feed during controlled tests. It neither powers nor repairs an absent device.'),
 ('Foxglove Honey Cakes','Consumable','mundane',8,'',None,'',0,'Four fragrant little cakes wrapped in a leaf, sticky enough to require a careful pocket.'),
 ('Snowcedar Soup Parcel','Consumable','mundane',10,'',None,'',0,'A sealed pot of hearty stew meant to be warmed at a real shelter.'),
 ('Wayfarer\'s Salt Plums','Consumable','mundane',6,'',None,'',0,'A small packet of fiercely sour plums, favored by travelers who enjoy arguing about the best variety.'),
 ('Festival Fox Mask','Tool','mundane',16,'',None,'',0,'A brightly painted wooden festival mask with a new ribbon and a slightly lopsided smile.'),
 ('A Suspiciously Polite Fan','Relic','artisan',160,'',None,'',0,'A lacquer fan that clicks shut whenever its owner is about to give an embarrassingly long introduction. It cannot stop speech.'),
 ('Cup of the Second Opinion','Relic','artisan',180,'',None,'',0,'Tea poured into this cup briefly reflects a slightly different expression from its drinker. The image is a playful enchantment, not proof of hidden intent.'),
 ('Unfinished Boundary Doll','Relic','special',520,'',None,'',0,'A little unfinished wooden figure with a hollow back. A soft tapping answers from it near certain old boundary stones.'),
 ('Amber-Salt Sample Case','Tool','mundane',30,'',None,'',0,'Small sealed compartments hold separately labeled mineral samples. The case itself is empty when purchased.'),
 ('White Crane Message Fold','Document','artisan',75,'',None,'',0,'Thick folded paper that can keep a short ordinary message dry. It has no power to choose a recipient or fly there by itself.'),
 ('Cedar Thread Spool','Tool','mundane',12,'',None,'',0,'Strong pale thread used by repairers and shrine attendants, with a pleasantly resinous smell.'),
 ('Lanternwood Resin Lump','Tool','artisan',65,'',None,'',0,'Dark fragrant resin gathered from an actual fallen branch, useful to an informed craftsperson.'),
 ('Hagire\'s Torn Hem','Relic','special',750,'',None,'',0,'A ragged strip of faded floral cloth torn from the towering cedar-haunt. The fibers twitch once when a distant branch cracks.'),
 ('Restored Way Bell','Key','mundane',20,'',None,'',0,'A small bronze way bell repaired at Evening Maple Shrine. Its clear double note answers the old hook at Moonless Torii.'),
 ('Oni Nation Portal Key','Key','mundane',0,'',None,'',0,'A reusable issued transit key for the Evertree route to Akitsuhara. Its carved torii mark identifies Benitsuru Transit Shrine as the outward destination; the receiving hall’s return passage leads to the Evertree Portal Room.'),
]

# name | governing skill | minimum | bonus | cooldown | resource cost | concrete technique
TECHNIQUES = '''
Reed-Tip Greeting|Finesse Combat|1|2|0|Stamina:3|Make one measured spear thrust that tests a guard without committing to a pursuit.
Crane's Small Step|Finesse Combat|5|3|1|Stamina:4|Step across a narrow attack line and answer with one close counter if an opening exists.
Gatepost Brace|Guarded Combat|1|2|0|Stamina:3|Set a grounded guard against one incoming pressure while keeping a retreat lane clear.
Bamboo-Shadow Draw|Finesse Combat|10|4|1|Stamina:6|Draw a sheathed blade into one short cutting line without gaining a second free attack.
Millstone Shoulder|Force Combat|5|3|1|Stamina:5|Use body position and one controlled shoulder drive to disturb a nearby opponent's balance.
Hanging-Reed Catch|Guarded Combat|10|4|1|Stamina:6|Catch or redirect a weapon with a suitable hook or guarded polearm angle.
Eight-Petal Return|Finesse Combat|15|4|2|Stamina:7|Turn a reinforced fan or short blade through one counter line after a genuine avoided strike.
Bridge-Rail Measure|Guarded Combat|15|4|1|Stamina:6|Deny a narrow approach with a disciplined weapon line rather than an automatic knockback.
Heron's Low Wing|Finesse Combat|20|5|2|Stamina:8|Sweep a reachable leg with an appropriate staff or polearm while preserving your balance.
Red Gate Rising|Force Combat|25|5|2|Stamina:10|Commit to one rising heavy-weapon strike through a weak guard.
Long Road Reversal|Finesse Combat|30|6|2|Stamina:10|Change direction around a real obstacle and attack once from the newly earned line.
Hundred-Reed Stillness|Guarded Combat|40|7|3|Stamina:12|Read one sustained approach and meet it with a braced stop, vulnerable to a changed angle.
Quiet Knot Release|Stealth|5|3|1|Stamina:3|Free a prepared cord or simple knot without a loud tug; locks still need a real solution.
Footfall beyond the Screen|Stealth|15|4|2|Stamina:5|Use a real interruption and cover to change position without claiming invisibility.
Gatewatch Count|Perception|5|3|1|Stamina:2|Attend to one lane and distinguish actual movement from distracting activity.
Thread across the Shoal|survival|10|3|1|Stamina:4|Establish a practical tethered crossing through a short uncertain stretch.
Paper-Crane Record|Arcane Magic|1|2|0|Mana:4|Hold a small raw-mana tracing steady long enough to compare a real mark or movement.
Indigo Palm Ward|Arcane Magic|5|3|1|Mana:6|Shape one compact curved barrier across an expected line of attack.
Cedar-Ring Lattice|Arcane Magic|20|5|2|Mana:12|Raise a limited framework that obstructs a short lane while it is maintained.
Vermilion Sleeve|Fire Magic|1|2|0|Mana:4|Guide a small tongue of flame along a safe open line to light or heat a chosen point.
Autumn Fan Unfurled|Fire Magic|10|4|1|Mana:8|Sweep one flowing fan of fire across a short clear arc, accounting for people and fuel.
Red Maple Curtain|Fire Magic|25|5|2|Mana:14|Raise a vivid moving heat screen across one lane; it is dangerous, temporary and not a solid wall.
River-Silk Turn|Water Magic|1|2|0|Mana:4|Guide nearby water into a smooth narrow stream to rinse, fill or nudge a light object.
Ferrywake Binding|Water Magic|10|4|1|Mana:8|Pull available water around reachable footing to hinder one movement briefly.
Blue Sash Falling|Water Magic|25|5|2|Mana:14|Drop one controlled sheet of water to disrupt an approach without freezing it or drawing blood.
Ricebank Seat|Earth Magic|1|2|0|Mana:4|Settle a small patch of loose real soil into a firmer working surface.
Shrine-Step Uprising|Earth Magic|10|4|1|Mana:8|Raise one short ridge of available earth to interrupt a lane or give low cover.
Mountain's Folded Hand|Earth Magic|30|6|3|Mana:16|Close a limited earthen barrier around an actual position, leaving escape and structural consequences relevant.
Green Ribbon Breeze|Wind Magic|1|2|0|Mana:4|Guide a small translucent curl of air around a light object or a short exposed flame.
Swallow past the Eaves|Wind Magic|10|4|1|Mana:8|Use one brief gust to aid a committed lateral movement; it is not sustained flight.
Thousand Leaves Passing|Wind Magic|30|6|2|Mana:16|Send a broad curling gust through one lane, disturbing aim and loose footing.
Thunder under Silk|Lightning Magic|5|3|1|Mana:6|Release one short branching discharge toward a reachable conductor or target.
Storm-Drum Crack|Lightning Magic|20|5|2|Mana:12|Commit one forceful lightning strike with a visible line and real risk to nearby conductors.
Winter Plum Mark|Ice Magic|5|3|1|Mana:6|Form a small temporary ice mark that cools or makes one defined contact surface slick.
White Branch Lattice|Ice Magic|25|5|2|Mana:14|Grow a brittle temporary ice obstruction with actual gaps, anchors and melting limits.
Lantern on the Water|Light Magic|1|2|0|Mana:4|Place a small floating light near the caster, illuminating a useful area without healing anyone.
Dawn through the Screen|Light Magic|20|5|2|Mana:12|Project one concentrated beam through an actual open line.
Iron Petal Turn|Metal Magic|5|3|1|Mana:6|Turn or stabilize a small reachable metal piece without controlling an entire weapon collection.
Folded Steel Oath|Metal Magic|25|5|2|Mana:14|Reinforce one real blade through a committed action; the metal and learned weapon method still matter.
Root Bow of Welcome|Nature Magic|1|2|0|Mana:4|Guide a real pliant root or stem into a useful short curve without healing a creature.
Wisteria Gate|Nature Magic|20|5|2|Mana:12|Raise temporary plant growth across a limited opening; solid ground and fire remain relevant.
Bell over Still Water|Sound Magic|5|3|1|Mana:6|Send one tuned vibration that tests a small material or interrupts fragile concentration.
Drumbeat without Echo|Sound Magic|25|5|2|Mana:14|Release one directional sound pulse to spoil timing; allies in its line are not automatically exempt.
Ancestor's Threshold|Soul Magic|5|3|1|Mana:6|Tend a narrow spiritual boundary and contest one weak intrusive manifestation.
White Sleeve Parting|Soul Magic|20|5|2|Mana:12|Separate a hostile spirit's immediate hold through a real contested working, without commanding its entire soul.
Borrowed Festival Frame|Soul Magic|30|6|3|Mana:16|Animate one prepared empty frame for a short task using residual mana rather than a deceased conscious person.
Fox behind the Lantern|Illusion Magic|5|3|1|Mana:6|Place a limited false silhouette within a real sightline; touch and inconsistent behavior can reveal it.
Rain on an Empty Sleeve|Illusion Magic|25|5|2|Mana:14|Sustain a convincing moving decoy in one area while concentration and actual movement remain distinct.
Ink between the Leaves|Void Magic|20|5|2|Mana:12|Create a small absence that contests one fragile spell edge rather than deleting all nearby magic.
Petalweight Landing|Gravity Magic|15|4|1|Mana:10|Reduce the strain of one prepared descent over a short distance; no unrestricted flight or portal follows.
Hold the Turning Joint|Magitech|5|3|1|Stamina:4|Brace and isolate an actual mechanism's loaded joint for inspection without granting a free repair.
One Honest Charge|Magitech|10|4|1|Stamina:5|Test a real crystal feed through a controlled cycle, identifying an observable fault or safe operating limit.
Crossbow's Patient Return|Magitech|20|5|2|Stamina:7|Clear a plausible feed obstruction and reset a loaded mechanism using real tools and time.
Cooling Sparrow Cycle|Magitech|30|6|3|Stamina:9|Vent an actual overheated device through a prepared cycle; charge, material damage and safe positioning remain relevant.
'''

TALENTS = [
 ('Breath before the Blade','You settle into a clear rhythm before a difficult commitment. Gain Finesse +1 and Finesse Combat +3. Surprise and a broken rhythm still matter.','finesse','Finesse Combat',3),
 ('Root at the Heel','You are hard to hurry out of a guarded position. Gain Force +1 and Guarded Combat +3; this is practiced balance rather than immunity to being moved.','force','Guarded Combat',3),
 ('Ear for the Returning Bell','You notice small differences in repeated sounds. Gain Intuition +1 and Perception +3; a familiar voice is not proof of a familiar person.','intuition','Perception',3),
 ('Hands that Know the Form','Repeated craft and movement come readily to you. Gain Logic +1 and Spellcraft +3; invention still needs genuine experimentation.','logic','spellcraft',3),
 ('A Host at Any Hearth','You find a graceful way into ordinary conversation. Gain Empathy +1 and Persuasion +3; welcome does not grant authority or free service.','empathy','persuasion',3),
 ('Borrowed Storm Nerve','Pressure sharpens your commitment. Gain Passion +2 and Lightning Magic +3, but reduce maximum Stamina by 10. This is learned familiarity, not an added affinity.','passion','Lightning Magic',3),
]
