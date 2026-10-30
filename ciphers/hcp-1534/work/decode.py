#!/usr/bin/env python3
"""Read-only reproducibility check of the manual source-image record; not OCR."""
from pathlib import Path
import csv,hashlib,json,io
p=Path(__file__).resolve().parent; root=p.parent
sha=lambda path:hashlib.sha256(path.read_bytes()).hexdigest()
meta=json.loads((p/'transcription.json').read_text()); key=json.loads((p/'key.json').read_text())
for name,want in meta['source_sha256'].items():
 assert sha(root/'source'/name)==want, 'original hash changed: '+name
for name,want in json.loads((p/'record-hashes.json').read_text()).items():
 assert sha(p/name)==want, 'record hash changed: '+name
for name,want in json.loads((p/'reference-sha256.json').read_text()).items():
 assert sha(root.parent.parent/name)==want, 'reference hash changed: '+name
assert len(set(key.values()))==len(key)
inverse={v:k for k,v in key.items()}; csvrows=list(csv.DictReader((p/'indexed-units.csv').open()))
i=0; letters=0; unknowns=0; ch=0
for row in meta['rows']:
 parts=[]; j=0
 for token in row['cipher']:
  if token in key:
   plain=key[token];j+=1;i+=1
   assert inverse[plain]==token
   expected={'ordinal':str(i),'row':row['id'],'row_unit':str(j),'glyph_label':token,'plain':plain,'row_box':','.join(map(str,row['box']))}
   assert csvrows[i-1]==expected, (row['id'],j)
   if token=='?': unknowns+=1
   else: letters+=len(plain)
   ch+=token=='H'; parts.append(plain)
  else:
   assert token in ' .,-;:', (row['id'],token)
   parts.append(token)
 print(''.join(parts))
assert i==len(csvrows)
print(f'\nCHECK: source/record hashes and 2 published-reference hashes OK; {len(meta["rows"])} rows; {i} indexed marks; {i-unknowns} assigned units; {unknowns} unresolved overink; {ch} CH units; {letters} assigned base letters; token round-trip OK.')
print('Manual transcription remains a source-reading claim; the checks do not independently validate glyph choices.'+(' The unresolved overink could contain more than one original cipher unit.' if unknowns else ''))
