"""HCP1242: check source hashes, decode the sign ledger. Run from repo root: python3 -I ciphers/hcp-1242/work/decode.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/picture-large.jpg': '5173e2c63341b082d276c42c293c4e8d5c6b8aac50d3615519897425ba453118',
        'source/address-large.jpg': '6514e0f269c7db1297727844e7b05f5e59ddb166ba169622e6668ea642207003'}
for f, h in HASH.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
KEY = {'F': 'r', ')': 's', 'X': 'u', '6': 'b', '+': 'f', 'H': 'h', 'P': 'p', 'GY': 'gy', 'CS': 'cs', '[s]': '[s]', '[u]': '[u]'}
MARK = {'diaeresis': '̈', 'double-acute': '̋'}
def dec(t):
    b, _, a = t.partition(':')
    s = KEY.get(b, b.lower() if b.isalpha() else None)
    if s is None: raise SystemExit('unknown token ' + t)
    return unicodedata.normalize('NFC', s + MARK[a]) if a else s
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if line.strip() and not line.startswith('#'):
        lab, *toks = line.split()
        print(lab, ''.join(dec(t) for t in toks))
print('\nNormalized (editorial):\n' + open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
