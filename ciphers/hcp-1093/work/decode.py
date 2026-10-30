#!/usr/bin/env python3
"""HCP1093: decode the Pigpen transcription (interleaved undotted/dotted key)."""
from pathlib import Path
import hashlib, json, sys
root = Path(__file__).resolve().parents[1]
for name, digest in json.loads((root/'work/source-sha256.json').read_text()).items():
    if hashlib.sha256((root/'source'/name).read_bytes()).hexdigest() != digest:
        sys.exit('Source hash mismatch: ' + name)
shapes = ['BR','B','BL','R','C','L','TR','T','TL','V','>','<','^']
key = {f'{s}{d}': chr(65 + 2*i + d) for i, s in enumerate(shapes) for d in (0, 1)}
assert len(set(key.values())) == 26
lit, emd = [], []
n = 0
for line in (root/'work/transcription.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    a = b = ''
    for t in line.split():
        if t == '|':
            a += ' '; b += ' '; continue
        n += 1
        base, _, fix = t.partition('!')
        restored = base.endswith('*')
        p = key[base.rstrip('*')]
        a += p.lower() if restored else p
        b += fix if fix else p
    lit.append(a); emd.append(b)
print('LITERAL (lower case = restored under blot):')
print('\n'.join(lit))
print('\nEMENDED (3 slips BR0->E):')
print('\n'.join(emd))
expected = ('DEAREST BETTY WHAT ABOUT THIS FOR A PHOTO OF BRUCE SHALL GO TO BED EARLY '
            'TONIGHT FEELS TIRED OR SOME THING COLD A LITTLE BETTER WITH FONDEST LOVE '
            'AND KISSES FROM YOURS EVER BOB XXXXXXXXX')
got = ' '.join(' '.join(emd).split())
assert got.replace(' ', '') == expected.replace(' ', ''), got
print(f'\n{n} signs decoded; source hashes OK; emended text matches SOLUTION.md.')
