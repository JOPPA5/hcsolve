"""HCP1224: verify scan hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1224/work/decode.py"""
import hashlib, os, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/picture-large.jpg': '31ed29236e1576f7b98801b9b7784b72e8c6702d846d58f13c622215b41e46dd',
        'source/address-large.jpg': 'e162370ac235a61560490b1ffd8c18ff24f8238c30eb148f9934c3f9df4a4fe1',
        'work/hires/cpc_1912-10-12_HU__HU_Jasz-Arokszalas_jolanka-32_pic.jpg': '10713832859aa15b3504d4c26bfeb5f6a8afbae278605ca6bc9d2718ee365cda',
        'work/hires/cpc_1912-10-12_HU__HU_Jasz-Arokszalas_jolanka-32_adr.jpg': 'cd21227c06e0decaec1d204abb1987f7f0435a061277c97c730a4c3048e89184'}
for f, h in HASH.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
ALPHA = 'A B C D E F G H I J K L M N O P R S T U V Y Z GY CS'.split()
def dec(t):
    if t in ALPHA: return t.lower()
    if t in ('O:', 'U:'): return {'O:': 'ö', 'U:': 'ü'}[t]
    if t.startswith('H:'): return t[2:]
    if t == 'X': return '{#}'   # struck-through two-stroke sign
    if t == 'Q': return '{o|i?}'   # undotted curved sign, row 26
    if t.startswith('plain:'): return '[' + t[6:].replace('_', ' ') + ']'
    raise SystemExit('unknown token ' + t)
print('\nLiteral decipherment, one row per written line:')
n = 0
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split(); n += len(toks)
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print(f'\n{n} tokens decoded.\n\nNormalized Hungarian (editorial word division, accents and spelling; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
