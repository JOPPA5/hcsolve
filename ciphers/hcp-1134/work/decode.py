"""hcp-1134: number substitution, A=2 ... I=10, J omitted, K=11 ... Z=26; '"' = umlaut.
Run from repo root: python3 -I ciphers/hcp-1134/work/decode.py"""
import hashlib, os, sys
D = os.path.dirname(os.path.abspath(__file__)); C = os.path.dirname(D)
H = {'source/address-large.jpg': 'd1522948d1e24b0a5b8fb7b17d5d5b74a979c53966a2c6ed8170e4f84594ce79',
     'source/picture-large.jpg': 'ff020d3b2bcfda5477627afa64585b4b5eb09b442cd8e1e2e345b42b50885461',
     'work/hires/cpc_1910-03-11_DE_Schweidnitz_DE_Schweidnitz_fritzlehmann-10_adr.jpg': 'edb1c58ecc1bd82f890ec266e42cce66cd82a6b337d05e0b3595b71afd22f0de'}
for p, h in H.items():
    got = hashlib.sha256(open(os.path.join(C, p), 'rb').read()).hexdigest()
    print(('OK   ' if got == h else 'FAIL ') + p)
    if got != h: sys.exit(1)
ALPHA = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'          # 25 letters, no J
KEY = {i + 2: ch for i, ch in enumerate(ALPHA)}  # A=2..I=10, K=11..Z=26; 1 unused
UML = {'A': 'Ä', 'O': 'Ö', 'U': 'Ü'}
out = []
for line in open(os.path.join(D, 'transcription.txt'), encoding='utf-8'):
    if line.startswith('#') or not line.strip(): continue
    words = []
    for tok in line.replace('-', ' ').split():
        w = ''
        for n in tok.strip('.').split('.'):
            u = n.endswith('"'); ch = KEY[int(n.rstrip('"'))]
            w += UML[ch] if u else ch
        words.append(w)
    out.append(' '.join(words))
print('\n'.join(out))
