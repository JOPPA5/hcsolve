"""HCP1273: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1273/work/decode.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/picture-large.jpg': 'dc103d2cd33757422946d933dda33c91ced5b3cfa50c83c6217b205d801dec47',
        'source/address-large.jpg': '978c47884fe717f718dbfbaf7df1e586dee245df07d96d0af17ae8e51556b6b8',
        'work/hires/cpc_1912-05-04_HU__HU_Jasz-Arokszalas_jolanka-18_pic.jpg': 'dd0662096455aa7baf39a81c12c44e94aeda0a7eb622782b0e0f7e67c037f372',
        'work/hires/cpc_1912-05-04_HU__HU_Jasz-Arokszalas_jolanka-18_adr.jpg': 'fb415989858b0d76c06be53bbc90c45698d81821270dec4c62714eefc944cc94'}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f)
    if got != h: sys.exit(1)
KEY = {'F': 'r', ')': 's', 'X': 'u', '6': 'b', '+': 'f', 'H': 'h', 'GY': 'gy', 'CS': 'cs'}
MARK = {'diaeresis': '̈'}
def dec(tok):
    base, _, acc = tok.partition(':')
    s = KEY.get(base, base.lower() if base.isalpha() else None)
    if s is None: raise SystemExit('unknown token ' + tok)
    return unicodedata.normalize('NFC', s + MARK[acc]) if acc else s
print('\nLiteral decipherment, one row per written line (h stands for the h/p sign):')
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print('\nNormalized Hungarian (editorial word division, accents and spelling; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
