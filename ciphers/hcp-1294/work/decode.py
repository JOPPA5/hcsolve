"""HCP1294: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1294/work/decode.py"""
import hashlib, os, sys, re
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/picture-large.jpg': '652b28366535d7b305f2ce29c27de98a4f169059a62d325a4112764151b80f89',
        'source/address-large.jpg': '8e9eb7a730a543a9d554354f48050a5f7fe74840259ae4c759154eec9df8da48',
        'work/hires/cpc_1912-03-26_HU__HU_Jasz-Arokszalas_jolanka-12_pic.jpg': 'a41fa4c8d01a2aafb46a5f8689315900f491d1b15cfdf24b909d70f36a331faa',
        'work/hires/cpc_1912-03-26_HU__HU_Jasz-Arokszalas_jolanka-12_adr.jpg': 'cfc254e99d1cf7fe9ba24f0f85ff8d83fc54bace6ef4898810b27a0a9c299214'}
for f, h in HASH.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
SPECIAL = {'O:': 'ö', 'O1': 'ȯ', 'X': 'u', 'Z': 'z', 'H': 'h', 'P': 'p', 'cs': 'cs',
           'n*': 'n', 'j!': 'j', 'a!': 'a'}
LETTERS = set('abdegijklmnorstvy')
def dec(t):
    if t in SPECIAL: return SPECIAL[t]
    if t in LETTERS: return t
    raise SystemExit('unknown token ' + t)
print('\nLiteral decipherment, one row per written line:')
n = 0
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    n += len(toks)
    print(lab, ''.join(dec(t) for t in toks))
print(f'\n{n} signs decoded, none without a value.')
print('\nNormalized Hungarian (editorial; accents supplied, see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
