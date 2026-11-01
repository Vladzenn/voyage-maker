if(!here){skip=true;}else{
 const due=Object.keys(c.care).find(k=>solo&&c.care[k].owner===names[0]);
 if(due){delete c.care[due];say('The accepted post-bout care/check-up/rest is complete. Use the actual condition: an unharmed person has no invented injury; depleted Mana or Stamina can be addressed through appropriate rest. Apply only recovery supported by the actual care, without duplicate item grants. Preparation may continue without an exact resource-percentage test. Let the player choose when to fight again.');}
 else skip=true;mirror();
}

