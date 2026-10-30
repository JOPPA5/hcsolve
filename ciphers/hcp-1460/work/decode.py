#!/usr/bin/env python3
"""Confirmed prefix only; manual transcript, no invented final lines."""
from pathlib import Path
import hashlib, json
p = Path(__file__).resolve().parents[1]
for name, digest in json.loads((p/'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((p/'source'/name).read_bytes()).hexdigest() == digest
count = 0
for raw in (p/'work/confirmed-prefix.txt').read_text().splitlines():
    out = []
    lo, hi = 0, len(raw)-1
    while lo <= hi:
        out.append(raw[lo]); lo += 1
        if lo <= hi:
            out.append(raw[hi]); hi -= 1
    text = ''.join(out)
    assert text[::2] + text[1::2][::-1] == raw
    print(text)
    count += len(raw)
print('[final two lines unresolved]')
print(f'{count} prefix letters; source hashes and inverse-key roundtrips passed.')
