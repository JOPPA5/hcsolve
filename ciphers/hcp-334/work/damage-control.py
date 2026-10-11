from pathlib import Path
import random,json
p=Path(__file__).parent
plain=(p/'control-vig-plain.txt').read_text();rng=random.Random(334)
def enc(s,k):return ''.join(s[c::len(k)] for c in k)
def dec(s,k):
 n=len(s);w=len(k);out=['']*n;at=0
 for c in k:
  for r in range(n//w+(c<n%w)):out[r*w+c]=s[at];at+=1
 return ''.join(out)
keys=[];ct=plain
for w in [19,17,22]:
 k=list(range(w));rng.shuffle(k);keys.append(k);ct=enc(ct,k)
def decrypt(s):
 for k in reversed(keys):s=dec(s,k)
 return s
assert decrypt(ct)==plain
masked=''.join('?' if i in [70,94] else c for i,c in enumerate(ct));out=decrypt(masked);compact=decrypt(masked.replace('?',''))
report={'description':'Synthetic triple-columnar control, not identification of target', 'length':150,'erasure_positions_zero_based':[70,94], 'correct_known_positions_with_erasures':sum(a==b for a,b in zip(out,plain) if a!='?'),'known_positions':148,'uncertain_plain_positions_zero_based':[i for i,c in enumerate(out) if c=='?'],'compact_naive_same_index_matches':sum(a==b for a,b in zip(compact,plain)),'compact_length':len(compact),'compact_comparison_note':'Naive same-index comparison to first148 plaintext positions; demonstrates changed grid dimensions, not cryptanalytic impossibility','keys':keys}
print(json.dumps(report,indent=2))
