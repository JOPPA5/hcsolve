#!/usr/bin/env python3
"""hcp-1787: check source hashes, decode transcription.txt, print the literal, then the reading; strict check that each reading adds only unwritten a to the literal."""
import hashlib, os, re, sys, unicodedata
D = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(D)
H = {'source/picture-large.jpg':'c604d5e08dd416963a24cfd9a68ccbdd3b754d7e710589a491f17eed5eafde36',
     'source/address-large.jpg':'3e270fb28191ce3633a975c73d28e679376cb8f77282f02db0da875ea8e97ae9',
     'work/hires/pc_hcp_468_pic.JPG':'ca8d558f20e99ebc640af978d31b055ded1d660ddec1c1125639cebfc1328e5b',
     'work/hires/pc_hcp_468_adr.JPG':'1f107f7f7be4018549bec4deb0af33713e4b0fed10269eb6a70f8435075f13a8'}
for p, h in H.items():
    assert hashlib.sha256(open(os.path.join(R, p), 'rb').read()).hexdigest() == h, p
K = dict(zip('01234568 9vxzcSUoa?'.replace(' ', ''), 'ltnmrspHkvzjcsuoa?'))
CAR = {'t':'ť','s':'š','r':'ř','z':'ž','c':'č'}
def lit(w):
    if w[0] == '{': return w.strip('{}')
    o = ''
    for s, m in re.findall(r'([0-9a-zA-Z?])([_/^R]*(?:-\^|-|\.|:)?)', w):
        c = K[s]
        if '^' in m[:2] and not m.startswith('-'): c = CAR[c]
        if 'R' in m: c = 'ď'
        if '_' in m: c += 'a'
        if '/' in m: c += 'o'
        if '-^' in m: c += 'ě'
        elif m.endswith('-'): c += 'e'
        elif m.endswith('.'): c += 'y'
        elif m.endswith(':'): c += 'u'
        o += c
    return o
def norm(s):
    s = unicodedata.normalize('NFD', s.lower()); s = ''.join(c for c in s if not unicodedata.combining(c))
    return s.replace('[?]', '?').replace('ch', 'h').replace('d', 't').replace('b', 'p').replace('y', 'i')
def fits(a, b):
    """Strict: letters of the literal in order; the ONLY thing a reading may add is an unwritten a."""
    return re.fullmatch('a?' + 'a?'.join(re.escape(c) for c in norm(a)) + 'a?', norm(b)) is not None
# Words whose literal does not fit even so; each pair is pinned here and explained in SOLUTION.md (Uncertainties).
EXC = {('netoHolyl', 'nedovolil'), ('Hjtman', 'hejtman'), ('jasme', 'jsme'), ('moHlu', 'mohli'), ('vytaět', 'vidět'),
       ('taělame', 'děláme'), ('toe', 'to'), ('stětu', 'středu'), ('ž', 'že')}
bad = 0; exc = []; lits = []; reads = []
for l in open(os.path.join(D, 'transcription.txt'), encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    i, c, r = l.rstrip('\n').split('\t'); cw = c.split(); rw = r.split()
    assert len(cw) == len(rw), (i, cw, rw)
    L = [lit(w) for w in cw]
    for a, b in zip(L, rw):
        if not fits(a, b):
            exc.append((i, a, b))
    lits.append(f'{i:5} {" ".join(L)}'); reads += rw
print('LITERAL (decoded mechanically from work/transcription.txt)'); print('\n'.join(lits)); print()
print('READING (typed column of transcription.txt, checked word by word against the literal; not itself decoder output)')
print(' '.join(reads)); print()
for i, a, b in exc:
    if (a, b) in EXC: print(f'disclosed exception {i}: {a} -> {b}')
    else: bad += 1; print('MISFIT', i, a, b, file=sys.stderr)
print(f'\nhashes ok; words: {len(reads)}; disclosed exceptions: {len(exc) - bad}; misfits: {bad}')
sys.exit(1 if bad else 0)
