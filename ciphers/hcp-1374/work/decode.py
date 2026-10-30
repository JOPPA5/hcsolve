#!/usr/bin/env python3
"""HCP 1374: verify source hashes, decode the manual transcription (Caesar -1)."""
from pathlib import Path
import hashlib, json, re, string

D = Path(__file__).resolve().parents[1]
data = json.loads((D / 'work/transcription.json').read_text())
for name, h in data['sha256'].items():
    if hashlib.sha256((D / name).read_bytes()).hexdigest() != h:
        raise SystemExit(f'Source hash mismatch: {name}')
U, L = string.ascii_uppercase, string.ascii_lowercase
dec = str.maketrans(U + L, U[-1] + U[:-1] + L[-1] + L[:-1])
enc = str.maketrans(U[-1] + U[:-1] + L[-1] + L[:-1], U + L)
n_cipher = n_abbr = n_emended = 0
print('Plain (not enciphered):', data['plain_heading'], '/', data['plain_date'])
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
            n_emended += len(re.findall(r'\[[A-Za-z]\]', tok))
            out.append(p.upper())
    print(' '.join(out))
print(f'{n_cipher} enciphered letters decoded ({n_cipher - n_emended} read, {n_emended} emended, in square brackets)'
      f' + {n_abbr} abbreviation letters kept literal; hashes OK.')
