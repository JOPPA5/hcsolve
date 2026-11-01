"""HCP1269: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1269/work/decode_opus.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/picture-large.jpg': 'e1a9e3642e65c535a8d2fb39cc62b652c38d21c8a7e08ecf289190540a0f3afe',
        'source/address-large.jpg': 'd93b4641f1de8f557ee4a0a9dd6091461ff4128c115681133b6e9edd21ebb402',
        'work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-71_pic.jpg': '586fae22706e389a7201ad7542c29bba592b567dd09f5443e55764d0df566e23',
        'work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-71_adr.jpg': '771f229645a1df7161a74cd60b9c781787f8626a37db86cabb04e561338ea1a1'}
for f, h in HASH.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
KEY = {'F': 'r', ')': 's', 'X': 'u', '6': 'b', '+': 'f', 'H': 'h', 'CS': 'cs',
       '??': '{?}', '^': '-', '.': '.'}
MARK = {'diaeresis': '̈', 'dbl': '̋'}
def dec(tok):
    base, _, acc = tok.partition(':')
    s = KEY.get(base, base.lower() if base.isalpha() else None)
    if s is None: raise SystemExit('unknown token ' + tok)
    return unicodedata.normalize('NFC', s + MARK[acc]) if acc else s
print('\nLiteral decipherment, one row per written line (h stands for the h/p sign):')
for line in open(os.path.join(D, 'work/ledger-opus.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print('\nNormalized Hungarian (editorial; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized-opus.txt'), encoding='utf-8').read())
