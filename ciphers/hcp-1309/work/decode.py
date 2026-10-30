"""HCP1309: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1309/work/decode.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/address-large.jpg': 'b3d9216d007fcc0d6fb98efadf9c32527153d0ec535b651e9d543726cef09a5e',
        'source/picture-large.jpg': '397e3032a5d38fb9c321b5cf6cdaa69196bc1c70050667ada04136c095ac54a5',
        'work/hires/cpc_1912--_HU__HU_Jasz-Arokszalas_jolanka-99_adr.jpg': 'a06270351424fd06a7c8bbba6b9e9e819a3bf6a92b20c3840d879c3f488190c3',
        'work/hires/cpc_1912--_HU__HU_Jasz-Arokszalas_jolanka-99_pic.jpg': '6641ebb7b740afdd0163503e55814e0c44e6e5799ee0ae1547963b1905da6e07'}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f)
    if got != h: sys.exit(1)
KEY = {'F': 'r', ')': 's', 'X': 'u', '6': 'b', '+': 'f', 'CS': 'cs'}
MARK = {'dia': '̈', 'tick': '́'}
def dec(tok):
    if tok[0] in '[{': return tok
    base, _, acc = tok.partition(':')
    s = KEY.get(base, base.lower() if base.isalpha() else None)
    if s is None: raise SystemExit('unknown token ' + tok)
    return unicodedata.normalize('NFC', s + MARK[acc]) if acc else s
print('\nLiteral decipherment, one row per written line:')
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print('\nNormalized Hungarian (editorial word division, accents and spelling; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
