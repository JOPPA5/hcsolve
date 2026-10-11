from pathlib import Path
import json
from exact_cover import solve
P=Path(__file__).parent;src=json.loads((P/'aligned-equal-control.json').read_text());c=src['ciphertext'];chosen=[i for i,x in enumerate(c) if x!='r'][:3];damaged=list(c)
for i in chosen:damaged[i]='z'
out=solve(src['plaintext'][:-1]+'?',''.join(damaged),[16,16,16],20000,3,[11,11,11]);out.update(mode='independent_aligned_equal_3_error_unknown_filler_control',alignments=[11,11,11],true_keys=src['planted_keys'],keys_equal_planted=out.get('keys')==src['planted_keys'],original_ciphertext=c,damaged_ciphertext=''.join(damaged),true_error_positions=chosen,undamaged_re_encryption_exact=out.get('predicted_ciphertext')==c);(P/'aligned-equal-error-control.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
