#!/usr/bin/env python3
"""HCP 1407: verify source hashes, decode work/transcription-v2.json with Caesar -1.
Run from repo root: python3 -I ciphers/hcp-1407/work/solve.py"""
from pathlib import Path
import hashlib, json, string
p = Path(__file__).resolve().parents[1]
for n, h in json.loads((p/'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((p/'source'/n).read_bytes()).hexdigest() == h, 'hash mismatch: ' + n
print('source hashes OK')
U, L = string.ascii_uppercase, string.ascii_lowercase
key = str.maketrans(U + L, U[-1] + U[:-1] + L[-1] + L[:-1])   # cipher letter -> previous letter
d = json.loads((p/'work/transcription-v2.json').read_text())
n = 0
for row in d['rows']:
    out = []
    for f in row['fields']:
        if f['kind'] == 'cipher':
            n += sum(c.isalpha() for c in f['text'])
            out.append(f['text'].translate(key).upper())
        elif f['kind'] == 'literal':
            out.append('[' + f['text'] + ']')
        else:
            out.append(f['text'])
    print(f"{row['region']:8} {' '.join(out)}")
print(f'{n} enciphered letters decoded; [..] = initial groups kept literal')
