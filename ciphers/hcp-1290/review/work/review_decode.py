"""Independent reviewer decoder for HCP1290 (does not import or reuse work/decode.py).
Usage from repo root: python3 -I ciphers/hcp-1290/review/work/review_decode.py
Builds a corrected token list from work/ledger.txt with the three reviewer corrections,
decodes both versions with an own key table and reports the differences and statistics."""
import os, re, collections
B = os.path.dirname(os.path.abspath(__file__))
L = os.path.join(B, '..', '..', 'work', 'ledger.txt')
KEY = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower(), 'abcdefghijklmnopqrstuvwxyz'))
SIGN = {'F':'r',')':'s','X':'u','Z':'z','6':'b','+':'f','GY':'gy','CS':'cs','J?':'J','I?':'I','[BLOT]':'#',
        'A':'a','D':'d','E':'e','G':'g','H':'h','I':'i','J':'j','K':'k','L':'l','M':'m','N':'n','O':'o','P':'p','T':'t','V':'v'}
def tok(t):
    b = t.split(':')[0]
    if b not in SIGN: raise SystemExit('no value for ' + t)
    return SIGN[b]
rows = {}
for ln in open(L, encoding='utf-8'):
    if ln.strip() and not ln.startswith('#'):
        p = ln.split(); rows[p[0]] = p[1:]
fix = {k: list(v) for k, v in rows.items()}
# C1 row 03: sign after final H is dotted i, not o (higy)
i = len(fix['03']) - 2; assert fix['03'][i:] == ['O', 'GY']; fix['03'][i] = 'I'
# C2 row 20: marked sign is i with its dot (is), not o-acute
i = fix['20'].index('O:acute'); fix['20'][i] = 'I'
# C3 row 24: only three strokes (one m) between e and o
i = fix['24'].index('M'); assert fix['24'][i:i+2] == ['M', 'M']; del fix['24'][i]
n1 = n2 = 0
for k in rows:
    a = ''.join(map(tok, rows[k])); b = ''.join(map(tok, fix[k]))
    n1 += len(rows[k]); n2 += len(fix[k])
    print(k, b, '' if a == b else f'   <-- solver: {a}')
print('tokens solver', n1, 'corrected', n2)
txt = ''.join(''.join(map(tok, v)) for v in fix.values())
c = collections.Counter(re.sub(r'[^a-z]', '', txt.replace('gy','g').replace('cs','c')))
t = sum(c.values()); print('letters', t, ' '.join(f'{k}{v*100/t:.1f}' for k, v in c.most_common()))
print('unvalued signs: none (every token mapped); open tokens:', txt.count('#'), 'blot,', txt.count('J')+txt.count('I'), 'sense-based')
