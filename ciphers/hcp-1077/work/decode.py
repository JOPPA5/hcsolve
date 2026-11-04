"""hcp-1077: number substitution, 24-letter alphabet without J (I/J=9) and with U/V separate.
Run from repo root: python3 -I ciphers/hcp-1077/work/decode.py"""
import hashlib, os, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
H = {'source/picture-large.jpg': '07ca4d3bb0a633ab81e749dc12fb80cd3e2a3476f8bad323e698d656d6664a7b',
     'source/address-large.jpg': '7553d041702a47c3d3ad17380ff037b6e49a9223d9dfc5fa8db95363f5b51333',
     'work/hires/cpc_1908-01-10_DE_Fechenheim_DE_Fechenheim__pic.jpg': 'e73c7aa211998dbbd9cb49e4a7e4cd21a6d48939402f2710ac084658615bc62e'}
for p, h in H.items():
    got = hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest()
    print(('OK   ' if got == h else 'FAIL ') + p)
    if got != h: sys.exit(1)
ALPHA = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # no J
KEY = {i + 1: c for i, c in enumerate(ALPHA)}
out = []
for line in open(os.path.join(D, 'work/transcription.txt')):
    if line.startswith('#') or not line.strip(): continue
    out.append(''.join(KEY[int(n)] for n in line.split()))
print('Herzlichen Gruss sendet')
print(' '.join(out))
