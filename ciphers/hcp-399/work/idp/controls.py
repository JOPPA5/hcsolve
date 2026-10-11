from pathlib import Path
import random,json,unicodedata,hashlib
w=Path(__file__).resolve().parent
norm=lambda s: ''.join(c for c in unicodedata.normalize('NFD',s.lower()) if 'a'<=c<='z')
test=Path('ciphers/hcp-393/work/square10/sk_snk-ud-test.conllu');train=Path('ciphers/hcp-393/work/sk_snk-ud-train.conllu')
texts=[s[9:] for s in test.read_text().splitlines() if s.startswith('# text = ')];train_sentences={norm(t[9:]) for t in train.read_text().splitlines() if t.startswith('# text = ')};chosen=' '.join(s for s in texts if norm(s) not in train_sentences)[:1500]
records=[]
for n in [240,245]:
 authored=w.parent.joinpath(f'control-{n}-plain.txt').read_text().strip()
 for label,p in [('authored',authored),('heldout',norm(chosen)[:n])]:
  rng=random.Random(613990+n+(label=='heldout'));keys=[];s=p
  for size in [20,17]:
   k=list(range(size));rng.shuffle(k);keys.append(k);s=''.join(s[c::size] for c in k)
  name=f'{label}-{n}';w.joinpath(name+'.txt').write_text(s+'\n');w.joinpath(name+'.plain.txt').write_text(p+'\n');w.joinpath(name+'.outer-key.txt').write_text(','.join(map(str,keys[-1]))+'\n');records.append(dict(label=name,plaintext=p,keys=keys,heldout_excerpt=chosen if label=='heldout' else None))
w.joinpath('controls.json').write_text(json.dumps(records,ensure_ascii=False,indent=2))
w.joinpath('corpus-provenance.json').write_text(json.dumps({str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [test,train]},indent=2))
print('four independent planting cases created; TEST excerpt saved in controls.json')

for rec in records:
 s=w.joinpath(rec["label"]+".txt").read_text().strip();k=rec["keys"][-1];p=[""]*len(s);at=0
 for c in k:
  for j in range(c,len(s),len(k)):p[j]=s[at];at+=1
 w.joinpath(rec["label"]+".true-middle.txt").write_text("".join(p)+"\n")
