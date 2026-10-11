from scout import P, solve, enc, keys
from pathlib import Path
import json
rows=json.loads((P/'targets.json').read_text());prior={(r['cipher'],r['ciphertext']) for r in rows};added=[]
for n in [393,371,399]:
 groups=Path(f'ciphers/hcp-{n}/work/transcription.txt').read_text().lower().split()
 assert groups[0].isdigit();header=groups.pop(0)
 raw=''.join(groups);variants=[('body-only',raw)]
 if n==393:variants += [(f'body-omit-{i+1}',''.join(g for j,g in enumerate(groups) if j!=i)) for i in range(len(groups))]
 for tag,ct in variants:
  for rev in [False,True]:
   s=ct[::-1] if rev else ct
   if (n,s) in prior:continue
   best=solve(s)
   for c in best:
    re=c['plaintext']
    for k in c['physical_labels']:re=enc(re,k)
    assert re==s
   added.append(dict(cipher=n,variant=tag,excluded_unencrypted_numeric_header=header,reverse=rev,ciphertext=s,tested=len(keys),candidates=best,whole_reencryption_exact=True))
(P/'body-targets.json').write_text(json.dumps(added,indent=2));print('new body cases',len(added))
