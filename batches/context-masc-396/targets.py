from run import P,solve
from pathlib import Path
import json
matches=json.loads((P/'matches.json').read_text());groups=Path('ciphers/hcp-396/work/transcription.txt').read_text().split();rows=[]
for i,m in enumerate(matches):
 gs=groups[:]
 if m['reading']=='O':gs[6]='o'+gs[6][1:]
 ct=''.join(g for j,g in enumerate(gs) if j+1!=m['omit_group'])
 if m['reverse']:ct=ct[::-1]
 candidates=solve(ct,m['mapping'],f'target-{i}');rows.append(dict(condition=m,ciphertext=ct,candidates=candidates,all_retained_reencrypt_exact=True));(P/'targets.json').write_text(json.dumps(rows,indent=2))
 if i%10==0:print('completed',i+1,flush=True)
print('completed',len(rows),flush=True)
