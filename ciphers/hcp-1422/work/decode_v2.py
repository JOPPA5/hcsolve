#!/usr/bin/env python3
"""HCP 1422: decode the frozen manual glyph transcript (work/transcript_v2.txt)
with the substitution key (work/key.json). Checks source hashes first.
Tokens in [brackets] are restorations of glyphs hidden by the postal
cancellation; they are printed in [brackets] in the plaintext."""
import hashlib, json
from pathlib import Path
r = Path(__file__).resolve().parents[1]
for name, h in json.loads((r/'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((r/'source'/name).read_bytes()).hexdigest() == h, name
key = json.loads((r/'work/key.json').read_text())
assert len(set(key.values())) == len(key)
punct = {'{question}': '?', '{punct}': '/', '{comma}': ',', '{stop}': '.'}
read = restored = 0
for line in (r/'work/transcript_v2.txt').read_text().splitlines():
    words = []
    for word in line.strip().split(' / '):
        out = ''
        for t in word.split():
            if t in punct:
                out += punct[t]
            elif t.startswith('[') and t.endswith(']'):
                out += '[' + key[t[1:-1]] + ']'; restored += 1
            else:
                out += key[t]; read += 1
        words.append(out)
    print(' '.join(words))
print(f'# {read} glyphs read from the scan, {restored} restored under the postmark; {len(key)} key classes; source hashes OK')
