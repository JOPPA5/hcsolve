#!/usr/bin/env python3
"""Reviewer's independent A1Z26 decoder (does not import solver code)."""
import sys
from collections import Counter
rows = [l.split() for l in open(sys.argv[1]) if l.strip() and not l.startswith("#")]
nums = [int(x) for r in rows for x in r]
assert all(1 <= n <= 26 for n in nums)
for r in rows:
    print(" ".join(r).ljust(48), "".join(chr(64 + int(x)) for x in r))
print("numbers:", len(nums), "letters used:", "".join(sorted({chr(64+n) for n in nums})))
