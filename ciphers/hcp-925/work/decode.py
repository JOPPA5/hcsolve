"""hcp-925: number substitution A=1 .. I=9, K=10 .. Z=25 (J omitted). Run from repo root:
   python3 -I ciphers/hcp-925/work/decode.py"""
import hashlib, os, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASHES = {
 'source/picture-large.jpg': 'b4bcaebc0ad4acd8eaf7d1b868ceb919650130921362dc2195d4e6d14926829f',
 'source/address-large.jpg': 'bf7070bc133a3a4ea0f31e886b8f4c7233940bee9abcbb9c03bec77313651055',
 'work/hires/cpc_1903-05-03_DE_Wollstein_DE_Volsheim__pic.jpg': '3aaa87a642db91f62f745121a7822b3dfeb9bd9ba6e385f96ec2fe12a16a7b26',
 'work/hires/cpc_1903-05-03_DE_Wollstein_DE_Volsheim__adr.jpg': 'ab33bc3168f070a72e080bc2d74d917af9bb41d4594d8e4d7d78fa2cc8b3773e',
}
ok = True
for p, h in HASHES.items():
    got = hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + p); ok &= got == h
ALPHA = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'   # no J
KEY = {i + 1: c for i, c in enumerate(ALPHA)}
out = []
for line in open(os.path.join(D, 'work/transcription.txt'), encoding='utf-8'):
    line = line.strip()
    if not line or line.startswith('#'): continue
    tag = ''
    if line.startswith('CIRCLED '): tag, line = '(circled) ', line[8:]
    nums = [int(x) for x in line.replace('|', '.').split('.')]
    txt = ''.join(KEY[n] for n in nums)
    print(f'{tag}{line:60s} -> {txt}'); out.append(txt)
print('\nFULL:', ''.join(out))
sys.exit(0 if ok else 1)
