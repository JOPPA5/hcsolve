"""HCP1275: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1275/work/decode_opus.py"""
import hashlib, os, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HIRES = 'work/hires/cpc_1913-08-13_HU__HU_Jasz-Arokszalas_jolanka-40_'
HASH = {'source/picture-large.jpg': '7b9f69eb54cb71c3c6129c21b15b5a4aa1b0be2ead31febc48863f567f2a0ac7',
        'source/address-large.jpg': '2683c50f15f6cec968b4402093be6d84e2a1e0067bf1a28fd34a9161dae31cb3',
        HIRES + 'pic.jpg': 'eae11e5119c5b23325edbc9e52f011e1c963d4d742c6738770d83bcb65d36ac1',
        HIRES + 'adr.jpg': 'f1290723474b329b95b347cc2151be9c3bc2bed4f758bbc9364ce47a0f7de00f'}
for f, h in HASH.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
SPECIAL = {'O:': 'ö', 'U:': 'ü', "O'": 'ó', "I'": 'í', '.': '.', ',': ','}
def dec(t):
    if t in SPECIAL: return SPECIAL[t]
    if t[0] in '{[': return t
    return t.lower()
rows = []
for line in open(os.path.join(D, 'work/ledger-opus.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    rows.append((lab, ''.join(dec(t) for t in toks)))
print('\nLiteral decipherment, one row per written line (E1 = up the right edge, S = under the stamp; h stands for the h/p sign):')
for lab, txt in rows: print(f'{lab:>3} {txt}')
print(f"\nSigns (approximate, see SOLUTION.md): {sum(len(l.split())-1 for l in open(os.path.join(D,'work/ledger-opus.txt'),encoding='utf-8') if l.strip() and not l.startswith('#'))}")
print('\nNormalized Hungarian (editorial word division, accents and spelling; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized-opus.txt'), encoding='utf-8').read())
