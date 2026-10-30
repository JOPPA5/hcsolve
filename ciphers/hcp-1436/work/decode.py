#!/usr/bin/env python3
"""Decode frozen manual excerpts only; uncertain/cancelled marks are excluded."""
from pathlib import Path
import hashlib, json
p = Path(__file__).resolve().parents[1]
for name, digest in json.loads((p/'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((p/'source'/name).read_bytes()).hexdigest() == digest
codes = '.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..'.split()
key = dict(zip(codes, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
inverse = {v:k for k,v in key.items()}
data = json.loads((p/'work/transcript.json').read_text())
count = 0
for excerpt in data['excerpts']:
    words = []
    for word in excerpt['codes'].split(' // '):
        tokens = word.split(' / ')
        plain = ''.join(key[token] for token in tokens)
        assert [inverse[c] for c in plain] == tokens
        count += len(plain)
        words.append(plain)
    print(excerpt['position'] + ': ' + ' '.join(words))
print(f'{count} frozen excerpt letters; other marks remain unresolved.')
print('Source hashes and mapping roundtrips pass; not OCR/full-message proof.')
