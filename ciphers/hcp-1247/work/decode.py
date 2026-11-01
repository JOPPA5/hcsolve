"""HCP1247: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1247/work/decode.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
P = 'cpc_1913-09-19_HU__HU_Jasz-Arokszalas_jolanka-44_'
HASH = {'source/picture-large.jpg': 'bfc320dd05d42c5fbb1d7b872ee8204c97f8e6a2e1edb0eec45d00abc8b7f8f0',
        'source/address-large.jpg': '3a046bd19ce24da851c05ff0f35f19039e03d488983490d2cc6e5f708442c17d',
        'work/hires/' + P + 'pic.jpg': '76a308c23d1d9975b062097f3ee97b293399f507eefd7fdf1845ae4393257293',
        'work/hires/' + P + 'adr.jpg': '052709b4321e7e250cbfabcd26916e89daba9624a570209c7187644f6a07d9de'}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f)
    if got != h: sys.exit(1)
def dec(t):
    if t.startswith('['): return '[' + t[1:-1].lower() + ']'
    if t in ('?', '.', '5', '0'): return t
    base, _, m = t.partition(':')
    s = 'u' if base == 'X' else base.lower()
    return unicodedata.normalize('NFC', s + '̈') if m else s
print('\nLiteral decipherment, one row per written line:')
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print('\nNormalized Hungarian (editorial; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
