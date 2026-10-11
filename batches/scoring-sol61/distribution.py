from pathlib import Path
from collections import Counter
import json,unicodedata,statistics
p=Path(__file__).resolve().parent

def norm(w):return ''.join(c for c in unicodedata.normalize('NFD',w.lower().replace('ß','ss')) if 'a'<=c<='z')
def metrics(s):
 c=Counter(s);n=len(s)
 return sum(v*(v-1) for v in c.values())/(n*(n-1)),len(c)
result={}
for lang,f in [('sk',Path('ciphers/hcp-393/work/sk_snk-ud-train.conllu')),('de',p/'german/source/de_gsd-ud-train.conllu')]:
 sentences=[norm(l[9:]) for l in f.read_text().splitlines() if l.startswith('# text = ')]
 result[lang]={}
 for n in [40,43]:
  windows=[metrics(s[i:i+n]) for s in sentences for i in range(0,len(s)-n+1,5)]
  ics=sorted(x[0] for x in windows);distinct=[x[1] for x in windows]
  target=Path(f'ciphers/hcp-332/work/target-o-{n}.txt').read_text();ti,td=metrics(target)
  result[lang][n]={'window_count':len(windows),'stride':5,'IC_median':statistics.median(ics),'IC_5_percentile':ics[len(ics)//20],'IC_95_percentile':ics[len(ics)*19//20],'distinct_median':statistics.median(distinct),'target_IC':ti,'target_distinct':td,'fraction_IC_at_most_target':sum(i<=ti for i,d in windows)/len(windows),'fraction_distinct_at_least_target':sum(d>=td for i,d in windows)/len(windows),'fraction_joint':sum(i<=ti and d>=td for i,d in windows)/len(windows)}
(p/'distribution.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
