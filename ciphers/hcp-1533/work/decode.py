#!/usr/bin/env python3
"""Read-only known-key decode of a manual, image-anchored transcription."""
from pathlib import Path
from collections import Counter
import csv,hashlib,io,json
R=Path(__file__).resolve().parents[1]; W=R/'work'
for manifest in ('source-sha256.json','record-sha256.json'):
 for name,wanted in json.loads((W/manifest).read_text()).items():
  assert hashlib.sha256((R/name).read_bytes()).hexdigest()==wanted, f'Hash mismatch: {name}'
key=json.loads((W/'key.json').read_text());assert len(set(key.values()))==len(key)
inv={v:k for k,v in key.items()}; record=json.loads((W/'transcription.json').read_text())
positions=[];total=ch=letters=0;counts=Counter()
for row in record['rows']:
 out=[];idx=0;roundtrip=[]
 for c in row['cipher']:
  if c in key:
   idx+=1;total+=1;ch+=c=='ř';letters+=len(key[c]);counts[c]+=1
   positions.append([str(total),row['id'],str(idx),c,key[c]])
   out.append(key[c]);roundtrip.append(inv[key[c]])
  else:
   assert c in ' .,?;-',f'Unknown shape label: {c}'
   out.append(c);roundtrip.append(c)
 text=''.join(out)
 assert text==row['plaintext'] and idx==row['active_units']
 assert ''.join(roundtrip)==row['cipher']
 print(text)
assert [r['id'] for r in record['rows']]==[f'A{i:02}' for i in range(1,12)]+[f'B{i:02}' for i in range(1,9)]
assert (total,ch,letters)==(236,4,240)
expected=list(csv.reader(io.StringIO((W/'positions.csv').read_text())))[1:]
assert positions==expected
print(f'\nVerified: 3 immutable source hashes; 3 record hashes; 19 indexed rows; {total} active cipher units, including {ch} CH units -> {letters} base letters; all positional indices and exact tokenwise inverse-key round trips match.')
print('Input is a manual transcription linked to source hashes, row boxes and original-pixel controls; this command does not perform OCR or independently establish the visual readings.')
print('Ordinary date/address, arrow, punctuation and spacing lie outside the cipher-unit count. No canceled cipher unit is identified; a dark pen stroke within MYSLEN is documented in controls.')
print('Key inventory:',' '.join(f'{c}:{counts[c]}' for c in key))
