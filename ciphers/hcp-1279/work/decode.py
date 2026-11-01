"""HCP1279: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1279/work/decode.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/picture-large.jpg': '8d8d61fd73f16126a1f058efdbf5d5682ea1c4411777f87c769ae58cc793ea89',
        'source/address-large.jpg': 'd733640a90b53377ee406aff847c78764a0118e1d38d8e7aacab1a18c0c5cf9c',
        'work/hires/cpc_1914-04-12_HU__HU_Jasz-Arokszalas_jolanka-53_adr.jpg': '3bc0c1d93d60199e9ae2b1fc912f4e1897e33a0ce283c3b835995c2a8342219a'}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f)
    if got != h: sys.exit(1)
KEY = {'F': 'r', ')': 's', 'X': 'u', '6': 'b', '+': 'f', 'H': 'h', 'CS': 'cs', '*': '{x}', 'AE': '{a|e}', 'OI': '{o|i}', 'NH': '{n|h}'}
OK = set('ACDEGIJKLMNOTVYZ')
def dec(tok):
    if tok.startswith('['): return '[' + dec(tok[1:-1]) + ']'
    base, _, acc = tok.partition(':')
    if base in KEY: s = KEY[base]
    elif base in OK: s = base.lower()
    else: raise SystemExit('unknown token ' + tok)
    return unicodedata.normalize('NFC', s + {'d': '̈', 'a': '́', '': ''}[acc])
n = 0
print('\nLiteral decipherment, one row per written line (h stands for the h/p sign):')
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split(); n += len(toks)
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print(f'\n{n} signs. Normalized Hungarian (editorial; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
