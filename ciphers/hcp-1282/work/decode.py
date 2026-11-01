"""HCP1282: check source hashes, decode the sign ledger. From repo root:
   python3 -I ciphers/hcp-1282/work/decode.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
H = {'source/picture-large.jpg': '52574aeaabb882a94c676295fba7da69f2bf6a8b64ee659f3d8b995c8cd96b05',
     'source/address-large.jpg': '325227aae6fed2276c09faa96c7b5d308b2c99cacda336993fde4a3d5ed01186',
     'work/hires/cpc_-04-11_HU__HU_Jasz-Arokszalas_jolanka-94_pic.jpg': '514e6e6e4a4dca5e93b43964076cc364f128d958c6b2fded8f77c86b56b55963',
     'work/hires/cpc_-04-11_HU__HU_Jasz-Arokszalas_jolanka-94_adr.jpg': '50bd56a292d87964a461d9d9d058dd51f130f738f5ef18ad38106a6de666b549'}
for f, h in H.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
SP = {'X': 'u', 'U:': 'ü', 'O:': 'ö', 'O"': 'ő', '+J': 'j', '+F': 'f', 'Ic': 'I', '/': '|', '*': '·', '[T]': '[t]', '[E]': '[e]'}
LETTERS = set('ABCDEFGHIJKLMNOPRSTUVYZ') | {'GY'}
def dec(t):
    if t in SP: return SP[t]
    if t in LETTERS: return t.lower()
    sys.exit('unknown token ' + t)
print('\nLiteral decipherment, one row per written line:')
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    print(lab, unicodedata.normalize('NFC', ''.join(dec(t) for t in toks)))
print('\nNormalized Hungarian (editorial; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
