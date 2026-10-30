"""Reviewer's independent decoder for HCP1216 (round 1).
Maps each ledger token to a named graphic class, then the class to a letter through the
sister-card key ciphers/hcp-1301/work/graphic-key.json (not the solver's decoder or key table).
Then aligns the literal letter stream with the solver's normalized text to list every editorial change.
Run from repo root: python3 -I ciphers/hcp-1216/review/work/decode_review.py"""
import json, os, sys, unicodedata, difflib
R = os.path.dirname(os.path.abspath(__file__)); C = os.path.join(R, '..', '..'); ROOT = os.path.join(C, '..', '..')
key = json.load(open(os.path.join(ROOT, 'ciphers/hcp-1301/work/graphic-key.json'), encoding='utf-8'))
CLS = {'A':'two-bars','6':'six','C':'left-bowl','D':'joined-two-strokes','/':'joined-two-strokes','E':'three-bars',
 '+':'cross','G':'open-loop-descender','H':'two-tall-strokes','I':'dotted-crossed-curve','J':'inverted-T','K':'section-mark',
 'L':'wave','M':'three-short-strokes','N':'two-short-strokes','O':'cursive-loop','F':'F',')':'right-bowl','T':'gamma',
 'X':'x','V':'chevron','Y':'low-descender','Z':'crossed-diagonal'}
DIG = {'GY':'gy','CS':'cs'}
def dec(t):
    b, _, acc = t.partition(':')
    if b in DIG: return DIG[b]
    if b == 'M?': return 'm'          # solver's own m|n ambiguity: take m
    if b == '|': return ''            # stray stroke, no value
    k = CLS[b] + (':' + acc if acc else '')
    return key[k]
lit = []
for line in open(os.path.join(C, 'work/ledger-opus.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split(); s = ''.join(dec(t) for t in toks); lit.append(s); print(f'{lab:>3} {s}')
L = ''.join(lit)
norm = open(os.path.join(C, 'work/normalized-opus.txt'), encoding='utf-8').read().split('[Under the stamp:]')
N = ''.join(ch for ch in unicodedata.normalize('NFD', ''.join(norm).lower()) if ch.isalpha() and unicodedata.category(ch) != 'Mn')
L0 = ''.join(ch for ch in unicodedata.normalize('NFD', L) if unicodedata.category(ch) != 'Mn')
print('\nletters literal:', len(L0), ' normalized:', len(N))
sm = difflib.SequenceMatcher(None, L0, N, autojunk=False)
print('match ratio %.3f' % sm.ratio()); print('editorial differences (literal -> normalized):')
for op, a1, a2, b1, b2 in sm.get_opcodes():
    if op != 'equal': print(f'  {op:8} ...{L0[max(0,a1-6):a1]}[{L0[a1:a2]}]{L0[a2:a2+6]}...  ->  [{N[b1:b2]}]')
