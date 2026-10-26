#!/usr/bin/env python3
"""Reviewer's independent decoder for hcp-1506 (does not import solver code).
Usage: python3 -I review_decode.py <transcription-file>
Key typed from SOLUTION.md (shared with hcp-1507). Unknown numbers print as '[n]'."""
import sys, collections
KEY = {1:'M',3:'E',4:'R',5:'V',6:'L',7:'O',8:'T',9:'P',10:'S',11:'F',12:'A',13:'G',
       14:'K',15:'B',16:'U',17:'I',18:'D',20:'C',21:'W',22:'H',24:'X',25:'N',26:'Y'}
assert len(set(KEY.values())) == len(KEY), 'key not injective'
uses = collections.Counter(); unknown = []; n = 0
for raw in open(sys.argv[1], encoding='utf-8'):
    line = raw.strip()
    if not line or line.startswith('#'): continue
    out = []
    for w in line.split(' / '):
        if w.startswith('{'): out.append(w[1:-1]); continue
        s = ''
        for t in w.split('.'):
            k = int(t); n += 1; uses[k] += 1
            if k in KEY: s += KEY[k]
            else: s += f'[{k}]'; unknown.append(k)
        out.append(s)
    print(' '.join(out))
print(f'-- cipher tokens: {n}; distinct numbers: {len(uses)}; unmapped tokens: {unknown}')
print('-- numbers used:', dict(sorted(uses.items())))
