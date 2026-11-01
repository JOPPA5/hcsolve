"""HCP1284: verify source hashes, print the decoded ledger and normalized text. Run from repo root:
   python3 -I ciphers/hcp-1284/work/decode.py"""
import hashlib, glob, os, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/picture-large.jpg': 'bd250d30f27dbef8aebc1e4399718d8b0f00bafd77f591c2cb65240e16fd49c9',
        'source/address-large.jpg': 'baa405f22c65163861df8e8d62f4098da8784bec972cd228bb11d2ede4e3a336',
        'work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-74_pic.jpg': 'a41d5fa7497fac5cc449505d580de2b6301f9d4583caf69e2045f9baa8401b49',
        'work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-74_adr.jpg': '9d376c47ef5d88e139a8dbb34c05de2786e1228708286fcf136bde9d17358384'}
for f, h in HASH.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
UM = {'o:': 'ö', 'u:': 'ü'}
print('\nLiteral decipherment, row by row:')
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *t = line.split()
    print(f'{lab:>3} ' + ''.join(UM.get(x, x) for x in t))
print('\nNormalized Hungarian (editorial; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
