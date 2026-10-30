"""HCP1310: check source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1310/work/decode.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/picture-large.jpg': '200617c04371d55eddfede0be0688c1e5fd961990df45e612414ba0b2fbeb4fa',
 'source/address-large.jpg': '5538b604fe76c83ab5c714c3595fe924b5339a481dd5da414cd4de91f59967e1',
 'work/hires/cpc_1912-07-03_HU__HU_Jasz-Arokszalas_jolanka-28_pic.jpg': '9bd74fb745d90a34ea54e1084544762df6e364798e4f635eca432684536a4bb6',
 'work/hires/cpc_1912-07-03_HU__HU_Jasz-Arokszalas_jolanka-28_adr.jpg': '7ad60adad7349373cfef0eacfbdc6e5d92fcf7a5fc420b742d21888a43b27d60'}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f)
    if got != h: sys.exit(1)
KEY = {'=': 'a', '6': 'b', 'CS': 'cs', '/d': 'd', 'E': 'e', '+': 'f', 'G': 'g', 'GY': 'gy', '/h': 'h', 'I': 'i',
       'J': 'j', 'S': 'k', '~': 'l', '3': 'm', '2': 'n', 'O': 'o', 'F': 'r', ')': 's', 'T': 't', 'X': 'u',
       'V': 'v', 'Y': 'y', 'Z': 'z'}
def dec(t):
    base, _, acc = t.partition(':')
    if base not in KEY: raise SystemExit('unknown token ' + t)
    return unicodedata.normalize('NFC', KEY[base] + ('̈' if acc else ''))
print('\nLiteral decipherment, row by row (S = under the stamp, A = below the address):')
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if line.startswith('#') or not line.strip(): continue
    lab, *toks = line.split()
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print('\nNormalized Hungarian (editorial; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
