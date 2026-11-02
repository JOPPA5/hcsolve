"""HCP1221: verify source hashes, decode the sign ledger with the Jolanka family key.
Run from the repo root: python3 -I ciphers/hcp-1221/work/decode.py"""
import hashlib, os, re, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/picture-large.jpg': '733441334f19e70d8d6c9d275b1fb93a57b6883540e86bf99c801cfe96f0cd89',
        'source/address-large.jpg': 'ef3a9b37759afa9c1c9eab86f5b9daa40e62fa35b56a859e31a4c28435a11de5',
        'work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-66_pic.jpg': '5c7ff43fc4b50dbf3b1a3f981d4c06f884a29e1ea9b9fe61e6042f9866b4d657',
        'work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-66_adr.jpg': '9fda39dc78afab18c0ba7c9d936e4aaf2c4537b6256af6c763b47b67ed031f0f'}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f)
    if got != h: sys.exit(1)
KEY = {'F': 'r', ')': 's', 'X': 'u', '6': 'b', '+': 'f', 'H': 'h', 'P': 'p', 'CS': 'cs', '8': '8', '*': '', 'I?': 'i', 'D?': 'd'}
MARK = {'acute': '́', 'double': '̋', 'diaeresis': '̈'}
def dec(tok):
    base, *marks = tok.split(':')
    if base.startswith('{'):
        return '[' + base.strip('{}').lower() + ']'
    s = KEY.get(base, base.lower() if base.isalpha() and len(base) == 1 else None)
    if s is None: raise SystemExit('unknown token ' + tok)
    for m in marks:
        if m != 'dot': s += MARK[m]
    return unicodedata.normalize('NFC', s)
rows = []
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    rows.append((lab, ''.join(dec(t) for t in toks)))
print('\nLiteral decipherment, one row per written line (h and p are one sign, chosen by word sense; [x] = restored under overwrite):')
for lab, txt in rows: print(f'{lab:>3} {txt}')
print('\nNormalized Hungarian (editorial word division, accents and spelling; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
