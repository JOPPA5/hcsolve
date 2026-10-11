from collections import Counter
from pathlib import Path
import math,unicodedata
w=Path(__file__).resolve().parent;cs={n:Counter() for n in range(6,10)}
for line in w.parent.joinpath('sk_snk-ud-train.conllu').read_text().splitlines():
 if line.startswith('# text = '):
  s=''.join(c for c in unicodedata.normalize('NFD',line[9:].lower()) if 'a'<=c<='z')
  for n,counts in cs.items():counts.update(s[i:i+n] for i in range(len(s)-n+1))
for n,counts in cs.items():w.joinpath(f'phrase{n}.tsv').write_text(''.join(f'{s} {math.log1p(count)}\n' for s,count in sorted(counts.items())))
