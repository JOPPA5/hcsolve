"""HCP1204: verify source hashes, decode the sign ledger, print normalized text.
Run from repo root: python3 -I ciphers/hcp-1204/work/decode.py"""
import hashlib, os, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/picture-large.jpg': '40ccdf48481bc4bf3b7dda69a521ffc3eecbf3b6dc51f27df10b4b2dbe7edfb4',
        'source/address-large.jpg': 'ccf581162966aa92480e6f5d15c9af88bdbc43e3d5315aab236c812e5db3559d',
        'work/hires/cpc_--_HU__HU_Rakos-Palota-Ujfalu_jolanka-59_adr.jpg': '66ed23b179a50755265a0ff051151dc6dc79d0bf08151a34d42200b578e11e8f'}
for f, h in HASH.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
KEY = {'SZ': 'sz', 'Xu': 'u', 'Xz': 'z', 'Y': 'gy', 'C': 'cs', 'A': 'a', '?': '?', '[..]': '[..]'}
def dec(t):
    hidden = t.startswith('{')
    t = t.strip('{}')
    mark = ''
    if t[-1] in '\'"' and len(t) > 1: mark, t = t[-1], t[:-1]
    s = KEY.get(t, t.lower())
    s += {"'": "'", '"': ':'}.get(mark, '')
    return '{' + s + '}' if hidden else s
print('\nLiteral decipherment, row by row (\' accent, : two dots, {x} restored, ? unassigned, h = h/p sign):')
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    out, prev = [], ''
    for t in toks:
        out.append('y' if t == 'Y' and prev in ('N', 'G', 'T', 'L') else dec(t))
        prev = t
    print(f'{lab:>3} ' + ''.join(out))
print('\nNormalized Hungarian (editorial; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
