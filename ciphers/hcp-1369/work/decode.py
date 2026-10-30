#!/usr/bin/env python3
"""HCP 1369: verify hashes, decode the manual transcription (Caesar -1)."""
from pathlib import Path
import hashlib, json, re, string

D = Path(__file__).resolve().parents[1]
data = json.loads((D / 'work/transcription.json').read_text())
for name, h in data['source_sha256'].items():
    if hashlib.sha256((D / name).read_bytes()).hexdigest() != h:
        raise SystemExit(f'Source hash mismatch: {name}')
U, L = string.ascii_uppercase, string.ascii_lowercase
dec = str.maketrans(U + L, U[-1] + U[:-1] + L[-1] + L[:-1])
enc = str.maketrans(U[-1] + U[:-1] + L[-1] + L[:-1], U + L)
n_cipher = n_lit = 0
print('Heading (plain):', data['heading_plain_not_enciphered'])
for row in data['rows']:
    out = []
    for tok in row:
        m = re.fullmatch(r'\{(.*)\}', tok)
        if m:
            n_lit += sum(c.isalpha() for c in m.group(1))
            out.append(m.group(1))
            continue
        plain = tok
        p = plain.translate(dec)
        assert p.translate(enc) == plain
        n_cipher += sum(c.isalpha() for c in plain)
        out.append(p.upper())
    print(' '.join(out))
print(f"{n_cipher} letters read and decoded, {len(data['restored_tokens'])} restored tokens, {n_lit} kept literal; hashes OK.")
