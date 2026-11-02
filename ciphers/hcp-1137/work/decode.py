#!/usr/bin/env python3
"""hcp-1137: verify scan hashes, decode the digit cipher, print the full plaintext."""
import hashlib, os, sys
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B = 'work/hires/cpc_1916-06-10_HU_Mezokovesd_HU_Szomolya_szomolya-39_'
H = {'source/picture-large.jpg': '6fe36ffe1e4c2abf97916ccf6c23448433a80640d56c94290a716d17452997a9',
     'source/address-large.jpg': '19a8343d6880ca5e20f8da16f84c4de32e15f81be40b8d37e0612dac8da976cc',
     B + 'pic.jpg': '7615e784068fa735e5745d8eb77b965f88d9035596d42e3cf4c1c58fa5fa871b',
     B + 'adr.jpg': '88fb79ef4a7672ce6d17aef81163c6cd953eddd57f7e675c6d8f62e1fd5c04b3'}
for p, h in H.items():
    if hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest() != h:
        sys.exit('HASH MISMATCH ' + p)
print('source hashes OK (%d files)' % len(H))
# Key: sign -> letter, only signs attested on this card.
# `1'` = 1 with a high dot; `.1` and `:1` = dots LEFT of the stem.
KEY = {'0': 'o', '0,': 'ö', '1': 'i', '1.': 'a', '1:': 'e', "1'": 'á', '1,': 'b',
       '.1': 'u', ':1': 'ü', '2,': 'cs', '2.': 'é', '3': 'd', '3,': 'r', '3.': 'v',
       '4': 'f', '4,': 'g', '4.': 'gy', '5': 'h', '5,': 'l', '6': 'j', '6,': 'n',
       '6.': 'ny', '7': 'k', '7,': 's', '7.': 'sz', '8': 'm', '8,': 't', '9': 'p',
       '9,': 'z', '9.': 'zs'}
# Words where the signs as written do not give the reading (see SOLUTION.md): reading -> table output.
SENSE = {'rózsaszál': 'rózsiszál',          # plain 1, no dot (the same word has 1. in rózsaszálam)
         'csókolom': 'csókohom',            # 5 with no comma
         'lányka': 'hányka',                # 5 with no comma
         'Számtalanszor': 'szátalanszor'}   # m omitted; `8,` = t is an ordinary sign
