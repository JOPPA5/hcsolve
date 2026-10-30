"""HCP1317: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1317/work/decode.py"""
import hashlib, os, sys, unicodedata
W = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(W, '..')
HASH = {'source/picture-large.jpg': 'c79c8da79700169d6c271726da6e413a974cf4588235f249dc8f2c381bdd278e',
        'source/address-large.jpg': 'ce21d18b0b1eeb1ec4f25d70f5653f75e0c302486677863c19b45140699877e2',
        'work/hires/cpc_1913--_HU__HU_Jasz-Arokszalas_jolanka-110_pic.jpg': 'd49812f4045ed568cd016e853497df361c53c5e85e4f48f6bbe652e5e27834fa',
        'work/hires/cpc_1913--_HU__HU_Jasz-Arokszalas_jolanka-110_adr.jpg': '7726daded854be7c95f37bf20d71a0af58dda06399606d55daed34818fe051cd'}
for f, h in HASH.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
KEY = {'F': 'r', 'Fc': 'r', ')': 's', 'X': 'u', '+': 'f', 'T+': 't', 'CS': 'cs', 'H': 'h'}
def dec(tok):
    hid = tok.startswith('[')
    tok = tok.strip('[]')
    base, _, acc = tok.partition(':')
    s = KEY.get(base, base.lower() if base.isalpha() else None)
    if s is None: raise SystemExit('unknown token ' + tok)
    if acc: s = unicodedata.normalize('NFC', s + '̈')
    return f'[{s}]' if hid else s
print('\nLiteral decipherment, one row per written line (h stands for the h/p sign; [ ] = restored, hidden by the stamp tear):')
n = 0
for line in open(os.path.join(W, 'ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *t = line.split(); n += len(t)
    print(f'{lab:>3} ' + ''.join(dec(x) for x in t))
print(f'\n{n} signs decoded.\n\nNormalized Hungarian (editorial; see SOLUTION.md):')
print(open(os.path.join(W, 'normalized.txt'), encoding='utf-8').read())
