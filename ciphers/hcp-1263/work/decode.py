"""HCP1263: verify scans, decode the sign ledger. Run from repo root: python3 -I ciphers/hcp-1263/work/decode.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
N = 'cpc_1913--_HU__HU_Jasz-Arokszalas_jolanka-109_'
HASH = {'source/address-large.jpg': '4975beecabb79289c8d4b5c5be2c07f1b203dbddf71d679b0936be0f99994ae5',
        'source/picture-large.jpg': 'bddd65ba8af25d41989c1a16bab33892875d2bd5f615f44451e79ce0e27ce9f5',
        'work/hires/' + N + 'adr.jpg': 'e29382e037f0b2c3f69ec4ce469b8b021d8bf2ca18a71e01c7ff5f19ca39eca7',
        'work/hires/' + N + 'pic.jpg': '02032066ff5af85ee35b6c42800848239cb9ce92f9781addc9ea6f33c02be056'}
for f, h in HASH.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
SPECIAL = {'K8': 'k', 'D1': 'd', 'Z9': 'z', 'CS': 'cs', 'A?': '[a]', '3': '3', 'O:d': 'ö', 'U:d': 'ü', 'U:x': 'ü', 'N:x': 'n', 'M:k': 'm', 'R:g': 'r', 'F:x': 'f'}
def dec(t):
    if t in SPECIAL: return SPECIAL[t]
    if len(t) == 1 and t.isalpha() and t.isupper(): return t.lower()
    raise SystemExit('unknown token ' + t)
print('\nLiteral decipherment, one row per written line ([a] = rubbed sign restored):')
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print('\nNormalized Hungarian (editorial word division, accents, spelling; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
