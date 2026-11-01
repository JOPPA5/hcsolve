"""HCP1251: verify source hashes, validate the ledger against key.json, print the reading.
The ledger is a manual transcription already written in plaintext letters; no key is applied here.
Run from the repository root: python3 -I ciphers/hcp-1251/work/decode.py"""
import hashlib, json, os, re, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/picture-large.jpg': '6afbc565bd2a951857d97b6d6d08c976d539ee2555ddda4315df3828c1aeeca4',
        'source/address-large.jpg': '0bd8e91cb1e5383cce9c9ae32b2057e195ac28dd88d5f6b56416e663502fdb4f',
        'work/hires/cpc_1914-04-12_HU__HU_Jasz-Arokszalas_jolanka-52_pic.jpg': '3b445312d0ab519ff5d9e9235b25c4eb891e84832e70ba97ccc45165b069b6b5',
        'work/hires/cpc_1914-04-12_HU__HU_Jasz-Arokszalas_jolanka-52_adr.jpg': 'a47671e612764b8b12de17823173cb2ddc9f876dfe7da78e31e5f2985787d7cd'}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f)
    if got != h: sys.exit(1)
key = json.load(open(os.path.join(D, 'work/key.json'), encoding='utf-8'))
known = set(key['signs']) | set('öüőóéá')
n = 0
print('\nLiteral decipherment, one row per written line (h = h/p sign, [ ] restored, { } doubtful):')
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, text = line.split()
    for ch in re.sub(r'[\[\]{}]', '', text):
        if ch not in known: sys.exit('unknown sign ' + ch + ' in row ' + lab)
        n += 1
    print(f'{lab:>3} {text.replace("c", "cs")}')
print('\nSigns in ledger:', n)
print('\nNormalized Hungarian (editorial word division, accents, spelling; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
