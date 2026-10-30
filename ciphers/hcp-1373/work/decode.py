#!/usr/bin/env python3
"""HCP 1373: Caesar -1 decryption of the full manual transcript; checks source hashes."""
from pathlib import Path
import hashlib, json, string
here = Path(__file__).resolve().parent
root = here.parent
for name, digest in json.loads((here / 'source-sha256.json').read_text()).items():
    assert hashlib.sha256((root / 'source' / name).read_bytes()).hexdigest() == digest, name
print('source hashes OK')
A = string.ascii_uppercase
dec_key = dict(zip(A, A[-1:] + A[:-1]))
enc_key = {v: k for k, v in dec_key.items()}
dec = lambda s: ''.join(dec_key.get(c.upper(), c) for c in s)
enc = lambda s: ''.join(enc_key.get(c, c) for c in s)
data = json.loads((here / 'transcription.json').read_text())
n_cipher = n_abbr = 0
print('Heading (plain):', data['ordinary_heading'])
for row in data['rows']:
    out = []
    for f in row:
        t = f['text']
        if f['kind'] == 'cipher':
            p = dec(t)
            assert enc(p).lower() == t.lower(), t
            out.append(p); n_cipher += sum(c.isalpha() for c in t)
        elif f['kind'] == 'abbrev':
            out.append('[' + t + ']'); n_abbr += sum(c.isalpha() for c in t)
        else:
            out.append(t)
    print(' '.join(out))
print(f'{n_cipher} enciphered letters decoded, {n_abbr} abbreviation letters kept literal.')
print('Editorial note: NCIELY is the literal decode of odjfmz; reading NICELY (see SOLUTION.md).')
