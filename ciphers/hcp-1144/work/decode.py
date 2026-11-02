#!/usr/bin/env python3
"""hcp-1144: verify source hashes, decode work/transcription.txt, print the plaintext."""
import hashlib, os, sys
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H = {'source/picture-large.jpg': 'b143b4d3c016dfedce7be6e3660b0536928c8c0ad953eec8a23859241391d20d',
     'source/address-large.jpg': '2dc273606a2858fccef64f8b40c3e126f6e76731d1ac3cc98e9c4d5a06bb1ae7',
     'work/hires/cpc_1916-05-19_HU_Mezokovesd_HU_Szomolya_szomolya-36_pic.jpg': '3ff4010b9bb9199b1a712ee1bd76af6d8bab9cfccbd3ac4935ee1a7e50e552b6',
     'work/hires/cpc_1916-05-19_HU_Mezokovesd_HU_Szomolya_szomolya-36_adr.jpg': '0c74cf3d760d44fd2c3b7745b32057b1d4b4cb06003f36e31ee682af52d1e808'}
for p, h in H.items():
    if hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest() != h:
        sys.exit('HASH MISMATCH ' + p)
print('source hashes OK (%d files)' % len(H))
KEY = {'0': 'o', '0,': 'ö', '1': 'i', '1.': 'a', '1:': 'e', "1'": 'á', '1,': 'b',
       ':1': 'ü', '.1': 'u', '2': 'c', '2,': 'cs', '2.': 'é', '3': 'd', '3,': 'r', '3.': 'v',
       '4': 'f', '4,': 'g', '4.': 'gy', '5': 'h', '5,': 'l', '5.': 'ly', '6': 'j', '6,': 'n',
       '6.': 'ny', '7': 'k', '7,': 's', '7.': 'sz', '8': 'm', '8,': 't', '9': 'p', '9,': 'z',
       '?7,': '[s?]'}
# Expected reading of each word group, in card order (card's own spelling).
READ = '''édes margitkám
ha e lapot megkapod légy szíves értesíte
ni hogy lejösz avagyis lejöttöke kedves
ángyikával vasárnap a fényképészhez
mert azt montad mikor ott voltam hogy most va
sárnap fogtok lejönni te
hát hacsak lehet jöjetek
mert úgy is soká lesz kész
az enyém is csak pünkösdre
lesz meg janinak még most
sem írtam mert nem lá[s?]ni
nol a címét most egyebet
nem írok szervusz
milyen nagyon nagy a tenger
de nagyobb a szerelem
a tengernek van határa
a szerelem végtelen
hogy ha ajkam ajkadra
rátapad
menyországban érzem én
magamat
számtalanszor
ölel
csókol és
üdvözöl hű kedvesed árpád'''.split('\n')
FOLD = str.maketrans('óőíúű', 'oöiuü')
rows = [l for l in open(os.path.join(D, 'work/transcription.txt'), encoding='utf-8') if l.strip() and l[0] != '#']
assert len(rows) == len(READ), (len(rows), len(READ))
n = odd = 0
for row, exp in zip(rows, READ):
    out = ''
    for t in row.replace(')', '|').replace('|', ' | ').split():
        if t == '|':
            out += ' '; continue
        n += 1
        if '~' in t:
            odd += 1; out += t.split('~')[1]
        else:
            out += KEY[t]
            odd += t.startswith('?')
    out = ' '.join(out.split())
    if out != exp.translate(FOLD):
        sys.exit('MISMATCH\n %s\n %s' % (out, exp.translate(FOLD)))
print('all %d rows match; %d cipher signs, %d by the table, %d by sense or doubtful\n' % (len(rows), n, n - odd, odd))
print('''Mezőkövesd, 1916. V/19. [open]

[Édes Margitkám!
Ha e lapot megkapod, légy szíves értesíteni, hogy lejösz, avagyis lejöttök-e
kedves ángyikával vasárnap a fényképészhez, mert azt montad, mikor ott voltam,
hogy most vasárnap fogtok lejönni. Tehát hacsak lehet, jöjetek, mert úgy is soká
lesz kész, az enyém is csak pünkösdre lesz meg. Janinak még most sem írtam, mert
nem lá[s?]ninol a címét. Most egyebet nem írok. Szervusz.

Milyen nagyon nagy a tenger,
De nagyobb a szerelem,
A tengernek van határa,
A szerelem végtelen.

Hogy ha ajkam ajkadra rátapad,
menyországban érzem én magamat.

Számtalanszor ölel, csókol és üdvözöl hű kedvesed (Árpád)]

Address [open]: Őnagysága / Sziber Margitka / kisasszonynak / Szomolya / (u.p. Bogács) / (Borsod m.)
[ ] = enciphered on the card. Punctuation, capitals and accents on o, i, u are editorial,
except the ! after the salutation (Margitkám !) and line-end hyphens, which the writer drew; they are not cipher signs.''')
