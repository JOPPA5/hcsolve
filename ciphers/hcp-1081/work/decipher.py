#!/usr/bin/env python3
"""HCP 1081: verify source hashes, then undo the line-wise reversal.
Each body row was written backwards letter by letter (whole row reversed,
so both word order and letters within words are reversed). Decipherment =
reverse every row string; rows are then read top to bottom.
Run from the repository root:  python3 ciphers/hcp-1081/work/decipher.py
"""
from pathlib import Path
import hashlib
d = Path(__file__).resolve().parents[1]
checks = {
 'address.jpg': '80c1cd93d4ce3d041c83f9494778544a52aef8d934a1d3e0025f6240ddbd9c42',
 'picture.jpg': '1d862b81164caf04a465b39d37ec30a3ab2b716fea017e40b333a43a02ada0b7',
 'metadata.md': '4d062211111ea8929e5124dbb019fafed015c10ebce26af7a2d397fc41836972',
 'schrodel-2021.pdf': '3e2ff353d1fa438d59f08fd4a984923b1e04e966bc9db09651108378f63a9580',
}
for name, exp in checks.items():
    got = hashlib.sha256((d / 'source' / name).read_bytes()).hexdigest()
    assert got == exp, (name, got)
print('source SHA256: 4/4 OK')
rows = [l.strip() for l in (d / 'work' / 'transcription.txt').read_text().splitlines()
        if l.strip() and not l.startswith('#')]
print('Header (plain): Dear M / Just a card / thanking you / for letter')
plain = []
for i, r in enumerate(rows, 1):
    p = r[::-1]
    plain.append(p)
    print(f'B{i}: {r:<22} -> {p}')
print('Body plaintext:', ' / '.join(plain), '+ x')
