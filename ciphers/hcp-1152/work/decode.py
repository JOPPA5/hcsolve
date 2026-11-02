#!/usr/bin/env python3
"""hcp-1152: verify scan hashes, decode the digit cipher, print the full plaintext."""
import hashlib, os, sys
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H = {'source/picture-large.jpg': '5e326508a6077c7721ac9e8a3c9a11dc3d0180ef7be99e3ec6b08e0d56edf8cd',
     'source/address-large.jpg': 'c123e4fbe8921b4335fe0d6bcde2e65eb499fd7e1f00f358543f541f498342d4',
     'work/hires/cpc_1915-12-05_HU_Mezokovesd_HU_Szomolya_szomolya-09_pic.jpg': '5f229be0a6a7e941f8390416fa4f06be333b6a24f45094f0c3f5f7c5c7b028cf',
     'work/hires/cpc_1915-12-05_HU_Mezokovesd_HU_Szomolya_szomolya-09_adr.jpg': '20a36eb24c95850756825dfc079e9705d19455c1dd39a2efbca02b56bbccca34'}
for p, h in H.items():
    if hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest() != h:
        sys.exit('HASH MISMATCH ' + p)
print('source hashes OK (%d files)' % len(H))
# Family key (hcp-1174, 1165, 1168, 1170): only signs attested on this card.
KEY = {'0': 'o', '1': 'i', '1.': 'a', '1:': 'e', "1'": 'á', '.1': 'u', '-1': 'ú',
       '2,': 'cs', '2.': 'é', '3': 'd', '3,': 'r', '3.': 'v', '4,': 'g', '4.': 'gy',
       '5': 'h', '5,': 'l', '6': 'j', '6,': 'n', '7': 'k', '7,': 's', '7.': 'sz',
       '8': 'm', '8,': 't', '9': 'p'}
# Signs not clean as written; each is disclosed in SOLUTION.md.
ODD = {'4x~k': 'k',  # K-edves: a crossed, closed 4-like sign (retouched?), sense wants 7
       '7~sz': 'sz', # hi-SZ, hara-g-SZ-ol: crossed 7, no dot under it
       '[0]': 'o'}   # komOrícsd: solid ink blot; restoration, not read
K = {**KEY, **ODD}
LINES = [
 [("4x~k 1: 3 3. 1: 7,", 'Kedves'), ("8 1. 4, 1 8, 7 1' 8", 'Magitkám')],
 [("8 1", 'Mi'), ("3. 1. 6,", 'van'), ("3. 1: 5, 1: 3", 'veled'), ("5 0 4.", 'hogy'),
  ("6, 1: 8", 'nem'), ("1 3, 7.", 'írsz')],
 [("5 1 7~sz", 'hisz'), ("8, 1. 5, 1' 6,", 'talán'), ("2, 1. 7", 'csak'), ("6, 1: 8", 'nem'),
  ("5 1. 3, 1. 4, 7~sz 0 5,", 'haragszol'), ("2, 1. 7", 'csak'), (".1 4. 1. 6,", 'ugyan')],
 [("1 3, 6 1' 5,", 'írjál'), ("7 1: 3 3. 1: 7,", 'kedves'), ("7 2. 3, 5, 1: 7", 'kérlek'),
  ("7. 2. 9 1: 6,", 'szépen')],
 [("6, 1:", 'ne'), ("7 0 8 [0] 3, 1 2, 3", 'komorícsd'), ("1.", 'a'),
  ("7. 1 3. 1: 8 1: 8,", 'szívemet')],
 [("2. 6,", 'én'), ("-1 4. 1 7,", 'úgyis'), ("1 3, 0 7", 'irok'), ("8 1 6, 3 1 4,", 'mindig')],
]
FOLD = str.maketrans({'ó': 'o', 'í': 'i', 'K': 'k', 'M': 'm'})
out = []
for ws in LINES:
    res = []
    for ct, reading in ws:
        got = ''.join(K[t] for t in ct.split())
        if got != reading.translate(FOLD):
            sys.exit('MISMATCH %r -> %r vs %r' % (ct, got, reading))
        res.append(reading)
    out.append(' '.join(res))
TOK = [t for ws in LINES for c, _ in ws for t in c.split()]
n = sum(t in ODD for t in TOK)
print('ciphertext signs: %d - %d decode by the table, %d by sense (ODD: 3 dotless/odd, 1 restored blot)'
      % (len(TOK), len(TOK) - n, n))
print()
print('[%s]!\n' % out[0])
print('[%s?\n%s,\n%s,\n%s,\n%s] még többet ez után mert mostanába nem érkeztem.   Sz. A.\n'
      % tuple(out[1:]))
print('''Emészt a vágy napról napra,
Mint sorvasztó-kór betegét;
Csókot hintani ajakadra,
Szívni édes leheletét.

II
Emészt a vágy... sivó, kopár,
Tikkadt mező a kebelem,
Perzsel a hő, a napsugár,
Égő vágyam: a szerelem.

III
S te szép leányka kaczagsz tán
Amig én érted epedek...
Oh, kaczagj, csak nem neked fáj
Hogyha én érted szenvedek!

mindnyájatokat csókollak.

Address: Tek. Szépreménnyü Sziber Margitka kisasszonynak Szomolya u. p. Bogács
Pencil note: 1915 XII 5''')
