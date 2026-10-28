#!/usr/bin/env python3
"""Independent reviewer decoder for HCP 1556 (pc_hcp_237).

Transcription below is the reviewer's own sign-by-sign reading of
source/picture.jpg (main block rotated 90 deg clockwise, bottom two lines
in original orientation). Labels are the reviewer's own, chosen by visual
shape:
  d = looped d (bowl + ascender curling back)    -> T
  t = crossed t                                  -> D
  c = round c                                    -> S
  s = small angular/pointed s                    -> C
  m = two-hump m                                 -> N
  n = one-hump n                                 -> M
  b = tall looped b                              -> P
  p = p with descender                           -> B
  g = bowl with top-right flick, looped tail     -> K
  9 = closed bowl, tail hooking left (no flick)  -> Z
  7 = 7-like sign with descender                 -> J
  r = plain r                                    -> H
  R = r with cap / caron mark                    -> CH
Nothing is imported from the solver's code. The solver's literal file is
read only as data for a diff.
Run: python3 -I ciphers/hcp-1556/review/work/my_decode.py
"""
import os, re

KEY = {'1': 'y', '2': 'u', '3': 'o', '4': 'i', '5': 'e', '6': 'a', '8': 'l',
       '9': 'z', 'g': 'k', 'f': 'v', 'h': 'r', 't': 'd', 'r': 'h', 'c': 's',
       's': 'c', 'n': 'm', 'm': 'n', 'p': 'b', 'b': 'p', 'd': 't', '7': 'j',
       'R': 'ch'}

ROWS = [
    ('M01', 'fh581 d4g, t2c4m-'),
    ('M02', 'g3 n375 75t4m6,'),
    ('M03', '96 th6r1 84cd5g.'),
    ('M04', 'm596m5tp6f6 nm5 n375'),
    ('M05', '6m2mg6 d6g5 f5 cf5n'),
    ('M06', 'cht5sg2? n6n d5, 6m2cg3'),
    ('M07', 'd384g h6t 6 d3294n b3 d3p5'),
    ('M08', 'm5cn4hm5! - 75 b. h4t4s4'),
    ('M09', 'c5t4f1 d19, 75n29 m5t6fm3'),
    ('M10', '95nh586 b6m4? - c57t5n5 c5'),
    ('M11', '6m2mg3 bh5th6r6, p5r5n'),
    ('M12', 'gf5dm6? - d5c4 c5 m6'),
    ('M13', 'th6r5 h6tg1 df5 6 d4c4s'),
    ('M14', 'fh581R, f6cm4f1R b2c d4'),
    ('M15', 'b3c486 df27 cd685 f9b3n4-'),
    ('M16', 'm674s4 b5b32c.'),
    ('B01', '9dh6d48 c5 749 m5g384g6d1 n27 84cd5g'),
    ('B02', 'd3p5 96c86m1. gt5 f594 d3r3 6c4 bh4s4m6?'),
]


def decode(s):
    return ''.join(KEY.get(ch, ch) for ch in s)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    units = letters = ch = 0
    mine = {}
    for label, row in ROWS:
        for c in row:
            if c in KEY:
                units += 1
                letters += len(KEY[c])
                ch += c == 'R'
            elif c.isalnum():
                raise SystemExit('unmapped sign %r in %s' % (c, label))
        mine[label] = decode(row)
        print(label, mine[label].upper())
    print('rows=%d units=%d letters=%d CH=%d' % (len(ROWS), units, letters, ch))
    used = {c for _, r in ROWS for c in r if c in KEY}
    print('key one-to-one:', len(set(KEY.values())) == len(KEY),
          '| labels used: %d/%d' % (len(used), len(KEY)))
    path = os.path.join(here, '..', '..', 'work', 'literal-cz.txt')
    solver = {}
    for line in open(path, encoding='utf-8'):
        m = re.match(r'(\w\d\d) (.*)', line.rstrip('\n'))
        if m:
            solver[m.group(1)] = m.group(2)
    diffs = [(k, mine[k], solver.get(k)) for k, _ in ROWS if mine[k] != solver.get(k)]
    print('diff vs solver literal-cz.txt:', 'none' if not diffs else '')
    for k, a, b in diffs:
        print(' ', k, 'mine  :', a)
        print(' ', k, 'solver:', b)


if __name__ == '__main__':
    main()
