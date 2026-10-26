#!/usr/bin/env python3
"""Decode manual three-count Pigpen tokens, not OCR."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
shapes = ['BR', 'B', 'BL', 'R', 'C', 'L', 'TR', 'T', 'TL']
key = {f'{s}{n}': chr(65+9*(n-1)+i)
       for n in (1,2,3) for i,s in enumerate(shapes) if 9*(n-1)+i<26}
inverse = {v:k for k,v in key.items()}
for name,digest in json.loads((ROOT/'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((ROOT/'source'/name).read_bytes()).hexdigest() == digest, name
count = 0
for line in (ROOT/'work/transcription.txt').read_text().splitlines():
    if not line or line.startswith('#'): continue
    out=[]
    for t in line.split():
        if t=='|': out.append(' '); continue
        out.append(key[t]); count+=1
        assert inverse[key[t]]==t
    print(''.join(out))
print(f'{count} cipher letters; source hashes and token/key roundtrips passed.')
print('Manual transcription; checks do not independently prove image-to-token readings.')
