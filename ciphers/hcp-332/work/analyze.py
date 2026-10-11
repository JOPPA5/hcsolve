from pathlib import Path
from collections import Counter
import math,json,subprocess
p=Path(__file__).parent
q={a:float(b) for a,b in (x.split() for x in (p/'quadgrams.tsv').read_text().splitlines())}
def score(s):return sum(q.get(s[i:i+4],-4) for i in range(len(s)-3))
report=[]
for f in sorted(p.glob('target-*.txt')):
 if '-result' in f.name:continue
 s=f.read_text();c=Counter(s);n=len(s);cand=[]
 for rev in [False,True]:
  x=s[::-1] if rev else s
  for a in range(26):
   if math.gcd(a,26)!=1:continue
   ai=pow(a,-1,26)
   for b in range(26):
    pt=''.join(chr(97+ai*(ord(v)-97-b)%26) for v in x);cand.append({'score':score(pt),'a':a,'b':b,'reverse':rev,'candidate':pt})
 out=subprocess.check_output([str(p/'vigenere'),str(p),str(f)],text=True)
 (p/(f.stem+'-result.txt')).write_text(out)
 report.append({'variant':f.name,'length':n,'IC':sum(v*(v-1) for v in c.values())/(n*(n-1)), 'affine_test_count':len(cand),'affine_top':sorted(cand,key=lambda x:x['score'],reverse=True)[:5]})
(p/'analysis.json').write_text(json.dumps(report,indent=2))
truth=(p/'control-plain.txt').read_text();row=next(l.split() for l in (p/'control-results.txt').read_text().splitlines() if l.split()[0]=='3');print('Control period3 exact key',row[2]=='7,13,2,','exact plaintext',row[3]==truth)
for r in report:print(r['variant'],r['length'],r['IC'],r['affine_top'][0])
