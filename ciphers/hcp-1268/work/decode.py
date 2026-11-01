"""HCP1268: verify scan hashes and apply the key to the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1268/work/decode.py"""
import hashlib, os, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
H = 'work/hires/cpc_1912-01-17_HU__HU_Jasz-Arokszalas_jolanka-03_'
HASH = {'source/picture-large.jpg': 'e7378843b11727c1b909859d75fab110f49a3b91907c4e30259a6e31f713aa52',
        'source/address-large.jpg': '6334427d0ccaca1916bbacf8e0e607696c4428d3908efdd68afe79b12234b37e',
        H + 'pic.jpg': '8f939361975e3482504938dfce5c6d71cc206b503f5f55f3c30f479ef5cfea38',
        H + 'adr.jpg': '8af5004057d4b0489b2d1bb9e3412a4d952f29efb3dc218b651f427d070a0d61'}
for f, h in HASH.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
# The key: written sign (shape name, see ledger.txt) -> plaintext.
KEY = {'bar2': 'a', 'bar3': 'e', 'six': 'b', 'ls': 'd', 'chev': 'v', 'rb': 's', 'lb': 'g', 'bb': 'cs', 'it': 'j',
       'loop': 'o', 'loop2': 'ő', 'wave': 'l', 'st2': 'n', 'st3': 'm', 'sec': 'k', 'gam': 't', 'eff': 'r',
       'cc': 'i', 'cn': 'i', 'hi1': 'h', 'lo1': 'p', 'tq': 'h', 'xx': 'z', 'xd': 'ü', 'gy': 'gy', 'plus': 'f',
       # uncertain signs: the reading is shown with its alternative
       'strk3': '{e|a}', 'strk2': '{a}', 'over': '{c|k}', 'loopn': 'o(n?)',
       # plain longhand and the written dot pass through
       'meg': ' meg ', 'hi': 'hi', '.': '.'}
def dec(t):
    if t not in KEY: raise SystemExit('unknown token ' + t)
    return KEY[t]
print('\nLiteral decipherment by row (S1-S4 = stamp box):')
n = 0
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split(); n += len(toks)
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks).strip())
print(f'({n} tokens)\n\nNormalized (editorial; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
