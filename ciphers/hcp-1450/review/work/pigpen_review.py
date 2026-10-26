#!/usr/bin/env python3
"""Reviewer's independent three-count Pigpen decoder (does not import solver code).
Glyph notation: set of PRESENT border strokes (T,B,L,R in any order) + dot count.
Key derived from the 3x3 grid geometry: cell (r,c) has top if r>0, bottom if r<2,
left if c>0, right if c<2; letter = A + 9*(dots-1) + 3*r + c."""
import sys, string
key = {}
for r in range(3):
    for c in range(3):
        s = frozenset(x for x, ok in (('T', r > 0), ('B', r < 2), ('L', c > 0), ('R', c < 2)) if ok)
        for d in (1, 2, 3):
            n = 9 * (d - 1) + 3 * r + c
            if n < 26:
                key[(s, d)] = string.ascii_uppercase[n]
def dec(tok):
    return key[(frozenset(tok[:-1]), int(tok[-1]))]
def run(path):
    out, n = [], 0
    for line in open(path, encoding='utf-8'):
        line = line.split('#')[0].strip()
        if not line:
            continue
        words = []
        for w in line.split('|'):
            toks = w.split()
            words.append(''.join(t.strip('{}') if t.startswith('{') else (dec(t)) for t in toks))
            n += sum(1 for t in toks if not t.startswith('{'))
        out.append(' '.join(words))
    return out, n
if __name__ == '__main__':
    lines, n = run(sys.argv[1])
    print('\n'.join(lines)); print(n, 'cipher glyphs')
