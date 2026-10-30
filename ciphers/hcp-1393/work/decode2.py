#!/usr/bin/env python3
"""HCP 1393: check source hashes, decrypt the complete manual transcription with Caesar -1.
Run from the repository root:  python3 -I ciphers/hcp-1393/work/decode2.py
This replays a manual transcription (no OCR)."""
from pathlib import Path
import hashlib, json, string

ROOT = Path(__file__).resolve().parents[1]
for fn, digest in json.loads((ROOT / 'work/source-sha256.json').read_text()).items():
    got = hashlib.sha256((ROOT / fn).read_bytes()).hexdigest()
    assert got == digest, f'hash mismatch: {fn}'
print('source hashes OK')

def shift(s, k):
    out = []
    for c in s:
        if c in string.ascii_lowercase:
            out.append(string.ascii_lowercase[(string.ascii_lowercase.index(c) + k) % 26])
        elif c in string.ascii_uppercase:
            out.append(string.ascii_uppercase[(string.ascii_uppercase.index(c) + k) % 26])
        else:
            out.append(c)
    return ''.join(out)

def dec(s):
    # the lone kiss-cross 'x' token in L4 is not a letter
    return ' '.join(t if t == 'x' else shift(t, -1) for t in s.split(' '))

data = json.loads((ROOT / 'work/transcription2.json').read_text())
print('[plain heading]', data['plain_heading'])
n = 0
for L in data['lines']:
    c = L['cipher']
    p = dec(c)
    assert ' '.join(t if t == 'x' else shift(t, 1) for t in p.split(' ')) == c  # round trip
    n += sum(ch.isalpha() for t in c.split(' ') if t != 'x' for ch in t)
    pre = (L['shorthand'] + ' ') if L['id'] == 'L6' else ''
    post = (' ' + L['shorthand']) if L['id'] == 'L4' else ''
    tag = '  [shorthand kept literal]' if 'shorthand' in L else ''
    print(f"{L['id']}: {pre}{c}{post}  ->  {pre}{p.upper()}{post}{tag}")
print('enciphered letters decoded:', n)
