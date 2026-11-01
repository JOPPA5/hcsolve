#!/usr/bin/env python3
"""hcp-1178: run from repo root: python3 -I ciphers/hcp-1178/work/decode.py"""
import hashlib, pathlib
D = pathlib.Path('ciphers/hcp-1178')
H = {'source/address-large.jpg': '93c5ccff7f9c7d801337667703ebe178118c7c328e611ec8885f586c5788350d',
     'source/picture-large.jpg': '5be841f626e6595db3add05717da5e8e882990085f9376404ad323378acc282b',
     'work/hires/cpc_1915--_HU_Mezokovesd_HU_Szomolya_szomolya-43_adr.jpg': '1d1eba05a2b8d6d70edb3e77f36e29f02d98b368f5f88b57c6d060819f1b963b'}
for f, h in H.items():
    assert hashlib.sha256((D / f).read_bytes()).hexdigest() == h, f
print('source hashes OK')
# 5, and 5. are both l (review 1, finding 1). 1, = b comes from hcp-1179 only and is used only in a control.
KEY = {'1.': 'a', '1:': 'e', '1': 'i', '1,': 'b', '0': 'o', '0,': 'ö', '2.': 'é', '2,': 'cs',
       '3': 'd', '3,': 'r', '4,': 'g', '5': 'h', '5,': 'l', '5.': 'l',
       '6,': 'n', '7': 'k', '7,': 's', '7.': 'sz', '8': 'm', '8,': 't'}
dec = lambda s: ''.join(KEY.get(t, '[%s]' % t) for t in s.split())
toks = [l for l in (D / 'work/transcription.txt').read_text().splitlines() if l and l[0] != '#'][0]
print('cipher   :', toks)
pt = dec(toks)
print('plaintext:', pt)
assert pt == 'csokollaktéged'
assert not any(c == '[' for c in pt)
print('=> csókollak téged')
print('\nControls on sister cards (hardcoded sign strings, so they show agreement, not proof):')
for name, s, want in [
    ('1174 foot', '2, 0 7 0 5, 5, 1. 7', 'csokollak'),
    ('1174 line II', '0, 5, 1: 5, 5 1: 8, 5, 1: 7 2. 6,', 'ölelhetlekén'),
    ('1174 head', '2. 3 1: 7, 8 1. 3, 4, 1 8, 7 1: 8', 'édesmargitkem'),
    ('1179 foot', '1. 5. 1: 4, 7. 1: 1,', 'alegszeb')]:
    got = dec(s)
    assert got == want, (name, got)
    print(f'  {name:13}', got)
print('  (1174 head: the card has a high-dot sign for á; the reading here is the bare 1: as first transcribed.)')
