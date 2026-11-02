#!/usr/bin/env python3
"""hcp-1139: verify scan hashes, decode work/transcription.txt, print the full plaintext."""
import hashlib, os, sys
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H = {'source/picture-large.jpg': '30ca16cf43faa662ce7689e18a17c2818668f6e61dc0a95c49752d88b1a7c011',
     'source/address-large.jpg': '532ee4151fbfc2a1d30bca970a53f33832a7e9789cd88d04bad53d5d1f2daea1',
     'work/hires/cpc_1916-01-06_HU_Mezokovesd_HU_Szomolya_szomolya-15_pic.jpg': '1b9d990fdb5e44a76148da376ee2bc0a46683da3a3b59709fc661a309ade27ee',
     'work/hires/cpc_1916-01-06_HU_Mezokovesd_HU_Szomolya_szomolya-15_adr.jpg': 'f4a344193e49d64389a6e221c25df4c9d00b4889c7a1522c7fd890f87f1c15d6'}
for p, h in H.items():
    if hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest() != h:
        sys.exit('HASH MISMATCH ' + p)
print('source hashes OK (%d files)' % len(H))
KEY = {'0': 'o', '0,': 'ö', '1': 'i', '1.': 'a', '1:': 'e', "1'": 'á', '1,': 'b',
       '.1': 'u', ':1': 'ü', '2': 'c', '2,': 'cs', '2.': 'é', '3': 'd', '3,': 'r', '3.': 'v',
       '4,': 'g', '4.': 'gy', '5': 'h', '5,': 'l', '6': 'j', '6,': 'n', '6.': 'ny',
       '7': 'k', '7,': 's', '7.': 'sz', '8': 'm', '8,': 't', '9': 'p', '9,': 'z'}
# Not clean sign-for-sign; disclosed in SOLUTION.md.
ODD = {'7~sz': 'sz',  # ink blot under the 7 in the first rosszul: dot or comma not separable
       '8~t': 't'}  # plain 8, no comma: the key gives méged, rhyme and sense need téged
K = {**KEY, **ODD}
# Expected reading per card line (accents as a reader would write them, folded for the check).
EXP = '''Kedves Margitkám
Hogy múlt el az új év ne
ked jól e vagy rosszul
mert nekem nagyon rosszul
egyrészt mer nem veled tölt
hettem az tán meg máskép
is egy kicsit beütöt a krak
aranyos babuskám
szeressél igazán
boldog csak úgy lehetsz
hogy ha engem szeretsz
üdvözletem küldöm
édesem tenéked
úgy szeressél engem
mint ahogy én téged
nem kérek istentől
kincset gazdagságot
csak téged tubicám
s hozzád boldogságot
sokszor csókolva és üdvözöl
ve téged maradok hű kedvesed
Árpád'''.split('\n')
FOLD = str.maketrans({'ó': 'o', 'ő': 'ö', 'í': 'i', 'ú': 'u', 'ű': 'u', 'Á': 'á', 'K': 'k', 'M': 'm', 'H': 'h'})
rows = [l.strip() for l in open(os.path.join(D, 'work/transcription.txt'), encoding='utf-8')
        if l.strip() and not l.startswith('#')]
if len(rows) != len(EXP):
    sys.exit('line count %d vs %d' % (len(rows), len(EXP)))
tok = []
for r, e in zip(rows, EXP):
    words = [''.join(K[t] for t in w.split()) for w in r.split('|')]
    tok += r.replace('|', ' ').split()
    if words != e.translate(FOLD).split():
        sys.exit('MISMATCH %r vs %r' % (words, e))
n = sum(t in ODD for t in tok)
print('cipher signs: %d, distinct: %d; %d decode by the table, %d rest on sense (ODD)\n'
      % (len(tok), len(set(tok)), len(tok) - n, n))
print('Decoded by card line:')
for e in EXP:
    print('  ' + e)
print('''
Reading text:

(open, written up the margin) Mezőkövesd 1916 I/6

Kedves Margitkám!
Hogy múlt el az új év neked, jól-e vagy rosszul? Mert nekem nagyon rosszul,
egyrészt mer nem veled tölthettem, az tán meg máskép is egy kicsit beütöt a krak.
Aranyos babuskám, szeressél igazán.

Boldog csak úgy lehetsz,
hogy ha engem szeretsz.

Üdvözletem küldöm, édesem, tenéked,
úgy szeressél engem, mint ahogy én téged.
Nem kérek Istentől kincset, gazdagságot,
csak téged, tubicám, s hozzád boldogságot.

Sokszor csókolva és üdvözölve téged maradok hű kedvesed
Árpád

Address (open): Őnagysága / Sziber Margitka / ur-leánynak / Szomolya / u. p. Bogács''')
