"""HCP1223: verify scan hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1223/work/decode.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/picture-large.jpg': '5e800e2c40262cb988bff014e6a7abdb3f08dd618280f14b8d7d1e0f9f41fd14',
        'source/address-large.jpg': '5403063fb0237c6f1f093d9c8e1f965d6c7dad26908d680c66d80055e67018c5',
        'work/hires/cpc_1913-01-_HU__HU_Jasz-Arokszalas_jolanka-114_pic.jpg': '1fd3ea910dfefb0712198d5918e1b682535556f9bdcb3c16f149ea645f590458',
        'work/hires/cpc_1913-01-_HU__HU_Jasz-Arokszalas_jolanka-114_adr.jpg': 'f3e1987fb3ce6a64fa28a65f2ad67ac901303c68ea0d72ea3750d398f7a64b4a'}
for f, h in HASH.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
KEY = {c: c.lower() for c in 'ABDEGHIJKLMNOPRSTUVYZ'}
KEY.update({'HD': 'd', 'LY': 'ly', 'CS': 'cs', 'FF': 'f', '.': '.'})
MARK = {'diaeresis': '̈', 'acute': '́'}
def dec(t):
    b, _, a = t.partition(':')
    return unicodedata.normalize('NFC', KEY[b] + MARK[a]) if a else KEY[b]
n = 0
print('\nLiteral decipherment, one row per written line (S1-S6 = under the stamp):')
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line[0] == '#': continue
    lab, *toks = line.split(); n += sum(t != '.' for t in toks)
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print(f'\n{n} signs decoded, none without a value.')
print('\nNormalized Hungarian (editorial; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
