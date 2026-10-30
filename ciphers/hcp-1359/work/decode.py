#!/usr/bin/env python3
"""HCP 1359: Caesar -1 decode of the manual transcription; checks source hashes."""
import hashlib, json, string, sys
from pathlib import Path
d = Path(__file__).resolve().parents[1]
H = {'source/picture-large.jpg': '27eeca135692b184e6aff291f47107fb0d016789782b3563cbbfac52c095c96e',
     'source/address-large.jpg': '58387e3eea851cf00cb75f3e20aeeda0dc6d6100f465c52e2eef4a3b77205b6c',
     'work/hires/pc_hcp_40_pic.JPG': 'bcc7d1f956db9d955987644ed38e032e60ee4a037b950fbefe55bbcf2c10057d',
     'work/hires/pc_hcp_40_adr.JPG': 'ac71093b7bef944294d4fa51f6521eac8cfb6bdcf4f01ccfe7986b8472984ba6'}
for f, h in H.items():
    if hashlib.sha256((d / f).read_bytes()).hexdigest() != h:
        sys.exit('HASH MISMATCH ' + f)
print('source hashes OK')
L, U = string.ascii_lowercase, string.ascii_uppercase
dec = str.maketrans(L + U, U[-1] + U[:-1] + U[-1] + U[:-1])
enc = str.maketrans(U, U[1:] + U[0])
t = json.loads((d / 'work/transcription.json').read_text())
print('[plain heading]', t['heading_plain'])
n = lit = 0
for line in t['lines']:
    out = []
    for kind, s in line:
        if kind == 'cipher':
            p = s.translate(dec)
            assert p.translate(enc).lower() == s.lower(), s
            n += sum(c.isalpha() for c in s)
            out.append(p)
        else:
            lit += sum(c.isalpha() for c in s)
            out.append('[' + s + ']')
    print(' '.join(s for _, s in line), ' => ', ' '.join(out))
print('[plain date]', t['date_plain'])
print(n, 'cipher letters decoded, round trip OK;', lit, 'letters kept literal')
u = t['uncertain_sign']
print('uncertain sign: in', u['token'], u['letter'], 'preferred; literal alternative',
      u['alternative'], '=> ' + u['token'].replace(u['letter'], u['alternative']).translate(dec))
