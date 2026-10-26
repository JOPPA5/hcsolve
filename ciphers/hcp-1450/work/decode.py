#!/usr/bin/env python3
"""Decode explicitly manual outline/dot tokens; not OCR."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
SHAPES = ['BR', 'B', 'BL', 'R', 'C', 'L', 'TR', 'T', 'TL']
KEY = {f'{s}{n}': chr(65+9*(n-1)+i)
       for n in (1, 2, 3) for i, s in enumerate(SHAPES)
       if 9*(n-1)+i < 26}
inverse = {v: k for k, v in KEY.items()}
for name, digest in json.loads((ROOT/'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((ROOT/'source'/name).read_bytes()).hexdigest() == digest, name
count = 0
for line in (ROOT/'work/transcription.txt').read_text().splitlines():
    if not line or line.startswith('#'):
        continue
    out = []
    for token in line.split():
        if token in KEY:
            out.append(KEY[token])
            assert inverse[KEY[token]] == token
            count += 1
        elif token == '|':
            out.append(' ')
        elif token == '=?':
            out.append('?')
        elif token == "{won't}":
            out.append("{won't}")
        else:
            raise ValueError(token)
    print(''.join(out))
print(f'{count} cipher letters; source hashes and token/key roundtrips passed.')
print('Manual reading; merged/overdrawn dots remain visually uncertain. See SOLUTION.md.')
