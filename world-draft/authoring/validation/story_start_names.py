"""Studio-observed story-start identity guard.

Current Studio rejects a different key/name even where community documentation
suggests otherwise. Keep the native Write Your Own identity intact.
"""

def story_start_name_errors(world):
 return [f'storyStarts.{key}.name: key {key!r} != name {value.get("name")!r}'
         for key,value in world.get('storyStarts',{}).items() if key!=value.get('name')]

def normalize_story_start_names(world):
 starts=world['storyStarts'];mapping={}
 for key,value in starts.items():
  target='Write Your Own' if key=='Write Your Own' else value['name']
  if target!=key:mapping[key]=target
 targets=[mapping.get(key,key) for key in starts]
 if len(set(targets))!=len(targets):raise ValueError('Story start rename would create duplicate IDs')
 if 'Write Your Own' in starts:starts['Write Your Own']['name']='Write Your Own'
 world['storyStarts']={mapping.get(key,key):value for key,value in starts.items()}
 changed=[]
 def visit(obj,path=''):
  if isinstance(obj,dict):
   if obj.get('type')=='story-start' and obj.get('value') in mapping:
    obj['value']=mapping[obj['value']];changed.append(path+'/value')
   for key,value in obj.items():visit(value,path+'/'+str(key))
  elif isinstance(obj,list):
   for index,value in enumerate(obj):visit(value,path+'/'+str(index))
 visit(world)
 for name,trait in world.get('traits',{}).items():
  for key in ['unlockedBy','excludedBy']:
   for i,value in enumerate(trait.get(key,[])):
    if value in mapping:trait[key][i]=mapping[value];changed.append(f'/traits/{name}/{key}/{i}')
 assert not story_start_name_errors(world)
 return {'renamedIDs':mapping,'updatedReferences':changed}
