from pathlib import Path
from collections import Counter
import json,subprocess
p=Path(__file__).resolve().parent
q={a:float(b) for a,b in (line.split() for line in (p/'ring-4grams.tsv').read_text().splitlines())}
def score(text):return sum(q.get(text[i:i+4],-4) for i in range(len(text)-3))
for m in (20,26,30):
 f=p/f'control-m{m}';key=json.loads((f/'key.json').read_text())
 (f/'known-output-mask-candidate.txt').write_text('0 '+','.join(map(str,key['output_positions']))+', '+','.join(map(str,key['active_holes']))+', '+str(key['active_phase_index'])+'\n')
 out=subprocess.check_output([str(p/'wheel_masc'),str(p),str(f/'ciphertext.txt'),str(p/'adjacent-distances.txt'),str(f/'known-output-mask-candidate.txt')],text=True)
 (f/'known-output-mask-result.txt').write_text(out);text=out.splitlines()[1].split()[1];plain=(f/'plaintext.txt').read_text().strip()
 r=dict(known_output_ring=True,known_mask_and_phase=True,length=385,exact_plaintext=text==plain,match_count=sum(a==b for a,b in zip(text,plain)),score=float(out.splitlines()[1].split()[0]),true_score=score(plain),substitution_mismatches=dict(Counter(a+'->'+b for a,b in zip(plain,text) if a!=b)))
 (f/'known-output-mask-verification.json').write_text(json.dumps(r,indent=2));print(m,r)
