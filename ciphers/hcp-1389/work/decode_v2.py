#!/usr/bin/env python3
"""HCP 1389 partial decode (v2, Claude Opus 5.5, 2026-10-29). Checks source hashes, applies Caesar -1
to the lines read from the scan, and lists the unresolved fields literally. Run from the repo root."""
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
print('source hashes OK')
t = json.loads((root/'work/transcription_v2.json').read_text())
def dec(s):
    return ''.join(chr((ord(c)-65-1)%26+65) if 'A'<=c<='Z' else chr((ord(c)-97-1)%26+97) if 'a'<=c<='z' else c for c in s)
print('PARTIAL READING (unresolved fields in brackets, not decoded):')
for l in t['lines']:
    if l['status'].startswith('read'):
        print(f"  {l['cipher']:<20} -> {dec(l['cipher'])}")
    else:
        print(f"  [{l['cipher']}]  {l['status']}: {l.get('note','')}")
n = sum(c.isalpha() for s in t['decoded_lines'] for c in s)
print('decoded cipher letters:', n)
print('literal shift of the unresolved line-4 word usjot ->', dec('usjot'), '(not English; left unresolved)')
