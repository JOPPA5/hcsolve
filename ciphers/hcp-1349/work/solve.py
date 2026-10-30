#!/usr/bin/env python3
"""HCP 1349: verify source hashes, decode work/transcription.json with Caesar -1.
Run from repo root: python3 -I ciphers/hcp-1349/work/solve.py"""
from pathlib import Path
import hashlib, json, string
p = Path(__file__).resolve().parents[1]
for n, h in json.loads((p/'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((p/'source'/n).read_bytes()).hexdigest() == h, 'hash mismatch: ' + n
print('source hashes OK')
U, L = string.ascii_uppercase, string.ascii_lowercase
dec = str.maketrans(U + L, U[-1] + U[:-1] + L[-1] + L[:-1])
enc = str.maketrans(U + L, U[1:] + U[0] + L[1:] + L[0])
d = json.loads((p/'work/transcription.json').read_text())
n = 0
for row in d['rows']:
    out = []
    for f in row['fields']:
        t = f['text']
        if f['kind'] == 'cipher':
            n += sum(c.isalpha() for c in t)
            assert t.translate(dec).translate(enc) == t
            out.append(t.translate(dec).upper())
        elif f['kind'] == 'literal':
            out.append('[' + t + ']')
        else:
            out.append(t)
    print(f"{row['region']:8} {' '.join(out)}")
print(f'{n} enciphered letters decoded, round trip OK; [..] = abbreviation groups kept literal')
