"""Validate Voyage's typed quest completionCondition union; absence is valid."""
def condition_errors(world):
 errors=[]
 for party_key,party in world.get('parties',{}).items():
  for quest_key,quest in party.get('quests',{}).items():
   if 'completionCondition' not in quest:continue
   value=quest['completionCondition'];path=f'parties[{party_key!r}].quests[{quest_key!r}].completionCondition'
   if not isinstance(value,dict):errors.append(path+': expected a typed object');continue
   kind=value.get('type')
   if kind=='story':
    if not isinstance(value.get('query'),str):errors.append(path+': story requires string query')
   elif kind=='narrative-event-completed':
    if not isinstance(value.get('eventId'),str):errors.append(path+': narrative event requires string eventId')
   else:errors.append(path+': unsupported condition type '+repr(kind))
 return errors
