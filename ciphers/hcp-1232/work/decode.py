"""HCP1232: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1232/work/decode.py"""
import hashlib, os, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/picture-large.jpg': '33878f472e7f28a05ea468b57d0272de5847bf56fad9f2b5e5e59b57bdd5c6de',
        'source/address-large.jpg': '192428c57be4e0d287dd4da2eebdba328ca98b50d1882bbbe269293ad662b271',
        'work/hires/cpc_--24_HU__HU_Jasz-Arokszalas_jolanka-89_pic.jpg': 'dc325afb7703d1e4a7f2192e491d5856a9548cca48b2e100ab42a69dbe8af03b',
        'work/hires/cpc_--24_HU__HU_Jasz-Arokszalas_jolanka-89_adr.jpg': '9ab2a2940c44781753bc62a924923c5c8854d9e190ad1f960392db59d6965b1f'}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f)
    if got != h: sys.exit(1)
KEY = {'F': 'r', ')': 's', 'X': 'u', '6': 'b', '+': 'f', 'O:': 'ö', 'X:': 'ü', '#': '[blot]'}
def dec(t):
    if t.startswith('='): return t[1:]
    if t.startswith('{'): return '{' + dec(t[1:-1]) + '}'
    if t in KEY: return KEY[t]
    if len(t) == 1 and t.isalpha(): return t.lower()
    raise SystemExit('unknown token ' + t)
print('\nLiteral decipherment, one row per written line ({x} = restored or doubtful sign):')
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print('\nNormalized Hungarian (editorial; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
