"""HCP1248: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1248/work/decode.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
H = {'source/picture-large.jpg': 'd6a95710d408e45019621f6f7c84804a3682d3034a09f1766755244c0bfd640b',
     'source/address-large.jpg': 'd8a1ffb6de3848a68b17f68fb89c605000f9e1b482e21bc7d5f0a8a0375ed6f0',
     'work/hires/cpc_1913-09-13_HU__HU_Jasz-Arokszalas_jolanka-43_pic.jpg': '7164816d8a19b7f05d421bc99f4316ebc64c8bd540048fac44925ed63a8de4ad',
     'work/hires/cpc_1913-09-13_HU__HU_Jasz-Arokszalas_jolanka-43_adr.jpg': 'b99d2ca47320e4381492e742e53dca00d03f19b7fa565f86e9afad496495b14a'}
for f, h in H.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
KEY = {'F': 'r', ')': 's', '6': 'b', '+': 'f', 'H': 'h', 'CS': 'cs', 'BLOT': '[blot]', 'DOT': '.'}
MARK = {'d': '̈', 'a': '́', 'da': '̋'}
def dec(t):
    if t.startswith('#'): return '<' + t[1:] + '>'
    base, _, m = t.partition(':')
    s = KEY.get(base, base.lower() if base.isalpha() else None)
    if s is None: raise SystemExit('unknown token ' + t)
    return unicodedata.normalize('NFC', s + MARK[m]) if m else s
n = 0
print('\nLiteral decipherment, one row per written line (h stands for the h/p sign):')
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split(); n += len(toks)
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print(f'\n{n} signs. Normalized Hungarian (editorial; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
