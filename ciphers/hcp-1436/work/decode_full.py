#!/usr/bin/env python3
"""Full decode of HCP 1436: check source hashes, then decode work/full-transcript.json
with the standard International Morse alphabet. Run from the repo root:
    python3 -I ciphers/hcp-1436/work/decode_full.py
"""
from pathlib import Path
import hashlib, json

p = Path(__file__).resolve().parents[1]
for name, digest in json.loads((p / 'work/source-sha256.json').read_text()).items():
    got = hashlib.sha256((p / 'source' / name).read_bytes()).hexdigest()
    assert got == digest, f'hash mismatch: {name}'

codes = ('.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- '
         '.-. ... - ..- ...- .-- -..- -.-- --..').split()
key = dict(zip(codes, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

data = json.loads((p / 'work/full-transcript.json').read_text())
words, marked, letters = [], 0, 0
for line in data['lines']:
    for w in line.strip().rstrip('/').strip().split(' // '):
        w = w.strip()
        if not w:
            continue
        if w.startswith('['):
            words.append(w)
            continue
        out = ''
        for tok in w.split(' / '):
            flag = tok.startswith('!')
            ch = key[tok.lstrip('!')]   # KeyError = not a Morse letter
            out += ch.lower() if flag else ch
            marked += flag
            letters += 1
        words.append(out)
text = ' '.join(words)
print(text)
print(f'{letters} letters decoded ({marked} disclosed restorations/judgments shown in lower case); '
      'source hashes OK.')
