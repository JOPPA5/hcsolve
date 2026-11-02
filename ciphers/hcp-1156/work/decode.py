#!/usr/bin/env python3
"""hcp-1156: verify scan hashes, decode the digit cipher, print the full plaintext."""
import hashlib, os, sys
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B = 'work/hires/cpc_1915-12-28_HU_Mezokovesd_HU_Szomolya_szomolya-13_'
H = {'source/picture-large.jpg': '9eb9b6c31a35c7a45abe8ca0c094edb336d168b3b0938efe8b748e8353d1e1fc',
     'source/address-large.jpg': 'a18f569b69cc3d43fc34d79bfcfc355f338fd72a9006268c1d20b4b3a839be39',
     B + 'pic.jpg': 'ac905f7c9757f5461306d9727817d3724390904874a9e79ba097eb1f64f07350',
     B + 'adr.jpg': '6b708b89e999ceaa21952b1873e53fc2f6258d827527582f351f3771e5033ecf'}
for p, h in H.items():
    if hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest() != h:
        sys.exit('HASH MISMATCH ' + p)
print('source hashes OK (%d files)' % len(H))
# Key: sign -> letter. Only signs attested on this card.
# 1. stands for a and for unmarked a-with-accent; :1 for u, ue and their long forms; 0 for o and o-acute.
KEY = {'0': 'o', '1': 'i', '1.': 'a', '1:': 'e', "1'": 'á', ':1': 'ü', '1,': 'b',
       '2.': 'é', '3': 'd', '3,': 'r', '3.': 'v', '4': 'f', '4,': 'g', '4.': 'gy',
       '5': 'h', '5,': 'l', '6': 'j', '6,': 'n', '7': 'k', '7,': 's', '7.': 'sz',
       '8': 'm', '8,': 't', '9': 'p', '9,': 'z'}
# Word-by-word ciphertext as read from the hires scan, with the reading.
C = {
 'A': [("7 1: 3 3. 1: 7,", 'Kedves'), ("1 4, 1. 9, 7. 1 3. :1", 'igazszívű'),
       ("8 1. 3, 4, 1 8, 7 1' 8", 'Margitkám')],
 'B': [("1 3, 5 1. 8, 7.", 'irhatsz'), ("1. 7 1. 3, 8 1 8,", 'akármit'),
       ("6, 1:", 'ne'), ("4 2. 5, 6", 'félj'), (":1 4. 7, 1:", 'úgyse')],
 'C': [("8 1: 4,", 'meg'), ("7, 1: 6, 7 1", 'senki'), ("5 1.", 'ha'),
       ("1, 1: 8, :1 3. 1: 5,", 'betüvel'), ("6, 1: 8", 'nem'),
       ("1. 7 7 0 3,", 'akkor'), ("1 3, 6 1. 5,", 'irjál'),
       ("7. 1. 8 0 7 7 1. 5,", 'számokkal'),
       ("1, 1 9, 5 1. 8, 7.", 'bizhatsz'), ("1, 1: 6, 6, 1: 8", 'bennem'),
       ("8, 1: 7, 8, 3. 2. 3,", 'testvér'), ("2. 6,", 'én'),
       (":1 4.", 'úgy'), ("1, 1 9, 0 7", 'bizok'), ("1, 1: 6, 6, 1: 3", 'benned'),
           ("8 1 6, 8,", 'mint'), ("1.", 'a'), ("6 0", 'jó'),
           ("1 7, 8, 1: 6, 7 2. 1, 1: 6,", 'istenkében')],
 'D': [("5 :1", 'hű'), ("7 1: 3 3. 1: 7, 1: 3", 'kedvesed')],
 'E': [("1' 3, 9 1' 3", 'Árpád')],
}
# The writer does not mark long vowels except in Margitkám/Árpád: reduce the reading to the signs.
FOLD = str.maketrans({'ó': 'o', 'í': 'i', 'ú': 'ü', 'ű': 'ü'})
PLAIN_A = {'akármit': 'akarmit', 'irjál': 'irjal', 'számokkal': 'szamokkal'}
def want(w):
    return PLAIN_A.get(w, w).lower().translate(FOLD)
OUT = {}
for k, ws in C.items():
    res = []
    for ct, reading in ws:
        got = ''.join(KEY[t] for t in ct.split())
        if got != want(reading):
            sys.exit('MISMATCH %r -> %r vs %r' % (ct, got, want(reading)))
        res.append(reading)
    OUT[k] = ' '.join(res)
TOK = [t for ws in C.values() for c, _ in ws for t in c.split()]
print('ciphertext signs: %d, distinct %d; all decode by the table (1 is a restoration under the blot: first 7. of számokkal)'
      % (len(TOK), len(set(TOK))))
print()
print('[%s]!\n' % OUT['A'])
print('''Szerencsésen haza érkeztem, nagyon meleg volt és nagy sár. Gyalog jöttem a
telepen lejjebb egy darabig, ott ért utól Nagy Lojzi, egy lovas kocsival jött és
felvett. Úgy értem aztán haza nyolc órakor. Már a lapokat is megvettem, de nem
volt akitől elküldjem. Már az arcképet is berámáztattam, ami othol maradt neked
arckép, annak majd magam fogok faragott rámát csinálni. Más különös ujság nincs.
Róza nem jött el. Majd ha irsz, sokat irjál mindenről. Most már''')
b, c = OUT['B'], OUT['C']
print('[%s] lássa [%s]' % (b, c))
print('Sokszor csókollak, maradok [%s] ([%s])' % (OUT['D'], OUT['E']))
print('Mezőkövesd, 1915. XII/28.\n')
print('Address: Tek. / Rózsareményű / Sziber Margitka / kisasszonynak / Szomolya / u. p. Bogács')
print('Postmark: Mezőkövesd, DEC 28 (year hidden).')
print('[ ] = enciphered on the card (punctuation added by the editor; the ciphertext has none).')
