#!/usr/bin/env python3
"""Decode manual, visibly supported spans; retain every uncertain field."""
from pathlib import Path
import hashlib,json,string
root=Path(__file__).resolve().parents[1]
for name,digest in json.loads((root/'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((root/'source'/name).read_bytes()).hexdigest()==digest,name
alpha=string.ascii_uppercase
key=dict(zip(alpha,alpha[-1:]+alpha[:-1]))
def decode(s):
    return ''.join(key.get(c.upper(),c) for c in s)
count=0
for row in json.loads((root/'work/transcription.json').read_text())['rows']:
    out=[]
    for field in row['fields']:
        if field['kind']=='cipher':
            out.append(decode(field['text']));count+=sum(c.isalpha() and c.isascii() for c in field['text'])
        elif field['kind']=='plain':out.append('[ordinary: '+field['text']+']')
        elif field['kind']=='cipher-alternative':
            out.append('[PROVISIONAL: '+' / '.join(decode(s) for s in field['alternatives'])+']')
        else:out.append('[UNRESOLVED: '+field['description']+']')
    print(row['region']+': '+' '.join(out))
print(f'{count} frozen alphabetic positions decoded; source hashes checked. PARTIAL.')
# Explicitly verify the Day field without converting it into a guessed number.
assert decode('Ebz')=='DAY'
assert decode('joeppst')=='INDOORS'
