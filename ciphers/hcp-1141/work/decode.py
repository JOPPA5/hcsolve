#!/usr/bin/env python3
"""hcp-1141: verify scan hashes, decode work/transcription.txt with the key, print the plaintext."""
import hashlib, os, re, sys
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H = {'source/picture-large.jpg': 'fe8fed45fd307bcd09138d9d57d6387d362f7e7dbff2ba86b519cbc1ccaa2a9e',
     'source/address-large.jpg': '0ab3fa1e57cb9a6490f4cf1d8e46243054527802c4cb6c757b63b41e9a6dd2a4',
     'work/hires/cpc_1916-02-29_HU_Mezokovesd_HU_Szomolya_szomolya-21_pic.jpg': 'cf6c5ab7fb11f5df23d66107db0010c84d9f80f1bf1f2125ad4e7cb6ce4c7772',
     'work/hires/cpc_1916-02-29_HU_Mezokovesd_HU_Szomolya_szomolya-21_adr.jpg': '42393343573323ede8d95e4a9334f11eaf55cf185b6124eceb82af243a42e2ee'}
for p, h in H.items():
    if hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest() != h:
        sys.exit('HASH MISMATCH ' + p)
print('source hashes OK (%d files)' % len(H))
KEY = {'0': 'o', '0,': 'ö', '1': 'i', '1.': 'a', '1:': 'e', "1'": 'á', '1,': 'b', ':1': 'u',
       '2': 'c', '2,': 'cs', '2.': 'é', '3': 'd', '3,': 'r', '3.': 'v',
       '4': 'f', '4,': 'g', '4.': 'gy', '5': 'h', '5,': 'l',
       '6': 'j', '6,': 'n', '6.': 'ny', '7': 'k', '7,': 's', '7.': 'sz',
       '8': 'm', '8,': 't', '9': 'p', '9,': 'z'}
# Word expected at each position: normal Hungarian as the writer spelled it.
READ = """Édes Margitkám a napok nállad nélkül nagyon rosszul telnek de szeretnék legalább
esténkint együtt lenni vélled harctéri tudósítás galiciába megint támadnak az oroszok
minden vonalon de az nem baj jelenleg többet nem írok majd írd meg hogy megkaptade a lapokat
ott kunn a hó tornyosulhat jég is hullhat szél is dúlhat megzörrentve ablakom soha nem
panaszkodom mert szívemben itt van az édes kép a friss tavasz téged látlak mindég álmomban
álmom után minden dolgomban ha sóhajtok érted a panasz ha víg vagyok érted vagyok az
sok csókomat és üdvözletemet küldve maradok hű imádód a sírig Árpád""".split()
def fold(w):
    w = w.lower()
    for a, b in ('óo', 'őö', 'íi', 'úu', 'üu', 'űu'):
        w = w.replace(a, b)
    return w
txt = [l for l in open(os.path.join(D, 'work/transcription.txt'), encoding='utf-8') if not l.startswith('#')]
# A line end divides words unless the writer's hyphen carries the word over.
s = ' '.join(l.strip()[:-1] if l.strip().endswith('-') else l.strip() + ' /' for l in txt)
s = re.sub(r'<[^>]+>', ' / ', s)
s = re.sub(r'(/\s*)+', '/ ', s)
words = [w.split() for w in s.split('/') if w.strip()]
n = odd = 0
out = []
for ws in words:
    g = ''
    for t in ws:
        n += 1
        if '~' in t:
            odd += 1
            g += t.split('~')[1]
        else:
            g += KEY[t]
    out.append(g)
if len(out) != len(READ):
    sys.exit('WORD COUNT %d vs %d' % (len(out), len(READ)))
for g, r in zip(out, READ):
    if g != fold(r):
        sys.exit('MISMATCH %r vs %r' % (g, r))
print('ciphertext signs: %d, words: %d; %d by the table, %d read by sense (~ in transcription.txt)'
      % (n, len(out), n - odd, odd))
print('distinct signs used:', len({t.split('~')[0] for w in words for t in w}))
print()
print('Raw decode: ' + ' '.join(out))
print()
print('''Édes Margitkám!

A napok nállad nélkül nagyon rosszul telnek, de szeretnék legalább esténkint
együtt lenni vélled.

(Harctéri tudósítás) Galiciába megint támadnak az oroszok minden vonalon, de az
nem baj. Jelenleg többet nem írok. Majd írd meg, hogy megkaptad-e a lapokat.

Ott kunn a hó tornyosulhat,
jég is hullhat, szél is dúlhat,
megzörrentve ablakom)
soha nem panaszkodom,
mert szívemben itt van az:
édes kép, a friss tavasz.

Téged látlak mindég álmomban,
álmom után minden dolgomban,
ha sóhajtok érted a panasz,
ha víg vagyok érted vagyok az.

Sok csókomat és üdvözletemet küldve maradok hű imádód a sírig (Árpád)

Open text: Mezőkövesd, 1916, II/29
Address, open: Őnagysága / Szépreményű Sziber Margitka kisasszonynak / Szomolya / u. p. (Bogács) (Borsod m.)
Sentence punctuation other than ! ( ) : and the commas in the verse is editorial.''')
