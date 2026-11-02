#!/usr/bin/env python3
"""hcp-1175: check scan hashes, decode the digit block, print the card's full text.
Run from anywhere: python3 -I ciphers/hcp-1175/work/decode.py"""
import hashlib, os, sys
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H = {'source/picture-large.jpg': 'c0b0c99ee96d65bc088c2d5cc96299c37ee82c4ebe9b5d56c975965ffa9a1125',
     'source/address-large.jpg': 'e99e3bc4f39e82557231160723e6cbeb2fb73000b29657286fe066dad94ddf28',
     'work/hires/cpc_1915-10-25_HU_Mezokovesd_HU_Szomolya_szomolya-03_pic.jpg': '5eb0ba4581b46ed489009c9cde54db17f3c81183a7bfeb0a5f73ee60e3405629',
     'work/hires/cpc_1915-10-25_HU_Mezokovesd_HU_Szomolya_szomolya-03_adr.jpg': '7725721529e94e6067ff525f81615f142d3e6141f78aae9cc11db71ccf76f5b7'}
for p, h in H.items():
    if hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest() != h:
        sys.exit('HASH MISMATCH ' + p)
print('source hashes OK (%d files)' % len(H))
FAMILY = {'0': 'o', '0,': 'ö', '1': 'i', '1.': 'a', '1:': 'e', '2.': 'é', '3': 'd', '3,': 'r', '3.': 'v',
          '4,': 'g', '5': 'h', '5,': 'l', '6,': 'n', '7': 'k', '7,': 's', '7.': 'sz', '8': 'm', '8,': 't', '9,': 'z'}
NEW = {'.1': 'u', '4.': 'gy', '4': 'f', '1,': 'b'}   # not in the hcp-1174 table; attested on sister cards (hcp-1138, 1165, 1167)
KEY = {**FAMILY, **NEW}
toks = []; lines = []
for l in open(os.path.join(D, 'work/transcription2.txt'), encoding='utf-8'):
    if l.startswith('#'): continue
    t = l.split(); toks += t; lines.append(''.join(KEY[x] for x in t))
s = ''.join(lines)
WANT = ['ha', 'még', 'egyszer', 'elindulok', 'és', 'oda', 'nem', 'érhetek', 'akor', 'az', 'uton', 'főblövöm', 'magam']
if s != ''.join(WANT).replace('ő', 'ö'):
    sys.exit('MISMATCH ' + s)
print('signs: %d; by the hcp-1174 table: %d; by the 4 signs outside that table, attested on sister cards: %d'
      % (len(toks), sum(t in FAMILY for t in toks), sum(t in NEW for t in toks)))
print('raw by line:', ' / '.join(lines))
print('''
[blue-black pen, top corner, probably the writer] 1915. (X.25.)
Kedves Ángyika!
[digits] Ha még egyszer elindulok és oda nem érhetek akor az uton főblövöm magam
(Margitkám!)   [violet]
A szellő is csak azt sugja,
Amely tőlem hozzád téved,
A gerle is csak azt bugja:
Mikor látlak ujra téged?

Távolban a vágyam-
nekem;
Ha te is itt volnál
velem.   [boxed:] Légy szives irjál
mert . . . . . . . . m . . . . .   [8 marks, m, 5 marks as on the card]
Sz. A.

Address: Tek. Szegedi Jánosné urasszonynak / Szomolya / Borsod m. / u. p. (Bogács)''')
