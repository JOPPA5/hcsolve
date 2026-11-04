"""hcp-979: number substitution, A=2 ... I=10, J omitted, K=11 ... Z=26 (key of Lehmann sister cards hcp-1134/1113/1045).
Run from repo root: python3 -I ciphers/hcp-979/work/decode.py"""
import hashlib, os, sys
D = os.path.dirname(os.path.abspath(__file__)); C = os.path.dirname(D)
H = {'source/address-large.jpg': '33385d0f797ee47a57f916ad992d3a86b16eb231dea877ad79b537c2d12ef65b',
     'source/picture-large.jpg': '205798713f0bee0ffa3abb8efdebed110c7eb54385d7a46cce2bb7253f77db2a',
     'work/hires/cpc_1909-09-10_DE_Dortmund_DE_Hier_fritzlehmann-08_adr.jpg': '91c1191dcd8739baf109190cce314bff036a5ffede144eecd7c67191a4d58f2f',
     'work/hires/cpc_1909-09-10_DE_Dortmund_DE_Hier_fritzlehmann-08_pic.jpg': '7fc3d701a2719390adbc582755719dc41f19ced6ab12105d26e6b37b0c503eb9'}
for p, h in H.items():
    got = hashlib.sha256(open(os.path.join(C, p), 'rb').read()).hexdigest()
    print(('OK   ' if got == h else 'FAIL ') + p)
    if got != h: sys.exit(1)
ALPHA = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'          # 25 letters, no J
KEY = {i + 2: ch for i, ch in enumerate(ALPHA)}
out = []
for line in open(os.path.join(D, 'transcription.txt'), encoding='utf-8'):
    if line.startswith('#') or not line.strip(): continue
    lit = ''
    if '[' in line:
        line, lit = line.split('[', 1); lit = lit.rstrip().rstrip(']')
    words = []
    for tok in line.replace('-', ' ').split():
        if tok == '!': words.append('!'); continue
        words.append(''.join(KEY[int(n.rstrip('x'))] for n in tok.strip('.').split('.')))
    if lit: words.append(lit)
    out.append(' '.join(words))
print('\n'.join(out))
print('\nRunning text:', ' '.join(out))
