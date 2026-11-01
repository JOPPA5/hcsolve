"""HCP1249: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1249/work/decode.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/picture-large.jpg': '5e93d1bb919b46ed75051d796dcabece0f0f7e49f7fed41e436cb3b43feeb71d',
        'source/address-large.jpg': 'ba65473651f75410ce0f8c7a2500c08d031280e2e6310a4cbcc1608043cd14d5',
        'work/hires/cpc_1914-03-25_HU__HU_Jasz-Arokszalas_jolanka-51_pic.jpg': '851d2697fb9e1ba100abe033937558bb59b10cabe64368f481f496799f540189',
        'work/hires/cpc_1914-03-25_HU__HU_Jasz-Arokszalas_jolanka-51_adr.jpg': '8357170ac5ea48ffe37c1975dd884457112e2b1e3a8c9336a081493832ede702'}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f)
    if got != h: sys.exit(1)
KEY = {'F': 'r', ')': 's', 'X': 'u', 'Z': 'z', '6': 'b', '+': 'f', 'CS': 'cs', '2': '2', '4': '4', '5': '5'}
MARK = {'diaeresis': '̈', 'double-acute': '̋', 'acute': '́', 'dot': ''}
def dec(tok):
    base, _, acc = tok.partition(':')
    dmg = base.endswith('#'); base = base.rstrip('#')
    if base.startswith('{'): s = base
    else:
        s = KEY.get(base, base.lower() if base.isalpha() else None)
    if s is None: raise SystemExit('unknown token ' + tok)
    if acc: s = unicodedata.normalize('NFC', s + MARK[acc])
    return '[' + s + ']' if dmg else s
print('\nLiteral decipherment, one row per written line (h and p are one sign, split by word sense; [x] = read through damage):')
n = 0
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split(); n += len(toks)
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print(f'\n{n} signs')
print('\nNormalized Hungarian (editorial; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
