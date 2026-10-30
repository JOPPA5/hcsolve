#!/usr/bin/env python3
"""HCP 1395: verify source hashes, then decrypt the manual transcript with Caesar -1.

Run from the repo root:  python3 -I ciphers/hcp-1395/work/decode.py
"""
from pathlib import Path
import hashlib, json, string

p = Path(__file__).resolve().parents[1]
for f, h in json.loads((p / 'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((p / 'source' / f).read_bytes()).hexdigest() == h, f'hash mismatch: {f}'
print('source hashes OK')

A = string.ascii_uppercase
DEC = str.maketrans(A + A.lower(), A[-1] + A[:-1] + A[-1] + A[:-1])   # cipher X -> plain X-1
ENC = str.maketrans(A[-1] + A[:-1], A)

d = json.loads((p / 'work/transcription.json').read_text())
n, lines = 0, []
for r in d['rows']:
    c = r['cipher']
    pt = c.translate(DEC).upper()
    assert pt.translate(ENC) == c.upper(), r['region']        # round trip
    n += sum(ch.isalpha() for ch in c)
    lines.append(pt)
    print(f"{r['region']:16s} {c:18s} -> {pt}")
print(f'{n} cipher letters, all decrypted by one fixed shift (no unknowns)')
print('ordinary (not shifted):', d['ordinary_context']['heading'], '|', d['ordinary_context']['date'])
print('PLAINTEXT:', ' '.join(lines))
