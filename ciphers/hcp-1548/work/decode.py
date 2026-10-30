#!/usr/bin/env python3
"""Read-only source/record guarded known-key decoder; never regenerates inputs.
Revised 2026-10-29 after review 1: the former unknown span U1 is recorded as restored glyphs 5 2 (R02 positions 18-19)."""
from pathlib import Path
from collections import Counter
import hashlib,json,csv,io,re
R=Path(__file__).resolve().parents[1];W=R/'work';REPO=R.parents[1]
source_guard=json.loads((REPO/'batches/easy-2026-10-28/cz226-228-229-source-sha256.json').read_text())
for name in ('picture.jpg','address.jpg','metadata.md'):
 p=R/'source'/name;assert hashlib.sha256(p.read_bytes()).hexdigest()==source_guard[str(p.relative_to(REPO))],f'Original hash mismatch: {name}'
for filename,wanted in json.loads((W/'record-sha256.json').read_text()).items():
 assert hashlib.sha256((R/filename).read_bytes()).hexdigest()==wanted,f'Record hash mismatch: {filename}'
for filename,wanted in json.loads((W/'reference-sha256.json').read_text()).items():
 assert hashlib.sha256((REPO/filename).read_bytes()).hexdigest()==wanted,f'Reference hash mismatch: {filename}'
key=json.loads((W/'key.json').read_text());inv={v:k for k,v in key.items()};assert len(inv)==len(key)
# Fixed whole-string inverse: greedily recognise the single CH digraph, then base letters.
# No per-token dictionary derived from a claimed plaintext is used.
def inverse(text):
 out=[];i=0
 while i<len(text):
  if text.startswith('CH',i):out.append(inv['CH']);i+=2
  elif text[i] in inv:out.append(inv[text[i]]);i+=1
  else:assert text[i] in ' .?;-',repr(text[i]);out.append(text[i]);i+=1
 return ''.join(out)
record=json.loads((W/'transcription.json').read_text());positions=[];total=0;counts=Counter();outrows=[];restored=[]
for row in record['rows']:
 out=[];idx=0;raw=[]
 for token in row['tokens']:
  if token['kind']=='glyph':
   c=token['shape'];assert c in key and set(token)<={'kind','shape','restored'}
   if token.get('restored'):restored.append((row['id'],idx+1,c))
   idx+=1;total+=1;counts[c]+=1;out.append(key[c]);raw.append(c);positions.append([str(total),row['id'],str(idx),c,key[c]])
  else:
   assert token['kind']=='punctuation' and len(token['text'])==1 and token['text'] in ' .?;-';out.append(token['text']);raw.append(token['text'])
 plaintext=''.join(out);cipher=''.join(raw)
 assert plaintext==row['plaintext'] and cipher==row['cipher'] and idx==row['readable_units']
 assert inverse(plaintext)==cipher,f'Whole-row inverse mismatch {row["id"]}'
 outrows.append(plaintext)
assert restored==[('R02',18,'5'),('R02',19,'2')];assert len(record['rows'])==9;assert total==296;assert counts['ř']==1
assert positions==list(csv.reader(io.StringIO((W/'positions.csv').read_text())))[1:]
assert '\n'.join(outrows)+'\n'==(W/'literal.txt').read_text()
assert '\n'.join(r['cipher'] for r in record['rows'])+'\n'==(W/'ciphertext.txt').read_text()
print('\n'.join(outrows))
print('\nOrdinary picture-side date: 6.VII.1903. Underlined terminal b is decoded P (signature initial; confirmed on the scan in review 1); expansion to Pepous is a family inference only.')
print(f'Verified 3 originals, 5 record hashes, reference hashes, 9 rows and all indexed positions. {total} base cipher units, all mapped by the fixed key -> {sum(counts[c]*len(key[c]) for c in key)} base letters; no unmapped sign.')
print('Restoration: R02 positions 18-19 (5 2 -> E U, NEUSTALE) lie under the printed stem; U clearly visible, E partly visible and required by Czech.')
print('Whole-row fixed-key inverse matches every saved row; no broad aliases or inferred missing CH marks. R08 VRELYH / DLOUHYH retained literally (no bar on the r, writer omission); R09 r with a separate bar = CH (both confirmed in review 1).')
print('Manual transcription, linked by row boxes and visual controls; checked row by row against the scan in review 1.')
print('Inventory:',' '.join(f'{c}:{counts[c]}' for c in key))
