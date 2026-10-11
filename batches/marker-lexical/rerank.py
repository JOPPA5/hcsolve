"""Blind all-one-swap/all-three-cycle plaintext-letter neighborhood.

The Slovak dictionary is frozen independently; X/Q conventions are conditional.
No true control plaintext or planted key participates in ranking.
"""
from pathlib import Path
from functools import lru_cache
from itertools import combinations
import json, math, sys

p=Path(__file__).parent
weights={}
for line in Path('batches/scoring-sol61/frequency/words.tsv').read_text().splitlines():
    w,f=line.split('\t'); f=int(f)
    if 1<=len(w)<=25:
        weights[w]=3*len(w)-4+min(5,math.log(1+f))

@lru_cache(maxsize=200000)
def segment(s):
    d=[-1e9]*(len(s)+1);d[0]=0
    for i in range(len(s)):
        d[i+1]=max(d[i+1],d[i]-8)
        for j in range(i+1,min(len(s),i+25)+1):
            w=weights.get(s[i:j])
            if w is not None:d[j]=max(d[j],d[i]+w)
    return d[-1]

def score(s):
    total=0
    for part in s.split('x'):
        pieces=part.split('q')
        if len(pieces)%2==0:total-=25 # unmatched proper-name delimiter
        for i,chunk in enumerate(pieces):
            if i%2:
                total+=3*len(chunk)-4 if 1<=len(chunk)<=25 else -20-8*len(chunk)
            else:total+=segment(chunk)
    return total

source=Path(sys.argv[1]); obj=json.loads(source.read_text()); text=obj['plaintext']
rows=[dict(change=[],score=score(text),plaintext=text)]
alphabet='abcdefghijklmnopqrstuvwxyz'
for a,b in combinations(alphabet,2):
    s=text.translate(str.maketrans(a+b,b+a));rows.append(dict(change=[a,b],score=score(s),plaintext=s))
for a,b,c in combinations(alphabet,3):
    for v in [b+c+a,c+a+b]:
        s=text.translate(str.maketrans(a+b+c,v)); rows.append(dict(change=[a,b,c,v],score=score(s),plaintext=s))
rows.sort(key=lambda r:r['score'],reverse=True)
out=dict(source=str(source),method='all325 swaps and5200 3-cycles plus identity; frozen dictionary DP, conditional X/Q boundaries',truth_used_for_ranking=False,top=rows[:25],candidate_count=len(rows))
if 'planted' in obj:
    truth=obj['planted']['plaintext']; ranks=[i for i,r in enumerate(rows) if r['plaintext']==truth]
    out['diagnostic_truth_rank_after_ranking']=ranks
    out['diagnostic_exact_best']=rows[0]['plaintext']==truth
dest=p/(source.parent.parent.name+'-reranked.json');dest.write_text(json.dumps(out,indent=2))
print(dest, out.get('diagnostic_exact_best'),out.get('diagnostic_truth_rank_after_ranking'),rows[0],flush=True)
