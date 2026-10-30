"""HCP1296: verify source hashes and print the diplomatic reading (the card has no cipher).
Run from repo root: python3 -I ciphers/hcp-1296/work/show_plain.py"""
import hashlib, os, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/picture-large.jpg': '826d6675671a5442afc9141b01163a7160fd08d66e00c40321fee415d622d06c',
        'source/address-large.jpg': '93c2fa1e944cef6b2588f5ea0d33577833c470dbe1f9ae7c9a98853381895229',
        'work/hires/cpc_1912-06-11_HU__HU_Jasz-Arokszalas_jolanka-25_pic.jpg': '5ddecf2b1c08c533027bfbca0960cc07048b32184e85c66895d4305153122244',
        'work/hires/cpc_1912-06-11_HU__HU_Jasz-Arokszalas_jolanka-25_adr.jpg': '8dac1ee83b6ee6137fbf46b03a21839ec640e6737b1f68359d4e54be6d9df182'}
for f, h in HASH.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
print(open(os.path.join(D, 'work/transcription.txt'), encoding='utf-8').read())
