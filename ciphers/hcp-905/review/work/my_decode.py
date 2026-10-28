#!/usr/bin/env python3
"""Reviewer's independent decoder for HCP 905 (reads no solver file except, with
--diff, the solver's transcript.json word notations for comparison).

My own sign-by-sign reading of source/picture.jpg, in my own notation:
  grid cells 1..9 = the 3x3 grid read row-wise, named by the strokes drawn:
    1=┘ 2=⊔ 3=└ / 4=⊐ 5=□ 6=⊏ / 7=┐ 8=⊓ 9=┌
  '.' suffix = interior dot (second grid, J omitted: K L M N O P Q R S)
  '|' = upright stroke (T), 'v' = check (U), '<' = V, '^' = W, '^.' = Z
  '"' suffix = two strokes above (umlaut), 'X' = cancelled field (not decoded)
Words separated by spaces, rows by list entries.
"""
import json, sys
from pathlib import Path

G1 = dict(zip('123456789', 'ABCDEFGHI'))
G2 = dict(zip('123456789', 'KLMNOPQRS'))
SPECIAL = {'|': 'T', 'v': 'U', '<': 'V', '^': 'W'}

ROWS = [
 '91  <58.4  4.938|  594.3.12.',
 '498.  1.14.4.  938\'9.  3.588.  8.538|',
 '3.13854.  ^95  4594.5  2.5|^.|5',
 '93.  v"28.9754.  91  ^95  1v38  495',
 '14.458.4.  ^.^59  1.v"4.9.|2.58.1.18.|54.',
 '9.588.  8v"29.385  X  v4.4  41858.  <5.4.',
 '3.98.  3.9|  858.^.2.93853.  414.1.  54.|',
 '75754.7545.3.3.54.5  94.  5|^19.  3.58.1.',
 '^v"8.49753.  |5.4.5  1275619.9.|5',
 '9.5.4.4.54.1.18.|5  938  294.  68.5.8  419.9.  938',
 '9.95  9.52.29.|  <5.3.  6.5.9.|25.|54.  54.|75754.',
 '4.183.  1v89.58.453.  3.v89.  938  9545  <58.',
 '14.|^5.8.|v4.7  6v"8.  1.v"494.785.<54.58.  692.912.',
 '6.5.9.|<58.81"2|4.99.9.5  122.584.54.  9.382.v89.  v  1.v89.',
]

def dec(tok):
    out = ''; i = 0
    while i < len(tok):
        c = tok[i]
        if c == "'": out += "'"; i += 1; continue
        if c == 'X': out += '[X]'; i += 1; continue
        dot = i + 1 < len(tok) and tok[i+1] == '.'
        if c in G1:
            out += (G2 if dot else G1)[c]
        elif c == '^' and dot:
            out += 'Z'
        else:
            out += SPECIAL[c]
        i += 2 if dot else 1
        if i < len(tok) and tok[i] == '"':
            out = out[:-1] + {'A': 'Ä', 'U': 'Ü', 'O': 'Ö'}[out[-1]]; i += 1
    return out

mine = []
n = 0
for r in ROWS:
    words = [dec(w) for w in r.split()]
    mine.append(words)
    n += sum(len(w.replace("'", '').replace('[X]', '#')) for w in words)
for i, w in enumerate(mine, 1):
    print(f'{i:02}: ' + ' '.join(w))
print(f'positions (incl. cancelled field) = {n}')

if '--diff' in sys.argv:
    d = json.loads((Path(__file__).resolve().parents[2] / 'work' / 'transcript.json').read_text())
    print('\nDifferences vs solver transcript.json notations (J folded to I):')
    for i, (row, words) in enumerate(zip(d['rows'], mine), 1):
        theirs = [w['notation'].replace('J', 'I').replace('[CANCELLED]', '[X]') for w in row['words']]
        if len(theirs) != len(words):
            print(f'  row {i}: word count {len(theirs)} vs {len(words)}')
        for a, b in zip(theirs, words):
            if a != b:
                print(f'  row {i}: solver {a!r} -> reviewer {b!r}')
