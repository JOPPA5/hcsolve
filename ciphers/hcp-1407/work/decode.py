#!/usr/bin/env python3
"""Caesar -1 of manual scan transcription; not OCR. Uncertain fields explicit."""
from pathlib import Path
import hashlib,json,string
p=Path(__file__).resolve().parents[1]
for n,h in json.loads((p/'work/source-sha256.json').read_text()).items():
 assert hashlib.sha256((p/'source'/n).read_bytes()).hexdigest()==h,n
key=str.maketrans(string.ascii_uppercase+string.ascii_lowercase,string.ascii_uppercase[-1:]+string.ascii_uppercase[:-1]+string.ascii_lowercase[-1:]+string.ascii_lowercase[:-1])
d=json.loads((p/'work/transcription.json').read_text())
count=0
for row in d['rows']:
 out=[]
 for field in row['fields']:
  if field['kind']=='cipher':
   count+=sum(c.isalpha() for c in field['text']);out.append(field['text'].translate(key))
  elif field['kind']=='cipher-alternative':
   out.append('['+'/'.join(v.translate(key) for v in field['alternatives'])+']')
  else:out.append('['+field['description']+']')
 print(row['region']+': '+' '.join(out))
print(f'{count} securely recorded cipher letters; abbreviated fields remain unclassified.')
