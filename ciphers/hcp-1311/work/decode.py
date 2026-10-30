"""HCP1311: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1311/work/decode.py"""
import hashlib, os, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {
 'source/picture-large.jpg': 'b87a710b6a1e2712f5262d836885760fb17319753e8e22b1c417c72de912d71c',
 'source/address-large.jpg': 'e140a2cd5ef7b1f96478da7cbf003cf2f686c5d8b857a808596d85e17f1542bd',
 'work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-81_pic.jpg': '33d911d146d2c87a879c800573a67ee4a7121fa3f55725e7d5190b601bb3f116',
 'work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-81_adr.jpg': 'bf8fd62a0ad12550b957a4d3e68df5ffe713bfbad810a6ea5e3844d5bcdca770'}
for f, h in HASH.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
SPECIAL = {'K2': 'k', 'I0': 'i', 'CS': 'cs', 'O:': 'ö', 'A:': 'á', '2½': '2½', '~x~': '', '!': '·'}
def dec(t):
    if t in SPECIAL: return SPECIAL[t]
    if t.startswith('?'): return '{' + dec(t[1:]) + '?}'
    if len(t) == 1 and t.isalpha(): return t.lower()
    raise SystemExit('unknown token ' + t)
n = 0
print('\nLiteral decipherment, one row per written line (h = the h/p sign, · = unresolved sign):')
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    n += len(toks)
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print(f'\n{n} signs in ledger.\n\nNormalized Hungarian (editorial; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
