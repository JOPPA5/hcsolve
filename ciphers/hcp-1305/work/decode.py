"""HCP1305: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1305/work/decode.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/picture-large.jpg': '0cb65ad713ee66d6d914d9276912dfc11e0b7696a545fa2d32328ae4b248e861',
        'source/address-large.jpg': 'cdff485c1441784a35769a15e25e4c72767d8fb0c7646f410491675f400a14eb',
        'work/hires/cpc_1912--_HU__HU_Jasz-Arokszalas_jolanka-98_pic.jpg': '8446883735c7d694c6d8cd2e9ecc2ec0aa2d615f9907e48b5711d5d688139586',
        'work/hires/cpc_1912--_HU__HU_Jasz-Arokszalas_jolanka-98_adr.jpg': '09ad8c0ba3731e0c3cef9715b38674da96b7636e3640da8bed3055c592602b96'}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f)
    if got != h: sys.exit(1)
KEY = {'AE?': '{a|e}'}
MARK = {'diaeresis': '̈', 'acute': '́'}
def dec(tok):
    if tok.startswith('='): return tok[1:]
    base, _, acc = tok.partition(':')
    s = KEY.get(base, base.lower() if base.isalpha() and len(base) == 1 else None)
    if s is None: raise SystemExit('unknown token ' + tok)
    return unicodedata.normalize('NFC', s + MARK[acc]) if acc else s
print('\nLiteral decipherment, one row per written line (h stands for the h/p sign):')
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print('\nNormalized Hungarian (editorial word division, accents and spelling; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
