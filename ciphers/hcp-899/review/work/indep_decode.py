#!/usr/bin/env python3
"""Reviewer's independent decoder for HCP 899 (does not use the solver's key dict).
Key rebuilt from the stated rule: 9 cell shapes in order, 3 letters each,
alphabet A..Z with J kept and ß appended; tick count 1..3 picks the letter."""
import json, sys
from pathlib import Path
d = Path(__file__).resolve().parents[2]
shapes = ['br', 'lbr', 'bl', 'tbr', 'box', 'tbl', 'tr', 'tlr', 'tl']
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZß'
key = {f'{s}{n+1}': alpha[3*i+n] for i, s in enumerate(shapes) for n in range(3)}
uml = {'A': 'Ä', 'O': 'Ö', 'U': 'Ü'}
def dec(tok):
    base, _, mod = tok.partition(':')
    c = key[base]
    return uml[c] if mod == 'umlaut' else c
t = json.loads((d / 'work/transcript_v2.json').read_text())
n = 0
for r in t['upper']:
    ws = [w.split() for w in r['tokens'].split('/')]
    n += sum(map(len, ws)); print(r['label'], ' '.join(''.join(map(dec, w)) for w in ws))
for r in t['lower']:
    ws = [w['tokens'].split() for w in r['words']]
    n += sum(map(len, ws)); print(r['label'], ' '.join(''.join(map(dec, w)) for w in ws))
print('glyphs', n)
# reviewer's reading of L4 word 3 from the scan (review/work/L4w3.png): 6 signs
print('L4 word3 as seen by reviewer:', ''.join(map(dec, 'tbr3 bl3 lbr2 br2 lbr2 tr1'.split())))
