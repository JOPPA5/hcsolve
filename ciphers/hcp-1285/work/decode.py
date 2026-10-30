"""HCP1285: verify scan hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1285/work/decode.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/picture-large.jpg': '2a1d1ae191c18b518153480247a6ea6ca2225771104e8318be69c55fd5e435c0',
        'source/address-large.jpg': 'ac6d4009d90d7ce373123e013c70d1dd8ece801cc1c1e6d3465bfe6674249539',
        'work/hires/cpc_1912-01-14_HU__HU_Jasz-Arokszalas_jolanka-02_adr.jpg': '4f7ca645158ba6570383d5b35a44f5169c60db280e28c12fc30bd4e31349cecd',
        'work/hires/cpc_1912-01-14_HU__HU_Jasz-Arokszalas_jolanka-02_pic.jpg': 'e161c29d5188a91050090ce1735c7e114d6725c908669bcf3dfce9f0a5433b0e'}
for f, h in HASH.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
MARK = {'d': '̈', 'a': '́'}
def dec(t):
    if t == '#': return '{blot}'
    if t == '.': return '.'
    if t.startswith('^'): return '^' + t[1:].lower()
    b, _, m = t.partition(':')
    if not b.isalpha(): raise SystemExit('unknown token ' + t)
    return unicodedata.normalize('NFC', b.lower() + MARK[m]) if m else b.lower()
print('\nLiteral decipherment by written row (^n = n written small above the row):')
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if line.strip() and not line.startswith('#'):
        lab, *toks = line.split()
        print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print('\nNormalized Hungarian (editorial; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
