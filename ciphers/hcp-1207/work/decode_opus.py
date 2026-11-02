"""HCP1207: verify scan hashes and decode the sign ledger. Run from the repository root:
   python3 -I ciphers/hcp-1207/work/decode_opus.py"""
import hashlib, os, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {
 'source/picture-large.jpg': '656c5de16a969c04b04e03a78bec8919d64dbfa50897a5e05e722d60c330c574',
 'source/address-large.jpg': '9be997ca3b3a74cf02bb31476f06ff274c9f786f2b627dfe424351d34bf27715',
 'work/hires/cpc_--_HU__HU_Budapest_jolanka-62_pic.jpg': 'd9f50cfc2290225c1754b30878b04771e1fa1044c4c7b2ac3891774a003def31',
 'work/hires/cpc_--_HU__HU_Budapest_jolanka-62_adr.jpg': '75faf61d7d6e2c68239494a7cef61e0098941c806c36eb17f6e60a8f3a25c8d8'}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f)
    if got != h: sys.exit(1)
SPECIAL = {'O:': 'ö', 'U"': 'ű', '7': ' 7', '0': ' 0', '[orakor]': ' [orakor] ', '{?}': '{?}', '{R/H}': '{r|h}'}
def dec(t):
    if t in SPECIAL: return SPECIAL[t]
    if t.isalpha() and t.isupper(): return t.lower()
    raise SystemExit('unknown token ' + t)
print('\nLiteral decipherment, one row per written line (h stands for the h/p sign):')
for line in open(os.path.join(D, 'work/ledger-opus.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks).strip())
print('\nNormalized Hungarian (editorial; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized-opus.txt'), encoding='utf-8').read())
