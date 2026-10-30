#!/usr/bin/env python3
"""HCP1399: verify source hashes, decode work/transcription-v2.json with Caesar -1.
Initial groups are printed literally plus their Caesar -1 equivalent; they are not expanded."""
from pathlib import Path
import json, hashlib, string
p = Path(__file__).resolve().parents[1]
for f, h in json.loads((p/'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((p/'source'/f).read_bytes()).hexdigest() == h, f
print('source hashes OK')
A = string.ascii_uppercase
dec = str.maketrans(A + A.lower(), (A[-1]+A[:-1]) + (A[-1]+A[:-1]).lower())
enc = str.maketrans(A + A.lower(), (A[1:]+A[0]) + (A[1:]+A[0]).lower())
d = json.loads((p/'work/transcription-v2.json').read_text())
n = 0
for line in d['lines']:
    out = []
    for kind, t in line['tokens']:
        if kind == 'c':
            pt = t.translate(dec); assert pt.translate(enc) == t
            n += sum(ch.isalpha() for ch in t); out.append(pt.upper())
        else:
            out.append(f'[{t} | Caesar-1: {t.translate(dec)}]')
    print(f"{line['region']:10s} " + ' '.join(out))
print(f'{n} enciphered letters decoded with one key; initial groups literal, not expanded.')
