"""HCP1277: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1277/work/decode_opus.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
H = 'work/hires/cpc_1914-03-01_HU__HU_Jasz-Arokszalas_jolanka-48_'
HASH = {'source/picture-large.jpg': '0341dea948fc94252baea6cd004cbba664ba69dbe4842c800d1fe261ffd0626a',
        'source/address-large.jpg': '1aa8f5c1190516575a81d6425a2d2b9b4a8204798e138f967aba1417bb93c0b5',
        H + 'pic.jpg': '66bcf12b308b98a2e01b794349af36fb83aa8b9c60fd0dd33e7f37216fb440e4',
        H + 'adr.jpg': 'df9c150f9ff35a1422e30c9e7ca93a6604e372730ed9c826cb36b59507f622a2'}
for f, h in HASH.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
KEY = {'F': 'r', ')': 's', 'X': 'u', '6': 'b', '+': 'f', 'H': 'h', 'CS': 'cs', 'V/6': '{v/b}', '#': '{?}', '[': '[...]'}
def dec(tok):
    base, _, acc = tok.partition(':')
    s = KEY.get(base, base.lower() if base.isalpha() else None)
    if s is None: raise SystemExit('unknown token ' + tok)
    return unicodedata.normalize('NFC', s + '̈') if acc else s
print('\nLiteral decipherment, one row per written line (h = the h/p sign; S rows are under the stamp):')
for line in open(os.path.join(D, 'work/ledger-opus.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print('\nNormalized Hungarian (editorial word division, accents, spelling; {v/b} = overwritten sign; [...] = lost; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized-opus.txt'), encoding='utf-8').read())
