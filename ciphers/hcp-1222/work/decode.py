"""HCP1222: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1222/work/decode.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
H = 'cpc_1913-01-_HU__HU_Jasz-Arokszalas_jolanka-113_'
HASH = {'source/picture-large.jpg': 'd74e45a64ed4777b56ae2742cfbf458c4acc8f9093e29ee833caf72c4944bcc0',
        'source/address-large.jpg': '9ef00d9c83a7ec9775ecc620e0ef97af0736b1c51fb832ef62a19e4ac61fa494',
        'work/hires/' + H + 'pic.jpg': 'ccad14ad5b3eb1fde2282862168ea628eef047ae9e18e8cf6a31a3203a3c1858',
        'work/hires/' + H + 'adr.jpg': '0050c53fca0659c600aae5c5bfed585d2011fd3e5379677379124e55eae2a45a'}
for f, h in HASH.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
KEY = {'F': 'r', ')': 's', 'X': 'u', 'Z': 'z', '6': 'b', '+': 'f', '/': 'd', 'H': 'h', 'P': 'p', 'GY': 'gy', 'CS': 'cs',
       '7': '7', '.': '.', 'D?': '{d?}', 'R>T': '{t>r}', 'BLOT': '{a|e}'}
MARK = {'diaeresis': '̈', 'acute': '́'}
def dec(tok):
    base, _, acc = tok.partition(':')
    s = KEY.get(base, base.lower() if base.isalpha() and len(base) == 1 else None)
    if s is None: raise SystemExit('unknown token ' + tok)
    return unicodedata.normalize('NFC', s + MARK[acc]) if acc else s
print('\nLiteral decipherment, one row per written line (c1-c6: stamp corner):')
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print('\nNormalized Hungarian (editorial word division, spelling; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
