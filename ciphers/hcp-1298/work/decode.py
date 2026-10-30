"""HCP1298: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1298/work/decode.py"""
import hashlib, json, os, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/picture-large.jpg': '92838831ef52d90ddedba33622077f4440529592f52fa90a92ff7f69458e58b0',
        'source/address-large.jpg': '32b6b853c79e25d039834a4b2ae653b2362d0ddb224f8d1f03661de9c8893fbe',
        'work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-77_pic.jpg': 'c6062ac587cfebaba6efa0de053ad8adf554442b472ef37adcced91f2c98fa3a',
        'work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-77_adr.jpg': '3f43429759f71e54fd73825c6bc8450a03658a7e243ffc6344427c1d63993e10'}
for f, h in HASH.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
KEY = json.load(open(os.path.join(D, 'work/key.json'), encoding='utf-8'))
def dec(t):
    if t[0] == '[': return '·'
    if t.isdigit(): return t
    q = t.endswith('?'); s = KEY[t.rstrip('?')]
    return s + ('?' if q else '')
print('\nLiteral decipherment (h stands for the h/p sign; ? = value rests on word sense; · = mark with no letter value):')
n = 0
for line in open(os.path.join(D, 'work/sign-ledger.txt'), encoding='utf-8'):
    if not line.strip() or line[0] == '#': continue
    lab, *t = line.split(); n += len(t)
    print(f'{lab} ' + ''.join(dec(x) for x in t))
print(f'\n{n} tokens.\n\nNormalized Hungarian (editorial; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
