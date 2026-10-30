#!/usr/bin/env python3
"""Reproduce a provisional Caesar reading of a manual transcript, not image OCR."""
from pathlib import Path
import hashlib
import json
import string

ROOT = Path(__file__).resolve().parents[1]
HASHES = {
    'address.jpg': '8910f9ce51e7fcf6734f77e3362aaa76a120ec8882738b5356a1d242e9165a54',
    'picture.jpg': '87257b8aaad4f5d6377c8b5912d292b1dda44098a2b1c9d1445f18f2f2e21f84',
}
for name, expected in HASHES.items():
    actual = hashlib.sha256((ROOT / 'source' / name).read_bytes()).hexdigest()
    if actual != expected:
        raise SystemExit(f'Source hash mismatch: {name}')
data = json.loads((ROOT / 'work' / 'transcription.json').read_text())
table = str.maketrans(string.ascii_lowercase + string.ascii_uppercase,
                     'zabcdefghijklmnopqrstuvwxyZABCDEFGHIJKLMNOPQRSTUVWXY')
print('PARTIAL / PROVISIONAL: manual glyph reading, not OCR or full decipherment')
for line in data['lines']:
    print(line.translate(table))
print('Candidate letter positions:', sum(c in string.ascii_letters for line in data['lines'] for c in line))
print('Uncertain readings:')
for item in data['uncertain_words']:
    print(f"  Line {item['line']}: {item['cipher']} -> {item['reading']}: {item['note']}")
print('Untranscribed:', data['untranscribed'])
