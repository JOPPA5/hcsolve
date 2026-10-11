from pathlib import Path
from collections import Counter
from itertools import permutations
import heapq, json
root=Path(__file__).resolve().parent
s=''.join((root/'transcription.txt').read_text().split())
assert len(s)==55
words='som sme ste nie pri pre pro ako pod nad vam vas nas jeho jej aby bude budu bolo bola boli ktory ktore ktoru sprava spravy prosim oznamujem ziadam dnes zajtra dna potvrdzujem prijatie prosime opakujte znovu povodnom zneni'.split()
def score(t):return sum(len(w)**2*t.count(w) for w in words)
def decrypt(ct,key):
    # key lists original column indices in ciphertext emission order.
    n=len(ct);width=len(key);q,r=divmod(n,width);cols={};offset=0
    for j in key:
        h=q+(j<r);cols[j]=ct[offset:offset+h];offset+=h
    return ''.join(cols[j][i] for i in range(q+1) for j in range(width) if i<len(cols[j]))
def stats(t):
    c=Counter(t);n=len(t)
    return dict(length=n,counts=dict(sorted(c.items())),ic=sum(v*(v-1) for v in c.values())/(n*(n-1)))
result={'transcription':s,'stats':stats(s),'note':'Scores are transparent substring heuristics, not probabilities. Candidate strings are NOT proposed plaintexts. Group7 first letter read C; O variant also checked.','tests':[]}
for variant in ['c','o']:
    text=s[:30]+variant+s[31:]
    for omit in [None,7]: # zero-based group8 is plausible indicator, but not established
        ct=text if omit is None else text[:5*omit]+text[5*omit+5:]
        top=[];tested=0
        for width in range(2,9):
            for key in permutations(range(width)):
                t=decrypt(ct,key);tested+=1
                item=(score(t),width,key,t)
                if len(top)<10:heapq.heappush(top,item)
                elif item>top[0]:heapq.heapreplace(top,item)
        result['tests'].append(dict(group7_initial=variant,omitted_group=None if omit is None else omit+1,stats=stats(ct),tested_keys=tested,top_candidates=sorted(top,reverse=True)))
# Unkeyed rectangular/irregular routes for every single-group omission and both readings.
routes=[]
for variant in ['c','o']:
    text=s[:30]+variant+s[31:]
    for omit in range(-1,11):
        ct=text if omit<0 else text[:5*omit]+text[5*omit+5:]
        for width in range(2,len(ct)):
            for rev in [False,True]:
                x=ct[::-1] if rev else ct
                t=''.join(x[j::width] for j in range(width))
                routes.append((score(t),variant,omit+1,width,rev,t))
result['route_tests']=len(routes)
result['top_routes']=sorted(routes,reverse=True)[:20]
(root/'analysis.json').write_text(json.dumps(result,indent=2)+'\n')
print('Written analysis.json; single-columnar keys tested',sum(x['tested_keys'] for x in result['tests']),'routes',len(routes))
for x in result['tests']: print(x['group7_initial'],x['omitted_group'],x['stats'],x['top_candidates'][:3])
