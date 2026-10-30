"""HCP1316: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1316/work/decode.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/picture-large.jpg': '9155ec2bb8c99aa4f779253f430e3651b78aed295d242ba8613294fdeb4e6c5a',
        'source/address-large.jpg': '29ab5187ac4b786ae32b2df14c0d685c95e241c539c6f26f7073cf04ad13af46',
        'work/hires/cpc_1912-06-30_HU__HU_Jasz-Arokszalas_jolanka-27_pic.jpg': 'f19c43e8ba71857425ab4e0f6e91cd66a23abea48c46128560204ae31a02d8d2',
        'work/hires/cpc_1912-06-30_HU__HU_Jasz-Arokszalas_jolanka-27_adr.jpg': '84156a3dbecaee6ebe2482743b1a81a7d51d9f77ec9e82c6ce47a979352ab4b3'}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f)
    if got != h: sys.exit(1)
KEY = {'F': 'r', ')': 's', 'X': 'u', 'Z': 'z', '6': 'b', '+': 'f', 'H': 'h', '#': '', 'M#': 'm', 'M?': 'm?', 'A?': 'a?', 'BD?': '{b|d}', 'EA?': '{e|a}',
       '[K]': '[k]', '[O]': '[o]'}
MARK = {'diaeresis': '̈', 'double-acute': '̋'}
def dec(tok):
    base, _, acc = tok.partition(':')
    s = KEY.get(base, base.lower() if len(base) == 1 and base.isalpha() else None)
    if s is None: raise SystemExit('unknown token ' + tok)
    return unicodedata.normalize('NFC', s + MARK[acc]) if acc else s
print('\nLiteral decipherment, one row per written line (? = doubtful sign, {x|y} = sign read x, y not excluded, [] = stain-damaged, h = h/p sign):')
n = 0
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    n += len(toks)
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print(f'\nSigns in ledger: {n}')
print('\nNormalized Hungarian (editorial word division, accents and spelling; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
