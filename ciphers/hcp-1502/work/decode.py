#!/usr/bin/env python3
"""HCP 1502: check source hashes, decode the full manual Morse transcription.
Run from the repo root:  python3 ciphers/hcp-1502/work/decode.py"""
from pathlib import Path
import hashlib, json
root = Path(__file__).resolve().parents[1]
for name, digest in json.loads((root / 'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((root / 'source' / name).read_bytes()).hexdigest() == digest, name
codes = ('.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. '
         '... - ..- ...- .-- -..- -.-- --..').split()
key = dict(zip(codes, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
key['&'] = '&'
blocks = {'A': [], 'B': []}
for line in (root / 'work/transcription.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    label, body = line.split('#', 1)[0].split(':', 1)  # text after '#' is a comment
    words = [''.join(key[g] for g in w.split()) for w in body.split('/')]
    blocks[label[0]].append(' '.join(w for w in words if w) + (' ' if body.rstrip().endswith('/') else ''))
letters = 0
for b, rows in blocks.items():
    for r in rows:
        letters += sum(c.isalpha() for c in r)
text = {b: ' '.join(''.join(rows).split()) for b, rows in blocks.items()}
print('P.S. (top block):  P.S. ' + text['A'])
print('Main letter:       ' + text['B'])
print(f'{letters} Morse letters decoded, all groups valid. Source hashes OK.')
