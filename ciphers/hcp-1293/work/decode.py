"""HCP1293: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1293/work/decode.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
H = {'source/picture-large.jpg': 'da6ebe5bb9d6d8d91c55458b28eb199722ef8a05f5eb05a7580568e4b7c24869',
     'source/address-large.jpg': 'c80603c35893336f85ee1b4e4172bd53f26633c00951cae87afd93baff1272b3',
     'work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-76_pic.jpg': '7f282f45aef02c044b8d268168ae234daa83d116e19b39572981ff351c2802b9',
     'work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-76_adr.jpg': 'c91989a477ea7b80e461f67327761883e07a595d754ef049fb07ac063ec3c8fc'}
for f, h in H.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
LETTERS = set('ABDEFGHIJKLMNOPRSTUVYZ') | {'CS'}
def dec(t):
    b, _, acc = t.partition(':')
    if b not in LETTERS: raise SystemExit('unknown token ' + t)
    s = b.lower()
    return unicodedata.normalize('NFC', s + '̈') if acc == 'diaeresis' else s
print('\nLiteral decipherment, one row per written line:')
for l in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if l.strip() and not l.startswith('#'):
        lab, *t = l.split()
        print(f'{lab:>3} ' + ''.join(dec(x) for x in t))
print('\nNormalized Hungarian (editorial; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
