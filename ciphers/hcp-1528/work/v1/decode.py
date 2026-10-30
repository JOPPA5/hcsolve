#!/usr/bin/env python3
"""Read-only source verification and known-key decoding of PARTIAL manual record."""
from pathlib import Path
from collections import Counter
import hashlib,json,csv,io,re
R=Path(__file__).resolve().parents[1];W=R/'work'
for manifest in ('source-sha256.json','record-sha256.json'):
 for filename,wanted in json.loads((W/manifest).read_text()).items():
  assert hashlib.sha256((R/filename).read_bytes()).hexdigest()==wanted, f'Hash mismatch: {filename}'
key=json.loads((W/'key.json').read_text());assert len(key)==len(set(key.values()))
inv={v:k for k,v in key.items()};record=json.loads((W/'transcription.json').read_text())
positions=[];counts=Counter();outrows=[];total=letters=0;unknowns=[]
for row in record['rows']:
 out=[];idx=0
 for token in re.findall(r'\{U\d+\}|.',row['cipher']):
  if token in key:
   idx+=1;total+=1;letters+=len(key[token]);counts[token]+=1
   assert inv[key[token]]==token
   positions.append([str(total),row['id'],str(idx),token,key[token]]);out.append(key[token])
  elif token.startswith('{U'):
   uid=token[1:-1];assert uid in record['unknown_spans'];unknowns.append(uid);out.append('['+uid+']')
  else:
   assert token in ' .,-';out.append(token)
 text=''.join(out);assert text==row['plaintext'];assert idx==row['confirmed_units']
 outrows.append(text);print(text)
assert len(record['rows'])==18 and total==492 and letters==499 and counts['ř']==7
assert len(unknowns)==len(set(unknowns)) and set(unknowns)==set(record['unknown_spans'])
assert positions==list(csv.reader(io.StringIO((W/'positions.csv').read_text())))[1:]
assert '\n'.join(outrows)+'\n'==(W/'plaintext.txt').read_text()
print(f'\nPARTIAL: {total} confirmed cipher units -> {letters} base letters, including {counts["ř"]} CH units; all confirmed positions and tokenwise round trip verified.')
print('Verified 3 immutable source hashes and 3 record hashes. 18 rows inventoried, 8 unknown spans (U6-U8 each exactly one position; U1-U5 have unestablished lengths). Full ciphertext denominator and coverage percentage UNKNOWN.')
print('This command verifies indexed manual image transcription, not automatic OCR or independent visual accuracy. Known family key transferred; no published target plaintext supplied.')
