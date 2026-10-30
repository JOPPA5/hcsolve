#!/usr/bin/env python3
"""Keep existing27 confirmed excerpts and new explicitly provisional route positions."""
from pathlib import Path
import hashlib,json
p=Path(__file__).resolve().parents[1]
for name,digest in json.loads((p/'work/source-sha256.json').read_text()).items():
 assert hashlib.sha256((p/'source'/name).read_bytes()).hexdigest()==digest,name
def route(xs):
 out=[]; lo=0; hi=len(xs)-1
 while lo<=hi:
  out.append(xs[lo]);lo+=1
  if lo<=hi:out.append(xs[hi]);hi-=1
 return out
confirmed=0
for raw in (p/'work/confirmed-excerpts.txt').read_text().splitlines():
 text=''.join(route(raw))
 assert text[::2]+text[1::2][::-1]==raw
 print('existing excerpt: '+text);confirmed+=len(raw)
print(f'{confirmed} existing confirmed excerpt letters; unchanged.')
count=0; uncertain=0
for row in json.loads((p/'work/follow-provisional.json').read_text())['rows']:
 out=route(row['tokens'])
 display=''.join(x if isinstance(x,str) else '['+'/'.join(x)+']' for x in out)
 print(row['id']+': '+display)
 count+=len(out);uncertain+=sum(isinstance(x,list) for x in out)
print(f'{count} new provisional positions, {uncertain} explicit alternatives; not added to confirmed count.')
print('Manual transcription and bounded route check, not OCR/pixel verification or whole-card coverage.')