K = KEY
# Text of the card, sign by sign, exactly as written. Each entry: (signs, reading).
# Words are kept whole, so a word split at a line end (Tere-nyén, találkoz-tam, Szent-kúthoz)
# stands in the entry where it starts, not on its physical line.
ROWS = [
 [("2. 3 1: 7,", 'Édes'), ("8 1. 3, 4, 1 8, 7 1' 8", 'Margitkám')],
 [("7, 1 8, 5, 1: 7", '-sítlek'), ("5 0 4.", 'hogy'), ("8 1' 3,", 'már'),
  ("1 8, 8,", 'itt'), ("3. 1. 4. 0 7", 'vagyok'), ("8, 1: 3, 1: 6. 2. 6,", 'Terenyén')],
 [("8 2. 4,", 'még'), ("3, 0 9, 1' 3. 1. 5,", 'Rózával'), ("6, 1: 8", 'nem'),
  ("8, 1. 5, 1' 5, 7 0 9, 8, 1. 8", 'találkoztam')],
 [("5, 1: 5 1: 8,", 'lehet'), ("5 0 4.", 'hogy'), ("1: 5, 8 1: 4. 1: 7", 'elmegyek'),
  ("1.", 'a'), ("7. 1: 6, 8,", 'Szent-')],
 [("7 .1 8, 5 0 9,", 'kúthoz'), ("1 7,", 'is'), ("1: 4. 1: 1,", 'egyeb'),
  (".1 6 7, 1' 4, 0 8,", 'újságot'), ("6, 1: 8", 'nem'), ("8, .1 3 0 7", 'tudok')],
 [("1 3, 6, 1", 'írni'), ("7. 1: 3, 3. .1 7.", 'szervusz')],
 [("1: 5, 5 1: 3, 3. 1. 3", 'Elhervad'), ("1.", 'a'),
  ("3, 0 9. 1 7. 1' 5,", 'rózsaszál'), ("1 7,", 'is')],
 [("5 1.", 'Ha'), ("8 1: 4, 2, 1 9 8, 1:", 'megcsípte'), ("8 1' 3,", 'már'),
  ("1.", 'a'), ("3 2. 3,", 'dér')],
 [("1: 5, 5 1: 3, 3. 1. 3", 'Elhervad'), ("1.", 'a'), ("5, 1: 1' 6.", 'leány'),
  ("1 7,", 'is'), ("5 0 4. 5 1.", 'hogyha')],
 [("6, 1: 8", 'Nem'), ("4 0 3,", 'for[r]'), ("1, 1: 6, 6, 1:", 'benne'), ("8 1' 3,", 'már'),
  ("1.", 'a'), ("3. 2. 3,", 'vér')],
 [(":1 3 1:", 'Üde'), ("1. 9,", 'az'), ("2. 6,", 'én'),
  ("3, 0 9. 1. 7. 1' 5, 1. 8", 'rózsaszálam')],
 [("8 1: 5, 1: 4,", 'Meleg'), ("1' 4. 1, 1. 6,", 'ágyban'), ("1' 9 0 5, 0 8", 'ápolom')],
 [("4 0 3, 3,", 'Forr'), ("1.", 'a'), ("3. 2. 3, 1:", 'vére'), ("1.", 'a'),
  ("1, 1. 1, 1' 8 6, 1. 7", 'babámnak')],
 [("8 1: 3, 8,", 'Mert'), ("5 1 7.", 'hisz'), ("4. 1. 7 3, 1. 6,", 'gyakran'),
  ("2, 0 7 0 5 0 8", 'csókolom')],
 [("1. 9, 2. 3, 8,", 'Azért'), ("5 0 4.", 'hogy'), ("1: 5, 6 0, 8, 8, 1: 8", 'eljöttem')],
 [("7. 1: 3, 1: 7, 7,", 'szeress'), ("2, 1. 7", 'csak'), ("8, 0 3. 1' 1, 1, 3, 1.", 'továbbra')],
 [("8 1: 3, 8,", 'Mert'), ("8 2. 4,", 'még'), ("3. 1 7, 7. 1. 8, 2. 3, 1: 7", 'visszatérek')],
 [("1 7, 8 2. 8,", 'ismét'), ("5 0 9, 9, 1' 3", 'hozzád'), ("5 1' 6. 7 1.", 'lányka')],
 [("7. 1' 8, 1. 5, 1. 6, 7. 0 3,", 'Számtalanszor'), ("0, 5, 1: 5,", 'ölel'), ("2. 7,", 'és'),
  ("2, 0 7 0 5,", 'csókol')],
 [("1.", 'a'), ("8, 1' 3. 0 5, 1, 0 5,", 'távolból')],
 [("5 :1", 'hű'), ("1 8 1' 3 0 3", 'imádód'), ("1' 3, 9 1' 3", 'Árpád')],
]
FOLD = str.maketrans({'ó': 'o', 'ő': 'ö', 'í': 'i', 'ú': 'u', 'ű': 'ü', 'É': 'é', 'Á': 'á', '-': None, '[': None})
O = []
for row in ROWS:
    w = []
    for ct, reading in row:
        got = ''.join(K[t] for t in ct.split())
        want = SENSE.get(reading, reading).replace('[r]', '').lower().translate(FOLD)
        if got != want:
            sys.exit('MISMATCH %r -> %r vs %r' % (ct, got, reading))
        w.append(reading)
    O.append(' '.join(w))
TOK = [t for r in ROWS for c, _ in r for t in c.split()]
assert set(TOK) == set(KEY), set(KEY) ^ set(TOK)
print('ciphertext signs: %d, %d distinct, all in the key' % (len(TOK), len(set(TOK))))
print('Corrected by sense: 3 signs lacking their mark, 1 omitted letter (m). Table output of those words: %s\n'
      % ', '.join(SENSE.values()))
print('Kis Terenne, 1916 VI 10   (open)\n')
print('[%s]!\n' % O[0])
print('Érte[%s,' % O[1].replace('-sítlek', 'sítlek'))
print('%s,' % O[2])
print('%s' % O[3])
print('%s' % O[4].replace('kúthoz is', 'kúthoz is,'))
print('%s]\n' % O[5].replace('írni', 'írni,'))
for i in (6, 7, 8, 9):
    print('[%s]' % O[i])
print()
for i in (10, 11, 12, 13):
    print('[%s]' % O[i])
print()
for i in (14, 15, 16, 17):
    print('[%s]' % O[i])
print()
print('[%s] [%s] [%s]' % (O[18], O[19], O[20].replace('imádód', 'imádód,')))
print('\nAddress (open): Őnagysága. / Sziber Margitka Kisasszonynak / Szomolya / (Borsod m.) u. p. Bogács.')
print('Postmark: KISTERENYE, 1916, JUN 10 as far as legible.')
print('[ ] = enciphered on the card. Word division and commas partly editorial.')
