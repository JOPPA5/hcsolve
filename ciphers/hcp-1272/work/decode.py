"""HCP1272: verify scan hashes and decode the ledger. From repo root: python3 -I ciphers/hcp-1272/work/decode.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
N = 'cpc_1912-04-30_HU__HU_Jasz-Arokszalas_jolanka-17_'
HASH = {'source/picture-large.jpg': 'f02f55e0184e368501ee627750a1b29f88596eaa55c6f4d92d4bc2bac332b9b1',
        'source/address-large.jpg': '80f3c8aff2e2552f01c50b614470e4b83a079fbefefd46851cd15e7436c63705',
        'work/hires/' + N + 'pic.jpg': '3ed4c158898689c5003408d76d7bb100e0b0b62232ba7a93c3f77e1f0b18b6e3',
        'work/hires/' + N + 'adr.jpg': '3b5a26104c77b0ddfca92d17adfb7c6d5b97021892c70011a506b9b8e561e179'}
for f, h in HASH.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
KEY = dict(zip('ADEFGHIJKLMNOPSTVXYZ', 'adergh' 'ijklmnopst' 'vuyz'))
KEY.update({'6': 'b', 'C': 'c', 'CS': 'cs', 'GY': 'gy', '{lm}': '{lm}', '.': '.', '=': '='})
MARK = {"'": '́', ':': '̈', '"': '̋'}
def dec(t):
    if t[0] == '~': return '[' + t[1:] + ']'
    if t[-1] in MARK: return unicodedata.normalize('NFC', KEY[t[:-1]] + MARK[t[-1]])
    return KEY[t]
print('\nLiteral decipherment ([..] = unenciphered cursive; H/P sign printed by sense):')
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if line.strip() and line[0] != '#':
        lab, *toks = line.split()
        print(lab, ''.join(dec(t) for t in toks))
print('\nNormalized Hungarian (word division, accents, spelling are editorial; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
