from pathlib import Path
from collections import Counter
import json
p=Path(__file__).parent

def stats(s):
 c=Counter(s);n=len(s)
 return {'n':n,'counts':dict(sorted(c.items())), 'IC':sum(v*(v-1) for v in c.values())/(n*(n-1)), 'repeated_bigrams':{k:v for k,v in Counter(s[i:i+2] for i in range(n-1)).items() if v>1},'period_column_IC':{str(w):[sum(v*(v-1) for v in Counter(s[i::w]).values())/(len(s[i::w])*(len(s[i::w])-1)) if len(s[i::w])>1 else None for i in range(w)] for w in range(2,7)}}

def mono_matches(c,t):
 return all((c[i]==c[j])==(t[i]==t[j]) for i in range(len(t)) for j in range(i))
# Test functions with an explicit artificial control; these are NOT target solutions.
assert mono_matches('qweqq','abcaa')
assert not mono_matches('qweqq','abcca')
cribs=['ziadameopakovanie','opakovanie','telegram','predoslehotelegramu','kluc','sifra']
result={}
for f in sorted(p.glob('target-*.txt')):
 if '-result' in f.name:continue
 s=f.read_text().strip()
 d=stats(s)
 d['mono_crib_compatible_offsets']={t:[i for i in range(len(s)-len(t)+1) if mono_matches(s[i:i+len(t)],t)] for t in cribs}
 result[f.name]=d
(p/'structure.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:{a:v for a,v in d.items() if a!='period_column_IC'} for k,d in result.items()},indent=2))
