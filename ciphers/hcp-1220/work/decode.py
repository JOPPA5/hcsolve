"""HCP1220: check source hashes, decode the sign ledger, print literal rows, the plain stamp note and the normalized text.
Run from the repo root: python3 -I ciphers/hcp-1220/work/decode.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/picture-large.jpg': '20f5c6b7047a6210a3cd1752667b9eb532239613c9df7dcae2b15e4b67c32d9b',
        'source/address-large.jpg': '54af519d04f46e284372e8df3e17d1f18f455636caa8032c90f86ce4d5e757fb',
        'work/hires/cpc_-12-27_HU__HU_Jasz-Arokszalas_jolanka-97_pic.jpg': '52cb35cd5a78b28a8f07c26c4093cee23539c22d579c5fd4d90536a15bfa71fd',
        'work/hires/cpc_-12-27_HU__HU_Jasz-Arokszalas_jolanka-97_adr.jpg': '74f98575225101875577d6cf7ffd85c56de575bb65e619d8554ff18db561ae36'}
for f, h in HASH.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
LETTERS = set('abdefgiHjklmnoprstuvyz') | {'cs'}
MARK = {'a': '́', 'd': '̈'}
def dec(t):
    if t == '|': return ' '
    if t == '?': return '{?}'
    base, _, acc = t.partition(':')
    base = base.rstrip('!^')
    if base not in LETTERS: raise SystemExit('unknown token ' + t)
    base = base.replace('H', 'h')                   # h/p near-homograph, printed h
    return unicodedata.normalize('NFC', base + MARK[acc]) if acc else base
print('\nLiteral decipherment by written row (h = h/p sign; spaces editorial; accents only where a mark was seen):')
n = q = 0
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    n += sum(t not in '|?' for t in toks)
    q += toks.count('?')
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print(f'\n{n} letter signs decoded, plus {q} unassigned mark ({n + q} written signs).\n\nPlain-script note under the stamp (read directly, not ciphertext; [ ] = supplied from the HCP1234 formula, traces only compatible):')
print(open(os.path.join(D, 'work/plain-note.txt'), encoding='utf-8').read())
print('Normalized Hungarian (editorial; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
