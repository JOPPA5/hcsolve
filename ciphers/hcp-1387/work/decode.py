#!/usr/bin/env python3
"""Verify original hashes and decode a partial, manually frozen transcript."""
import hashlib
import json
from pathlib import Path

base = Path(__file__).resolve().parents[1]
data = json.loads((base / 'work/transcription.json').read_text())
for name, expected in data['source_sha256'].items():
    actual = hashlib.sha256((base / name).read_bytes()).hexdigest()
    assert actual == expected, f'Original changed: {name}'

def shift(text, amount):
    out = []
    for c in text:
        if 'A' <= c <= 'Z' or 'a' <= c <= 'z':
            first = ord('A' if c.isupper() else 'a')
            c = chr(first + (ord(c) - first + amount) % 26)
        out.append(c)
    return ''.join(out)

count = 0
for row in data['segments']:
    cipher = row['cipher']
    plain = shift(cipher, -1)
    assert shift(plain, 1) == cipher
    count += sum(c.isascii() and c.isalpha() for c in cipher)
    print(f"{row['location']}: {cipher} -> {plain}")
print(f'{count} frozen letter positions; incomplete-message coverage.')
print('Unfrozen handwriting and abbreviations remain unresolved. This is not OCR.')
