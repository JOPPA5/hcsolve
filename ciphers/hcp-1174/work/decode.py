#!/usr/bin/env python3
"""hcp-1174: verify scan hashes, decode the digit cipher, print the full plaintext."""
import hashlib, os, sys
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H = {'source/picture-large.jpg': '0554e5614263d6982f20e3669ba129100ea814990ff2c211121cf694a656d7d3',
     'source/address-large.jpg': 'fb84ce7cb2210d62f31691fbcc0797a5af38e49523131a85718ebb76b2278ce7',
     'work/hires/cpc_1916-02-15_HU_Mezokovesd_HU_Szomolya_szomolya-18_pic.jpg': '74749779d4ca0625a8908bfb0a411f9df695f68651b98a079a9bb9e5b8d6ca99',
     'work/hires/cpc_1916-02-15_HU_Mezokovesd_HU_Szomolya_szomolya-18_adr.jpg': 'f70ba8442fb6e39db6020a89b30f40eb8411499ab63371a387c14ed2f126010b'}
for p, h in H.items():
    if hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest() != h:
        sys.exit('HASH MISMATCH ' + p)
print('source hashes OK (%d files)' % len(H))
# Key: sign -> letter. Only signs attested on this card.
KEY = {'0': 'o', '0,': 'ö', '1': 'i', '1.': 'a', '1:': 'e', "1'": 'á', ':1': 'ü',
       '2,': 'cs', '2.': 'é', '3': 'd', '3,': 'r', '3.': 'v', '4,': 'g',
       '5': 'h', '5,': 'l', '6,': 'n', '7': 'k', '7,': 's', '7.': 'sz',
       '8': 'm', '8,': 't', '9': 'p', '9,': 'z'}
# Readings that are not clean sign-for-sign; each is disclosed in SOLUTION.md.
ODD = {'1~a': 'á',   # sz-A-mtalan: a plain 1 on the card, no high dot seen
       '9~o': 'ö',   # üdv-Ö-z-Ö-llek: 9-shaped, taken as a joined 0, (third has a dot above)
       '7~sz': 'sz', # SZ-erető: no separate dot visible under the crossed 7
       '3~r': 'r'}   # sze-R-ető: body blotted, comma clear
K = {**KEY, **ODD}
# (word-by-word ciphertext as read, reading with accents)
C = {
 'T': [("2. 3 1: 7,", 'Édes'), ("8 1. 3, 4, 1 8, 7 1' 8", 'Margitkám')],
 'B': [("0, 5, 1: 5, 5 1: 8, 5, 1: 7", 'ölelhetlek'), ("2. 6,", 'én')],
 'C': [("7. 1 3. 1: 8", 'szívem'), ("2. 5, 1: 3", 'éled')],
 'D': [("7. 1: 3, 1: 8, 1: 8", 'szeretem')],
 'E': [("7. 1~a 8 8, 1. 5, 1. 6, 7. 0 3,", 'számtalanszor'),
       (":1 3 3. 9~o 9, 9~o 5, 5, 1: 7", 'üdvözöllek')],
 'F': [("2, 0 7 0 5, 5, 1. 7", 'csókollak')],
 'G': [("7~sz 1: 3~r 1: 8, 0,", 'szerető'), ("7 1: 3 3. 1: 7, 1: 3", 'kedvesed')],
 'H': [("1' 3, 9 1' 3", 'Árpád')],
}
FOLD = str.maketrans({'ó': 'o', 'ő': 'ö', 'í': 'i', 'É': 'é', 'Á': 'á', 'M': 'm'})
OUT = {}
for k, ws in C.items():
    res = []
    for ct, reading in ws:
        got = ''.join(K[t] for t in ct.split())
        if got != reading.translate(FOLD):
            sys.exit('MISMATCH %r -> %r vs %r' % (ct, got, reading))
        res.append(reading)
    OUT[k] = ' '.join(res)
TOK = [t for ws in C.values() for c, _ in ws for t in c.split()]
n_odd = sum(t in ODD for t in TOK)
print('ciphertext signs: %d - %d decode by the table, %d are read by sense (see ODD)'
      % (len(TOK), len(TOK) - n_odd, n_odd))
print()
print('Mezőkövesd, 916. II/15.\n')
print('[%s]!\n' % OUT['T'])
print('''Bocsáss meg, hogy ígéretemet nem teljesítettem, vagyis nem mehettem fel, de
semmi tekintetben sem tehettem. A jövő vasárnapi bátran felmegyek, az idő nem
diferál, hogy milyen lesz az mindegy, és majd pótolni fogom a multat is.
''')
print('II Ha [%s], téged,\nArcom derül, [%s].\n' % (OUT['B'], OUT['C']))
print('''Lágy tavaszodal [vagi oltál ?]
Halkan keblemet
Messzi csendülj röpke kis dal
Át a tér felett.

II Csengj ki váltig ama házig
Hol virág terem
És ha ott egy rózsa látszik
Mondd, hogy [%s]
''' % OUT['D'])
print('[%s] és [%s] ([%s]) [%s]\n' % (OUT['E'], OUT['F'], OUT['G'], OUT['H']))
print('Address: Őnsg. / Szépreményű Sziber Margitka kisasszonynak / Szomolya / u. p. Bogács.')
print('Postmark: Mezőkövesd, FEB 15, year damaged, fits 916.')
print('[ ] = enciphered on the card. [vagi oltál ?] = letters as seen, unresolved open text.')
