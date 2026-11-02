"""The additional scoped character-creation and guild-exam fixes requested during production."""
PROFESSIONS={
 'Civic Work and Law':[
  ('Petition Clerk','You have helped people turn a confused grievance into an intelligible petition and kept the supporting papers in order.','Etiquette','investigation'),
  ('Hearing Assistant','You have prepared hearing rooms, recorded testimony and learned when a witness needs a clearer question.','Insight','Etiquette'),
  ('Customs Clerk','You have checked manifests, compared real cargo and learned the familiar ways a description conceals a load.','Trade','Perception'),
  ('Village Steward','You have organized shared repairs, supplies and meetings among neighbors with competing needs.','persuasion','Trade'),
  ('Warehouse Keeper','You have kept goods dry, counted incoming loads and identified which missing crate actually matters.','Trade','investigation'),
  ('Court Messenger','You have carried time-sensitive dispatches and learned who can receive them without turning every doorway into an argument.','Etiquette','athletics')],
 'Roads, Rivers and Transport':[
  ('Ferryman','You have handled a real ferry, judged crossings and helped awkward passengers reach the bank.','survival','athletics'),
  ('River Pilot','You have read channels, currents and landing approaches while bringing a loaded boat through.','survival','Perception'),
  ('Porter','You have balanced difficult loads, tied working knots and learned which promise is heavier than its fee.','athletics','Trade'),
  ('Caravan Cook','You have fed traveling crews with limited fuel, uncertain weather and ingredients that survived the road.','Cooking','survival'),
  ('Salvage Diver','You have worked below water with preparation, practical tools and respect for a return line.','athletics','Perception'),
  ('Bridge Inspector','You have checked joints, wear and load paths, and can explain a repair without making damage sound mysterious.','investigation','Magitech')],
 'Textiles, Timber and Earthen Craft':[
  ('Papermaker','You have prepared fibers, judged pulp and dried usable sheets in weather that rarely cooperates.','Trade','Perception'),
  ('Lacquerer','You have prepared surfaces, applied patient layers and learned how light reveals a careless finish.','Trade','Perception'),
  ('Weaver','You have set a loom, planned a pattern and repaired the small fault that would spoil an entire length.','Trade','Perception'),
  ('Ropemaker','You have selected fibers, laid strands and tested a rope before someone trusted their weight to it.','Trade','athletics'),
  ('Shipwright','You have fitted timber, followed a hull line and learned what a quiet leak can become at sea.','Magitech','survival'),
  ('Miller','You have managed grain, working water and the unpleasant sound a bearing makes before it fails.','Trade','Perception'),
  ('Potter','You have shaped clay, prepared a firing and learned to distinguish an attractive vessel from a sound one.','Trade','Perception'),
  ('Dyer','You have mixed real dyes, prepared fabric and kept a reliable record of colors that change while drying.','Trade','Alchemy')],
 'Stage, Festivals and Story':[
  ('Actor','You have rehearsed scenes, listened for a cue and held an audience through a line that did not land as expected.','performance','Deception'),
  ('Storyteller','You have shaped a tale for listeners, recognized impatience and changed pace without losing its thread.','performance','Insight'),
  ('Puppeteer','You have built a convincing gesture from cord, timing and a voice the audience wants to follow.','performance','Magitech'),
  ('Costume Maker','You have fitted garments for movement, quick changes and people whose measurements keep becoming an opinion.','Trade','performance'),
  ('Festival Organizer','You have scheduled performers, arranged supplies and found room for celebrations amid ordinary work.','persuasion','Trade')],
 'Woodland, Fields and Wildlife':[
  ('Beekeeper','You have tended hives, read a disturbed swarm and gathered honey without treating the colony as disposable.','Animal Handling','survival'),
  ('Orchardist','You have pruned fruit trees, judged harvests and kept pests from becoming everyone else’s problem.','survival','Trade'),
  ('Charcoal Burner','You have managed slow earth kilns, watched heat and kept the right sort of fire alive for days.','survival','Perception'),
  ('Woodcutter','You have judged a tree’s lean, maintained an edge and cleared timber with a safe working space.','athletics','survival'),
  ('Trapmaker','You have built and checked practical traps, followed signs and understood what an unintended catch costs.','survival','Magitech'),
  ('Gamekeeper','You have monitored a hunting ground, distinguished ordinary tracks and dealt with people ignoring sensible limits.','survival','Animal Handling')],
 'Martial Service and Pursuit':[
  ('Dojo Assistant','You have maintained a practice floor, helped beginners find a safe stance and learned through repeated correction.','Guarded Combat','Insight'),
  ('Household Retainer','You have served a household through escort duties, ceremonies and the ordinary work behind an impressive gate.','Etiquette','Guarded Combat'),
  ('Bodyguard','You have watched approaches, planned an exit and put yourself in position before a threat became obvious.','Guarded Combat','Perception'),
  ('Bounty Tracker','You have followed a particular person through evidence, testimony and preparation for an actual capture.','survival','investigation'),
  ('Scout Runner','You have carried observations quickly and learned how to report uncertainty without hiding it.','athletics','Stealth')],
 'Shrines and Spiritual Care':[
  ('Shrine Attendant','You have tended a shrine, received ordinary visitors and practiced the small routines that keep its court useful.','Etiquette','Soul Magic'),
  ('Funeral Assistant','You have prepared solemn gatherings, handled belongings respectfully and supported people whose needs differ from the formal rite.','Medicine','Insight'),
  ('Ritual Musician','You have maintained a ceremonial rhythm and heard how an uncertain performer changes the whole group.','performance','Sound Magic'),
  ('Spirit Mediator','You have practiced listening, recognizing a limited manifestation and making a carefully scoped spiritual agreement.','Soul Magic','Insight')],
 'Discreet and Questionable Trades':[
  ('Smuggler','You have moved goods through unwanted attention and learned that a route is only as good as its next handover.','Stealth','Trade'),
  ('Fence','You have assessed doubtful goods, negotiated hurried sales and noticed the questions a seller avoids.','Trade','Insight'),
  ('Forger','You have imitated papers and marks, studied mundane materials and learned which small inconsistency draws an eye.','Deception','investigation'),
  ('Locksmith','You have maintained real locks, understood their wear and opened mechanisms with the right tools and patience.','Magitech','Perception')]
}

