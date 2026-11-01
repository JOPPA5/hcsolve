"""HCP1266: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1266/work/decode.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/picture-large.jpg': 'f6d91858e4d3970ac7d67275a53acb42b046b0e3a223c54a05d63074da7bc2c0',
        'source/address-large.jpg': '605a16ca62c074874593010cd253cc8b7435f7ccc40451c996a4351c7836c3aa',
        'work/hires/cpc_--09_HU__HU_Jasz-Arokszalas_jolanka-83_pic.jpg': '08ef049b6a089cdac9f5f0c14181e0b5f174dcc510fd22af957c09e13c054e0d',
        'work/hires/cpc_--09_HU__HU_Jasz-Arokszalas_jolanka-83_adr.jpg': '84f0bae10335f9f3b8b58106e8a35b2f5c602776e9f2d6d806e370369ada6b0e'}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f)
    if got != h: sys.exit(1)
KEY = {'F': 'r', ')': 's', 'X': 'u', '6': 'b', '+': 'f', '8': 'k', 'DP': '{d=p}', 'HD': '{h=d}', '?': '{?}'}
MARK = {'diaeresis': '\u0308', 'double-acute': '\u030b', 'acute': '\u0301'}
def dec(tok):
    base, _, acc = tok.partition(':')
    s = KEY.get(base, base.lower() if len(base) == 1 and base.isalpha() else None)
    if s is None: raise SystemExit('unknown token ' + tok)
    return unicodedata.normalize('NFC', s + MARK[acc]) if acc else s
print('\nLiteral decipherment, one row per written line:')
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print('\nNormalized Hungarian ([ ] supplied by editor, < > sign read on word sense, {?} overwritten sign):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
