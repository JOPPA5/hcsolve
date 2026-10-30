#!/usr/bin/env python3
"""HCP 1460: full decode. Each written line is read first, last, second,
second-to-last, ... (restarting on every line). Verifies source hashes and
the inverse (encryption) roundtrip. No letters are added or reordered; the
editorial reading is printed separately and labelled as such."""
from pathlib import Path
import hashlib, json
p = Path(__file__).resolve().parents[1]
for name, digest in json.loads((p/'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((p/'source'/name).read_bytes()).hexdigest() == digest, name
def dec(raw):
    out, lo, hi = [], 0, len(raw)-1
    while lo <= hi:
        out.append(raw[lo]); lo += 1
        if lo <= hi:
            out.append(raw[hi]); hi -= 1
    return ''.join(out)
def enc(pt):
    return pt[::2] + pt[1::2][::-1]
lines = (p/'work/transcription.txt').read_text().split()
n = 0
for raw in lines:
    t = dec(raw); assert enc(t) == raw
    print(f'{raw:20s} -> {t}'); n += len(raw)
assert sorted(lines[4]) == sorted('askedmetgiveyou')
print(f'{len(lines)} lines, {n} letters; source hashes and roundtrips OK.')
print('Editorial reading (slip in the asked-me line, see SOLUTION.md):')
print('Dear Sadie, Father was delighted with the Concert last night and has '
      'asked me t[o] give you his congratulations. Ys H.A.r')
