#!/usr/bin/env python3
"""hcp-1168: verify scan hashes, decode work/transcription.txt, print the full plaintext."""
import hashlib, os, sys
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H = {'source/picture-large.jpg': '1014fbc93410175e16c5c68df7ba72df99e083a1260649c691fe7222c61d0e1e',
     'source/address-large.jpg': '218f9ce4f457cdaf60b5026b53c8753dec2f1628dcc0a0fb1db24cf6f22f1825',
     'work/hires/cpc_1916-01-30_HU_Mezokovesd_HU_Szomolya_szomolya-16_pic.jpg': '665f1785cf8d4543651a8c3b7064a1b35f8b6619c742c2d37c874db16832b590',
     'work/hires/cpc_1916-01-30_HU_Mezokovesd_HU_Szomolya_szomolya-16_adr.jpg': 'b32e7ddce4b4c533a3f2eece73473134cd9ad770d4aa61e4a4c79efd3bb134e6'}
for p, h in H.items():
    if hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest() != h:
        sys.exit('HASH MISMATCH ' + p)
print('source hashes OK (%d files)' % len(H))
KEY = {'0': 'o', '0,': 'ö', '1': 'i', '1,': 'b', '1.': 'a', '1:': 'e', "1'": 'á', '.1': 'u', ':1': 'ü',
       '2': 'c', '2,': 'cs', '2.': 'é', '3': 'd', '3,': 'r', '3.': 'v', '4': 'f', '4,': 'g', '4.': 'gy',
       '5': 'h', '5,': 'l', '5.': 'l', '6': 'j', '6,': 'n', '6.': 'ny', '7': 'k', '7,': 's', '7.': 'sz',
       '8': 'm', '8,': 't', '9': 'p', '9,': 'z'}
READ = {  # line -> reading of each word; a word ending in = continues on the next line
 'L01': 'Édes Margitkám', 'L02': 'bocsás meg hogy inyen ritkán', 'L03': 'írok de most az anyagi',
 'L04': 'viszonyok nem fizetik', 'L05': 'ki jobban nem tehetünk', 'L06': 'rólla hogy ahoz a pár krájcárhoz',
 'L07': 'olan nehezen lehet', 'L08': 'hozzájutni amit', 'L09': 'keves Anyukád ide adot',
 'L10': 'kilenc koronát már nincs', 'L11': 'belőle mert nyolc korona', 'L12': 'kellet a cipőre az mán',
 'L13': 'az egy koronából az adóságomat', 'L14': 'fizettem még most', 'L15': 'is tartozok egy pár krajcárral', 'L16': '',
 'SIG': 'Árpád', 'V2': 'magamat', 'V4': 'megcsókoljam ajkadat',
 'L21': 'sokszor üdvözölve és csókolva maradok szerető kedvesed a sírig'}
FOLD = str.maketrans({'ó': 'o', 'ő': 'ö', 'í': 'i', 'É': 'é', 'Á': 'á', 'M': 'm', 'A': 'a'})
rows = {}
for ln in open(os.path.join(D, 'work/transcription.txt'), encoding='utf-8'):
    if ln.strip() and not ln.startswith('#'):
        k, v = ln.rstrip('\n').split(' ', 1); rows[k] = v
letters = ''; n = odd = 0
dec = {}
for k, v in rows.items():
    s = ''
    for t in v.replace('=', '').split():
        if t == '|': s += ' '; continue
        n += 1
        if '~' in t:
            sign, val = t.split('~'); odd += 1
            s += val or KEY[sign]
        else:
            s += KEY[t]
    dec[k] = s.replace(' ', '')
    letters += dec[k]
# whole-text check, across the line breaks: signs -> letters == stated reading
want = ''.join(READ[k].replace(' ', '').translate(FOLD) for k in rows)
if letters != want:
    i = next((i for i, (a, b) in enumerate(zip(letters, want)) if a != b), min(len(letters), len(want)))
    sys.exit('MISMATCH at %d: %r vs %r' % (i, letters[i-10:i+15], want[i-10:i+15]))
print('cipher signs: %d; %d by the table as written, %d rest on word sense (tagged ~ in transcription.txt)\n' % (n, n-odd, odd))
R = READ
print('Mezőkövesd, 1916, I 30, (open, picture side)\n')
print('[%s!]\n' % R['L01'])
print('[Bocsás meg, hogy inyen ritkán írok, de most az anyagi viszonyok nem fizetik ki jobban,')
print('nem tehetünk rólla, hogy ahoz a pár krájcárhoz olan nehezen lehet hozzájutni, amit keves')
print('Anyukád ide adot, kilenc koronát már nincs belőle mert nyolc korona kellet a cipőre az mán')
print('az egy koronából az adóságomat fizettem még most is tartozok egy pár krajcárral]')
print(') ([Árpád]) 1916, I/30  (the date is open, boxed)\n')
print('Saját kis versembe zárni\nSzeretném én [%s]\nHogy mikor ajkad elszavalja,\n[Megcsókoljam - ajkadat]\n' % R['V2'])
print('[Sokszor üdvözölve és csókolva - maradok szerető kedvesed a sírig]\n')
print('Address: Őnsg. / Szépreményű / Sziber Margitka / urleánynak / Szomolya / (Borsod m.) u. p. Bogács.')
print('[ ] = enciphered on the card.')
