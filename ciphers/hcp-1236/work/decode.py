"""HCP1236: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1236/work/decode.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/picture-large.jpg': '8fb122475756226f770e86737da957e2a26236ef70cf2a55c5a979c5a64374a5',
        'source/address-large.jpg': 'b165244fa920c51efa72b604ab40f4d17eb2a9d15fd178f9cebc9b707eb2adc0',
        'work/hires/cpc_1912--22_HU__HU_Jasz-Arokszalas_jolanka-102_pic.jpg': '5ef39176f131bb12374381e6eb3aca31df41272475861c2429762d60548b0376',
        'work/hires/cpc_1912--22_HU__HU_Jasz-Arokszalas_jolanka-102_adr.jpg': 'fb07d227bb9932c21dcda46d22b8cf0631f5d0c4338f24538926630bad4a8a36'}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f)
    if got != h: sys.exit(1)
KEY = {'F': 'r', ')': 's', 'X': 'u', '6': 'b', '+': 'f', 'H': 'h', 'GY': 'gy', 'CS': 'cs',
       'VT': 'vt', 'I?': 'i', 'A!': 'a'}
MARK = {'diaeresis': '̈', 'acute': '́'}
def dec(tok):
    base, _, acc = tok.partition(':')
    s = KEY.get(base, base.lower() if base.isalpha() else None)
    if s is None: raise SystemExit('unknown token ' + tok)
    return unicodedata.normalize('NFC', s + MARK[acc]) if acc else s
print('\nLiteral decipherment by written row (h stands for the h/p sign):')
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print('\nNormalized Hungarian (editorial; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
