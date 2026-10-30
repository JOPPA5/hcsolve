#!/usr/bin/env python3
"""HCP 1193: verify source hashes, then decode work/transcription-full.txt
with the numbered-Pigpen key. Run from the repo root:

    python3 -I ciphers/hcp-1193/work/decode_full.py
"""
from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parents[1]

HASHES = {
    'address-large.jpg': '65de4e16d3e10c29cff949d88235ff7a79c5a4e04707311c11dcc7e4a6813a40',
    'address-thumb.jpg': 'f62ab217a22803dee3933e75f47c86431e33fa706be17b1091e69dea0aef135e',
    'metadata.md': 'f91168e72605b1152b3cd9ed18bbba21f76c7b60d47e740af855f8278ff52646',
    'picture-large.jpg': '72360ebc23f9347645ce537c8b71235b729578e5fb3c52bf0eb105e07a0b4b38',
    'picture-original.jpg': 'd2f76e4e4d387fad96727d2b7be65704709753c43f5b4a9257b8c87a42d5e617',
}
for name, digest in HASHES.items():
    actual = hashlib.sha256((ROOT / 'source' / name).read_bytes()).hexdigest()
    if actual != digest:
        raise SystemExit(f'source hash mismatch: {name}')
print('source hashes OK (5 files)\n')

# Nine outlines in grid order; numeral n selects letters 9(n-1)+1 .. 9n.
SHAPES = ['BR', 'B', 'BL', 'R', 'C', 'L', 'TR', 'T', 'TL']
KEY = {}
for n in (1, 2, 3):
    for i, s in enumerate(SHAPES):
        k = (n - 1) * 9 + i
        if k < 26:
            KEY[f'{s}{n}'] = chr(65 + k)
CLEAR = {'|': ' ', '&': '&', ',': ',', '.': '.', '?': '?', '-': '-', '~': ' ~'}

counts = {'sign': 0, 'restored': 0, 'ambiguous': 0, 'nokey': 0}


def dec(tok):
    if tok in CLEAR:
        return CLEAR[tok]
    counts['sign'] += 1
    if tok.startswith('NOKEY:'):
        counts['nokey'] += 1
        return f'<{tok[6:]}>'
    if tok.startswith('*'):
        counts['restored'] += 1
        return '{' + KEY[tok[1:]] + '}'
    if '/' in tok:
        counts['ambiguous'] += 1
        return '[' + '/'.join(KEY[t] for t in tok.split('/')) + ']'
    return KEY[tok]


for line in (ROOT / 'work/transcription-full.txt').read_text().splitlines():
    if line.strip() and not line.startswith('#'):
        print(''.join(dec(t) for t in line.split()))

print(f"\n{counts['sign']} cipher signs: {counts['restored']} restored {{}}, "
      f"{counts['ambiguous']} ambiguous [], {counts['nokey']} outside the key <>; "
      "~ = signs under the stamp, not legible.")
