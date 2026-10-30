#!/usr/bin/env python3
"""Additional scan-led, deliberately partial checks; no place-name completion."""
from pathlib import Path
import hashlib, json

p = Path(__file__).resolve().parents[1]
for name, digest in json.loads((p / 'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((p / 'source' / name).read_bytes()).hexdigest() == digest
codes = '.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..'.split()
key = dict(zip(codes, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

def decode(tokens):
    return ''.join(key[token] for token in tokens.split())

# Manual traces from original picture-large.jpg, bottom row y=600..610.
# x centres (approximate source pixels), left to right:
# N: 65 dash, 85 dot; E: 130 dot;
# L: 175 dot, 194 dash, 211 dot, 230 dot;
# C: 305 dash, 328 dot, 351 dash, 374 dot.
prefix = '-. . .-.. -.-.'
assert decode(prefix) == 'NELC'
print('Picture row 3 frozen prefix:', prefix, '=>', decode(prefix))
print('NELC is a literal partial reading, not a claimed English word/place name.')
print('Remaining row-3 dots/crossing strokes and terminal question-like mark excluded.')

# Address final row: the same initial run can be divided two ways.
for tokens in ('- .-. .--- ..-.', '-.-. .--- ..-.'):
    print('Address final-row segmentation alternative:', tokens, '=>', decode(tokens))
print('Neither segmentation establishes an expanded signature or complete plaintext.')
print('Original source hashes passed. Manual traces are not independent image recognition.')
