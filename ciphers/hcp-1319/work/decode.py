"""HCP1319: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1319/work/decode.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/address-large.jpg': 'b661f385abb78cd202573301c0ba23a7b00f30ccb99e915298870b4b7f1c9c34',
        'source/picture-large.jpg': '79bde8cb32baaec690aa325ca0c6ae8c4351a36d486e0b92c475a393252cb48b',
        'work/hires/cpc_1912-09-_HU__HU_Jasz-Arokszalas_jolanka-107_adr.jpg': '88e5a0abd90b365f8f2fc7d6066456b981add95502201dfe49a641d904fa0d0d',
        'work/hires/cpc_1912-09-_HU__HU_Jasz-Arokszalas_jolanka-107_pic.jpg': '1f3beac08307188c75795b4f5bdc9c52d9a32ac18e6a0ca6d27d3ead892fc4fc'}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f)
    if got != h: sys.exit(1)
KEY = {c: c.lower() for c in 'ABDEGHIJKLMNOPRSTUVZ'}
KEY.update({'SD': 'd', 'GY': 'gy'})
def dec(tok):
    base, _, acc = tok.partition(':')
    q = base.endswith('?'); base = base.rstrip('?')
    s = KEY[base]
    if acc == 'diaeresis': s = unicodedata.normalize('NFC', s + '̈')
    return '{' + s + '?}' if q else s
print('\nLiteral decipherment, one row per written line ({x?} = value rests on word sense):')
n = 0
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split(); n += len(toks)
    print(lab, ''.join(dec(t) for t in toks))
print(f'\n{n} signs decoded.\n\nNormalized Hungarian (editorial; [ ] = letters not written on the card):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
