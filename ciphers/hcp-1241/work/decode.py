"""HCP1241: check source hashes, decode the sign ledger with the Jolanka family key. From repo root:
   python3 -I ciphers/hcp-1241/work/decode.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/picture-large.jpg': '1269d934a2a436765bac3ba91d4ffb5ce85491a211c00dc93ba240f23b223a81',
        'source/address-large.jpg': '130e0dca1658e5bdad9c981a4d9fd4dc353515e500974060b88a53e5edd4be6c',
        'work/hires/cpc_1912-05-12_HU__HU_Jasz-Arokszalas_jolanka-20_pic.jpg': '5990c27082ab7877b935e37d27fd5ebb1e31992be0802809bb0615cca8c63faf',
        'work/hires/cpc_1912-05-12_HU__HU_Jasz-Arokszalas_jolanka-20_adr.jpg': 'b382612a247de1262292e5ee4a71228751804f7972e25afa0472dca5fafd8e01'}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f)
    if got != h: sys.exit(1)
KEY = {'F': 'r', ')': 's', 'X': 'u', '6': 'b', '+': 'f', 'GY': 'gy', 'CS': 'cs', 'B?': '{b?}', '[)]': '[s]', '.': '.'}
MARK = {'d': '̈', 'a': '́'}
def dec(tok):
    base, _, acc = tok.partition(':')
    s = KEY.get(base, base.lower() if base.isalpha() and len(base) == 1 else None)
    if s is None: raise SystemExit('unknown token ' + tok)
    return unicodedata.normalize('NFC', s + MARK[acc]) if acc else s
print('\nLiteral decipherment, one row per written line:')
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    print(lab, ''.join(dec(t) for t in toks))
print('\nNormalized text, including the plain-script parts (editorial; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
