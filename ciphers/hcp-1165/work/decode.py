#!/usr/bin/env python3
"""hcp-1165: verify scan hashes, decode the digit cipher, print the full plaintext.
Run from the repo root: python3 -I ciphers/hcp-1165/work/decode.py"""
import hashlib, os, sys
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H = {'source/picture-large.jpg': '9a62c716807227edba9b14f1e9c667a97ee1d5af991d92dca522aa9f26643082',
     'source/address-large.jpg': '486e8e69b47e9adae58784b96f544390cc4c6a779c132cbbfaf73321279009f1',
     'work/hires/cpc_1915--_HU_Mezokovesd_HU_Szomolya_szomolya-42_pic.jpg': '5fc26a54f378bad969724dfc7d20118d706a4feb3c95437398adad07da944dbf',
     'work/hires/cpc_1915--_HU_Mezokovesd_HU_Szomolya_szomolya-42_adr.jpg': '4e887b56fd29d4530ffd950f7decbe852afd5d15c634206e12c35cd1695f6e11'}
for p, h in H.items():
    if hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest() != h:
        sys.exit('HASH MISMATCH ' + p)
print('source hashes OK (%d files)' % len(H))
# Key: only signs attested on this card.
KEY = {'0': 'o', '0,': 'ö', '1': 'i', '1,': 'b', '1.': 'a', '1:': 'e', "1'": 'á', '.1': 'u', ':1': 'ü',
       '2,': 'cs', '2.': 'é', '3': 'd', '3,': 'r', '3.': 'v', '4': 'f', '4,': 'g', '4.': 'gy',
       '5': 'h', '5,': 'l', '6': 'j', '6,': 'n', '6.': 'ny', '7': 'k', '7,': 's', '7.': 'sz',
       '8': 'm', '8,': 't', '9': 'p', '9,': 'z'}
# Signs that are not clean by the table; each is disclosed in SOLUTION.md.
ODD = {'1~a': 'a',   # article a, three times: plain 1 with no dot on the card
       '5~l': 'l',   # lassan: plain 5, no comma visible (table h)
       '8~t': 't',   # üzlet (hook in place of comma)
       '9~z': 'z',   # üzlet: plain 9, no comma (table p)
       '1~b': 'b',   # bűbájtól: comma displaced to the right, may be part of the line below
       'G~g': 'g'}   # igaz: looks like a written g, not the 4, of this card
