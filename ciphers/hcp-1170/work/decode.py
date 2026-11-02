#!/usr/bin/env python3
"""hcp-1170: verify scan hashes, decode work/transcription.txt, print the full card text."""
import hashlib, os, sys
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H = {'source/picture-large.jpg': '18a0cdda5953e9a49233524448e1eed50b24e1ea3b75a7c61cd23caa8fa05058',
     'source/address-large.jpg': '853ab0119307d8d187f135a04949ddeacf5c73a612245c7633c1ad77adcee8a7',
     'work/hires/cpc_1915-12-14_HU_Mezokovesd_HU_Szomolya_szomolya-11_pic.jpg': 'b2fb97566b801d2fabc0d7e2c4929ae5a3ad024db43cc26b55f4873999089acd',
     'work/hires/cpc_1915-12-14_HU_Mezokovesd_HU_Szomolya_szomolya-11_adr.jpg': 'a12ff4939f74afa0fb463578ced7b7611035254aa33fba5184ffb3d386b064e9'}
for p, h in H.items():
    if hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest() != h:
        sys.exit('HASH MISMATCH ' + p)
print('source hashes OK (%d files)' % len(H))
FAMILY = {'0': 'o', '0,': 'ö', '1': 'i', '1.': 'a', '1:': 'e', "1'": 'á', ':1': 'ü', '2,': 'cs',
          '2.': 'é', '3': 'd', '3,': 'r', '3.': 'v', '4,': 'g', '5': 'h', '5,': 'l', '6,': 'n',
          '7': 'k', '7,': 's', '7.': 'sz', '8': 'm', '8,': 't', '9': 'p', '9,': 'z'}
NEW = {'-1': 'ú', '4.': 'gy', '6': 'j', '6.': 'ny'}   # first established on this card; '-1' = u, ú, printed ú by standard spelling only
KEY = {**FAMILY, **NEW}
rows = [l.strip() for l in open(os.path.join(D, 'work/transcription.txt'), encoding='utf-8')
        if l.strip() and not l.startswith('#')]
words = []
signs = []
for r in rows:
    for w in r.split('|'):
        t = w.split()
        signs += t
        words.append(''.join(KEY[x] for x in t))   # KeyError = unknown sign
# Check against the stated reading (ő is written with the ö sign, so üdö here; the word mindnyájatokat breaks at a line end on the card).
RAW = 'drága margitkám üdvözöllek és téged és mindnyája tokat mi újság van ot és hogy vagytok rosz üdö van e ot'
if ' '.join(words) != RAW:
    sys.exit('MISMATCH\n%s\n%s' % (' '.join(words), RAW))
print('cipher signs: %d, distinct: %d (%d family, %d new); all decoded by the table'
      % (len(signs), len(set(signs)), len(set(signs) & set(FAMILY)), len(set(signs) & set(NEW))))
print('raw decode:', ' '.join(words))
print('''
[Drága Margitkám]! [Üdvözöllek és] csókollak [téged és mindnyájatokat. Mi újság
van ot és hogy vagytok, rosz üdő van-e ot], írd meg, hogy mikor jön kedves anyukád
Kövesdre. Karácsonyig talán még le jön [card: jöm], mert ha megírod akkor bemegyek a
fényképészhez és megmondom hogy mikor legyen kész biztosan a kép. Semi különös
ujság nincs. Számtalanszor csókollak mindnyájatokat maradtam
Mezőkövesd 1915. XII/14.

Address: Tek. / Szépreményű / Sziber Margitka / kisasszonynak / Borsod megye / Szomolya / u. p. (Bogács)
Postmark: Mezőkövesd 915 DEC 13 N9
[ ] = enciphered on the card; the open text is typed here, read from the pixels.''')
