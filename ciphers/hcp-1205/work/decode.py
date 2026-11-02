"""HCP1205: verify source hashes and decode the sign ledger. Run from the repo root:
   python3 -I ciphers/hcp-1205/work/decode.py"""
import hashlib, os, sys, collections
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/picture-large.jpg': 'a7148b1a7dc61158148480153ac3002e466af8b745da092ab1df3229bfdd848d',
        'source/address-large.jpg': 'fff9a3359beae9567a993842f4deb22a618a7f6c2fcbef6e4aa8dc98ccfacd4b',
        'work/hires/cpc_--_HU__HU_Rakos-Palota-Ujfalu_jolanka-60_pic.jpg': '9c591996b42db41f155b04a401a1c5295f0cd93da2049c9e83b8592f34f8895d',
        'work/hires/cpc_--_HU__HU_Rakos-Palota-Ujfalu_jolanka-60_adr.jpg': 'd21c65a3da7fef379f40eadbfe6ae35ee759d87089622d956167197761019ddb'}
for f, h in HASH.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
KEY = {'5': '5', 'C': 'cs', 'G': 'gy', 'Y': 'y', 'H': 'h', 'P': 'p', 'N': 'n', 'D': 'h', 'M': 'm', '#': '{struck}', '?': '?'}
rows, cnt = [], collections.Counter()
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, toks = line.split()
    out = ''
    for t in toks:
        if t not in KEY and t not in 'abdefgijklmnoöprstuüvyz5': raise SystemExit('unknown token ' + t)
        out += KEY.get(t, t)
        if t != '?': cnt[t] += 1
    rows.append((lab, out))
print('\nLiteral decipherment, one row per written line:')
for lab, txt in rows: print(f'{lab:>3} {txt}')
print(f'\n{sum(cnt.values())} signs; doubtful flags: {sum(r[1].count("?") for r in rows)}')
print('\nNormalized Hungarian (editorial word division, accents and spelling; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
