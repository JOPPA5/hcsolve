#!/usr/bin/env python3
"""HCP 1392: check source hashes, decrypt the full manual transcript (Caesar -1), verify round trip."""
from pathlib import Path
import hashlib, json, string

base = Path(__file__).resolve().parents[1]
expected = {
    'address.jpg': '5d3920d8c9d77569101046f582bed51d3deab473e94a9dd6c9803a9527cff617',
    'picture.jpg': '31c4b0d26c4a0bfaf0dcd6e8978eecedca70b83b57ed01202e612fbb2dbb8191',
}
for name, digest in expected.items():
    if hashlib.sha256((base / 'source' / name).read_bytes()).hexdigest() != digest:
        raise SystemExit(f'Source hash mismatch: {name}')
print('source hashes OK')
up, lo = string.ascii_uppercase, string.ascii_lowercase
dec = str.maketrans(up + lo, up[-1] + up[:-1] + lo[-1] + lo[:-1])
enc = str.maketrans(up[-1] + up[:-1] + lo[-1] + lo[:-1], up + lo)
data = json.loads((base / 'work' / 'transcript_full.json').read_text())
n = 0
print('cipher                 -> plain')
for line in data['cipher_lines']:
    p = line.translate(dec)
    assert p.translate(enc) == line
    n += sum(c.isalpha() for c in line)
    print(f'{line:22s} -> {p}')
print('alphabetic cipher letters decoded:', n)
for k, v in data['literal_groups'].items():
    print('not decoded, literal:', k, '=', v)
print('reading: My Own. Dearest / Sending. a. card / to. Y— instead / of. letter. [N & L!] /'
      ' From. your own [N^b abbreviation, literal] / Girl')
print('plain fields (not enciphered):', data['plain_fields'])
