#!/usr/bin/env python3
"""hcp-1151: verify scan hashes, decode work/transcription.txt, check it against the stated reading."""
import hashlib, os, sys
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H = {'source/picture-large.jpg': 'a1ebf8031c0081131d696a410e4b6efa31d95a7e3cdb8af8ca859e9966e23892',
     'source/address-large.jpg': 'b6e745d8bf85a50142addbf57d9bc38d600eaec386ca04f0f9ba85a0080c9770',
     'work/hires/cpc_1916-05-13_HU_Mezokovesd_HU_Szomolya_szomolya-35_pic.jpg': '7767bfc35f7b3f07065eb739fa380ac03fb36301ea29351583b2c014744ddd37',
     'work/hires/cpc_1916-05-13_HU_Mezokovesd_HU_Szomolya_szomolya-35_adr.jpg': '1fc73640bf855bcefc6cd41637b83690a3c4a92aef5c2bf4ba51ad4e1989aa26'}
for p, h in H.items():
    if hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest() != h:
        sys.exit('HASH MISMATCH ' + p)
print('source hashes OK (%d files)' % len(H))
KEY = {'0': 'o', '0,': 'ö', '1': 'i', '1.': 'a', '1:': 'e', "1'": 'á', ':1': 'ü', '1,': 'b',
       '2,': 'cs', '2.': 'é', '3': 'd', '3,': 'r', '3.': 'v',
       '4': 'f', '4,': 'g', '4.': 'gy', '5': 'h', '5,': 'l', '5.': 'ly',
       '6': 'j', '6,': 'n', '6.': 'ny', '7': 'k', '7,': 's', '7.': 'sz',
       '8': 'm', '8,': 't', '8.': 'ty', '9': 'p', '9,': 'z'}
# reading per word in card order; accents beyond the key's letters are mine.
READ = '''Édes Margitkám
Lapodat megkaptam melynek igazán megörültem
hisz hogy ne mikor már egy hónapja hogy nem
kaptam tőlled most pedig értesítlek hogy
csak a jövő hónap ötödikén soroznak holnap
nem megyek fel mert most fogom levetetni magamat
továbbá értesítlek hogy
meghányattam a kártyát jól
beszélt megmondta aszt is hogy
valaki közülünk fogoly és
nagyon jó dolga van nincs semi
baja pénze van elég és kapt
is megmondta hogy nem soká
kapok tőle hírt é igaz is
let mert épen ma kaptam
tőle két lapot egyiket
apámnak írja másikat
meg egész családnak írja
hogy egészséges Szibériába
van
hegyen ülök völgybe nézek
ellátok a messzeségbe
ott lakik egy szőke lányka
ez én lelkem üdvössége
sokszor
ölel és
csókol szerető
hű kedvesed Árpád'''.split()
FOLD = str.maketrans({'ó': 'o', 'ő': 'ö', 'í': 'i', 'ű': 'ü', 'É': 'é', 'Á': 'á', 'L': 'l', 'M': 'm', 'S': 's'})
words, tot, odd, cur = [], 0, 0, ''
for line in open(os.path.join(D, 'work/transcription.txt'), encoding='utf-8'):
    if line.startswith('#') or not line.strip():
        continue
    parts = line.split()[1:]
    cont = parts[-1] == '='
    if parts[-1] in ('=', '-'):
        parts = parts[:-1]
    for i, t in enumerate(parts + ['|']):
        if t == '|':
            if i == len(parts) and cont:
                break
            words.append(cur); cur = ''
            continue
        tot += 1
        if '~' in t:
            odd += 1; cur += t.split('~')[1]
        else:
            cur += KEY[t]
if len(words) != len(READ):
    sys.exit('word count %d vs %d' % (len(words), len(READ)))
for w, r in zip(words, READ):
    if w != r.translate(FOLD):
        sys.exit('MISMATCH %r vs %r' % (w, r))
print('cipher signs: %d - %d decode by the table, %d are read by sense (~ in transcription); %d words' % (tot, tot - odd, odd, len(words)))
print('open text: Mezőkövesd, 1916. V/13. Address: Őnagysága Sziber Margitka Kisasszonynak, Szomolya (u. p. Bogács.) (Borsod m.)\n')
print(' '.join(READ))
from collections import Counter
c = Counter(t.split('~')[0] for l in open(os.path.join(D, 'work/transcription.txt'), encoding='utf-8')
            if not l.startswith('#') for t in l.split()[1:] if t not in ('|', '=', '-'))
print("\nsign counts: 1. %d, 1' %d, 5, %d, 5. %d, 8. %d" % (c['1.'], c["1'"], c['5,'], c['5.'], c['8.']))
print('Reading order: rows 1-19 above the ruled line, then the poem left of the dashed frame (rows 20-23), then the framed signature (rows 24-27).')
