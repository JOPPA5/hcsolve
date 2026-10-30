#!/usr/bin/env python3
"""HCP 1433: check source hashes, decode the full manual Morse transcript."""
from pathlib import Path
import hashlib, json
root = Path(__file__).resolve().parents[1]
for name, digest in json.loads((root/'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((root/'source'/name).read_bytes()).hexdigest() == digest, name
codes = ('.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. '
         '... - ..- ...- .-- -..- -.-- --..').split()
key = dict(zip(codes, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
rows = [l for l in (root/'work/transcription-full.txt').read_text().splitlines()
        if l.strip() and not l.startswith('#')]
out = [''.join(key[t.strip()] for t in r.split('/')) for r in rows]
for r in out: print(r)
n = sum(map(len, out)); assert n == 39, n
print(f'{n} letters. Source hashes OK.')
print('Main:  ' + ''.join(out[:5]))
print('Bottom:' + ''.join(out[5:]))
