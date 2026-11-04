"""hcp-1060: decode the number block. Run from repo root: python3 -I ciphers/hcp-1060/work/decode.py"""
import hashlib, os, re, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
H = {'source/picture-large.jpg': 'b2f53edee3505a543349fa25c24595556701cddb0d33ee8b665e39aba5b05b8f',
     'source/address-large.jpg': '6dab395fff6699d93db63212ccd187a261b7627e18b8bde771cac4ce322d74a6',
     'work/hires/cpc_1911-11-23_DE_Schweidnitz_DE_Hier_fritzlehmann-15_adr.jpg': '1928297de0590535a6e6f86b5d6c1e52dd39d9118eeab9e85c67ff1ea4a347ca'}
for p, h in H.items():
    got = hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + p)
    if got != h: sys.exit(1)
ALPHA = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'          # 25 letters without J, A = 2
KEY = {i + 2: c for i, c in enumerate(ALPHA)}
out = []
for line in open(os.path.join(D, 'work/transcription.txt'), encoding='utf-8'):
    if line.startswith('#') or not line.strip(): continue
    words = []
    for w in re.split(r'\s+-\s*|\s+-$', line.strip()):
        w = w.strip(' -')
        if not w: continue
        s = ''
        for tok in w.split('.'):
            m = re.fullmatch(r'(\d+)(["\']?)', tok)
            ch = KEY[int(m.group(1))]
            s += {'A': 'Ä', 'O': 'Ö', 'U': 'Ü'}[ch] if m.group(2) == '"' else ch + ("'" if m.group(2) == "'" else '')
        words.append(s)
    out.append(' '.join(words))
print('\n'.join(out))
