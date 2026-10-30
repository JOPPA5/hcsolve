#!/usr/bin/env python3
"""Caesar -1 of manual scan transcription; initials remain unclassified."""
from pathlib import Path
import json,hashlib,string
p=Path(__file__).resolve().parents[1]
for f,h in json.loads((p/'work/source-sha256.json').read_text()).items():
 assert hashlib.sha256((p/'source'/f).read_bytes()).hexdigest()==h,f
abc=string.ascii_uppercase;k=str.maketrans(abc+abc.lower(),(abc[-1]+abc[:-1])+(abc[-1]+abc[:-1]).lower())
d=json.loads((p/'work/transcription.json').read_text());n=0
for row in d['rows']:
 out=[]
 for f in row['fields']:
  if f['kind']=='cipher':n+=sum(c.isalpha() for c in f['text']);out.append(f['text'].translate(k))
  else:out.append('['+f['description']+']')
 print(row['region']+': '+' '.join(out))
print(f'{n} frozen cipher letters; three initial-like fields outside decoded coverage. Partial.')
