#!/usr/bin/env python3
"""Reviewer's independent Pigpen decoder for hcp-1511 (no solver code imported).
Usage: python3 -I review_decode.py <token-file> [--wedges=SOLVER|ALT]
SOLVER: wedge values as stated in SOLUTION.md (< = U/V, > = W/X, ^ = Y/Z).
ALT:    < = U/V, ^ = W/X, > = Y/Z (what the card needs if its Y-sign is '>')."""
import sys
cells = {'BR':'AB','B':'CD','BL':'EF','R':'GH','C':'IJ','L':'KL','TR':'MN','T':'OP','TL':'QR','V':'ST'}
mode = 'ALT' if '--wedges=ALT' in sys.argv else 'SOLVER'
cells.update({'<':'UV','>':'WX','^':'YZ'} if mode == 'SOLVER' else {'<':'UV','^':'WX','>':'YZ'})
inv = {}
for shape, pair in cells.items():
    for d, ch in enumerate(pair):
        assert ch not in inv; inv[ch] = (shape, d)
assert len(inv) == 26
def dec(tok):
    if tok == 'X': return '#'
    shape, dot = tok[:-1], tok[-1]
    if dot == '?':   # dot undecidable: show both readings
        a, b = cells[shape]; return f'({a}|{b})'
    return cells[shape][int(dot)]
n = 0
for line in open(sys.argv[1], encoding='utf-8'):
    line = line.strip()
    if not line or line.startswith('#'): continue
    toks = [t.replace('{cancelled}', 'X') for t in line.split()]
    n += sum(t != 'X' for t in toks)
    print(''.join(dec(t) for t in toks))
print(f'-- mode {mode}; intact signs: {n}')
