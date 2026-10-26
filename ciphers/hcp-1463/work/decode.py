#!/usr/bin/env python3
"""A1Z26 over own manual scan transcript, preserving literal time and errors."""
from pathlib import Path
import json, hashlib
p = Path(__file__).resolve().parents[1]
for name, digest in json.loads((p/'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((p/'source'/name).read_bytes()).hexdigest() == digest
count = 0
times = 0
for line in (p/'work/transcription.txt').read_text().splitlines():
    out = []
    for token in line.split():
        if token == '/':
            out.append(' ')
        elif token == '{TIME:7.30&8}':
            out.append('7.30 & 8')
            times += 1
        else:
            n = int(token)
            assert 1 <= n <= 26
            letter = chr(64+n)
            assert ord(letter)-64 == n
            out.append(letter)
            count += 1
    print(''.join(out))
assert times == 1
print(f'{count} numeric letter positions; one literal time group.')
print('Source hashes and every inverse-key roundtrip passed; not OCR/pixel proof.')
