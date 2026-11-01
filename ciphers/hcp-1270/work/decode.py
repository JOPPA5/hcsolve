"""HCP1270: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1270/work/decode.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/picture-large.jpg': 'd958b4c7c5fbf755585d9c6bbc67049116dd8585889b4024d5b6ae16972e94cd',
        'source/address-large.jpg': '92dbf1652f3d0440665aa5cc7c7662f7d52ac5efddc4724ccee9aaabd7e8cb34',
        'work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-72_pic.jpg': 'dc2d9bc1f1676424d400210aced2e94d1cf54e7efbafe895825f9060033cfc92',
        'work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-72_adr.jpg': '278000e582fc8d2be0b1a6f2182d5ed66b10131a9883444b3614c111c3523238'}
for f, h in HASH.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
KEY = {'F': 'r', ')': 's', 'X': 'u', '6': 'b', '+': 'f', 'H': 'h', 'CS': 'cs', '#': '', '|': ''}
def dec(tok):
    base, _, mark = tok.partition(':')
    hidden = base.startswith('[')
    base = base.strip('[]')
    s = KEY.get(base, base.lower() if base.isalpha() else None)
    if s is None: raise SystemExit('unknown token ' + tok)
    if mark: s = unicodedata.normalize('NFC', s + '̈')
    return '[' + s + ']' if hidden else s
print('\nLiteral decipherment, one row per written line (h stands for the h/p sign; [x] = damaged sign):')
n = 0
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split(); n += len(toks)
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print(f'\n{n} signs')
print('\nNormalized Hungarian (editorial; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
