"""HCP1250: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1250/work/decode.py"""
import hashlib, os, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/picture-large.jpg': 'f008abad4842fd71f7fb0df827bc21974fe756f673a110073eca791e157ab802',
        'source/address-large.jpg': '3fe9ed73e95a0ee27eb4703620981764e235a78aae7ca51da8c58451172a7a9f',
        'work/hires/cpc_1913-06-16_HU__HU_Jasz-Arokszalas_jolanka-38_pic.jpg': 'b6be6c51465f59bcd45f0f92c14c95cff7b3c716566d08f58d84026a8da2d29e',
        'work/hires/cpc_1913-06-16_HU__HU_Jasz-Arokszalas_jolanka-38_adr.jpg': 'a70a24f467827da3fdcd0ef68252e0027ea4b5315cd553afe51c35b232ffd102'}
for f, h in HASH.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
KEY = {'F': 'r', ')': 's', 'X': 'u', '6': 'b', '+': 'f', 'CS': 'cs', '[L]': '[l]', '[A]': '[a]', 'E/I': '{e/i}'}
def dec(t):
    if t in KEY: return KEY[t]
    if t.isalpha(): return t.lower()
    raise SystemExit('unknown token ' + t)
print('\nLiteral decipherment, one row per written line:')
n = 0
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split(); n += len(toks)
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print(f'\n{n} signs. Normalized Hungarian (editorial; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
