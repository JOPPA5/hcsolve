#!/usr/bin/env python3
"""Reviewer's independent Kryha decoder for HCP 409.

Reads the rings and stop mask from the *reviewed hcp-374* key (not hcp-409's copy)
and computes each displacement in closed form: d_i = d0 + walk(h0 -> h_i) + 179*(i//23),
instead of stepping edge by edge as the solver's decoder does.
usage: kryha_review.py <transcription> [--phase P --d0 D] [--search] [--need]
"""
import json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[4]
K = json.loads((ROOT / 'ciphers/hcp-374/work/key.json').read_text())
P, O, E = K['input_positions'], K['output_positions'], K['adjacent_distances']
H = sorted(K['holes_zero_based'])             # 23 selected holes on a 52-position wheel
CYCLE = sum(E)                                # 179
pos = [0]
for e in E: pos.append(pos[-1] + e)           # absolute coordinate of each of 52 holes

def walk(a, b):                               # distance from hole a forward to hole b
    return (pos[b] - pos[a]) % CYCLE if b != a else 0

invP = {p: chr(97 + i) for i, p in enumerate(P)}
invO = {o: chr(97 + i) for i, o in enumerate(O)}


def displacements(n, phase, d0):
    out = []
    for i in range(n):
        k = phase + i
        out.append(d0 + (pos[H[k % 23]] + CYCLE * (k // 23)) - pos[H[phase]])
    return out

def decode(ct, phase, d0):
    return ''.join(invP[(O[ord(c) - 97] - d) % 26] for c, d in zip(ct, displacements(len(ct), phase, d0)))

def encode_letter(pl, d):
    return invO[(P[ord(pl) - 97] + d) % 26]

WORDS = ['slovensk', 'nie', 'alebo', 'ktor', 'vlad', 'prezident', 'obyvatel', 'samostatn', 'agent', 'povstan', 'cesk']

if __name__ == '__main__':
    ct = ''.join(Path(sys.argv[1]).read_text().lower().split())
    args = sys.argv[2:]
    if '--search' in args:
        res = []
        for ph in range(23):
            for d0 in range(26):
                t = decode(ct, ph, d0)
                res.append((sum(t.count(w) for w in WORDS), ph, d0, t[:40]))
        res.sort(reverse=True)
        for r in res[:4]: print(r)
        print('settings tried:', len(res), '; settings with score>0:', sum(1 for r in res if r[0] > 0))
    else:
        ph = int(args[args.index('--phase') + 1]); d0 = int(args[args.index('--d0') + 1])
        print(decode(ct, ph, d0).upper())
