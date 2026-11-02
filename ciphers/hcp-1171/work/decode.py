#!/usr/bin/env python3
"""hcp-1171: verify scan hashes, decode the digit signs, print the full card text."""
import hashlib, os, sys
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H = {'source/picture-large.jpg': 'be27e2b2c9f6ef1e875fa433bb60e3723591ad030612ed6a5e956ea19959abab',
     'source/address-large.jpg': '05bf7c378e2e51015384ca85b35ae37f9de6d870ab260ec3fe2d80a4bfb34d88',
     'work/hires/cpc_1915-11-22_HU_Mezokovesd_HU_Szomolya_szomolya-06_pic.jpg': 'da087a330add26201fc974d4830422022961a4d97010ed163ac252454493a87d',
     'work/hires/cpc_1915-11-22_HU_Mezokovesd_HU_Szomolya_szomolya-06_adr.jpg': '73c94fa5087a710e1f3abfbf36c1587c2afe7a4827d7ee7f811b49be713cf268'}
for p, h in H.items():
    if hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest() != h:
        sys.exit('HASH MISMATCH ' + p)
print('source hashes OK (%d files)' % len(H))
# Key transferred from FINAL card hcp-1174; only signs attested on this card.
KEY = {'1': 'i', '1.': 'a', '1:': 'e', "1'": 'á', '3': 'd', '3,': 'r', '3.': 'v',
       '4,': 'g', '7': 'k', '7,': 's', '8': 'm', '8,': 't', '9': 'p'}
C = [("7 1: 3 3. 1: 7,", 'kedves'), ("8 1. 3, 4, 1 8, 7 1' 8", 'margitkám'),
     ("1' 3, 9 1' 3", 'árpád')]
OUT = []
for ct, want in C:
    got = ''.join(KEY[t] for t in ct.split())
    if got != want:
        sys.exit('MISMATCH %r -> %r' % (ct, got))
    OUT.append(got)
print('cipher signs: %d, all decoded by the table\n' % sum(len(c.split()) for c, _ in C))
print('[%s %s]!\n' % (OUT[0].capitalize(), OUT[1].capitalize()))
print('''Szerencsésen megérkeztünk
nagyon szép és világos üdő volt
és jól megvolt fagyva haza-
felé mindenüt örömtől eltel-
ve daloltunk és fütyörésztünk
csak mégis mind a kettőnket
hogy ilyen alkalmatlanságot
csináltunk nektek mert olyan
későre maradtunk és nem
hagytunk aludni no de
bocsás meg mert nagyon
nehéz volt ott hagyni téged.
Más ujságot nem irhatok majd
levélbe többet.

Szerencsésen megérkeztem,
Nincsen semmi bajom,
Csak te nélküled, édesem,
Unatkozom nagyon.

Mindnyájatokat számta-
lanszor csókollak a legtisztáb-
szivvel. ([%s]) (A)
''' % OUT[2].capitalize())
print('Address: Tek. / Szépreménnyu / Sziber Margitka / kisasszonynak / Szomolya / u. p. Bogács')
print('Postmark: Mezőkövesd (M... legible), 915 NOV 2?; portal file name gives 1915-11-22.')
print('[ ] = enciphered on the card; the rest is open text (later struck through).')
