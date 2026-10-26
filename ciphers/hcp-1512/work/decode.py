#!/usr/bin/env python3
"""Decode a scan-derived manual transcript; this is not OCR."""
from pathlib import Path
import hashlib, json
p = Path(__file__).resolve().parents[1]
for name, digest in json.loads((p/'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((p/'source'/name).read_bytes()).hexdigest() == digest
key = json.loads((p/'work/key.json').read_text())
variant = {'%': 'P'}  # Phi-shaped overwritten A, not a new plaintext letter
base = {g:v for g,v in key.items() if g not in variant}
assert len(set(base.values())) == len(base)
assert all(key[g] == key[canonical] for g,canonical in variant.items())
raw = (p/'work/transcription.txt').read_text()
punctuation = set(".,'")
assert all(c.isspace() or c in punctuation or c in key for c in raw)
text = ''.join(key.get(c,c) for c in raw)
inverse = {v:k for k,v in base.items()}
canonical_raw = ''.join(variant.get(c,c) for c in raw)
assert ''.join(inverse.get(c,c) for c in text) == canonical_raw
used = {c for c in raw if c in key}
assert used == set(key)
assert sum(c in key for c in raw) == 281
print(text, end='')
print(f'{sum(c in key for c in raw)} cipher positions, {len(used)} visual glyph IDs, {len(base)} base glyph types / plaintext letters.')
print('Source hashes, full token coverage and canonical re-encryption passed.')
print('Re-encryption canonicalizes the explicit %-to-P overwrite variant; it does not reconstruct its original pen strokes.')
