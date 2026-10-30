"""HCP1288: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1288/work/decode.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
H = {'source/address-large.jpg': 'c687b6fdb65a3231f009266230ced422935eb950ef2f129360f6d865d275c519',
     'source/picture-large.jpg': '6c6d322ee645cf6c477a61e6310cd863924e527514bc142f5d5db2ae9be305b9',
     'work/hires/cpc_1913--13_HU__HU_Jasz-Arokszalas_jolanka-112_adr.jpg': 'eb08bf2919940258a9b53e5db352178370d50aad8471414f1d600f7681d20097',
     'work/hires/cpc_1913--13_HU__HU_Jasz-Arokszalas_jolanka-112_pic.jpg': '06a090463e8d52fda3164684865712a970f5c4ec57e199de3411efd505455a28'}
for f, h in H.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
KEY = {')': 's', 'X': 'u', '6': 'b', '+': 'f', 'CS': 'cs', '?': '{?}', '|': '{|}'}
MARK = {'diaeresis': '̈', 'acute': '́'}
def dec(t):
    b, _, a = t.partition(':')
    s = KEY.get(b, b.lower() if b.isalpha() else None)
    if s is None: sys.exit('unknown token ' + t)
    return unicodedata.normalize('NFC', s + MARK[a]) if a else s
n = 0
print('\nLiteral decipherment, one row per written line:')
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split(); n += len(toks)
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print(f'\n{n} written signs.\n\nNormalized Hungarian (editorial; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
