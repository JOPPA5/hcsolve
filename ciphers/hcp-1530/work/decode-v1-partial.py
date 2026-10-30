#!/usr/bin/env python3
"""Read-only standard-library verification of partial manual source transcription."""
from pathlib import Path
from collections import Counter
import hashlib,json,csv,io
R=Path(__file__).resolve().parents[1];W=R/'work'
for manifest in ('source-sha256.json','record-sha256.json'):
 for filename,digest in json.loads((W/manifest).read_text()).items():
  assert hashlib.sha256((R/filename).read_bytes()).hexdigest()==digest, f'Hash mismatch: {filename}'
for filename,digest in json.loads((W/'reference-sha256.json').read_text()).items():
 assert hashlib.sha256((R.parents[1]/filename).read_bytes()).hexdigest()==digest, f'Reference hash mismatch: {filename}'
key=json.loads((W/'key.json').read_text());inv={v:k for k,v in key.items()};assert len(inv)==len(key)
record=json.loads((W/'transcription.json').read_text());positions=[];total=ch=letters=0;counts=Counter();unknowns=[]
for row in record['rows']:
 text=[];raw=[];idx=0
 for p in row['parts']:
  if 'cipher' in p:
   c=p['cipher'];plain=key[c];assert plain==p['plain'];assert inv[plain]==c
   total+=1;idx+=1;ch+=plain=='CH';letters+=len(plain);counts[c]+=1
   positions.append([str(total),row['id'],str(idx),'known',c,plain]);raw.append(c);text.append(plain)
  elif 'unknown' in p:
   u=p['unknown'];assert u in record['unknowns'];token='['+u+']';unknowns.append(u)
   positions.append(['',row['id'],'','unresolved',token,'']);raw.append(token);text.append(token)
  else:
   token=p.get('ordinary',p.get('literal'));assert token is not None;raw.append(token);text.append(token)
 assert ''.join(raw)==row['cipher'];assert ''.join(text)==row['plaintext'];assert idx==row['known_units']
 print(row['id']+' '+''.join(text))
assert (len(record['rows']),total,ch,letters)==(14,445,6,451)
assert unknowns==['U1','U2','U4','U3']
expected=list(csv.reader(io.StringIO((W/'positions.csv').read_text())))[1:];assert positions==expected
print(f'\nPARTIAL: {total} positively transcribed cipher units, including {ch} CH units, produce {letters} base letters.')
print('Four unresolved dark spans U1/U2/U3/U4 have unknown unit count. No complete denominator or coverage percentage is asserted.')
print('Verified 3 target source hashes, 2 published-reference hashes, 3 record hashes, all known ordinal positions, exact per-token inverse-key round trip, and unresolved-span preservation.')
print('This links a manual transcription to hashed originals and documented row boxes; it is not OCR or independent visual proof. Ordinary date/address/title, punctuation, spacing and accents are outside the cipher count.')
print('Known key inventory:', ' '.join(f'{c}:{counts[c]}' for c in key))
