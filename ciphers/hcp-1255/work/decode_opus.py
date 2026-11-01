"""HCP1255: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1255/work/decode_opus.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HIRES = 'work/hires/cpc_1912-03-11_HU__HU_Jasz-Arokszalas_jolanka-08_'
HASH = {'source/picture-large.jpg': 'd42746327dcf0f661347d7b1094faadf82bb8c3a86fcb8a9fa33b3f67ed04c48',
        'source/address-large.jpg': '9fe34775c0845d99a28d5d415e1a8126392e52c32dc54fc3acb30b3acaad0967',
        HIRES + 'pic.jpg': '10bb9724c44ca7a86d08a3e28903f07b9af93d976c31b5eb0afbfa1b5dfea896',
        HIRES + 'adr.jpg': '0c06fbb588901146c3c20247c94759100bbdfc25891007187978820c6d9bdeb3'}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f)
    if got != h: sys.exit(1)
MARK = {'diaeresis': '̈', 'double-acute': '̋', 'acute': '́'}
def dec(tok):
    if tok == '[?]': return '[?]'
    base, _, acc = tok.partition(':')
    if base not in ('GY', 'CS') and not (len(base) == 1 and base.isalpha()):
        raise SystemExit('unknown token ' + tok)
    s = base.lower()
    return unicodedata.normalize('NFC', s + MARK[acc]) if acc else s
print('\nLiteral decipherment, one row per written line:')
for line in open(os.path.join(D, 'work/ledger-opus.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    print(lab, ''.join(dec(t) for t in toks))
print('\nNormalized Hungarian (editorial; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized-opus.txt'), encoding='utf-8').read())
