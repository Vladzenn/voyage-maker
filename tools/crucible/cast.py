"""Original recurring cast. Native cards, not runtime generator instructions."""
import random

# Name, age, species, level, affinity, hair, eyes, weapon, ordinary life,
# flaw, private stake, signature habit, combat method.
FIGHTERS = [
 ('Kōta Mibu',19,'Human',1,'Earth','russet, cropped unevenly','green','a short ash spear',
  'helps his aunt sell roofing tiles and spends his evenings carving tiny model houses',
  'applauds too early and makes promises before checking whether he can keep them',
  'wants enough confidence to ask for an apprenticeship away from the family counter',
  'counts the arena paving stones under his breath',
  'keeps both hands on his spear, holds a low forward guard and uses small earth braces; his earnest rushes leave his flank open'),
 ('Nene Inui',20,'Rabbit Beastfolk',2,'Wind','peach-pink, tied in two short puffs','amber','padded striking gloves',
  'delivers laundry, keeps absurdly competitive footrace records and loves terrible romantic plays',
  'takes corrections as dares and cannot conceal her sulking',
  'wants her older sister to stop introducing her as the unreliable one',
  'flicks a loose glove strap against her wrist when impatient',
  'boxes from an upright bouncing guard, with brief wind-assisted steps; she is fast to commit and slow to notice a patient counter'),
 ('Masato Oda',23,'Human',2,'Light','dark blue, soft and tousled','hazel','a leather sling',
  'is a parcel runner who sketches birds on wrapping offcuts and saves pretty stamps',
  'apologizes so much that people sometimes miss his actual objections',
  'wants to compete without his family turning every setback into a rescue operation',
  'checks a pebble three times before loading it',
  'favors distance and a compact side-on sling release; small flashes obscure his retreat, but his close defense is rudimentary'),
 ('Chika Umemori',22,'Human',3,'Nature','moss-green, in a blunt bob','brown','a wooden practice shield and short cudgel',
  'works in a plant nursery, grows excellent radishes and sings badly while watering',
  'becomes stubbornly silent when embarrassed instead of explaining the problem',
  'wants her friends to take a defensive fighter seriously',
  'brushes imaginary soil from her palms before introductions',
  'plants a broad shield-first stance and uses small roots to stabilize existing footing; attacks are short and cautious rather than overwhelming'),
 ('Shun Kurebayashi',24,'Human',4,'Nature','chestnut, shoulder-length and loosely tied','gold','a reinforced walking staff',
  'maintains courtyard hedges and knows an unreasonable amount of neighborhood gossip',
  'cannot resist explaining what someone else ought to have done',
  'wants to win something that cannot be attributed to a helpful relative',
  'addresses an especially stubborn weed as if it were an old enemy',
  'holds his staff diagonally with generous reach and temporary vine grips; he talks while retreating and can be rushed during a complicated cast'),
 ('Rena Kogetsu',26,'Half-elf',5,'Water','silver-lilac, in a high knot','blue','a blunt-tipped saber',
  'repairs umbrellas, collects sea glass and insists that rainy walks are underrated',
  'quietly keeps score of favors and gets prickly when people forget them',
  'wants to build a business with her own name over the door',
  'shakes water from a completely dry sleeve when thinking',
  'uses a narrow side-on saber guard and water ribbons to disguise changes in blade angle; sustained close pressure unsettles her'),
 ('Eita Kuroda',27,'Human',6,'Metal','black, shaved at the sides','gray','a short chain-linked club',
  'makes belts and harnesses and enjoys dressing far better than his workshop suggests',
  'assumes caution means cowardice until experience proves otherwise',
  'needs prize money to replace a damaged leather press he broke himself',
  'tests every chair buckle before sitting on it',
  'keeps the chain short in a compact circular guard, stiffening a link with Metal magic before a controlled strike; long-range casters force him to work'),
 ('Fuyumi Hase',25,'Cat Beastfolk',7,'Ice','white, in a long side braid','violet','a short casting wand',
  'collects overdue invoices, plays tabletop strategy games and adores warm custard',
  'enjoys being intimidating and occasionally mistakes silence for agreement',
  'wants to leave collection work without admitting how much she dislikes it',
  'smooths the same ear tuft when a plan fails',
  'stands with her wand close to her ribs, laying modest frost patches and narrow ice screens; she is patient at range but not a strong grappler'),
 ('Tsubasa Maki',21,'Avian Beastfolk',8,'Wind','teal, swept back through small feather tufts','orange','a compact recurve bow',
  'works stage rigging, dances enthusiastically and alters secondhand coats into bright costumes',
  'laughs when anxious, which can sound cruel at exactly the wrong moment',
  'wants steady work that allows time for rehearsals',
  'taps rhythms on the bow grip before drawing',
  'uses a standing three-quarter bow guard, short wind corrections and deliberate retreat; rushed shots become wild rather than magically perfect'),
 ('Yae Mitsuhara',29,'Human',9,'Water','wine-red, in loose ringlets','turquoise','a reinforced fighting umbrella',
  'sells rainwear, follows theater fashions and writes pointed anonymous shop reviews',
  'offers unsolicited advice and is deeply offended when someone returns the favor',
  'wants customers to remember her designs rather than her family connections',
  'opens an umbrella a finger-width to punctuate a dry remark',
  'turns the umbrella across her body as a guard, using a water veil to conceal a short thrust; she needs room to pivot'),
 ('Daisuke Kariya',32,'Human',10,'Earth','brown, in a rough undercut','dark green','a broad work axe',
  'loads harbor cargo, cooks extravagant stews and visits his father for weekly card games',
  'doubles down on a bad first impression instead of admitting he misjudged someone',
  'wants a less punishing job before his shoulders give out',
  'rolls a knotted rope between his palms before a match',
  'fights with a two-handed axe guard and grounded weight shifts, reinforcing his footing with Earth; he hits hard but must recover after a missed swing'),
 ('Mayu Kido',30,'Human',12,'Gravity','honey-blond, in a precise curled ponytail','ice blue','a small steel buckler and thrusting sword',
  'manages a modest family estate and has a surprisingly childish enthusiasm for marionette theater',
  'can be patronizing toward people whose manners differ from hers',
  'wants recognition that has nothing to do with the money behind her training',
  'straightens a sleeve while struggling to find an ordinary conversational reply',
  'presents a compact buckler-first guard and brief local weight shifts; her careful timing is strong, but rapid improvised exchanges expose her rigidity'),
 ('Akito Senzaki',33,'Human',13,'Illusion','ash-gray, in a loose fringe','brown','a long parrying dagger',
  'assists a funeral carver and tells beautifully timed jokes that sometimes land in dreadful company',
  'uses humor to dodge responsibility when an honest answer would be easier',
  'wants to keep the workshop afloat without asking its retired owner for help',
  'polishes a wooden button while pretending not to worry',
  'keeps his dagger low beside the hip, using a small false shoulder movement to sell a feint; the illusions do not strike or protect him on their own'),
 ('Mihana Shiraishi',31,'Fae',15,'Nature','pale green, in a thick shoulder-length braid','pink','a short harvesting scythe',
  'is an apothecary assistant with small antlers, pointed ears and barklike forearm plates; she loves dancing and sour fruit',
  'becomes possessive about useful discoveries and hates sharing credit',
  'wants to publish a practical herb guide under her own name',
  'checks the scent of a leaf whenever conversation grows awkward',
  'holds the short scythe across her waist, using plant-fiber snares to draw opponents into its hook; cutting her anchors changes the fight'),
 ('Junpei Haneda',35,'Human',16,'Fire','copper, tied into a tiny tail','golden brown','a single-edged short sword',
  'runs a lunch stall, experiments with grilled sweets and feeds stray cats after closing',
  'is generous with food but petty about criticism of his cooking',
  'wants enough winnings to hire a helper and take a real holiday',
  'compares poor footwork to an underheated pan',
  'uses a square, close short-sword guard and controlled heat along the edge; he favors short pressure sequences over distant fireballs'),
 ('Riko Narumi',28,'Human',18,'Light','midnight blue, cropped to her jaw','silver','a slender rapier',
  'is a noble-house tutor who loves elaborate puzzles and is appalling at small talk',
  'corrects people in public and cannot understand why precision fails to charm them',
  'wants a friendship that does not depend on her usefulness as a tutor',
  'starts to raise a teaching finger, then forces herself to lower it',
  'uses a long side-on rapier stance, light feints and careful point control; a close grapple or broken rhythm takes away her preferred distance'),
 ('Kenta Ishizaki',37,'Dwarf',20,'Metal','dark auburn, braided with a short beard','amber','a compact war hammer',
  'repairs mill fittings, dotes on his daughter and is fiercely competitive at children\'s board games',
  'says he is being practical when he is actually frightened of change',
  'wants to afford his daughter\'s chosen education without making her feel indebted',
  'checks a hammer fitting even when he knows it is sound',
  'keeps a low compact two-handed guard, using reinforced metal to catch a weapon and answer with a short hammer stroke; fast lateral movement costs him effort'),
 ('Sayo Kirihara',42,'Human',22,'Metal','iron-gray, in a tight bun','dark blue','a service-worn halberd',
  'is a retired caravan soldier learning amateur stage performance and enjoying it far more than she admits',
  'expects people to understand instructions she has not actually given',
  'wants to discover who she is when nobody needs a dependable sergeant',
  'marks a beat with the halberd butt before stepping into position',
  'uses a disciplined long guard, hook-and-thrust combinations and limited metal reinforcement; she is difficult to rush but can be drawn into a slow turn'),
 ('Haruto Otsuki',34,'Half-elf',24,'Enchantment','sandy blond, tied loosely back','green','a folding crossbow',
  'inspects household locks, paints miniature scenery and habitually arrives early',
  'keeps asking one more question after someone has clearly said no',
  'wants to be trusted without having to make himself indispensable',
  'aligns three bolts in exactly the same direction',
  'uses a compact crossbow stance and short reinforcement charms, choosing lanes carefully; loading and close pressure create real openings'),
 ('Natsume Aiba',39,'Human',25,'Soul','black, with a single white streak in a low braid','pale violet','a bell-topped combat staff',
  'works as an undertaker, breeds bright canaries and laughs loudly at terrible puns',
  'is nosy about other people\'s grief and sometimes mistakes curiosity for care',
  'wants to train an apprentice without becoming the sort of controlling mentor she disliked',
  'stills the staff bell with her thumb when listening seriously',
  'holds the staff diagonally in a balanced guard and uses limited spiritual wards to blunt hostile workings; she relies on solid staff strikes against physical pressure'),
 ('Daichi Kawanobe',40,'Human',27,'Earth','black, close-cropped','hazel','reinforced handwraps',
  'is a blacksmith who keeps a tiny rooftop garden and cannot resist a roadside snack',
  'believes any problem can be solved by doing more work and becomes judgmental about fatigue',
  'wants to learn how to rest before his marriage becomes another neglected project',
  'opens and closes his hands to check each wrap before the bell',
  'fights from a heavy boxing guard, bracing his feet with Earth and entering with short body blows; he must work to catch a disciplined ranged opponent'),
 ('Midori Hozumi',36,'Human',29,'Nature','bright green, in a long high ponytail','brown','a pair of hooked knives',
  'works in elder care, acts in amateur melodramas and knows everyone\'s preferred tea',
  'enjoys an audience and resents being overlooked even when the occasion belongs to someone else',
  'wants to prove that care work has not made her ordinary or invisible',
  'bows extravagantly after an unimpressive success',
  'uses a mobile crossed-knife guard and brief vine tethers to pull at a guard; the tethers have real anchors and can be cut'),
 ('Kojirō Tsunematsu',45,'Human',31,'Gravity','dark brown, graying at the temples','gray-green','a plain longsword',
  'teaches private arithmetic lessons and secretly collects ridiculous romance serials',
  'treats disagreement as a test of competence and can become insufferably condescending',
  'wants to win a championship before he convinces himself that trying was beneath him',
  'adjusts his spectacles with the clean side of a knuckle',
  'holds a high two-handed longsword guard and shifts local weight to alter a committed strike; he needs to read an approach rather than reacting to everything'),
 ('Ema Tsukishiro',29,'Human',33,'Sound','white, in an asymmetrical bob','cobalt','a ringed bronze staff',
  'is a deaf instrument maker who feels resonance through her hands, signs fluently and enjoys very bad silent comedy',
  'is blunt about mistakes and has little patience for people who mistake loud speech for accommodation',
  'wants her instruments judged for their sound rather than sold as an inspirational story',
  'rests two fingers on the staff rings to read a vibration',
  'uses a steady two-handed guard and felt vibration cues, sending short directional pulses; she cannot hear hidden conversation or sense every movement through empty air'),
 ('Ayato Nikaidō',48,'Human',35,'Arcane','violet-black, swept into a dramatic wave','gold','a broad brass-bound grimoire',
  'performs stage illusions, spends extravagantly on coats and is excellent at entertaining shy children',
  'turns conversations toward himself and sulks when a practical person gets more applause',
  'wants an actual competitive achievement that cannot be dismissed as stagecraft',
  'flourishes a page turn even when no one is watching',
  'casts from a turned stance with the grimoire braced near his ribs, using stable arcane panels and angled bolts; crowded close exchanges disrupt his elaborate setups'),
 ('Haruna Yashima',44,'Oni',38,'Soul','plum-purple, in a long loose braid','crimson','a double-ended blade',
  'works as a traveling bodyguard and misses her homeland\'s countryside food more than its politics',
  'tests people with small provocations and is indignant when they call her on it',
  'wants enough savings to take a year off rather than accept another household retainer contract',
  'offers a wrapped sweet immediately after a particularly cutting remark',
  'uses a compact diagonal twinblade guard, short pivots and spiritual reinforcement; her learned wards do not make her immune to ordinary weapons'),
 ('Seiji Makabe',51,'Human',41,'Earth','steel-gray, cropped short','brown','a broad sword and kite shield',
  'trains warehouse guards, fishes patiently and keeps losing tools in his own tidy shed',
  'takes an unfair dislike to people who remind him of his younger self',
  'wants to retire while he can still enjoy the work he keeps postponing',
  'checks the shield strap while letting an awkward silence lengthen',
  'holds his shield close with a short forward sword line, uses small earthen braces and punishes overextension; attacks from separated angles force him to reposition'),
 ('Kanna Tsuruno',47,'Dragonkin',44,'Lightning','storm-blue, in a thick braid','yellow with vertical slit pupils','a long steel-tipped spear',
  'comes from Drakenspire, appraises spearheads and loves hot springs and aggressively spicy stew',
  'is a sore loser and becomes petty about the smallest disputed point',
  'wants to win abroad before returning home to manage a workshop she is not certain she wants',
  'lashes her thick blue tail once, then pointedly stills it',
  'uses a long poised spear guard, lightning-assisted bursts and a measured retreat; her human-faced dragonkin body has swept horns and scales along her cheekbones and the backs of her arms'),
 ('Ranmaru Tōdō',55,'Human',48,'Enchantment','black, silver at the temples and tied high','emerald','a pair of steel gauntlets',
  'is a household champion who loves arranging flowers and argues passionately about vase proportions',
  'confuses refusing assistance with dignity and can be painfully proud',
  'wants to choose his own successor rather than have one selected to flatter his employer',
  'sets his sleeves back by exactly the same amount before a bout',
  'holds a poised open-handed guard, reinforces his actual body and gauntlets, and turns a caught line into a short strike; sustained reinforcement has a real Mana cost'),
 ('Mizuki Kaneshiro',118,'High Elf',53,'Wind','pale gold, in a shoulder-length braided half-up style','silver-blue','an elegant swept-hilt rapier',
  'is a youthful adult traveling collector of clocks and broken music boxes, speaking Glowhaven\'s common language with careful courtesy',
  'is vain about experience and can make a younger person feel foolish for asking a sensible question',
  'wants to find a place to live without admitting that constant travel has become lonely',
  'listens to the ticking of a small watch before answering',
  'uses a narrow side-on rapier guard with short wind-propelled entries, preserving distance instead of adding endless attacks; enclosed terrain limits the sweeping retreat'),
 ('Takeshi Onizuka',63,'Oni',58,'Gravity','salt-and-pepper, in a heavy topknot','amber','a short iron-shod greatclub',
  'is a quiet caravan veteran who knits beautiful gloves and becomes animated about wool quality',
  'holds grudges over disrespect and sees insults in clumsy attempts at familiarity',
  'wants to apologize to a former traveling partner without pretending the fault was mutual',
  'folds a finished pair of gloves with unexpectedly delicate fingers',
  'supports the club in a grounded two-handed guard and changes its apparent weight during a committed arc; the technique is costly and a missed blow still requires recovery'),
 ('Reina Hazakura',60,'Human',64,'Fire','white, in a long low ponytail','deep red','a curved two-handed saber',
  'is a former circuit champion who tends a modest orchard and is obsessed with cheap detective stories',
  'gets bored with caution and can push a promising opponent harder than they wanted',
  'wants to discover whether she still loves competing when nobody expects her to win',
  'peels an apple in one unbroken strip while considering a challenge',
  'holds the saber low across her body, lifting into decisive heat-laced cuts; she uses experience and pressure rather than pretending age grants unlimited speed'),
]

