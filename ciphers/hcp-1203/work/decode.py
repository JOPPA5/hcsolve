"""HCP1203 (PARTIAL): check source hashes and print the ledger plus working normalization.
Run from the repo root: python3 -I ciphers/hcp-1203/work/decode.py"""
import hashlib, os, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/picture-large.jpg': '197a3da3d6ebba46c28cbba58598e63a81be487822a067984c9a22b097dec81f',
        'source/address-large.jpg': 'de0ede91bcb493e1b36f0900f16d5c7e1b9297fb510593005d8bb9acc8ebf0ef',
        'work/hires/cpc_--23_HU__HU_Rakos-Palota-Ujfalu_jolanka-88_pic.jpg': '45a87b8df5da51744d9c7f2fcf5b0ef5f8091c8d8b8dc5440d5393892805fed7',
        'work/hires/cpc_--23_HU__HU_Rakos-Palota-Ujfalu_jolanka-88_adr.jpg': 'f61f6d8be8774079cc6f374778197a28fe3169e1d052835109c96112f09e879c'}
for f, h in HASH.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
print('\nLedger:')
for l in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if l.strip() and not l.startswith('#'): print(l.rstrip())
print('\nWorking normalization (PARTIAL):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
