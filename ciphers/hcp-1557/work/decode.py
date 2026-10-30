#!/usr/bin/env python3
"""Read-only manual-transcript audit; not OCR or a test of glyph truth."""
from pathlib import Path
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[3]; W=Path(__file__).resolve().parent
H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
manifest=json.loads((W/'sha256.json').read_text())
for path,digest in manifest['inputs'].items():
 assert H(ROOT/path)==digest,('input hash mismatch',path)
guard=json.loads((ROOT/'batches/easy-2026-10-28/cz235-237-next-source-sha256.json').read_text())
assert len(guard)==9
for path,digest in guard.items():assert H(ROOT/path)==digest,('batch guard mismatch',path)
for path,digest in manifest['records'].items():assert H(W/path)==digest,('record mismatch',path)
key=json.loads((W/'key.json').read_text()); inv={v:k for k,v in key.items()}
assert len(inv)==len(key), 'non-injective key'
base=json.loads((ROOT/'ciphers/hcp-1520/work/key.json').read_text())
assert key==dict(base,v='f'),'unexpected key alteration'
rows=json.loads((W/'rows.json').read_text()); pos=json.loads((W/'positions.json').read_text())
trans=(W/'manual-transcript.txt').read_text();lines=trans.splitlines();assert [r['transcript'] for r in rows]==lines
expected=[];counts={};out=[]
for row,line in zip(rows,lines):
 oi=[];cirow=0
 for word_idx,word in enumerate(line.split(),1):
  unit_idx=0
  for m in re.finditer(r'\{U1\}|[^\s.,;:!?\-]',word):
   s=m.group();unit_idx+=1;cirow+=s!='{U1}'
   assert s in key or s=='{U1}',('unrecognized',s)
   expected.append((row['row'],word_idx,unit_idx,s))
 for s in re.findall(r'\{U1\}|.',line):oi.append(s if s=='{U1}' or s not in key else key[s])
 counts[row['row']]=cirow;out.append(''.join(oi))
assert len(pos)==len(expected)
for i,(p,e) in enumerate(zip(pos,expected),1):
 assert (p['index'],p['row'],p['word'],p['unit_in_word'],p['symbol'])==(i,*e)
 row=next(r for r in rows if r['row']==p['row'])
 assert p['row_box_original_pixels']==row['box_original_pixels'] and p['orientation_degrees_clockwise']==0
 if p['kind']=='glyph':assert p['plaintext']==key[p['symbol']]
 else:assert p['symbol']=='{U1}' and p['glyph_length'] is None
for row in rows:assert row['indices']==[p['index'] for p in pos if p['row']==row['row']]
literal='\n'.join(out)+'\n';assert literal==(W/'literal-cz.txt').read_text()
# Re-encode the complete printed plaintext independently of token positions.
# CH is the longest fixed-key plaintext unit. The opaque unknown-run label is
# passed through, because its ink cannot be encoded by any asserted key entry.
plain_units=sorted(inv,key=len,reverse=True)
encoded=[];i=0
while i<len(literal):
 if literal.startswith('{U1}',i):encoded.append('{U1}');i+=4;continue
 c=literal[i]
 if not c.isalpha():encoded.append(c);i+=1;continue
 for u in plain_units:
  if literal.startswith(u,i):encoded.append(inv[u]);i+=len(u);break
 else:raise AssertionError(('unencodable literal',i,c))
assert ''.join(encoded)==trans,'whole-plaintext fixed-key inverse mismatch'
known=sum(counts.values());letters=sum(len(key[p['symbol']]) for p in pos if p['kind']=='glyph');ch=sum(p['symbol']=='H' for p in pos)
print(literal,end='')
print(f'\nVerified: {len(manifest["inputs"])} input hashes; all {len(guard)} batch source hashes; {len(manifest["records"])} record hashes; {len(rows)} physical rows; {counts}; {known} known cipher units -> {letters} base letters; {ch} CH units; 1 unknown ink run of unknown length. Whole-plaintext fixed-key inverse exact for known text; no OCR or independent glyph-truth claim.')
