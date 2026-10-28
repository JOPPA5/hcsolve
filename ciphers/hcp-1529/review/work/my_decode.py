#!/usr/bin/env python3
"""Reviewer's independent decoder for HCP 1529 (pc_hcp_210).

The transcription below is the reviewer's own sign-by-sign reading of
source/picture.jpg (used upright, no rotation), made from the crops in this folder.
Shape labels: digits as written; c = round c-shape; s = angular s-shape;
d = looped d-shape; y = descending j/7-like J sign; t = crossed t-shape; f = tall looped f; v = shallow v;
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

KEY = {'1': 'Y', '2': 'U', '3': 'O', '4': 'I', '5': 'E', '6': 'A', 'y': 'J',
       '8': 'L', 'b': 'P', 'c': 'S', 'd': 'T', 'f': 'V', 'g': 'K', 'h': 'R',
       'm': 'N', 'n': 'M', 'p': 'B', 'q': 'Z', 'r': 'H', 's': 'C', 't': 'D',
       'R': 'CH'}

MINE = """\
yc5n, 6m4sg3, 3t sdfhdg6 3b5d t3n6 c Rh4bg32, gd5h6 c5 nm5 3b5d c48m5y4 fh6d486.
m5p18 yc5n bh5cd3 2b8m5 qth6f5n 6 m6R86t48 yc5n c5 3b5d m6 s5cd5 q 2cd4
y5cd5 f4s5 fc6g bh4 84s5m4 3r85tm5 2b6tg2 cf6d3f6s86fcg5 q683qm1,
gt5 yc5n c5 p18 b3t4f6d4 6 gt5 p18 f58g1 m6f68 6 rh3qm5 f5th3.
p38586 nm5 f584s5 r86f6 6 m5p18 yc5n cg3h3 6m4 n4c85m4 cR3b5m.
t3c2t 85q4n, bh3d3q5 fc6g tm5c y4q 85b5 6 fqg6q68 yc5n t3 2h6t2,
q5 bh4yt2 f5 sdfhd5g m5p3 f b6d5g.
m6 d5p5 fqb3n4m6n cd685 y6g3 m6 cf5 y5t4m5 cht5sg3 6 b3c486n d4 fh5832 b2c2.
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
    solver = Path(__file__).resolve().parents[2] / 'work' / 'transcription.txt'
    if solver.exists():
        theirs = solver.read_text(encoding='utf-8').replace('H', 'R').splitlines()
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
