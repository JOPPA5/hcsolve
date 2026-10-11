from collections import Counter
from pathlib import Path
import unicodedata,math
p=Path(__file__).parent
c=Counter()
for l in (p/'sk_snk-ud-train.conllu').read_text().splitlines():
 if l.startswith('# text = '):
  s=''.join(x for x in unicodedata.normalize('NFD',l[9:].lower()) if 'a'<=x<='z')
  c.update(s[i:i+4] for i in range(len(s)-3))
with (p/'quadgrams.tsv').open('w') as f:
 for k,v in c.items():f.write(f'{k} {math.log(v)}\n')
s=''.join(x for x in (p/'transcription.txt').read_text() if x.isalpha())
(p/'cipher.txt').write_text(s)
f=Counter(s); n=len(s)
print('length',n,'IC',sum(v*(v-1) for v in f.values())/(n*(n-1)), 'quadgram types',len(c))
