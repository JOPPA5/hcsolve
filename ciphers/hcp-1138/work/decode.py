#!/usr/bin/env python3
"""hcp-1138: verify scan hashes, decode work/transcription.txt, assert every word, print the plaintext from the decoded words."""
import hashlib, os, re, sys
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H = {'source/picture-large.jpg': 'a1b210aa0d4dda3fd36eeef4f13d8a045a166d85a783a283b4449e536eb60413',
     'source/address-large.jpg': '75ddcca07c16fd5c0823e195f351a48aacc409a8135168a216372309c784fce7',
     'work/hires/cpc_1916-03-17_HU_Mezokovesd_HU_Szomolya_szomolya-23_pic.jpg': '51c97ba568862918879231672cb85ab8f68ed3555014f65217c44c154428644b',
     'work/hires/cpc_1916-03-17_HU_Mezokovesd_HU_Szomolya_szomolya-23_adr.jpg': '18c007b38192e0250efa7514fe217a24a879f47e9e5e649bf6d95353f683759a'}
for p, h in H.items():
    if hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest() != h:
        sys.exit('HASH MISMATCH ' + p)
print('source hashes OK (%d files)' % len(H))
KEY = {'0':'o','0,':'ö','1':'i','1.':'a','1:':'e',"1'":'á','.1':'u',':1':'ü','1,':'b',
       '2':'c','2,':'cs','2.':'é','3':'d','3,':'r','3.':'v','4':'f','4,':'g','4.':'gy',
       '5':'h','5,':'l','6':'j','6,':'n','6.':'ny','7':'k','7,':'s','7.':'sz',
       '8':'m','8,':'t','8.':'ty','9':'p','9,':'z','9~':'z','/':''}
FOLD = str.maketrans({'ó':'o','ő':'ö','í':'i','ú':'u','ű':'ü'})
def fold(w):
    """Reading column to bare decoded letters: lower case, no vowel length the cipher lacks, no added punctuation."""
    return re.sub(r"[()!.,:]", '', w.replace('(d)', '')).lower().translate(FOLD)
paras, cur, toks, words = [], [], [], 0
for ln in open(os.path.join(D, 'work/transcription.txt'), encoding='utf-8'):
    if ln.startswith('#') or not ln.strip(): continue
    if ln.startswith('@end'):
        paras.append(cur); cur = []; continue
    if ln.startswith('@open '):
        paras.append(['OPEN', ln[6:].strip()]); continue
    ct, rd = [x.strip() for x in ln.split('|')]
    got = ''.join(KEY[t] for t in ct.split())
    if got != fold(rd):
        sys.exit('MISMATCH %r -> %r vs %r' % (ct, got, rd))
    cur.append(rd); words += 1
    toks += [t for t in ct.split() if t != '/']
print('cipher signs: %d in %d words, %d distinct; %d plain 9 used as z (no comma); %d 8. = ty'
      % (len(toks), words, len(set(toks)), toks.count('9~'), toks.count('8.')))
print('\nDecoded from the signs ([ ] = enciphered; each word above asserted against the signs; '
      'open text from the @open lines is read, not decoded):')
out = []
for p in paras:
    if p[0] == 'OPEN':
        out.append(p[1])
    else:
        out.append('[' + ' '.join(p) + ']')
# Kívánom: stands in clear on the same line as its enciphered wish
print('\n'.join(out).replace('Kívánom:\n', 'Kívánom: '))
print('\nAddress (open, read not decoded): Őnagysága. Rózsareményű Sziber Margitka kisasszonynak Szomolya u. p. Bogács Borsod m.')
