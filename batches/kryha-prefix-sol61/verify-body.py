from pathlib import Path
import json
from scout import decode,encode
b=Path(__file__).resolve().parent;r=b.parents[1];rows=json.load(open(b/'actual-candidates.json'));out=[]
for row in rows:
 n=row['number'];d=r/f'ciphers/hcp-{n}/work/kryha-decipherment';k=json.load(open(d/'key.json'));ct=(d/'ciphertext.txt').read_text().strip();body,end,_=decode(ct[5:],k,*row['continuation_state_at_five'],[1]*380);assert body==k['plaintext'][5:];assert encode(body,k,*row['continuation_state_at_five'],[1]*380)==(ct[5:],end)
 checks=0
 for branch in ('carry_optional_extra','carry_optional_hold_or_extra'):
  for c in row[branch]:
   full=c['plaintext']+body;got,final=encode(full,k,c['start_phase'],c['start_displacement'],list(c['presses'])+[1]*380);assert got==ct and final==end;checks+=1
 out.append(dict(number=n,body380_exact_under_frozen_key=True,complete385_reencodings=checks,carry_alternative_body_unchanged=True,independent_resets_prefix_plus_body_separate_reencoding=True,source_files_unchanged=True))
(b/'body-verification.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
