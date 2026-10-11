"""Test the visible proposed reply as a conditional single-columnar crib.
No transcription is corrected to agree with the quote. Up to three substitution
errors are tolerated mathematically; this is not an assertion that they occurred.
"""
from pathlib import Path
from functools import lru_cache
from collections import Counter
import json,random
P=Path(__file__).parent
groups=(P/'transcription.txt').read_text().split()
quote='Nelustitelne.Neudal si cislo pred textom.Vid bod tri pokynov.Uved cislo.'
plain=''.join(c.lower() for c in quote if c.isalpha())
prepared=''.join(c.lower() if c.isalpha() else 'x' if c=='.' else '' for c in quote)+'?'
assert len(plain)==60 and len(prepared)==65

def enc(p,k):return ''.join(p[i::len(k)] for i in k)
def solve(c,p,w,budget=3):
 q,r=divmod(len(c),w);full=(1<<w)-1;nodes=0;limited=False
 cols=[p[i::w] for i in range(w)]
 @lru_cache(None)
 def dfs(mask,off,left):
  nonlocal nodes,limited
  nodes+=1
  if nodes>150000:limited=True;return None
  if mask==full:return ()
  candidates=[];seen=set()
  for col in range(w):
   if mask>>col&1:continue
   expected=cols[col]
   if expected in seen:continue
   seen.add(expected)
   chunk=c[off:off+len(expected)]
   cost=sum(a!=b and b!='?' for a,b in zip(chunk,expected))
   if cost<=left:candidates.append((cost,col))
  for cost,col in sorted(candidates):
   tail=dfs(mask|1<<col,off+len(cols[col]),left-cost)
   if tail is not None:return (col,)+tail
  return None
 key=dfs(0,0,budget)
 return {'key':key,'visited_states':nodes,'complete':not limited}
# A new fixed independent key; three injected errors. Match the same target length.
rng=random.Random(36461);key=list(range(21));rng.shuffle(key)
control_plain=prepared.replace('?','z');cc=list(enc(control_plain,key))
for pos in [7,29,50]:cc[pos]=chr((ord(cc[pos])-97+7)%26+97)
control=solve(''.join(cc),prepared,21)
assert control['key'] is not None,control
control['exact_original_key']=list(control['key'])==key
control['injected_substitutions']=3
# All one-group removals, both transport directions, widths2..22. This tests one
# full quoted plaintext preparation, NOT arbitrary variants or triple transposition.
cases=[]
for omit in range(len(groups)):
 c=''.join(g for i,g in enumerate(groups) if i!=omit)
 for reverse in [False,True]:
  cc=c[::-1] if reverse else c
  for w in range(2,23):
   result=solve(cc,prepared,w)
   cases.append(dict(omit_group=omit+1,width=w,reverse=reverse,**result))
out={'status':'unresolved','quote_origin':'visible unencrypted proposed outgoing reply on the same source scan; not a decipherment',
'quote':quote,'plain_letters':len(plain),'prepared':prepared,'literal_cipher_letters':sum(map(len,groups)),
'assumptions':['single ordinary irregular columnar transposition','one five-letter indicator removed','four sentence-end X characters','one final unknown filler','at most three ciphertext substitution errors'],
'raw_inventory_difference':{'cipher_extra':dict(Counter(''.join(groups))-Counter(plain)), 'quote_extra':dict(Counter(plain)-Counter(''.join(groups)))},
'control':control,'cases':cases}
(P/'known_quote_results.json').write_text(json.dumps(out,indent=2)+'\n')
print('control',control)
print('target_cases',len(cases),'complete',sum(x['complete'] for x in cases),'hits',[x for x in cases if x['key'] is not None])
