"""HCP1260: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1260/work/decode.py"""
import hashlib, os, sys
W = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(W, '..')
HASH = {'source/picture-large.jpg': 'f57e7f7bfac0104519bf018010cd612063a27e538c2db342fbba72962b6db2fb',
        'source/address-large.jpg': '3629227d36ce9f1ecf3a4f4f308cbb77da4746011bb5afc9d53797a5b0adc85e',
        'work/hires/cpc_--25_HU__HU_Jasz-Arokszalas_jolanka-90_pic.jpg': '9a9dbdb0345e654edcfe9e5c59810aea5f9e93ed654bb1af233ba01526f414b0',
        'work/hires/cpc_--25_HU__HU_Jasz-Arokszalas_jolanka-90_adr.jpg': 'c31d7d97a38cb8ed2be62802cffba5afd6fcea0ecfcca274835c8a7bf96574fd'}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f)
    if got != h: sys.exit(1)
KEY = {'F': 'r', ')': 's', 'X': 'u', '6': 'b', '+': 'f', 'CS': 'cs', 'O': 'ö', 'OO': 'ő', 'U': 'ü', '7': '7'}
def dec(t):
    b = t.rstrip('?')
    s = KEY.get(b, b if len(b) == 1 and b.islower() else None)
    if s is None: raise SystemExit('unknown token ' + t)
    return s
print('\nLiteral decipherment, row by row (h = h/p sign class is resolved per sign; C = corner block):')
for line in open(os.path.join(W, 'ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *t = line.split()
    print(f'{lab} ' + ''.join(dec(x) for x in t))
print('\nNormalized Hungarian (editorial; see SOLUTION.md):')
print(open(os.path.join(W, 'normalized.txt'), encoding='utf-8').read())
