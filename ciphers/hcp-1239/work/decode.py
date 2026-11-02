"""HCP1239: verify image hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1239/work/decode.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
N = 'cpc_1912-06-_HU__HU_Jasz-Arokszalas_jolanka-105'
HASH = {'source/picture-large.jpg': '0528e84a51eabc26394d8ea961cadd6e3545723a487e3bacf2a13afe10c43ca4',
        'source/address-large.jpg': 'a35122f516d616ae960c189da4c9e23b9e2e1534cd8a60ed7d9fe3ae53b24469',
        f'work/hires/{N}_pic.jpg': '5523e1bf7ed35d1329e3ece54ac367e2192eca5097f833769a10dc2a8c8c470c',
        f'work/hires/{N}_adr.jpg': 'eb79c7753b9a63ca2bab9e07795b3f0e5266a2eeb0776aab3c1d84e22068402e'}
for f, h in HASH.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
KEY = {'F': 'r', ')': 's', 'X': 'u', '6': 'b', '+': 'f', 'H': 'h', 'GY': 'gy', 'CS': 'cs', 'K8': 'k',
       'D>p': 'p', 'D>h': 'h', '?s': 's', '?g': 'g', '{T}': 't', '{J}': '[j]', '{#}': '[#]', '-': '-', ':': ':'}
def dec(t):
    b, _, m = t.partition(':') if t != ':' else (t, '', '')
    s = KEY.get(b, b.lower() if b.isalpha() else None)
    if s is None: raise SystemExit('unknown token ' + t)
    return unicodedata.normalize('NFC', s + '̈') if m == 'd' else s
print('\nLiteral decipherment, one row per written line ([j] [#] = signs taken as deleted):')
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if line.strip() and not line.startswith('#'):
        lab, *toks = line.split()
        print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print('\nNormalized Hungarian (editorial word division, accents and spelling; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
