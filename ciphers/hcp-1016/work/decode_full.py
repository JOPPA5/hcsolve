#!/usr/bin/env python3
"""HCP 1016: decode the complete manual Pigpen shape transcription (incl. DEIN).

Run from repo root:  python3 -I ciphers/hcp-1016/work/decode_full.py
Checks source hashes, decodes every row with ONE fixed key, prints the literal
plaintext and, separately, the editorial normalisation. Not OCR: the shape
tokens were read by eye from enlarged crops of source/picture.jpg.
"""
import hashlib, sys
from pathlib import Path

CIPHER = Path(__file__).resolve().parent.parent
EXPECTED = {
    'picture.jpg': '66ca9429f5d203dd8d6ac8475a64f57533d0bea638f633b51f9fdaa15d134456',
    'address.jpg': 'deb068160ca24ee30164b578dc8dd85c2c7db31036e68ec1ecd989eede52a770',
}
# Shape = strokes drawn: SE=┘ S=⊔ SW=└ E=⊐ O=□ W=⊏ NE=┐ N=⊓ NW=┌ ; '.' = interior dot
KEY = {'SE': 'A', 'S': 'B', 'SW': 'C', 'E': 'D', 'O': 'E', 'W': 'F', 'NE': 'G', 'N': 'H', 'NW': 'I',
       'SE.': 'K', 'S.': 'L', 'SW.': 'M', 'E.': 'N', 'O.': 'O', 'W.': 'P', 'NE.': 'Q', 'N.': 'R', 'NW.': 'S',
       'I': 'T', 'check': 'U', 'up.': 'Z'}
# '|' = the dash-like word separator drawn on the card
ROWS = [
    ('row1 y~438', 'SW. O NW E. O NW. | S. NW O S O |'),
    ('row2 y~486', 'N O N. up. NW NE O E. | SW. SE O check NW. SW N O E.'),
    ('row3 y~518', 'SE. O. SW. SW. O | NW SW N | O NW E. O E. | SE. N. SE O W I NW NE O. E. |'),
    ('row4 y~562', 'NW. SW N S. check SW SE. | check E. E | O NW E. O E. | NW. check O NW. NW. O E. |'),
    ('row5 y~606', 'NE check I O E. SE SW N I SE. check NW. NW.'),
    ('closing x~519-604 y~592 (small)', 'E O NW E.'),
    ('signature x~641-756 y~613', 'I N O O.'),
]
NORMALISED = ("Meinem lieben herzigen Mäuschen komme ich einen kräftigen Schluck "
              "und einen süßen Gutenachtkuss. Dein Theo.")

ok = True
for name, h in EXPECTED.items():
    got = hashlib.sha256((CIPHER / 'source' / name).read_bytes()).hexdigest()
    print(f'SHA256 {name} {got} {"OK" if got == h else "MISMATCH"}')
    ok &= got == h
if not ok:
    sys.exit('source hash mismatch')

n = 0
lines = []
for label, s in ROWS:
    out = ''
    for t in s.split():
        if t == '|':
            out += ' - '
        else:
            out += KEY[t]
            n += 1
    lines.append(out.strip(' -'))
    print(f'{label:34s} {out.strip()}')
assert n == 94, n
print('Glyphs decoded:', n)
print()
print('LITERAL :', ' '.join(lines).replace(' - ', ' '))
print('READING :', NORMALISED)
print('(editorial: MEINES->MEINEM, KRAEFTIGON->KRÄFTIGEN, LIEBE->LIEBEN?, AE/UE/SS->Ä/Ü/ß; see SOLUTION.md)')
