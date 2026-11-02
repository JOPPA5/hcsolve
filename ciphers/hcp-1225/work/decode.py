"""HCP1225: verify scan hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1225/work/decode.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
P = 'work/hires/cpc_1912-02-29_HU__HU_Jasz-Arokszalas_jolanka-06_'
HASH = {'source/picture-large.jpg': 'eeb8fa7a04c251d3ba0a821b188796083a39c66f3fe7731b30e6c18b7b2d49a1',
        P + 'pic.jpg': '64f35fad3cd3aa620fd368c45028e6f48ed3467ae82cd5fbfc8e9a1d88eefb7e',
        'source/address-large.jpg': 'fbfbaead48dbf21a4b5844ba297bafedfb114c10e364d7d22e8227c80ed3cebb',
        P + 'adr.jpg': '14cfcb7423d362385d038d84b65fb4462236cbb0343db70c821a62c642a329cc'}
for f, h in HASH.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
MARK = {'diaeresis': '̈', 'double-acute': '̋', 'acute': '́'}
def dec(t):
    base, _, acc = t.partition(':')
    if base in '.,?-': return base
    s = base if base.startswith('{') else base.lower()
    return unicodedata.normalize('NFC', s + MARK[acc]) if acc else s
print('\nLiteral decipherment, one row per written line (N1 = cipher line beside the address):')
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print('\nNormalized (editorial word division, accents, spelling; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
