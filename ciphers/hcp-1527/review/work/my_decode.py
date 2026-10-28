#!/usr/bin/env python3
"""Reviewer's independent decoder for HCP 1527 (pc_hcp_208).

The transcription below is the reviewer's own sign-by-sign reading of
source/picture.jpg (rotated 90 deg CCW), made from the crops in this folder.
Shape labels: digits as written; c = round c-shape; s = angular s-shape;
d = looped d-shape; t = crossed t-shape; f = tall looped f; v = shallow v;
n = two-hump n; m = three-hump m; b = b-shape; p = p-shape; h = h-shape;
r = r/+ shape; q = q/9-shape with straight descender; g = g-shape;
R = capped r (the CH unit).

The key is the reviewer's own statement of the family table; no solver code
is imported. The solver's transcription.txt is read only as data, to print a
per-row diff of labels.
"""
import difflib
import sys
from pathlib import Path

KEY = {'1': 'Y', '2': 'U', '3': 'O', '4': 'I', '5': 'E', '6': 'A', '7': 'J',
       '8': 'L', 'b': 'P', 'c': 'S', 'd': 'T', 'f': 'V', 'g': 'K', 'h': 'R',
       'm': 'N', 'n': 'M', 'p': 'B', 'q': 'Z', 'r': 'H', 's': 'C', 't': 'D',
       'R': 'CH'}

MINE = """\
fh581 t4g q6 th6r5 bc6mg3. 3pc6r5n 75r3 p18
7c5n s6cd5sm5 f58n4 bh5gf6b5m. s85sm6 c5t86s-
g3f6 c5 6c4 nm3r3 bh5c85R86; m5n6n 3 d5d3 mn5
2hs3f6m5 m5f5cd5 6m4 d2c5m4. m5m685q4n d5q
g d5n, gt3q t674 c4 cm6t 2hs3f6d4 cf374 m5f5cd2
74m1n4.
bh6m4 cf5r3 cht5sg6 cb8m4n 6 3tb3f4n n2 bh5t
sdfhd h3g5n. 7c5n m1m4 s585 tm1 f 2h6t5 6 d6g5
c5 t385 cdh6f274; 75m m6r3t32 q6c58 7c5n tm5c
fb385tm5 t3n2. d4c4s fh581R b2c 6 b3qth6f2 b3c486
d4 df27 b5b32c, gd5h1 cf5n2 sht5sg2 bh575, 6p1
cdh6f483 r3tm5 r5qg5 cf6dg1. p2t2 fqb3n4m6d4.
"""


def decode(line):
    return ''.join(KEY.get(ch, ch) for ch in line)


def main():
    rows = MINE.splitlines()
    units = sum(1 for r in rows for ch in r if ch in KEY)
    letters = sum(len(KEY[ch]) for r in rows for ch in r if ch in KEY)
    for i, r in enumerate(rows, 1):
        print(f'R{i:02d} {decode(r)}')
    print(f'\nrows={len(rows)} units={units} base_letters={letters} '
          f'CH={sum(r.count("R") for r in rows)}')
    solver = Path(__file__).resolve().parents[2] / 'work' / 'transcription.json'
    if solver.exists():
        import json
        theirs = [r['cipher'].replace('ř', 'R') for r in json.loads(solver.read_text(encoding='utf-8'))['rows']]
        print('\nDifferences from solver transcription (solver -> reviewer):')
        for i, (a, b) in enumerate(zip(theirs, rows), 1):
            sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
            for op, a0, a1, b0, b1 in sm.get_opcodes():
                if op != 'equal':
                    print(f'  R{i:02d} {op:8s} solver[{a[a0:a1]!r}] -> reviewer[{b[b0:b1]!r}]'
                          f'   ({decode(a[a0:a1])!r} -> {decode(b[b0:b1])!r})')
    return 0


if __name__ == '__main__':
    sys.exit(main())
