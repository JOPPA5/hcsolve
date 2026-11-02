"""HCP1228: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1228/work/decode.py"""
import hashlib, os, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
N = 'cpc_1913-09-07_HU__HU_Jasz-Arokszalas_jolanka-42'
HASH = {'source/picture-large.jpg': '2bf6ae9ea58226c466aa83d665720298b2821c37dd076fb8124bdab7b3e9e664',
        'source/address-large.jpg': '0ec5973a887aaf2a9218fc58c64fea0af7c35b8596fb685a9470aa6ea8942078',
        f'work/hires/{N}_pic.jpg': 'e832dccee8891690f837de6a9cf63778832c691f81d5c28c50de3a097c582c53',
        f'work/hires/{N}_adr.jpg': '26cee184c9f2daadfbc496eca265e9f4f443e1c083746456cc0c10d56cd368d4'}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f)
    if got != h: sys.exit(1)
KEY = dict(zip('ABDEGHIJKLMNOTVYZ', 'abdeghijklmnotvyz'))
KEY.update({'F': 'r', ')': 's', 'X': 'u', '+': 'f', 'CS': 'cs', "A'": 'á', "E'": 'é', 'O:': 'ö', 'U:': 'ü',
            'Hp': 'p', 'Hd': 'd', 'TF': 't', '/': ' ', '.': '.', '[cancelled]': '[cancelled]'})
def dec(t):
    if t.startswith('#'): return t[1:]
    if t.startswith('^'): t = t[1:]
    if t.endswith('?'): return '[' + KEY[t[:-1]] + ']'
    if t not in KEY: raise SystemExit('unknown token ' + t)
    return KEY[t]
print('\nLiteral decipherment, row by row ([x] = restored sign, h = tall+tick sign):')
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *t = line.split()
    print(f'{lab:>3} ' + ''.join(dec(x) for x in t))
print('\nNormalized Hungarian (editorial; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
