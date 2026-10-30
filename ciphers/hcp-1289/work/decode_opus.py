"""HCP1289: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1289/work/decode_opus.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/picture-large.jpg': '21cbb74d3efb9cc72dd794403493ebade4fdc8e8dce379bf8f7b6b06ec859776',
        'source/address-large.jpg': 'dc33e0e97416d23a74a7684800d74fb57b18c199d3234b2621d45e8986a783da',
        'work/hires/cpc_--22_HU__HU_Jasz-Arokszalas_jolanka-87_pic.jpg': '3fedb295dea3195d4b29e3f88f20e7caa7de06b1ce48557cd94319912b2c8f30',
        'work/hires/cpc_--22_HU__HU_Jasz-Arokszalas_jolanka-87_adr.jpg': 'f8dfb7b9183d2873a46e1dff99386025aec9a718054c28a5f0e9ebac5874a38b'}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f)
    if got != h: sys.exit(1)
KEY = {'F': 'r', ')': 's', 'X': 'u', '6': 'b', '+': 'f', 'CS': 'cs'}
def dec(tok):
    base, _, acc = tok.partition(':')
    flag = ''
    for mark in '^#?':
        if base.endswith(mark): flag, base = mark, base[:-1]
    s = KEY.get(base, base.lower() if base.isalpha() and len(base) == 1 else None)
    if s is None: raise SystemExit('unknown token ' + tok)
    if acc: s = unicodedata.normalize('NFC', s + '̈')
    return {'^': '[%s]', '#': '(%s)', '?': '%s?', '': '%s'}[flag] % s
print('\nLiteral decipherment, one row per written line (h stands for the h/p sign):')
n = 0
for line in open(os.path.join(D, 'work/ledger-opus.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    n += len(toks)
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print(f'\n{n} signs decoded.')
print('\nNormalized Hungarian (editorial word division, accents and spelling; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized-opus.txt'), encoding='utf-8').read())
