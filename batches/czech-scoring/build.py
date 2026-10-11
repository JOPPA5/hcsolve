from pathlib import Path
from collections import Counter
import hashlib, json, math, unicodedata

p=Path(__file__).parent
def norm(s):
    return ''.join(c for c in unicodedata.normalize('NFD',s.lower()) if 'a'<=c<='z')
train=p/'source/cs_cac-ud-train.conllu'
sentences=[norm(line[9:]) for line in train.read_text().splitlines() if line.startswith('# text = ')]
assert sentences
counts={n:Counter() for n in (3,4,5)}
for s in sentences:
    for n in counts: counts[n].update(s[i:i+n] for i in range(len(s)-n+1))
for n,c in counts.items():
    den=sum(c.values())+.1*26**n
    (p/f'model{n}.tsv').write_text(f'#floor {math.log(.1/den)}\n'+''.join(f'{g}\t{math.log((v+.1)/den)}\n' for g,v in sorted(c.items())))
report=dict(sentences=len(sentences),grams={n:len(c) for n,c in counts.items()},training='TRAIN only; no TEST sentences, ciphertexts, candidate plaintexts or known target words',sources={f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in (p/'source').iterdir() if f.is_file()})
(p/'build-report.json').write_text(json.dumps(report,indent=2))
base=Path('ciphers/hcp-369/work/mono-c28.cpp').read_text()
(p/'mono28.cpp').write_text(base)
base=base.replace('v==26?2:v==27?18:v','v').replace('x<28','x<26').replace('k(28)','k(26)').replace('rng()%28','rng()%26')
(p/'mono26.cpp').write_text(base)
print(json.dumps(report,indent=2))
