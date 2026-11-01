"""HCP1253: verify the image hashes and decode the sign ledger. Run from the repo root:
   python3 -I ciphers/hcp-1253/work/decode.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {
 'source/picture-large.jpg': '4b153a88cfcafab96f893a1d270316d509bb1230e2169614b47e45c3a8f9c5ff',
 'source/address-large.jpg': '4f3bcf69f4c65976473156e3236e52eed34c66eed319779ee658d650ae3965d0',
 'work/hires/cpc_1913-02-22_HU__HU_Jasz-Arokszalas_jolanka-33_pic.jpg': '3c5ead4d2f991229544b41771549b5c55be3589c2ef08adf2e3b0a784d747f6b',
 'work/hires/cpc_1913-02-22_HU__HU_Jasz-Arokszalas_jolanka-33_adr.jpg': '9164d966a73a795c29c032f90a6f0086318dd8d55a3cf215e18cb2066cd31267'}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f)
    if got != h: sys.exit(1)
KEY = {'F': 'r', ')': 's', '(': 's', '6': 'b', '+': 'f', 'X': 'u', 'H': 'h', 'D': 'd', 'GY': 'gy', 'CS': 'cs',
       '#': '{n}', 'CS?': '[cs]', 'D?': '{d}', 'T?': '{j|t}', 'I?': '{i}'}
MARK = {'diaeresis': '̈', 'double-acute': '̋', 'acute': '́'}
def dec(tok):
    base, _, acc = tok.partition(':')
    s = KEY.get(base, base.lower() if base.isalpha() else None)
    if s is None: raise SystemExit('unknown token ' + tok)
    return unicodedata.normalize('NFC', s + MARK[acc]) if acc else s
print('\nLiteral decipherment, one row per written line ({} = call on an unclear sign, [] = restored):')
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print('\nNormalized Hungarian (editorial word division, accents and spelling; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
