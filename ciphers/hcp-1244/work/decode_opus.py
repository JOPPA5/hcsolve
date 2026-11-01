"""HCP1244: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1244/work/decode_opus.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/picture-large.jpg': '4cb6dd4490b5f0522683079ea387ed11f53a81baf6545eb0d00b12f14dad1b84',
        'source/address-large.jpg': 'e1b22aed07d8541bf19aaf16855de908b628e4e296d202a96797844ce2007614',
        'work/hires/cpc_1912-04-10_HU__HU_Jasz-Arokszalas_jolanka-16_pic.jpg': 'b9bbe4d583c3e1d22dbde0b5a26affeb9de3f5cfc84d74ed3850f7171915a5c0',
        'work/hires/cpc_1912-04-10_HU__HU_Jasz-Arokszalas_jolanka-16_adr.jpg': '477cef3e06db196c20576d8a068fb4ab0fa8c444f7edc623739bda1ecec910ba'}
for f, h in HASH.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
KEY = {'=': 'a', '#': 'e', 'S': 'k', '4': 'd', '^': 'v', ')': 's', 'T': 'j', 'Q': 'o', '~': 'l', '2': 'n', '3': 'm',
       '7': 't', 'x': 'u', 'Z': 'z', 'H': 'h', 'F': 'r', '9': 'g', 'J': 'i', 'y': 'y', '6': 'b', '()': 'cs', 'GY': 'gy',
       '4T': 'dj', '[)]': '[s]', '7T': '{j|t}', '<ap>': '’', '<,>': ',', '<.>': '.'}
def dec(t):
    if t[-1] in "'\"" and t[:-1] in KEY:
        return unicodedata.normalize('NFC', KEY[t[:-1]] + ('́' if t[-1] == "'" else '̈'))
    if t not in KEY: raise SystemExit('unknown token ' + t)
    return KEY[t]
print('\nLiteral decipherment, one row per written line (h = the h/p sign; {j|t} = sign with both a j and a t feature; A1 = line below the address):')
for line in open(os.path.join(D, 'work/ledger-opus.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print('\nNormalized Hungarian (editorial word division, accents and spelling; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized-opus.txt'), encoding='utf-8').read())
