#!/usr/bin/env python3
"""Reviewer's independent Pigpen decoder for HCP 1467.
Glyphs are described by the frame strokes they HAVE (t,b,l,r) or a wedge
opening direction, plus '*' when an internal dot is present.  The key is the
'interleaved' Pigpen: each # cell holds two consecutive letters, the second
dotted; X cells hold S..Z.  Reading from body-rot.png, l1..l7.png, love-rot.png,
sig-rot.png, look*.png in this dir (image rotated 38 deg clockwise)."""
import sys, pathlib
# cells of the # grid in reading order: top-left .. bottom-right
GRID = ['rb','lrb','lb','trb','tlrb','tlb','tr','tlr','tl']
WEDGE = ['V','>','<','^']   # opening up(V), left(>), right(<), down(^)
key = {}
letters = iter('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
for g in GRID + WEDGE:
    key[g] = next(letters); key[g+'*'] = next(letters)
# reviewer's own reading, one card line per string; '|' = written word dot
MINE = [
 'trb* tlr tlr* lb | V* tlr |',
 'V lb lb | ^ tlr > | < tlrb V* trb* |',
 'tlb* > lrb tlb | V tlr tlr tr* | tlb* tlr tlr tlb |',
 'tlr > V* | lb* tlr tl* | V* trb* tl* lb lb |',
 'lrb tlr > tr* V* tl* ^ | ^ tlr tlb lb tlb* V |',
 'tlb* tlr >* lb |',
 'rb* tlr tlr [dots] rb* tlr tlr |',
]
for line in MINE:
    print(''.join(' ' if t=='|' else '[dots]' if t=='[dots]' else key[t] for t in line.split()))
n = sum(t not in ('|','[dots]') for l in MINE for t in l.split())
print('letter glyphs:', n)
# translate the solver's labels (BR,B,BL,R,C,L,TR,T,TL + 0/1) to mine and compare
if len(sys.argv) > 1:
    m = dict(zip(['BR','B','BL','R','C','L','TR','T','TL','V','>','<','^'], GRID+WEDGE))
    sol = [t for t in pathlib.Path(sys.argv[1]).read_text().split() if t not in ('.','/','DOT_CLUSTER')]
    sol = [m[t[:-1]] + ('*' if t[-1]=='1' else '') for t in sol]
    mine = [t for l in MINE for t in l.split() if t not in ('|','[dots]')]
    print('solver glyphs:', len(sol))
    for i,(a,b) in enumerate(zip(mine, sol)):
        if a != b: print(f'  differs at glyph {i+1}: reviewer {a} ({key[a]}) vs solver {b} ({key[b]})')
