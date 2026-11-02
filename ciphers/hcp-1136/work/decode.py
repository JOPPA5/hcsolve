#!/usr/bin/env python3
"""hcp-1136: verify scan hashes, decode work/transcription.txt with work/key.json, print the text."""
import hashlib, json, os, re, sys, glob
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H = {'source/picture-large.jpg': 'e85585b2ebdc3d94f25f9cf0b401d59298cd4963f7d6f21297360d2d9a5df9cc',
     'source/address-large.jpg': '66709f8140c8ddf667cb2c2c20b9d8941bf9ca33bd082b0c9535862d71eab8a1',
     'work/hires/cpc_1916-03-24_HU_Mezokovesd_HU_Szomolya_szomolya-24_pic.jpg': 'a98161d34ff09a4abf6b1869fdb55b4815b23cc9e979167ec1dbd3d8b035bf71',
     'work/hires/cpc_1916-03-24_HU_Mezokovesd_HU_Szomolya_szomolya-24_adr.jpg': '46e7ff555aaabfd7b2e977e6381317489d2eaf06fca61193ee5a6c475cf8a8eb'}
for p, h in H.items():
    if hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest() != h:
        sys.exit('HASH MISMATCH ' + p)
print('source hashes OK (%d files)' % len(H))
KEY = json.load(open(os.path.join(D, 'work/key.json'), encoding='utf-8'))
FOLD = str.maketrans('óőíű', 'oöiü')
def fold(s):
    return re.sub(r'[^a-záéöüóőíű]', '', s.lower()).translate(FOLD)
n = sense = clear = 0
used = {}
out = []
for line in open(os.path.join(D, 'work/transcription.txt'), encoding='utf-8'):
    if line.startswith('#') or not line.strip():
        continue
    ct, reading = [x.strip() for x in line.split('|')]
    got = ''
    for t in ct.replace('/', ' ').split():
        if t.startswith('='):
            got += t[1:].lower(); clear += 1
        else:
            if t.startswith('['):
                t = t.strip('[]'); sense += 1
            n += 1; used[t] = used.get(t, 0) + 1
            got += KEY[t]
    if got != fold(reading):
        sys.exit('MISMATCH %r -> %r vs %r' % (ct, got, fold(reading)))
    out.append(reading)
print('cipher signs: %d (%d distinct), of which %d read by sense; %d letters written in clear'
      % (n, len(used), sense, clear))
assert not set(KEY) - set(used), set(KEY) - set(used)
print()
print('\n'.join(out[:6])); print(); print('I'); print('\n'.join(out[6:10]))
print('II'); print('\n'.join(out[10:14])); print(); print('\n'.join(out[14:]))
print('\nMezőkövesd, 1916. III/24. (in clear)')
print('Address (in clear): Őnsg. / Szépreményű / Sziber Margitka / kisasszonynak / Szomolya / (Borsod m.) u. p. Bogács.')
