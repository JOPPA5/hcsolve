"""HCP1295: verify source hashes and print the ledger. Run from repo root: python3 -I ciphers/hcp-1295/work/decode_opus.py
The ledger already holds key values (the signs have no ASCII form); this checks hashes, token validity and prints the rows."""
import hashlib, os, re, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/picture-large.jpg': 'f4e3c9efe2ed30f2aa7a882331bcf95d0c8d7dc9c2de5f2f2883e12542edac20',
 'source/address-large.jpg': 'a133d6233e4980bdcd0f9ed88ed04c2b140377fe17a322051bb84b86eebf4dfb',
 'work/hires/cpc_1912-06-06_HU__HU_Jasz-Arokszalas_jolanka-24_pic.jpg': '561dc4c946e6b17310293120575e4f66845d7bfada9e2c7d90ea0ce57ae36fd7',
 'work/hires/cpc_1912-06-06_HU__HU_Jasz-Arokszalas_jolanka-24_adr.jpg': 'e96cc9b6d08587ca7ab91f57641226935515215a28ce0d960f66887fe44a9e92'}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f)
    if got != h: sys.exit(1)
OK = re.compile(r'^([a-z]|gy|cs|[a-z]:|\[[a-z]\]|\{.*\}|\.|-|3)$')
n = 0
print('\nLiteral rows (h = h/p/d group; {..} = see SOLUTION.md; [x] = restoration):')
for line in open(os.path.join(D, 'work/ledger-opus.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *t = line.split()
    bad = [x for x in t if not OK.match(x)]
    if bad: sys.exit(f'bad token {bad} in {lab}')
    n += len(t)
    print(f'{lab:>3} ' + ''.join(x.replace(':', '̈') for x in t))
print(f'\n{n} tokens\n\nNormalized (partial; braces mark unresolved words):')
print(open(os.path.join(D, 'work/normalized-opus.txt'), encoding='utf-8').read())
