"""Decode hcp-910. Run from repo root:
   python3 -I ciphers/hcp-910/work/decode.py
Checks source hashes, then maps digits to letters (all other letters are plain)."""
import hashlib, os, sys
D = os.path.dirname(os.path.abspath(__file__))
C = os.path.dirname(D)
HASHES = {
 'source/address-large.jpg': '916374218afacfaa0b659799254ea487bd49cc5c0bc3a67177c500dd7928d941',
 'source/picture-large.jpg': '8f1dc2baa36cb13244087fc8e537f96adcdb91764850fa744fe1a055c9e5ddf7',
 'work/hires/cpc_1917-08-03_DE_Ulm_DE_Erbenschwang_zwick-02_adr.jpg': 'a790c03ca28645fbcda20176f572cf32e9ded1eb7784932f9dc18f17aa137d46',
 'work/hires/cpc_1917-08-03_DE_Ulm_DE_Erbenschwang_zwick-02_pic.jpg': 'eafef9863e23c6130f52d123e176122abe7964e84b203839d51a68525bed514e',
}
ok = True
for p, h in HASHES.items():
    got = hashlib.sha256(open(os.path.join(C, p), 'rb').read()).hexdigest()
    print(('OK   ' if got == h else 'FAIL ') + p); ok &= got == h
if not ok:
    sys.exit('hash mismatch')
KEY = {'1': 'a', '2': 'e', '3': 'i', '4': 'o', '5': 'u', '6': 'l', '7': 'n', '8': 'm', '9': 'r', '0': 's'}
UML = {'1"': 'ä', '4"': 'ö', '5"': 'ü'}
print('\nKey: ' + ' '.join(f'{k}={v}' for k, v in sorted(KEY.items())) + '\n')
out = []
for line in open(os.path.join(D, 'transcription.txt'), encoding='utf-8'):
    line = line.rstrip('\n')
    if line.startswith('#') or not line.strip():
        continue
    if line.startswith('PLAIN: '):
        print(f'{"(plain)":28s} -> {line[7:]}'); out.append(line[7:]); continue
    t = line
    for a, b in UML.items():
        t = t.replace(a, b)
    dec = ''.join(KEY.get(c, c) for c in t)
    print(f'{line:28s} -> {dec}'); out.append(dec)
print('\nRunning text:\n' + ' '.join(out))
