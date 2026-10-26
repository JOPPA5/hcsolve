#!/usr/bin/env python3
"""Observed Pigpen alternatives and separately labelled contextual word readings."""
from pathlib import Path
import hashlib,json
r=Path(__file__).resolve().parents[1]
for name,digest in json.loads((r/'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((r/'source'/name).read_bytes()).hexdigest()==digest, name
pairs=[('BR','AB'),('B','CD'),('BL','EF'),('R','GH'),('C','IJ'),
       ('L','KL'),('TR','MN'),('T','OP'),('TL','QR'),('V','ST'),('<','UV')]
key={f'{s}{d}':{c} for s,pair in pairs for d,c in enumerate(pair)}
# Rightward wedges occur where prose requires W and Y. No unique value claimed.
key['>0']={'W','Y'}
def values(token):
    if token.startswith('{') and token.endswith('}'):
        return set().union(*(values(t) for t in token[1:-1].split('|')))
    if token.endswith('?'):
        return key[token[:-1]+'0'] | key[token[:-1]+'1']
    return key[token]
expected=['HOUSE','LOUISE','PORCH','LONG','WOODEN','STORE','SALOON','BARBER',
          'SHOP','FRANKS','LIVERY','STABLES','LIBRARY']
rows=[s.split() for s in (r/'work/transcription.txt').read_text().splitlines()
      if s and not s.startswith('#')]
assert len(rows)==len(expected)
count=0
for number,(row,word) in enumerate(zip(rows,expected),1):
    observed=[]; contextual=[]; i=0
    for token in row:
        if token=='{cancelled}':
            observed.append('[cancelled]');contextual.append('[cancelled]');continue
        choices=values(token)
        assert word[i] in choices, (number,token,word[i],choices)
        observed.append(next(iter(choices)) if len(choices)==1 else '['+'/'.join(sorted(choices))+']')
        contextual.append(word[i]);i+=1;count+=1
    assert i==len(word)
    print(f'{number:02}: observed '+''.join(observed)+' | contextual '+''.join(contextual))
    if number==2: print('    plain cursive & follows LOUISE (not cipher)')
    if number==9: print('    plain cursive & between SHOP and FRANKS (not cipher)')
print(f'\n{count} non-cancelled cipher positions in 13 contextual word readings.')
print('Rightward >0 is ambiguous W/Y; dots/outlines retained as alternatives.')
print('Source hashes and candidate-membership checks passed; not a unique-key roundtrip or OCR.')
