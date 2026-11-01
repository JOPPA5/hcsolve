"""HCP1271: verify image hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1271/work/decode.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
B = 'work/hires/cpc_1912-03-16_HU__HU_Jasz-Arokszalas_jolanka-10_'
HASH = {'source/picture-large.jpg': 'c9a3d1cfede92a4e308241ed2396f14f586c7b464e0edf0e6a3accd7e7d2b551',
        B + 'pic.jpg': 'bf0b67ad7c84ed388c4c48fe08c44ac506831fd55daa4a743db33bfbffb37459',
        'source/address-large.jpg': '1e5d364478c23770fcf5c9703fb51a2ee32581d3793426de4345da40d3153534',
        B + 'adr.jpg': '895f04b9c2db9bd8ec02086b4b23b0a1124f8348e6e84a0801fc3a13d7e81c7b'}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f)
    if got != h: sys.exit(1)
KEY = {'F': 'r', ')': 's', 'X': 'u', '6': 'b', 'H': 'h', '/': 'd', 'GY': 'gy', 'CS': 'cs'}
def dec(t):
    res = t.endswith('!'); t = t.rstrip('!')
    base, _, acc = t.partition(':')
    s = KEY.get(base, base.lower() if base.isalpha() else None)
    if s is None: raise SystemExit('unknown token ' + t)
    if acc: s = unicodedata.normalize('NFC', s + '̈')
    return f'[{s}]' if res else s
n = 0
print('\nLiteral decipherment ([x] = blotted sign restored by word sense; h = the h/p sign):')
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split(); n += len(toks)
    print(f'{lab} ' + ''.join(dec(t) for t in toks))
print(f'\n{n} signs. Plain between rows 9 and 10: Gyöngyös Püspöki')
print('\nNormalized Hungarian (editorial):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
