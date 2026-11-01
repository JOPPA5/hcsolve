"""HCP1264: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1264/work/decode_opus.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/picture-large.jpg': '62caf960a09007612a080eb8739d1297594b4cea90f80a2de5ded16462a37feb',
        'source/address-large.jpg': '8a7283be4296a53079c7bb48e749ca1c70926a0809833b0be5f476888b7c934d',
        'work/hires/cpc_-02-04_HU__HU_Jasz-Arokszalas_jolanka-93_pic.jpg': 'd10cbb5edbd7a62edd7a928dd14bfccad94a62e41a7e2822a6165dc8570fc13b',
        'work/hires/cpc_-02-04_HU__HU_Jasz-Arokszalas_jolanka-93_adr.jpg': '91369eefb5e8e544f91b35373af12656ad523c03a60d3ceef80dd93458884703'}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f)
    if got != h: sys.exit(1)
KEY = {'F': 'r', ')': 's', 'X': 'u', '6': 'b', '+': 'f', 'H': 'h', 'D': 'd', "D'": 'd', 'CS': 'cs', 'M?': 'm',
       'a?': '[a]', 'e!': '{struck e}', 'T?': '{t?}', 'X?': '{u/f}', '-': '-', '<': '<', '>': '>'}
MARKS = {'<', '>', '-'}  # insertion brackets and line-end dash: written marks, not cipher signs
MARK = {'d': '̈', 'a': '́'}
def dec(tok):
    base, _, acc = tok.partition(':')
    s = KEY.get(base, base.lower() if base.isalpha() else None)
    if s is None: raise SystemExit('unknown token ' + tok)
    return unicodedata.normalize('NFC', s + MARK[acc]) if acc else s
print('\nLiteral decipherment, one row per written line (h stands for the h/p sign):')
n = 0
for line in open(os.path.join(D, 'work/ledger-opus.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    n += sum(t not in MARKS for t in toks)
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print(f'\n{n} signs')
print('\nNormalized Hungarian (editorial word division, accents and spelling; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized-opus.txt'), encoding='utf-8').read())
