"""hcp-978 partial decode with the Lehmann key (A=2..Z=26, no J). Run from repo root:
python3 -I ciphers/hcp-978/work/decode_partial.py"""
import os
D = os.path.dirname(os.path.abspath(__file__))
KEY = {i + 2: c for i, c in enumerate('ABCDEFGHIKLMNOPQRSTUVWXYZ')}
for line in open(os.path.join(D, 'transcription_partial.txt'), encoding='utf-8'):
    if line.startswith('#') or not line.strip(): continue
    words = []
    for tok in line.replace('-', ' ').split():
        w = ''
        for n in tok.strip('.').split('.'):
            q = '?' if '?' in n else ''; uml = '"' in n; dbl = '=' in n
            ch = KEY[int(n.strip('?"='))]
            if uml: ch = {'O': 'Ö', 'U': 'Ü', 'A': 'Ä'}.get(ch, ch)
            w += ch * (2 if dbl else 1) + q
        words.append(w)
    print(' '.join(words))
