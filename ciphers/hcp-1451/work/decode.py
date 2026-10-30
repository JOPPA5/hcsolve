#!/usr/bin/env python3
"""HCP 1451: verify source hashes, then decode the transcription with Atbash (A<->Z, B<->Y, ...)."""
import hashlib, json, string
from pathlib import Path
root = Path(__file__).resolve().parents[1]
for name, digest in json.loads((root/'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((root/'source'/name).read_bytes()).hexdigest() == digest, 'hash mismatch: ' + name
U, L = string.ascii_uppercase, string.ascii_lowercase
key = str.maketrans(U + L, U[::-1] + L[::-1])
rows = json.loads((root/'work/transcription.json').read_text())['rows']
out = []
for r in rows:
    p = r['cipher'].translate(key)
    assert p.translate(key) == r['cipher']
    assert r['diplomatic'].replace('J', 'Z').replace('j', 'z') == r['cipher'], 'diplomatic/normalised mismatch'
    print(f"{r['cipher']:8s} -> {p}")
    out.append(p)
print('Plaintext:', ' '.join(out))
print('Source hashes OK;', sum(len(r['cipher']) for r in rows), 'cipher letters decoded.')
