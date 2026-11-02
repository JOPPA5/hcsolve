"""HCP1286: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1286/work/decode_rev2.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
H = {'source/address-large.jpg': '427e179e45452be26d8a6133bfbd6a965026e99bf74804138372b99e66277b36',
     'source/picture-large.jpg': 'fac36a672881481fdadb56488ea36a27fc4c887ce336d5313b622384da1dc447',
     'work/hires/cpc_1914-01-10_HU__HU_Jasz-Arokszalas_jolanka-47_adr.jpg': '364f251fb20119ce6829a4375be3dd76aeae3f6de93c742a732bb714909e750c'}
for f, h in H.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
KEY = {'F': 'r', ')': 's', 'X': 'u', '6': 'b', '+': 'f', 'H': 'h', 'GY': 'gy', 'CS': 'cs', 'G?': 'g',
       '|': '{|}', '.': '.', '?': '?', '1': '1', '2': '2', '9': '{9}'}
MARK = {'d': '̈', 'a': '́'}
def dec(t):
    hid = t.startswith('[')
    t = t.strip('[]')
    b, _, a = t.partition(':')
    s = KEY.get(b, b.lower() if b.isalpha() else None)
    if s is None: raise SystemExit('unknown token ' + t)
    if a: s = unicodedata.normalize('NFC', s + MARK[a])
    return '[' + s + ']' if hid else s
print('\nLiteral decipherment (h = the h/p sign; [x] hidden sign; {|} stray stroke):')
for l in open(os.path.join(D, 'work/ledger-rev2.txt'), encoding='utf-8'):
    if l.strip() and not l.startswith('#'):
        lab, *toks = l.split()
        print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print('\nNormalized Hungarian (editorial; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized-rev2.txt'), encoding='utf-8').read())
