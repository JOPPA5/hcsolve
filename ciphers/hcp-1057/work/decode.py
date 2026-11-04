"""Decode hcp-1057. Run from repo root:
   python3 -I ciphers/hcp-1057/work/decode.py
Checks source hashes, then maps digits to letters (all other letters are plain)."""
import hashlib, os, re, sys
D = os.path.dirname(os.path.abspath(__file__))
C = os.path.dirname(D)
HASHES = {
 'source/picture-large.jpg': '66f6b4dd79eb20b40c280690b055e9d221b61901d8348e66d4368b74139a3e80',
 'source/address-large.jpg': '6d47883cc72e497f978447dcaac40eb846d6d19c37a0a0f311fb046c6d2980a9',
 'work/hires/cpc_1917-07-12_DE_lendorf_DE_Erbenschwang_zwick-01_pic.jpg': '2f2dc9ece8825effb8f83d69cc873a189f95e7c102ff9bfb9b19cacf7c650c7e',
 'work/hires/cpc_1917-07-12_DE_lendorf_DE_Erbenschwang_zwick-01_adr.jpg': 'e31241c14b066700fa41790adb7942d5b4b44831f4e954e271cb873f0b92ce6c',
}
ok = True
for p, h in HASHES.items():
    got = hashlib.sha256(open(os.path.join(C, p), 'rb').read()).hexdigest()
    print(('OK   ' if got == h else 'FAIL ') + p); ok &= got == h
if not ok: sys.exit('hash mismatch')
KEY = {'1':'a','2':'e','3':'i','4':'o','5':'u','6':'l','7':'n','8':'m','9':'r','0':'s'}
print('\nKey: ' + ' '.join(f'{k}={v}' for k, v in sorted(KEY.items())))
print()
for line in open(os.path.join(D, 'transcription.txt'), encoding='utf-8'):
    if line.startswith('#') or not line.strip(): continue
    t = line.rstrip('\n').replace('1"', 'ä').replace('[h]', 'h')
    print(f'{line.rstrip():32s} -> ' + ''.join(KEY.get(c, c) for c in t))
