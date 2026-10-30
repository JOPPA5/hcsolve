"""HCP1306: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1306/work/decode.py"""
import hashlib, os, re, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/picture-large.jpg': '11466f5567166eafb1f9f92fe48cf5556e393552e8cca1f3a6989eb4356835e1',
        'source/address-large.jpg': '0b608c2ecb15aee29796f905630a4cfd78598bfdc8c4654afd0571e5aa55d835',
        'work/hires/cpc_1914-03-05_HU__HU_Jasz-Arokszalas_jolanka-49_pic.jpg': '0cf43077bca81760dec7bcd1888e4af0ce0f027096e6562d7c7b2aceb37e70eb',
        'work/hires/cpc_1914-03-05_HU__HU_Jasz-Arokszalas_jolanka-49_adr.jpg': '7c842d269d64fea849f54579043247ea4fa85c9e68e7533b9b19fca52396fa88'}
for f, h in HASH.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
KEY = {'F': 'r', ')': 's', 'X': 'u', '6': 'b', '+': 'f', 'H': 'h', 'CS': 'cs', '/': '/', '?': '?'}
def dec(t):
    if t.startswith('{'): return t
    base, _, m = t.partition(':')
    s = KEY.get(base, base.lower())
    return s + ('̈' if m == 'd' and s in 'ou' else '')
n = 0
print('\nLiteral decipherment (h = h/p sign; / = reduced d or h; {a|b} = undecided shape):')
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *t = line.split(); n += len(t)
    print(f'{lab:>3} ' + ''.join(dec(x) for x in t))
print(f'\n{n} signs in the ledger.')
print('\nNormalized Hungarian (editorial, PARTIAL; see SOLUTION.md):\n')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
