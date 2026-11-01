"""HCP1280: verify scan hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1280/work/decode.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
B = 'work/hires/cpc_1912-03-13_HU__HU_Jasz-Arokszalas_jolanka-09_'
HASH = {'source/picture-large.jpg': '12878dd298cc9f43632233b49a7726da6f17ce45b893fa719284c0b93d487be4',
        'source/address-large.jpg': '3239c3aded13968d3e2297913e3aa6345fae7d351d16a6d92970b5d34222d978',
        B + 'pic.jpg': '075f0aa02530b8d72af940da063ee0bce1966cd7fdbdfb01d61289ec7a48f314',
        B + 'adr.jpg': '19b51f3ca260f6d42f21cba9d76f78ffb760106662e48b1fc6deef8427ab4350'}
for f, h in HASH.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
MARK = {'a': '́', 'd': '̈', 'dd': '̋'}
def dec(t):
    if t in ('-', '.'): return t
    b, _, m = t.partition(':')
    q = b.endswith('!')
    b = b.rstrip('!')
    if not b.isalpha(): raise SystemExit('unknown token ' + t)
    s = unicodedata.normalize('NFC', b.lower() + MARK[m]) if m else b.lower()
    return '{' + s + '}' if q else s
print('\nLiteral decipherment by written row ({x} = overwritten/irregular sign, value by word sense):')
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if line.strip() and not line.startswith('#'):
        lab, *toks = line.split()
        print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print('\nNormalized Hungarian (editorial; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
