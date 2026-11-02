#!/usr/bin/env python3
"""hcp-1140: verify scan hashes, decode the digit cipher, print the full plaintext."""
import hashlib, os, sys
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B = 'cpc_1915-12-10_HU_Mezokovesd_HU_Szomolya_szomolya-10'
H = {'source/picture-large.jpg': 'd38f8409a009991b0b78272530d08dceba56e8f5cfe95f466cf4a8676245d08d',
     'source/address-large.jpg': '43ef300540d4b6d345f5ab816dd7e0c92a74fd326bb0848a8be61f125963b723',
     'work/hires/%s_pic.jpg' % B: '25831d6ad3e813ee5bacad8a15e15943e89a72e880a94a39e206624a416182f9',
     'work/hires/%s_adr.jpg' % B: '1ee19c5dc464035497080c56c58ece514888de1ed9e22eeb8a6305099a5345dc'}
for p, h in H.items():
    if hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest() != h:
        sys.exit('HASH MISMATCH ' + p)
print('source hashes OK (%d files)' % len(H))
KEY = {'0': 'o', '1': 'i', '1.': 'a', '1:': 'e', "1'": 'á', '.1': 'u', '1,': 'b',
       '2.': 'é', '3': 'd', '3,': 'r', '3.': 'v', '4,': 'g', '4.': 'gy',
       '5': 'h', '5,': 'l', '6': 'j', '6,': 'n', '7': 'k', '7,': 's', '7.': 'sz',
       '8': 'm', '8,': 't'}
# A crossed 7 with no dot, read as 7. = sz by word sense; the table alone gives k.
ODD = {'7~sz': 'sz'}
K = {**KEY, **ODD}
# Ciphertext as read, word by word: (signs, reading with accents as normally written).
TOP = [("7 1: 3 3. 1: 7,", 'Kedves'), ("8 1. 3, 4, 1 8, 7 1' 8", 'Margitkám')]
BODY = [("7 1: 3 3, 1: 7,", 'Kedres'), ("8 1. 3, 4, 1 8, 7 1' 8", 'Margitkám'),
        ("8 1' 3,", 'már'), (".1 4.", 'úgy'), ("5, 1' 8, 7. 1 7", 'látszik'),
        ("5 0 4.", 'hogy'), ("5 1 1' 1, 1.", 'hiába'), ("7 2. 3, 5, 1: 7", 'kérlek'),
        ("5 0 4.", 'hogy'), ("1 3, 6 1' 5,", 'írjál'),
        ("8 1' 3,", 'már'), ("6, 1: 8", 'nem'), ("1 3, 7.", 'írsz'), ("6, 0", 'no'),
        ("2. 6,", 'én'), ("1 3, 0 7", 'írok'), ("8 1 4,", 'míg'), ("2. 5, 1: 7", 'élek'),
        ("5 1 7~sz", 'hisz'), ("1: 7~sz 8,", 'eszt'), (".1 4. 7, 1: 8", 'úgysem'),
        ("7, 0 7 1' 1 4,", 'sokáig'), ("1, 1 3, 0 8", 'bírom'),
        ("1: 5, 3. 1 7, 1: 5, 6, 1", 'elviselni')]
LAST = [("7. 1: 3, 1: 8, 6, 1", 'szeretni')]
FOLD = str.maketrans({'ó': 'o', 'ő': 'ö', 'í': 'i', 'ú': 'u', 'K': 'k', 'M': 'm'})
def dec(ws):
    res = []
    for ct, reading in ws:
        got = ''.join(K[t] for t in ct.split())
        if got != reading.translate(FOLD):
            sys.exit('MISMATCH %r -> %r vs %r' % (ct, got, reading))
        res.append(reading)
    return res
t, b, l = dec(TOP), dec(BODY), dec(LAST)
TOK = [x for ws in (TOP, BODY, LAST) for c, _ in ws for x in c.split()]
odd = sum(x in ODD for x in TOK)
# 7~sz is a working label for a plain 7 on the card, so it is not a sign of its own.
distinct = len({'7' if x in ODD else x for x in TOK})
print('ciphertext signs: %d, distinct %d; %d decode by the table, %d read by sense (dotless 7)'
      % (len(TOK), distinct, len(TOK) - odd, odd))
print('table-only form of the sense words: hik ekt')
w = ' '.join
# The open greeting breaks as `üdv-` / `vözöllek` on the card (v written twice); normal form printed.
print('''
[%s]!
A legtisztább szívből üdvözöllek mindnyájatokat

[%s! %s. %s, %s, %s.]

Féld az Istent, szeresd a dalt,
Növelj virágokat!
Isten emel, dal vigasztal,
Virág illatot ad!

Hiába, hiába
Nem tudlak feledni...
Csak tégedet foglak
Örökké keresni,
Igazán [%s]!    Sz. A.

Számtalanszor csókollak maradtam) Mezőkövesd, 1915. XII/10

Address: Tek. Szépreménnyü Sziber Margitka kisasszonynak, Szomolya, u. p. Bogács.
[ ] = enciphered on the card; punctuation inside [ ] is editorial.'''
 % (w(t), w(b[:2]), w(b[2:10]), w(b[10:13]), w(b[13:18]), w(b[18:]), l[0]))
