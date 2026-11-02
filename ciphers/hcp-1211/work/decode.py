"""HCP1211: check source hashes and decode the sign ledger. From repo root:
   python3 -I ciphers/hcp-1211/work/decode.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/picture-large.jpg': '1970b43454a0e8d4c03ea92302fb4165e289f8c354ead6dfbd1757d744b21bfb',
 'source/address-large.jpg': '184ad987351308b86aeb48701c32133e17eb9fe374ad1e907dec9bd9874f848a',
 'work/hires/cpc_1912-02-10_HU__HU_Jasz-Arokszalas_jolanka-04_pic.jpg': '25db1259938391f5604d911e051d8038a9ccd23dfc24fad3492361f5e1faafb9',
 'work/hires/cpc_1912-02-10_HU__HU_Jasz-Arokszalas_jolanka-04_adr.jpg': '09b8f847e98ef5fe5eb0e51f518c1b192b93d5b53b54a96d1d119576eaea4880'}
for f, h in HASH.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
KEY = {'=': 'a', '6': 'b', 'C': 'g', 'CY': 'gy', 'CS': 'cs', '/': 'd', 'E': 'e', 'E*': 'e', '+': 'f', 'P': 'h',
       'I': 'i', 'J': 'j', 'S': 'k', 'L': 'l', 'LY': 'ly', 'III': 'm', 'II': 'n', 'NY': 'ny', 'O': 'o',
       'F': 'r', ')': 's', 'T': 't', 'X': 'u', 'V': 'v', 'Z': 'z', 'is': '[is]', '{O}': '{O}', '{blot}': '{blot}'}
def dec(t):
    acc = ''
    if t[-1] in "'\"" : acc = {"'": '́', '"': '̈'}[t[-1]]; t = t[:-1]
    return unicodedata.normalize('NFC', KEY[t] + acc)
print('\nLiteral decipherment by written row (P is shown as h; see SOLUTION.md for h/p):')
n = 0
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if line.startswith('#') or not line.strip(): continue
    lab, *toks = line.split(); n += len(toks)
    print(lab, ''.join(dec(t) for t in toks))
print('\nSigns in ledger:', n)
print('\nNormalized Hungarian (editorial):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
