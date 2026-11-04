"""Decode hcp-1010. Run from repo root: python3 -I ciphers/hcp-1010/work/decode.py"""
import hashlib, os, re, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
H = {'source/picture-large.jpg': '4409a658d0b5aaeb2382846badf95832ff86a0cf3a0c4dcd6e90eaeb01c11808',
     'source/address-large.jpg': 'c96cc5d73cbe1fb2a5a687cb3643d5aa38bc225b982f18770605372aadecdaa7',
     'work/hires/cpc_--_DE__DE_Hier__pic.jpg': '4f6428559ecfa4d06810cd64f5fc5cbe47a216d069c6a7961b7a52045e2b3c3a'}
for p, h in H.items():
    got = hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest()
    print(('OK   ' if got == h else 'FAIL ') + p); 
    if got != h: sys.exit(1)
# Key: A-M (J omitted) = 1..12 ascending, N-Z = 25..13 descending.
first = 'ABCDEFGHIKLM'; second = 'NOPQRSTUVWXYZ'
KEY = {i + 1: c for i, c in enumerate(first)}
KEY.update({25 - i: c for i, c in enumerate(second)})
print('key:', ' '.join(f'{n}={KEY[n]}' for n in sorted(KEY)))
for line in open(os.path.join(D, 'work/transcription.txt')):
    if line.startswith('#') or not line.strip(): continue
    tag, body = line.split(':', 1)
    out = []
    for word in body.split('|'):
        w = ''
        for tok in word.split():
            if tok == '.': w += '.'; continue
            uml = tok.endswith(':') and tok != ':'
            n = int(re.sub(r'[^0-9]', '', tok))
            c = KEY[n]
            if uml: c = {'A': 'Ä', 'U': 'Ü', 'O': 'Ö'}[c]
            if '[' in tok: c = c.lower()
            w += c
        out.append(w)
    print(tag + ':', ' '.join(out))
print('(lowercase = restored letter: hidden by stamp/damage/shading, or read on word sense)')
