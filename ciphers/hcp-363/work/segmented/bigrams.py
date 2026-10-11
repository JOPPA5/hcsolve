from pathlib import Path
from collections import Counter
import unicodedata,math,json
p=Path(__file__).resolve().parent;root=p.parents[3]
source=root/'ciphers/hcp-393/work/sk_snk-ud-train.conllu'
c=Counter();n=0
for line in source.read_text().splitlines():
 if line.startswith('# text = '):
  t=''.join(x for x in unicodedata.normalize('NFD',line[9:].lower()) if 'a'<=x<='z')
  c.update(t[i:i+2] for i in range(len(t)-1));n+=1
(p/'bigrams.tsv').write_text(''.join(f'{a}{b}\t{math.log(c[a+b]+.1)}\n' for a in 'abcdefghijklmnopqrstuvwxyz' for b in 'abcdefghijklmnopqrstuvwxyz'))
(p/'bigram-provenance.json').write_text(json.dumps({'source':str(source),'sentences':n,'controls_used':False,'normalization':'NFD lowercase AZ, spaces omitted'},indent=2)+'\n')
