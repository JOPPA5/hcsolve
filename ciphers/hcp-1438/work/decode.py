#!/usr/bin/env python3
"""Decode explicitly manual shape/dot tokens, not OCR."""
from pathlib import Path
import hashlib
import json
root = Path(__file__).resolve().parents[1]
shapes = ['BR','B','BL','R','C','L','TR','T','TL']
key = {f'{s}{n}': chr(65+9*(n-1)+i)
       for n in (1,2,3) for i,s in enumerate(shapes)
       if 9*(n-1)+i < 26}
inverse = {v:k for k,v in key.items()}
for name,digest in json.loads((root/'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((root/'source'/name).read_bytes()).hexdigest() == digest,name
count=0
for line in (root/'work/transcription.txt').read_text().splitlines():
    if not line or line.startswith('#'): continue
    out=[]
    for token in line.split():
        if token=='|': out.append(' '); continue
        out.append(key[token]); count+=1
        assert inverse[key[token]] == token
    print(''.join(out))
assert count == 36
print('36 cipher letters; source hashes and token/key roundtrips passed.')
print('Manual transcription, not image recognition. Literal RLEAS retained.')
