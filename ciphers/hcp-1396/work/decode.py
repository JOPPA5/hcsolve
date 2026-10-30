#!/usr/bin/env python3
"""Decode frozen manually transcribed spans, retain unclassified ink."""
from pathlib import Path
import hashlib,json,string
root=Path(__file__).resolve().parents[1]
for name,digest in json.loads((root/'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((root/'source'/name).read_bytes()).hexdigest()==digest,name
key=dict(zip(string.ascii_uppercase,'ZABCDEFGHIJKLMNOPQRSTUVWXY'))
def dec(s):return ''.join(key.get(c.upper(),c) for c in s)
data=json.loads((root/'work/transcription.json').read_text());count=0
for item in data['ordinary']:
    print('ORDINARY:',item['text'])
for row in data['rows']:
    out=[]
    for f in row:
        if f['kind']=='cipher':
            out.append(dec(f['text']));count+=sum(c.isalpha() and c.isascii() for c in f['text'])
        elif f['kind']=='provisional':out.append('[PROVISIONAL '+dec(f['text'])+']')
        else:out.append('[UNRESOLVED '+f['text']+']')
    print(' '.join(out))
print(f'{count} frozen alphabetic positions. Source hashes checked. PARTIAL.')
