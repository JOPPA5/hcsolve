"""HCP1302: verify scan hashes and print the partial ledger. Run from the repo root:
   python3 -I ciphers/hcp-1302/work/decode_opus.py"""
import hashlib, os, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
H = {'source/picture-large.jpg': 'acabcabdd0fb0a1dd37a977d765a859f668504360177130e495805943f445a23',
     'source/address-large.jpg': '4a3a8d3ed0e81c415c9e6a79cd1c42a096348a99ae64d2de046afe0a7ae66fa7',
     'work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-78_pic.jpg': '511290e04453f0a5614a383ea97f64ef3d0c55a20456a9ac27f2a07b49d799f7',
     'work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-78_adr.jpg': '82f7e89c4c2d6dc2ed444a96fbfa47c08d0df1537d2b7539538fb193f4841347'}
for f, h in H.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
print('\nPARTIAL literal reading; {?} = not read, [x] = word sense:')
for l in open(os.path.join(D, 'work/ledger-opus.txt'), encoding='utf-8'):
    if l.strip() and not l.startswith('#'):
        lab, *t = l.split(); print(f'{lab:>3} ' + ''.join(t))
