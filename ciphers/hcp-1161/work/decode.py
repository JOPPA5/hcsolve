#!/usr/bin/env python3
"""hcp-1161: verify scan hashes, decode the digit cipher, print the full plaintext."""
import hashlib, os, sys
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B = 'work/hires/cpc_1915-12-18_HU_Mezokovesd_HU_Szomolya_szomolya-12_'
H = {'source/picture-large.jpg': 'a6234701bf92ccb63cec201e6d07a7e605ec4a9617bbfca61df07627aae50d0b',
     'source/address-large.jpg': '78bdd7fed9b4ce06e5b3c4e32afc5074173c30767c485de49cdedc5347626f13',
     B + 'pic.jpg': 'e5761093ee4b9b1f8653548570860b2811fa4f446ab66943def185c34b854b14',
     B + 'adr.jpg': '8e2b8c4553beb8ca3f398e682f3dccbdf62133c129f8ede6e0fc525b0c855c26'}
for p, h in H.items():
    if hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest() != h:
        sys.exit('HASH MISMATCH ' + p)
print('source hashes OK (%d files)' % len(H))
KEY = {'0': 'o', '0,': 'ö', '1': 'i', '1.': 'a', '1:': 'e', "1'": 'á', '.1': 'u', '-1': 'ú',
       '1,': 'b', '2,': 'cs', '2.': 'é', '3': 'd', '3,': 'r', '3.': 'v', '4,': 'g', '4.': 'gy',
       '5': 'h', '5,': 'l', '6,': 'n', '6.': 'ny', '7': 'k', '7,': 's', '7.': 'sz',
       '8': 'm', '8,': 't', '9,': 'z'}
# Not clean sign-for-sign; each is disclosed in SOLUTION.md. As-seen form ~ value used.
ODD = {'4,~gy': 'gy',  # így: the mark after the 4 is a short tick, read as the dot of 4.
       '4blot': 'gy',  # úgy (2nd): an ink blot covers the mark of the 4; the mark is unreadable
       '3blot': 'v',   # voltam: an ink blot covers the mark of the 3; the mark is unreadable
       '9,~p': 'p'}    # Árpád: the 9 has a clear comma, so the table alone gives z
K = {**KEY, **ODD}
C = [("7 1: 3 3. 1: 7,", 'Kedves'), ("8 1' 3, 4, 1 8, 7 1' 8", 'Márgitkám'),
 ("2. 6,", 'én'), ("1. 7. 8,", 'aszt'), ("7, 1: 8", 'sem'), ("8, .1 3 0 8", 'tudom'), ("5 0 4.", 'hogy'),
 ("8 1 8,", 'mit'), ("1 3, 8, 1. 8", 'írtam'), ("1. 7 7 0 3,", 'akkor'), ("-1 4.", 'úgy'),
 ("1: 5,", 'el'), ("3blot 0 5, 8, 1. 8", 'voltam'), ("7 1' 1, .1 5, 3. 1.", 'kábulva'), ("6, 0", 'no'),
 ("8, 1: 6, 6, 2. 8", 'tenném'), ("2. 3, 8, 1: 3", 'érted'), ("5 1.", 'ha'),
 ("5 1 3 1: 4, 1: 6,", 'hidegen'), ("1: 5, .1 8, 1. 7, 1 8, 1. 6, 1' 5,", 'elutasítanál'),
 ("1: 5, 3. 1 7, 1: 5, 6, 1", 'elviselni'), ("5 1 7.", 'hisz'), ("1 4,~gy", 'így'),
 ("7, 1 6, 2,", 'sincs'), ("7, 1: 6, 7 1", 'senki'), ("5 1' 8,", 'hát'), ("-1 4blot", 'úgy'),
 ("8 1: 4,", 'meg'), ("7 1", 'ki'), ("3. 0 5, 6, 1.", 'volna'), ("5 1.", 'ha'), ("8, 1:", 'te'),
 ("7, 1:", 'se'), ("3. 0 5, 6, 1' 5,", 'volnál'), ("8 1' 3,", 'már'),
 ("8 0 7, 8,", 'most'), ("1 7,", 'is'), ("2. 3 1: 7,", 'édes'), ("1. 6. 1' 8", 'anyám'), ("1 7,", 'is'),
 ("8 1: 4,", 'meg'), ("3, 0 9, 1.", 'Róza'), ("1 7,", 'is'), ("1 3, 8, 1. 7", 'írtak'), ("8 1' 7, 6, 1. 7", 'másnak'),
 ("7. 1' 8 8, 1. 5, 1. 6, 7. 0 3,", 'számtalanszor'), ("0, 5, 1: 5, 5, 1: 7", 'ölellek'),
 ("2. 7,", 'és'), ("2, 0 7 0 5, 5, 1. 7", 'csókollak'), ("1' 3, 9,~p 1' 3", 'Árpád')]
FOLD = str.maketrans({'ó': 'o', 'ő': 'ö', 'í': 'i', 'É': 'é', 'Á': 'á', 'M': 'm', 'K': 'k', 'R': 'r'})
W = []
for ct, reading in C:
    got = ''.join(K[t] for t in ct.split())
    if got != reading.translate(FOLD):
        sys.exit('MISMATCH %r -> %r vs %r' % (ct, got, reading))
    W.append(reading)
n = sum(len(c.split()) for c, _ in C)
odd = sum(t in ODD for c, _ in C for t in c.split())
print('ciphertext signs: %d - %d decode by the table, %d are read by sense (see ODD)\n' % (n, n - odd, odd))
g = lambda a, b: ' '.join(W[a:b])
print('[%s]!\n' % g(0, 2))
print('Lapodat megkaptam melynek nagyon örvendek nem tudom micsoda borzasztóságot írsz,')
print('hogy volt aba a levélbe [%s] de az se-mi én azt bár mikor' % g(2, 15))
print('meg[%s] mer én azt nem tudnám' % g(15, 20))
print('[%s] és én még már két lapot írtam nekik és ma se kapok választ.\n' % g(20, 45))
print('[%s] ([%s])\n' % (g(45, 49), W[49]))
print('Date, open: 1915. XII/18 Mezőkövesd.')
print('Address: Tek. / Szépreményű / Sziber Margitka / kisasszonynak / (Borsod m.) Szomolya / u. p. Bogács.')
print('[ ] = enciphered on the card.')
