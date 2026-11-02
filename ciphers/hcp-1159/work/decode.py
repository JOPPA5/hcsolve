#!/usr/bin/env python3
"""hcp-1159: verify scan hashes, decode the digit cipher, print the full text of the card."""
import hashlib, os, sys
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H = {'source/picture-large.jpg': '3cf630f12ae1fdca6c01499b1a01c1ed27dcc9840086c5cc7fc7bb85f6a81247',
     'source/address-large.jpg': 'b201e26902389022f32c90794a1318bf9217756b6140a83d426d477d2c97a1cf',
     'work/hires/cpc_1915-11-_HU_Mezokovesd_HU_Szomolya_szomolya-45_pic.jpg': '4b19e916f5116f0cbfc177a1ce7574ab9837ad829893bcb98aec24ec33070566',
     'work/hires/cpc_1915-11-_HU_Mezokovesd_HU_Szomolya_szomolya-45_adr.jpg': '0ac74b9ed9c07edc9cc15f5fe71422d7f64ed48dcf25ead458d2f2ef14b353c6'}
for p, h in H.items():
    if hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest() != h:
        sys.exit('HASH MISMATCH ' + p)
print('source hashes OK (%d files)' % len(H))
# Key: family key of hcp-1174 / 1163 / 1164; only signs attested on this card.
KEY = {'0': 'o', '0,': 'ö', '1': 'i', '1.': 'a', '1:': 'e', "1'": 'á', '1,': 'b',
       '2.': 'é', '3': 'd', '3,': 'r', '3.': 'v', '4,': 'g', '4.': 'gy',
       '5': 'h', '5,': 'l', '6,': 'n', '7': 'k', '7,': 's', '7.': 'sz',
       '8': 'm', '8,': 't', '9': 'p', '9,': 'z'}
# X = the blotted sign after "itt": a smeared body with a clear comma; nothing is decoded from it.
# Signs in card order, grouped here by verse line (the card wraps differently: lapot and -lem stand on their own rows); | marks my word division, none on the card.
ROWS = [
 "2. 3 1: 7, | 8 1. 3, 4, 1 8, 7 1' 8",
 "3. 1: 3 3 | 8, 0, 5, 1: 8 | 1: | 7 2. 9 1: 7, | 5, 1. 9 0 8,",
 "7, | 3. 2. 5, 1: | 8, 1 7. 8, 1. | 7. 1 3. 1: 8 1: 8,",
 "2. 3, 8, 1: 3 | 5, 1' 4, 0 5, | 2. 3, 8, 1: 3 | 2. 4, | 1. 9,",
 "8 1 4, | 1. | 7, 1 3, | 1: 5, | 6, 1: 8 | 8, 1: 8 1: 8,",
 "8, 1' 3. 0 5, 1, 1. 6, | 1. | 3. 1' 4. 1. 8 | 6, 1: 7 1: 8",
 "5 1. | 8, 1: | 1 7, | 1 8, 8, X | 3. 0 5, 6, 1' 5, | 3. 1: 5, 1: 8",
]
WANT = [
 "Édes Margitkám",
 "Vedd tőlem e képes lapot",
 "s véle tiszta szívemet",
 "érted lágol érted ég az",
 "míg a sír el nem temet",
 "távolban a vágyam nekem",
 "ha te is itt volnál velem",
]
FOLD = str.maketrans({'ó': 'o', 'ő': 'ö', 'í': 'i', 'É': 'é', 'M': 'm', 'V': 'v'})
n = 0
for row, want in zip(ROWS, WANT):
    words = []
    for w in row.split('|'):
        toks = [t for t in w.split() if t != 'X']
        n += len(toks)
        words.append(''.join(KEY[t] for t in toks))
    got = ' '.join(words)
    if got != want.translate(FOLD):
        sys.exit('MISMATCH %r vs %r' % (got, want))
print('cipher signs decoded by the table: %d (distinct %d); 1 blotted sign X not decoded\n'
      % (n, len({t for r in ROWS for t in r.split() if t not in '|X'})))
print('[%s]\n' % WANT[0])
print('Kérlek írd meg, hogy megkaptad-e a levelet, mert küldtem benne a számbetűket is.\n')
print('[Vedd tőlem e képes lapot]\n[s véle tiszta szívemet]\n[érted lá(n)gol, érted ég az,]')
print('[míg a sír el nem temet.]\n[Távolban a vágyam nekem,]\n[ha te is itt volnál velem.]\n')
print('Mindnyájatokat csókollak. Sz. Á.\nÍrjál.\n')
print('Address: Tek. / Rózsareményű Sziber Margitka kisasszonynak / Szomolya / u. p. Bogács / Borsod m.')
print('[ ] = enciphered on the card; (n) = not written on the card, spelling as written is lágol.')
