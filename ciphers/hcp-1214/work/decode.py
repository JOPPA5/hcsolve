"""HCP1214: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1214/work/decode.py"""
import glob, hashlib, os, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/picture-large.jpg': '51a8326de35faeed08e84e4195572efcaab6f3f1cb94275aa077cef821ea226d',
        'source/address-large.jpg': '1b9aef8727c25c5cef7c9a18951f6abc8c3ce00040ad04a32275c4d881d5da0a',
        'work/hires/cpc_--_HU__HU_helyben-(locally)-Budapest_jolanka-63_pic.jpg': 'b254ad9e53c6ec5b3a730380fb7cbf8c008a2a5c71c7d1c4a8b2732a1d04b1f5',
        'work/hires/cpc_--_HU__HU_helyben-(locally)-Budapest_jolanka-63_adr.jpg': '0929da04e1f6f718a115fd77f65296747127b05833999ec5b4643f914583dc6b'}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f)
    if got != h: sys.exit(1)
KEY = {'F': 'r', ')': 's', 'X': 'u', '6': 'b', '+': 'f', 'H': 'h', 'GY': 'gy', 'Z#': '[z]', 'A#': '[a]',
       '#': '{#}', 'J!': '{j}', 'D!': '{d}', 'E?': '{e}', 'O:': 'ö', 'X:': 'ü'}
def dec(t):
    if t in KEY: return KEY[t]
    if len(t) == 1 and t.isalpha(): return t.lower()
    raise SystemExit('unknown token ' + t)
print('\nLiteral decipherment, row by row (h = h/p sign; {} = see SOLUTION.md):')
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    print(lab, ''.join(dec(t) for t in toks))
print('\nNormalized Hungarian (editorial):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
