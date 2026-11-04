#!/usr/bin/env python3
"""hcp-1094: decode the numeric (Greek-style place-value) alphabet.
Run from the repo root:  python3 -I ciphers/hcp-1094/work/decode.py
Checks the source hashes, then prints the plaintext."""
import hashlib, os, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASHES = {
    'source/picture-large.jpg': '443b93a2c1dad2a4ba380cc9ae7cf2234fff345eb7cdc9565c7a795443b35914',
    'source/address-large.jpg': 'e22754c968a7ba4f91197f794234aff14f16cd69cabc43066d2572e5650d7156',
    'work/hires/cpc_1912-03-0_AT_Schneegattern_AT_Schneegattern__adr.jpg': '76f60d4204338fd90c71e120826969ebe80917ce30f342a8be676e4928cf5e48',
}
for p, h in HASHES.items():
    got = hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest()
    if got != h:
        sys.exit(f'HASH MISMATCH {p}')
print('source hashes OK')
# Key: a..i = 1..9, k..s = 10..90, t..w = 100..400 (German alphabet without j; i/j share 9)
letters = 'abcdefghi' + 'klmnopqrs' + 'tuvwxyz'
values = list(range(1, 10)) + list(range(10, 100, 10)) + list(range(100, 800, 100))
KEY = dict(zip(values, letters))
# Transcription (address side, left half, written vertically top-to-bottom;
# columns read right to left; dots separate letters, wider gaps separate words).
# A trailing '"' marks umlaut dots written above a number group (only 200" = ü).
COLUMNS = [
    ['400.200\".40.90.3.8.100'],          # column 1 (nearest the divider)
    ['4.9.80', '4.5.9.40'],             # column 2
    ['9.50.8.1.40.40'],                 # column 3 (leftmost)
]
words = []
for col in COLUMNS:
    for w in col:
        out = ''
        for n in w.split('.'):
            uml = n.endswith('"')
            ch = KEY[int(n.rstrip('"'))]
            out += {'a': 'ä', 'o': 'ö', 'u': 'ü'}[ch] if uml else ch
        words.append(out)
print(' '.join(words))
