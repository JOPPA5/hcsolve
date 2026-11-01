"""HCP1274: verify source hashes and decode the sign ledger. Run from the repo root:
   python3 -I ciphers/hcp-1274/work/decode.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/picture-large.jpg': 'c628ef0a8e81bdf468ee38c51fa7b2d6a1d14fc650b908e30cd0d702a2666056',
        'source/address-large.jpg': '9a3ec680f7d5685f4ce4d69df9354800e7bd2ce352d5ac04ffb5f7479c9a7ae8',
        'work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-73_pic.jpg': 'f426cac3bf67e13a204bb0e1e451a430e74b5bd412b6433294fe260aa47abf29',
        'work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-73_adr.jpg': '1c97edde4955951be4c89872352a05ce8f330240e10947bbce467102ddb12a29'}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f)
    if got != h: sys.exit(1)
MARK = {'d': '̈', 'a': '́'}
def dec(tok):
    base, _, acc = tok.partition(':')
    if base == '[X]': return '[x]'
    s = base.lower()
    return unicodedata.normalize('NFC', s + MARK[acc]) if acc else s
print('\nLiteral decipherment, one row per written line (no word division on the card):')
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    print(lab, ''.join(dec(t) for t in toks))
print('\nNormalized Hungarian (editorial; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
