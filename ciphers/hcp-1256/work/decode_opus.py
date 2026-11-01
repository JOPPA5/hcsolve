"""HCP1256: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1256/work/decode_opus.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/picture-large.jpg': '5cfa5b678db9ae59bbf996b6d57589bd05a3ebcf73c65565471bb4f01e481fb0',
        'source/address-large.jpg': '5aaac96110f9ede146b88b935e3b8bd191f309415eca37a89409a27b8edba92d',
        'work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-68_pic.jpg': 'bafb87bac85c3f270a6d9b3bb2dee267e71508a4e4b611031ca0505ab55c1cea',
        'work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-68_adr.jpg': '2f4aa3646b7225df66ca963cd973e1692752f1c676e6f00f0bb5c89fc34d44b3'}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f)
    if got != h: sys.exit(1)
KEY = {'F': 'r', ')': 's', 'X': 'u', '6': 'b', '+': 'f', 'H': 'h', 'A/E': '{a/e}', '?': '{?}', '-': '{-}'}
def dec(tok):
    if tok.startswith('['): return '[' + dec(tok[1:-1]) + ']'
    base, _, acc = tok.partition(':')
    s = KEY.get(base, base.lower() if base.isalpha() else None)
    if s is None: raise SystemExit('unknown token ' + tok)
    return unicodedata.normalize('NFC', s + '̈') if acc else s
print('\nLiteral decipherment, one row per written line (h stands for the h/p sign):')
for line in open(os.path.join(D, 'work/ledger-opus.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print('\nNormalized Hungarian (editorial word division, accents and spelling; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized-opus.txt'), encoding='utf-8').read())
