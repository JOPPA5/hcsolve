"""HCP1246: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1246/work/decode.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/address-large.jpg': 'cbb5ccabfe4371d619b0a5e0476c1cfeb77671492db7ff9b14c5436ecac2f6ae',
        'source/picture-large.jpg': '4743c2f8850b60f90b0db128dd0da6ebea668b5a631195ab61be309989663bd7',
        'work/hires/cpc_1913-09-_HU__HU_Jasz-Arokszalas_jolanka-115_adr.jpg': '0386e29afb5d29e42884dd8cc3861f43ef8178f33156ca9c636323d2607dd123',
        'work/hires/cpc_1913-09-_HU__HU_Jasz-Arokszalas_jolanka-115_pic.jpg': 'a4689cd4f041b5013cbf65f4608d911453c35dcd56d2733e44f782f11257503a'}
for f, h in HASH.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
# family key (HCP1216): sign class -> letter; each sign's ledger token is already the family letter, H = h/p
KEY = {c: c.lower() for c in 'ABCDEFGHIJKLMNORSTUVYZ'}
def dec(t):
    if t == '.': return '.'
    if t.startswith('['): return '[' + KEY[t[1]] + ']'
    b, dots = t[0], t.endswith(':')
    return unicodedata.normalize('NFC', KEY[b] + '̈') if dots else KEY[b]
print('\nLiteral decipherment, one row per written line (h stands for the h/p sign; row 29 runs up the right edge; S = stamp box):')
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print('\nNormalized Hungarian (editorial; [..] = letters not on the card; {..} = literal form kept, sense uncertain; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
