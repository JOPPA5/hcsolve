#!/usr/bin/env python3
"""HCP 1387: check source hashes, decrypt the full manual transcript with Caesar -1."""
import hashlib, json, sys
from pathlib import Path

base = Path(__file__).resolve().parents[1]
data = json.loads((base / 'work/transcript_full.json').read_text())
for name, expected in data['source_sha256'].items():
    actual = hashlib.sha256((base / name).read_bytes()).hexdigest()
    if actual != expected:
        sys.exit(f'HASH MISMATCH: {name}')
print('source hashes OK')

def shift(text, k):
    out = []
    for c in text:
        if c.isascii() and c.isalpha():
            a = ord('A' if c.isupper() else 'a')
            c = chr(a + (ord(c) - a + k) % 26)
        out.append(c)
    return ''.join(out)

n = 0
for row in data['rows']:
    p = shift(row, -1)
    assert shift(p, 1) == row
    n += sum(c.isascii() and c.isalpha() for c in row)
    print(f'{row:22s} -> {p}')
print(f'{n} cipher letters decrypted with one key (each cipher letter = plaintext letter + 1).')
print('Plain fields (not shifted):', '; '.join(f'{k}: {v}' for k, v in data['plain_fields'].items()))
