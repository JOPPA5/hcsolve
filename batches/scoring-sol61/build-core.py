from pathlib import Path
import unicodedata
p=Path(__file__).resolve().parent

def norm(w):return ''.join(c for c in unicodedata.normalize('NFD',w.lower()) if 'a'<=c<='z')
core=set()
for l in (p/'source/sk_SK.dic').read_text().splitlines()[1:]:
 f=l.split()
 if f and f[0].split('/')[0].isalpha():core.add(norm(f[0].split('/')[0]))
for l in Path('ciphers/hcp-393/work/sk_snk-ud-train.conllu').read_text().splitlines():
 f=l.split('\t')
 if len(f)>2 and f[0].isdigit():core.add(norm(f[1]))
(p/'core-words.txt').write_text('\n'.join(sorted(w for w in core if w))+'\n')
