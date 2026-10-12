from pathlib import Path
from itertools import permutations,product
import random,json
from engine import solve
B=Path(__file__).resolve().parent;base='abcuvd';widths=[2,3,4];rng=random.Random(364617180);records=[];enumerated=0
def independent(p,key):return ''.join(p[i]for col in key for i in range(col,len(p),len(key)))
for n in[1,2]:
 orders=[[k for k in permutations(range(w))if k.index(0)==n-1]for w in widths];possible={}
 for insertion in range(7):
  p=base[:insertion]+'x'+base[insertion:]
  for keys in product(*orders):
   c=p
   for key in keys:c=independent(c,key)
   possible.setdefault(c,[]).append((p,keys));enumerated+=1
 for case in range(8):
  c=rng.choice(sorted(possible))if case<4 else''.join(rng.sample(list(base+'x'),7));a=list(c);u=c.index('u');v=c.index('v');a[u],a[v]=a[v],a[u];variants=[c,''.join(a)];expected=any(v in possible for v in variants)
  r=solve('?'*7,c,widths,5000,alignments=[n]*3,backend='eager',insert_x_template=base,cipher_variants=variants)
  assert r['status']!='unknown'and(r['status']=='sat')==expected
  if r['status']=='sat':
   pred=r['conditional_plaintext']
   for key in r['keys']:pred=independent(pred,key)
   assert pred==r['selected_ciphertext_variant']
  records.append(dict(alignment=n,variants=variants,enumerated_expected=expected,result=r))
(B/'small-audit.json').write_text(json.dumps(dict(enumerated_insertion_keysets=enumerated,cases=records),indent=2)+'\n');print('16 cases agree with',enumerated,'direct insertion/keysets')
