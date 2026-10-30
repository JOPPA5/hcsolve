#!/usr/bin/env python3
"""Three manually read excerpts only; not a full-message decipherment."""
from pathlib import Path
import hashlib, json
p = Path(__file__).resolve().parents[1]
for name, digest in json.loads((p/'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((p/'source'/name).read_bytes()).hexdigest() == digest
count = 0
for raw in (p/'work/confirmed-excerpts.txt').read_text().splitlines():
    out = []
    lo,hi = 0,len(raw)-1
    while lo <= hi:
        out.append(raw[lo]);lo += 1
        if lo <= hi:
            out.append(raw[hi]);hi -= 1
    text = ''.join(out)
    assert text[::2]+text[1::2][::-1] == raw
    print(text)
    count += len(raw)
print(f'{count} letters across 3 separate excerpts; not continuous plaintext.')
print('Source hashes and excerpt roundtrips passed, not OCR/pixel proof.')
