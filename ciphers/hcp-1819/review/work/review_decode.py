#!/usr/bin/env python3
"""Reviewer's independent decoder for alternating dotted/undotted Pigpen (does not import solver code).
Sign notation: grid cell 1..9 (1=bottom+right, 2=bottom+left+right, 3=bottom+left, 4=top+bottom+right,
5=box, 6=top+bottom+left, 7=top+right, 8=top+left+right, 9=top+left) or wedge wD/wR/wL/wU (named by the
direction its POINT faces); suffix '*' = dotted.  '/' word gap, other tokens printed as punctuation.
Usage: python3 -I review_decode.py <reading-file> [solver-transcription]"""
import sys
PLAIN, DOTTED = 'ACEGIKMOQSUWY', 'BDFHJLNPRTVXZ'
ORDER = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'wD', 'wR', 'wL', 'wU']
def dec(t):
    d = t.endswith('*'); i = ORDER.index(t.rstrip('*'))
    return (DOTTED if d else PLAIN)[i]
def issign(t):
    return t.rstrip('*') in ORDER
def load(p):
    return [l.split() for l in open(p, encoding='utf-8') if l.strip() and not l.startswith('#')]
mine = load(sys.argv[1]); signs = []
for r in mine:
    print(''.join(dec(t) if issign(t) else (' ' if t == '/' else t) for t in r))
    signs += [t for t in r if issign(t)]
print(f'{len(signs)} signs; distinct {len(set(signs))}')
inv = {}
for t in signs: inv.setdefault(dec(t), set()).add(t)
print('letters written with >1 sign:', {k: v for k, v in inv.items() if len(v) > 1} or 'none')
if len(sys.argv) > 2:
    S2C = {'BR': '1', 'B': '2', 'BL': '3', 'R': '4', 'C': '5', 'L': '6', 'TR': '7', 'T': '8', 'TL': '9',
           'V': 'wD', '>': 'wR', '<': 'wL', '^': 'wU'}
    sol = [S2C[t[:-1]] + ('*' if t[-1] == '1' else '') for r in load(sys.argv[2]) for t in r
           if t[:-1] in S2C and t[-1] in '01']
    import difflib
    sm = difflib.SequenceMatcher(a=sol, b=signs, autojunk=False)
    print('solver signs:', len(sol))
    for op, a1, a2, b1, b2 in sm.get_opcodes():
        if op != 'equal':
            print(f'  {op}: solver[{a1}:{a2}]={sol[a1:a2]} -> reviewer[{b1}:{b2}]={signs[b1:b2]}'
                  f'  ({"".join(map(dec, sol[a1:a2]))} -> {"".join(map(dec, signs[b1:b2]))})')
