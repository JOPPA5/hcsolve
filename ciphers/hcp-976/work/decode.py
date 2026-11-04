"""hcp-976: decode the number-substitution card. Run from repo root:
   python3 -I ciphers/hcp-976/work/decode.py
"""
import hashlib, os, re, sys
D = os.path.dirname(os.path.abspath(__file__))
C = os.path.dirname(D)
HASHES = {
 'source/picture-large.jpg': '54debf0e5345d401e4468a23a84378a5e58595ba2059bdc6830107a7a7e2f6eb',
 'source/address-large.jpg': 'f8de1c8ff813a0b60ad15181f6c42e0e1ca6d9bb4b36a2715f88a0c29ad471b4',
 'work/hires/cpc_1910-03-21_DE_Bruckenau_DE_Heidelberg_heidelberg-01_pic.jpg': '162953a0f395cfdd4150429f22edc5f5a233fc606a78c252b99490a74d2d3b94',
 'work/hires/cpc_1910-03-21_DE_Bruckenau_DE_Heidelberg_heidelberg-01_adr.jpg': '3cdc991c7955f6002ee4087bd9af6491078ea1484fc609d1712d597ef39a3253',
}
for p, h in HASHES.items():
    got = hashlib.sha256(open(os.path.join(C, p), 'rb').read()).hexdigest()
    if got != h:
        sys.exit(f'hash mismatch: {p}')
print('source hashes OK')
# key: vowels a e i o u -> 1..5, then l m n r s -> 6 7 8 9 0
KEY = {'1':'a','2':'e','3':'i','4':'o','5':'u','6':'l','7':'m','8':'n','9':'r','0':'s'}
def dec(line):
    out, i = [], 0
    while i < len(line):
        ch = line[i]
        if ch == '{':
            j = line.index('}', i); out.append(line[i+1:j]); i = j+1; continue
        if ch == '[':
            j = line.index(']', i); i = j+1; continue
        if ch in KEY:
            if line[i+1:i+2] == '^':
                out.append({'5':'ü'}[ch]); i += 2; continue
            out.append(KEY[ch]); i += 1; continue
        out.append(ch); i += 1
    return ''.join(out)
lines = []
for raw in open(os.path.join(D, 'transcription.txt'), encoding='utf-8'):
    raw = raw.rstrip('\n')
    if not raw or raw.startswith('#'):
        continue
    lines.append(raw[1:] if raw.startswith('@') else dec(raw))
print('\n'.join(lines))
text = ' '.join(lines).replace('/ ', '')
text = text
print('\nRunning text:\n' + re.sub(r'\s+', ' ', text))
