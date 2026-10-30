#!/usr/bin/env python3
"""HCP 1375: verify source hashes, decode the full manual transcription (Caesar -1)."""
from pathlib import Path
import hashlib, json, re, string

D = Path(__file__).resolve().parents[1]
data = json.loads((D / 'work/transcription.json').read_text())
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
for name, h in data['source_sha256'].items():
    if sha(D / 'source' / name) != h:
        raise SystemExit(f'Source hash mismatch: {name}')
for name, h in data['hires_sha256'].items():
    if sha(D / 'work/hires' / name) != h:
        raise SystemExit(f'Hires hash mismatch: {name}')
U, L = string.ascii_uppercase, string.ascii_lowercase
dec = str.maketrans(U + L, U[-1] + U[:-1] + L[-1] + L[:-1])
n_cipher = n_abbr = 0
print('Heading (plain):', data['heading_plain_not_enciphered'])
for row in data['rows']:
    out = []
    for tok in row:
        m = re.fullmatch(r'\{(.*)\}', tok)
        if m:
            a = m.group(1)
            n_abbr += sum(c.isalpha() for c in a)
            out.append(f'[{a}]')
        else:
            n_cipher += sum(c.isalpha() for c in tok)
            out.append(tok.translate(dec).upper())
    print(' '.join(out))
print('Dateline (plain):', data['dateline_plain_not_enciphered'])
print(f'{n_cipher} enciphered letters decoded + {n_abbr} abbreviation letters kept literal; hashes OK.')
