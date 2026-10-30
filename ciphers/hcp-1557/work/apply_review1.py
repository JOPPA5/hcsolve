#!/usr/bin/env python3
"""Apply review-1 transcript corrections (literal = visible sign) and refresh record hashes."""
from pathlib import Path
import hashlib,json
W=Path(__file__).resolve().parent
key=json.loads((W/'key.json').read_text())
fixes=[('n3r8 ','n3h8 '),(' cm5 ',' sm5 '),('g3mdh383h2','g3mth383h2'),('m5ybh4y5nm5y4.','m3ybh4y5nm5y4!')]
t=(W/'manual-transcript.txt').read_text()
for a,b in fixes:
 if b in t: continue
 assert t.count(a)==1,a; t=t.replace(a,b)
(W/'manual-transcript.txt').write_text(t)
lines=t.splitlines()
rows=json.loads((W/'rows.json').read_text())
for r,l in zip(rows,lines): r['transcript']=l
(W/'rows.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False)+'\n')
pos=json.loads((W/'positions.json').read_text())
import re
exp=[]
for r,l in zip(rows,lines):
 for wi,w in enumerate(l.split(),1):
  for ui,m in enumerate(re.finditer(r'\{U1\}|[^\s.,;:!?\-]',w),1): exp.append((r['row'],wi,ui,m.group()))
assert len(exp)==len(pos)
for p,e in zip(pos,exp):
 assert (p['row'],p['word'],p['unit_in_word'])==e[:3]
 if p['symbol']!=e[3]:
  print('changed',p['index'],p['row'],p['word'],p['symbol'],'->',e[3]); p['symbol']=e[3]; p['plaintext']=key[e[3]]
(W/'positions.json').write_text(json.dumps(pos,indent=2,ensure_ascii=False)+'\n')
out=[]
for l in lines: out.append(''.join(s if s=='{U1}' or s not in key else key[s] for s in re.findall(r'\{U1\}|.',l)))
(W/'literal-cz.txt').write_text('\n'.join(out)+'\n')
man=json.loads((W/'sha256.json').read_text())
for f in man['records']: man['records'][f]=hashlib.sha256((W/f).read_bytes()).hexdigest()
(W/'sha256.json').write_text(json.dumps(man,indent=2)+'\n')
