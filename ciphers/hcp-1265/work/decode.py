"""HCP1265: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1265/work/decode.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/picture-large.jpg': 'af57b83c7c3192242d9dcd5d27c5306cb43bd9876d374d10e029d2bb756eee76',
        'source/address-large.jpg': 'd5d6b287cc339685ee9635998b530df7b1c3ebfc110173656201ce648bf01395',
        'work/hires/cpc_--17_HU__HU_Jasz-Arokszalas_jolanka-86_pic.jpg': 'bb6709f45417488907592df4629aaaf34c9d543528b3a34dd7e038a95a5e1b05',
        'work/hires/cpc_--17_HU__HU_Jasz-Arokszalas_jolanka-86_adr.jpg': '59249a036f2ffa348f0685406ec97f2d9658d8a03965713d8614680ac28ddaa4'}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f)
    if got != h: sys.exit(1)
KEY = {'F': 'r', ')': 's', 'X': 'u', '6': 'b', '+': 'f', 'H': 'h', 'CS': 'cs', 'STRUCK': '[deleted]',
       'K~': 'k', 'N?': 'n', 'E#': 'e', 'D#': 'd', 'D?': 'd', 'X#': 'u', 'H#': 'p', 'T?': 't', 'D~': 'd', 'A#': 'a',
       'N#': 'n', 'M~': 'm', 'S~': 's', 'S#': 's', 'R~': 'r'}
MARK = {'dia': '̈', 'dbl': '̋'}
def dec(tok):
    base, _, acc = tok.partition(':')
    s = KEY.get(base, base.lower() if len(base) == 1 and base.isalpha() else None)
    if s is None: raise SystemExit('unknown token ' + tok)
    return unicodedata.normalize('NFC', s + MARK[acc]) if acc else s
rows, n = [], 0
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    n += len(toks)
    rows.append((lab, ''.join(dec(t) for t in toks)))
print('\nLiteral decipherment, one row per written line (h stands for the h/p sign unless the ledger marks p):')
for lab, txt in rows: print(f'{lab:>3} {txt}')
print(f'\n{n} signs in {len(rows)} rows.')
print('\nNormalized Hungarian (editorial word division, accents and spelling; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
