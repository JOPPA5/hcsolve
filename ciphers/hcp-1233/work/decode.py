"""HCP1233: verify source hashes, decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1233/work/decode.py"""
import hashlib, os, sys, unicodedata
W = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(W, '..')
HASH = {'source/picture-large.jpg': '3ec923171afa031d06719a699b546d3465223ea9fd8068b6f8950f111303622b',
        'source/address-large.jpg': '3d11758e6ba5b3006e30cbad2248b54c7bc9a3d823ee2e30d4e6860bfbc970ee',
        'work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-67_pic.jpg': '2b793716caa809e522d617a83d32cc738d2d27931187558c1a51caffd9578b3e',
        'work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-67_adr.jpg': '521502718f6760185750522c2bd2f054b9e8dcbb9b109b11f1f445ae425459f3'}
for f, h in HASH.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
KEY = {'F': 'r', ')': 's', 'X': 'u', '6': 'b', '+': 'f', 'H': 'h', 'CS': 'cs', '?': '?'}
MARK = {'diaeresis': '̈', 'double-acute': '̋'}
def dec(t):
    if t.startswith('['): return '[' + dec(t[1:-1]) + ']'
    base, _, acc = t.partition(':')
    s = KEY.get(base, base.lower() if len(base) == 1 and base.isalpha() else None)
    if s is None: raise SystemExit('unknown token ' + t)
    return unicodedata.normalize('NFC', s + MARK[acc]) if acc else s
print('\nLiteral decipherment, one row per written line (h stands for the h/p sign, [x] = value from sense or a damaged trace, ? = mark with no value):')
for line in open(os.path.join(W, 'ledger.txt'), encoding='utf-8'):
    if line.strip() and not line.startswith('#'):
        lab, *toks = line.split()
        print(lab, ''.join(dec(t) for t in toks))
print('\nNormalized Hungarian (editorial; see SOLUTION.md):')
print(open(os.path.join(W, 'normalized.txt'), encoding='utf-8').read())
