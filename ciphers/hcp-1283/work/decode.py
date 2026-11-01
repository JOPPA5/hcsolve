"""HCP1283: check source hashes, decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1283/work/decode.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/picture-large.jpg': '1b0fb551604798cb70dd80ed7827d5293f592e232fb235e9abe74d8c154faf1c',
        'source/address-large.jpg': '46ed28e7f0615aceea42e6107848602b612a403bfa8e9dd4bf42bccadd56b52c',
        'work/hires/cpc_1913-03-20_HU__HU_Jasz-Arokszalas_jolanka-34_pic.jpg': '7e938a417d75961ad5efac6d00638b646c4ca1573420aa3b418d610bcf7f1189',
        'work/hires/cpc_1913-03-20_HU__HU_Jasz-Arokszalas_jolanka-34_adr.jpg': '1b3c82ecc756be75de54af54d60acc9147146da18c40b2e00d9210d8db1b92de'}
for f, h in HASH.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
KEY = {'F': 'r', ')': 's', 'X': 'u', '6': 'b', '+': 'f', 'CS': 'cs'}
MARK = {'a': '́', 'd': '̈'}
def dec(t):
    if t.startswith('['): return '[' + dec(t[1:-1]) + ']'
    base, _, m = t.partition(':')
    s = KEY.get(base, base.lower())
    return unicodedata.normalize('NFC', s + MARK[m]) if m else s
print('\nLiteral decipherment by written row:')
n = 0
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split(); n += sum(t not in ',.' for t in toks)
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print(f'\n{n} signs. Normalized Hungarian (editorial; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
