#!/usr/bin/env python3
"""hcp-1173: verify scan hashes, decode the digit cipher, print the PARTIAL text."""
import hashlib, os, sys
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H = {'source/picture-large.jpg': 'ea981947d4a957517a44f774cc84f4dbc6bf9443fb35e1502c20804b96f855ed',
     'source/address-large.jpg': 'd119fae9dc62759135e0927e85ffca72839e03590e395a56e3783d8586c9f66b',
     'work/hires/cpc_1916-05-25_HU_Mezokovesd_HU_Szomolya_szomolya-37_pic.jpg': '867aa6f786a452b35189061c32c256cac40d51978074f0e5b6ae978949d808ff',
     'work/hires/cpc_1916-05-25_HU_Mezokovesd_HU_Szomolya_szomolya-37_adr.jpg': 'c0db58ff7e6fac726b66a18d238f7a9b5a8330fefc45d0fbb8a4635bd5503580'}
for p, h in H.items():
    if hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest() != h:
        sys.exit('HASH MISMATCH ' + p)
print('source hashes OK (%d files)' % len(H))
# Family key (hcp-1174), only signs attested on this card.
KEY = {'1': 'i', '1.': 'a', '1:': 'e', "1'": 'á', ':1': 'ü', '3': 'd', '3,': 'r', '3.': 'v',
       '4,': 'g', '5': 'h', '7': 'k', '7,': 's', '8': 'm', '8,': 't', '9': 'p'}
C = [("7 1: 3 3. 1: 7,", 'kedves'), ("8 1. 3, 4, 1 8, 7 1' 8", 'margitkám'),
     ("5 :1", 'hü'), ("7 1: 3 3. 1: 7, 1: 3", 'kedvesed'), ("1' 3, 9 1' 3", 'árpád')]
out = []
for ct, want in C:
    got = ''.join(KEY[t] for t in ct.split())
    if got != want:
        sys.exit('MISMATCH %r -> %r vs %r' % (ct, got, want))
    out.append(got)
print('cipher signs: %d, all decode by the table' % sum(len(c.split()) for c, _ in C))
print()
print('[%s %s]!' % (out[0].capitalize(), out[1].capitalize()))
print('''Szerencsésen haza értem, nagyon szép idő volt, jól meg volt fagyva a sár,
kocsira nem <UNREAD WORD 1> de még jobb, mert szét rázott volna. Elég hamar
haza értem, hat óra után tíz perccel. Egész úton egy élő lénnyel sem
találkoztam. Most midőn e lapot írom, este három negyed tíz óra van, a gyerekek
alszanak, én pedig a kis asztal mellett gondolkodva ülök és írok. Pistának is
most írok egy lapot. (Mezőkövesd) 1916. V/25.

Itt, benn e szívbe lész te zárva,
S itt senki másnak nincs helye,
Hő szerelmem sugarába
Senki más nem fürödhete.

Számtalanszor csókollak <UNREAD WORD 2> és mindnyájatokat''')
print('maradok [hű %s]) [%s])' % (out[3], out[4].capitalize()))
print()
print('Address: Őnsg. / Rózsa reményű / Sziber Margitka / kisasszonynak / Szomolya / u. p. (Bogács)')
