#!/usr/bin/env python3
"""READ-ONLY by default: verify immutable inputs and decode manual glyph rows."""
from pathlib import Path
from collections import Counter
import csv,hashlib,io,json
R=Path(__file__).resolve().parents[1];W=R/'work'
for mf in ['source-sha256.json','record-sha256.json']:
 for name,wanted in json.loads((W/mf).read_text()).items():
  assert hashlib.sha256((R/name).read_bytes()).hexdigest()==wanted,f'Hash mismatch: {name}'
key=json.loads((W/'key.json').read_text());inv={v:k for k,v in key.items()};assert len(inv)==len(key)
rec=json.loads((W/'transcription.json').read_text());positions=[];counts=Counter();total=letters=ch=unknown=restored=0
for row in rec['rows']:
 out=[];idx=0
 for c in row['cipher']:
  if c in key:
   idx+=1;total+=1;letters+=len(key[c]);ch+=c=='ř';counts[c]+=1
   assert inv[key[c]]==c
   positions.append([str(total),row['id'],str(idx),c,key[c]])
  elif c in '[]':restored+=c=='['
  else:assert c in ' .,?-',f'Unknown glyph {c}'
  out.append(key.get(c,c))
 text=''.join(out);assert text==row['plaintext'];assert idx==row['active_units'];print(text)
assert (len(rec['rows']),total,ch,letters,unknown,restored)==(17,383,3,386,0,1)
assert positions==list(csv.reader(io.StringIO((W/'positions.csv').read_text())))[1:]
print(f'\nVerified: 3 immutable source hashes; 3 record hashes; 17 rows; {total} indexed cipher positions, {total} assigned, {unknown} unresolved, {restored} contextual restoration shown in [brackets] (R12 PSAN[I]); {ch} CH units; {letters} base letters; exact tokenwise key round trip for every assigned unit; ordinal inventory.')
print('Manual transcription, not OCR: consistency checks do not independently validate source glyph readings. Row boxes and focused original-pixel controls are supplied.')
print('Ordinary date/address, spacing, punctuation and accent marks excluded from cipher-unit counts. No canceled cipher units identified.')
print('Key inventory:',' '.join(f'{s}:{counts[s]}' for s in key))
