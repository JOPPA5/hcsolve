"""HCP1303: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1303/work/decode.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/picture-large.jpg': '37c197ffcecdbb98863d1f0723b76c0916bc38dfc51ce6b189790ace9f0db079',
        'source/address-large.jpg': 'a8cd7e43d2d6b3273100cbab2ff907354c7dac65987cdc77107265139469aa0e',
        'work/hires/cpc_--13_HU__HU_Jasz-Arokszalas_jolanka-84_pic.jpg': 'd27bbb6d4bcb9bbd8675cb3e1d011794f4f679d9caa86ecaa6aa55bd6a2d4a51',
        'work/hires/cpc_--13_HU__HU_Jasz-Arokszalas_jolanka-84_adr.jpg': 'cb01e4067ad4bf30c7888f3d6a8e57b285586b8dd87bf03ca49f59707b116a29'}
for f, h in HASH.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
MARK = {'dia': '̈', 'acute': '́'}
def dec(t):
    if t.startswith('<'): return '<' + t[1:-1] + '>'
    if t == '.': return '.'
    base, _, acc = t.partition(':')
    if not (base.isalpha() and base.isupper()): raise SystemExit('unknown token ' + t)
    s = base.lower()
    return unicodedata.normalize('NFC', s + MARK[acc]) if acc else s
print('\nLiteral decipherment, one row per written line (h = the h/p sign):')
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print('\nNormalized Hungarian (editorial word division, accents, spelling; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
