#!/usr/bin/env python3
"""Reviewer's independent Pigpen decoder: stroke set -> grid cell, dots -> which of 3 grids."""
import sys
cells = {frozenset('rb'):1, frozenset('lrb'):2, frozenset('lb'):3,
         frozenset('trb'):4, frozenset('tlrb'):5, frozenset('tlb'):6,
         frozenset('tr'):7, frozenset('tlr'):8, frozenset('tl'):9}
n = 0
for line in open(sys.argv[1]):
    if line.startswith('#') or not line.strip(): continue
    out = []
    for tok in line.split():
        if tok in ',.': out.append(' ' if tok == ',' else '.'); continue
        idx = (int(tok[-1]) - 1) * 9 + cells[frozenset(tok[:-1])]
        assert idx <= 26, tok
        out.append(chr(64 + idx)); n += 1
    print(''.join(out))
print(n, 'signs')
