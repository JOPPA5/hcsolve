#!/usr/bin/env python3
"""Decode an own manual digit/Latin transcription, not OCR."""
from pathlib import Path
import hashlib, json, string

p = Path(__file__).resolve().parents[1]
for name, digest in json.loads((p/'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((p/'source'/name).read_bytes()).hexdigest() == digest
raw = (p/'work/transcript.txt').read_text()
key = dict(zip('123456789', 'AEIOUTNSR'))
inverse = {v:k for k,v in key.items()}
out = ''.join(key.get(c, c.upper()) for c in raw)
assert ''.join(inverse.get(c, c) for c in out) == raw.upper()
assert set(c for c in raw if c.isdigit()) == set(key)
assert all(c in string.ascii_letters + string.digits + ' .\n' for c in raw)
print(out, end='')
print(f'\n{sum(c.isalnum() for c in raw)} manually transcribed letter positions; '
      f'{sum(c.isdigit() for c in raw)} digit substitutions.')
print('Source hashes and inverse encoding passed. Not OCR/independent scan validation.')
