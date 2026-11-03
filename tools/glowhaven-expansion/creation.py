"""The two explicitly requested foundation/experience corrections."""
import copy
def apply(w):
    t=w['traits']['Physical Foundations']
    t['skills']=[{'skill':k,'modifier':1} for k in ['Force Combat','Finesse Combat','Guarded Combat']]
    t['description']=t['description'].replace('+1 Force Combat and +1 Finesse Combat','+1 Force Combat, +1 Finesse Combat and +1 Guarded Combat')
    t['traitNarrativeEffects']=t['description']
    c=w['traitCategories']['Starting Magical Study']
    c['description']=c['description'].replace('+1 Force Combat and +1 Finesse Combat','+1 Force Combat, +1 Finesse Combat and +1 Guarded Combat')
    name='Self-Taught Spell Experimenter';t=copy.deepcopy(w['traits']['Veteran Infantry Soldier'])
    t.update(name=name,description='Before formal instruction, you spent spare evenings taking simple spells apart, changing one detail and finding out why the result misbehaved. You learned to keep experiments small and notice which change mattered. Start with +1 Spellcraft.',traitNarrativeEffects='You have experience with small personal spell experiments and the patience to test one change at a time. This is practical familiarity, not an academic qualification or a ready-made spell.',skills=[{'skill':'spellcraft','modifier':1}])
    w['traits'][name]=t;c=w['traitCategories']['Past Experience']
    if name not in c['traits']:c['traits'].append(name)
    if not any(g['name']=='Study and Experiment' for g in c['subcategories']):c['subcategories'].append({'name':'Study and Experiment','traits':[name]})

