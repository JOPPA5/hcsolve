from pathlib import Path
from collections import Counter
import unicodedata,json,random
p=Path(__file__).resolve().parent

def norm(w):return ''.join(c for c in unicodedata.normalize('NFD',w.lower().replace('ß','ss')) if 'a'<=c<='z')
def m(s):
 c=Counter(s);return sum(v*(v-1) for v in c.values())/(len(s)*(len(s)-1)),len(c)
target=Path('ciphers/hcp-332/work/target-o-40.txt').read_text();ic,nd=m(target)
candidates=[];allwindows=[]
for l in (p/'source/de_gsd-ud-test.conllu').read_text().splitlines():
 if l.startswith('# sent_id = '):sid=l[12:]
 if not l.startswith('# text = '):continue
 raw=l[9:];s=norm(raw)
 for i in range(len(s)-39):
  x=s[i:i+40];ci,cd=m(x);allwindows.append((ci,cd))
  if ci<=ic and cd>=nd:candidates.append((sid,i,x,ci,cd,raw))
if not candidates:raise SystemExit('No sufficiently flat held-out window; no fabricated control.')
r=random.Random(927012);sid,offset,plain,ci,cd,raw=r.choice(candidates);alpha=list('abcdefghijklmnopqrstuvwxyz');r.shuffle(alpha)
(p/'flat40-plain.txt').write_text(plain);(p/'flat40-key.txt').write_text(''.join(alpha));(p/'flat40-cipher.txt').write_text(''.join(alpha[ord(c)-97] for c in plain))
report={'selection':'uniform random qualifying normalized40char test window, seed927012','source':'de_gsd-ud-test.conllu not used for training','qualifying_windows':len(candidates),'all_windows':len(allwindows),'sentence_id':sid,'normalized_offset':offset,'original_sentence':raw,'plaintext':plain,'IC':ci,'distinct':cd,'target_IC':ic,'target_distinct':nd,'training_sentence_injection':False}
(p/'flat40-generation.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n');print(json.dumps(report,indent=2,ensure_ascii=False))
