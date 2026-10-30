#!/usr/bin/env python3
"""HCP 1348: verify hashes, decrypt the manual transcript with Caesar -1.
Run from the repo root:  python3 -I ciphers/hcp-1348/work/decode.py
"""
from pathlib import Path
import hashlib, json, string
p = Path(__file__).resolve().parents[1]
for f, h in json.loads((p/'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((p/f).read_bytes()).hexdigest() == h, f
print('source hashes OK')
A = string.ascii_uppercase
DEC = str.maketrans(A+A.lower(), A[-1]+A[:-1]+A[-1]+A[:-1])
ENC = str.maketrans(A[-1]+A[:-1], A)
d = json.loads((p/'work/transcription.json').read_text())
n, out = 0, []
for r in d['rows']:
    c = r['cipher']; pt = c.translate(DEC).upper()
    assert pt.translate(ENC) == c.upper()
    n += sum(ch.isalpha() for ch in c); out.append(pt)
    print(f"{r['region']:18s} {c:20s} -> {pt}")
print(n, 'cipher letters, one fixed shift')
print('LITERAL :', ' / '.join(out))
print('READING : WITH LOVE AND [K]ISSES FROM [Y]OURS / L.O.O. = LOO')
print('(square brackets are editorial, not deciphered; see SOLUTION.md uncertainties 1, 2; the capital of M.p.p. is uncertainty 3)')
print('ordinary:', d['ordinary']['date'], '|', d['ordinary']['address'])
