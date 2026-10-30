#!/usr/bin/env python3
"""hcp-1462: full decipherment of the address-side cipher.

Route transposition per physical line: the plaintext's odd-position letters
are written first, then its even-position letters in reverse order. To
decipher, read leftmost, rightmost, 2nd, 2nd-from-right, ... inward.
Run from the repository root:  python3 ciphers/hcp-1462/work/decode-full.py
"""
from pathlib import Path
import hashlib, json

d = Path(__file__).resolve().parents[1]
for name, digest in json.loads((d / 'work/source-sha256.json').read_text()).items():
    got = hashlib.sha256((d / 'source' / name).read_bytes()).hexdigest()
    assert got == digest, f'source hash mismatch: {name}'

def decrypt(c):
    out, lo, hi = [], 0, len(c) - 1
    while lo <= hi:
        out.append(c[lo]); lo += 1
        if lo <= hi:
            out.append(c[hi]); hi -= 1
    return ''.join(out)

def encrypt(p):
    return p[0::2] + p[1::2][::-1]

lines = [l.strip() for l in (d / 'work/transcription.txt').read_text().splitlines()
         if l.strip() and not l.startswith('#')]
total = 0
for c in lines:
    p = decrypt(c)
    assert encrypt(p) == c
    total += len(c)
    print(f'{c:20s} -> {p}')
print(f'{len(lines)} lines, {total} cipher letters, all decrypted; source hashes OK.')
