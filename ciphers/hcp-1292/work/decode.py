"""HCP1292: verify source hashes, print the row reading and normalized text. Run from repo root:
   python3 -I ciphers/hcp-1292/work/decode.py"""
import hashlib, os, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
H = {'source/picture-large.jpg': 'd099307edec4c17daefd451067f6264caa7d753033f791827e7c62d8f2661107',
     'source/address-large.jpg': 'bebabed14ad1a1c68d8156c655cf17f83408c1832fd780337eeaafa148c39db8',
     'work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-75_adr.jpg': '03dceafa776d527c490583fc938b3216249edb7652e4b7e6fcfef5c19d93a5fc'}
for f, h in H.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
print('\nRow reading:')
for l in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if l.strip() and not l.startswith('#'): print(l.rstrip())
print('\nNormalized:')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
