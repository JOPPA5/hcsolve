"""HCP1278: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1278/work/decode_opus.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {
 'source/picture-large.jpg': 'b22e1e5a5aeb4e8e84078482ddf3e4b01aa09ee05a8e200f059d7718e1025979',
 'source/address-large.jpg': '5ddaedcd1662f68bad84dea1bcf05d04d68614ddbb59f670c69a368a3072ae7b',
 'work/hires/cpc_1912--27_HU__HU_Jasz-Arokszalas_jolanka-103_pic.jpg': '7b045a547e2e93849adfcbc1e3cf7897661246727f85e5597b3571e58c33e702',
 'work/hires/cpc_1912--27_HU__HU_Jasz-Arokszalas_jolanka-103_adr.jpg': '8a5ae6367fcef4f64e5627a5ab2226b1d047e7166d622e42c9b1bc0758a384e2'}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f)
    if got != h: sys.exit(1)
KEY = {'F': 'r', ')': 's', 'X': 'u', '6': 'b', 'H': 'h', 'P': 'p', 'GY': 'gy', 'H=d': 'd', '{r=F.}': '{r=F.}',
       '[ü]': '[ü]', '[d]': '[d]', '[n]': '[n]', '[h]': '[h]', '{blot}': '{blot}', '.': '.'}
MARK = {'diaeresis': '̈', 'acute': '́'}
def dec(tok):
    base, _, acc = tok.partition(':')
    s = KEY.get(base, base.lower() if len(base) == 1 and base.isalpha() else None)
    if s is None: raise SystemExit('unknown token ' + tok)
    return unicodedata.normalize('NFC', s + MARK[acc]) if acc else s
print('\nLiteral decipherment, one row per written line:')
for line in open(os.path.join(D, 'work/ledger-opus.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    print(lab, ''.join(dec(t) for t in toks))
print('\nNormalized Hungarian (editorial word division, accents and spelling; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized-opus.txt'), encoding='utf-8').read())
