#!/usr/bin/env python3
"""HCP 921: verify source hashes, decode the manual Pigpen transcription.

Run from the repository root:  python3 -I ciphers/hcp-921/work/decode.py
Tokens (upright orientation, card turned so the cipher lines are horizontal):
outline tokens name the strokes present (TR top/right, C closed square,
BR bottom/right, B bottom/left/right, BL bottom/left); wedges are named by
where their vertex points (> right, ^ up); 0 undotted, 1 dotted.
"""
from pathlib import Path
import hashlib, json

r = Path(__file__).resolve().parents[1]
for name, digest in json.loads((r/'work/source-sha256.json').read_text()).items():
    if hashlib.sha256((r/'source'/name).read_bytes()).hexdigest() != digest:
        raise SystemExit('Source hash mismatch: ' + name)

# Interleaved Pigpen key of the sister cards HCP 1188/1187/1497/1498
# (grid pairs A/B .. Q/R, wedges V=S/T, >=U/V, <=W/X, ^=Y/Z).
KEY = {'BR0': 'A', 'BR1': 'B', 'B0': 'C', 'B1': 'D', 'BL0': 'E', 'BL1': 'F',
       'R0': 'G', 'R1': 'H', 'C0': 'I', 'C1': 'J', 'L0': 'K', 'L1': 'L',
       'TR0': 'M', 'TR1': 'N', 'T0': 'O', 'T1': 'P', 'TL0': 'Q', 'TL1': 'R',
       'V0': 'S', 'V1': 'T', '>0': 'U', '>1': 'V', '<0': 'W', '<1': 'X',
       '^0': 'Y', '^1': 'Z'}
# Card-specific exception: the writer's dotted right-pointing wedge stands
# for S here (contextual value from MISS; the sister key would give V).
CARD = dict(KEY, **{'>1': 'S'})
EXTRA = {'{cancelled}': '', '|': ' ', '.': '.'}

def decode(key):
    out = []
    for line in (r/'work/transcription.txt').read_text().splitlines():
        if not line or line.startswith('#'):
            continue
        out.append(''.join(key.get(t, EXTRA.get(t)) for t in line.split()))
    return out

lit = decode(CARD)
print('\n'.join(lit))
n = sum(t in KEY for l in (r/'work/transcription.txt').read_text().splitlines()
        if l and not l.startswith('#') for t in l.split())
print(f'\n[{n} intact signs decoded; 1 blotted (cancelled) sign omitted]')
print('[sister key unchanged would give: ' + ' / '.join(decode(KEY)) + ']')
