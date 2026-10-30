"""HCP1315: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1315/work/decode_opus.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
P = 'work/hires/cpc_1914--_HU__HU_Jasz-Arokszalas_jolanka-119_'
HASH = {'source/picture-large.jpg': '69349e01a4cfa0392501d9def528db16a2ba61b4bdfcbbac80703ce1091a7a11',
        'source/address-large.jpg': 'a77ce8d93de9ee70f72d48f63b92d0dd2f4bb2ffe33ab1a7038371605dd3cb27',
        P + 'pic.jpg': '6bd8d90a14df63d4dd999070bef53d694bd8df7d540ba6a6c3c3e3b63d6b9b56',
        P + 'adr.jpg': '74c40e2077f747b05cdac1c47756e6364f5a3ed281824516efd263173af587f2'}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f)
    if got != h: sys.exit(1)
SPECIAL = {'1/2': '½', '9': '9', '{a|e}': '{a|e}', '[s]': '[s]', 'TT': 'tt', 'CS': 'cs'}
MARK = {'d': '̈', 'dd': '̋'}
def dec(tok):
    base, _, acc = tok.partition(':')
    weak = base.endswith('?') and len(base) > 1
    base = base.rstrip('?') if weak else base
    s = SPECIAL.get(base, base.lower() if base.isalpha() and len(base) == 1 else None)
    if s is None: raise SystemExit('unknown token ' + tok)
    if acc: s = unicodedata.normalize('NFC', s + MARK[acc])
    return s + ('?' if weak else '')
n = 0
print('\nLiteral decipherment, one row per written line (? = weak sign, see SOLUTION.md):')
for line in open(os.path.join(D, 'work/ledger-opus.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split(); n += len(toks)
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print(f'\n{n} signs in the ledger.')
print('\nNormalized Hungarian (editorial word division, accents and spelling; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized-opus.txt'), encoding='utf-8').read())
