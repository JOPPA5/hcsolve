"""HCP1262: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1262/work/decode.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
H = 'work/hires/cpc_1912--15_HU__HU_Jasz-Arokszalas_jolanka-100_'
HASH = {'source/picture-large.jpg': 'da6b4cb09840d5fbceabefe964d7185d1176d4426777741e85bb6461d14bc553',
        'source/address-large.jpg': '83b7b8a8b579fc986b20658fa575dbcc3c8e777210ce8de3ceae08e2b9db7a1f',
        H + 'pic.jpg': 'abb5b14abbe62a8bb6f9b82b6824ac4a675406e18da4862876e2aa75cc4db0c4',
        H + 'adr.jpg': '735580477cf7ae3f4249be78ffc0c2ce2f4987f3b53102d1e31c5755a69872bb'}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f)
    if got != h: sys.exit(1)
KEY = {'6': 'b', 'GY': 'gy', 'CS': 'cs', 'E?': '{e|a}', 'M?': '{m|n}', 'D?': '{d|p}', 'C?': '{c|cs}', 'OL?': '{ol}', '[M]': '[m]'}
def dec(tok):
    base, _, acc = tok.partition(':')
    s = KEY.get(base, base.lower() if base.isalpha() and len(base) == 1 else None)
    if s is None: raise SystemExit('unknown token ' + tok)
    return unicodedata.normalize('NFC', s + '̈') if acc else s
print('\nLiteral decipherment, one row per written line (h and p are one sign, printed by word sense; {x|y} = shape value|value the word needs):')
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print('\nNormalized Hungarian (editorial word division, accents and spelling; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
