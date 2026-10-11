from pathlib import Path
from collections import Counter,defaultdict
import unicodedata,math
w=Path(__file__).resolve().parent;root=w.parents[1];d=w/'cs-lex';d.mkdir(exist_ok=True)
norm=lambda s:''.join(c for c in unicodedata.normalize('NFD',s.lower()) if 'a'<=c<='z')
pos={'NOUN':0,'PROPN':0,'ADJ':1,'VERB':2,'AUX':2,'ADV':3,'ADP':4,'PRON':5,'DET':5,'SCONJ':5,'CCONJ':5,'PART':5,'NUM':6}
freq=Counter();mask=defaultdict(int);trans=Counter();prev=8
for s in (root/'batches/czech-scoring/source/cs_cac-ud-train.conllu').read_text().splitlines()+['']:
 if not s:
  if prev!=8:trans[prev,9]+=1
  prev=8;continue
 f=s.split('\t')
 if len(f)>3 and f[0].isdigit():
  word=norm(f[1]);p=pos.get(f[3],7)
  if word:freq[word]+=1;mask[word]|=1<<p;trans[prev,p]+=1;prev=p
(d/'words-pos.tsv').write_text(''.join(f'{s}\t{f}\t{mask[s]}\n' for s,f in sorted(freq.items())))
(d/'pos-transitions.tsv').write_text(''.join(f'{a}\t{b}\t{math.log((trans[a,b]+.5)/(sum(trans[a,j] for j in range(10))+5))}\n' for a in range(9) for b in range(10)))
for n in (3,4,5):
 link=d/f'model{n}.tsv'
 if not link.exists():link.symlink_to(root/'batches/czech-scoring'/f'model{n}.tsv')
print('Czech lexical score uses TRAIN only:',len(freq),'words')
