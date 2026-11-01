"""HCP1267: verify scan hashes and decode the sign ledger. From the repo root:
   python3 -I ciphers/hcp-1267/work/decode.py"""
import hashlib, os, re, shlex, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/address-large.jpg': '059a8108e443135ed60006aca5d67a5a6694249151ea48f89e5c9f59afd37bce',
        'source/picture-large.jpg': '884a0f71eff526fc2568f60c522f3f15f5bc324fe9b68a83b25cee79239d1287',
        'work/hires/cpc_1913-07-13_HU__HU_Jasz-Arokszalas_jolanka-39_adr.jpg': '05377f69fcbea69dc904bd5114259abf74c8cd15ad14ac9b6144eec6b31ce5ea',
        'work/hires/cpc_1913-07-13_HU__HU_Jasz-Arokszalas_jolanka-39_pic.jpg': '973ff0087ee5dd2ee8f5fd8e953ba4ddf6525b6c7087832b46ce2ff25aea1c92'}
for f, h in HASH.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
KEY = {'F': 'r', ')': 's', 'X': 'u', '6': 'b', '+': 'f', 'H': 'h', 'CS': 'cs'}
def dec(t):
    if t.startswith('{'): return t
    if t.startswith('"'): return t.strip('"')
    m = re.fullmatch(r"(\[?)([A-Z]+|\)|\+|6)(\]?)(\?)?(:'|:)?", t)
    if not m: raise SystemExit('bad token ' + t)
    s = KEY.get(m[2], m[2].lower())
    if m[5]: s = unicodedata.normalize('NFC', s + ('́' if m[5] == ":'" else '̈'))
    return (m[1] + s + m[3]) + ('?' if m[4] else '')
print('\nLiteral decipherment, one row per written line (h stands for the h/p sign; [x] restored; ? depends on word sense):')
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, rest = line.split(None, 1)
    toks = re.findall(r'"[^"]*"|\S+', rest)
    print(f'{lab:>3} ' + ''.join(dec(t) if not t.startswith('"') else ' ' + t.strip('"') + ' ' for t in toks))
print('\nNormalized Hungarian (word division, accents and bracketed letters are editorial):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
