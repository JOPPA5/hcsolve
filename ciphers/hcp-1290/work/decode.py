"""HCP1290: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1290/work/decode.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/picture-large.jpg': '59f8ce98db1d4a54a5480390772fb928685d7195991b33ecafc1f1f2140c7a95',
        'source/address-large.jpg': '0db1c8390d0a265a2e16f78ff42cf679001b1e539f4169da5b56d47acaa0da4d',
        'work/hires/cpc_-02-_HU__HU_Jasz-Arokszalas_jolanka-92_pic.jpg': 'f9f9302a0e536e0ce350b294d2fedbd0ac459cecfd6ed9cd2768eeb27ce78116',
        'work/hires/cpc_-02-_HU__HU_Jasz-Arokszalas_jolanka-92_adr.jpg': '4d3231711c8124c774e6f4457a958ebbd582ff3d765807e15c63d9145acdc4b4'}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f)
    if got != h: sys.exit(1)
KEY = {'F': 'r', ')': 's', 'X': 'u', '6': 'b', '+': 'f', 'GY': 'gy', 'CS': 'cs', 'J?': '{j}', 'I?': '{i}', '[BLOT]': '[blot]', '[UNREAD]': '[unread]'}
MARK = {'diaeresis': '̈', 'double-acute': '̋', 'acute': '́'}
def dec(tok):
    base, _, acc = tok.partition(':')
    s = KEY.get(base, base.lower() if base.isalpha() and len(base) == 1 else None)
    if s is None: raise SystemExit('unknown token ' + tok)
    return unicodedata.normalize('NFC', s + MARK[acc]) if acc else s
rows, n = [], 0
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    n += len(toks)
    rows.append((lab, ''.join(dec(t) for t in toks)))
print(f'\nLiteral decipherment, one row per written line ({n} sign tokens; S rows = where the stamp was):')
for lab, txt in rows: print(f'{lab:>3} {txt}')
print('\nNormalized Hungarian (editorial word division, accents and spelling; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
