#!/usr/bin/env python3
"""Decode manual working transcription, preserving unresolved line and alternatives."""
import hashlib,json,string
from pathlib import Path
root=Path(__file__).resolve().parents[1]
for name,digest in json.loads((root/'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((root/'source'/name).read_bytes()).hexdigest()==digest,name
key=str.maketrans(string.ascii_uppercase,string.ascii_uppercase[::-1])
data=json.loads((root/'work/transcription-atbash.json').read_text())
count=0
for row in data['rows']:
    if row['cipher'] is None:
        print('[unresolved line; candidate readings: '+', '.join(s+' -> '+s.translate(key) for s in row['alternatives'])+']')
    else:
        out=row['cipher'].translate(key)
        assert out.translate(key)==row['cipher']
        print(out)
        count+=len(row['cipher'])
print(f'{count} letters outside unresolved line; manual transcription remains a hypothesis, not pixel validation.')
