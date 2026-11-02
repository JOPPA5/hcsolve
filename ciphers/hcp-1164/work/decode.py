#!/usr/bin/env python3
"""hcp-1164: check scan hashes, decode work/transcription.txt, print the full plaintext."""
import hashlib, os, sys, unicodedata
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H = {'source/picture-large.jpg': 'b6fd72a2ab0a6e6d7d70249c3f2ab9a354446eef9417f2627ddebd6570316ee3',
     'source/address-large.jpg': '0f354ee19c9d1a4f0a470dca6b500929dad2a748d4b8f08c629da1e7aa0d4e72',
     'work/hires/cpc_1916-04-01_HU_Mezokovesd_HU_Szomolya_szomolya-26_pic.jpg': '62fdba7aba0237912de5f15b8ec5c50751ad2639deb791e69028e77688bc8636',
     'work/hires/cpc_1916-04-01_HU_Mezokovesd_HU_Szomolya_szomolya-26_adr.jpg': 'becb91ed99163b0d0189d35fd20d1a059873349254078ce4786d45c02e23ff45'}
for p, h in H.items():
    if hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest() != h:
        sys.exit('HASH MISMATCH ' + p)
print('source hashes OK (%d files)' % len(H))
KEY = {'0': 'o', '0,': 'ö', '1': 'i', '1.': 'a', '1:': 'e', "1'": 'á', ':1': 'ü', '1,': 'b',
       '2,': 'cs', '2.': 'é', '3': 'd', '3,': 'r', '3.': 'v', '4': 'f', '4,': 'g', '4.': 'gy',
       '5': 'h', '5,': 'l', '5.': 'ly', '6': 'j', '6,': 'n', '6.': 'ny', '7': 'k', '7,': 's',
       '7.': 'sz', '8': 'm', '8,': 't', '8.': 'ty', '9': 'p', '9,': 'z', '9.': 'zs'}
FOLD = str.maketrans({'ó': 'o', 'ő': 'ö', 'í': 'i', 'ú': 'ü', 'ű': 'ü', 'u': 'ü'})
def norm(s):
    return ''.join(c for c in s.lower() if c.isalpha()).translate(FOLD)
out, n, used = [], 0, set()
for line in open(os.path.join(D, 'work/transcription.txt'), encoding='utf-8'):
    line = line.rstrip('\n')
    if line.startswith('#'):
        continue
    if line.startswith('@'):
        out.append('\n[' + line[1:] + ']\n'); continue
    if line == '/':
        out.append('\n'); continue
    ct, reading = [x.strip() for x in line.split('|')]
    got = ''
    for t in ct.split():
        if t.startswith('='):
            got += t[1:]
        else:
            got += KEY[t]; n += 1; used.add(t)
    if norm(got) != norm(reading):
        sys.exit('MISMATCH %r -> %r vs %r' % (ct, got, reading))
    out.append(reading + ' ')
print('%d cipher signs, %d distinct, all decode by the fixed table into the stated words' % (n, len(used)))
print('unused key signs:', sorted(set(KEY) - used) or 'none')
print(''.join(out).replace(' \n', '\n'))
