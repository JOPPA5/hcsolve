#!/usr/bin/env python3
"""hcp-1377: verify source hashes, apply Caesar -1 to the transcription. Run from repo root."""
import hashlib, json, os, sys
D = 'ciphers/hcp-1377'
H = {'source/picture-large.jpg': '1709792f5c89da8f8e37affbfd5cea41041dc4b91002fc2ad08386cc5a946db0',
     'source/address-large.jpg': 'aa1d8b46317d46e84e5dd9b4c292e632cb085430d240b07530d056d99b9392a2',
     'work/hires/pc_hcp_58_pic.JPG': 'c3223bee7b92f515567b4fb187f46a5eef07fe73a39750bf3a9c03dabd2f8f98',
     'work/hires/pc_hcp_58_adr.JPG': '8e8ae4cfd44b326ee1630678ae320b2ce2dce149d2c4626108a6eb1605441ff6'}
for f, h in H.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    if got != h: sys.exit(f'HASH MISMATCH {f}')
print('source hashes OK')
def shift(s, k):
    return ''.join(chr((ord(c) - b + k) % 26 + b) if c.isascii() and c.isalpha() else c
                   for c in s for b in [65 if c.isupper() else 97])
T = json.load(open(os.path.join(D, 'work/transcription.json')))
print('[plain heading]', T['heading_plain'])
n = 0
for row in T['rows']:
    out = []
    for kind, tok in row:
        if kind == 'c':
            p = shift(tok, -1); assert shift(p, 1) == tok
            n += sum(c.isalpha() for c in tok); out.append(p.upper())
        else:
            out.append('[' + tok + ']')
    print(' '.join(t for _, t in row).ljust(36), '=>', ' '.join(out))
print('enciphered letters decoded:', n)
