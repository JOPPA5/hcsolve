#!/usr/bin/env python3
"""Reviewer's independent decoder for HCP 1189: Pigpen grid repeated three
times, the block given by the number of dots (1: A-I, 2: J-R, 3: S-Z).
Written from scratch; does not import the solver's decode.py.
usage: review_decode.py TRANSCRIPTION [CLAIMED]   tokens <shape><dots>, '|' gap, '.' full stop
"""
import sys, string
CELLS = ['BR', 'B', 'BL', 'R', 'C', 'L', 'TR', 'T', 'TL']   # strokes of the 9 grid cells
KEY = {}
letters = iter(string.ascii_uppercase)
for dots in (1, 2, 3):
    for cell in CELLS:
        ch = next(letters, None)
        if ch:
            KEY[f'{cell}{dots}'] = ch
assert len(KEY) == 26
out = []
n = 0
for raw in open(sys.argv[1], encoding='utf-8'):
    raw = raw.split('#', 1)[0].strip()
    if not raw:
        continue
    s = ''
    for t in raw.split():
        if t == '|': s += ' '
        elif t == '.': s += '.'
        else: s += KEY[t]; n += 1
    out.append(s)
print('\n'.join(out)); print(f'\n{n} glyphs')
if len(sys.argv) > 2:
    claimed = [l.strip() for l in open(sys.argv[2], encoding='utf-8') if l.strip()]
    print('MATCHES CLAIMED' if out == claimed else f'DIFFERS: {out} vs {claimed}')
