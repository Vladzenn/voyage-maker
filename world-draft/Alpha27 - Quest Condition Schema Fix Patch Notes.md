# Alpha27 — Quest Completion Condition Schema Fix

Use **GlowhavenAlpha27 - Quest Condition Schema Fix.json**, identical to WorldAlpha - World.json. It supersedes the Alpha25/Alpha26 full exports for importing. If replacing only the Quests section, use the updated WorldAlpha - Quests.json plain map.

## Cause and repair

The eight first-morning and instructor-preparation quests added in Alpha25 incorrectly used plain string completionCondition values. Studio requires a typed object. Each is now `{ "type": "story", "query": "the existing completion text" }`. The query text itself is unchanged.

The error was in the authoring code and local validation: the earlier checks confirmed that a completion description existed but did not check its object shape. Consequently, a passing local report did not mean a successful Studio import. The construction template now emits the typed objects, and both affected authoring validators include the reusable typed-condition schema guard.

All 116 current quests were checked. Sixty-eight have correctly typed story conditions; the other forty-eight intentionally omit the optional field and retain their existing progression mechanisms. No additional invalid completion conditions were found. Twelve regression fixtures cover accepted story/event objects, omitted conditions and rejected string/null/list/malformed objects. The actual Alpha25 and Alpha26 files are regression inputs and correctly fail on eight values.

## Preserved content

Exactly eight completionCondition values changed from strings to their story-object wrappers. A reverse transformation reproduces the previous complete world exactly. All uploaded image URLs/crops, coordinates, AuthorSeeds, local danger guidance, first-day prose, appearance traits, abilities, NPC stats, quests' prose/objectives/rewards, triggers and travel settings are unchanged. All twenty-one standalone section maps match the full world.

The exact schema is confirmed by the user's Studio validation error and the [community quest reference](https://wiki.unofficial.voyage/world/quests#completioncondition). No live Studio import or gameplay test was performed by this repair. Reimport the corrected full file and check the save in Studio; local shape validation is not a substitute for that runtime check.
