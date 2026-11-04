"""Decode hcp-1186. Run from repo root: python3 -I ciphers/hcp-1186/work/decode.py"""
import hashlib, os, re, sys
D = os.path.dirname(os.path.abspath(__file__))
C = os.path.dirname(D)
HASHES = {
 'source/picture-large.jpg': 'b5d753d6404cd1e6c473de6c6f76cfdf2338ee4014e9e3bbbec2e9f5bd46163f',
 'source/address-large.jpg': 'a0d877b628d87a65a97c20ab1c3bc819ac64193ab6c9fb0ae10aecb59e5bb8da',
 'work/hires/cpc_1904-10-12_UK_Dorchester_UK_Dorchester__pic.jpg': '51cbce2476af1b6a415e2de4d4d92b843dc08be405dacefb870ed3c604bf12d3',
 'work/hires/cpc_1904-10-12_UK_Dorchester_UK_Dorchester__adr.jpg': '2a299b972c0948cd4833bdec0944ec088a4e9de5c00519530ffa255b32a7f567',
}
for p, h in HASHES.items():
    got = hashlib.sha256(open(os.path.join(C, p), 'rb').read()).hexdigest()
    if got != h:
        sys.exit('HASH MISMATCH ' + p)
print('source hashes OK (%d files)' % len(HASHES))
KEY = {'6':'A','k':'B','w':'C','n':'D','9':'E','o':'F','5':'G','u':'H','4':'I','t':'K',
       '2':'L','M':'M','8':'N','3':'O','R':'R','a':'S','y':'T','1':'U','v':'V','e':'W',
       'i':'Y','&':'&'}
inv = {}
for k, v in KEY.items():
    assert v not in inv, 'key not one-to-one: ' + v
    inv[v] = k
out = []
for line in open(os.path.join(D, 'transcription.txt')):
    line = line.rstrip('\n')
    if not line or line.startswith('#'):
        continue
    parts = re.split(r'(\[[^\]]*\])', line)
    res = []
    for p in parts:
        if p.startswith('['):
            res.append(p[1:-1].upper()); continue
        res.append(' '.join(''.join(KEY[c] for c in w) for w in p.split()))
    out.append(' '.join(x for x in res if x))
print('\n'.join(out))
