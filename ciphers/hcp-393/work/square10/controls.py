from pathlib import Path
import unicodedata,json,random,hashlib
w=Path(__file__).resolve().parent
norm=lambda s: ''.join(c for c in unicodedata.normalize('NFD',s.lower()) if 'a'<=c<='z')
train=w.parent.joinpath('sk_snk-ud-train.conllu').read_text()
train_sentences={norm(s[9:]) for s in train.splitlines() if s.startswith('# text = ')}
test=w.joinpath('sk_snk-ud-test.conllu').read_text()
sentence=next(s[9:] for s in test.splitlines() if s.startswith('# text = ') and len(norm(s[9:]))==100 and norm(s[9:]) not in train_sentences)
base='ministerstvozahranicnychveciziadavyslanectvoabybezodkladneoznamilovysledokrokovaniasprislusnymiuradmiazaslalo'[:100]
records=[]
for name,p in [('heldout',norm(sentence)),('authored',base)]:
 for j in range(2):
  rng=random.Random(393100+j);cols=list(range(10));rows=list(range(10));rng.shuffle(cols);rng.shuffle(rows);label=f'{name}-{j}'
  w.joinpath(label+'.txt').write_text(''.join(p[r*10+c] for r in rows for c in cols)+'\n')
  records.append(dict(label=label,plaintext=p,column_order=[cols.index(i) for i in range(10)],row_order=[rows.index(i) for i in range(10)],original_sentence=sentence if name=='heldout' else None))
w.joinpath('controls.json').write_text(json.dumps(records,ensure_ascii=False,indent=2))
