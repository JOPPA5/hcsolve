"""hcp-1082: decode digit+tick number substitution. Run from repo root:
python3 -I ciphers/hcp-1082/work/decode.py"""
import hashlib, os, sys
B = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASHES = {
 'source/address-large.jpg': '3d6be9dacd893de3cab3ee61fde7fa5e7b2c9b8dbea278d00ecf38097e700ab7',
 'source/picture-large.jpg': '28a810e47129316c6708782fcec7b06321ab65e9ebc3656e4b5fa7d7ca1e5264',
 'work/hires/cpc_1942-08-27_FR_Loiret,-Gare-des-Aubres_FR_Nantes__adr.jpg': 'd4915107c0d1db75216f910880a70d0907e55ceaf12d5f0bd39fc5184b053605',
 'work/hires/cpc_1942-08-27_FR_Loiret,-Gare-des-Aubres_FR_Nantes__pic.jpg': 'fc5b32e637472ae2e5ab0f8f0350958034cebfc1cb7d715a2cc4ad2201655985',
}
for p, h in HASHES.items():
    got = hashlib.sha256(open(os.path.join(B, p), 'rb').read()).hexdigest()
    if got != h:
        sys.exit('HASH MISMATCH ' + p)
print('source hashes OK')
# Key: digit order 1..9,0 = positions 1..10; no mark -> A..J, ' -> K..T, " -> U..Z
ORDER = '1234567890'
ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def dec(tok):
    d, m = tok[0], tok[1:]
    i = ORDER.index(d) + {'': 0, "'": 10, '"': 20}[m]
    return ABC[i] if i < 26 else '?'
# Writer's slips: (line, group, position) -> intended token, all listed in SOLUTION.md
EMEND = {(0,2,4):'5', (6,1,2):"4'", (6,1,3):'2"', (6,1,4):"5'", (7,0,3):"4'", (7,1,2):"9'", (9,0,0):"4'"}
lit, emd = [], []
for li, line in enumerate(l for l in open(os.path.join(B, 'work/transcription.txt')) if l.strip() and not l.startswith('#')):
    a, b = [], []
    for gi, g in enumerate(line.split('|')):
        toks = g.split()
        a.append(''.join(dec(t) for t in toks))
        b.append(''.join(dec(EMEND.get((li, gi, k), t)) for k, t in enumerate(toks)))
    lit.append(' '.join(a)); emd.append(' '.join(b))
print('\nLITERAL (marks exactly as written):'); print('\n'.join(lit))
print('\nWITH THE 7 DISCLOSED SLIP CORRECTIONS:'); print('\n'.join(emd))
