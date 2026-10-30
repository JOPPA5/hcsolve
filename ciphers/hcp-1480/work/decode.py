#!/usr/bin/env python3
"""HCP1480: decode the manual shape transcription with the shape key.
Run from repo root: python3 -I ciphers/hcp-1480/work/decode.py"""
from pathlib import Path
import hashlib, json
p = Path(__file__).resolve().parents[1]
for name, digest in json.loads((p/'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((p/'source'/name).read_bytes()).hexdigest() == digest, name
key = json.loads((p/'work/key.json').read_text())
total = 0
lines = []
for line in (p/'work/transcription.txt').read_text().splitlines():
    words = []
    for group in line.split('/'):
        toks = group.split()
        for t in toks:
            assert t in key and key[t], t
        total += len(toks)
        words.append(''.join(key[t] for t in toks))
    lines.append(' '.join(words))
print('\n'.join(lines))
print(f'-- {total} signs, all mapped; source hashes OK')
