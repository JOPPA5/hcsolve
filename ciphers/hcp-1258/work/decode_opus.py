"""HCP1258: verify source hashes and decode the sign-class ledger with the family key. Run from repo root:
   python3 -I ciphers/hcp-1258/work/decode_opus.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/picture-large.jpg': '9f1380c2b5a050b0a048f474112f9a03558954150887f571349d62768f14baf7',
        'source/address-large.jpg': '71e785b8ce1c7f3d3c63c89895200bb199351bf2d22ffbf14cdba98ba4d53aaa',
        'work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-70_pic.jpg': 'f2e40e79722340185a7cfae5319a3d3cd5a19499a70554d4113bf166aa3cb6a2',
        'work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-70_adr.jpg': 'f37a5f5edf2c4b25bf437c6a22ce4ffee61fb30a3a75144540aada287cf2db7d'}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f)
    if got != h: sys.exit(1)
KEY = {'BAR2': 'a', 'SIX': 'b', 'LBOWL': 'c', 'TICK': 'd', 'BAR3': 'e', 'CROSS': 'f', 'GLOOP': 'g', 'TALL': 'h',
       'CURVE': 'i', 'INVT': 'j', 'SECT': 'k', 'WAVE': 'l', 'STROKE3': 'm', 'STROKE2': 'n', 'LOOP': 'o', 'FLIKE': 'r',
       'RBOWL': 's', 'GAMMA': 't', 'XPLAIN': 'u', 'CHEV': 'v', 'DESC': 'y', 'XTAIL': 'z',
       'LOOPDESC': 'gy', 'JOINTY': 'ty', 'OPPBOWL': 'cs'}
MARK = {'a': '\u0301', 'd': '\u0308', 'dd': '\u030b'}
def dec(t):
    if t == '.' or t.isdigit(): return t
    if t.startswith('['): return '[' + dec(t[1:-1]) + ']'
    base, _, acc = t.partition(':')
    return unicodedata.normalize('NFC', KEY[base] + MARK[acc]) if acc else KEY[base]
print('\nLiteral decipherment, one row per written line (h stands for the h/p sign; [x] = restoration of a hidden sign):')
for line in open(os.path.join(D, 'work/ledger-signs.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    print(f'{lab:>3} {"".join(dec(t) for t in toks)}')
print('\nNormalized Hungarian (editorial word division, accents and spelling; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized-opus.txt'), encoding='utf-8').read())
