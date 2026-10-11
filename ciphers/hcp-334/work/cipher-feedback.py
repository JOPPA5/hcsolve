"""Explicit finite ciphertext-feedback recurrences; initial key prefix remains unknown."""
from pathlib import Path
import json
p=Path(__file__).parent
q={a:float(b) for a,b in (l.split() for l in (p/'quadgrams.tsv').read_text().splitlines())}
def decrypt_tail(s,lag,family):
 out=['?']*lag
 for i in range(lag,len(s)):
  if '?' in (s[i],s[i-lag]):out.append('?');continue
  c=ord(s[i])-97;k=ord(s[i-lag])-97
  v=(c-k)%26 if family=='subtract' else (k-c)%26 if family=='reverse-subtract' else (c+k)%26
  out.append(chr(97+v))
 return ''.join(out)
def score(s):
 a=[q.get(s[i:i+4],-4.) for i in range(len(s)-3) if '?' not in s[i:i+4]]
 return sum(a)/len(a) if a else -999.
plain=(p/'control-vig-plain.txt').read_text().strip();controls=[]
for family in ('subtract','reverse-subtract','add'):
 for lag in (9,15):
  ct=[]
  for i,x in enumerate(plain):
   k=(7*i+3)%26 if i<lag else ord(ct[i-lag])-97;c=ord(x)-97
   v=(c+k)%26 if family=='subtract' else (k-c)%26 if family=='reverse-subtract' else (c-k)%26
   ct.append(chr(97+v))
  ct=''.join(ct);damaged=ct[:70]+'?'+ct[71:94]+'?'+ct[95:];recovered=decrypt_tail(damaged,lag,family)
  expected_known=[i for i,c in enumerate(recovered) if c!='?'];assert all(recovered[i]==plain[i] for i in expected_known)
  controls.append({'family':family,'lag':lag,'cipher':damaged,'recovered_tail':recovered,'known_positions':len(expected_known),'exact_known_tail':True,'score':score(recovered)})
results=[]
for off in range(5):
 ct=(p/f'target-phase-{off}.txt').read_text().strip()
 for reverse in (False,True):
  s=ct[::-1] if reverse else ct
  for family in ('subtract','reverse-subtract','add'):
   for lag in range(1,33):
    tail=decrypt_tail(s,lag,family);results.append({'gap_offset':off,'reverse':reverse,'family':family,'lag':lag,'tail':tail,'score':score(tail)})
report={'description':'C_i=P_i+C_(i-lag), C_i=C_(i-lag)-P_i, or C_i=P_i-C_(i-lag), mod26. Initial key prefix and consequences of erasures are left unknown, not invented.','controls':controls,'target_cases':len(results),'targets':sorted(results,key=lambda r:r['score'],reverse=True)}
(p/'cipher-feedback-results.json').write_text(json.dumps(report,indent=2)+'\n');print('controls',len(controls),'target cases',len(results));print(json.dumps(report['targets'][:5],indent=2))
