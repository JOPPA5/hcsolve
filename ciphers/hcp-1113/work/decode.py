"""hcp-1113: number substitution, A=2 ... I=10, J omitted, K=11 ... Z=26 (same table as hcp-1134).
'x' suffix = capital-marking stroke (ignored); '=' suffix = doubled letter. Run from repo root:
python3 -I ciphers/hcp-1113/work/decode.py"""
import hashlib, os, sys
D = os.path.dirname(os.path.abspath(__file__)); C = os.path.dirname(D)
H = {'source/address-large.jpg': '55e3d1d0e873dc7ebda9e74b759b02975bc31a653b962e2a9076b59ca6331862',
     'source/picture-large.jpg': 'c8887b5fd59da29ee5eeb72d1f716693604c7208c6af798558d16aeb66df66d0',
     'work/hires/cpc_1909-07-30_DE_Freiburg-(Schlesien)_DE_Hier_fritzlehmann-06_adr.jpg': '954baa20af8ac788219f74f4d936016d542b7b0d1ca9aabe0377b91719a3d1c1'}
for p, h in H.items():
    got = hashlib.sha256(open(os.path.join(C, p), 'rb').read()).hexdigest()
    print(('OK   ' if got == h else 'FAIL ') + p)
    if got != h: sys.exit(1)
ALPHA = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'          # 25 letters, no J
KEY = {i + 2: ch for i, ch in enumerate(ALPHA)}
out = []
for line in open(os.path.join(D, 'transcription.txt'), encoding='utf-8'):
    if line.startswith('#') or not line.strip(): continue
    words = []
    for tok in line.replace('-', ' ').split():
        punct = '!' if '!' in tok else ''
        w = ''
        for n in tok.replace('!', '').strip('.').split('.'):
            dbl = n.endswith('='); n = n.rstrip('=x')
            ch = KEY[int(n)]
            w += ch * (2 if dbl else 1)
        words.append(w + punct)
    out.append(' '.join(words))
print('\n'.join(out))
