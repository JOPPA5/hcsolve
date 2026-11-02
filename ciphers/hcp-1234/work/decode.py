"""HCP1234: check source hashes, decode the sign ledger, print literal rows and the normalized text.
Run from the repo root: python3 -I ciphers/hcp-1234/work/decode.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/picture-large.jpg': '70a229246ce10f652d0a44baa371f41ccbc4178c2f7a6bf3b97c61c35cbcc123',
        'source/address-large.jpg': 'ca90d9452202ae0e41eb5b42f00280ad5c9f98f014cef8d072596032fbec2e78',
        'work/hires/cpc_1913-12-16_HU__HU_Jasz-Arokszalas_jolanka-45_pic.jpg': 'c35812de636c76078f346c379e9f02199da4c86140554c291213b95acb3c70ae',
        'work/hires/cpc_1913-12-16_HU__HU_Jasz-Arokszalas_jolanka-45_adr.jpg': '07163aee8470d80805948846cb7654a4332f69451f875385eff08b66394bb38f'}
for f, h in HASH.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
LETTERS = set('abcdefghijklmnoprstuvyz')
MARK = {'a': '́', 'd': '̈', '2': '̋'}
def dec(t):
    if t == '|': return ' '
    if t.endswith('*'): return t[:-1].upper()      # plain cursive Latin letter, not a cipher sign
    base, _, acc = t.partition(':')
    base = base.rstrip('!')
    if base == 'H': base = 'h'                      # h/p near-homograph, printed h
    if base not in LETTERS: raise SystemExit('unknown token ' + t)
    return unicodedata.normalize('NFC', base + MARK[acc]) if acc else base
print('\nLiteral decipherment by written row (h = h/p sign; spaces editorial; accents only where a mark was seen):')
n = 0
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    n += sum(t != '|' for t in toks)
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print(f'\n{n} signs decoded.\n\nNormalized Hungarian (editorial; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
