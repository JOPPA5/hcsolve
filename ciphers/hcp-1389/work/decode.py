#!/usr/bin/env python3
"""Decode a frozen MANUAL transcription; hashes anchor images, not OCR validation."""
import hashlib, json
from pathlib import Path
root = Path(__file__).resolve().parents[1]
expected = {
    'address.jpg': 'b1e6bb27e323385a8f5f49650e89065541731e80c68d1bdf4cad16006ebc3cb0',
    'picture.jpg': '7a7c9236d0c0f6c60d1ccfc0a7fed8711feca89e4e0509de1e3262feddef6abc',
    'metadata.md': 'f5f73261bc96f4fd9fb44eecadca850d2fb782288fda2e9c922437bd0973159c',
}
for name, digest in expected.items():
    assert hashlib.sha256((root/'source'/name).read_bytes()).hexdigest() == digest, name
transcript = json.loads((root/'work/transcript.json').read_text())
def decode(s):
    return ''.join(chr((ord(c)-ord('A')-1)%26+ord('A')) if 'A'<=c<='Z' else chr((ord(c)-ord('a')-1)%26+ord('a')) if 'a'<=c<='z' else c for c in s)
print('PARTIAL: frozen manually transcribed lines only; unresolved marks excluded.')
for line in transcript['frozen_lines']:
    print(decode(line))
print('Frozen letters:', sum(c.isascii() and c.isalpha() for s in transcript['frozen_lines'] for c in s))
print('Unresolved regions:')
for note in transcript['unresolved']:
    print('-', note)
