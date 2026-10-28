#!/usr/bin/env python3
"""Read-only image-transcription verification and known-key decipherment."""
from pathlib import Path
from collections import Counter
import hashlib,json,csv,io
R=Path(__file__).resolve().parents[1];W=R/'work'
for manifest in ('source-sha256.json','record-sha256.json'):
 for filename,wanted in json.loads((W/manifest).read_text()).items():
  assert hashlib.sha256((R/filename).read_bytes()).hexdigest()==wanted, f'Hash mismatch: {filename}'
key=json.loads((W/'key.json').read_text());assert len(set(key.values()))==len(key)
assert hashlib.sha256((W/'key.json').read_bytes()).hexdigest()=='2873a356dc562bbbd65840438651395f5e780a989a4524fc5d42717d10094a3b','fixed transferred key changed'
for filename,wanted in json.loads((W/'reference-sha256.json').read_text()).items():
 assert hashlib.sha256((R.parent.parent/filename).read_bytes()).hexdigest()==wanted,'reference changed: '+filename
inv={v:k for k,v in key.items()};record=json.loads((W/'transcription.json').read_text())
positions=[];total=0;ch=0;letters=0;counts=Counter();literal=[]
for row in record['rows']:
 out=[];idx=0
 for c in row['cipher']:
  if c in key:
   idx+=1;total+=1;ch+=c=='ř';letters+=len(key[c]);counts[c]+=1
   assert inv[key[c]]==c
   positions.append([str(total),row['id'],str(idx),c,key[c]])
  else:assert c in ' .,;-',f'Unknown symbol {c}'
  out.append(key.get(c,c))
 text=''.join(out);assert text==row['plaintext'];assert idx==row['active_units']
 back='';offset=0
 while offset<len(text):
  value='CH' if text.startswith('CH',offset) else text[offset]
  back+=inv.get(value,value);offset+=len(value)
 assert back==row['cipher'],('actual whole-row inverse differs',row['id'])
 literal.append(text)
 print(text)
assert len(record['rows'])==12
assert (total,ch,letters)==(415,2,417)
expected=list(csv.reader(io.StringIO((W/'positions.csv').read_text())))[1:];assert positions==expected
assert record['counts']=={'rows':12,'active_units':total,'CH_units':ch,'base_letters':letters,'observed_assigned_classes':len(counts),'unassigned_active_units':0,'class_counts':dict(sorted(counts.items()))}
assert (W/'transcription.txt').read_text()==''.join(row['id']+' '+row['cipher']+'\n' for row in record['rows'])
assert (W/'literal.txt').read_text()=='\n'.join(literal)+'\n'
solution=(R/'SOLUTION.md').read_text();block=solution.split('```text\n',1)[1].split('\n```',1)[0]
assert block=='\n'.join(literal),'SOLUTION literal differs'
for uncertain in record['uncertain_positions']:
 position=positions[uncertain['global_position']-1]
 assert position[1:4]==[uncertain['row'],str(uncertain['row_position']),uncertain['preferred_shape']]
 assert key[uncertain['preferred_shape']]==uncertain['preferred_plaintext']
 assert key[uncertain['bounded_alternative_shape']]==uncertain['bounded_alternative_plaintext']
nrecords=len(json.loads((W/'record-sha256.json').read_text()))
print(f'\nVerified: 3 immutable source hashes; {nrecords} record/crop/code hashes; 2 reference hashes; 12 indexed rows; {total} active cipher units, including {ch} CH units -> {letters} base letters; tokenwise and actual whole-row inverse, all positions/counts and saved/SOLUTION literal match.')
print('The manual transcription is linked to the source image by row-coordinate boxes, indexed.png and focused controls; this is not automatic OCR or independent visual verification.')
print('Ordinary date/address, punctuation, spacing and underline are outside the cipher-unit count. No canceled cipher unit identified.')
print('Key inventory:', ' '.join(f'{c}:{counts[c]}' for c in key))
print('All 415 active units have preferred assignments; one retraced R06 sign has bounded alternative 2/U to preferred 1/Y. No unassigned active unit or guessed missing word.')
