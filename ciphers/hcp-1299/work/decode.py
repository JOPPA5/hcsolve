"""HCP1299: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1299/work/decode.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
H = 'work/hires/cpc_-12-03_HU__HU_Jasz-Arokszalas_jolanka-96_'
HASH = {'source/picture-large.jpg': '8d50d8ff25045787ccfd0e555a8a9c2bbd942c3b22589eecd3e8dec51cbb53e2',
        'source/address-large.jpg': 'c0395fe3fb5f74d8bec019beab9f3640b3559c619e43d2d163ed00702fd74676',
        H + 'pic.jpg': '42ce8ccbbb5be449878dad055d23ffee8fc7868e1db5004e9b44bcb30cd8f018',
        H + 'adr.jpg': '43e5b64a66bfdfb90245e8ffedd2f29a98b21dbb7a56a9bc661f5ac8f7f61791'}
for f, h in HASH.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
KEY = {'=': 'a', '6': 'b', '(': 'c', 'CS': 'cs', '4': 'd', '#': 'e', '+': 'f', 'G': 'g', 'H': 'h', 'P': 'p',
       'i': 'i', 'T': 'j', 'S': 'k', '~': 'l', '3': 'm', '2': 'n', 'Q': 'o', 'F': 'r', ')': 's', 'L': 't',
       'X': 'u', '^': 'v', 'Y': 'y', 'Z': 'z'}
def dec(t):
    if t.startswith('['): return '[' + dec(t[1:-1]) + ']'
    if t.startswith('{'): return '{' + dec(t[1:-1]) + '}'
    if t.endswith(':'): return unicodedata.normalize('NFC', KEY[t[:-1]] + '̈')
    return KEY[t]
print('\nLiteral decipherment, one row per written line ([x] = blot-hidden sign, {x} = interlinear insertion):')
n = 0
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split(); n += len(toks)
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print(f'\nSigns: {n}')
print('\nNormalized Hungarian (editorial word division, accents and spelling; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
