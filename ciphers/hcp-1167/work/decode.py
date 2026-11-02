#!/usr/bin/env python3
"""hcp-1167. Run from the repo root: python3 -I ciphers/hcp-1167/work/decode.py
Checks source hashes, decodes work/transcription.txt with the key, prints the plaintext."""
import hashlib, os, sys
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B = 'cpc_1916-03-11_HU_Mezokovesd_HU_Szomolya_szomolya-22'
H = {'source/picture-large.jpg': 'ca310a0827622ef4665a26390d23f045bc2a94184ce5660dce4dbaf3a4e50234',
     'source/address-large.jpg': '2ddb5f99ada3c0a2ccb278d0e9fd36bf4f3f4549241284a831c3a2b2b12bb5f0',
     'work/hires/%s_pic.jpg' % B: '102b3f1779d30055d2522b9faf22cf83d8abdec672258a2b0fa48a1f946f2bf0',
     'work/hires/%s_adr.jpg' % B: '3a28ff96617c5c63f9324dce7df94c1313382e3662337bc7f74d9c84820f714b'}
for p, h in H.items():
    if hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest() != h:
        sys.exit('HASH MISMATCH ' + p)
print('source hashes OK (%d files)' % len(H))
KEY = {'0': 'o', '0,': 'ö', '1': 'i', '1.': 'a', '1:': 'e', "1'": 'á', '1,': 'b',
       ':1': 'ü', '.1': 'u', '2,': 'cs', '2.': 'é', '3': 'd', '3,': 'r', '3.': 'v',
       '4': 'f', '4,': 'g', '4.': 'gy', '5': 'h', '5,': 'l', '5.': 'ly', '6': 'j',
       '6,': 'n', '6.': 'ny', '7': 'k', '7,': 's', '7.': 'sz', '8': 'm', '8,': 't',
       '9': 'p', '9,': 'z'}
# sign~letter: the sign as written does not give the letter; taken by sense, disclosed.
n = odd = 0
out = []
for line in open(os.path.join(D, 'work/transcription.txt'), encoding='utf-8'):
    if line.startswith('#') or not line.strip():
        continue
    words = []
    for w in line.split('|'):
        s = ''
        for t in w.split():
            if t in '()!':
                s += t
            elif '~' in t:
                sign, by_sense = t.split('~')
                n += 1; odd += 1
                s += '[%s<%s]' % (by_sense, KEY[sign])
            else:
                n += 1
                s += KEY[t]
        words.append(s)
    out.append(' '.join(words))
print('cipher signs: %d, by the table %d, by sense %d; distinct signs in key: %d\n' % (n, n - odd, odd, len(KEY)))
print('\n'.join(out))
print('\n[x<y] = sign gives y as written, sense requires x. Open text (not enciphered):')
print('Sokszor csókolom ángyikát is / és [a?] kis Mariskát is. / Mezőkövesd, 1916. III/11.')
