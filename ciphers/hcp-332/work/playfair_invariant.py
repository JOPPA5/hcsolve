"""Conditional ordinary Playfair check, not a general fractionation exclusion."""
from pathlib import Path
import json
p=Path(__file__).resolve().parent
# Independently planted control via ordinary 5x5 square, I/J merged.
alphabet='abcdefghiklmnopqrstuvwxyz'
pos={c:divmod(i,5) for i,c in enumerate(alphabet)}
def encrypt(a,b):
 ra,ca=pos[a];rb,cb=pos[b]
 if ra==rb:return alphabet[5*ra+(ca+1)%5]+alphabet[5*rb+(cb+1)%5]
 if ca==cb:return alphabet[5*((ra+1)%5)+ca]+alphabet[5*((rb+1)%5)+cb]
 return alphabet[5*ra+cb]+alphabet[5*rb+ca]
# Exhaust every distinct-input pair: an ordinary Playfair permutation never
# emits the same symbol twice in one pair. Real plaintext repeats split first.
assert all(encrypt(a,b)[0]!=encrypt(a,b)[1] for a in alphabet for b in alphabet if a!=b)
assert encrypt('h','i')=='ik'
result={'control_pairs_checked':25*24,'variants':{}}
for f in sorted(p.glob('target-*.txt')):
 if '-result' in f.name:continue
 s=f.read_text().strip()
 result['variants'][f.name]={'even_length':len(s)%2==0,'doubled_pairs_zero_based':[(i,s[i:i+2]) for i in range(0,len(s)-1,2) if s[i]==s[i+1]],'both_i_and_j_present':'i' in s and 'j' in s}
(p/'playfair-invariant.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
