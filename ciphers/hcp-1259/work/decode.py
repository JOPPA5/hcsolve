"""HCP1259: check source hashes, decode the sign ledger with the Jolanka key. Run from the repo root:
   python3 -I ciphers/hcp-1259/work/decode.py"""
import hashlib, os, sys, unicodedata
W = os.path.dirname(os.path.abspath(__file__)); D = os.path.dirname(W)
HASH = {'source/picture-large.jpg': '007e59490fffdd3aa47ee1931560d66dd002f1e71a129f40ef2424ce3cbf5020',
 'source/address-large.jpg': '7fd659ab1139353c08cddf91662d101cd5fc19d3db6c3d205eb254509bd9dbe1',
 'work/hires/cpc_1912-04-04_HU__HU_Jasz-Arokszalas_jolanka-14_pic.jpg': '0ab0d5f5ada2ad4ef59d34e1b1f3ca2fb2dbfe45f121add20e17b4f7fb045b5f',
 'work/hires/cpc_1912-04-04_HU__HU_Jasz-Arokszalas_jolanka-14_adr.jpg': '23d47e9635a5302fc184ce0b2d7083ccb715fbeee0c8009deb00472bd072017f'}
for f, h in HASH.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
KEY = dict(gy='gy', b2='a', six='b', sl='d', b3='e', lg='g', th='h', dc='i', ud='y', it='j', sec='k', wv='l', s3='m', s2='n',
           lp='o', Fr='r', rb='s', gm='t', xc='u', ch='v', zc='z', thd='h', io='i/o')
def dec(t):
    if t in '[].': return t
    if t[0] == '~': return t[1:].upper()      # ordinary cursive, not enciphered
    b = t.lstrip('?').rstrip("'")
    s = KEY[b]
    if t.endswith("'"): s = unicodedata.normalize('NFC', s + '́')
    return '{' + s + '}' if t[0] == '?' else s
print('\nLiteral decipherment, row by row (th prints as h = h/p; UPPERCASE plain cursive; {x} blotted; [..] struck):')
for line in open(os.path.join(W, 'ledger.txt'), encoding='utf-8'):
    if line.startswith('#') or not line.strip(): continue
    lab, *t = line.split()
    print(lab, ''.join(dec(x) for x in t))
print('\nNormalized Hungarian (editorial word division, accents and spelling; see SOLUTION.md):')
print(open(os.path.join(W, 'normalized.txt'), encoding='utf-8').read())
