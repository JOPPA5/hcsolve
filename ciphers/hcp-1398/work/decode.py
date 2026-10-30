#!/usr/bin/env python3
"""HCP 1398: Caesar -1 on a manual visual transcription (no OCR)."""
from pathlib import Path
import json,hashlib,string
p=Path(__file__).resolve().parents[1]
for f,h in json.loads((p/'work/source-sha256.json').read_text()).items():
 assert hashlib.sha256((p/'source'/f).read_bytes()).hexdigest()==h,f
abc=string.ascii_uppercase;k=str.maketrans(abc,abc[-1]+abc[:-1])
d=json.loads((p/'work/transcription.json').read_text());n=0;lines=[]
for row in d['rows']:
 t=''.join(f['text'] for f in row['fields']);n+=sum(c.isalpha() for c in t)
 lines.append(t.upper().translate(k));print(row['region']+': '+lines[-1])
assert 'DEARST' in lines[0]
print('normalized: '+' / '.join(lines).replace('DEARST','DEAR[E]ST'))
print(f'{n} cipher letters, all decoded with one key (Caesar -1); 0 alternatives.')
print('Note: the card writes DEARST (efbstu); [E] is an editorial restoration.')
