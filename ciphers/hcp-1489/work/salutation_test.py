#!/usr/bin/env python3
"""HCP 1489, response to review 1: compare the two readings of line 1 after DEAR.
Keeps the card's first 7 signs (S D E O L A R, containing DEAR) fixed, shuffles the
other 137 signs, and counts how often the next 9 signs contain (a) E,S,T in order
(-> DEAREST within 15 signs, as on the card) or (b) N,A,N adjacent (-> NAN as a group)."""
import json, random
from pathlib import Path
root = Path(__file__).resolve().parents[1]
ct = ''.join(json.loads((root/'work/transcription-v2.json').read_text())['lines'])
head, rest = ct[:7], list(ct[7:])
def subseq(s, p):
    it = iter(s); return all(c in it for c in p)
rng = random.Random(14891); N = 20000; est = nan = 0
for _ in range(N):
    rng.shuffle(rest); w = ''.join(rest[:9])
    est += subseq(w, 'EST'); nan += 'NAN' in w
print('card, signs 8-16:', ct[7:16], '| EST in order:', subseq(ct[7:16], 'EST'), '| NAN adjacent:', 'NAN' in ct[7:16])
print(f'random: EST in order {est}/{N} = {est/N:.1%}; NAN adjacent {nan}/{N} = {nan/N:.2%}')
