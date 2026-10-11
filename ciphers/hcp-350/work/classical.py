from pathlib import Path
from collections import Counter
from math import log
import unicodedata
p=Path(__file__).parent;s=p.joinpath('cipher.txt').read_text();a='abcdefghijklmnopqrstuvwxyz';n=len(s)
counts=Counter(s)
def ic(t):
 c=Counter(t);return sum(v*(v-1) for v in c.values())/(len(t)*(len(t)-1)) if len(t)>1 else 0
print('Length',n,'groups',n//5,'IC',ic(s),'counts',counts)
print('Period IC: exploratory, not proof of periodic cipher')
for k in range(1,31):print(k,round(sum(ic(s[j::k]) for j in range(k))/k,5))
# Known visible heading as speculative key, never asserted a cipher key.
for key in ['holakovi','cieker','madrid','bratislava']:
 for kind in ['vigenere','beaufort','variant']:
  ks=[a.index(c) for c in key];v=[a.index(c) for c in s]
  t=''.join(a[((x-ks[i%len(ks)]) if kind=='vigenere' else (ks[i%len(ks)]-x) if kind=='beaufort' else (x+ks[i%len(ks)]))%26] for i,x in enumerate(v))
  print(key,kind,t)
# Unigram key estimates for ordinary Vigenere periods1..30.
corpus=p.parents[1]/'hcp-393/work/sk_snk-ud-train.conllu'
freq=Counter()
for line in corpus.read_text().splitlines():
 if line.startswith('# text = '):freq.update(c for c in unicodedata.normalize('NFD',line[9:].lower()) if c in a)
probs=[(freq[c]+1)/(sum(freq.values())+26) for c in a]
print('Vigenere maximum unigram-likelihood key estimates')
for period in range(1,31):
 key=[]
 for j in range(period):
  col=Counter(a.index(c) for c in s[j::period])
  key.append(max(range(26),key=lambda k:sum(v*log(probs[(c-k)%26]) for c,v in col.items())))
 t=''.join(a[(a.index(c)-key[i%period])%26] for i,c in enumerate(s))
 print(period,''.join(a[x] for x in key),t)
