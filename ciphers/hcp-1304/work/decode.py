"""HCP1304: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1304/work/decode.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/picture-large.jpg': 'd029818b63416a77d70a4d09edacf4e28b80e19b2fa1dc5730693c85a4d04a15',
        'source/address-large.jpg': 'b5a05e3679333f24aaf28b445675401d429bd2eaeabaf31930e850504690bc78',
        'work/hires/cpc_--04_HU__HU_Jasz-Arokszalas_jolanka-82_pic.jpg': '4ded392c294cb837bfd85b224016203c5cc205c597958dca83a0c8d6095f89b2',
        'work/hires/cpc_--04_HU__HU_Jasz-Arokszalas_jolanka-82_adr.jpg': '3d764b2857a3fae0b830c32032da37523701482042d011d41329a71b219cb6a0'}
for f, h in HASH.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
KEY = {'=': 'a', '3': 'e', '6': 'b', '(': 'c', '()': 'cs', 'J': 'd', '+': 'f', 'G': 'g', 'H': 'h',
       'I': 'i', 'L': 'j', 'K': 'k', 'W': 'l', 'III': 'm', 'II': 'n', 'O': 'o', 'F': 'r', ')': 's', 'T': 't',
       'X': 'u', '^': 'v', 'Y': 'y', 'Z': 'z', '.': '.'}
def dec(t):
    if '>' in t: return '{' + t.split('>')[1] + '}'
    if t.endswith('"') and t != '"': return unicodedata.normalize('NFC', KEY[t[:-1]] + '̈')
    return KEY[t]
n = 0
print('\nLiteral decipherment, row by row (h = the h/p sign; {x} = value by word sense, see SOLUTION.md):')
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if line.startswith('#') or not line.strip(): continue
    lab, *toks = line.split(); n += len(toks)
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print(f'\n{n} signs decoded.\n\nNormalized Hungarian (editorial word division, accents, spelling; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
