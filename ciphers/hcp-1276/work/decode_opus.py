"""HCP1276: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1276/work/decode_opus.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
N = 'work/hires/cpc_1912-08-11_HU__HU_Jasz-Arokszalas_jolanka-30_'
HASH = {'source/address-large.jpg': '4cb9a43e9e09133f2145ddcf508a9b0cbab12f5e346f73baae8f40dc3291c17d',
        'source/picture-large.jpg': '3c8d19e4a85a82a4a5e5cded1b6a71b3289a7bbc930b73012f8532dd28976911',
        N + 'adr.jpg': 'c375e9c4940f00ab1b633a4a4be26c7e84a57f82a2604685cdec9db58d5df7d2',
        N + 'pic.jpg': 'cde9ffcefed9b7ed58d238360d63a8d6df682f053344e7d6c4e384570952590b'}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f)
    if got != h: sys.exit(1)
KEY = {'F': 'r', ')': 's', 'X': 'u', '6': 'b', '+': 'f', '(': 'c', 'GY': 'gy', '7': '7',
       '|': '{|}', 'H~': 'h'}
def dec(tok):
    base, _, acc = tok.lstrip('*').partition(':')
    s = KEY.get(base, base.lower() if base.isalpha() and len(base) == 1 else None)
    if s is None: raise SystemExit('unknown token ' + tok)
    return unicodedata.normalize('NFC', s + '̈') if acc else s
print('\nLiteral decipherment, one row per written line (s1-s5 = stamp box):')
for line in open(os.path.join(D, 'work/ledger-opus.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print('\nNormalized Hungarian (editorial word division, accents and spelling; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized-opus.txt'), encoding='utf-8').read())