def apply(w):
    cat=w['traitCategories']['Profession & Useful Skills']
    # Keep all existing choices and replace the four broad display groups with clearer groups.
    groups=[
      {'name':'Metal, Tools and Workshop','traits':['Magitech Technician','Blacksmith Apprentice','Armorer','Jeweler','Glassblower']},
      {'name':'Study, Medicine and Records','traits':['Research Assistant','Medical Assistant','Alchemist Apprentice','Perfumery Apprentice','Scribe','Archivist','Interpreter','Tutor','Appraiser','Private Investigator']},
      {'name':'Trade and Hospitality','traits':['Merchant Apprentice','Cook','Accountant','Innkeeper','Tavern Worker','Baker','Tea Blender']},
    ]
    additions=[]
    for group,rows in PROFESSIONS.items():
        names=[]
        for name,desc,primary,secondary in rows:
            if name in w['traits']:raise ValueError('Profession collision '+name)
            w['traits'][name]={'name':name,'description':desc+f' Start with +2 {primary} and +1 {secondary}.','traitNarrativeEffects':desc,'attributes':[],'skills':[{'skill':primary,'modifier':2},{'skill':secondary,'modifier':1}],'resources':[],'startingItems':[],'abilities':[],'unlockedBy':[],'excludedBy':[],'requirements':[]}
            cat['traits'].append(name);names.append(name);additions.append(name)
        groups.append({'name':group,'traits':names})
    routing={
     'Textiles, Timber and Earthen Craft':['Carpenter','Mason','Tailor','Bookbinder'],
     'Roads, Rivers and Transport':['Courier','Caravan Hand','Sailor','Cartographer'],
     'Stage, Festivals and Story':['Performer','Stage Magician','Dancer','Musician'],
     'Woodland, Fields and Wildlife':['Field Scout','Animal Caretaker','Farmer','Herbalist','Gardener','Fisher','Shepherd','Stablehand','Monster Hunter Apprentice','Miner','Prospector'],
     'Civic Work and Law':['Community Coordinator','Lamplighter','Watch Recruit']}
    for group in groups:group['traits']=routing.get(group['name'],[])+group['traits']
    cat['subcategories']=groups
    covered=[x for g in groups for x in g['traits']]
    assert sorted(covered)==sorted(cat['traits']) and len(set(covered))==len(covered)
    desc='Your foundation comes from regular physical practice: carrying awkward loads, keeping your footing, controlling a fall and repeating movements until they become dependable. Strength and coordination develop together, whether you plan to fight, travel, work with your hands or support later magical training. Start with +1 Force and +1 Finesse.'
    for key in ['description','traitNarrativeEffects']:w['traits']['Physical Foundations'][key]=desc
    talent=w['traitCategories']['Special Talent'];talent['maxSelections']=2
    talent['description']=talent['description'].replace('choose one unusual gift','choose up to two unusual gifts').replace('blessing or exceptional aptitude','blessings or exceptional aptitudes')
    # Story starts already own their base 1,000 marks. Remove only the duplicate shared 18.
    shared=w['itemSettings']['startingItems']
    assert {'item':'Mark','quantity':18} in shared
    w['itemSettings']['startingItems']=[r for r in shared if r!={'item':'Mark','quantity':18}]
    guidance='\n\nASSESSMENT SAMPLES\nGuild judgment examples, practice notices and classroom hypotheticals are not live contracts or new journal quests. Generate no job from an exam sample. First licensure remains its existing quest; real work needs a separate actual offer.'
    w['storySettings']['questGenerationGuidance']+=guidance+' For configured contracts keep the exact client, place and fee; accept only the single identified chosen offer.'
    assert len(w['storySettings']['questGenerationGuidance'].encode('utf-16-le'))//2<=5000
    q=w['parties']['']['quests']['Guild: Adventurer Licensure']
    q['questDesignBrief']+='\n\nThe judgment review uses a clearly labeled sample scenario, not a live request from the board. Its fictional client, terms and place do not become a quest, appointment or map destination. State the short example fully and recognize a natural answer that shows scope, ownership and sensible withdrawal; do not demand a repeated three-part recitation after understanding has been demonstrated. The practical is an onsite controlled exercise, not a commissioned repair, delivery or monster hunt. Only the existing licensure quest tracks the exam. Offer real contracts separately after actual licensing or an actual later request.'
    origins={
      'Akitsuhara — Town and Country':[
       ('Benitsuru Ward Local','You grew up among Benitsuru’s canal markets, crowded lanes and household gates. You know the practical rhythm of a capital neighborhood, from morning deliveries to festival preparations.','investigation'),
       ('Mizuhara Lakeside Upbringing','Your early life followed ferries, fish markets and changing lake weather around Mizuhara. You learned to judge a crossing and listen to people whose livelihood depends on the water.','survival'),
       ('Koganedai Castle-Town Upbringing','You grew up around Koganedai’s busy workshops, market terraces and household offices. Comparing workmanship and hearing competing prices became ordinary habits.','Trade'),
       ('Akitsuhara Farming Village','You grew up among shared irrigation, seasonal harvests and neighbors who noticed an unattended task. You learned to read the ground and work around weather.','survival'),
       ('Reed-Valley Childhood','You grew up among bamboo groves, mill paths and narrow river crossings. Quiet footing and attention to an obscured approach came from ordinary travel.','Perception'),
       ('Northern Pass Household','Your household made a living along Akitsuhara’s colder passes. Planning fuel, shelter and a return route mattered more than the appearance of an easy journey.','survival')],
      'Akitsuhara — Formative Communities':[
       ('Household Service Upbringing','You grew up around the practical work behind a territorial household: deliveries, formal visitors, records and rooms that had to be ready. You learned the uses and limits of courtesy.','Etiquette'),
       ('Dojo Neighborhood Upbringing','The sound of practice was part of your childhood. Watching corrections, cleaning a floor and helping with equipment taught you to notice how people move and learn.','Insight'),
       ('Shrine-Court Upbringing','You grew up near a working shrine and its stream of ordinary visitors. You learned how a ceremony, a private worry and a practical request can occupy the same courtyard.','Etiquette'),
       ('Road-Theatre Upbringing','You grew up among traveling stages, costume bundles and audiences that changed at every stop. Timing, listening and making a small performance carry became familiar skills.','performance')],
      'Mountain and Sky Communities':[
       ('Drakenspire Forge Neighborhood','You grew up among Drakenspire’s workshops and winter deliveries. You learned to compare a repair, a bargain and a piece of workmanship without mistaking ornament for quality.','Trade'),
       ('Drakenspire Caravan Upbringing','Your early life followed mountain supplies, snowbound delays and nights in shared lodges. You learned to prepare for the stretch between safe hearths.','survival'),
       ('Asterveil Canopy Household','You grew up among Asterveil’s household assembly, landing paths and shared gardens. Recognizing a neighbor’s concern and finding a workable agreement were everyday skills.','Insight'),
       ('Asterveil Field-Shelter Upbringing','You grew up around guides, conservatory work and careful journeys between sky-island shelters. You learned to notice a route’s changing conditions before committing to it.','Perception')]
    }
    category=w['traitCategories']['Origin & Upbringing']
    category['subcategories']=[{'name':'Established Backgrounds','traits':list(category['traits'])}]
    category['description']='Optionally choose one place or community that shaped your early life. Each background adds +1 to a useful skill; your present circumstances are yours to establish.'
    for group,rows in origins.items():
        names=[]
        for name,desc,skill in rows:
            assert name not in w['traits']
            w['traits'][name]={'name':name,'description':desc+f' Start with +1 {skill}.','traitNarrativeEffects':desc,'attributes':[],'skills':[{'skill':skill,'modifier':1}],'resources':[],'startingItems':[],'abilities':[],'unlockedBy':[],'excludedBy':[],'requirements':[]}
            names.append(name);category['traits'].append(name)
        category['subcategories'].append({'name':group,'traits':names})
    return additions
