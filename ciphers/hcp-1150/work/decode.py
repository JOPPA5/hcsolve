#!/usr/bin/env python3
"""hcp-1150: verify scan hashes, decode the digit cipher, print the full plaintext.
Tokens are signs as read from the card. A token 'x~L' is a sign read as written x but taken
as letter L against the table (disclosed in SOLUTION.md). '?~L' = sign physically hidden."""
import hashlib, os, sys
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = 'cpc_1916-06-12_HU_Mezokovesd_HU_Szomolya_szomolya-40_'
H = {'source/picture-large.jpg': 'a2620d6223ddf396f50899d7f7ec6d7839ed9791a822005c4f99bd49d98346d8',
     'source/address-large.jpg': 'b17043da8157dad8c388ffa9263502b296c456cdc6669b778fe6917de19d7ac4',
     'work/hires/' + A + 'pic.jpg': '4fc1b027cbe9d67caa1326182b459fc4ae768a532faed01f9355648d4b2dd824',
     'work/hires/' + A + 'adr.jpg': '390b8bc43f38801469e265de724a3a1d77adac8bc03aec5e6b180fdec251dca5'}
for p, h in H.items():
    if hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest() != h:
        sys.exit('HASH MISMATCH ' + p)
print('source hashes OK (%d files)' % len(H))
KEY = {'0': 'o', '0,': 'ö', '1': 'i', '1.': 'a', '1:': 'e', "1'": 'á', ':1': 'ü', '1,': 'b',
       '2,': 'cs', '2.': 'é', '3': 'd', '3,': 'r', '3.': 'v', '4': 'f', '4,': 'g', '4.': 'gy',
       '5': 'h', '5,': 'l', '6': 'j', '6,': 'n', '6.': 'ny', '7': 'k', '7,': 's', '7.': 'sz',
       '8': 'm', '8,': 't', '9': 'p', '9,': 'z'}
T = """
Drága|3 3, 1' 4, 1.
Margitkám!|8 1. 3, 4, 1 8, 7 1' 8
#
értesítlek|2. 3, 8, 1: 7, 1 8, 5, 1: 7
hogy|5 0 4.
inet|1 6, 1: 8,
hétfőn|5 2. 8, 4 0, 6,
éjjel|2. 6 6 1: 5,
elutazom|1: 5, :1 8, 1. 9, 0 8
hazafelé.|5 1. 9, 1. 4 1: 5, 2.
Az|1~a 9,
ünnepek|1~ü 6, 6, 1: 9 1: 7
itt|1 8, 8,
nagyon|6~n 1. 4. 0 6,
lassan|5, 1. 7, 7, 1. 6,
teltek,|8, 1: 5, 8, 1: 7
jobban|6 0 1, 1, 1. 6,
szerettem|7. 1: 3, 1: 8, 8, 1: 8
volna|3. 0 5, 6, 1. 
veled|3. 1: 5, 1: 3
tölteni,|8, 0, 5, 8, 1: 6, 1
no|6, 0
de|3 1:
nem|6, 1: 8
soká|7, 0 7 1'
ott|0 8, 8,
leszek.|5, 1: 7. 1: 7
Egyéb|1: 4. ?~é 1,
újságot|:1 6 7, 1' 4, 0 8,
nem|6, 1: 8
tudok|8, :1 3 0 7
írni.|1 3, 6, 1
Gerzon|4, 1: 3, 9, 0 6,
hazajött|5 1. 9, 1. 6 0, 8, 8,
hát|5 1. 8,
hadi|5 1. 3 1
szabadságra.|7. 1. 1, 1~a 3 7, 1' 4, 3, 1.
Majd|8 1. 6 3
szóval|7. 0 3. 1. 5,
többet.|8, 0, 1, 1, 1: 8,
#
Van|3. 1. 6,
egy|1: 4.
kis|7 1 7,
szende|7. 1: 6, 3 1:
virág,|3. 1 3, 1' 4,
úgy|:1 4.
hívják|5 1 3. 6 1' 7
hogy|5 0 4.
nefelejcs.|6, 1: 4 1: 5, 1: 6 2,
Ez|1: 9,
a|1.
virág|3. 1 3, 1' 4,
tolmácsolom|8, 0 5, 8 1' 2, 0 5, 0 8
lányka,|5, 1' 6. 7 1.
engem|1: 6, 4, 1: 8
ne|6, 1:
felejts!|4 1: 5, 1: 6 8, 7,
#
Nem|6, 1: 8
bámulok|1, 1' 8 :1 5, 0 7
a|1.
fényeségre,|4 2. 6. 1: 7, 2. 4, 3, 1:
ragyognak|3, 1. 4. 0 4, 6, 1. 7
bár|1, 1' 3,
a|1.
csillagok,|2, 1 5, 5, 1. 4, 0 7
mert|8 1: 3, 8,
itt|1 8, 8,
a|1.
földön|4 0, 5, 3 0, 6,
reád|3, 1: 1' 3
nézve|6, 2. 9, 3. 1:
egy|1: 4.
szebb|7. 1: 1, 1,
csillagot|2, 1 5, 5, 1. 4, 0 8,
láthatok.|5, 1' 8, 5 1. 8, 0 7
#
Soraimat|7, 0 3, 1. 1 8 4.~a 8,
zárva|9, 1' 3, 3. 1.
számtalanszor|7. 1. 8 8, 1. 5, 1. 6, 7. 0 3,
ölel,|0, 5, 1: 5,
csókol|2, 0 7 0 5,
és|2. 7,
üdvözöl|:1 3 3. 0, 9, 0, 5,
hű|5 :1
imádód|1 8 1. 3 0 3
(Árpád)|1' 3, 9 1' 3
"""
F = str.maketrans({'ó': 'o', 'ő': 'ö', 'í': 'i', 'ú': 'ü', 'u': 'ü', 'ű': 'ü', 'á': 'a'})
n = odd = 0; out = []; line = []
for r in T.strip().split('\n'):
    if r == '#':
        out.append(' '.join(line)); line = []; continue
    w, c = r.split('|')
    got = ''
    for t in c.split():
        n += 1
        if '~' in t:
            odd += 1; got += t.split('~')[1]
        else:
            got += KEY[t]
    clean = w.lower().strip('.,!()[]').replace('[', '').replace(']', '')
    if got.translate(F) != clean.translate(F):
        sys.exit('MISMATCH %r -> %r' % (w, got))
    line.append(w)
out.append(' '.join(line))
print('signs: %d; %d by the table, %d against it or hidden (see SOLUTION.md)\n' % (n, n - odd, odd))
print('Kisterenne, 1916 VI/.. [open text]\n')
print('\n\n'.join(out))
print('\nAddress [open text]: Őnagyságn. / Sziber Margitka / Kisasszonynak / Szomolya / (Borsod m.) / u. p. Bogács')
