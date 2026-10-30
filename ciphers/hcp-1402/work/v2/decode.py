#!/usr/bin/env python3
"""HCP 1402: verify source hashes, decode the full manual transcription (Caesar -1)."""
from pathlib import Path
import hashlib, json, re, string

D = Path(__file__).resolve().parents[2]
data = json.loads((D / 'work/v2/transcription.json').read_text())
for name, h in data['source_sha256'].items():
    if hashlib.sha256((D / 'source' / name).read_bytes()).hexdigest() != h:
        raise SystemExit(f'Source hash mismatch: {name}')
U, L = string.ascii_uppercase, string.ascii_lowercase
dec = str.maketrans(U + L, U[-1] + U[:-1] + L[-1] + L[:-1])
enc = str.maketrans(U[-1] + U[:-1] + L[-1] + L[:-1], U + L)
n_cipher = n_abbr = 0
print('Heading (plain):', data['heading_plain_not_enciphered'])
for row in data['rows']:
    out = []
    for tok in row:
        m = re.fullmatch(r'\{(.*)\}', tok)
        if m:
            a = m.group(1)
            n_abbr += sum(c.isalpha() for c in a)
            out.append(f'[{a} | shifted: {a.translate(dec)}]')
        else:
            p = tok.translate(dec)
            assert p.translate(enc) == tok
            n_cipher += sum(c.isalpha() for c in tok)
            out.append(p.upper())
    print(' '.join(out))
print(f'{n_cipher} enciphered letters decoded + {n_abbr} abbreviation letters kept literal; hashes OK.')
