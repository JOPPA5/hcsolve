#!/usr/bin/env python3
"""Reproduce the explicitly partial manual reading; no pixel-to-text claim."""
from pathlib import Path
import hashlib
import json
import string

base = Path(__file__).resolve().parents[1]
expected = {
    'address.jpg': '5d3920d8c9d77569101046f582bed51d3deab473e94a9dd6c9803a9527cff617',
    'picture.jpg': '31c4b0d26c4a0bfaf0dcd6e8978eecedca70b83b57ed01202e612fbb2dbb8191',
}
for name, digest in expected.items():
    actual = hashlib.sha256((base / 'source' / name).read_bytes()).hexdigest()
    if actual != digest:
        raise SystemExit(f'Source hash mismatch: {name}')
data = json.loads((base / 'work' / 'transcript.json').read_text())
alphabet = string.ascii_uppercase
mapping = str.maketrans(alphabet + alphabet.lower(),
                        alphabet[-1:] + alphabet[:-1] +
                        (alphabet[-1:] + alphabet[:-1]).lower())
print('PARTIAL MANUAL READING; ? and [?] are unresolved ink, not ciphertext letters.')
for line in data['lines']:
    print(line.translate(mapping))
print('Frozen alphabetic positions:', sum(c.isascii() and c.isalpha()
                                        for line in data['lines'] for c in line))
print('No independent image recognition is performed.')
