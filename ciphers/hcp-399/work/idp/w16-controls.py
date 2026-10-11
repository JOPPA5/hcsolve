from pathlib import Path
import json,random
w=Path(__file__).resolve().parent;out=[]
for rec in json.loads(w.joinpath('controls.json').read_text()):
 if not rec['label'].endswith('240'):continue
 label=rec['label']+'-w16';s=rec['plaintext'];rng=random.Random(163994+label.startswith('heldout'));keys=[]
 for width in [16,17]:
  k=list(range(width));rng.shuffle(k);keys.append(k);s=''.join(s[c::width] for c in k)
 w.joinpath(label+'.txt').write_text(s+'\n');out.append(dict(label=label,plaintext=rec['plaintext'],keys=keys))
w.joinpath('controls-w16.json').write_text(json.dumps(out,indent=2))
