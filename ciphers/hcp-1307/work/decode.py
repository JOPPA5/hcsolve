"""HCP1307: check source hashes, decode the sign ledger, print the plaintext. From repo root:
   python3 -I ciphers/hcp-1307/work/decode.py"""
import hashlib, os, sys, unicodedata
W = os.path.dirname(os.path.abspath(__file__)); D = os.path.dirname(W)
H = {'source/picture-large.jpg': '5ecce2e7a01fa57a961ecf2cc7225c0a603e75bff63e64992e89355d3b6a8e12',
     'source/address-large.jpg': 'e65978e55b59be52b173a9f360fa321d5a5aa64c74a45e842450f40bc1670df1',
     'work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-79_pic.jpg': 'd60f331d849d958b7e48b07cb8cfb9d06fce8267c9396537f93c233c70433ee3',
     'work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-79_adr.jpg': 'b7bb6cc962fd7356fc57fcd72f39aa3b306ff4fd608646e1b35f9d2c86f78ed7'}
for f, h in H.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
KEY = {'=': 'a', '6': 'b', '()': 'cs', '%': 'd', 'E': 'e', '+': 'f', 'G': 'g', 'H': 'h', '@': 'i', 'J': 'j',
       'K': 'k', '~': 'l', '3': 'm', '2': 'n', 'O': 'o', 'R': 'r', ')': 's', 'T': 't', 'X': 'u', 'V': 'v', 'Y': 'y', 'Z': 'z'}
MARK = {"'": '́', ':': '̈'}
def dec(tok):
    t = tok.rstrip('*?^'); flags = tok[len(t):]
    acc = ''
    if t[-1] in MARK and len(t) > 1: acc = MARK[t[-1]]; t = t[:-1]
    if t not in KEY: raise SystemExit('unknown token ' + tok)
    s = unicodedata.normalize('NFC', KEY[t] + acc)
    return '[' + s + ']' if '^' in flags else s
n = 0
print('\nLiteral decipherment, one row per written line (h stands for the h/p sign):')
for line in open(os.path.join(W, 'ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split(); n += len(toks)
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print(f'\n{n} signs decoded, none without a value.')
print('\nNormalized Hungarian (editorial word division, accents and spelling; see SOLUTION.md):')
print(open(os.path.join(W, 'normalized.txt'), encoding='utf-8').read())
