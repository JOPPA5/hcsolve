#!/usr/bin/env python3
"""hcp-1135: verify source hashes, decode work/transcription.txt with the family key, print the text."""
import hashlib, os, sys
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H = {'source/picture-large.jpg': '955638a65813f14d0cdab4b6302cfedc931223de50e1ff1a253399b111d45639',
     'source/address-large.jpg': '2d5a9d0b2fa11d213294c9589946fd0de6ee4b3486e8af517bd62e2c7bdeb5f5',
     'work/hires/cpc_1916-04-22_HU_Mezokovesd_HU_Szomolya_szomolya-30_pic.jpg': '4df062b36a91c915943feb49c2c5963962312e21dd65129a7e836c5e272e0b56',
     'work/hires/cpc_1916-04-22_HU_Mezokovesd_HU_Szomolya_szomolya-30_adr.jpg': '45bcd5c81c2b0823e1815cc4b13c9f8d0afda0566b2e1ac71e3f1b20887856c3'}
for p, h in H.items():
    if hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest() != h:
        sys.exit('HASH MISMATCH ' + p)
print('source hashes OK (%d files)' % len(H))
FAMILY = {'0': 'o', '0,': 'ö', '1': 'i', '1.': 'a', '1:': 'e', "1'": 'á', ':1': 'ü', '2,': 'cs',
          '2.': 'é', '3': 'd', '3,': 'r', '3.': 'v', '4,': 'g', '5': 'h', '5,': 'l', '6,': 'n',
          '7': 'k', '7,': 's', '7.': 'sz', '8': 'm', '8,': 't', '9': 'p', '9,': 'z', '1,': 'b', '5.': 'l'}
NEW = {'.1': 'u', '4.': 'gy', '6': 'j', '6.': 'ny'}  # first attested on this card
KEY = {**FAMILY, **NEW}
# Reading of each line, accented as normal Hungarian (spelling kept where the signs differ).
R = ['Édes Margitkám',
     'Kívánom a leg boldogabb húsvéti ünepeket',
     'neked a leg tisztább szívből az igaz hogy ez nem valami boldog húsvét no de majd ad még az isten jobbat is',
     'Te testté vált tündérrege', 'Te bájjá lett virág', 'Utánad vágyik csak szívem', 'Becsül szeret imád',
     'A szerelem szárnyán küldöm', 'Te hozzád a lelkem', 'Fogadd lánykám szerelemmel', 'S küld helette lelked',
     'Soraimat zárva üdvözöl és sokszor csókol hű kedvesed Árpád']
FOLD = str.maketrans({'ó': 'o', 'ő': 'ö', 'í': 'i', 'ú': 'u', 'ű': 'ü'})
lines = [l.rstrip('\n') for l in open(os.path.join(D, 'work/transcription.txt'), encoding='utf-8') if l[0] != '#']
assert len(lines) == len(R), 'line count'
n = ncl = nodd = 0
used = {}
for line, reading in zip(lines, R):
    words = []
    for w in line.split(' | '):
        s = ''
        for t in w.split():
            if t == '-':
                continue
            if t[0] == '=':
                s += t[1:]; ncl += 1
            elif '~' in t:
                s += t.split('~')[1]; nodd += 1; n += 1
            else:
                v = KEY[t]; used[t] = v; n += 1
                s += v
        words.append(s)
    raw = ' '.join(words)
    a = raw.lower().translate(FOLD).replace(' ', '')
    b = reading.lower().translate(FOLD).replace(' ', '')
    if a != b:
        sys.exit('MISMATCH\n %s\n %s' % (a, b))
    print(raw.ljust(58 if len(raw) < 58 else 0), '=>', reading)
print('\ncipher signs: %d; by the table %d, by sense %d (SIGN~letter); letters/words in clear: %d groups'
      % (n, n - nodd, nodd, ncl))
print('distinct table signs used: %d, of which new on this card: %s' % (len(used), sorted(set(used) & set(NEW))))
print('\nDate in clear: Mezőkövesd. 1916. IV/22. Address in clear: Őnsg. / Szépreményű Sziber Margitka Kisasszonynak / Szomolya / u. p. (Bogács)')
# Easter 1916 (Gregorian computus), against the card's date.
y = 1916; a = y % 19; b, c = y // 100, y % 100; d, e = b // 4, b % 4; f = (b + 8) // 25; g = (b - f + 1) // 3
h = (19 * a + b - d - g + 15) % 30; i, k = c // 4, c % 4; l = (32 + 2 * e + 2 * i - h - k) % 7
m = (a + 11 * h + 22 * l) // 451; mo = (h + l - 7 * m + 114) // 31; da = (h + l - 7 * m + 114) % 31 + 1
print('Easter Sunday 1916 by the computus: %d-%02d-%02d' % (y, mo, da))
