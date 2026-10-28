#!/usr/bin/env python3
"""Reviewer's independent decoder for HCP 962 (does not import solver code).

Transcription made by the reviewer from source/picture.jpg crops (review/work/*.png).
Notation: grid cells numbered by position in a 3x3 tic-tac-toe grid
  1 2 3      1 = walls bottom+right (┘)   2 = ⊔   3 = └
  4 5 6      4 = ⊐ (open left)            5 = □   6 = ⊏ (open right)
  7 8 9      7 = ┐                        8 = ⊓   9 = ┌
X-figure wedges: v (down-pointing V), > , < , ^.
A trailing '*' = interior dot. 'v*"' = dotted V with two extra umlaut dots.
"""
import collections

# Pair-filled grid, J omitted: undotted = first letter, dotted = second.
pairs = ['AB', 'CD', 'EF', 'GH', 'IK', 'LM', 'NO', 'PQ', 'RS']
KEY = {}
for i, p in enumerate(pairs, 1):
    KEY[str(i)] = p[0]
    KEY[str(i) + '*'] = p[1]
for sym, p in zip(['v', '>', '<', '^'], ['TU', 'VW', 'XY', 'Z']):
    KEY[sym] = p[0]
    if len(p) > 1:
        KEY[sym + '*'] = p[1]
KEY['v*"'] = 'Ü'

ROWS = [
    "6 5 3 1* 3 9 / 3 7 4 3 6 !",
    "2* 5 9 / ^ v* / 4 3 3* 1 6 6 3 7",
    "5* 7* 6* 6* 3 / 4* 7* 9 4 3 7",
    "^ v* 9 v*\" 2 5* . / 1* 5 9* / 9* 7* 7 7 =",
    "v 1 4 / 7 1 2 4* / 2* 3 9 / 6* 3 9* 9* 3 / > 3 9 1* 6 3 5 1* 3 / "
    "v* 7 v 3 9 / 4* 3 9 ^ 6 5 2 4* 3 6*",
    "4 9 v* 9* 9* / v* 7 2* / 5* v* 9* 9* / 2* 3 5 7 / 2* 5 2 4* / "
    "6 5 3 1* 3 7 2* 3 9 / 6*",
]
PUNCT = {'!', '.', '='}

total = 0
used = collections.Counter()
for row in ROWS:
    out = []
    for tok in row.split():
        if tok == '/':
            out.append(' ')
        elif tok in PUNCT:
            out.append(tok)
        else:
            out.append(KEY[tok])
            used[tok] += 1
            total += 1
    print(''.join(out))
print('cipher glyphs:', total)
print('symbols used:', len(used), 'unused key cells:',
      sorted(k for k in KEY if k not in used))
