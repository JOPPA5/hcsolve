#!/usr/bin/env python3
"""HCP 1362: Caesar -1 decode of the manual transcription; checks source hashes."""
import hashlib, json, string, sys
from pathlib import Path
d = Path(__file__).resolve().parents[1]
H = {'source/picture-large.jpg': 'c40cd421f348cb525a0d920b2643fcc499ef653de29bc7e9170f42736dd2a7ad',
     'source/address-large.jpg': '703945425aa314230d2fde79f26a47ba84e2b02acdcf8d28bd1f7ce023ac8441',
     'work/hires/pc_hcp_43_pic.JPG': 'ee4e84d803c5bd9bff000671155d8ee41206f229b17c02d69b7be7f35375e148',
     'work/hires/pc_hcp_43_adr.JPG': '64cd0a67dd9c208654f0fac5412746aa60d446edda6009d2d5ad470b5e63e013'}
for f, h in H.items():
    if hashlib.sha256((d / f).read_bytes()).hexdigest() != h:
        sys.exit('HASH MISMATCH ' + f)
print('source hashes OK')
L, U = string.ascii_lowercase, string.ascii_uppercase
dec = str.maketrans(L + U, U[-1] + U[:-1] + U[-1] + U[:-1])
enc = str.maketrans(U, L[1:] + L[0])
t = json.loads((d / 'work/transcription.json').read_text())
n = 0
for line in t['lines']:
    o = []
    for kind, s in line:
        p = s.translate(dec)
        assert p.translate(enc) == s.lower()
        n += len(s); o.append(p)
    print(' '.join(o))
print('[plain closing]', t['closing_plain'])
print(f'{n} enciphered letters decoded by one key')
