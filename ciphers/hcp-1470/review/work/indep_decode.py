#!/usr/bin/env python3
"""Reviewer's independent A1Z26 decode of hcp-1470 from the reviewer's own reading."""
import string, sys
own = "13 1 18 9 13 1 18 18 1 14 4 5 15 20"   # read by reviewer from enlarged crops
alts = {10: [4, 7]}                              # 0-based index 10 = position 11
nums = [int(x) for x in own.split()]
A = string.ascii_uppercase
print(len(nums), "numbers, range", min(nums), max(nums))
print("own reading :", "".join(A[n-1] for n in nums))
for i, vs in alts.items():
    for v in vs:
        t = nums[:]; t[i] = v
        print(f"pos {i+1}={v:>2}:", "".join(A[n-1] for n in t))
sol = open(sys.argv[1]).read().split()
sol = [l for l in open(sys.argv[1]).read().splitlines() if l.strip() and not l.startswith('#')][0]
print("solver transcription identical:", [int(x) for x in sol.split('-')] == nums)
