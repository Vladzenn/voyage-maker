"""Apply distinct local visual reads only to scenes not generated yet."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
jobs = json.loads((HERE / 'location-jobs.json').read_text(encoding='utf-8'))
saved = json.loads((HERE / 'location-files.json').read_text(encoding='utf-8'))
directions = dict(line.split('|', 1) for line in (HERE / 'art-directions.txt').read_text(encoding='utf-8').splitlines() if line.strip())
changed = []
for job in jobs:
    if job['id'] in saved or job['name'] not in directions:
        continue
    original = job['prompt']
    facts = original.split('Scene facts: ', 1)[1].split(' Location areas for context', 1)[0]
    job['visualRead'] = directions[job['name']]
    job['prompt'] = (f"Create one square 1:1 location establishing illustration of {job['name']} in Caelrath, Ardelis. "
                     f"{job['visualRead']} Scene facts: {facts} "
                     "Use our richly colored 2D fantasy-anime environment style: deliberate drawn shapes, painterly lighting, convincing depth and selective fine detail. "
                     "Caelrath is a wealthy city on connected mountain terraces above coastal water, with pale masonry, gold ornament and violet roof accents in its civic architecture. "
                     "Local materials and the specific palette above define this site. A skyline is optional and distant; interiors should remain interiors. "
                     "Compose around this site's own function and silhouette. Use a few relevant functional prop clusters and tiny secondary people only where public activity fits. "
                     "Keep the defining focal feature in the central 60% for narrow and wide crops. Subtle magical lamps may fit; no unsupported spectacular magical installation. "
                     "No named NPC, permanent boss, fighting, floating islands, readable text, map, UI, logo, watermark, photograph or 3D render. One finished PNG.")
    changed.append(job['id'])
(HERE / 'location-jobs.json').write_text(json.dumps(jobs, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'refinedUnstartedScenes': len(changed), 'first': changed[:2], 'last': changed[-2:]}))
