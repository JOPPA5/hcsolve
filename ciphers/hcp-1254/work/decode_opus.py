"""HCP1254: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1254/work/decode_opus.py"""
import hashlib, os, sys, unicodedata
W = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(W, '..')
P = 'work/hires/cpc_1912-03-27_HU__HU_Jasz-Arokszalas_jolanka-13_'
HASH = {'source/picture-large.jpg': '355de84cfd552607c210441c85db9a2455d1b395a1a02e8233d185ebed95b1ca',
        'source/address-large.jpg': '3382db362052ce703242a2c01fead9a31d5b2a576bd9971838a080a0f21325cb',
        P + 'pic.jpg': '2e57a67c4ca2846ada67ccae7bf19d3631e1aa0e48b7284feb738f5ece92421e',
        P + 'adr.jpg': 'cd4f2c9ed162dd7eff2e9c57ab0be2d7f490581ea7067ac543f86b0f16d3bf6d'}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f)
    if got != h: sys.exit(1)
KEY = {'F': 'r', ')': 's', 'X': 'u', '6': 'b', 'GY': 'gy', 'CS': 'cs', 'XX': '[deleted]',
       '?+': '{+}', 'J?': '{j?}'}
MARK = {'diaeresis': '̈'}
def dec(tok):
    base, _, acc = tok.partition(':')
    s = KEY.get(base, base.lower() if base.isalpha() else None)
    if s is None: raise SystemExit('unknown token ' + tok)
    return unicodedata.normalize('NFC', s + MARK[acc]) if acc else s
print('\nLiteral decipherment, one row per written line:')
for line in open(os.path.join(W, 'ledger-opus.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print('\nNormalized Hungarian (editorial word division, accents, [ ] supplied letters; see SOLUTION.md):')
print(open(os.path.join(W, 'normalized-opus.txt'), encoding='utf-8').read())
