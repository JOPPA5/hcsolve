#!/usr/bin/env python3
"""hcp-1075: decode the frozen manual American-Morse transcription.
Run from the repo root:  python3 -I ciphers/hcp-1075/work/decode.py
Checks source and hi-res hashes, decodes every transcribed letter with the
American (landline) Morse key and checks the key/inverse roundtrip.
It decodes the manual transcription, not the image pixels."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HASHES = {
    'source/address-large.jpg': 'b5dc84df2070bc288954590f34a092806fbed2b3b204146bd46927c7bd5bcbcc',
    'source/picture-large.jpg': 'c5c3becff97f20261eb0705bea96c0637c330be0c1d7e3d59573c4ec12b2e276',
    'work/hires/cpc_--_USA__USA___adr.jpg': 'e63a91fc52cb194d8db01187f50f7201b5c80df7b2c85d9feba61bdb66b94e30',
    'work/hires/cpc_--_USA__USA___pic.jpg': '7ac2968ef92f8d375e57fb70693744bf0ecc56345d29a2208ef6338d39dbcf34',
}
# American Morse ('.' dot, '-' dash, '=' long dash, space = internal gap)
KEY = {
    'A': '.-', 'B': '-...', 'C': '.. .', 'D': '-..', 'E': '.',
    'F': '.-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '-.-.',
    'K': '-.-', 'L': '=', 'M': '--', 'N': '-.', 'O': '. .',
    'P': '.....', 'Q': '..-.', 'R': '. ..', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '.-..',
    'Y': '.. ..', 'Z': '... .',
    '1': '.--.', '2': '..-..', '3': '...-.', '4': '....-', '5': '---',
    '6': '......', '7': '--..', '8': '-....', '9': '-..-', '0': '==',
}
INV = {v: k for k, v in KEY.items()}
assert len(INV) == len(KEY)

for rel, h in HASHES.items():
    assert hashlib.sha256((ROOT / rel).read_bytes()).hexdigest() == h, rel
data = json.loads((ROOT / 'work/transcript.json').read_text())
words, n = [], 0
for w in data['words']:
    txt = ''.join(INV[c] for c in w)
    assert [KEY[ch] for ch in txt] == w
    n += len(txt)
    words.append(txt)
print(' '.join(words))
print(f'{len(words)} words, {n} signs decoded; hashes and key roundtrip OK.')
# Literal form (review 1, finding 4): the strictest pixel reading of the
# word-sense points, with the card's own word division (no comma between
# I and WILL, nor between AKRON and OHIO). (word index, letter index) are
# 0-based; the WILL dashes are middle-length, so T is shown as the
# strict alternative in brackets.
LITERAL = {(5, 0): 'O', (6, 2): '[L/T]', (6, 3): '[L/T]', (8, 2): 'I'}
lit = [[LITERAL.get((i, j), ch) for j, ch in enumerate(w)] for i, w in enumerate(words)]
lit = [''.join(w) for w in lit]
lit_line = ' '.join(lit[:5]) + ' ' + lit[5] + lit[6] + ' ' + ' '.join(lit[7:15]) + ' ' + lit[15] + lit[16]
print('Literal form (strict pixel reading, card word division):')
print('  ' + lit_line)
print('Flagged readings (word sense involved):')
for k, v in data['flags'].items():
    print(f'  {k}: {v}')
