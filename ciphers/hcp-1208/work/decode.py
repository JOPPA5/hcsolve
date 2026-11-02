"""HCP1208: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1208/work/decode.py"""
import datetime, hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/picture-large.jpg': 'f9d90d4dd9e5c49a1951cef80760926ab06f9f22a187d8fff8608af63838d9f4',
        'source/address-large.jpg': 'fa3bf04afe9db8e1e06a3b3b032f822f8df8769bfbc711bdb2cfaad1e50ac39d',
        'work/hires/cpc_1914-10-15_HU__HU_Budapest_jolanka-55_pic.jpg': 'ee6064a20dfd52a5abb8c7a26cc598e15f4eb6015ca376e1ddda89f0f2a4259d',
        'work/hires/cpc_1914-10-15_HU__HU_Budapest_jolanka-55_adr.jpg': 'ebfe0a44dd9392bc2c8bdec08be2a84ce39afd5a54845c2df29f96f0f3c18f12'}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f)
    if got != h: sys.exit(1)
KEY = {'B2': 'a', 'SIX': 'b', 'LB': 'c', 'TICK': 'd', 'B3': 'e', 'PLUS': 'f', 'OPEN': 'g', 'TS': 'h', 'DOT': 'i', 'INV': 'j', 'FIVE': 'k',
       'WAVE': 'l', 'S3': 'm', 'S2': 'n', 'LOOP': 'o', 'F': 'r', 'RB': 's', 'GAM': 't', 'X': 'u', 'CHEV': 'v', 'DESC': 'y', 'CROSS': 'z'}
ALT = {('TS', 'p'), ('FIVE', 'g')}  # the only permitted word-sense choices (near-homographs)
MARK = {'d': '\u0308', '2': '\u030b', 'a': '\u0301'}
def dec(tok):
    tok, _, acc = tok.partition(':')
    cls, _, alt = tok.partition('=')
    if cls not in KEY or (acc and acc not in MARK) or (alt and (cls, alt) not in ALT): raise SystemExit('unknown token ' + tok)
    return unicodedata.normalize('NFC', (alt or KEY[cls]) + (MARK[acc] if acc else ''))
n = 0
print('\nLiteral decipherment, one row per written line:')
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split(); n += len(toks)
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print(f'\n{n} signs. Postmark date 1914-10-15 is a {datetime.date(1914,10,15):%A}; the text says holnap, azaz pénteken.')
print('\nNormalized Hungarian (editorial word division, accents and spelling; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
