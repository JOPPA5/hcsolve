"""HCP1281: verify source hashes, decode the sign ledger, print the literal rows and the normalized text.
Run from the repo root:  python3 -I ciphers/hcp-1281/work/decode.py"""
import hashlib, os, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {
 'source/picture-large.jpg': '049a7acc4bf5a9dc46dd974965cade7a0fc4d394f04b5b334c374be7a2f315df',
 'source/address-large.jpg': '3a9839e02541d468a82a29a517d6c24c761f91117bf67db68df5cc840f7600ed',
 'work/hires/cpc_1914-06-10_HU__HU_Jasz-Arokszalas_jolanka-54_pic.jpg': 'f238ec564d7889a0c015dc4f6b12618c13c2620b40b56b197d73a9b06002ff1b',
 'work/hires/cpc_1914-06-10_HU__HU_Jasz-Arokszalas_jolanka-54_adr.jpg': '37d28ffb3aff8c8cad374023b5f3e6fb7c2239cd5bbe6c5ae1f2ee5c56a8fc35',
}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f)
    if got != h: sys.exit(1)
print('\nLiteral decipherment, one row per written line (h = h/p sign; brackets = doubtful sign):')
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    print(f'{lab:>3} ' + ''.join(toks))
print('\nNormalized Hungarian (editorial; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
