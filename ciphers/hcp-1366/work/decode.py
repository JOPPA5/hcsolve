#!/usr/bin/env python3
"""HCP 1366: verify file hashes, decode the manual transcription (Caesar -1), print the plaintext."""
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
nc = na = 0
print('Plain (not enciphered):', ' | '.join(data['plain_not_enciphered']))
for row in data['rows']:
    out = []
    for tok in row:
        m = re.fullmatch(r'\{(.*)\}', tok)
        if m:
            a = m.group(1)
            na += sum(c.isalpha() for c in a)
            out.append(f'[{a} | shifted: {a.translate(dec)}]')
        elif tok == '&':
            out.append('&')
        else:
            p = tok.translate(dec)
            assert p.translate(enc) == tok
            nc += sum(c.isalpha() for c in tok)
            out.append(p.upper())
    print(' '.join(out))
print(f'{nc} enciphered letters decoded + {na} abbreviation letters kept literal; hashes OK.')
