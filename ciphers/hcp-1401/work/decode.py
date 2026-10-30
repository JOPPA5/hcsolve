#!/usr/bin/env python3
"""Caesar-1 on the manual transcript; no automatic image recognition."""
from pathlib import Path
import hashlib,json,string
root=Path(__file__).resolve().parents[1]
for name,digest in json.loads((root/'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((root/'source'/name).read_bytes()).hexdigest()==digest,name
alphabet=string.ascii_uppercase
key=dict(zip(alphabet,alphabet[-1:]+alphabet[:-1]))
def dec(s):return ''.join(key.get(c.upper(),c) for c in s)
data=json.loads((root/'work/transcription.json').read_text());count=0
for row in data['rows']:
    out=[]
    for field in row:
        if field['kind']=='cipher':
            out.append(dec(field['text']));count+=sum(c.isascii() and c.isalpha() for c in field['text'])
        elif field['kind']=='ambiguous':
            out.append('[UNRESOLVED raw h/l/1; if cipher letters: G/K; numeral status unproved]')
        else:out.append(field['text'])
    print(' '.join(out))
assert count==16
print('16 frozen letters, one unresolved narrow-stem sign; source hashes checked. PARTIAL.')
