#!/usr/bin/env python3
"""hcp-1155: check scan hashes, decode work/transcription.txt, assert the reading, print the full text."""
import hashlib, os, sys, collections
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H = {'source/picture-large.jpg': '84b3b352ef93dfc3badeb99cd022c88c09045dbca3bb4a7eb066d4fcb38a5c6e',
     'source/address-large.jpg': '4278d0f93e8c6f4c9f6cdd3820fbcac059b1627f7d33f78f21a7e23acd99a82c',
     'work/hires/cpc_1916-02-22_HU_Mezokovesd_HU_Szomolya_szomolya-19_pic.jpg': '3b8600375469bba92fc56f1877d86669599cc0448ae6f214fb3237923fc9666b',
     'work/hires/cpc_1916-02-22_HU_Mezokovesd_HU_Szomolya_szomolya-19_adr.jpg': 'fac9c3405f3dbdb0f8accc44a4a25d9338bc3a39b332238cb8b86b08caa09d55'}
for p, h in H.items():
    if hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest() != h:
        sys.exit('HASH MISMATCH ' + p)
print('source hashes OK (%d files)' % len(H))
FAMILY = {'0': 'o', '0,': 'ö', '1': 'i', '1.': 'a', '1:': 'e', "1'": 'á', ':1': 'ü', '2,': 'cs', '2.': 'é',
          '3': 'd', '3,': 'r', '3.': 'v', '4,': 'g', '5': 'h', '5,': 'l', '6,': 'n', '7': 'k', '7,': 's',
          '7.': 'sz', '8': 'm', '8,': 't', '9': 'p', '9,': 'z'}   # as on hcp-1174
NEW = {'1,': 'b', '2': 'c', '4': 'f', '4.': 'gy', '5.': 'ly', '6': 'j', '6.': 'ny', '.1': 'ú'}  # added from this card; 1, and 4 are also reported on hcp-1179, the other six need this card
KEY = {**FAMILY, **NEW}
rows = []
for l in open(os.path.join(D, 'work/transcription.txt'), encoding='utf-8'):
    if l.startswith('#') or not l.strip():
        continue
    tag, body = l.split(':', 1)
    rows.append((tag.strip(), [w.split() for w in body.split('|')]))
EXP = {'L01': 'édes margitkám', 'L02': 'értesitlek hogy szerencsé', 'L03': 'sen leértem az út sokkal',
 'L04': 'jobb volt mint mikor mentem', 'L05': 'csak a falútol a nyúllápáig', 'L06': 'rosz volt de onnat a telepig',
 'L07': 'nagyon jo volt a kövesdi ha', 'L08': 'tárba jobban meg volt fagyva', 'L09': 'a sár de a teleptöl kövesd',
 'L10': 'ig alig birtam bemenni tér', 'L11': 'dig érö ho volt és nagy ho', 'L12': 'fúvássok jo hogy nem vartam',
 'L13': 'kocsi útán mert nem láttam', 'L14': 'hogy jöt volna útánnam talán', 'L15': 'nem is jöt kövesdre kovács imre',
 'L16': 'fél nyolckor értem az üzletbe', 'L17': 'lúbin agyon haragúdott de én egy', 'L18': 'szot sem szoltam',
 'III': 'ha körül ölleled nyakam', 'L20': 'boldogságom határtalan', 'IV': 'olyan vagyok mint a madár',
 'L22': 'ha a párjára rátalál', 'L23': 'csokol hú kedvesed', 'L24': 'árpád',
 'BR1': 'édes margitkám arra kérlek hogy', 'BR2': 'azt a levelet ne kérd vissza töllem'}
n = 0; flagged = 0; cnt = collections.Counter(); got = {}
for tag, words in rows:
    out = []
    for w in words:
        s = ''
        for t in w:
            n += 1
            if t.endswith('~'):
                flagged += 1; t = t[:-1]
            cnt[t] += 1
            s += KEY[t]
        out.append(s)
    got[tag] = ' '.join(out)
    if got[tag] != EXP[tag]:
        sys.exit('MISMATCH %s: %r vs %r' % (tag, got[tag], EXP[tag]))
print('cipher signs: %d, distinct: %d, flagged ~: %d; all decode by the key without exception' % (n, len(cnt), flagged))
print('signs added to the hcp-1174 table:', {k: (NEW[k], cnt[k]) for k in NEW})
print()
g = got
print('[%s]!\n' % g['L01'])
print('[' + ' '.join(g[k] for k in ['L02','L03','L04','L05','L06','L07','L08','L09','L10','L11','L12','L13','L14','L15','L16','L17','L18'])
      .replace('szerencsé sen', 'szerencsésen').replace('ha tárba', 'határba').replace('kövesd ig', 'kövesdig')
      .replace('tér dig', 'térdig').replace('ho fúvássok', 'hofúvássok') + ']\n')
print('III [%s]\n    [%s]' % (g['III'], g['L20']))
print('IV  [%s]\n    [%s]\n' % (g['IV'], g['L22']))
print('Sokszor üdvözöl és [%s] ([%s])\n' % (g['L23'], g['L24']))
print('Bracketed at the foot of the address side: ([%s\n%s] Mezőkövesd. 1916. II/22.)\n' % (g['BR1'], g['BR2']))
print('Normalised reading (accents and spacing supplied, spelling otherwise as written):')
print('''Édes Margitkám! Értesítlek, hogy szerencsésen leértem. Az út sokkal jobb volt, mint mikor mentem,
csak a falutól a Nyúllápáig rosz volt, de onnat a telepig nagyon jó volt. A kövesdi határba jobban
meg volt fagyva a sár, de a teleptől Kövesdig alig bírtam bemenni, térdig érő hó volt és nagy
hófúvássok. Jó hogy nem vártam kocsi után, mert nem láttam hogy jöt volna utánnam, talán nem is
jöt Kövesdre Kovács Imre. Fél nyolckor értem az üzletbe. Lúbin agyon haragudott, de én egy szót
sem szóltam.
III Ha körül ölleled nyakam / boldogságom határtalan.
IV Olyan vagyok, mint a madár, / ha a párjára rátalál.
Sokszor üdvözöl és csókol hű kedvesed (Árpád).
(Édes Margitkám, arra kérlek, hogy azt a levelet ne kérd vissza tőllem. Mezőkövesd. 1916. II/22.)
''')
print('Address (open): Őnagysága / Rózsa reményű / Sziber Margitka kisasszonynak / Szomolya / (Borsod m.) u. p. Bogács')
print('[ ] = enciphered on the card; no accents or word spaces are restored inside the brackets.')
