#!/usr/bin/env python3
"""Reviewer's independent decoder for HCP 1526 (pc_hcp_207).

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
       'R': 'CH', 'v': 'F'}

MINE = """\
fh581 t4g, q86d3 n375, q6 th6r1 84cd5g.
7c5n 3t5 cdh5t1 3b5d f 2h6t5, gt5 75cd
f6m3sm4 c5s3m6 74q f bhm5n bh32t2. n6n
c4s5 75cd5 dh3R2 h1n2, 6fc6g t32v6n, q5 7c5n
Rh4bg2 74q bh5n3r8. fqb3n4m6n fc6g m6
cf5 sht5sg3, gt5h5 m1m4 q6s5 n4cd3
nm5 Rh4bg6 dh6b4. m6R86t486 c5 p5qb3R1p1
p5r5n 74qt1 b3 th6q5. n2c4 c5 n5 cht5sg3
r3tm5 c5dh4t4, 76g3 nm5 t3 n6 6mt284sg6
c6n6 d6g t2dg84f6 h6t486. bh3c4n 74 3 d3.
d6q5 c5, qt6 7c5n m6 m4 fqb3n4m68, gt1q
nm5 r86f6 p38586. q674cd5, th6r32cg2,
fqt4d 7c5n p18 d5n5h cd685 c6n. fqb3n4m68
7c5n nm3r3 6 fh585. d4c4s t832r1R, f6cm4f1R
b2c b3c486 d4 df27 b5b32c, gt5h1 c5 f584s5
d5c4 m6 c84p5m5 bc6mg3.
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
          f'CH={sum(r.count("R") for r in rows)} F={sum(r.count("v") for r in rows)}')
    solver = Path(__file__).resolve().parents[2] / 'work' / 'transcription.txt'
    if solver.exists():
        theirs = solver.read_text(encoding='utf-8').replace('ř', 'R').splitlines()
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
