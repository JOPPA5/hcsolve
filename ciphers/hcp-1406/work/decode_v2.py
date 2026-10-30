#!/usr/bin/env python3
"""HCP 1406: verify source hashes, decode work/transcript-v2.json with Caesar -1.

Run from the repo root:  python3 -I ciphers/hcp-1406/work/decode_v2.py
"""
import hashlib, json, string
from pathlib import Path

root = Path(__file__).resolve().parents[1]
for name, digest in json.loads((root / 'work/source-sha256.json').read_text()).items():
    got = hashlib.sha256((root / 'source' / name).read_bytes()).hexdigest()
    assert got == digest, f'hash mismatch: {name}'

U = string.ascii_uppercase
KEY = {c: U[(i - 1) % 26] for i, c in enumerate(U)}  # cipher -> plain


def dec(s):
    return ''.join(KEY.get(ch.upper(), ch) for ch in s)


t = json.loads((root / 'work/transcript-v2.json').read_text())
out, letters = [], 0
for line in t['lines']:
    parts = []
    for kind, text in line:
        if kind == 'cipher':
            parts.append(dec(text))
            letters += sum(ch.isalpha() for ch in text)
        elif kind == 'abbr':
            parts.append('[' + text + ']')
        else:
            parts.append(text)
    out.append(' '.join(parts))
print('\n'.join(out))
assert out == t['expected_plaintext'], 'decoded text differs from expected'
print(f'-- source hashes OK; {letters} enciphered letters decoded with one key (shift -1); '
      'abbreviations E. L. / N. & L. kept literal')
