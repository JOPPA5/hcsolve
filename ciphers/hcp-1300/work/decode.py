"""HCP1300: verify source hashes and decode the sign ledger. From the repo root:
   python3 -I ciphers/hcp-1300/work/decode.py"""
import hashlib, os, sys
W = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(W, '..')
HASH = {'source/picture-large.jpg': '83fc655d38d2d4f510426ccb4830ed2329ca8730ccff2ddad6ee999e1335dd4a',
 'source/address-large.jpg': 'df7c5f962a33b8b3570ea0fb67b8ac7979c5cfeb757a551fd14963b6ea5b6ccf',
 'work/hires/cpc_--26_HU__HU_Jasz-Arokszalas_jolanka-91_pic.jpg': '0c851c78cc6c760dced3cf27fa59c5631e05f93c5b455f1f812920c2303e0509',
 'work/hires/cpc_--26_HU__HU_Jasz-Arokszalas_jolanka-91_adr.jpg': '788f91e94ed86a0c5114bd269769dfb9204f71c2eb7200e6056b1592896d1039'}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f)
    if got != h: sys.exit(1)
SPECIAL = {'GY': 'gy', 'CS': 'cs', 'NY': 'ny', 'EL': 'el', 'ZP': 'z', 'X': 'u', 'XF': 'f'}
n = 0; print('\nLiteral decipherment, row by row (h = h/p sign):')
for line in open(os.path.join(W, 'ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split(); out = ''
    for t in toks:
        if t.startswith('{'): out += t
        elif t in SPECIAL: out += SPECIAL[t]
        elif len(t) == 1 and t.isalpha(): out += t.lower()
        else: sys.exit('unknown token ' + t)
        n += 1
    print(f'{lab:>3} {out}')
print(f'\n{n} written signs in the ledger.\n\nNormalized Hungarian (editorial; see SOLUTION.md):')
print(open(os.path.join(W, 'normalized.txt'), encoding='utf-8').read())