K = {**KEY, **ODD}
# Each entry: signs, reading in normal spelling, optional literal letters where unmarked
# accents differ (the writer often leaves ó, á, ú unmarked).
T = {
 'head': [("2. 3 1: 7,", 'Édes'), ("8 1. 3, 4, 1 8, 7 1' 8", 'Margitkám')],
 'body': [("2. 3, 8, 1: 7, 1 8, 5, 1: 7", 'értesítlek'), ("5 0 4.", 'hogy'),
  ("7. 1: 3, 1: 6, 2, 2. 7, 1: 6,", 'szerencsésen'), ("5 1. 9, 1. 2. 3, 8, 1: 8", 'hazaértem'),
  ("6, 1. 4. 0 6,", 'nagyon'), ("6 0", 'jó'), ("1 3 0,", 'idő'), ("3. 0 5, 8,", 'volt'),
  ("7. 1 6, 8, 1:", 'szinte'), ("9 1. 7, 7. 1 0", 'passzió'), ("3. 0 5, 8,", 'volt'),
  ("6 0, 6, 6, 1", 'jönni'), ("5 2. 8, 0 3, 1' 3, 1.", 'hét órára'), ("2. 3, 8, 1: 8", 'értem'),
  ("1~a 3. 1' 3, 0 7, 1, 1.", 'a városba'), ("8 1: 3, 8,", 'mert'),
  ("5~l 1. 7, 7, 1. 6,", 'lassan'), ("6 0, 8, 8, 1: 8", 'jöttem'),
  ("1~a 7. 1. 5, 0 7 1", 'a szalóki'), ("4 1 .1", 'fiú'), ("1 7,", 'is'),
  (".1 8, 0 5, 2. 3, 8,", 'utolért'), ("1~a 7. 0, 5, 5, 0, 7", 'a szőllők'), ("7 0, 9, 8,", 'közt'),
  ("8 1 3, 1:", 'mire'), ("1. 9,", 'az'), (":1 9~z 5, 1: 8~t 5 1. 9,", 'üzletház', 'üzlethaz'),
  ("2. 3, 8, :1 6, 7", 'értünk'), ("8 1' 3,", 'már'), ("6. 1 8, 3. 1.", 'nyitva'),
  ("3. 0 5, 8,", 'volt'), ("3 1:", 'de'), ("6, 1: 8", 'nem'), ("7. 0 5, 8,", 'szólt'),
  ("7, 1: 8 1 8,", 'semit'), ("1. 9,", 'az'), ("0, 3, 1: 4,", 'öreg'), ("5, .1 1, 1", 'Lubi')],
 'p1': [("1~b :1 1, 1' 6 8, 0 5,", 'bűbájtól'), ("3. 0 6, 9, 3. 1.", 'vonzva')],
 'p2': [("7 1: 9, 1: 3 1: 8,", 'kezedet')],
 'p3': [("7. 1 3. 1, 1: 6,", 'szívben'), ("7. 1: 3, 1: 5, 1: 8", 'szerelem')],
 'e1': [("7, 0 7 7. 0 3,", 'sokszor'), ("2, 0 7 0 5, 3. 1.", 'csókolva')],
 'e2': [("5 :1", 'hű'), ("1 8 1' 3 0 3", 'imádód')],
 'e3': [("1 G~g 1. 9,", 'igaz')],
 'e4': [("1 3.", 'ív')],                 # sz[ív]ű: sz and ű are in clear letters
 'e5': [("7 1: 3 3. 1: 7, 1: 3", 'kedvesed')],
 'e6': [("1' 3, 9 1' 3", 'Árpád')],
}
FOLD = str.maketrans({'ó': 'o', 'ő': 'ö', 'í': 'i', 'ú': 'u', 'ű': 'ü',
                      'É': 'é', 'Á': 'á', 'M': 'm', 'L': 'l', ' ': None})
OUT = {}; tok = []
for k, ws in T.items():
    res = []
    for w in ws:
        ct, reading = w[0], w[1]
        lit = w[2] if len(w) > 2 else reading
        got = ''.join(K[t] for t in ct.split())
        if got.translate(FOLD) != lit.translate(FOLD):
            sys.exit('MISMATCH %r -> %r vs %r' % (ct, got, lit))
        tok += ct.split(); res.append(reading)
    OUT[k] = ' '.join(res)
n = sum(t in ODD for t in tok)
print('ciphertext signs: %d - %d decode by the table, %d are read by sense (see ODD)\n'
      % (len(tok), len(tok) - n, n))
print('[%s]!\n\n[%s]' % (OUT['head'], OUT['body']))
print('Más különös ujság nincs.\n')
print('''Kicsiny kezed körül csapongva
Egy tarka pille röppen,
Mintegy [%s] vonva
Mind szűkebb körökben
Míg végül össze vonva szárnyait
Pihenni száll a kézre
Fehér [%s], a parányit
Ő liliomnak nézte.

Ha a szőlő nedvtül árad,
A fecske is ott terem,
Mikor a szem könnybe lábad
Héba [%s].
''' % (OUT['p1'], OUT['p2'], OUT['p3']))
print('Üdvözölve és [%s] maradok [%s] és [%s] sz[%s]ű [%s] ([%s])'
      % (OUT['e1'], OUT['e2'], OUT['e3'], OUT['e4'], OUT['e5'], OUT['e6']))
print('csókolom angyikát és Mariskát is\n')
print('Address: Őnsg. / Szépreményű Sziber Margitka kisasszonynak / Szomolya / u. p. (Borsod megye) / u. p. Bogács')
print('[ ] = enciphered on the card; the rest is in clear.')
