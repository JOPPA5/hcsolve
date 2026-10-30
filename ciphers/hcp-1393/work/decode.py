#!/usr/bin/env python3
"""Replay a MANUAL partial transcription; this does not perform OCR."""
from pathlib import Path
import hashlib
import json
import string

ROOT = Path(__file__).resolve().parents[1]
hashes = json.loads((ROOT / 'work/source-sha256.json').read_text())
for filename, digest in hashes.items():
    assert hashlib.sha256((ROOT / filename).read_bytes()).hexdigest() == digest, filename

def decrypt(s, shift=1):
    result = []
    for c in s:
        alphabet = string.ascii_uppercase if c.isupper() else string.ascii_lowercase
        result.append(alphabet[(alphabet.index(c) - shift) % 26] if c in alphabet else c)
    return ''.join(result)

data = json.loads((ROOT / 'work/transcription.json').read_text())
print('PARTIAL: original files hash-checked; manual transcription, no OCR.')
for line in data['lines']:
    print(f"{line['id']}: {line['cipher']} -> {decrypt(line['cipher'])}")
print('UNFROZEN / NOT DECODED:')
for item in data['unfrozen']:
    print(' - ' + item)
print('LETTER POSITIONS IN COMMITTED/PROVISIONAL EXCERPTS:', sum(c.isalpha() for line in data['lines'] for c in line['cipher']))
