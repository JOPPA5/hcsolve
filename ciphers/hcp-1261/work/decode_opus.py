"""HCP1261: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1261/work/decode_opus.py"""
import hashlib, os, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
H = 'cpc_1912-03-07_HU__HU_Jasz-Arokszalas_jolanka-07'
HASH = {'source/picture-large.jpg': '7085f9d28eee84e6e8f8295a70c72e4b35f6101d14a469652ffd70b9b170a1b8',
        'source/address-large.jpg': '91ec6c4d5684d7ae3fbe3dff7281bc8376b3376ed3844be883689fbd07cc8bba',
        f'work/hires/{H}_pic.jpg': '8ce184235264910bae164f29b5626257802e5d8e40affba8910b3ba608d6b12e',
        f'work/hires/{H}_adr.jpg': 'e736979cf5c3851a2c75a26333137b76cf16f0ed069490a53d5a1d6dbcde3d70'}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f)
    if got != h: sys.exit(1)
KEY = {'F': 'r', ')': 's', 'X': 'u', '6': 'b', '+': 'f', 'GY': 'gy', 'CS': 'cs', '.': '.'}
ACC = {'X:d': 'ü', 'O:d': 'ö', 'O:a': 'ó'}
def dec(t):
    if t in ACC: return ACC[t]
    if t == '#!': return '[#]'  # blot with no value of its own
    if t[-1] == '^': return t[:-1].lower() + '^'  # plain letter, not a cipher sign
    flag = ''
    if t[-1] in '!?' and len(t) > 1: t, flag = t[:-1], '*'
    s = KEY.get(t, t.lower() if t.isalpha() and len(t) == 1 else None)
    if s is None: raise SystemExit('unknown token ' + t)
    return s + flag
n = 0
print('\nLiteral decipherment, one row per written line (* = blotted or ambiguous sign, [#] = blot without a value, ^ = plain letter; see SOLUTION.md):')
for line in open(os.path.join(D, 'work/ledger-opus.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    n += len(toks)
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks) + (' + plain: egy igaz' if lab == 'S6' else ''))
print(' S7 plain: sziv\n\n%d written signs in the ledger (cipher signs and 2 dots, 1 valueless blot, 1 plain M).\n\nNormalized Hungarian (editorial; see SOLUTION.md):' % n)
print(open(os.path.join(D, 'work/normalized-opus.txt'), encoding='utf-8').read())
