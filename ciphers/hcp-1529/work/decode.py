#!/usr/bin/env python3
"""Read-only standard-library audit and fixed-family-key decoder; no OCR."""
from pathlib import Path
from collections import Counter
import csv,datetime,hashlib,io,json
R=Path(__file__).resolve().parents[1];W=R/'work';manifests={}
for name in ('source-sha256.json','record-sha256.json'):
 manifests[name]=json.loads((W/name).read_text())
 for filename,digest in manifests[name].items():assert hashlib.sha256((R/filename).read_bytes()).hexdigest()==digest,'Hash mismatch: '+filename
key=json.loads((W/'key.json').read_text());inv={v:k for k,v in key.items()};assert len(inv)==len(key)
record=json.loads((W/'transcription.json').read_text());positions=[];total=ch=letters=0;counts=Counter();texts=[];limits=[]
for row in record['rows']:
 idx=0
 for word,token in enumerate(row['cipher'].split(),1):
  for c in token:
   if c in key:idx+=1;total+=1;ch+=c=='H';letters+=len(key[c]);counts[c]+=1;positions.append([str(total),row['id'],str(idx),str(word),c,key[c]])
   else:assert c in ',.'
 text=''.join(key.get(c,c) for c in row['cipher']);assert text==row['plaintext'];assert idx==row['active_units'];texts.append(text);print(text)
 # Re-encode actual complete printed plaintext; CH has priority over C.
 out=[];i=0
 while i<len(text):
  if not text[i].isalpha():out.append(text[i]);i+=1;continue
  for unit in sorted(inv,key=len,reverse=True):
   if text.startswith(unit,i):out.append(inv[unit]);i+=len(unit);break
  else:raise AssertionError(('unencodable plaintext',row['id'],i))
 assert ''.join(out)==row['cipher'],'Whole-row fixed inverse mismatch '+row['id']
 units=[c for c in row['cipher'] if c in key]
 for v in row.get('source_reading_limits',[]):
  assert units[v['row_ordinal']-1]==v['selected_label'] and key[v['selected_label']]==v['plaintext'];limits.append({'row':row['id'],**v})
assert len(record['rows'])==8 and (total,ch,letters)==(417,3,420)
assert positions==list(csv.reader(io.StringIO((W/'positions.csv').read_text())))[1:]
assert '\n'.join(texts)+'\n'==(W/'plaintext.txt').read_text()
assert '\n'.join(r['cipher'] for r in record['rows'])+'\n'==(W/'transcription.txt').read_text()
inventory=json.loads((W/'inventory.json').read_text());assert inventory['label_counts']==dict(sorted(counts.items())) and inventory['source_reading_limits']==limits
assert (inventory['active_units'],inventory['CH_units'],inventory['base_letters'])==(total,ch,letters)
context=json.loads((W/'review1-context-check.json').read_text())
for day,weekday in context['computed_dates'].items():assert datetime.date.fromisoformat(day).strftime('%A')==weekday
print(f'\nVerified: {len(manifests["source-sha256.json"])} immutable source hashes; {len(manifests["record-sha256.json"])} record hashes; 8 indexed rows; {total} active units, {ch} CH -> {letters} base letters; exact whole-row fixed-key inverse, ordinal inventory and calendar calculations.')
for v in limits:print('SOURCE LIMIT:',v['row'],'ordinal',v['row_ordinal'],v['observation'])
print('Manual source transcription; no OCR or glyph-truth proof. Calendar/series compatibility does not identify an event or town. Current response is not a new independent review.')
print('Key inventory:',' '.join(f'{c}:{counts[c]}' for c in key))
