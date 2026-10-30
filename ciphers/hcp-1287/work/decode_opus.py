"""HCP1287: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1287/work/decode_opus.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
H = 'cpc_1912-05-15_HU__HU_Jasz-Arokszalas_jolanka-21_'
HASH = {'source/picture-large.jpg': 'ea8fd8c8501de5cd2e01dbedbf6f90ccd8cf993ee8a2b706108367a7b3454f49',
        'source/address-large.jpg': 'de68b7c894b611ab60c5e718dfee67c7d2b51a553b6910acc0cb9374facdeb93',
        'work/hires/' + H + 'pic.jpg': 'b3bd5408a12fe7f2532058c5f378d242b30f117e4049273c045cc3b4c4ce827a',
        'work/hires/' + H + 'adr.jpg': '7cb821a6245ec616066980eb90f8b80c992adaf6ffce6ff0ac4f8d71cbb09228'}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f)
    if got != h: sys.exit(1)
KEY = {'F': 'r', ')': 's', 'X': 'u', 'Z': 'z', '6': 'b', '+': 'f', 'HH': 'h', 'PP': 'p', 'DD': 'd',
       'CS': 'cs', 'NINE': '{9|k}'}
MARK = {'U': '̈', 'DA': '̋'}
def dec(tok):
    base, _, acc = tok.partition(':')
    br = base.startswith('[')
    base = base.strip('[]')
    s = KEY.get(base, base.lower() if base.isalpha() and len(base) == 1 else None)
    if s is None: raise SystemExit('unknown token ' + tok)
    s = unicodedata.normalize('NFC', s + MARK[acc]) if acc else s
    return '[' + s + ']' if br else s
print('\nLiteral decipherment, one row per written line ([x] = restored under the blot):')
n = 0
for line in open(os.path.join(D, 'work/ledger-opus.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split(); n += len(toks)
    print(lab, ''.join(dec(t) for t in toks))
print(f'\n{n} signs. Normalized Hungarian (editorial; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized-opus.txt'), encoding='utf-8').read())
