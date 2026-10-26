#!/usr/bin/env python3
"""Reviewer's independent decoder for HCP 1190 (does not import solver code).
Usage: python3 -I review_decode.py <reading-file> [solver-transcription]"""
import sys
ROWS = {1: 'ABCDEFGHI', 2: 'JKLMNOPQR', 3: 'STUVWXYZ'}   # dots -> letters by grid cell 1..9
def dec(tok):
    cell, dots = tok.split('.')
    return ROWS[int(dots)][int(cell) - 1]
def load(path):
    rows = [l.split() for l in open(path, encoding='utf-8') if l.strip() and not l.startswith('#')]
    return rows
mine = load(sys.argv[1])
letters = []
for r in mine:
    out = ''.join(' ' if t == '/' else (t if t == ',' else dec(t)) for t in r)
    letters += [t for t in r if t not in '/,']
    print(out)
print(f'{len(letters)} signs; distinct {len(set(letters))}')
# consistency: each sign -> exactly one letter, each letter <- exactly one sign
m = {}
for t in letters:
    m.setdefault(dec(t), set()).add(t)
print('letters written with >1 sign:', {k: v for k, v in m.items() if len(v) > 1} or 'none')
if len(sys.argv) > 2:
    # map solver's outline names to grid cells (from its README table, not its code)
    S2C = {'BR': 1, 'B': 2, 'BL': 3, 'R': 4, 'C': 5, 'L': 6, 'TR': 7, 'T': 8, 'TL': 9}
    sol = [t for r in load(sys.argv[2]) for t in r if t not in ('-', ',')]
    sol = [f'{S2C[t[:-1]]}.{t[-1]}' for t in sol]
    diffs = [(i, a, b) for i, (a, b) in enumerate(zip(letters, sol)) if a != b]
    print('solver signs:', len(sol), '| sign-level differences vs reviewer:', diffs or 'none')
