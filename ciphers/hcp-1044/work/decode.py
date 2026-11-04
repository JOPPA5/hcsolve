"""hcp-1044: number substitution (MASC), A=2 ... I=10, J omitted, K=11 ... Z=26 (same table as the Lehmann
sister cards hcp-1051, 1113, 1134). '"' = umlaut written over the number. The writer put the umlaut over 14 (N)
where U-umlaut is meant (Kurrent n/u confusion); the decoder prints N" and, in the normalised line, Ü.
Checks source hashes, then decodes work/transcription.txt. Run from repo root: python3 -I ciphers/hcp-1044/work/decode.py"""
import hashlib, os, sys
D = os.path.dirname(os.path.abspath(__file__)); C = os.path.dirname(D)
H = {'source/picture-large.jpg': '8dc7592a252fd384ce0720da1124a49b6a150517e2b0450c57adcc1b0906b0b7',
     'source/address-large.jpg': 'b700bac4448ae285c1e2c5b64e5cd1bd89422e151391477283589b75a470d362',
     'work/hires/cpc_--___DE_Hier_fritzlehmann-16_pic.jpg': '27367fb19cb19a885994efa67b1206edcf535e8aa3f5958562b69e2cc6b336dd',
     'work/hires/cpc_--___DE_Hier_fritzlehmann-16_adr.jpg': '0286b8f6497aa28db1c7d4fc0a3b0364da5da23abc094f55f0ac75b43e6b6eb5'}
for p, h in H.items():
    got = hashlib.sha256(open(os.path.join(C, p), 'rb').read()).hexdigest()
    print(('OK   ' if got == h else 'FAIL ') + p)
    if got != h: sys.exit(1)
ALPHA = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'          # 25 letters, no J
KEY = {i + 2: ch for i, ch in enumerate(ALPHA)}
UML = {'A': 'Ä', 'O': 'Ö', 'U': 'Ü', 'N': 'Ü'}   # N" = writer's Ü (see docstring)
lit, norm = [], []
for line in open(os.path.join(D, 'transcription.txt'), encoding='utf-8'):
    if line.startswith('#') or not line.strip(): continue
    lw, nw = [], []
    for tok in line.replace('-', ' ').split():
        a = b = ''
        for n in tok.strip('.').split('.'):
            u = n.endswith('"'); ch = KEY[int(n.rstrip('"'))]
            a += ch + ('"' if u else ''); b += UML[ch] if u else ch
        lw.append(a); nw.append(b)
    lit.append(' '.join(lw)); norm.append(' '.join(nw))
print('\n'.join(lit))
print('\n' + ' '.join(norm))