SUPPORT = [
 ('Shōgo Mizutani',49,'Human',28,'Nature','dark brown, close-cropped','gray','a blunt signal baton','referee',
  'is a former safety inspector who keeps bees, makes excellent jam and enjoys long, uneventful walks',
  'can be officious about an irrelevant detail when tired','wants competitors to trust his decisions without needing to like him','turns the baton once in his palm before giving a ruling'),
 ('Nozomi Hayase',41,'Half-elf',27,'Healing','warm brown, in a loose braid','green','a small healing staff','arena medic',
  'keeps rescue dogs with her partner and has a dry, infectious sense of humor','is impatient with dramatic patients and occasionally says so too sharply','wants enough staff to stop treating exhaustion as a personal failure','offers a chair before asking an intrusive medical question'),
 ('Gorō Azuma',56,'Human',30,'Healing','iron-gray, combed back','amber','a compact treatment grimoire','arena physician',
  'plays difficult board games, collects miniature ships and is surprisingly vain about his handwriting','explains more than a worried patient can absorb','wants to train a successor before his careful routines become the whole of his life','sets his spectacles on a folded cloth rather than a bare table'),
 ('Hina Wakabayashi',33,'Human',20,'Sound','bright orange, in a short curled bob','turquoise','a magitech voice amplifier','announcer and registration clerk',
  'sings in a little choir and keeps a notebook of overheard jokes','gets carried away by a good story and has to correct her own exaggerations','wants to become a performer without abandoning the steady work she enjoys','tries a quiet announcement into her palm before a difficult name'),
 ('Mika Koshimizu',38,'Human',24,'Enchantment','black, in a messy bob','violet','a narrow work wand','independent enchantment repairer',
  'repairs household tools at a cramped counter and loves miniature gardens','is defensive about her missing certification and treats every inspection as persecution','wants a respected shop while avoiding the debts and scrutiny a license would expose','tests a repair with the expression of someone daring it to disappoint her'),
 ('Renjirō Suda',44,'Human',22,'Arcane','brown, thinning at the crown','gray','a short iron baton','courier and private broker',
  'moves parcels through the city, plays bowls and cooks for his elderly mother','is dishonest about where a favor ends and a debt begins','wants money and discretion more than a reputation for being good','folds a receipt into a tiny square while haggling'),
 ('Momo Shiratori',27,'Human',20,'Illusion','candy pink, in a curled side ponytail','blue','a short folding fan with a mana-bearing spine','bookmaker and card player',
  'follows arena gossip, adores ugly souvenir mugs and dances badly with tremendous confidence','enjoys manipulating people who think they are cleverer than she is','wants a permanent betting room with respectable customers and very few questions','turns a coin over her knuckles without looking down'),
 ('Shiori Takase',72,'Dragonkin',26,'Water','white, in a high braided knot','blue with vertical slit pupils','a hooked short sword','Drakenspire curio dealer',
  'has slate-blue scales, curled horns and a thick tail, and enjoys elaborate stews and inexpensive theater','is a practiced opportunist who calls avarice good business','wants to stop depending on clan suppliers who can ruin a month with one refusal','taps a scale against a tooth before naming a price'),
 ('Genta Shishido',91,'Dragonkin',28,'Earth','iron-gray, in a cropped crest','green with vertical slit pupils','a heavy climbing pick','mine tally clerk',
  'has russet scales, swept horns and a thick tail, and raises stubborn goats with his spouse','is cowardly about confrontation and takes it out on people with less authority','wants enough money to leave the mine office without his household discovering the missing stock','counts a column twice when he knows someone is watching'),
 ('Koharu Mikazuki',58,'Dragonkin',32,'Wind','auburn, in a short practical braid','gold with vertical slit pupils','a pair of short cutting blades','courier and discreet fence',
  'has bronze scales, short swept horns and a thick tail, and loves racing, sewing and expensive boots','gets vindictive when a deal makes her feel foolish','wants to own a caravan rather than spend her life repairing someone else\'s mistakes','checks the stitching on a glove during an uncomfortable negotiation'),
]

