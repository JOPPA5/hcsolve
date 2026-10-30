#!/usr/bin/env python3
"""Reviewer's independent decoder for HCP1093: explicit table (from HCP1188 SOLUTION.md),
reads solver tokens, strips markup, reports literal text, unknown tokens and counts."""
import sys, re
from collections import Counter
T = {'BR':'AB','B':'CD','BL':'EF','R':'GH','C':'IJ','L':'KL','TR':'MN','T':'OP','TL':'QR',
     'V':'ST','>':'UV','<':'WX','^':'YZ'}
path = sys.argv[1]
out, n, bad, marks = [], 0, [], []
for line in open(path, encoding='utf-8'):
    if line.startswith('#') or not line.strip(): continue
    w = ''
    for t in line.split():
        if t == '|': w += ' '; continue
        m = re.fullmatch(r'(BR|BL|TR|TL|B|R|C|L|T|V|>|<|\^)([01])(\*?)(!([A-Z]))?', t)
        if not m: bad.append(t); w += '?'; continue
        n += 1
        ch = T[m.group(1)][int(m.group(2))]
        if m.group(3) or m.group(4): marks.append((t, ch))
        w += ch
    out.append(w)
print('\n'.join(out)); print('signs', n, 'unparsed', bad); print('marked', marks)
print(Counter(''.join(out).replace(' ','')).most_common())
