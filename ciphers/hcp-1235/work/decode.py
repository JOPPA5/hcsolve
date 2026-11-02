"""HCP1235: verify source hashes, decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1235/work/decode.py"""
import hashlib, os, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
H = {'source/picture-large.jpg': '5d03d378fdec548ccd5558b604c2efcb9d34a8e06830751cf8c8d32e48dd43e2',
     'source/address-large.jpg': '1e16f75ba134236977a314a6f3d4e1a178561fbd790f38b90a14a0e840771b48',
     'work/hires/cpc_1912--20_HU__HU_Jasz-Arokszalas_jolanka-101_pic.jpg': '1f6191fe190ab544839d16fad6348fa156cc16a28ab5aaba7ddf8dcb91515150',
     'work/hires/cpc_1912--20_HU__HU_Jasz-Arokszalas_jolanka-101_adr.jpg': '9c47c7ecb185876a4b6f9927aea6e49fb5986083f8531a7bf8da3db385d670f2'}
for f, h in H.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if line.startswith('#') or not line.strip(): continue
    lab, *t = line.split()
    print(lab, ''.join('{?}' if x == '?' else x.lower().replace("a'", 'á') for x in t))