def build(world):
    rng=random.Random(0xCC20261101)
    cards={};meta=[]
    names=[r[0] for r in FIGHTERS]
    common=['Arcane','Fire','Water','Earth','Wind','Lightning','Ice','Light','Metal','Nature','Sound','Gravity','Void','Healing','Enchantment','Summoning','Illusion','Divination','Soul']
    for i,row in enumerate(FIGHTERS+SUPPORT):
        fighter=i<len(FIGHTERS)
        if fighter:
            name,age,species,level,primary,hair,eyes,weapon,life,flaw,motive,quirk,method=row
            role='independent Crucible competitor'; location='The Eternal Crucible'
            area=['The Eternal Crucible - Concourse','The Eternal Crucible - Grand Stands','The Eternal Crucible - Competitor Lounge','The Eternal Crucible - Practice Gallery'][i%4]
            relation=names[(i//2)*2+(1-i%2)]
            relationships=f'{relation} is a recurring practice partner and the person most likely to challenge their excuse after a loss. Their friendship includes arguments, ordinary meals and favors that have nothing to do with tournament results.'
            secret=f'They have not told {relation} how much they are counting on the next few appearances. Their public confidence is less consistent than it looks, and {flaw}.'
            visual=f'An adult {species.lower()} with {hair} hair and {eyes} eyes. '
            visual+=['A lean build and a quick, openly curious expression.','A compact athletic build and a challenging tilted chin.','A sturdy build and a thoughtful, watchful face.','A tall build and an easy, slightly cocky posture.'][i%4]
            if species=='Rabbit Beastfolk':visual+=' Human facial features, upright rabbit ears and a short rabbit tail.'
            if species=='Cat Beastfolk':visual+=' Human facial features, small cat ears and a long cat tail.'
            if species=='Avian Beastfolk':visual+=' Human facial features, small feather tufts and feathers along the outer forearms, with human hands.'
            if species=='Fae':visual+=' Small branching antlers, pointed ears and barklike plates on the forearms; adult proportions.'
            if species=='Oni':visual+=' A human face, two short ridged horns and individually natural skin tones.'
            if species=='Dragonkin':visual+=' A human face, blue scales on the cheekbones and backs of the arms, swept horns, human palms and a thick dragon tail.'
            color=['terracotta and cream','mint and charcoal','cobalt and tan','violet and white','ochre and navy','rose and black','forest green and brass','coral and slate'][i%8]
            visual+=f' Their practical competition clothes use {color}, with a distinct well-kept travel coat or fitted training jacket.'
        else:
            name,age,species,level,primary,hair,eyes,weapon,role,life,flaw,motive,quirk=row
            visual=f'An adult {species.lower()} with {hair} hair and {eyes} eyes. '+['A sturdy build, expressive brows and a practical layered coat.','A lean build, a thoughtful face and a neat fitted waistcoat.','A curvy build, an alert smile and a handsome practical traveling jacket.'][i%3]
            if species=='Dragonkin':visual+=' A human face, swept or curled horns, scaled cheekbones and backs of the arms, human palms and a thick tail.'
            location='The Eternal Crucible' if i<36 else ('Four Sages Bazaar' if i<39 else 'Drakenspire')
            # Actual source addresses are resolved by the builder for the three Drakenspire contacts.
            area='The Eternal Crucible - Infirmary' if i in [33,34] else 'The Eternal Crucible - Competitor Passage'
            if i>=36:area=''
            relation=['Tomoe Enokida','Shōgo Mizutani','Nozomi Hayase','Tomoe Enokida','Renjirō Suda','Mika Koshimizu','Hina Wakabayashi','Koharu Mikazuki','Shiori Takase','Genta Shishido'][i-32]
            relationships=f'{relation} is a familiar professional contact whose advice they sometimes resent. Their dealings include favors, disagreements and ordinary company, not automatic trust.'
            secret=f'They minimize the cost of their ambition when speaking to {relation}. In private, {flaw}.'
            method=f'Uses {weapon} with practiced control. Their {primary} workings serve their actual work; they defend an escape route and seek help rather than pretending their occupation grants overwhelming combat power.'
        count=1 if (roll:=rng.random())<.65 else 2 if roll<.9 else 3
        affinities=[primary]+rng.sample([x for x in common if x!=primary],count-1)
        gender='female' if name in ['Nene Inui','Chika Umemori','Rena Kogetsu','Fuyumi Hase','Yae Mitsuhara','Mayu Kido','Mihana Shiraishi','Riko Narumi','Sayo Kirihara','Natsume Aiba','Midori Hozumi','Ema Tsukishiro','Haruna Yashima','Kanna Tsuruno','Mizuki Kaneshiro','Reina Hazakura','Nozomi Hayase','Hina Wakabayashi','Mika Koshimizu','Momo Shiratori','Shiori Takase','Koharu Mikazuki'] else 'male'
        visual=visual.replace('An adult '+species.lower(),'An adult '+species.lower()+' '+('woman' if gender=='female' else 'man'),1)
        public=f'{name} {life}. '+(f'They enter the Crucible when work and funds permit, and {flaw}. Winning matters to them, but their life continues after a loss.' if fighter else f'At work, {flaw}. They have limits, loyalties and interests beyond the next visitor\'s request.')
        basic=public+'\n\n'+visual+f'\n\n**Equipment:** They normally carry {weapon}, a small personal purse and the practical tools their daily work requires.'
        basic+=f'\n\n- **Gender:** {gender.title()}\n- **Age:** {age}\n- **Species:** {species}\n- **Role in faction:** {role}\n- **Magic affinity:** '+', '.join(affinities)
        hidden=f'**Private motive:** {motive.capitalize()}.\n\n**What they conceal:** {secret}\n\n**Concealment and knowledge:** {relation} knows their ordinary habits and has noticed their recent pressure, but does not automatically know the full private motive. Strangers must learn it through actual conversation and events.\n\n**Pressure point:** Being reduced to their most recent failure or treated as interchangeable labor.\n\n**Relationships:** {relationships}\n\n**How it surfaces:** They {quirk}, especially when a conversation touches the subject they are avoiding.'
        personality=[f'**Core:** {motive.capitalize()}, while remaining capable of selfish or foolish choices.',f'**Default behavior:** {life.capitalize()}; {flaw}.',
          '**Under Pressure:** Returns to their practiced method, becomes more direct and makes mistakes consistent with their actual experience.',
          '**Speaking Style:** '+['Brisk, candid and a little indignant.','Quietly dry, with pointed questions when annoyed.','Warm and animated, occasionally talking past a warning.','Formal when nervous and unexpectedly blunt when comfortable.'][i%4],
          '**Courtship Style:** Makes time for an adult they like and shares an ordinary interest; attraction does not erase existing boundaries.',
          '**Jealousy Style:** '+['Gets prickly and tries to impress, then struggles to admit why.','Withdraws into politeness before asking a direct private question.','Makes an ill-advised joke, then has to address the hurt honestly.','Becomes competitive about being helpful and resents noticing it.'][i%4],
          '**Routine or Quirk:** '+quirk.capitalize()+'.']
        abilities=[f'**Preferred Method:** {method.capitalize()}.',f'**{primary} Practice:** Uses learned {primary.lower()} techniques at a scale consistent with their experience; other affinities reflect easier study, not automatic mastery.',
          '**Fighting Style:** '+('Attempts actual subdual in regulated bouts, respects an official stop and can lose without losing their identity. Their guard, preferred reach and actual weapon remain consistent.' if fighter else 'Uses actual training to protect a route or withdraw; an official role does not confer invulnerability.')]
        card=dict(name=name,properName=name,currentLocation=location,currentArea=area,gender=gender,detailType='detailed',visualDescription=visual,basicInfo=basic,hiddenInfo=hidden,personality=personality,abilities=abilities,
          initialKnown=name in ['Reina Hazakura'],type='Crucible Competitor' if fighter else 'Resident',tier='weak' if level<=12 else 'average' if level<=44 else 'strong',level=level,faction='Glowhaven' if location!='Drakenspire' else 'Drakenspire')
        assert name not in world['npcs'],name
        cards[name]=card;meta.append(dict(name=name,level=level,fighter=fighter,major=fighter and i in [11,17,23,27,31],affinities=affinities,roll=roll,gender=gender,weapon=weapon))
    return cards,meta
