#!/usr/bin/env python3
"""hcp-1197: number substitution A=1 ... I=9, K=10 ... Z=25 (no J). Run from repo root:
   python3 -I ciphers/hcp-1197/work/decode.py"""
import hashlib, os, re, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASHES = {
 'source/picture-large.jpg': 'a11b1f2b660704df428ac001956be22ef3f7f28044383c6132913c305045981b',
 'source/address-large.jpg': '47a4d1054048731f3db9b243a3101a20da1b70629a967aaa8d3a84dd59af3a73',
 'work/hires/cpc_1899-02-14_DE_Frankfurt-Sachsenhausen_DE___pic.jpg': '45f844bb77bed0e718cf61dee5a8b7115bd62ba71e2bf3295346fd8ec0742161',
 'work/hires/cpc_1899-02-14_DE_Frankfurt-Sachsenhausen_DE___adr.jpg': '6803b2b4dd9ef0efa4899f9f93e3a08e058068db3a16d3a24e03bbc4da3919e7',
}
for p, h in HASHES.items():
    got = hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest()
    print(('OK   ' if got == h else 'FAIL ') + p)
    if got != h: sys.exit(1)
ALPHA = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # J omitted: A=1 ... I=9, K=10 ... Z=25
KEY = {i + 1: c for i, c in enumerate(ALPHA)}
text = ''.join(l for l in open(os.path.join(D, 'work/transcription.txt'), encoding='utf-8') if not l.startswith('#'))
out = []
for tok in re.findall(r'\d+(?:\[\d\])?|-|\|', text):
    if tok == '-': out.append(' '); continue
    if tok == '|': out.append(' / '); continue
    restored = '[' in tok
    n = int(tok.replace('[', '').replace(']', ''))
    out.append(KEY[n].lower() if restored else KEY[n])
print('Ciphertext :', ' '.join(text.split()))
print('Plaintext  :', ''.join(out), '  (lower case = restored under stamp)')
print('German     : Liebe Grüße an: DEINEN GELIEBTEN BRÄUTIGAM')
