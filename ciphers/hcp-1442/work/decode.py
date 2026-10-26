#!/usr/bin/env python3
"""Decode explicitly manual glyph tokens; source checksums do not validate pixels."""
from pathlib import Path
import hashlib,json,string
root=Path(__file__).resolve().parents[1]
for name,digest in json.loads((root/'work/source-sha256.json').read_text()).items():
 assert hashlib.sha256((root/'source'/name).read_bytes()).hexdigest()==digest,name
shapes=['BR','B','BL','R','C','L','TR','T','TL']
key={s+str(n):string.ascii_uppercase[(n-1)*9+i] for n in (1,2,3) for i,s in enumerate(shapes) if (n-1)*9+i<26}
rev={v:k for k,v in key.items()}
data=json.loads((root/'work/transcription.json').read_text())
total=0
for row in data['rows']:
 text=''.join(key[t] for t in row['tokens'])
 assert ''.join(c for c in row['display'] if c.isalpha())==text,(row['region'],text)
 assert [rev[c] for c in text]==row['tokens']
 print(row['region']+': '+row['display'])
 total+=len(text)
print(str(total)+' cipher letters decoded; manual transcription, no OCR.')
