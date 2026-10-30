#!/usr/bin/env python3
"""Read-only verification/decoding of a frozen MANUAL scan transcription; no OCR."""
from pathlib import Path
import hashlib,json,sys
W=Path(__file__).resolve().parent;R=W.parents[2]
RECORD_SHA='f4cd4bf125679411d5860d611dd6cf64f4e056230c3544253e2ce848a434fbd4'
KEY_SHA='47319cded98fe160ec187cc862ee80db6923d6ce14219cc4e3c158db277a47c2'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(W/'record.json')==RECORD_SHA,'manual record changed'
assert sha(W/'key.json')==KEY_SHA,'key changed'
r=json.loads((W/'record.json').read_text());key=json.loads((W/'key.json').read_text())
assert key==r['key']
for p,h in r['hashes'].items():assert sha(R/p)==h,f'source/reference hash changed: {p}'
inverse={}
for glyph,plain in key.items():inverse.setdefault(plain,set()).add(glyph)
seen=set();ng=nu=nletters=nch=nexact=nalias=0;observed_aliases=set();out=[];table=['position\ttype\tglyph\tliteral_plain']
for row in r['rows']:
 plain=[];raw=[];pos=0
 for t in row['tokens']:
  k=t['type']
  if k in ('space','literal'):
   plain.append(t['text']);raw.append(t['text']);continue
  pos+=1;pid=f"{row['id']}.{pos:03d}"
  assert t['id']==pid and pid not in seen;seen.add(pid)
  if k=='glyph':
   assert key[t['glyph']]==t['plain'];v=t['plain'];ng+=1;raw.append(t['glyph'])
   # Inverse comes from the whole key, independently of the token being checked.
   candidates=inverse[v];assert t['glyph'] in candidates
   if len(candidates)==1:
    assert next(iter(candidates))==t['glyph'];nexact+=1
   else:
    nalias+=1;observed_aliases.add(v)
   nletters+=len(v);nch+=int(v=='ch')
  elif k=='unknown_span':
   assert t['length'] is None;v=t['text'];nu+=1;raw.append(v)
  else:assert k in ('punctuation','plain_handwriting');v=t['text'];raw.append(v)
  plain.append(v);table.append(f"{pid}\t{k}\t{t.get('glyph','')}\t{v}")
 assert ''.join(raw)==row['manual_glyphs'],row['id']
 out.append(row['id']+' '+''.join(plain))
assert nu==r['unknown_length_spans']
print('Manual record, source and public-reference hashes: OK')
print(f'{ng} individually indexed assigned glyph units; {nu} unknown-length spans (excluded from any glyph denominator).')
print(f'Emitted cipher base letters: {nletters}; CH units: {nch} (each emits 2 letters; {ng-nch} other units each emit 1).')
print(f'All token IDs checked; whole-key inverse membership: OK; {nexact} observed units have a unique exact inverse; {nalias} units have key aliases.')
for v in sorted(observed_aliases):print(f'Alias limit: {v!r} reverses to {sorted(inverse[v])}; plaintext alone cannot recover which glyph was written.')
print('Glyph-stream reconstruction from stored tokens: exact. These checks do not independently validate visual readings.')
print('\n'.join(out))
if '--indexed' in sys.argv:print('\n'+'\n'.join(table))
