#!/usr/bin/env python3
"""HCP 1352: verify file hashes, decode the full manual transcription (Caesar -1)."""
from pathlib import Path
import hashlib, json, re, string

D = Path(__file__).resolve().parents[1]
data = json.loads((D / 'work/transcription.json').read_text())
for name, h in data['source_sha256'].items():
    if hashlib.sha256((D / name).read_bytes()).hexdigest() != h:
        raise SystemExit(f'Hash mismatch: {name}')
U, L = string.ascii_uppercase, string.ascii_lowercase
dec = str.maketrans(U + L, U[-1] + U[:-1] + L[-1] + L[:-1])
enc = str.maketrans(U[-1] + U[:-1] + L[-1] + L[:-1], U + L)
n = lit = 0
diffs = []
print('Heading (plain):', data['heading_plain_not_enciphered'])
for row in data['rows']:
    out = []
    for seen, norm in row:
        m = re.fullmatch(r'\{(.*)\}', norm)
        if m:
            a = m.group(1)
            lit += sum(c.isalpha() for c in a)
            out.append(f'[{a} | shifted: {a.translate(dec)}]')
            continue
        p = norm.translate(dec)
        assert p.translate(enc) == norm
        n += sum(c.isalpha() for c in norm)
        out.append(p.upper())
        if seen != norm:
            diffs.append(f'{seen} -> {norm}')
    print(' '.join(out))
print(f'{n} enciphered letters decoded + {lit} group letters kept literal; hashes OK.')
print('Sign-level normalisations:', '; '.join(diffs))
