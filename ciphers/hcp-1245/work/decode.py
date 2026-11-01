"""HCP1245: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1245/work/decode.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
H = 'work/hires/cpc_1912-03-20_HU__HU_Jasz-Arokszalas_jolanka-11_'
HASH = {'source/picture-large.jpg': '051a1d66015370ac84e15c2b83cfbd9df0f68edb096281e119337be050599f03',
        'source/address-large.jpg': '39e754ebd80f8a3d43bd1e6acd5d62c07b93b1751eba14e39817a6f0f8e66dd6',
        H + 'pic.jpg': '0dd990b9b24f0701716afbb0655bb367b350da395c477c6b54c902907285ace9',
        H + 'adr.jpg': '3559b6790ebe38c6a0e7739ea8221544b6b05bddd51fa0c7f8afb4b78fc21bd1'}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f)
    if got != h: sys.exit(1)
KEY = {'F': 'r', ')': 's', 'X': 'u', '6': 'b', 'GY': 'gy', 'CS': 'cs', 'N?': 'n', 'M?': 'm',
       '[?]': '[?]', '[?]Y': '[?]y', '[n?]': '[n?]'}
def dec(t):
    if t.startswith('<'): return t
    base, _, acc = t.partition(':')
    s = KEY.get(base, base.lower() if base.isalpha() else None)
    if s is None: raise SystemExit('unknown token ' + t)
    return unicodedata.normalize('NFC', s + '̋') if acc == 'dacute' else s
print('\nLiteral decipherment, one row per written line (<...> = plain Latin on the card):')
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    print(lab, ''.join(dec(t) for t in toks))
print('\nNormalized Hungarian (editorial word division, accents, spelling; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
