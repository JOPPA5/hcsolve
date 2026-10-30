"""HCP1297: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1297/work/decode_opus.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
H = 'work/hires/cpc_1912-07-07_HU__HU_Jasz-Arokszalas_jolanka-29_'
HASH = {'source/picture-large.jpg': '7d9aca9c680c6dea02e5b5e82286f7d77946859f8147b10754479b40a3c6dcd6',
        'source/address-large.jpg': '0e16c05abf2eed6733972187e5d51d58bdb66bdb5af23f6f7a89d9e25093dfd4',
        H + 'pic.jpg': '458e759451303abd98b4778946b7732eec942fa7efb3cbe4fb78e8e53f3a2f13',
        H + 'adr.jpg': 'f1eba5686064edb40255465098f027b43a381f682b1a1ea4a1fa77e4fada347d'}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f)
    if got != h: sys.exit(1)
KEY = {'F': 'r', ')': 's', 'X': 'u', '6': 'b', '+': 'f', '/': '{/}', '|': '{|}'}
def dec(tok):
    base, _, acc = tok.partition(':')
    s = KEY.get(base, base.lower() if base.isalpha() else None)
    if s is None: raise SystemExit('unknown token ' + tok)
    return unicodedata.normalize('NFC', s + '̈') if acc == 'd' else s
print('\nLiteral decipherment, one row per written line (H/P are one sign; s1-s5 under the stamp):')
n = 0
for line in open(os.path.join(D, 'work/ledger-opus.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split(); n += len(toks)
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print(f'\n{n} signs. Normalized Hungarian (editorial; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized-opus.txt'), encoding='utf-8').read())
