#!/usr/bin/env python3
"""Reviewer's independent decoder for HCP 1187/1188 (interleaved dotted Pigpen).

Key written out explicitly from the standard 3x3 grid, letters filled in
pairs (undotted, dotted) cell by cell, then the four X-wedges.  Does not
import or read the solver's decode.py.

usage: review_decode.py TRANSCRIPTION [CLAIMED_PLAINTEXT]
Tokens: <shape><0|1>; '|' word gap; '?' unreadable; a trailing '?' on a
token (e.g. C1?) marks an uncertain reading and is decoded but flagged.
"""
import sys

GRID = [  # cell -> visible strokes (standard pigpen #-grid)
    ('BR', 'AB'), ('B', 'CD'), ('BL', 'EF'),
    ('R', 'GH'), ('C', 'IJ'), ('L', 'KL'),
    ('TR', 'MN'), ('T', 'OP'), ('TL', 'QR'),
    ('V', 'ST'), ('>', 'UV'), ('<', 'WX'), ('^', 'YZ'),
]
KEY = {}
for shape, pair in GRID:
    KEY[shape + '0'] = pair[0]
    KEY[shape + '1'] = pair[1]
assert len(set(KEY.values())) == 26 and len(KEY) == 26

def decode(path):
    lines, n, unc = [], 0, []
    for raw in open(path, encoding='utf-8'):
        raw = raw.split('#', 1)[0].strip()
        if not raw:
            continue
        out = []
        for t in raw.split():
            if t == '|':
                out.append(' ')
            elif t == '?':
                out.append('[?]'); n += 1
            else:
                flag = t.endswith('?')
                t = t.rstrip('?')
                ch = KEY[t]          # KeyError = token outside the key
                n += 1
                if flag:
                    unc.append((len(lines) + 1, t, ch)); ch = ch.lower()
                out.append(ch)
        lines.append(''.join(out))
    return lines, n, unc

if __name__ == '__main__':
    lines, n, unc = decode(sys.argv[1])
    print('\n'.join(lines))
    print(f'\n{n} glyph positions; uncertain readings (lower-case): {unc}')
    if len(sys.argv) > 2:
        claimed = [l.strip() for l in open(sys.argv[2], encoding='utf-8') if l.strip()]
        got = [l.upper() for l in lines]
        print('MATCHES CLAIMED' if got == claimed else 'DIFFERS FROM CLAIMED')
        for i, (a, b) in enumerate(zip(got, claimed), 1):
            if a != b:
                print(f'  line {i}: got {a!r}\n          claimed {b!r}')
