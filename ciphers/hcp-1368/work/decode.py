#!/usr/bin/env python3
"""HCP 1368: Caesar -1 decode of the manual transcription; checks source hashes.
Kind c = enciphered text; kind a = the unresolved M. h group, printed as written with its shifted value."""
import hashlib, json, string, sys
from pathlib import Path
d = Path(__file__).resolve().parents[1]
H = {'source/picture-large.jpg': '3bbee27db48d007591a45003dd3c6bc1d2a17a835c34e1292c13f06a4e1386da',
     'source/address-large.jpg': '0e27f5c93dbe570ca795ab78f4744601660c651fcc5337fc529b0c11658e7393',
     'work/hires/pc_hcp_49_pic.JPG': 'e3611839b4858436af5da3125d3b9869d9d7d69aaa80c3f5b539dedc8eb041e6',
     'work/hires/pc_hcp_49_adr.JPG': '6aced506be0922964e06381e6eb2ef0989cb7842ff196125809ef029b1000674'}
for f, h in H.items():
    if hashlib.sha256((d / f).read_bytes()).hexdigest() != h:
        sys.exit('HASH MISMATCH ' + f)
print('source hashes OK')
L, U = string.ascii_lowercase, string.ascii_uppercase
dec = str.maketrans(L + U, U[-1] + U[:-1] + U[-1] + U[:-1])
enc = str.maketrans(U, L[1:] + L[0])
t = json.loads((d / 'work/transcription.json').read_text())
print('[plain heading]', t['heading_plain'])
n = a = 0
for line in t['lines']:
    o = []
    for kind, s in line:
        if kind == 'c':
            p = s.translate(dec)
            assert p.translate(enc) == s.lower()
            n += sum(c.isalpha() for c in s); o.append(p)
        else:
            a += sum(c.isalpha() for c in s); o.append('[' + s + ' = ' + s.translate(dec) + '?]')
    print(' '.join(o))
print('[plain date]', t['date_plain'])
print(f'{n} enciphered letters decoded by one key; {a} letters of the unresolved M. h groups (written form, shifted value after =)')
