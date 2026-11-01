"""HCP1252: verify source hashes, decode the sign ledger, print plain parts. Run from repo root:
   python3 -I ciphers/hcp-1252/work/decode_opus.py"""
import glob, hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/picture-large.jpg': '88a12609bc5fede3fb479bfce3ff932b0e562b35186028e664b5029dc5412970',
        'source/address-large.jpg': '9aad3d003c5459379a569b2343a5164c6f61f8b90e8a365cd57e41611af0fd15',
        'work/hires/cpc_1913-06-13_HU__HU_Jasz-Arokszalas_jolanka-37_pic.jpg': 'fb976ac0bc24ee171cbdf98d4ed56d67bd6787a7f100e56778a79386ef32d34e',
        'work/hires/cpc_1913-06-13_HU__HU_Jasz-Arokszalas_jolanka-37_adr.jpg': '6f02710a124aca5354307ac3e82d065a13a475fcce05eb244e0fd62a675c9223'}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f)
    if got != h: sys.exit(1)
KEY = {'F': 'r', ')': 's', '(': 'c', 'CS': 'cs', 'X': 'u', '6': 'b', 'H': 'h', 'Z': 'z',
       '1': '1', '0': '0', ',': ',', '.': '.', '-': '-'}
def dec(tok):
    base, _, acc = tok.partition(':')
    s = KEY.get(base, base.lower() if base.isalpha() and len(base) == 1 else None)
    if s is None: raise SystemExit('unknown token ' + tok)
    return unicodedata.normalize('NFC', s + '̈') if acc else s
print('\nLiteral decipherment of the cipher block (h stands for the h/p sign):')
n = 0
for line in open(os.path.join(D, 'work/ledger-opus.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    n += len(toks)
    print(f'{lab:>2} ' + ''.join(dec(t) for t in toks))
print(f'({n} tokens)')
print('\nNormalized text (editorial; {...} = letters read but word not understood or unsure; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized-opus.txt'), encoding='utf-8').read())
