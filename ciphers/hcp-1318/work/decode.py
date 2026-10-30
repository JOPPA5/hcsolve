"""HCP1318: verify source hashes and print the plaintext from the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1318/work/decode.py"""
import hashlib, os, re, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
H = {'source/picture-large.jpg': 'fcf7fab3f91a86be25b2538f6a42068896631284f640f3fb22745137e225dee8',
     'source/address-large.jpg': '0b73093f205343077062dd795dba16bfb3d094e77c0d098d338490ff3548128a',
     'work/hires/cpc_1913--_HU__HU_Jasz-Arokszalas_jolanka-111_pic.jpg': '60f7e23cb851364840df1cb0ec64ab9523fbb0c37abdaf0e31cb182f9bb69aa4',
     'work/hires/cpc_1913--_HU__HU_Jasz-Arokszalas_jolanka-111_adr.jpg': '79b2e0b9697399aa507dd081808ad98a53edf94d8364aaa2f89b31b1e755621d'}
for f, h in H.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
tok = re.compile(r"^(\[?)(cs|[a-zö])('?)(~?)(\]?)$")
print('\nLiteral decipherment ([x] = restored, x? = rests on word sense):')
n = 0
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if line.startswith('#') or not line.strip(): continue
    lab, *ts = line.split()
    out = ''
    for t in ts:
        if t == '.': out += '.'; continue
        if t == 'D': out += 'd?'; n += 1; continue
        m = tok.match(t)
        if not m: sys.exit('bad token ' + t)
        o, b, ac, q, c = m.groups()
        b = {'e': 'é'}.get(b, b) if ac else b
        out += o + b + ('?' if q else '') + c; n += 1
    print(f'{lab} {out}')
print(f'\n{n} signs.\n\nNormalized Hungarian (editorial; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
