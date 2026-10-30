#!/usr/bin/env python3
"""Bounded screen of a tentative MANUAL row transcript; does not read pixels."""
import hashlib, json
from pathlib import Path
root = Path(__file__).resolve().parents[1]
for name, expected in json.loads((root/'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((root/'source'/name).read_bytes()).hexdigest() == expected
abc='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
codes='.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..'.split()
key=dict(zip(codes, abc))
t=json.loads((root/'work/transcript.json').read_text())
g=t['row1_tentative_groups']
variants={'as grouped':g, 'groups reversed':g[::-1], 'each group reversed':[s[::-1] for s in g], 'entire row reversed':[s[::-1] for s in g[::-1]]}
for name,v in variants.items():
    print(name+': '+' '.join(v)+' -> '+''.join(key.get(s,'?') for s in v))
print(f'{sum(map(len,g))} tentative strokes in upper row only; 7 hypothetical groups.')
print('No plaintext established. Lower row, group spacing, direction, and dot/dash readings remain unresolved.')
print('Source hashes pass; the screen cannot validate the manual visual transcription.')
