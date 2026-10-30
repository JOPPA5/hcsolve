"""HCP1216: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1216/work/decode_opus.py"""
import hashlib, os, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/address.jpg': 'bbd77446dd58ebe11db31925d119b25f4a83941ec0f0110c29e4367456b82d0d',
        'source/picture.jpg': '2cd95e317d7bc03f81a2b3bb3031198c20d2ad1a1a134771c0dc37da1c56bcc8'}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f); 
    if got != h: sys.exit(1)
KEY = {'F': 'r', ')': 's', 'X': 'u', '6': 'b', '+': 'f', 'H': 'h', 'GY': 'gy', 'CS': 'cs',
       'M?': '{m|n}', '/': 'd', '|': '{|}'}
MARK = {'diaeresis': '̈', 'double-acute': '̋', 'acute': '́'}
def dec(tok):
    base, _, acc = tok.partition(':')
    s = KEY.get(base, base.lower() if base.isalpha() else None)
    if s is None: raise SystemExit('unknown token ' + tok)
    import unicodedata
    return unicodedata.normalize('NFC', s + MARK[acc]) if acc else s
rows = []
for line in open(os.path.join(D, 'work/ledger-opus.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    rows.append((lab, ''.join(dec(t) for t in toks)))
print('\nLiteral decipherment, one row per written line (h stands for the h/p sign):')
for lab, txt in rows: print(f'{lab:>3} {txt}')
print('\nNormalized Hungarian (editorial word division, accents and spelling; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized-opus.txt'), encoding='utf-8').read())
