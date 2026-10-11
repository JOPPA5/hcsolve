import json,subprocess,random
from pathlib import Path
w=Path(__file__).resolve().parent
root=w.parents[1]
def encode(s,k,n):
 pivot=k.index(n);aligned=k[pivot:]+k[:pivot]
 return ''.join(s[c::len(k)] for _,c in sorted((v,c) for c,v in enumerate(aligned)))
def check(keys,msgs,label):
 (w/'validation.input.txt').write_text(''.join(f'{n} {c}\n' for n,c,p in msgs))
 (w/'validation.keys.txt').write_text(''.join(' '.join(map(str,k))+'\n' for k in keys))
 out=subprocess.check_output([str(w/'joint'),str(root/'batches/scoring-sol61'),str(w/'validation.input.txt'),str(w/'validation.keys.txt'),'-1','0','0'],text=True)
 decoded=[s[len('verified '):] for s in out.splitlines() if s.startswith('verified ')]
 assert decoded==[p for n,c,p in msgs],label
for item in json.loads((w/'controls.json').read_text()):
 check(item['keys'],[(m['alignment'],m['ciphertext'],m['plaintext']) for m in item['messages']],item['label'])
r=random.Random(71395)
for i in range(12):
 keys=[]
 for width in (21,19,20):
  k=list(range(1,width+1));r.shuffle(k);keys.append(k)
 msgs=[]
 for length in (50,55,199,200,245,250):
  p=''.join(r.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(length));n=r.randint(1,19);c=p
  for k in keys:c=encode(c,k,n)
  msgs.append((n,c,p))
 check(keys,msgs,str(i))
(w/'inverse-validation.json').write_text(json.dumps({'independent_cpp_inverse':'PASS','heldout_pairs':2,'random_daily_key_sets':12,'random_messages':72,'lengths':[50,55,199,200,245,250],'python_encoder':'direct sorted rank column slicing','cpp_inverse':'rank assigned physical columns then row interleaving'},indent=2)+'\n')
print('Independent Python encoder / C++ inverse: 2 pairs and 72 random messages exact')
