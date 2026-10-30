#!/usr/bin/env python3
"""Manual scan transcript, not OCR; one abbreviated field remains unresolved."""
from pathlib import Path
import hashlib,json,string
p=Path(__file__).resolve().parents[1]
for n,h in json.loads((p/'work/source-sha256.json').read_text()).items():
 assert hashlib.sha256((p/'source'/n).read_bytes()).hexdigest()==h,n
abc=string.ascii_uppercase; key=str.maketrans(abc+abc.lower(),(abc[-1]+abc[:-1])+(abc[-1]+abc[:-1]).lower())
d=json.loads((p/'work/transcription.json').read_text());n=0
for row in d['rows']:
 out=[]
 for f in row['fields']:
  if f['kind']=='cipher':out.append(f['text'].translate(key));n+=sum(c.isalpha() for c in f['text'])
  else:out.append('['+f['description']+']')
 print(row['region']+': '+' '.join(out))
print(f'{n} frozen cipher letters; abbreviated field partially unresolved, no whole-card decipherment claim.')
