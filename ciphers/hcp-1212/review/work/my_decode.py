"""Reviewer's independent decoder for HCP1212 (does not use the solver's ledger or decoder)."""
import sys, unicodedata
from pathlib import Path
KEY = dict(b2='a', six='b', lbowl='c', sl='d', b3='e', cross='f', gl='g', tt='h', dc='i', invT='j',
           sect='k', wave='l', s3='m', s2='n', loop='o', tsp='p', Fr='r', rbowl='s', corner='t',
           x='u', chev='v', desc='y', xd='z')
ACC = {"'": '́', '"': '̈'}
for line in (Path(__file__).parent / 'my_ledger.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    row, *toks = line.split()
    out = []
    for t in toks:
        if t in ',.':
            out.append(t); continue
        q = t.endswith('?'); t = t.rstrip('?')
        acc = ''
        while t[-1] in ACC:
            acc = ACC[t[-1]] + acc; t = t[:-1]
        ch = unicodedata.normalize('NFC', KEY[t] + acc)
        out.append('{' + ch + '?}' if q else ch)
    print(f'{row}: ' + ''.join(out))
