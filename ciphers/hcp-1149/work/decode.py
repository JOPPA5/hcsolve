#!/usr/bin/env python3
"""hcp-1149: check scan hashes, decode work/transcription.txt, compare with the stated reading."""
import hashlib, os, sys, unicodedata
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H = {'source/picture-large.jpg': 'f1fc4b1c95794c3ceced72175655a3ca6a502e5e404b5f8bf8193754ec5c512f',
     'source/address-large.jpg': '7aab65795130e778ac5e860a7c75508a80edb50330132a8d2f4557efd0696df5',
     'work/hires/cpc_1916-04-26_HU_Mezokovesd_HU_Szomolya_szomolya-32_pic.jpg': '92d840ab88835d67e2bd7464862f7a7f1702db6ecf69d9590fa34e1546a513f8',
     'work/hires/cpc_1916-04-26_HU_Mezokovesd_HU_Szomolya_szomolya-32_adr.jpg': 'b48ccf1c5330277a24f1a8a6185c3de29006a90a79ebdb69c4f0ba6037a7d1da'}
for p, h in H.items():
    if hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest() != h:
        sys.exit('HASH MISMATCH ' + p)
print('source hashes OK (%d files)' % len(H))
KEY = {'0': 'o', '0,': 'ö', '1': 'i', '1.': 'a', '1:': 'e', "1'": 'á', '1,': 'b', ':1': 'ü',
       '2': 'c', '2,': 'cs', '2.': 'é', '3': 'd', '3,': 'r', '3.': 'v',
       '4': 'f', '4,': 'g', '4.': 'gy', '5': 'h', '5,': 'l', '5.': 'l',
       '6': 'j', '6,': 'n', '6.': 'ny', '7': 'k', '7,': 's', '7.': 'sz',
       '8': 'm', '8,': 't', '9': 'p', '9,': 'z'}
EXPECT = """Édes Margitkám
Értesítlek hogy szerencsésen haza
értünk félegyre nagyon sötét volt meg
nagy borulás dörgött villámlott de nem
eset szerencse hogy a lámpát elhoztam
még ilen hasznát nem vettem mint
most anélkül sehogy se tudtunk
volna jönni így is csak így bukdos
tunk)
Erről most többet nem irok
majd ha felmegyek elmondom hogy
hogy értünk le legalább fogsz raj
ta kacagni)
Nem kérdi senki, hogy a réten
Virág miért terem?
Ne kérd lányka hogy szívemben
Miért nyil a szerelem ?
A nap sugára süt a rétre
S fakaszt ott életet
Reám sütött szemed sugára
Azóta szeretlek
Számtalanszor ölel csókol
és üdvözöl hűséges
kedvesed (Árpád)
Mezőkövesd, 1916. IV/26
Én fehér madonnám
szép liliom lányom
te vagy a világom
te vagy a bálványom
üdvöm boldogságom)""".split('\n')
def fold(s):
    s = s.lower()
    for a, b in {'ó': 'o', 'ő': 'ö', 'í': 'i', 'ú': 'ü', 'ű': 'ü', 'u': 'ü'}.items():
        s = s.replace(a, b)
    return s
out, n, ids = [], 0, set()
for raw in open(os.path.join(D, 'work/transcription.txt'), encoding='utf-8'):
    raw = raw.rstrip('\n')
    if not raw or raw.startswith('#'):
        if raw.startswith('#') and raw[1:2].isupper():
            out.append(raw)
        continue
    parts = []
    for seg in raw.split(' ; '):
        if seg.startswith('open:'):
            parts.append(seg[5:].strip()); continue
        words = []
        for w in seg.split('|'):
            r = ''
            for t in w.split():
                if t in '()':
                    r += t
                else:
                    r += KEY[t]; n += 1; ids.add(t)
            words.append(r)
        parts.append(' '.join(words))
    out.append(' '.join(parts))
lines = [l for l in out if not l.startswith('#')]
if len(lines) != len(EXPECT):
    sys.exit('line count %d vs %d' % (len(lines), len(EXPECT)))
for a, b in zip(lines, EXPECT):
    fa, fb = fold(a).replace(' ', ''), fold(b).replace(' ', '')
    if fa != fb:
        sys.exit('MISMATCH\n %s\n %s' % (a, b))
print('%d cipher signs, %d distinct; every line agrees with the stated reading\n' % (n, len(ids)))
i = 0
for l in out:
    if l.startswith('#'):
        print('\n[%s]' % l[1:].split()[0]); continue
    print(EXPECT[i]); i += 1
print('\nAddress (open): Őnsg. / Szépreményű Sziber Margitka kisasszonynak / Szomolya / u. p. Bogács')
