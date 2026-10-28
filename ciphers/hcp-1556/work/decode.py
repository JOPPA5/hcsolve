#!/usr/bin/env python3
"""Read-only verification/decode of manually indexed photograph transcription; no OCR."""
from pathlib import Path
from collections import Counter
import hashlib,json,sys
D=Path(__file__).resolve().parent; R=D.parents[2]
manifest=json.loads((D/'sha256.json').read_text())
for rel,want in manifest.items():
 p=R/rel
 got=hashlib.sha256(p.read_bytes()).hexdigest()
 if got!=want:raise SystemExit(f'HASH MISMATCH: {rel}')
guard=json.loads((R/'batches/easy-2026-10-28/cz235-237-next-source-sha256.json').read_text())
for rel,want in manifest.items():
 if rel.startswith('ciphers/hcp-1556/source/'):
  assert guard[rel]==want,('target source guard mismatch',rel)
k=json.loads((D/'key.json').read_text());fixed=json.loads((R/'ciphers/hcp-1520/work/key.json').read_text())
assert k==fixed,'family key changed'
assert len(set(k.values()))==len(k),'noninjective fixed key'
rows=json.loads((D/'rows.json').read_text());indexed=json.loads((D/'positions.json').read_text())
actual=[];out=[];inverse={v:c for c,v in k.items()}
for row in rows:
 s=row['symbols'];lit=''.join(k.get(c,c) for c in s)
 assert lit==row['literal'],('row literal differs',row['id'])
 # Actual inverse of the entire literal line, with CH the only multiletter value.
 i=0;back=''
 while i<len(lit):
  v='ch' if lit.startswith('ch',i) else lit[i]
  back+=inverse.get(v,v);i+=len(v)
 assert back==s,('fixed-key inverse differs',row['id'],back,s)
 j=0
 for col,c in enumerate(s,1):
  if c in k:
   j+=1;actual.append({'row':row['id'],'position':j,'string_column':col,'class':c,'literal':k[c]})
  else:assert c in ' ,.?!-',('unaccounted symbol',row['id'],c)
 out.append(row['id']+' '+lit)
assert actual==indexed,'position/literal index differs'
assert (D/'manual-transcript.txt').read_text()==''.join(r['id']+' '+r['symbols']+'\n' for r in rows)
assert (D/'literal-cz.txt').read_text()=='\n'.join(out)+'\n'
prose=(D.parent/'SOLUTION.md').read_text()
block=prose.split('<!--literal-begin-->')[1].split('<!--literal-end-->')[0].strip()
assert block=='```text\n'+'\n'.join(out)+'\n```','SOLUTION literal block differs'
c=Counter(p['class'] for p in actual)
print('\n'.join(out))
print(f'\nVERIFY: {len(rows)} rows; {len(actual)} mapped cipher positions; CH={c["H"]}; unknown=0; literal letters={sum(len(x["literal"]) for x in actual)}; source/reference/record hashes, exact fixed key, inverse, indexed positions and literal match.',file=sys.stderr)
