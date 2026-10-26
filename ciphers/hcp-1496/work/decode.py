#!/usr/bin/env python3
from pathlib import Path
import hashlib,json
p=Path(__file__).resolve().parents[1]
key={n:chr(64+n) for n in range(1,27)}
for name,h in json.loads((p/"work/source-sha256.json").read_text()).items():
    assert hashlib.sha256((p/"source"/name).read_bytes()).hexdigest()==h
nums=[int(t) for t in (p/"work/transcription.txt").read_text().split()]
plain="".join(key[n] for n in nums)
assert [ord(c)-64 for c in plain]==nums
words=(p/"work/words.txt").read_text().split()
assert "".join(words)==plain,"Spacing must preserve every decoded letter in order"
print(" ".join(words))
print("Encrypted numeric positions:",len(nums))
print("Source hashes, inverse-key roundtrip, and ordered-letter spacing passed.")
