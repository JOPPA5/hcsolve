from pathlib import Path
import json,random
p=Path(__file__).resolve().parent;rng=random.Random(36320020)
base=json.loads((p.parent/'controls.json').read_text())['control-19']['plaintext']
plain=base+'kporo';assert len(plain)==400
controls={}
for i in range(2):
 keys=[];ct=plain
 for _ in range(2):
  key=list(range(20));rng.shuffle(key);keys.append(key);ct=''.join(ct[j::20] for j in key)
 (p/f'control-{i}.txt').write_text(ct+'\n');controls[str(i)]={'plaintext':plain,'keys':keys,'source':'earlier synthetic395-letter control continued by5 letters, not historical text, not inserted into model'}
(p/'controls.json').write_text(json.dumps(controls,indent=2)+'\n')
