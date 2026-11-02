"""HCP1226: verify source hashes and decode the sign ledger. Run from the repo root:
   python3 -I ciphers/hcp-1226/work/decode.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
A = 'cpc_--17_HU__HU_Jasz-Arokszalas_jolanka-85_'
HASH = {'source/picture-large.jpg': 'a1d7089bec3bca38703fe19277d27c133f60bd9cc01302806f197f2129f7050a',
        'source/address-large.jpg': '179a9fb6876f8bad38dc5eebd79edf443174a9923061e55c22033bf5261b73bc',
        'work/hires/' + A + 'pic.jpg': 'cd38faee0d811857d0839356265ea9f32a28baaa56b7eac745f6b50264b0a358',
        'work/hires/' + A + 'adr.jpg': '14897011e39190653db38549a75fd1f2af98f2562950b3bdb67634b2ae278e7f'}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f)
    if got != h: sys.exit(1)
KEY = {'F': 'r', ')': 's', 'X': 'u', '6': 'b', '+': 'f', 'H': 'h', 'CS': 'cs', 'D': 'd',
       'H/d': '{d}', 'D/p': '{p}', 'J?': '{j}', 'D?': '{d}', 'O?': '{o}', '+?': '{f}', '#': '[#]'}
def dec(tok):
    base, _, mark = tok.partition(':')
    s = KEY.get(base, base.lower() if base.isalpha() and len(base) == 1 else None)
    if s is None: raise SystemExit('unknown token ' + tok)
    return unicodedata.normalize('NFC', s + '̈') if mark == 'd' else s
print('\nLiteral decipherment, one row per written line (h stands for the h/p sign; {x} = value from word sense; [#] scribbled):')
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print('\nNormalized Hungarian (editorial word division, accents, spelling; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
