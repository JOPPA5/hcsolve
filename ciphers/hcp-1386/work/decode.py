#!/usr/bin/env python3
"""Verify immutable sources and decrypt a partial manual transcription."""
from pathlib import Path
import hashlib
import json
import string

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / 'work/transcription.json').read_text())
for name, expected in data['source_sha256'].items():
    actual = hashlib.sha256((ROOT / 'source' / name).read_bytes()).hexdigest()
    if actual != expected:
        raise SystemExit(f'Source hash mismatch: {name}')
table = str.maketrans(string.ascii_uppercase + string.ascii_lowercase,
                      'ZABCDEFGHIJKLMNOPQRSTUVWXYzabcdefghijklmnopqrstuvwxy')
inverse = str.maketrans('ZABCDEFGHIJKLMNOPQRSTUVWXYzabcdefghijklmnopqrstuvwxy',
                        string.ascii_uppercase + string.ascii_lowercase)
count = 0
print('Partial manual transcript; image handwriting is not automatically recognized.')
for row in data['rows']:
    if 'omission_before' in row:
        print('[UNRESOLVED: ' + row['omission_before'] + ']')
    cipher = row['cipher']
    plain = cipher.translate(table)
    assert plain.translate(inverse) == cipher
    count += sum(c in string.ascii_letters for c in cipher)
    print(plain)
    if 'omission_after' in row:
        print('[UNRESOLVED: ' + row['omission_after'] + ']')
print(f'{count} frozen alphabetic positions. Source hashes and round-trip verified.')
