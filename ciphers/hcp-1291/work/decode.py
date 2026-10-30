"""HCP1291: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1291/work/decode.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HIRES = 'work/hires/cpc_1913-08-31_HU__HU_Jasz-Arokszalas_jolanka-41_'
HASH = {'source/picture-large.jpg': '5420bc9b11d592728e42ad0693b205020eb5e6ad1c31c8f9bb2962796da179e5',
        'source/address-large.jpg': '5e072a3b297f2a4f1660afb04204f98e8dd8d0bbb1fc2a6ff8eb26943a5013e4',
        HIRES + 'pic.jpg': 'ea8aa8be9a75a22ac00496b4afe40d614f43fe3acc0e608daba8b141911ff3ab',
        HIRES + 'adr.jpg': '83e17b10ea4871fa45458c62860fb17b31b78009ad35b6308b9d8fbce538877a'}
for f, h in HASH.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
SPECIAL = {'H~': 'h', 'D~': 'd', 'P~': 'p', 'J?': '{j}', 'M?': '{m}', 'E+N': '{e+n}', 'N?': '{n}',
           'A?': '{a?}', 'D?': '{d}', '[E]': '[e]', 'I~': '{i}'}
MARK = {'diaeresis': '̈'}
def dec(tok):
    if tok in SPECIAL: return SPECIAL[tok]
    base, _, acc = tok.partition(':')
    if len(base) != 1 or not base.isalpha(): raise SystemExit('unknown token ' + tok)
    return unicodedata.normalize('NFC', base.lower() + MARK[acc]) if acc else base.lower()
print('\nLiteral decipherment, one row per written line; {x} = value rests on word sense, [x] = restoration:')
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print('\nNormalized Hungarian (editorial word division, accents and spelling; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
