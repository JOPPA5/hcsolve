"""HCP1312: verify source hashes, decode the sign ledger, print the plaintext.
Run from the repository root:  python3 -I ciphers/hcp-1312/work/decode_rev2.py
Output: (x) washed sign read from enhanced crops; {x} restored sign, shape count only. In the normalized text [x] is a letter the card does not have as written.
"""
import hashlib, os
D = 'ciphers/hcp-1312'
HASH = {'source/picture-large.jpg': 'dd64d57e9cad75d9c542fa0982c2351a844f704e7823a64ec90730e2b923db5c',
        'source/address-large.jpg': 'ff0aa5f61da71f1a043a027d98a9383980339dec1274607fdc2db94eea778903'}
for f, h in HASH.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(f, 'OK' if ok else 'HASH MISMATCH')
# Jolanka-family key (hcp-1216), sign class -> letter. tall+short is the h/p near-homograph,
# resolved in the ledger as tallH / tallP. lbowl and lbowlbar stand where sense needs s and cs.
KEY = dict(bars2='a', six='b', lbowl='c', lbowlbar='c', opp='cs', slashd='d', bars3='e', loopg='g',
           gy='gy', tallH='h', tallP='p', icurve='i', invT='j', sect='k', wave='l', st3='m', st2='n',
           oloop='o', oloopdots='ö', F='r', rbowl='s', gamma='t', xcross='u', chev='v', zcross='z')
for line in open(os.path.join(D, 'work/ledger-rev2.txt'), encoding='utf-8'):
    if line.startswith('#') or not line.strip():
        continue
    row, *toks = line.split()
    out = ''
    for t in toks:
        c = KEY[t.rstrip('~^')]
        out += '(%s)' % c if t.endswith('~') else '{%s}' % c if t.endswith('^') else c
    print(row, out)
print()
print(open(os.path.join(D, 'work/normalized-rev2.txt'), encoding='utf-8').read())
