# Rebirth implementation record

The approved merge base is the canonical Universal Fishing world and its 4 November Studio hotfix, world commit `48445de`, file SHA-256 `a84f4a5e898d6bd85f35b96b354523fe36a0afaeea556b8c827f261d22613200`. GitHub and desktop were at `364fca2` when this build began. The author explicitly confirmed the local world as the base on 5 November.

The planning brief remains the design reference. The author's implementation answers supersede it in these places.

- Earliest delegation is 200 completed turns after the opening, an established ordinary life, and a calm town scene. A trip, fight or expedition delays it.
- Support multiplayer personal ambushes through the actual `Summoned one` bearer. Companions can participate in the shared encounter.
- Preserve Vladimir's immortality. His canonical full name is `Valkazathoth'dmir`; ordinary address is Vladimir.
- Finish this build with evidence of the local relay and the impending second summoning. Ardelis's explorable nation and the controlled rival's deployment belong to the later Ardelis stage.
- Eight pocket-realm destinations, stable addresses and a fixed return.
- New principal portraits are part of this build.
- The port and its region layout are deferred. New local residents begin in Brookmeadow and can be relocated later.
- Retain the court investigator's independent evidence route if Vladimir's invitation is declined.
- Beastfae are a distinct rare ancestry. The rejected Force/Intuition package is replaced by a modest package chosen during implementation.

Run `build.py` against the approved base to produce a separate candidate. It refuses a different base unless explicitly supplied. The implementation records exact changes and preservation hashes in `review.json`. The canonical file is installed after the candidate passes structural and feature checks.

Local fixtures supply semantic answers. They verify emitted effects and state, and do not establish live Voyage recognition, multiplayer scheduling, media generation or Studio acceptance. The development notes list the live checks.
