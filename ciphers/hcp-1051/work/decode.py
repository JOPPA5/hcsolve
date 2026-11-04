"""hcp-1051: number substitution (MASC), A=2 ... I=10, J omitted, K=11 ... Z=26 - same table as the Lehmann
sister cards hcp-1113 and hcp-1134. Checks source hashes, then decodes work/transcription.txt. Run from repo root:
python3 -I ciphers/hcp-1051/work/decode.py"""
import hashlib, os, sys
D = os.path.dirname(os.path.abspath(__file__)); C = os.path.dirname(D)
H = {'source/address-large.jpg': 'a0c136ca955b4d38b482c28237fa0265b93ba01750ed68d8b84a097131c3d7f7',
     'source/picture-large.jpg': '8dfe08ecf74acd076fd9c4c8633faebe09110391422b245701a776a1a996d1ba',
     'work/hires/cpc_1910-03-31_DE_Schweidnitz_DE_Schweidnitz_fritzlehmann-12_adr.jpg': '2fc40743aab1e3f7b12f620754f621d6eb8e693134e689244554e544a4209e75',
     'work/hires/cpc_1910-03-31_DE_Schweidnitz_DE_Schweidnitz_fritzlehmann-12_pic.jpg': 'dd4ae68474ff5a4b62b96c525e5899203ca94167808b648da26b17318dd3f421'}
for p, h in H.items():
    got = hashlib.sha256(open(os.path.join(C, p), 'rb').read()).hexdigest()
    print(('OK   ' if got == h else 'FAIL ') + p)
    if got != h: sys.exit(1)
ALPHA = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'          # 25 letters, no J
KEY = {i + 2: ch for i, ch in enumerate(ALPHA)}
out = []
for line in open(os.path.join(D, 'transcription.txt'), encoding='utf-8'):
    if line.startswith('#') or not line.strip(): continue
    words = [''.join(KEY[int(n)] for n in tok.strip('.').split('.'))
             for tok in line.replace('-', ' ').replace('/', ' ').split()]
    out.append(' '.join(words))
print('\n'.join(out))
print('\n' + ' '.join(out))
