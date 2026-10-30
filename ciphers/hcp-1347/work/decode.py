#!/usr/bin/env python3
"""HCP 1347: verify image hashes, then decode the manual transcription with Caesar -1.

Run from the repo root:  python3 -I ciphers/hcp-1347/work/decode.py
Tokens that start with [ are initials kept literal.
Brackets inside a word (Hjs[m]) mark a restored letter: it is decoded, but not legible on the card.
"""
from pathlib import Path
import hashlib, json, re, string

p = Path(__file__).resolve().parents[1]
for f, h in json.loads((p / 'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((p / f).read_bytes()).hexdigest() == h, f'hash mismatch: {f}'
print('hashes OK (4 image files)')

A = string.ascii_uppercase
DEC = str.maketrans(A + A.lower(), A[-1] + A[:-1] + A[-1] + A[:-1])
ENC = str.maketrans(A[-1] + A[:-1], A)

d = json.loads((p / 'work/transcription.json').read_text())
print('clear heading:', d['clear']['heading'])
n, restored, out = 0, 0, []
for r in d['rows']:
    pts = []
    for t in r['tokens']:
        if t.startswith('['):
            pts.append(t)
            continue
        pt = t.translate(DEC).upper()
        assert pt.translate(ENC) == t.upper(), t
        n += sum(c.isalpha() for c in t)
        restored += sum(len(x) for x in re.findall(r'\[(\w+)\]', t))
        pts.append(pt)
    print(f"{r['line']}: {' '.join(r['tokens']):32s} -> {' '.join(pts)}")
    out += pts
print(f'{n} enciphered letters decoded by one fixed shift ({n - restored} read, {restored} restored); 4 initials kept literal')
print('PLAINTEXT:', d['clear']['heading'], ' '.join(out))
