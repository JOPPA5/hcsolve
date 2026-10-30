"""HCP1308: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1308/work/decode.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/picture-large.jpg': '45ec444699c799fb83c0549cc9af062f806d200260119c06db0df78c355a8806',
        'source/address-large.jpg': '8d3e3d79cb69fc80fa833e6c3c0f526e15089adf8095c5047223958fadfedb4f',
        'work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-80_pic.jpg': '0dfbd415d047a05ffade7c83373db0eafdfdbafd437d2cac019d0d1bccc8e601',
        'work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-80_adr.jpg': 'd1bba77bda960c582c2896f5b5004127ac256407947c33bc8ee37d7f83077684'}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f)
    if got != h: sys.exit(1)
KEY = {'F': 'r', ')': 's', 'X': 'u', '6': 'b', '+': 'f', 'CS': 'cs'}
def dec(tok):
    base, _, mark = tok.partition(':')
    sense = base.endswith('~') and len(base) > 1
    base = base.rstrip('~') if sense else base
    s = KEY.get(base, base.lower() if base.isalpha() else None)
    if s is None: raise SystemExit('unknown token ' + tok)
    if mark == 'd': s = unicodedata.normalize('NFC', s + '̈')
    return '{' + s + '}' if sense else s
n = 0
print('\nLiteral decipherment, one row per written line ({x} = value chosen by word sense):')
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    n += len(toks)
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print(f'\n{n} written signs.')
print('\nNormalized Hungarian (editorial word division, accents and spelling; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
